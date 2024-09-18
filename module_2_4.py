# Исходные данные

# ПОПЫТКА №3
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Решение
primes = []
not_primes = []

for num in numbers:
    if num > 1:
        is_prime = True
        for j in range(2, int(num ** 0.5)+1):
            if num % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        else:
            not_primes.append(num)
# Вывод результата
# print()
print('Primes: ', primes)
print('Not Primes: ', not_primes)