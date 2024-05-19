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

def get_value_from_url(url):
    try:
        # إرسال طلب GET لفتح الرابط
        response = requests.get(url)
        
        # التأكد من نجاح الطلب
        if response.status_code == 200:
            # إرجاع المحتوى المسترجع
            return response.text
        else:
            print("Failed to retrieve content. Status code:", response.status_code)
            return None
    except Exception as e:
        print("An error occurred:", e)
        return None

# تحديد الرابط الذي تريد فتحه
url = get_m3u8_url()
# استخدام الدالة لفتح الرابط واسترداد المحتوى
content = get_value_from_url(url)
if content:
    print("Content retrieved successfully:")
    print(content)
else:
    print("Failed to retrieve content from the URL.")
