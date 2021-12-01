import time

start = time.time()

# fibonacci sequence
fib = [0, 1]

# iterator
i = 2

# when the number is 1000 digits long
while True:
    # using the function given in question
    fib_new = fib[i - 1] + fib[i - 2]
    # Appending the new fibonacci to the list
    fib.append(fib_new)
    # condition to check for 1000 digits
    if fib_new > 10 ** 999:
        print(i)
        break
    i = i + 1

end = time.time()
print(end - start)
