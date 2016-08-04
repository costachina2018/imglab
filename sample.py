# import public_lib
from imglib import *
from xiyou_lib import *


print(screen_width)

item = readRawStream('excel_2','raw_items.xlsx')
item_sample = getRandomItem(item)
img_sample = getImageFromURL(item_sample[5])
core_sample = createCoreImage(img_sample)
gold_sample = createGoldImage(core_sample)

img_sample.show()
core_sample.show()
gold_sample.show()

user_input = ''

while user_input != '88':
    print()
    width_sample = 0
    height_sample = 0
    user_input = input('\n\n  请输入希望测试的窗体大小：（Enter 开始输入，88 结束程序）')
    width_sample = int(input('  width: '))
    height_sample = int(input('  height: '))
    put_sample = putImageIntoBox(img_sample,width_sample,height_sample)
    put_sample.show()

print('sample.py - ok')
