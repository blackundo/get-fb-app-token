import os
import time

import requests
from playsound import playsound

print('đang chạy')
while True:
    try:
        url = "https://spin.modundo.com/ajaxs/admin/bank-speech.php"
        response = requests.request("GET", url)
        data = response.json()
        if data["status"] == "error":
            # print(data['status'])
            time.sleep(15)
        else:
            datavip = data['data']
            for i in datavip:

                text = f"{i['user_name']} {i['text']}"
                audio_data = requests.get(f'https://proxy.junookyo.workers.dev/?language=vi-VN&text={text}').content
                with open('temp.mp3', 'wb') as f:
                    f.write(audio_data)
                playsound('temp.mp3', block=True) # block là khi phát hết âm thanh mới chạy tiếp theo thì không cần sleep nữa
                if os.path.exists('temp.mp3'):
                    os.remove('temp.mp3')
                # time.sleep(3)
    except Exception:
        pass
    except requests.exceptions.SSLError:
        pass