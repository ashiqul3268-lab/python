class players:
    def __init__(self,name,number,nationality):
        self.name = name
        self.jersey_number = number
        self.nationality = nationality
    
class messi(players):
    pass

p = messi("Lionel,","10,","Argentine")
print(p.name,p.jersey_number,p.nationality)

class neymar(players):
    pass

n = neymar("Jr,","10,","Brazilian")
print(n.name,n.jersey_number,n.nationality)