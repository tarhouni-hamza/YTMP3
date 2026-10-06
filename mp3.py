import yt_dlp


def download_mp3(url,output_folder="downloads"):
    
    options={
        
        "format" : "bestaudio/best",
        "outtmpl": f"{output_folder}/%(title)S,%(ext)s",
        "postprocessors": [{
            "key" : "FFmpegExtractAudio",
            "preferredcodec":"mp3",
            "preferredquality": "192",
        }],
    }
    
    with yt_dlp.YoutubeDL(options)as ydl:
        ydl.download([url])
        
        
url = input("get it from Youtube maaaaaaaan : ")
download_mp3(url)

print('Done check the downloads folder,hehehehehe!')

# Copyright (c) 2026 Hamza. All rights reserved.
# This code may not be copied, modified, or distributed without permission.