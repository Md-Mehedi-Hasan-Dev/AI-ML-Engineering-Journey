n = int(input())
inp = input()
numbers = [int(num) for num in inp.split()]

tup = tuple(numbers)

print(hash(tup))

# https://www.hackerrank.com/challenges/python-tuples/ 
# this problem requires python 2