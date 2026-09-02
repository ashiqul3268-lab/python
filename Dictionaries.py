friendinfo = {
    "Ashiqul" :{
        "name": "ashiqul",
        "roll": "17340",
        "location": "khulna",
        "subject": "science",
        "number": "01973343268"
    },
    "methil" : {
        "name": "methil",
        "roll": "12",
        "location": "nalta",
        "subject": "science"
        },
        "shamim": "asshole"
}


# print(friendinfo)
# print(friendinfo["methil"]) 

# # Accessing Items

# print(friendinfo["shamim"])
# print(friendinfo["Ashiqul"]["number"])
# print(friendinfo["methil"]["subject"])

# yo = friendinfo.get("methil")
# print(yo)

# y = friendinfo.keys()
# print(y)

# x = friendinfo.values()
# print(x)


# # change dictionary item

# #1
# friendinfo["shamim"] = ["motherfucker"]
# print(friendinfo)
# print(friendinfo["shamim"])

# #2 
# friendinfo.update({"methil": "methil is an asshole"})
# print(friendinfo["methil"])


# # remove dictionary item

# 1
# friendinfo.pop("Ashiqul")
# print(friendinfo)

# 2(last item remove)
# friendinfo.popitem()
# friendinfo.popitem()
# print(friendinfo)

# 3
# del friendinfo["Ashiqul"]
# print(friendinfo)

# 4
# friendinfo.clear()
# print(friendinfo)


# # Loop dictionaries

# 1
# for y in friendinfo:
#     print(y)

# for x in friendinfo.values():
#     print(x)

# 2
# for a in friendinfo.keys():
#     print(a)

# 3
# for b in friendinfo.items():
#     print(b)


# # Copy dictionaries

# 1
# vai = friendinfo.copy()
# print(vai)

# 2
y = dict(friendinfo)
print(y)


