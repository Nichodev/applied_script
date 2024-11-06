## args , kwargs ##

# def funcion_name(*args):
#     for arg in args:
#         print(arg)
# funcion_name(1,1,1,1,1,1,1,1,1)


# def print_info(name, *args):
#     print(f"Name: {name}")
#     for arg in args:
#         print(arg)
# print_info("Nicho", 25, "Stockholm")

# def function_name(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# function_name(Name="Nicho", age=25, city="stockholm")


# def print_all(args, **kwargs):
#     for arg in args:
#         print(arg)
#     for key, value in kwargs.items():
#         printUf(f"{key}: {value}")
# print_all([1,2,3],name="Nicho", age =25, city="Stockholm")


# def sum_numbers(*args):
#     return sum(args)
# print(sum_numbers(1,2,3,4,))


# def build_profile(**kwargs):
#     return kwargs
# profile = build_profile(name="Nicho", age=25, city="Stockholm")
# print(profile)


# def display_info(*args, **kwargs):
#     for arg in args:
#         print(arg)
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# display_info(1,2,4, name="Nicho", age=25, city="Stockholm")


# def calculate(operation, *args, **kwargs):
#     if operation == 'add':
#         return sum(args)
#     elif operation =="subtract":
#         results = args[0]
#         for num in args[1:]:
#             results -= num
#         return results
#     elif operation == "multiply":
#         results = 1
#         for num in args:
#             results *= num
#         return results
#     elif operation =="divide":
#         results = args[0]
#         try:
#             for num in args[1:]:
#                 results /= num
#         except ZeroDivisionError:
#             return "Cant divide by zero"
#         return results
#     else:
#         return "Unknown operation"
    
# print(calculate("add", 1,2,3,4,5,))
# print(calculate("subtract", 10, 2, 3))
# print(calculate("multiply", 3,5,8))
# print(calculate("divide" , 5, 0, 3))

## Lambda ##

# add = lambda x, y: x + y
# print(add(2, 3))


# def apply_func(f,x,y):
#     return f(x,y)

# results = apply_func(lambda a, b: a * b, 4, 5)
# print(results)

## map(function, iterable)

# def square(x):
#     return x * x
# numbers = [1,2,3,4,5]
# squared_numbers = list(map(square, numbers))
# print(squared_numbers)


##filter(function, iterable)##

# def is_even(x):
#     return x % 2 == 0

# numbers = [1,2,3,4,5,6,7,8]
# even_numbers = list(filter(is_even, numbers))
# print(even_numbers)

# number = [1,2,3,4,5,6]
# even_numbers = list(filter(lambda x: x % 2 == 0, number))
# print(even_numbers)

# def check_number(num):
#     if num > 0:
#         if num % 2 == 0:
#             print(f"{num} is a positive even number")
#         else:
#             print(f"{num} is a positive odd number")
#     else:
#             if num == 0:
#                 print (f"{num} is 0")
#             else:    
#                 print(f"{num} is negative")

# check_number(9)
# check_number(-5)
# check_number(0)


# def print_matrix(matrix):
#     for row in matrix:
#         for element in row:
#             print(element, end =" ")
#         print()
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9,]
# ]
# print_matrix(matrix)


# def my_function():
#     local_var = 10
#     print(local_var)

# my_function()
# print(local_var)


# global_var = 20

# def my_function():
#     print(global_var)

# my_function()
# print(global_var)


# def outer_function():
#     outer_var= "Yttre"

#     def inner_function():
#         inner_var = "Inre"
#         print(outer_var)
#         print(inner_var)

#     inner_function()

# outer_function()

# x = 10

# def modify_global():
#     global x 
#     x = 20

# modify_global()
# print(x)







