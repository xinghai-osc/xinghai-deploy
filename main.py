from tkinter import *
from . import core
import sys
import asyncio

main = Tk()
main.title("星海部署-XinghaiDeploy")
main.geometry("550x300")
main.resizable(0,0) #防止用户调整尺寸

# main.iconphoto(False, PhotoImage(file='./asstes/logo.png'))
# 上面那行设置图标的，不知道为什么打包后找不到文件。

async def deploy(text):
    if text == None:
        small_text.configure(text="请输入地址！")
    small_text.configure(text="正在部署中...")
    await core.deploy(text)
    small_text.configure(text="部署完成！")


# 使用相对单位调整字体大小
lbl = Label(main, text="星海部署", font=("Smiley Sans Oblique", 45))
lbl.place(relx=0.5, rely=0.3, anchor=CENTER)  # 使用place并居中

small_text = Label(main, text="请输入您的部署服务器", font=("Smiley Sans Oblique", 20))
small_text.place(relx=0.5, rely=0.5, anchor=CENTER)  # 同样居中放置

txt = Entry(main, width=50)
txt.place(relx=0.5, rely=0.7, anchor=CENTER)  # 输入框居中

btn = Button(main, text="开始部署", command=lambda:asyncio.run(deploy(txt.get())))
btn.place(relx=0.5, rely=0.9, anchor=CENTER)  # 按钮居中

if len(sys.argv) < 2:
    main.mainloop()
else:
    deploy(sys.argv[1])