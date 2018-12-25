alpha='abcdefghijklmnopqrstuvwxyz'
string=input("Enter a message to be encrypted : ")
key=int(input("Enter a key : "))
encrypted=''
for i in string:
    pos=alpha.find(i)
    newpos=(pos+key)%26
    newchar=alpha[newpos]
    encrypted+=newchar
print("Secret Message is :",encrypted)