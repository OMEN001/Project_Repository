#_*_conding:utf-8_*_
#@Time    :2020/3/415:08
#@Author  :xiaodong.wu
#@Email   :2586089125@qq.com

"""
#设置代码作者信息
    (1) 步骤  File -- Setting -- Editor -- File and Code Templates -- python Scripts


#常用的数据类型
    （1）数字
        整型（int）、浮点（float）、布尔（bool）
    （2）字符串
        用单引号或者双引号括起来 “123”，‘abc’,'柠檬班'
    （3）列表
        列表是有序的数据类型，用”[]“括起来，列表的元素可以是不同的数据类型（字符串、整型）
    （4）元组
        元组的元素不可更改
    （5）字典
        以键值对的形式存储用来表达映射关系
    （6）集合
"""
"""
#-----------------------------------------------------
#字符串的操作
str_1 = "hello"
str_2 = "python"
str_3 = "python,is,best"
str_4 = "python/"
#连接
print(str_1+str_2)
#重复输出
print(str_1*2)
#字符串的分割
print(str_3.split(',',2))
#strip()去掉头和尾指定的字符
print(str_2.strip("py"))
print(str_1.strip("o"))
print(str_4.strip('/'))

#----------------------------------------------------
#列表的操作
list = ['2',1,3.05,(1,2,3),[1,2,3]]
list_1 = [222,'python']
list_2 = [1,2,5,9,4]
#截取一个元素(列表的缩影从0开始)
print(list[1])
#截取一个片段(左闭右开)
print(list[1:])
print(list[2:4])
#新增操作
#append() 只能在列表的末尾添加数据，一次只能添加一个
list.append("4")
print(list)
#extend把两个列表合并成一个列表 list.extend(list_1) 存到list中
list.extend(list_1)
print(list)
#insert(x,value) 给列表中的某个位置插入元素
list.insert(2,"world")
print(list)
#删除操作
#pop(i) 删除列表指定位置的元素，如果不传参数某人删除最后一个
list.pop(1)
print(list)
list.pop()
print(list)
#remove() 删除列表中的指定元素（列表中的元素）
list.remove(222)
print(list)

#排序操作(只对数值类型的数据进行排序)
#sort() 对列表进行升序排序
list_2.sort()
print(list_2)
#reverse() 随对列表进行降序排序
list_2.reverse()
print(list_2)


#--------------------------------------------------
#字典的操作
dict = {"name":"Branlant","age":18,"sex":"gir"}

#新增操作
dict["height"]="180"
print(dict)
#修改操作
dict["height"]="180cm"
print(dict)
#删除操作
dict.pop("height")
print(dict)

#for循环取字典的键对应的值
for value in dict.values():
    print(value)
#for循环取字典的键
for key in dict.keys():
    print(key)

#for循环取字典的简直(键值对是一个元组的形式)
for item in dict.items():
    print(item)

"""


li = [11,22,33,44]
res = (enumerate(li))
for i in res:
    print(i)

# eval:识别字符串中的python表达式
s1 = "(1,2,3)"
s2 = "[11,22,33]"
print(eval(s1),type(s1))
# 注意点：如果是个纯粹的字符串，那么使用eval进行转换之后就变成了一个变量名
# s4 = "python"
# res4 = eval(s4)
# print(res4,type(res4))

#过滤函数： filter(lambda x:x<8,li)
li = [1,2,3,5,10,89,45,]
new_list = filter(lambda x:x<8,li)
print(new_list)


# #文件读取（文件不存在会报错）
# with open("data.txt","r",encoding="utf8") as f:
#     # c = f.read()
#     #读取文件的第一行内容
#     # c= f.readline()
#     #读取文件的所有内容，每一行内容作为一个元素放到列表当中
#     c = f.readlines()
#     print(c)
#
# #文件写入(写入的内容必须是字符串)
# # a,w模式打开文件，如果文件不存在，则会自动创建一个新的文件
# #a模式: 追加写入（在文件内容的结尾处写入）
# #w模式：写入（覆盖文件中原来的内容）
# with open("datas.txt","w",encoding="utf8") as file:
#     #write写入必须是字符串
#     file.write("天府三街 软件园 B区")
#     #writelines写入内容是一个列表（列表中的元素必须是字符串）
#     # file.writelines(["123","jshfks"])


# def fuc():
#     with open('data.txt',"r",encoding="utf8") as f:
#         c = f.readlines()
#         print(c)
#     dic = {}
#     for k,v in enumerate(c):
#         key = "data{}".format(k)
#         value = v.replace("\n",'')
#         dic[key] = value
#     return dic
# res = fuc()
# print(res)

# def fuc():
#     with open('data.txt',"r",encoding="utf8") as f:
#         data = f.readlines()
#         print(data)
#     list = []
#     for a in data:
#         b = a.split(",")
#         print(b)
#         dict = {}
#         for c in b:
#             # print(c)
#             # d = c.split(":")
#             # print(d)
#             # key = d[0]
#             # value = d[1].replace("\n","")
#             # dict[key]=value
#         # list.append(dict)
#             key = c.split(":")[0]
#             value = c.split(":")[1].replace("\n","")
#             dict[key] = value
#         list.append(dict)
#     return list
#
# res = fuc()
# print(res)



