# 导入所需的库
import sys
from tkinter import *
import requests
import json
import os

# 定义部署应用程序的函数
async def deploy(text):
    # 发送GET请求获取响应
    response = requests.get(text)
    app_list = json.loads(response.text)
    id=0
    while len(app_list)!=id:  # 使用len函数防止死循环。
        # 下载安装程序
        print(f"正在下载 {app_list[id]['name']}...")
        installer = requests.get(app_list[id]['url'])
        try:
            argument=app_list[id]['argument']
        except Exception:
            argument=""
        file_path = os.getcwd()+R"\xinghai\deploy\installer_"+app_list[id]['name']+"_installer.exe"
         # 创建临时文件并写入安装程序内容
        os.makedirs(os.getcwd()+"\\xinghai\\deploy", exist_ok=True)
        with open(file_path, 'wb') as f:
            f.write(installer.content)
            print(f"{app_list[id]['name']} 的临时文件路径: {file_path}")
            # 在命令行中启动安装程序
            f.close()
            if sys.platform.startwith('linux'):
                os.system('./'+file_path+" "+argument)
            elif sys.platform.startwith('win'):
                os.system('start '+file_path+" "+argument)  # 使用文件名启动，避免路径问题
            else:
                print("不支持的操作系统")
        id=id+1
    exit(0)