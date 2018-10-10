def fib(n):    # write Fibonacci series up to n
    "Print a Fibonacci series up to n"
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a+b

print "\n"
print "Hello, World!"

list=[10,500,2000]

for x in list:
    print "The Fibonacci numbers up to " + str(x) + " are:"
    fib(x)
    print "\n"