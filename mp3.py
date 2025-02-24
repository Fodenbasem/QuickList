import os
import yt_dlp

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
        'ignoreerrors': True 
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])
    
    print(f"\nAll possible tracks from {playlist_url} have been downloaded and saved in '{output_folder}'!")


playlists = []
while True:
    playlist_link = input("Enter the playlist URL (or 0 to start downloading): ")
    if playlist_link == "0":
        break
    folder_name = input("Enter the folder name to save this playlist: ")
    playlists.append((playlist_link, folder_name))


for link, folder in playlists:
    download_playlist(link, folder)
    
print("\nAll downloads are complete!")
