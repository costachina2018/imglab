import numpy
import urllib.request
from PIL import Image
import random
import xlwt
import xlrd

def readItemStream():
    r = xlrd.open_workbook('items.xlsx')
    return r

def initItems():
    item_xls = readItemStream()
    item_table = item_xls.sheets()[0]
    global item_num
    global item
    item_num = item_table.nrows - 1  # 获取商品数量
    item = []

    item_index = 0
    while item_index < item_num:
        print(item_table.cell(item_index,1).value)
        item_index = item_index + 1
        print(item_index)
        item.append([
            item_table.cell(item_index,0).value,
            item_table.cell(item_index,1).value,
            item_table.cell(item_index,2).value,
            item_table.cell(item_index,3).value,
            item_table.cell(item_index,4).value])

print()
print(item[100][4])

print()
print('ok')
