import requests 
import re
import json
import time
import xlwt

#
#
#配置表格
#不需要明白是干啥的
#有下面4行代码就可以往表格写中文了
#
style=xlwt.XFStyle()
font=xlwt.Font()
font.name='SimSun'
style.font=font

#创建一个表格
w=xlwt.Workbook(encoding='utf-8')
#添加个sheet
ws=w.add_sheet('sheet 1',cell_overwrite_ok=True)
#当前写入表格到第 row行
row=1
#
#写入表格头
#
ws.write(0,0,'content')
ws.write(0,1,'userClientShow')
ws.write(0,2,'creationTime')
ws.write(0,3,'userLevelName')
ws.write(0,4,'productColor')
ws.write(0,5,'userLevelId')
ws.write(0,6,'score')
ws.write(0,7,'referenceName')
ws.write(0,8,'referenceTime')
ws.write(0,9,'isMobile')
ws.write(0,10,'nickname')

#
#接受一个json对象
#将内容写进表格
#一次一页评论
#
def write_json_to_xls(dat):
    global row
    for comment in dat['comments']:
        ws.write(row,0,comment['content'])
        ws.write(row,1,comment['userClientShow'])
        ws.write(row,2,comment['creationTime'])
        ws.write(row,3,comment['userLevelName'])
        ws.write(row,4,comment['productColor'])
        ws.write(row,5,comment['userLevelId'])
        ws.write(row,6,comment['score'])
        ws.write(row,7,comment['referenceName'])
        ws.write(row,8,comment['referenceTime'])
        ws.write(row,9,comment['isMobile'])
        ws.write(row,10,comment['nickname'])
        row+=1

#
#
# 循环获取数据
#
#
for i in range(1,10+1):
    url='https://club.jd.com/comment/productPageComments.action?productId=1475512465&score=0&sortType=5&page=%d&pageSize=100&isShadowSku=0&fold=' % i
    try:
        json_req = requests.get(url)
        dat = json_req.json()
        write_json_to_xls(dat)
        print(u'写入一页数据')
    except Exception as e:
       print(u'获取数据失败数据',e)
    time.sleep(0.5)


#将数据存进表格
w.save('result.xls')