name,char = input("enter your name and character :").split(",")
print("length of your name is:",len(name))
print(f"chacacter count :{name.lower().count(char.lower())}")
