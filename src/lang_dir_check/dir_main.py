import os
import re


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


if __name__ == '__main__':
    _list = []
    list_out = []

    finder('project', _list)
    for i in _list:
        if '.lang' in i:
            format_regex = re.compile('project/assets/.*?/lang/(.*?)\.lang')
            list_out.extend(format_regex.findall(i))
            if len(format_regex.findall(i)) != 1:
                print(i)
            elif format_regex.findall(i)[0] == 'zh':
                print(i)

    print(set(list_out))