#Using strings in lists in functions
m = [1, 2, 3]
n = [4, 5, 6]

def join_lists(x,y):
    result = ""
    result = x+y
    return result
print join_lists(m, n)
# You want this to print [1, 2, 3, 4, 5, 6]