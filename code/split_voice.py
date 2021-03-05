from pydub import AudioSegment
import os

def split_voice(voice_path:str,split_seconds:int ,save_path: str) -> None:
    """
    :param voice_path: 传入的音频资源路径
    :param split_seconds: 分割秒数（最大为60s）
    :param save_path: 保存路径
    :return: void
    """
    # 删除split_voice中的所有文件
    path = "split_voice"
    for filename in os.listdir(path):
        os.remove(path + "\\" + filename)

    # 获取音频的格式
    file_format = os.path.splitext(voice_path)[-1][1:]

    # 读取音频文件
    song = AudioSegment.from_file(voice_path,format = file_format)

    # 获取音频的长度
    song_len = int(song.duration_seconds)

    # 起使截取时间
    start = 0

    # 处理每次截取时间，最大为60s
    split_seconds = split_seconds * 1000 if split_seconds <= 60 else 60 * 1000

    # 终止截取时间
    end = split_seconds

    while end < song_len * 1000:
        # 截取60秒然后保存成为 .wav格式的文件(方便调用API处理)
        sixty_seconds_voice = song[start:end]

        # 保存为单声道模式
        sixty_seconds_voice = sixty_seconds_voice.set_channels(1)

        sixty_seconds_voice.export(
            save_path + str(int(start / 1000)) + "_to_" + str(int(end / 1000)) + "_voice.wav", format="wav")
        start = end
        end = start + split_seconds

    # 截取最后的音频
    if end >= song_len * 1000:
        sixty_seconds_voice = song[start : song_len*1000]
        sixty_seconds_voice = sixty_seconds_voice.set_channels(1)
        sixty_seconds_voice.export(
            save_path + str(int(start / 1000)) + "_to_" + str(int(song_len)) + "_voice.wav", format="wav")
