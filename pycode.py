# for i in range(1, 20):
#     if (i > 2 and i % 2 != 0 and i % 5 != 0) or i == 2 or i == 5:
#         for d in range (3, int(i/2)+1):
#             if i % d == 0:
#                 break
#             elif d == int(i/2):
#                 print(i)
#             elif i == 2 or i == 3 or i == 5:
#                 print(i)



primes = [2, 3, 5, 7]

# print(len(primes))

# print(primes[len(primes)-1])


for i in range(11, 1000000):
    if (i > 2 and i % 2 != 0 and i % 5 != 0) or i == 2 or i == 5:
        for d in primes:
            if i % d == 0:
                break
            elif d == primes[len(primes)-1]:
                primes.append(i)

print(primes)
print(len(primes))