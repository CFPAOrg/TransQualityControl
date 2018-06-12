import os
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


def main_check(zh_dict, modid):
    list_out = []
    for k in zh_dict.keys():
        if '=' in zh_dict[k] and '.' in zh_dict[k]:
            list_out.append({'modid': modid, 'key': k, 'zh_cn': zh_dict[k]})
    return list_out


if __name__ == '__main__':
    list_total = []

    for modid in file_finder('./project/assets'):
        zh_dict = lang_to_dict('./project/assets/{}/lang/zh_cn.lang'.format(modid))
        list_total.extend(main_check(zh_dict, modid))

    print(json.dumps(list_total, ensure_ascii=False))
