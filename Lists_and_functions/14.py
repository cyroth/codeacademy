#Passing a range into a function

def my_function(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

print(my_function(list(range(0,3)))) # Add your range between the parentheses!
