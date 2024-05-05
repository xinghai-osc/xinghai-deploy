# 导入所需的库
from tkinter import *
import requests
import json
import os

# 定义部署应用程序的函数
def deploy(text):
    # 发送GET请求获取响应
    response = requests.get(text)
    message = json.loads(response.text)
    id=0
    while message[id]['id'] != "not":  # 假设 "not" 是结束循环的条件
        # 下载安装程序
        print(f"正在下载 {message[id]['name']}...")
        installer = requests.get(message[id]['url'])
        file_path = R"C:\xinghai\temp\d_"+message[id]['name']+"_installer.exe"
         # 创建临时文件并写入安装程序内容
        with open(file_path, 'wb') as f:
            f.write(installer.content)
            print(f"{message[id]['name']} 的临时文件路径: {file_path}")
            # 在命令行中启动安装程序
            f.close()
            os.system('start '+file_path)  # 使用文件名启动，避免路径问题
        id=id+1
    exit(0)