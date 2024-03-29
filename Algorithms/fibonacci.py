# Fibonacci sequence
# a, b = 0, 1
# for i in range(0, 10):
#     print(a)
#     a, b = b, a + b

# Fibonacci generator
def fib(num):
    a, b = 0, 1
    for i in range(0, num):
        yield "{}: {}".format(i, a) # yield is the keyword for generators
        a, b = b, a + b

for item in fib(20):
    print(item)
