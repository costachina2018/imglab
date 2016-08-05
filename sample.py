from imglib import *
from xiyou_lib import *
import sys

item = readRawStream('excel_2','raw_items.xlsx')
if len(sys.argv) == 1:
    item_sample = getRandomItem(item)
    img_sample = getImageFromURL(item_sample[5])
else:
    img_sample = Image.open(sys.argv[1]) # 如果带命令行参数，直接对本地目标文件操作
core_sample = createCoreImage(img_sample)
gold_sample = createGoldImage(core_sample)

img_sample.show()
core_sample.show()
gold_sample.show()

put_sample = putImageIntoBox(img_sample,300,150)
put_sample.show()

put_sample = putImageIntoBox(img_sample,100,200)
put_sample.show()

put_sample = putImageIntoBox(img_sample,200,200)
put_sample.show()

user_input = ''

while user_input != '88':
    print()
    width_sample = 0
    height_sample = 0
    user_input = input('\n\n  请输入希望测试的窗体大小：（回车继续，88 结束程序）')
    if user_input == '88':
        break
    width_sample = int(input('  width: '))
    height_sample = int(input('  height: '))
    put_sample = putImageIntoBox(img_sample,width_sample,height_sample)
    put_sample.show()

print('sample.py - ok')
