n = int(input())
inp = input()
numbers = [int(num) for num in inp.split()]

x = numbers.index(min(numbers)) 
y = numbers.index(max(numbers))

numbers[x], numbers[y] = numbers[y], numbers[x]

for i in numbers:
    print(i, end=" ")

# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/M