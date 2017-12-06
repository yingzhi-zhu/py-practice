# 基本类型练习
height = 1.75
weight = 60
name = '杨九日'
nameArr = ['杨九日', 12, 3, 43, 54]
tinyNameArr = ['杨九日', 12]
nameList = ('杨九日', 12, 3, 43, 54)
dict = {"haha": 1, 1: 2}

bmi = weight/(height*height)
print('hello python')
print(name[2:])
nameArr.append(12)
nameArr.append(12)
print(nameArr)
print(tinyNameArr)
print(len(nameList))
print(nameList[0])

print(dict["haha"])
print(dict[1])

if bmi < 18.5:
    print('过轻')
elif bmi < 25:
    print('正常')
elif bmi < 28:
    print('过重')
elif bmi < 32:
    print('肥胖')
else:
    print('严重肥胖')
# 运算符练习
