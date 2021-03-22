# C:\\Program Files\\Programme\\Python
import os

# 搜索路径
path = 'C:\\Program Files\\Programme\\Python'
# 搜索文件名
file = 'pycore_accu.h'

flag = 0
os.chdir(path)


# method 1
def search_file(file):
    global flag
    if os.path.isfile(file):
        print(os.path.abspath(file))   #print(os.getcwd() + '\\' + file)
        flag = 1
        return 1
    else:
        for item in os.listdir():
            if os.path.isdir(item):
                os.chdir(item)
                search_file(file)
                if flag == 1:
                    return 1
                os.chdir('..')
    return 0


if search_file(file):
    print("成功搜索到文件！")
else:
    print("未搜索到文件！")


"""
# method 2
def search_file(file):
    global flag
    for item in os.listdir():
        if os.path.isdir(item):
            os.chdir(item)
            search_file(file)
            if flag == 1:
                return 1
            os.chdir('..')
        else:
            if item == file:
                print(os.path.abspath(file))
                flag = 1
                return 1
        '''
        if os.path.isfile(item) and (item == file):
            print(os.path.abspath(file))
            flag = 1
            return 1
        elif os.path.isdir(item):
            os.chdir(item)
            search_file(file)
            if flag == 1:
                return 1
            os.chdir('..')
        '''
if search_file(file):
    print("成功搜索到文件！")
else:
    print("未搜索到文件！")
"""


"""
# 错误实例
def search_file(file):
    if os.path.exists(file):
        print(os.getcwd() + '\\' + file)
        return 0
    else:
        for dir in os.listdir():
            if os.path.isdir(dir):
                os.chdir(dir)
                search_file(file)   # 进入子目录后未返回到父目录，导致后续搜索路径错误
"""
