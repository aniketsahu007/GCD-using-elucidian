#GCd using elucidian 
def gcd(a,b):
    divisor = a
    dividend = b
    if a>b:
        dividend = a
        divisor = b
    if a == b:
        return a
    while (divisor>0):
        remainder = dividend%divisor
        dividend = divisor
        divisor = remainder
    return dividend
a , b =(input("enter the numbers").split())
a,b = int(a),int(b)
print(f"{gcd(a,b)}")
