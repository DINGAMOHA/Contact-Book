# a contact book is a database used to store entries related to a person contacts like a phone number, email address, etc it is also
# known as the address book.
while True:
   menu = input("(S) for search , (W) to write a new contact , (Q) to quit the app: ")
   if menu == "w":
    with open("Contact.txt", "a") as f:
      name = str(input("Enter a name: "))
      number = input("Enter a number: ")
      f.writelines((name, " : ", number,"\n"))
   elif menu == "s": 
     with open("contact.txt", "r") as f:
      search = input("Search:   ")
      for x in f:
        if search in x:
           print(x)
   else:
     print("Thank you for using the app")
     break