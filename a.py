
name = input("your name:")
name = int(name)
age= input("your age:")
age = int(age)
address = input("your address:")

if type(name) == int:
      print("Error")
elif age == int:
      print("Error")
else:
      print("Hello Mr/Ms", name, "age", age, "located in",address,"." , "\n" ,
      "thanks for beening one of our community," , "\t" , "\t","Enjoy")
