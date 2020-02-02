import os
import random

from flask import current_app
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

from slicer.download_helpers import download_youtube, download_ooyala
from slicer.storage_backends import get_s3_upload_url


class Slicer:

    def __init__(self, source, video_id, start, end):
        self.video_id = video_id
        self.start = start
        self.end = end
        self.source = source

    def get_clip(self, file_name):

        if self.source == 'youtube':
            return download_youtube(self.video_id, file_name)

        if self.source == 'ooyala':
            return download_ooyala(self.video_id, file_name)

    def get_url(self):
        file_name = self.source + "_" + self.video_id + "%08x" % random.getrandbits(32) + ".mp4"
        destination = f"{current_app.config['TMP_FOLDER']}/{file_name}"
        slice_destination = f"{current_app.config['TMP_FOLDER']}/sliced_{file_name}"

        self.get_clip(file_name)
        ffmpeg_extract_subclip(destination, self.start, self.end, targetname=slice_destination)
        url = get_s3_upload_url(file_name)
        os.remove(destination)
        os.remove(slice_destination)

        return url
