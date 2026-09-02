# int type data

Ashiqul = 420
print(Ashiqul)
print(type(Ashiqul))



# # Floating type data

yo = 55.5
print(yo)
print(type(yo))



# # complex type data


no = 568j
print(no)
print(type(no))


# # string type data

Methil = "motherfuther"
print(Methil)
print(type(Methil))
shamim = "bainmach"
print(Methil + (" ") + (shamim))
name = "ashiqul"
print("my name is" + (" ") + name)


# # bool type data

Bool = True
print(Bool)
print(type(Bool))
x = 7
y = 4
print(x == y)
print(x>y)
print(x<y)


# # Binary type data
# # byte 

numbers = [23,45,68,255]
b = bytes(numbers)
print(type(b))


# # byte array
num3 = [34,56,255,56]
b1 = bytearray(num3)
print(type(b1))
b1[2] = 6
print(b1[2])
print(b1)


# # none type data

g = None
print(g)
print(type(g))


# # list type data

friends = ["methil","shamim"]
print(friends)
friends[1] = "nishan"
print(type(friends))
print(friends)


# # tuple type data

vai = ("mon","shamim")
print(vai)
print(type(vai))



# # range type data

ran = range(45)

for i in ran:
    print(i)

print(b1)
for i in b1:
    print(i)
    print(ran)

yo = range(6)
print(yo)
for e in yo:
    print(e)

b2 = [20,28,52,245]
b3 =bytearray(b2)
b3[1] = 38
print(b3)
for x in b3:
    print(x)