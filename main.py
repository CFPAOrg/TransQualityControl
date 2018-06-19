#!/usr/bin/python3
import src.branch_error_check.branch_main
import src.duplicate_key_check.duplicate_main
import src.format_char_check.format_main

import sys
import os

if __name__ == '__main__':
    def info_w():
        branch_json = src.branch_error_check.branch_main.branch_check(project_assets)
        duplicate_json = src.duplicate_key_check.duplicate_main.duplicate_main(project_assets)
        format_json = src.format_char_check.format_main.format_main(project_assets)

        if (os.path.exists("./branch.js") == True):
            os.remove("./branch.js")
        if (os.path.exists("./duplicate.js") == True):
            os.remove("./duplicate.js")
        if (os.path.exists("./format.js") == True):
            os.remove("./format.js")

        # 删除文件
        branch = open("./branch.js", "w", encoding="utf-8")
        duplicate = open("./duplicate.js", "w", encoding="utf-8")
        formatjson = open("./format.js", "w", encoding="utf-8")
        branch.write("export let branches=" + branch_json + ";")
        duplicate.write("export let duplicates=" + duplicate_json + ";")
        formatjson.write("export let formats=" + format_json + ";")
        branch.close()
        duplicate.close()
        formatjson.close()
        # 写json数据到文件


    def setProjectDir(dir):
        global project_dir
        global project_assets
        project_dir = dir
        project_assets = project_dir + "/assets"


    syslist = sys.argv
    mainsyslist = [["--projectDir", setProjectDir], ["-D", setProjectDir]]

    for i in range(len(syslist)):
        for ii in range(len(mainsyslist)):
            if (syslist[i] == mainsyslist[ii][0]):
                # python3 main.py --projectDir ./project
                mainsyslist[ii][1](syslist[i + 1])
                info_w()
