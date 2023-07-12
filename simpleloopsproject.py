# repetition
# simple loop
n = 6
k = 9
j = 4

for i in range(n):
    k = k + 5

print('Simple loop')
print(k)

# nested loop
# outer loop
for i in range(n):  # outer loop executed 'n' times
    # inner loop
    for j in range(n):  # inner loop executed 'n' times
        k = k + i + j
# i = constant time
print('Nested loop 1')
print(k)

# nested loop
for x in range(n):  # outer loop executed n times
    print(x, end='\n')
    for y in range(n - x):  # inner loop executed y times, i = constant time
        k = k + i + j

print('Nested loop 2')
print(k)

# nested loop
k = 0
for i in range(n):  # outer loop executed n times
    for j in range(20):  # inner loop executed 20 times
        k = k + i + j

print('Nested loop 3')
print(k)

# sequence

# selection
items = [1, 2, 3, 4, 5]  #.... to n, also O(n)
x = 9
k = 0
if x in items:
    print(x, "exists")
else:  # Let n be list.size(). Executed n times
    for i in range(len(items)):
        k = k + i
        print(k)

# O(1) - constant time
# O(log n) - logarithmic time
# O(n) - linear time
# O(n log n) - log-linear time
# O(n^2) = quadratic time

'''
Results:
Simple loop
39
Nested loop 1
219
0
1
2
3
4
5
Nested loop 2
429
Nested loop 3
1440
0
1
3
6
10
'''