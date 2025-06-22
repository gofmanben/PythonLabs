# Third Assignment -- Python program

import csv
import json
import pickle
import random

# *******************************************************************
# Part 1 - OOP
# *******************************************************************

print('\nPart 1 - OOP\n')


# Code a Python program to define a specific computer output device
# (such as printer, scanner, etc.) as a class.
# Make sure the name of the class starts with a capital letter.
class Printer:  # Also, note the colon at the end. Example:  class Printer:
  # Main method
  def __init__(self, isColor, is3D, isNetwork):
    # The printer can be black and white or colored
    self.isColor = isColor
    # The printer can be 3D
    self.is3D = is3D
    # Can be connected to the wifi or local network by cable
    self.isNetwork = isNetwork

  # Include at least two methods (come up with your own methods) in your program.
  def deviceName(self, name):
    print(f'\n{name} Printer')

  # Generate an output with information regarding the properties and methods.
  def configuration(self):
    if self.isColor:
      print('Has Color')
    if self.is3D:
      print('3D Printer')
    if self.isNetwork:
      print('Has Wifi Connection')
    if not self.isColor and not self.is3D and not self.isNetwork:
      print("Basic Printer")


# Black and white, not 3D, uses local network
cheapPrinter = Printer(False, False, False)
cheapPrinter.deviceName('Home')
cheapPrinter.configuration()

# my home printer has color and WiFi Connection
colorPrinter = Printer(True, False, True)
colorPrinter.deviceName('Office')
colorPrinter.configuration()

# my 3D Printer is colorful but using only Micro Card
printer3D = Printer(True, True, False)
printer3D.deviceName('3D')
printer3D.configuration()

# *******************************************************************
# Part 2 - LIST
# *******************************************************************

print('\nPart 2 - LIST\n')

list = []
# make a list of 6 computer output devices
for _ in range(6):
  # Use a WHILE or FOR loop to create the computer output devices in
  # the list. Ask the user to enter data.
  list.append(input("Enter a computer output devices: "))
  # printer, scanner, keyboard, mouse, monitor, speaker; projector; headphones
# Print the list.
print(list)

# Add a 7th  computer output device to the list. The 7th computer
# output device should be located between the 4th and 5th computer
# output devices in the list.
list.insert(4, input("Enter another computer output device: "))
# Print the list.
print(list)
# Then print only the 5th to 6th computer output devices.
print(list[4:6])

# Add the 8th computer output device to the end of the list.
list.append(input("Enter one last computer output device: "))
# Print only the last computer output device on the list.
print(f'Last device: {list[-1]}')

# Print the number of computer output devices,
print(f'Number of devices: {len(list)}')
# the max, ascii code: https://www.prepbytes.com/blog/general/ascii-values-of-alphabet/#:~:text=ASCII%20Code%20of%20A%20to%20Z,-The%20ASCII%20code&text=Each%20character%20is%20associated%20with,to%20122%20for%20lowercase%20letters.
print(f'Highest 1st letter ascii code: {max(list)}')
# and the min values on the list.
print(f'Lowest 1st letter ascii code: {min(list)}')

# Change the list to a tuple.
list = tuple(list)
# Print the tuple.
print(list)

# *******************************************************************
# Part 3 - TEXT FILE
# *******************************************************************

print('\nPart 3 - TEXT FILE\n')

# Using the list you created in the previous program.
prList = list

# Using the open and close files statement, populate a .txt file (name
# the .txt file: device.txt) that contains the computer output devices
file = open('device.txt', 'w')

# There should be 8 lines in the file, containing the 8 computer output devices.
for item in prList:
  # Print out the data in the file.
  file.write(str(item) + '\n')
  print(item)
file.close()

# Using the with method, add three more computer output devices to the .txt file.
with open('device.txt', 'a') as file:
  for index in range(3):
    # microphone, controller, USB
    device = input('Enter a new computer output device: ')
    # Print out the data in the .txt file.
    file.write(device)
    if index < 2:
      file.write('\n')  # a new line
# Now you have 11 values.

with open('device.txt', 'r') as file:
  # Reading from the .txt file,
  content = file.read()
  # print out the # of computer output devices from the .txt file.
  print(content)

  list = content.split('\n')
  # The number in the output should be 11
  print(f'The number of lines in the file: {len(list)}')

# *******************************************************************
# Part 4 - DICTIONARY
# *******************************************************************

print('\nPart 4 - DICTIONARY\n')

academic = ('freshman', 'sophomore', 'junior', 'senior')
Lname = ('Jolie', 'Pitt', 'DiCaprio', 'Cruise', 'Gofman')
uniformLen = len(Lname)

school_year = {}
last_names = {}
entry_fees = {}
for uniform_number in range(uniformLen):
  # Write a program that creates a dictionary containing 5 track uniform numbers for
  # runners in a race and the school year
  school_year[uniform_number] = random.choice(academic)
  # The program should also create a dictionary containing 5 track uniform numbers for
  # runners in a race and only the last names of the runners in the competition.
  last_names[uniform_number] = Lname[uniform_number]
  # The program should also create a dictionary containing 5 track uniform numbers for
  # runners in a race and entry fee they paid to enter the competition.
  # Assume the runners pay different fees based on the # of competitions they entered.
  entry_fees[uniform_number] = f'${random.randrange(10, 100, 10):,.2f}'
  # each event costs $10 and there are 10 events total

# Print dictionaries
print('School Years:', school_year)
print('Last Names:', last_names)
print('Entry Fees:', entry_fees)

while True:
  # The program should let the user enter a track uniform number
  uniform_number = input(
      f'Enter the track uniform number 0-{uniformLen - 1}: ')
  if not uniform_number.isdigit():
    # If the user enters the incorrect track uniform number, display an error message.
    print("Invalid input. Please enter a numeric value.")
    # Keep giving the user the opportunity to enter
    continue

  # the correct track uniform number until the correct number is entered.
  uniform_number = int(uniform_number)
  if uniform_number < 0 or uniform_number >= uniformLen:
    # If the user enters the incorrect track uniform number, display an error message.
    print("Invalid uniform number range")
    # Keep giving the user the opportunity to enter
    continue

  # then it should display the school year, last name, and entry fee.
  print(f"School Year: {school_year[uniform_number]}")
  print(f"Last Name: {last_names[uniform_number]}")
  print(f"Entry Fee: {entry_fees[uniform_number]}")

  # Make sure all the prompts are clear and descriptive so the user will not have to
  # guess what to enter.
  q = input('Press (Y/y) to continue or any other key to exit: ')
  if q != 'Y' and q != 'y':
    break

print('Thanks for running a race\n')

# choose one of the dictionaries you created above and save it to a file using the
# three methods on the website.
# Save the dictionary to a text file.
with open('last_names.txt', 'wb') as fp:
  pickle.dump(last_names, fp)

with open('last_names.json', "w") as fp:
  # Use the dump() method of a json module to write a dictionary in a json file.
  json.dump(last_names, fp)

# Write the dictionary to a CSV file.
with open('last_names.csv', 'w', newline='') as fp:
  writer = csv.writer(fp)
  # writer.writerow(['uniform_number', 'last_name'])  # Write header
  for key, value in last_names.items():
    writer.writerow([key, value])

#Make sure you read from the file for each of the 3 techniques.
with open('last_names.txt', 'rb') as fp:
  print('pickle output:', pickle.load(fp))

with open('last_names.json', 'r') as fp:
  print('json output:', json.load(fp))

with open('last_names.csv', 'r') as infile:
  reader = csv.reader(infile)
  # next(reader)  # Skip header
  csv_data = {rows[0]: rows[1] for rows in reader}
  print('csv output:', csv_data)

# *******************************************************************
# Part 5 - SET
# *******************************************************************

print('\nPart 5 - SET\n')

# Create a set called deviceset with elements of five computer output devices.
# You can make up the computer output devices.
deviceset = {'printer', 'scanner', 'keyboard', 'mouse', 'monitor'}

# Print the set.
print(deviceset)
# Print the number of elements in deviceset.
print(f'Number of devices: {len(deviceset)}')

# you code the entire word, such as “football" not individual letters:
# f, o, o, t, b, a, l, l.
favoriteSport = 'football'

# Use a method to add the letters of one of your favorite sports
# (basketball, football, etc.) to devicese
deviceset.update(favoriteSport)

# and print the set.
print(deviceset, '\n')

devices = []
letters = []
for value in deviceset:
  # 1 character
  if len(value) == 1:
    # The output will have the individual f, o, t, b, a, l
    letters.append(value)
  else:
    # in addition to the computer output devices
    devices.append(value)

print(f'Devices: {devices}')
print('Favorite sport: ', end='')
# Print the characters in the original order
for char in favoriteSport:
  if char in letters:
    # Prints the respective character in the favorite sport (variable)
    print(char, end=',')
    # Removes the character from letters (variable) to avoid duplication
    letters.remove(char)

print('\nTry to remove letter q ...\n')
# Use a method to delete the letter q in deviceset raising an exception.
deviceset.remove('q')

# Use a method to delete the letter q in deviceset without raising an exception.
deviceset.discard('q') # won't be executed due to previous exception
