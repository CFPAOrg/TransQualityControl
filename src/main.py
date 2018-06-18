#!/usr/bin/python3
import src.branch_error_check.branch_main
import src.duplicate_key_check.duplicate_main
import src.format_char_check.format_main

if __name__ == '__main__':
    branch_json = src.branch_error_check.branch_main.branch_check('./project/assets')
    duplicate_json = src.duplicate_key_check.duplicate_main.duplicate_main('./project/assets')
    format_json = src.format_char_check.format_main.format_main('./project/assets')

    print(branch_json)
    print(duplicate_json)
    print(format_json)
