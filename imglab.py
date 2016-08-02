import numpy
import urllib.request
from PIL import Image, ImageDraw
import random
import xlwt
import xlrd
import io
import math

screen_width = 750


def readItemStream():
    r = xlrd.open_workbook('items.xlsx')
    return r

item_xls = readItemStream()
item_table = item_xls.sheets()[0]
global item_num
global item
item_num = item_table.nrows - 1  # 读入商品数
item = []

item_index = 0
while item_index < item_num:
    # print(item_table.cell(item_index,1).value)
    item_index = item_index + 1
    # print(item_index)
    item.append([
        item_table.cell(item_index,0).value,
        item_table.cell(item_index,1).value,
        item_table.cell(item_index,2).value,
        item_table.cell(item_index,3).value,
        item_table.cell(item_index,4).value])

print()

item_random = random.randint(0,item_num)

#print(item[item_random][4])

#img_url = item[item_random][4]
#img_file = urllib.request.urlopen(img_url)
#img_bytes = io.BytesIO(img_file.read())
#img_data = Image.open(img_bytes)
#img_data.show()

def getImageData(item_id):
    img_url = item[item_id][4]
    img_file = urllib.request.urlopen(img_url)
    img_bytes = io.BytesIO(img_file.read())
    r = Image.open(img_bytes)
    # r.show()
    return r

img_data = getImageData(item_random)

# img_array = img_data.load()

print(img_data.size)
print(img_data.size[0])
# print(img_array[0,0])




def calcColor(color_input,color_base):
    # 背景色过滤参考值
    r = (color_input[0] - color_base[0])**2 + (color_input[1] - color_base[1])**2 + (color_input[2] - color_base[2])**2
    return int(r)

def getImageBox(img_input):
    img_array = img_input.load()
    color_base = img_array[0,0] # 基本背景色取值
    img_width = img_input.size[0]
    img_height = img_input.size[1]

    # for X1
    x1 = 0
    sum = 0
    for i in range(0,img_width):
        x1 = i
        for j in range(0,img_height):
            # str(img_array[i,j]) + str(calcColor(img_array[i,j])))
            sum = sum + calcColor(img_array[i,j],color_base)
        # print('line: ' + str(i) + ' ' + str(sum/img_height))
        if (sum/img_height) > 2:
            break;
    #print('\nX1 stopped in line ' + str(x1) )

    # for X2
    x2 = 0
    sum = 0
    for i in range(0,img_width):
        x2 = img_width - i - 1
        for j in range(0,img_height):
            # str(img_array[i,j]) + str(calcColor(img_array[i,j])))
            sum = sum + calcColor(img_array[x2,j],color_base)
        # print('line: ' + str(i) + ' ' + str(sum/img_height))
        if (sum/img_height) > 2:
            break;
    #print('\nX2 stopped in line ' + str(x2) )

    # for Y1
    y1 = 0
    sum = 0
    for i in range(0,img_height):
        y1 = i
        for j in range(0,img_width):
            # str(img_array[i,j]) + str(calcColor(img_array[i,j])))
            sum = sum + calcColor(img_array[j,i],color_base)
        # print('line: ' + str(i) + ' ' + str(sum/img_width))
        if (sum/img_width) > 2:
            break;
    #print('\ny1 stopped in line ' + str(y1) )

    # for Y2
    y2 = 0
    sum = 0
    for i in range(0,img_height):
        y2 = img_height - i - 1
        for j in range(0,img_width):
            # str(img_array[i,j]) + str(calcColor(img_array[i,j])))
            sum = sum + calcColor(img_array[j,y2],color_base)
        # print('line: ' + str(i) + ' ' + str(sum/img_width))
        if (sum/img_width) > 2:
            break;
    #print('\ny2 stopped in line ' + str(y2) )

    # 画参考辅助线
    img_refer = img_input
    img_refer = img_refer.crop((0,0,img_width-1,img_height-1))
    img_draw = ImageDraw.Draw(img_refer)
    img_draw.line([(x1,0),(x1,img_height)],fill = (0,0,0),width = 1)
    img_draw.line([(x2,0),(x2,img_height)],fill = (0,0,0),width = 1)
    img_draw.line([(0,y1),(img_width,y1)],fill = (0,0,0),width = 1)
    img_draw.line([(0,y2),(img_width,y2)],fill = (0,0,0),width = 1)
    img_refer.show()

    return (x1,y1,x2,y2)

def createUnit(limit):
    mode = random.randint(2,limit)
    unit = []
    for i in range(0,mode):
        unit.append(random.randint(0,item_num))
    return unit

def createLayout(layout_num):
    r = []
    for i in range(0,layout_num):
        r.append([])
        if i == 0:
            r[i] = createUnit(2)
        else:
            r[i] = createUnit(4)
    return r

def createImageList(layout_input):
    r = []
    print('\ncreateImageList ...')
    for i in range(0,len(layout_input)):
        r.append([]) # 创建一行图像，并定位到 r[i]
        print()
        print(layout_input[i])
        for j in range(0,len(layout_input[i])):
            r[i].append(getImageData(layout_input[i][j])) # 原始图片载入
            r[i][j] = r[i][j].crop(getImageBox(r[i][j])) # 切掉白边
    print('- Image list done.')
    return r

def getGoldBox(img_input):
    w = img_input.size[0]
    h = img_input.size[1]
    delta = 4 * ((w + h) ** 2) - 4 * 4 * ( w * h - w * h / 0.618)
    r = (-2 * (w + h) + math.sqrt(delta)) / 8
    print('w = ' + str(w) + ' , h = ' + str(h) + ' , delta = ' + str(delta) + ' , r = ' + str(r))
    return [(int(w + 2 * r),int(h + 2 * r)),int(r)]

def createGoldList(img_list_input):
    g = []
    for i in range(0,len(img_list_input)):
        g.append([])
        j = 0
        for j in range(0,len(img_list_input[i])):
            print('\ngetGoldBox ' + str(i) + ' , ' + str(j))
            # t = input('wait')
            b = getGoldBox(img_list_input[i][j])
            g[i].append(Image.new('RGBA',b[0],(255,255,255)))
            g[i][j].paste(img_list_input[i][j],(b[1],b[1]))
            # g[i][j].show()
    return g

def createRow(row_input):
    pic_round = len(row_input)
    row_height = 0
    row_width = 0
    for i in range(0,pic_round):
        if row_input[i].size[1] > row_height:
            row_height = row_input[i].size[1]
    for i in range(0,pic_round):
        w = int(row_input[i].size[0] * row_height / row_input[i].size[1])
        h = row_height
        row_input[i] = row_input[i].resize((w,h),Image.ANTIALIAS)
        row_width = row_width + w
    r = Image.new('RGBA',(row_width,row_height),(255,255,255))
    x = 0
    for i in range(0,pic_round):
        if i > 0:
            x = x + row_input[i - 1].size[0]
        r.paste(row_input[i],(x,0))
    r = r.resize((750,int(row_height * 750 / row_width)),Image.ANTIALIAS)
    return r

def drawLayout(list_input):
    layout_width = screen_width
    layout_height = 0
    img_row = []
    for i in range(0,len(list_input)): # 布局
        img_row.append(createRow(list_input[i]))
        layout_height = layout_height + img_row[i].size[1]
    r = Image.new('RGBA',(layout_width,layout_height),(255,255,255))
    y = 0
    for i in range(0,len(list_input)): # 贴图
        if i > 0:
            y = y + img_row[i - 1].size[1]
        r.paste(img_row[i],(0,y))
    return r


layout = createLayout(5)
print(layout)
img_list = createImageList(layout)

gold_list = createGoldList(img_list)

print(layout)

#canvas = Image.new('RGBA',(750,960),(0,0,0))
#canvas.show()

#create_layout
img_layout = drawLayout(gold_list)
img_layout.show()



print()
print('ok')
