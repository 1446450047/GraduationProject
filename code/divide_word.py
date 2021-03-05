with open('./translate_text/translate.txt',encoding="utf-8") as lines:  #一次性读入txt文件，并把内容放在变量lines中
    array = lines.read()  #返回的是一个列表，该列表每一个元素是txt文件的每一行
    print(array)