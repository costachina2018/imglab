import urllib.request
import random
import xlwt
import xlrd
import io
import os

# 导入原始数据

def readRawStream(api,parameter): # 读取某个来源的原始数据
    r = []
    if api == 'excel_2':
        if not os.path.exists(parameter):
            print('Failed to read the file ' + parameter)
        item_xls = xlrd.open_workbook(parameter) # 打开参数指定的 .xls 文件
        item_table = item_xls.sheets()[0] # 映射第一张数据表
        item_num = item_table.nrows - 1 # 获取商品个数
        for i in range(0,item_num):
            r.append([
                item_table.cell(i,0).value, # ID
                item_table.cell(i,1).value, # 名称
                item_table.cell(i,2).value, # 类目
                item_table.cell(i,3).value, # 品牌
                item_table.cell(i,4).value, # 价格
                item_table.cell(i,5).value # 图片地址
            ])
    return r


def getRandomItem(item_list):
    r = item_list[random.randint(0,len(item_list) - 1)]
    return r

print('xiyou_lib.py imported. - ok')
