import urllib.request
import random
import xlwt
import xlrd
import io
import os

# ����ԭʼ����

def readRawStream(api,parameter): # ��ȡĳ����Դ��ԭʼ����
    r = []
    if api == 'excel_2':
        if not os.path.exists(parameter):
            print('Failed to read the file ' + parameter)
        item_xls = xlrd.open_workbook(parameter) # �򿪲���ָ���� .xls �ļ�
        item_table = item_xls.sheets()[0] # ӳ���һ�����ݱ�
        item_num = item_table.nrows - 1 # ��ȡ��Ʒ����
        for i in range(0,item_num):
            r.append([
                item_table.cell(i,0).value, # ID
                item_table.cell(i,1).value, # ����
                item_table.cell(i,2).value, # ��Ŀ
                item_table.cell(i,3).value, # Ʒ��
                item_table.cell(i,4).value, # �۸�
                item_table.cell(i,5).value # ͼƬ��ַ
            ])
    return r


def getRandomItem(item_list):
    r = item_list[random.randint(0,len(item_list) - 1)]
    return r

print('xiyou_lib.py imported. - ok')
