arg_list = [1, 2, 3]
arg = 25


def my_function(param, param2=27):
    """
    a description of what the function does

    :param param: usually an int or a list
    :param param2: defaults to 27
    :return:
    """
    if isinstance(param, list):
        param.append(100)
        param.append(param2)
        print(f"From inside function, param = {param}")

        param = [99, 88, 77]
        print(f"From inside function, param = {param}")
    elif isinstance(param, int):
        param = 32

        print(f"From inside function, param = {param}")
    else:
        pass


def my_fun_with_arbitrary_list(*args, **kwargs):
    for item in args:
        print(f"item is {item}")

    for k, v in kwargs.items():
        print(f"{k}: {v}")


my_function(arg, 99)

print(f"arg is {arg} in the global NS")

for i in range(5):
    my_function(arg_list)
    print(f"arg is {arg_list} in the global NS")

for i in range(10):
    if not i % 2:
        continue

    print(f"{i} is odd")

a_new_list = [1, 2, 3, 4, "a", "xyz"]
my_fun_with_arbitrary_list(9, 8, 7, a=123, b=234, xyz="abc")
