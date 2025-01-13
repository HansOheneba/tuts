def fizz_buzz(number):
    if() (number % 3 == 0) and (number % 5 == 0):
        return 'FizzBuzz'
    if number % 3 == 0:
        return 'Fizz'
    if number % 5 == 0:
        return 'Buzz'
    return number
    
number = int(input('Enter a number: '))
print(fizz_buzz(number))