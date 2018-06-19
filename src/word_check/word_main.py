import json
import os


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


def open_check_file(path):
    word_list = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f.readlines():
            word_list.append(line.rstrip('\n'))
    return word_list


def word_check(path, file_path):
    list_word = open_check_file(file_path)
    list_out = []

    modid_en_dict = {}
    modid_zh_dict = {}
    for modid in file_finder(path):
        en_dict = lang_to_dict('{}/{}/lang/en_us.lang'.format(path, modid))
        zh_dict = lang_to_dict('{}/{}/lang/zh_cn.lang'.format(path, modid))
        modid_en_dict[modid] = en_dict
        modid_zh_dict[modid] = zh_dict

    for word in list_word:
        item_list = []
        for modid in modid_zh_dict.keys():
            zh_dict_in = modid_zh_dict[modid]
            en_dict_in = modid_en_dict[modid]
            for key in zh_dict_in.keys():
                if word in zh_dict_in[key] and key in en_dict_in.keys():
                    item_list.append({"mod": modid, "en_us": en_dict_in[key], "zh_cn": zh_dict_in[key]})
        list_out.append({"word": word, "items": item_list})

    return json.dumps(list_out, ensure_ascii=False)


if __name__ == '__main__':
    path = '../project/assets'
    list_word = open_check_file("../../check_words.txt")
    list_out = []

    en_dict = {}
    zh_dict = {}
    modid_en_dict = {}
    modid_zh_dict = {}
    for modid in file_finder(path):
        en_dict = lang_to_dict('{}/{}/lang/en_us.lang'.format(path, modid))
        zh_dict = lang_to_dict('{}/{}/lang/zh_cn.lang'.format(path, modid))
        modid_en_dict[modid] = en_dict
        modid_zh_dict[modid] = zh_dict

    for word in list_word:
        item_list = []
        for modid in modid_zh_dict.keys():
            zh_dict_in = modid_zh_dict[modid]
            en_dict_in = modid_en_dict[modid]
            for key in zh_dict_in.keys():
                if word in zh_dict_in[key] and key in en_dict_in.keys():
                    item_list.append({"mod": modid, "en_us": en_dict_in[key], "zh_cn": zh_dict_in[key]})
        if word == "苦力怕":
            print("爬行者为 ：" + str(len(item_list)))
        elif word == "爬行者":
            print("苦力怕为 ：" + str(len(item_list)))

        list_out.append({"word": word, "items": item_list})

    # print(json.dumps(list_out, ensure_ascii=False))
