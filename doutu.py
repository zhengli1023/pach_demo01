import requests
import re
import pymysql

db = pymysql.connect(host = 'localhost',port = 3306,user = 'root',
                     passwd = 'qqzheng1023',db = 'pch_demo',charset = 'utf8'
                    )
# 创建游标 进行数据库操作
cursor = db.cursor()
def get_image_list(page):
    # 获取图片列表的方法
    html = requests.get('http://www.doutula.com/photo/list/?page={}'.format(page)).text
    # 正则表达式 通配符 匹配所有
    reg = r'data-original="(.*?)".*?alt="(.*?)"'
    # 增加匹配效率 S 多行匹配
    reg = re.compile(reg,re.S)
    image_list = re.findall(reg,html)
    for i in image_list:
        image_url = i[0]
        image_title = i[1]
        cursor.execute("insert into tb_image(`ititle`,`iur`) values('{}','{}')"
                       .format(image_title,image_url))
        print('正在保存 %s'%image_title)
        db.commit()
# 写到for 循环中获取多页页码
for i in range(1,5):
    print('当前爬取第{}页'.format(i))
    get_image_list(i)

