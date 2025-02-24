import os
import yt_dlp
from pydub import AudioSegment

def download_playlist(playlist_url, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ignoreerrors': True  # تخطي الأخطاء والاستمرار في التحميل
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])
    
    print("\nAll possible tracks have been downloaded and saved as MP3!")

# Playlist URL
playlist_link = input("Enter the playlist URL: ")
output_directory = "Downloaded_MP3"
download_playlist(playlist_link, output_directory)
