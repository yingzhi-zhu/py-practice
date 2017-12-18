# def print_hello(name="杨九日", age=16):
#     """默认参数定义"""
#     print(name, ":", age)
#
#
# print_hello("影之助", 18)
# print_hello("影之助")
# print_hello()
#
#
# def print_unlimited_param(name, *param):
#     """不定长参数"""
#     print("名字 ", name)
#     print("其他")
#     for item in param:
#         print(item, end=" ")
#
#
# print_unlimited_param("zhu", 1, "yang", "321", 1.215, [15, 45, 45, 2], {263, 213, 3213}, (1, 54, 545))

# python lambda函数
# my_sum = lambda arg1, arg2: arg1 + arg2
# print("lambda值为", my_sum(1, 2))


# global nonlocal关键字声明 修改局部变量
# num = 1
#
#
# def fun1():
#     global num  # 需要使用 global 关键字声明
#     print(num)
#     num = 123
#     print(num)
#
#
# def outer():
#     num1 = 10
#
#     def inner():
#         nonlocal num1  # nonlocal关键字声明
#         num1 = 100
#         print(num1)
#
#     print(num1)
#     inner()
#     print(num1)
#
#
# outer()
# fun1()
