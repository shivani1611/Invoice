
def Custmorinformation():
       fname = input ("Enter Your Firstname:")
       mname = input ("Entre Your Middlename:")
       lname = input ("Entre Your Lastname:")
       city  = input ("Entre your city:"
       state = input ("Entre State:")
       address = input ("Entre Your Street Address:")
       zipcode = input("Entre Zipcode:")
       product = input("Product Name:")
       price = int(input("Price of Product :"))
       quantity = int(input("Toatl Quantity:"))

       print("       ")
       print("-------Invoice-------")
       print("       ")

       print("Full name:", fname + " " + mname + " " + lname)
       print("Address:", address + " " + city + " " + state)
       print("Zipcode:", zipcode)
       print("Product details:", product + ", $" + "Price:", str(price) + ", " + "Quantity:",str(quantity))
       print("Total Price of Product: $", price * quantity)



Custmorinformation()



