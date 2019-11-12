# for i in range(1, 20):
#     if (i > 2 and i % 2 != 0 and i % 5 != 0) or i == 2 or i == 5:
#         for d in range (3, int(i/2)+1):
#             if i % d == 0:
#                 break
#             elif d == int(i/2):
#                 print(i)
#             elif i == 2 or i == 3 or i == 5:
#                 print(i)



# primes = [2, 3]
# notprimes = [1]


# a = 1
# b = 100




# for p in primes:
#     m = int((b + 1) / p)
#     for mc in range (2, m + 1):
#         notprimes.append(p * mc)



# notprimes.sort()
# print(notprimes)


# print(len(primes))

# print(primes[len(primes)-1])


primes = [2, 3]
notprimes = [1]


a = 1
b = 100











for i in range(a, b+1):
    if (i > 2 and i % 2 != 0 and i % 5 != 0) or i == 2 or i == 5:
        for d in primes:
            if i % d == 0:
                break
            elif d == primes[len(primes)-1]:
                primes.append(i)
                m = int((b + 1) / p)
                for mc in range (2, m + 1):
                    notprimes.append(p * mc)

notprimes.sort()
print(notprimes)
print(notprimes)

#test
#erer
#more lines
