def fizzbuzz_convert(number):
    if number % 15 == 0:
        return "FizzBuzz"

    if number % 3 == 0:
        return "Fizz"

    if number % 5 == 0:
        return "Buzz"

    return str(number)


for number in range(1, 101):
    print(fizzbuzz_convert(number))

# result = fizzbuzz_convert(1)
# print(result)  # 1
#
# result = fizzbuzz_convert(3)
# print(result)  # Fizz
#
# result = fizzbuzz_convert(5)
# print(result)  # Buzz
#
# result = fizzbuzz_convert(15)
# print(result)  # FizzBuzz
