# digite algo e descubra algumas caracteristicas sobre o que foi digitado

a = input("digite algo: ")
print(f"o tipo primitivo desse valor é: {type(a)}")
print(f"só tem espaço?  {a.isspace()}")
print(f"é um número? {a.isnumeric()}")
print(f"é alfabético ?  {a.isalpha()}")
print(f"é alfanuúmerico ?  {a.isalnum()}")
print(f"está em maiúsculas?  {a.isupper()}")
print(f"está em minúsculas? {a.islower()}")
print(f"está capitalizada?  {a.istitle()}")