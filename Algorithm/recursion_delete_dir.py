# 递归删除目录及目录下的文件

import os


def remove_dir(dir_name):
    if os.path.exists(dir_name):
        os.chdir(dir_name)
    else:
        return
    for i in os.listdir():
        if os.path.isfile(i):
            os.remove(i)
        else:
            remove_dir(i)
    os.chdir('..')
    os.removedirs(dir_name)


# 引用方式一：dir_name为目录所在路径
remove_dir('D:\\test\\1')

# 引用方式而：进入目录所在父目录下，dir_name为目录名
os.chdir('D:\\test')
remove_dir('1')

