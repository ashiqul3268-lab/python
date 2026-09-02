# class methil:
#     phone = "Iphone"
#     car = "Marcedis"
#     home = "big house"


# class shamim:
#      smart_phone = "samsung"
#      super_car = "lambo"
#      palace = "bigger house"

# class mon:
#      camera = "sony"
#      bike = "gpx"



# class ash(methil,shamim,mon):
#      broken_vivo = ""
#      small_house = ""

# """ mobile = "broken vivo"
# house = "small house"
# """



# k = ash()
# print(k.car)
# print(k.phone)
# print(k.camera)
# print(k.super_car)


class baba:
    phone = "Iphone"
    car = "Marcedis"
    home = "bigger house"


class son1(baba):
     smart_phone = "samsung"
     super_car = "lambo"
     palace = "big house"

class son2(son1):
     camera = "sony"
     bike = "gpx"



class son3(son2):
     broken_vivo = ""
     small_house = ""

""" mobile = "broken vivo"
house = "small house"
"""



k = son3()
print(k.car)
print(k.phone)
print(k.camera)
print(k.super_car)
y = son2
print(y.phone)
x = son1
print(x.home)