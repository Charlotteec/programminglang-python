# to reverse a string
s = "hello world"
print(s[::-1])

l = [1,2,5,4,2,3,1]
print(sorted(l)) # prints a sorted copy of l  but doesnt change l
l.sort() #sorts l and puts it into l for value in variable]
print(l)

l[::-1] #reverse

if 8 in l:
    print("8 is in l")
else:
    print("8 is not in l")

for i in range(len(l)):
    print("index is %d" % i)
    print("value is %d" % l[i])

a = 5;
b = 6;
a,b = b,a
# print("a = %d, b = %d " % a % b)
#
# def evens(l):
#     evens = []
#     for i in l:
#         if i%2 is 0:
#             evens.append(i)
#     return evens

def evens(l):
    return [x for x in l if x%2 == 0]

def odds(l):
    return [x for x in l if x%2 == 1]

print(evens([1,2,3,4,5,6,7,8,9]))
print(odds([1,2,3,4,5,6,7,8,9]))
