import tkinter as tk
import re
import requests
import webbrowser


#爬虫爬取播放网址
html = requests.get('https://daga.cc/').text
res = re.compile(r'option value="//(.*?)">')
reg = re.findall(res,html)
list1 = [1,2,3,4,5]
for i in range(5):
    list1[i] = reg[i]

# 程序界面

root = tk.Tk() # 画板
root.title('vip电影播放') # 标题
root.geometry('350x250+100+100') # 设置界面大小和出现位置
l1 = tk.Label(root,text='播放接口：')
l1.grid(row=0,column=0) # 空间
l2 = tk.Label(root,text='播放链接：')
l2.grid(row=5,column=0) # 空间
sech_t1 = tk.Entry(root,text='',width=30) # 网址输入框
sech_t1.grid(row=5,column=1)
var = tk.StringVar()
r1 = tk.Radiobutton(root,text='播放接口1', variable=var,value=list1[0])  # 单选按钮 为按钮赋值网址
r1.grid(row=0, column=1)
r2 = tk.Radiobutton(root,text='播放接口2', variable=var,value=list1[1])
r2.grid(row=1, column=1)
r3 = tk.Radiobutton(root,text='播放接口3', variable=var,value=list1[2])
r3.grid(row=2, column=1)
r4 = tk.Radiobutton(root,text='播放接口4', variable=var,value=list1[3])
r4.grid(row=3, column=1)
r5 = tk.Radiobutton(root,text='播放接口5', variable=var,value=list1[4])
r5.grid(row=4, column=1)

#自动化测试，实现浏览器播放
def bf(): # 播放的方法
    webbrowser.open(var.get()+sech_t1.get())
b1 = tk.Button(root,text='播放',width=6,command=bf) # command 进行命令绑定
b1.grid(row=6, column=1)
def del_text(): # 清除操作
    sech_t1.delete(0,'end')
b2 = tk.Button(root,text='清除',width=6,command=del_text)
b2.grid(row=7,column=1)

root.mainloop() # 消息循环，来保持界面
