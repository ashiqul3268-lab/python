# global
a = "ashiqul"
b = "shamim"

# local
def name():
    y = "mon"
    print(y)
name() #[eta type kore jekono jaygai function er vitorer man nite parbo]
print(b)
#print(y) [eta hobe na karon etake function er nich borabor likhte hobe]

def vai():
    global b
    b = "mm"
    print(b)

vai()