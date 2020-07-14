count=0
b=0
for x in range (6):
    a=int(input('number'))
    if a%2==0 :
        b+=a
        count+=1
print("the sum of the numbers" ,(b/count))
