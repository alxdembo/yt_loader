import requests
from flask import current_app
from pytube import YouTube


def download_youtube(video_id, file_name):
    video = YouTube(current_app.config['STREAM_HOST_YOUTUBE'] + video_id)
    video.streams.first().download(output_path=current_app.config['TMP_FOLDER'], filename=file_name)


def download_ooyala(video_id, file_name):
    r = requests.get(
        f"{current_app.config['STREAM_HOST_OOYALA'] + video_id}/{current_app.config['OOYALA_TOKEN']}",
        stream=True)

    # todo stop downloading after reaching end
    with open(f"{current_app.config['TMP_FOLDER']}/{file_name}.mp4", 'wb') as f:
        for chunk in r.iter_content(256):
            f.write(chunk)
