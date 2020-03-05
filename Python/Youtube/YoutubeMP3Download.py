from __future__ import unicode_literals
import youtube_dl


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

if __name__ == "__main__":
    link = input()
    print("Enter the link to the video, whose audio you want to download")
    youtube_dl.YoutubeDL(ydl_opts).download(link)