def encoder(num):
    roman,s,decimal= ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"],"",[1000,900,500,400,100,90,50,40,10,9,5,4,1]
    for i in range(13):
           while num >= decimal[i]:
                  num -= decimal[i]
                  s += roman[i]
    return s

def decoder(r):
    k=r
    if r=="":return "Don't leave the input blank"
    roman,s= {"M":1000,"CM":900, "D":500, "CD":400, "C":100, "XC":90, "L":50, "XL":40, "X":10, "IX":9, "V":5, "IV":4, "I":1},0
    while r!="":
        if r[:2] in roman:a,r=r[:2],r[2:]
        elif r[0] in roman:a,r=r[0],r[1:]
        else: return "Enter proper Decimal/Roman number as input"
        s+=roman[a]
    return s if encoder(int(s))==k else "Not a valid Roman Numeral"
    
a=input()
try:print(encoder(int(a)))
except:print(decoder(a.upper())) 