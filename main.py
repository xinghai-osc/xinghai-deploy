import sys
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from threading import Thread
import asyncio
from . import core

main = tk.Tk()
main.title("星海部署-XinghaiDeploy")
main.geometry("550x350")  # 增加高度以容纳进度条
main.resizable(0, 0)  # 防止用户调整尺寸

# main.iconphoto(False, tk.PhotoImage(file='./asstes/logo.png'))
# 上面那行设置图标的，不知道为什么打包后找不到文件。

def start_deploy():
    text = txt.get()
    if not text:
        small_text.configure(text="请输入地址！")
        return
    small_text.configure(text="正在部署中...")
    progress_bar.start()  # 开始进度条动画
    thread = Thread(target=run_deploy, args=(text,))
    thread.start()

def run_deploy(text):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(core.deploy(text))
    loop.close()
    main.after(0, finish_deploy)

def finish_deploy():
    small_text.configure(text="部署完成！")
    progress_bar.stop()  # 停止进度条动画

# 使用相对单位调整字体大小
lbl = tk.Label(main, text="星海部署", font=("Smiley Sans Oblique", 45))
lbl.place(relx=0.5, rely=0.2, anchor=tk.CENTER)  # 使用place并居中

small_text = tk.Label(main, text="请输入您的部署服务器", font=("Smiley Sans Oblique", 20))
small_text.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # 同样居中放置

txt = tk.Entry(main, width=50)
txt.place(relx=0.5, rely=0.7, anchor=tk.CENTER)  # 输入框居中

btn = tk.Button(main, text="开始部署", command=start_deploy)
btn.place(relx=0.5, rely=0.85, anchor=tk.CENTER)  # 按钮居中

progress_bar = ttk.Progressbar(main, orient='horizontal', mode='indeterminate', length=300)
progress_bar.place(relx=0.5, rely=0.95, anchor=tk.CENTER)  # 进度条居中

if __name__ == "__main__":
    if len(sys.argv) < 2:
        main.mainloop()
    else:
        start_deploy()