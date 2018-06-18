# 这次学习了 python3 的面向对象，尝试下
# 所以内容可能反而有点繁琐
import re
import os
import json


class FileReader:
    def __init__(self):
        pass;

    # 获取语言文件，处理得到一个 dict
    def lang_to_dict(self, file_path):
        lang_dict = {}
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f.readlines():
                if line is not None and line[0] != '#' and '=' in line:
                    line_list = line.split('=', 1)
                    lang_dict[line_list[0]] = line_list[1].rstrip('\n')
        return lang_dict


class FormatCheck:
    def __init__(self):
        pass;

    def format_check(self, en_dict, zh_dict, modid):
        list_out = []
        for k in en_dict.keys():
            if k in zh_dict and '%' in en_dict[k]:
                """
                Java 字符串格式化
                %[argumnet_index$][flags][width][.precision]conversion
                argumnet_index$：表示该 conversion 在后面参数列表中的位置，为一个从 1 开始的十进制数，如 2$；
                flags：修改输出格式的字符集；
                width：输出最小宽度；
                .precision：Sting表示输出字符的最大数量，浮点数表示小数位（不足补0）；
                conversion：参数，一般有 d，c，b，s，f，e，x，h；
                考虑到语言文件中从没有用 flags 参数的，略去不写。
              """
                format_regex = re.compile('%([1-9]+\$)?(\\d)*(\.(\\d)+)?[dcbsfexh]')
                if len(format_regex.findall(en_dict[k])) != len(format_regex.findall(zh_dict[k])):
                    list_out.append({'modid': modid, 'key': k, 'en_us': en_dict[k], 'zh_cn': zh_dict[k]})
        return list_out


class FileFinder:
    def __init__(self):
        pass;

    def file_finder(self, assets_path):
        check_file = []
        for modid in os.listdir(assets_path):
            if os.path.isfile('{}/{}/lang/en_us.lang'.format(assets_path, modid)) and os.path.isfile(
                    '{}/{}/lang/zh_cn.lang'.format(assets_path, modid)):
                check_file.append(modid)
        return check_file


def format_main(path):
    file_reader = FileReader()
    format_check = FormatCheck()
    file_finder = FileFinder()

    list_total = []

    for modid in file_finder.file_finder(path):
        en_dict = file_reader.lang_to_dict('{}/{}/lang/en_us.lang'.format(path, modid))
        zh_dict = file_reader.lang_to_dict('{}/{}/lang/zh_cn.lang'.format(path, modid))
        list_total.extend(format_check.format_check(en_dict, zh_dict, modid))

    return json.dumps(list_total, ensure_ascii=False)


if __name__ == '__main__':
    file_reader = FileReader()
    format_check = FormatCheck()
    file_finder = FileFinder()

    list_total = []

    for modid in file_finder.file_finder('../project/assets'):
        en_dict = file_reader.lang_to_dict('../project/assets/{}/lang/en_us.lang'.format(modid))
        zh_dict = file_reader.lang_to_dict('../project/assets/{}/lang/zh_cn.lang'.format(modid))
        list_total.extend(format_check.format_check(en_dict, zh_dict, modid))

    print(list_total)
