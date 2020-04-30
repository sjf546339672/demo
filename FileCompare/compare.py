# coding: utf-8

import hashlib


def getmd5(file):
    m = hashlib.md5()
    with open(file, 'rb') as f:
        for line in f:
            m.update(line)
    md5code = m.hexdigest()
    return md5code


def read_lines(file_path):
    context_list = []
    with open(file_path, 'rb') as fp:
        for fp in fp.readlines():
            context_list.append(fp.decode('utf-8'))
    return context_list


def file_legth(file_list1, file_list2):
    if len(file_list1) > len(file_list2):
        length = len(file_list2)
    else:
        length = len(file_list1)
    return length


def Compare_file(file1, file2):
    file1_md5_code = getmd5(file1)
    file2_md5_code = getmd5(file2)

    if file1_md5_code != file2_md5_code:
        with open(file1, 'r', encoding='utf-8') as f1:
            lines = f1.readlines()
            for line in lines:
                print(line)


Compare_file('file1.py', 'file2.py')