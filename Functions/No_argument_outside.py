# As the value is defined inside the function and not as a paramemter it will be only display when called 
# inside the function, when we create an object/call the function as no parameters were present
# we cant access the value within the function outside of that function

def fun():
    x=10
    print(x)
fun()
print(x)