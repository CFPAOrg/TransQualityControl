import json
import os


def finder(path, dir_list):
    if not os.path.exists(path):
        return
    list_name = os.listdir(path)
    for name in list_name:
        abs_path = os.path.join(path, name)
        if os.path.isfile(abs_path):
            dir_list.append(abs_path)
        if os.path.isdir(abs_path):
            finder(abs_path, dir_list)

def dir_main(path):
    _list = []
    list_out = []

    finder(path, _list)
    for i in _list:
        if 'zh_cn.lang' not in i and 'en_us.lang' not in i and 'zh_cn_old.lang' not in i and '.md' not in i and '.png' not in i and '.txt' not in i and '.json' not in i and '.mcmeta' not in i and '.bin' not in i:
            list_out.append(i)

    return json.dumps(list_out, ensure_ascii=False)

if __name__ == '__main__':
    _list = []
    list_out = []

    finder('../project', _list)
    for i in _list:
        if 'zh_cn.lang' not in i and 'en_us.lang' not in i and 'zh_cn_old.lang' not in i and '.md' not in i and '.png' not in i and '.txt' not in i and '.json' not in i and '.mcmeta' not in i and '.bin' not in i:
            list_out.append(i)

    print(json.dumps(list_out, ensure_ascii=False))
