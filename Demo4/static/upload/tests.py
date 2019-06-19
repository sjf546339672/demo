#-*- coding:UTF-8 -*-
'''
从命令行获取一个参数，该参数表示【待读取文件的完整路径】
要求：开始运行后，如果文件有新的内容行，检测内容行中如果带有
【quit】(无论大小写)则将其输出并退出程序运行，否则原样输出即可。
'''
import sys

def thief2(filename):
    file2 = open(filename,'r')
    while True:
        mystr = file2.readline() #每次读取一行内容
        mystr1 = mystr.strip().lower()
        p = 'quit'
        if not mystr1:
            continue
        if p in mystr1:
            print('检测到quit,退出运行')
            sys.exit(0)
        yield mystr1


def main(to_read_file):
    t = thief2(to_read_file)
    for i in t:
        print(i)

if __name__ == '__main__':
    '''
    print sys.argv
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        main(filename)
    else:
        print('Please special filename')
    '''
    main('file1.txt')
















