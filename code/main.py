from aip import AipSpeech

# 百度云账户的密钥
APP_ID = '23146498'
API_KEY = 'toczH3dDPXgpXHYeRZhrkAFy'
SECRET_KEY = 'eVyYTzWy8w6f5t1RbA1yyvPIaWD8eRHG'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别本地文件
from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_file("../resources/voices/testVoice.aac", format="aac")

ten_seconds = 10 * 1000

first_10_seconds = song[:ten_seconds]

# result = client.asr(get_file_content('../resources/voices/shortVoice.aac'), 'm4a', 16000, {
#     'dev_pid': 1537,
# })
result = client.asr(first_10_seconds, 'm4a', 16000, {
    'dev_pid': 1537,
})

print(result)



