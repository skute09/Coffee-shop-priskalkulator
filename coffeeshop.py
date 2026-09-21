#Kilde: The Coffee Shop Price Calculator - www.101computing.net/the-coffee-shop-price-calculator
menu = {
   "Espresso": 2.50,
   "Americano": 3,
   "Latte": 2.50,
   "Cappuccino": 3,
   "Macchiato": 2.50,
   "Mocha": 3.50,
   "Flat White": 2.50
}

coffeeSizes = {
   "Medium": 0,
   "Large": 1,
   "Extra Large": 1.50,
}

diningPlaceOptions = {
   "Take Away": 1,
   "Eat In": 0
}

receipt = 0

def chooseOption(dict, questionMessage, optionsMessage):
   global receipt
   print("\n----------------------------")
   print(optionsMessage)
   for item, price in dict.items():
      print(f" > {item} £{price}")

   while True:
      option = input(questionMessage).title()
      if option in dict:
         receipt += dict[option]
         break
      else:
         print(f"{option} is not an option please try again.")

print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("+                                 +")
print("+         The Coffee Shop         +")
print("+             Welcome             +")
print("+                                 +")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

chooseOption(menu, "What type of coffee would you like? ", "We serve the following coffees:")
chooseOption(coffeeSizes, "What size of coffe would you like? ", "We serve the coffies in the following sizes:")
chooseOption(diningPlaceOptions, "Eat in or take away: ", "Dining places:")

print("----------------------------")
print("Total Cost: £" + str(receipt))