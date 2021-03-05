def read_txt(path):
    """
    :param path: 读取txt文件的路径
    :return: 返回一个list，每个元素为文件每行的内容
    """
    txt_list = []
    # 一次性读入txt文件，并把内容放在变量f中
    with open(path,encoding="utf-8") as f:
        # 将每一行除去空白字符，然后追加到txt_list 里面
        for line in f.readlines():
            txt_list.append(line.strip())

    return txt_list
