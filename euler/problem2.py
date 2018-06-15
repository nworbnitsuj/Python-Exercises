fib = 1
fib2 = 2
num = 0
total = 0

while num <=4000000:
    num = fib2
    if num % 2 == 0:
        total += num
    num = fib + fib2
    fib = fib2
    fib2 = num

print(total)
