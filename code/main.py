import os
from code.split_voice import split_voice
from code.change_frequency import change_frequency
from code.voice_to_text import translate_to_text

if __name__ == '__main__':
    # 分割音频为十秒，单声道
    split_voice("../resources/voices/shortVoice.aac",10,"./split_voice/")

    # 改为 16k
    change_frequency(".\\split_voice")

    # 逐个文件转为文字，保存到translate.txt里面去
    for filename in os.listdir("finally_voice"):
        result = translate_to_text("./finally_voice/" + filename)
        print(result)
        path = "translate_text"
        if os._exists(path + "\\translate.txt"):
            os.remove(path + "\\translate.txt")
        with open(path + "\\translate.txt" , "a", encoding="utf-8") as f:
            f.write(result['result'][0] if result.get('result') is not None else "")


