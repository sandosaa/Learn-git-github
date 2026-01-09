# verb = input ("Enter a verb : ")
# print ("I can",verb,"better than you")
# print((verb + " ")*5)

# secret = 4
# var = int (input("guess the number: "))
# print (secret == var)

secret = 10
var = int (input("guess the number: "))
if secret>var:
    print("Your guess is too low!")
elif secret<var:
    print("Your guess is too high!")
else:
    print("Your guess is the same as the secret")