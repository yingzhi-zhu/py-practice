"""
流程语句练习
"""
# a, b = 1, 2
# while b < 10:
#     # print(b)
#     print(b, end=",")
#     # 先执行右边 然后再赋值
#     a, b = b, a + b

"""
if语句
"""
# a, b = -1, 1
# if a:
#     print("a为", "真")
# else:
#     print("a为", "假")
# if b:
#     print("b为", "真")
# else:
#     print("b为", "假")
#
# if a > 0:
#     print("a>0")
# elif a == 0:
#     print("a==0")
# else:
#     print("a<0")

"""
循环语句
"""
# n = 100
# mySum = 0
# counter = 1
# while counter <= n:
#     mySum = mySum + counter
#     counter += 1
# print("1 到 %d 之和为: %d" % (n, mySum))
#
# # while else语句
# while n > 100:
#     print("大于100")
# else:
#     print("小于100")
#
# # n = str(input("请输入一个名志:"))
# # print("你输入的数字", n)
#
# languages = ["chinese", "america", "english"]
# for item in languages:
#     print(item, end=" ")
#
# for i in range(len(languages)):
#     print(i, languages[i])
#
# # pass语句只用于占位
# for letter in "olive":
#     if letter == 'v':
#         pass
#     print("当前单词", letter)

"""
迭代器与生成器
"""
my_list = [1, 2, 3, 4, 5]
it = iter(my_list)
print(next(it))


# yield关键字 让函数自动返回一个迭代器
def fibonacci(n):
    a, b = 1, 2
    while a < n:
        yield a
        a, b = b, a + b


f = fibonacci(20)
print(next(f))
for item in f:
    print(item, end=" ")
