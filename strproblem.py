# #center method
# name = "Prateek"
# #**Prateek** , 11
# print(name.center(11,"*"))      # it will print name with 2 astrics in left and two in right

name = input("enter your name: ")
print(name.center(len(name) + 8 , "*"))