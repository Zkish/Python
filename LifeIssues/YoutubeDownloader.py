from pytube import YouTube

def download_youtube_video(url, output_path):
    try:
        # Download the YouTube video
        youtube = YouTube(url)
        video_stream = youtube.streams.get_highest_resolution()
        video_stream.download(output_path)

        print(f"Downloaded {youtube.title} successfully!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    output_folder = input("Enter the output folder path: ")

    download_youtube_video(video_url, output_folder)