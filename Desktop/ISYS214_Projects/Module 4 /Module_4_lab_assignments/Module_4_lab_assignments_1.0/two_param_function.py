def message(what, number):
    print("Enter", what, "number", number)

message("telephone", 11)
message("price", 5)
message("number", "number")



# Positional parameter passing
def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)


adding(c = 1, a = 2, b = 3)
adding(4, 3, c = 2)






# Entering a greeting name
def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")





# use-case: Entering a first and last name
def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction("Skywalker", "Luke")
introduction("Quick", "Jesse")
introduction("Kent", "Clark")





# Useful for math equations 
def my_function(a, b, c):
    print(a, b, c)

my_function(1, 2, 3)






# First example
def introduction(first_name, last_name="Smith"):
    print("Hello, my name is", first_name, last_name)
    
introduction("James", "Doe")
introduction(first_name="William")


# Second example
def introduction(first_name="John", last_name="Smith"):
    print("Hello, my name is", first_name, last_name)
