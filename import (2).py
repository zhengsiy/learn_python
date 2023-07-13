#导入整个function.py文件中的文件，在调用其中的任意函数的时候，实际是将所有程序都复制到了这个程序中
#import function


#function.make_pizza('beef','chiken','fruit')
#function.pets_message('candy')


#若只想导入模块中的特定函数，则使用from moudle_name import function_name
from function import make_pizza

make_pizza('apple','banana')


#给函数指定别名（适用于函数名太长或者这个文件中有重复函数名时）
from function import make_pizza as mp
mp('orange','beef')
