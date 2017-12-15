def print_hello(name="杨九日", age=16):
    """默认参数定义"""
    print(name, ":", age)


print_hello("影之助", 18)
print_hello("影之助")
print_hello()


def print_unlimited_param(name, *param):
    """不定长参数"""
    print("名字 ", name)
    print("其他")
    for item in param:
        print(item, end=" ")


print_unlimited_param("zhu", 1, "yang", "321", 1.215, [15, 45, 45, 2], {263, 213, 3213}, (1, 54, 545))


