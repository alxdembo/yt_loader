class DownloadHelpers:
    @staticmethod
    def download_youtube(video_id):
        from pytube import YouTube
        video = YouTube(f'https://www.youtube.com/watch?v={video_id}', defer_prefetch_init=False)
        video.streams.first().download()

