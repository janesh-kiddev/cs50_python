s = input("Camelcase:")
print('SnakeCase: ',end="")
for i in s:
   if i.isupper():
      print("_",i.lower(),end="",sep="")
   if i.islower():
      print(i,end="")

print()
