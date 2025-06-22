# At least 7 to 10 sentences. At least one multi-line comment.
"""
A customer enters a bookstore and finds themself in the fiction isle. 
The isle contains 5 different series and they end up picking out some 
books. They then notice a computer fron their peripheral vision and log 
into the store's website. The website presents a list of series and asks
the user to select one of them. After the user selects a series the 
website asks which book from it they would like to purchase. The user 
will then confirm their decision or select another series if they 
misclicked. After completing their selection of books the user will exit
the website and a receipt will be presented to them.
"""
# At least one constant
BOOKSTORE = "Gurtle's Bookstore"  # random name I chose
COST = 20  # each book costs $20

# Pick any ONE of the following to include in your program: Dictionary
series = {
    1: 'Harry Potter (7 books)',
    2: 'Percy Jackson (5 books)',
    3: 'Twilight (4 books)',
    4: 'Throne of Glass (7 books)',
    5: 'Five Kingdoms (5 books)'}

# Books in Harry Potter series
series1 = [
  "Harry Potter and the Sorcerer’s Stone",
  "Harry Potter and the Chamber of Secrets",
  "Harry Potter and the Prisoner of Azkaban",
  "Harry Potter and the Goblet of Fire",
  "Harry Potter and the Order of the Phoenix",
  "Harry Potter and the Half-Blood Prince",
  "Harry Potter and the Deathly Hallows"]

# Books in Percy Jackson series
series2 = [
  "The Lightning Thief",
  "The Sea of Monsters",
  "The Titan’s Curse",
  "The Battle of the Labyrinth",
  "The Last Olympian"]

# Books in Twilight series
series3 = [
  "Twilight",
  "New Moon",
  "Eclipse",
  "Breaking Dawn"]

# Books in Throne of Glass series
series4 = [
  "Throne of Glass",
  "Crown of Midnight",
  "Heir of Fire",
  "Queen of Shadows",
  "Empire of Storms",
  "Tower of Dawn",
  "Kingdom of Ash"]

# Books in Five Kingdoms series
series5 = [
  "Sky Raiders",
  "The Rogue Knight",
  "Crystal Keepers",
  "Death Weavers",
  "Time Jumpers"]

# At least THREE functions
def currency(value):
  # Money formating
  return "${:,.2f}".format(value)

# Select a series you enjoy
def bookSeries(series):
  # At least one loop -- if in the 2nd assignment, you use the WHILE
  # loop in your program, you must code the FOR loop
  # List the book series
  for i in series:
    print(f"{i}: {series[i]}")

  # Selects which series to look into
  seriesChoice = int(input("Choose a series (1-5): "))
  if seriesChoice < 1 or seriesChoice > 5:
    print("\nInvalid book series range.\n")
    return bookSeries(series)

  # Return selected series
  match seriesChoice:
    case 1: # Harry Potter
      return series1
    case 2: # Percy Jackson
      return series2
    case 3: # Twilight
      return series3
    case 4: # Throne of Glass
      return series4
    case 5: # Five Kingdoms
      return series5

# Select a book to purchase
def bookChoice(seriesChoice):
  for i in range(0, len(seriesChoice)):
    print(f"{i + 1}: {seriesChoice[i]}")

  # The series the user chose will lead to its respective match case
  # which will print the book based on the chosen book number
  while True:
    # Selects which book to look into (based on book order)
    book = input("Which book of this series would you like (ex. 1): Book ")
    book = int(book)
    if book < 1:
      print("\nNumber too small\n")
    elif book > len(seriesChoice):
      print("\nNumber too large\n")
    else:
      break

  bookHolder = seriesChoice[book - 1]
  print(f"That would be: {bookHolder}")

  # Confirm purchase
  purchase = input("Would you like to confirm your purchase? (y/n): ").lower()
  if purchase == "y":
    print("Thank you for your purchase!")
    # If the user bought something the price will be $20/COST
    return [COST, bookHolder]
  # If the user didn't buy anything the price would still be $0
  return [0, bookHolder]

# PROGRAM OFFICIALLY STARTS HERE
# Prints a happy message
print(f"Welocome to {BOOKSTORE} what can I get for you today?")
# Initialize variable
bank = 0
# List of purchaces
purchases = []
# Making an infinite loop
while True:
  # Calls forth the bookSeries function
  seriesChoice = bookSeries(series)
  # Calls on the bookChoice function and extracts values
  profit, bookHolder = bookChoice(seriesChoice)
  bank += profit
  # If the user bought something add it to the receipt
  if profit > 0:
    # Name of book and price
    purchases.append(f'{bookHolder} - {currency(profit)}')
  # Give the user a way to exit the loop
  exit = input("Tap 'e' to exit or anything else to continue: ")
  if exit == "e":
    break

# Create receipt for a new user
file = open('receipt.txt', 'w')
file.write(f'Receipt from {BOOKSTORE}')
# Sort purchases
purchases.sort()
# Find higest cost
print('Higherst cost:', max(purchases)) # Currently all books cost same
# Find lowest cost
print('Lowest cost:', min(purchases)) # If prices change in the future

for purchase in purchases:
  file.write(purchase + '\n')

# Prints the total price
file.write(f'\n\nTotal - {currency(bank)}')
file.close()

# Read using the with method
with open('receipt.txt', 'r') as file:
  # Display the receipt
  print('\n' + file.read())

# A goodbye message
print(f"\nThank you for visiting {BOOKSTORE}!")