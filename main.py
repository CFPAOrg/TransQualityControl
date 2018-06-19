#!/usr/bin/python3
import src.branch_error_check.branch_main
import src.duplicate_key_check.duplicate_main
import src.format_char_check.format_main

import sys
import os
import time
import json

if __name__ == '__main__':
    def info_w():
        branch_json = src.branch_error_check.branch_main.branch_check(project_assets)
        duplicate_json = src.duplicate_key_check.duplicate_main.duplicate_main(project_assets)
        format_json = src.format_char_check.format_main.format_main(project_assets)
        time_json = time_gen()

        # 重写文件
        branch = open("./branch.js", "w", encoding="utf-8")
        duplicate = open("./duplicate.js", "w", encoding="utf-8")
        format = open("./format.js", "w", encoding="utf-8")
        time = open("./time.js", "w", encoding="utf-8")

        # 写 js 数据到文件
        branch.write("export let branches=" + branch_json + ";")
        duplicate.write("export let duplicates=" + duplicate_json + ";")
        format.write("export let formats=" + format_json + ";")
        time.write("export let times=" + time_json + ";")

        branch.close()
        duplicate.close()
        format.close()
        time.close()


    def setProjectDir(dir):
        global project_dir
        global project_assets
        project_dir = dir
        project_assets = project_dir + "/assets"


    def time_gen():
        dict_time = {"time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}
        return json.dumps(dict_time, ensure_ascii=False)


    syslist = sys.argv
    mainsyslist = [["--projectDir", setProjectDir], ["-D", setProjectDir]]

    for i in range(len(syslist)):
        for ii in range(len(mainsyslist)):
            if (syslist[i] == mainsyslist[ii][0]):
                # python3 main.py --projectDir ./project
                mainsyslist[ii][1](syslist[i + 1])
                info_w()
