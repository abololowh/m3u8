import yt_dlp
from reader import *
import requests

def get_m3u8_url():  
    url = 'https://www.youtube.com/@neda_radio/live'  
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info_dict = ydl.extract_info(url, download=False)
            formats = info_dict.get('formats', [])
            for format in formats:
                    return format['manifest_url']      #['url']
            return None
        except Exception as e:
            print("An error occurred during the download:")
            print(str(e))

 get_m3u8_url()
