# 这次不折腾啥面向对象了
# 简单好用直接上函数式
import os
from collections import Counter
import json


# 获取语言文件，处理得到一个 dict
def lang_to_dict(file_path):
    lang_dict = {}
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f.readlines():
            if line is not None and line[0] != '#' and line[0] != '/' and '=' in line:
                line_list = line.split('=', 1)
                lang_dict[line_list[0]] = line_list[1].rstrip('\n')
    return lang_dict


def file_finder(assets_path):
    check_file = []
    for modid in os.listdir(assets_path):
        if os.path.isfile('{}/{}/lang/en_us.lang'.format(assets_path, modid)) and os.path.isfile(
                '{}/{}/lang/zh_cn.lang'.format(assets_path, modid)):
            check_file.append(modid)
    return check_file


if __name__ == '__main__':
    key_total = []  # 存储所有语言文件 key
    en_dict_total = {}  # 存储所有的英文语言文件键值对
    zh_dict_total = {}  # 存储所有的中文语言文件键值对

    key_duplicate = []  # 存储重复的语言文件 key
    dict_total = {}  # 最后的输出列表

    for modid in file_finder('../project/assets'):
        en_dict = lang_to_dict('../project/assets/{}/lang/en_us.lang'.format(modid))
        zh_dict = lang_to_dict('../project/assets/{}/lang/zh_cn.lang'.format(modid))

        en_dict_total[modid] = en_dict
        zh_dict_total[modid] = zh_dict
        key_total.extend(list(en_dict.keys()))

    _dict = Counter(key_total)
    for _key in _dict:
        if _dict[_key] > 1:
            key_duplicate.append(_key)

    for i in key_duplicate:
        dict_one = {}
        list_en = []
        list_zh = []

        for j in en_dict_total.keys():
            if i in en_dict_total[j].keys() and i in zh_dict_total[j].keys():
                dict_one[j] = {en_dict_total[j][i]: zh_dict_total[j][i]}
                list_en.append(en_dict_total[j][i])
                list_zh.append(zh_dict_total[j][i])

        if len(dict_one) > 1:
            if len(set(list_en)) > 1 or len(set(list_zh)) > 1:
                dict_total[i] = dict_one

    print(json.dumps(dict_total, ensure_ascii=False))
    print(len(dict_total))
