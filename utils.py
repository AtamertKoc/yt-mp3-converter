from pytubefix import YouTube
import os

def video_downloader(url, target_folder="/home/thinkpad/Masaüstü/deneme-proje"):
    try:
        yt = YouTube(url)
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
        
        folder_path = video.download(output_path=target_folder)
        return folder_path, yt.title
    except Exception as t:
        return None, str(t)

def mp3_converter(video_path):
    base, ext = os.path.splitext(video_path)
    new_folder = base + '.mp3'
    os.rename(video_path, new_folder)
    return new_folder