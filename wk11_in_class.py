my_dict = {}
my_other_dict = dict()

my_3rd_dict = {'a': 1, 'b': 2, 'c': 3}
my_3rd_dict['d'] = 99

print(my_3rd_dict['a'])

print(my_3rd_dict.keys())

for k,v in my_3rd_dict.items():
    print(f"key: {k}, value: {v}")


headers = ("h1", "h2", "h3")
body = ((1,2,3),(4,5,6), (7,8,9))

for row in body:
    my_4th_dict = dict(zip(headers, row))
    print(my_4th_dict)


import string

position = 0
my_5th_dict = {}
for letter in string.ascii_lowercase:
    my_5th_dict[letter] = position
    position += 1

print(my_5th_dict)

my_letters = [letter for letter in my_5th_dict.keys()]

print(my_letters)

class Student:
    def __init__(self, name, id):
        self.fullname = name
        self.studentid = id
    def __str__(self):
        return f"{self.fullname}, {self.studentid}"


first_student = Student("Joe", 1)

print(first_student)



