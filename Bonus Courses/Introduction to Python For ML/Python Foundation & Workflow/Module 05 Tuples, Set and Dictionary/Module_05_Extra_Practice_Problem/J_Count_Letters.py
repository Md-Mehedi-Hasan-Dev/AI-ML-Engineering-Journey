string = input()

count = {}

for i in range(len(string)):
    count[string[i]] = count.get(string[i], 0) + 1

sorted_c = dict(sorted(count.items()))

for key, value in sorted_c.items():
    print(f"{key} : {value}")

# https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/J