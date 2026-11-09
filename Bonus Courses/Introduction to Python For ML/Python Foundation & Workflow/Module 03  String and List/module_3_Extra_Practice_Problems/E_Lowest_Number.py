n = int(input())
inp = input()
numbers = [int(num) for num in inp.split()]

print(min(numbers), numbers.index(min(numbers)) + 1)

# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/E