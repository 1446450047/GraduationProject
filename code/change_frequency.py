import ffmpeg
import os

# 音频处理，设置为16k
def change_frequency(path: str = ".\\") -> None:
    # 删除split_voice中的所有文件
    for filename in os.listdir("finally_voice"):
        os.remove("finally_voice" + "\\" + filename)

    for filename in os.listdir(path):
        ffmpeg.input(path + '\\' + filename).output("./finally_voice" + "\\" + 'output' + filename , ar=16000).run()


