import random

user = int(input("how many characters should the password have?"))

list1 =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
list2=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
list3=["1","2","3","4","5","6","7","8","9","0"]

list4=["!","@","#","$","%","^","&","*","(",")","_","+","-","=","{","}","[","]",":",";","'","<",">",",",".","?"] 

password = ""
for i in range(user):
    list5 = random.choice(list1 + list2 + list3 + list4)
    password += list5

print("Generated password:", password)
