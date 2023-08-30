a = b = ""

#while a.isdigit() is False or b.isdigit() is False:
while not a.isdigit()  or not b.isdigit() :
    a = input("Entrez un premier nombre : ")
    b = input("Entrez un deuxième nombre : ")
    print("Veuillez rentrer des nombres !")
    
else:
    print(f"L'addition de {a} et {b} est égale à : {int(a) + int(b)}") 