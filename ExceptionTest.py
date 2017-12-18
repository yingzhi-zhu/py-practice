try:
    raise NameError("名志错了")
except NameError as e:
    print(e.args[0])
