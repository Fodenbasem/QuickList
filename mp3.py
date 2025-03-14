

import yt_dlp
import os
import tkinter as tk
from tkinter import messagebox, filedialog

class Downloader:
    def __init__(self):
        pass

    def validate_url(self, url):
        
        return url.startswith("http") and "playlist" in url

    def download_playlist(self, playlist_url, output_folder):
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

    def download(self, playlist_url, output_folder):
        if self.validate_url(playlist_url):
            self.download_playlist(playlist_url, output_folder)
            return True
        return False

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Playlist Downloader")
        self.root.geometry("500x300")

        self.downloader = Downloader()

        self.title_label = tk.Label(root, text="Playlist Downloader", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        self.url_label = tk.Label(root, text="Playlist URL:")
        self.url_label.pack()

        self.url_entry = tk.Entry(root, width=50)
        self.url_entry.pack()

        self.folder_label = tk.Label(root, text="Output Folder:")
        self.folder_label.pack()

        self.folder_entry = tk.Entry(root, width=50)
        self.folder_entry.pack()

        self.browse_button = tk.Button(root, text="Browse", command=self.browse_folder)
        self.browse_button.pack(pady=5)

        self.download_button = tk.Button(root, text="Download", command=self.download)
        self.download_button.pack(pady=10)

        self.status_label = tk.Label(root, text="", fg="green")
        self.status_label.pack(pady=5)

        self.footer_label = tk.Label(root, text="Made by Fady Basem", font=("Helvetica", 10))
        self.footer_label.pack(side="bottom", pady=10)

    def browse_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.folder_entry.delete(0, tk.END)
            self.folder_entry.insert(0, folder_selected)

    def download(self):
        playlist_url = self.url_entry.get().strip()
        output_folder = self.folder_entry.get().strip()

        if not playlist_url or not output_folder:
            messagebox.showerror("Error", "Please enter both the playlist URL and output folder.")
            return

        self.status_label.config(text="Downloading...", fg="blue")
        self.root.update_idletasks()

        if self.downloader.download(playlist_url, output_folder):
            self.status_label.config(text="Download completed successfully!", fg="green")
            messagebox.showinfo("Success", "Download completed successfully!")
        else:
            self.status_label.config(text="Invalid playlist URL.", fg="red")
            messagebox.showerror("Error", "Invalid playlist URL.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
