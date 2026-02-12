from utils import video_downloader, mp3_converter

def start_app():
    print("---Welcome the Youtube Video Downloader and MP3 Converter---")
    url = input("Paste the Youtube URL: ")
    print("Relax, the app is working...")

    folder, title = video_downloader(url)

    if folder:
        print(f"'{title}' downloaded...")
        choice = input("If you want i can converted a video by MP3(Y/N): ")
        if choice.lower() == 'y':
            mp3_folder = mp3_converter(folder)
            print(f"Done: {mp3_folder}")
    else:
        print(f"WE HAVE PROBLEM!!! >>> {title}")
if __name__ == "__main__":
    start_app()