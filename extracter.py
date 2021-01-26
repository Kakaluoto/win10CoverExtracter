import os
import shutil
from os import path
from PIL import Image
import time
import getpass

# 获取当前系统用户名
user_name = getpass.getuser()
# 获取文件路径，获取文件名称列表
print('搜索路径中...')
source = 'C:\\Users\\' + user_name + '\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets'
print('路径:')
print(source)
dst = os.path.join(os.getcwd(), 'backgroundImage')
shutil.copytree(source, dst)
fileList = os.listdir(dst)

for Sname in enumerate(fileList):  # 获取文件名并编号
    newName = time.strftime("%Y_%m_%d_", time.localtime()) + str(Sname[0]) + '.jpg'
    os.renames(os.path.join(dst, Sname[1]), os.path.join(dst, newName))
    f = open(os.path.join(dst, newName), 'rb')#读取用于剔除尺寸不对的
    img = Image.open(f)
    # print(img.width, img.height, img.format)
    if img.width != 1920 and img.height != 1080:
        f.close()  # 必须手动关闭文件流才能删除文件
        os.remove(os.path.join(dst, newName))

print("\n搞定了耶~！\n")
time.sleep(2)
