# C:\\Program Files\\Programme\\Python
# 1-file 2-dir 3-file+dir
import os

path = 'D:\\test'       # 搜索路径
file = '1.txt'          # 搜索文件名
count = 0               # 结果数
search_type = 3         # 搜索类型
search_limit = 0        # 搜索次数限制
os.chdir(path)


# 单个函数
def search_file(file):
    global search_type, search_limit, count
    for item in os.listdir():
        if os.path.isdir(item):
            if item == file:
                if search_type in [2, 3]:
                    print(os.path.abspath(file))
                    count += 1
                    if search_limit:
                        return count
            os.chdir(item)
            search_file(file)
            if search_limit and count:
                return count
        else:
            if item == file:
                if search_type in [1, 3]:
                    print(os.path.abspath(file))
                    count += 1
                    if search_limit:
                        return count
    return count


if search_file(file):
    print("成功搜索到%d个结果！" % count)
else:
    print("未搜索到结果！")

"""
def search_file(file):
    global flag
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

if search_file(file):
    print("成功搜索到结果！")
else:
    print("未搜索到结果！")
"""

"""
# 多个函数方法
def search_file(file):
    pass
def search_dir(dir):
    pass
def search_item(item)
    pass

if search_type == 1:
    search_file()
elif search_type == 2:
    search_dir()
elif search_type == 3:
    search_item()
"""

