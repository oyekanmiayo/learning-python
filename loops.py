primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

for x in range(3,7):
    print(x)

for x in range(3, 10, 2):
    print(x)

count = 0
while True:
    print(count)
    if count == 3:
        break
    count += 1

for x in range(10):
    if x % 2 == 0:
        continue
    print(x)


# Prints out 0,1,2,3,4 and then it prints "count value reached 5"

count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")