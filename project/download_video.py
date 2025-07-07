import yt_dlp
import whisper

model = whisper.load_model("base")
url = "https://www.youtube.com/watch?v=J1f47XwvQYA"


def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
        'outtmpl': 'downloaded_audio',  # Saves to downloaded_audio.wav
        'quiet': True,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])  # Saves to downloaded_audio.wav


def transcribe_audio(file_path):
    model = whisper.load_model("base")
    result = model.transcribe(file_path)
    return result["text"]


def download_video(url):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
        'merge_output_format': 'mp4',
        'outtmpl': 'downloaded_video',  # Saves as downloaded_video.mp4
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def get_video_chapters(url):
    with yt_dlp.YoutubeDL({}) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        chapters = info_dict.get("chapters", [])
        return chapters


def download_video_chapters(url):
    ydl_opts = {
        'format': 'bv+ba/b',
        # 'merge_output_format': 'mp4',
        'outtmpl': '%(chapter_number)02d - %(chapter)s.%(ext)s',  # saves clips by chapter
        'split_chapters': True,  # 🔥 this is the key!
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])



if __name__ == "__main__":
    # download_video(url)
    # download_audio(url)
    # download_video_chapters(url)
    print(get_video_chapters(url))

