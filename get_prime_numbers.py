
from matplotlib import pyplot as plt
# n = list(map(int,input().rstrip().split()))

a_limit = int(input())
divisors = []
divisors_count = 0
prime_numbers = []
for a_number in range(0, a_limit):
    divisors_count = 0
    divisors = []
    for i in range(2, a_number):
        if a_number % i == 0:
            divisors_count += 1
            divisors.append(i)

    if divisors_count > 0:
        is_prime = False
        print(a_number, "is not a prime number and its divisors are:")
        divisors_set = set(divisors)
        for m in divisors_set:
            print(m, end=", ")
    else:
        is_prime = True
        print(a_number, "is a prime number")
        prime_numbers.append(a_number)
    print("")

print("\nprime numbers are: ", end="")
for t in prime_numbers:
    print(str(t), end=", ")

### distance between prime numbers

dist = []
prev = prime_numbers[0]
for next_p in prime_numbers[1:]:
    dist.append(abs(prev - next_p))
    prev = next_p
print("\n\n")
print(dist)

#### plot
x_axis = range(len(dist))
plt.scatter(x_axis, dist)
plt.grid()
plt.show()