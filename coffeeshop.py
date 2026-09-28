#Kilde: The Coffee Shop Price Calculator - www.101computing.net/the-coffee-shop-price-calculator

# Så disse dictionariesene er stilt opp med valg : pris sånn at eg kan enkelt bruke samme funksjon på alle de type valgene
# Har også stilt det opp sånn at spørsmålet og tittelen til valgene er sammen sånn at eg kan loope igjennom uten å måtte manuelt legge til
# questionMessage, optionsMessage og options i chooseOption parametre fordi loopen gjør det selv når den looper igjennom coffeeTypeOptions
coffeeTypeOptions = {
   "menu": {
      "questionMessage": "What type of coffee would you like? ",
      "optionsMessage": "We serve the following coffees:",
      "options": {
         "Espresso": 2.50,
         "Americano": 3,
         "Latte": 2.50,
         "Cappuccino": 3,
         "Macchiato": 2.50,
         "Mocha": 3.50,
         "Flat White": 2.50,
      }
   },

   "coffeeSizes": {
      "questionMessage": "What size of coffe would you like? ",
      "optionsMessage": "We serve the coffies in the following sizes:",
      "options": {
         "Medium": 0,
         "Large": 1,
         "Extra Large": 1.50,
      }
   },

   "takeAwayOptions": {
      "questionMessage": "Take away? Yes/no: ",
      "optionsMessage": None,
      "options": {
         "Yes": 1,
         "No": 0,
      }
   },
}

# orders bruker vi for å lagre hva brukeren har bestilt sånn at vi til slutt kan vise bestillingens varer og regne ut summen av prisen
orders = []

# denne funksjonen bruker vi til å vise informasjon om et valg og spørre brukeren hva de vil velge
def chooseOption(dict, questionMessage, optionsMessage):
   # \n er det samme som når du trykker enter
   print("\n----------------------------")
   if optionsMessage:
      # her printer vi på en måte tittelen til alle itemsa som blir printet etter på
      print(optionsMessage)
      # dict er dictionaryet med de mulige valgene som brukeren har å velge mellom
      # dict.items() returner en liste med tuples med key value par
      for item, itemPrice in dict.items():
         print(f" > {item} £{itemPrice}")
   # bruker while true loop og breaker bare viss du gir et svar som faktisk er i dictionaryet
   while True:
      # .title er en funksjon som når blir brukt på en string kommer til å uppercase hver bokstav i begynnelsen av ordene i stringen
      # og resten av bokstavene i ordene vil være lowercase
      option = input(questionMessage).title()
      if option in dict:
         # returner option for å kunne legge det til i order listen
         return option, dict[option]
      else:
         print("Invalid option. Please select something from the list.")

def orderCoffee():
   # definerer listen med bestillings informasjonen
   order = {}
   # denne keyen er for når brukeren holder på å svare på alle spørsmålene relatert til bestillingen
   # til en kaffe så bruker vi denne til å summere prisen til kaffen 1x
   order["currentItemPrice"] = 0
   # legger til flere av verdiene til bestillingen i order sånn at vi kan senere vise hva som har blitt bestilt
   for orderName, options in coffeeTypeOptions.items():
      # her setter vi order[orderName] og currentItemPrice til å være lik de verdiene som
      # chooseOption returner i rekkefølge basert på hvor verdiene er i return
      order[orderName], currentItemPrice = chooseOption(options["options"], options["questionMessage"], options["optionsMessage"])
      # plusser på de ulike tallene som de ulike delene av bestillingen bestemmer
      order["currentItemPrice"] += currentItemPrice
   # må definere amount før while loopen fordi vi trenger det i sammenligning delen av loopen
   amount = 0
   while amount == 0:
      # try kjører kode på en trygg måte sånn at viss noe i den ikke fungerer krasjer ikke programmet
      # viss programmet krasjer i try vil den kjøre det som står i except
      try:
         # vi bruker abs for å passe på at amount er et positivt tall
         # int gjør stringen som input returner til en intager men viss brukeren ikke har skrevet bare tall så kommer int til å krasje koden
         # det er derfor vi putter den inn i try
         print("\n----------------------------")
         amount = abs(int(input("How many coffees do you want of this type? ")))
      except:
         print("Please input a number.")

   # legger til hvor mange ganger spilleren vil bestille denne kaffen
   order["amount"] = amount
   # legger til bestillingen i orders for når vi skal regne ut total summen av bestillingene og
   # vise hva brukeren har bestilt
   # list.append gjør at en verdi blir lagt til som det siste item
   orders.append(order)

print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("+                                 +")
print("+         The Coffee Shop         +")
print("+             Welcome             +")
print("+                                 +")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

# først be brukeren om å starte bestillingen
# fordi kan ikke spørre brukeren om de vil legge en bestilling til viss de ikke har bestilt noe før 
# då blir de forvirret og det høres feil ut
# og brukeren må jo kunne avslutte bestillingen
# derfor har vi orderCoffee() en gang før while loopen
orderCoffee()

# kommer til å repetere å spørre brukeren om de vil legge til en ny bestilling til de takker nei
while True:
   # .lower konverterer stringen som input returner til å være lower case sånn at choice kan være == "yes"
   choice = input("\n----------------------------\nWould you like to add another order? Yes/no: ").lower()
   if choice == "yes":
      orderCoffee()
   else:
      break

# variable for den totale prisen av brukeren sin bestilling
price = 0
print("\n----------------------------")
# looper igjennom bestillingene for å regne samme prisen og vise brukeren alle tingene de bestilte i en fin liste
for order in orders:
   # legger til i den totale prisen hva kaffene som er prisen for en kaffe * mengden med kaffeer bestilt
   price += order['currentItemPrice'] * order['amount']
   # order[takeAwayOptions] == 'Yes' and 'Take Away' sjekker om order[takeAwayOptions] er faktisk Yes viss det er det
   # så vil stringen "Take Away" bli brukt men viss order[takeAwayOptions] ikke er Yes då blir stringen "Eat In" brukt
   # bruker ' isteden for " for strings som er inni hoved f stringen fordi du kan ikke ha de samme string tingene inni hverandre
   print(f"{order['menu']} {order['coffeeSizes']} {(order['takeAwayOptions'] == 'Yes' and 'Take Away') or 'Eat In'} Price: ${order['currentItemPrice']} {order['amount']}x")

print("----------------------------")
# konverterer price til en string med str() sånn at vi kan legge den til i stringen til print
print("Total Cost: £" + str(price))