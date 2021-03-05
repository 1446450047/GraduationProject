from aip import AipSpeech
import os

# 百度云账户的密钥
APP_ID = '23146498'
API_KEY = 'toczH3dDPXgpXHYeRZhrkAFy'
SECRET_KEY = 'eVyYTzWy8w6f5t1RbA1yyvPIaWD8eRHG'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 逐个翻译，保存到文件里

def translate_to_text(path):
    result = client.asr(get_file_content(path), 'wav', 16000, {
        'dev_pid': 1537,
    })
    return result



