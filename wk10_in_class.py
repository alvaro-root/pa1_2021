arg_list = [1, 2, 3]
arg = 25


def my_function(param):
    if isinstance(param, list):
        param.append(100)
    elif isinstance(param, int):
        param = 32
    else:
        pass
    print(f"From inside function, param = {param}")


my_function(arg)

print(f"arg is {arg} in the global NS")

my_function(arg_list)
print(f"arg is {arg_list} in the global NS")

