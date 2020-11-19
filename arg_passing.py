
the_int = 99
the_list = [1,2,3]

def my_function_1(an_int, a_list):
    print(f"1.1 an_int ({id(an_int)}) is {an_int}, a_list ({id(a_list)}) is {a_list}")
    an_int = 77
    a_list.append(500)
    print(f"1.2 an_int ({id(an_int)}) is {an_int}, a_list ({id(a_list)}) is {a_list}")


print(f"1. the_int ({id(the_int)}) is {the_int}, the_list ({id(the_list)}) is {the_list}")

my_function_1(the_int, the_list)

print(f"2. the_int ({id(the_int)}) is {the_int}, the_list ({id(the_list)}) is {the_list}")