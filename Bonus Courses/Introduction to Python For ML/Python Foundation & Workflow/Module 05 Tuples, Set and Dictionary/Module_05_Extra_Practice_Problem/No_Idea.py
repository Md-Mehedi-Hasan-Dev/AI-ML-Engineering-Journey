inp = input()
n, m = map(int, inp.split())
inp = input()
numbers = [int(num) for num in inp.split()]
inp = input()
a = {int(x) for x in inp.split()}
inp = input()
b = {int(y) for y in inp.split()}

happiness = 0

for i in range(n):
    if numbers[i] in a:
        happiness += 1
    if numbers[i] in b:
        happiness -= 1

print(happiness)

# https://www.hackerrank.com/challenges/no-idea/