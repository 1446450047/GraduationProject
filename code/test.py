from pydub import AudioSegment

# 读取音频文件
song = AudioSegment.from_file("../resources/voices/testVoice.aac", format="aac")

# 获取音频的长度
song_len = int(song.duration_seconds)

# 起使截取时间
start = 0

# 终止截取时间
end = 60 * 1000

# 每次截取60秒
sixty_seconds = 60 * 1000

while end < song_len * 1000:
    # 截取60秒然后保存成为 .wav格式的文件
    sixty_seconds_voice = song[start:end]
    sixty_seconds_voice.export(str(int(start/1000)) + "_to_" + str(int(end/1000)) + "_voice.wav",format="wav")
    start = end
    end = start + sixty_seconds

# 截取最后的音频
if end > song_len * 1000:
    sixty_seconds_voice = song[start:song_len]
    sixty_seconds_voice.export(str(int(start/1000)) + "_to_" + str(int(song_len)) + "_voice.wav",format="wav")




# first_10_seconds = song[:sixty_seconds]
#
# last_5_seconds = song[-5000:]

# print(first_10_seconds.duration_seconds)

# first_10_seconds.export("first_ten_seconds.mp3", format="mp3")