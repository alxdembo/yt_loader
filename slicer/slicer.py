import os
import random

from flask import current_app
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

from slicer.download_helpers import download_youtube, download_ooyala
from slicer.storage_backends import get_s3_upload_url


class Slicer:

    def __init__(self, source, video_id, start, end):
        self.video_id = video_id
        self.start = start
        self.end = end
        self.source = source

    def __get_clip(self, file_name):

        if self.source == 'youtube':
            return download_youtube(self.video_id, file_name)

        if self.source == 'ooyala':
            return download_ooyala(self.video_id, file_name)

    def get_url(self):
        self.__validate_timestamps()
        file_name = self.source + "_" + self.video_id + "_%08x" % random.getrandbits(32) + ".mp4"
        original_clip_path = f"{current_app.config['TMP_FOLDER']}/{file_name}"
        sliced_clip_path = f"{current_app.config['TMP_FOLDER']}/sliced_{file_name}"

        self.__get_clip(file_name)
        self.__validate_timestamp_extents(original_clip_path)

        ffmpeg_extract_subclip(original_clip_path, self.start, self.end, targetname=sliced_clip_path)
        os.remove(original_clip_path)

        url = get_s3_upload_url(file_name)
        os.remove(sliced_clip_path)

        return url

    def __validate_timestamp_extents(self, destination):
        clip = VideoFileClip(destination)
        if clip.duration < self.end:
            raise ValueError(f'End timestamp {self.end} is out of clip bounds: {clip.duration}')

    def __validate_timestamps(self):
        if self.start is None:
            raise ValueError(f'Invalid start timestamp.')

        if self.end is None:
            raise ValueError(f'Invalid end timestamp.')

        if self.start >= self.end:
            raise ValueError(f'Start timestamp {self.start} is greater or equals end timestamp {self.end}')
