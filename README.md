
# Python Labs

This project contains three Python lab assignments that demonstrate structured programming, object-oriented design, file handling, data serialization, and basic business logic implementation.

---

## Lab 2 - **Bookstore Purchase System** (`HW2/hw2.py`)

### Business Scenario

The project simulates an online **Bookstore** experience where a customer can browse series, select individual books, confirm purchases, and receive a formatted receipt.

### Core Logic

- **Book Catalog**
  - 5 series of books are defined using either a dictionary (Lab 2).
  - Series include *Harry Potter*, *Percy Jackson*, *Twilight*, *Throne of Glass*, *Five Kingdoms*.

- **Functions**
  - `currency(value)`: Formats a float to USD currency style.
  - `bookSeries(series)`: Displays series and allows user to select one.
  - `bookChoice(seriesChoice)`: Displays books in the selected series, asks user to pick a book and confirm purchase.

- **Purchase Flow**
  - Infinite `while` loop keeps the user shopping until they choose to exit.
  - Purchases are recorded to a `receipt.txt` file.
  - Displays highest and lowest cost purchase (future proof if book prices vary).
  - Total amount is displayed at the end.

### Features

✅ User interaction  
✅ Loops and conditionals  
✅ File writing and reading (`receipt.txt`)  
✅ Sorting purchases  
✅ User-friendly prompts

---

## Lab 3 - **Device Management & Data Handling** (`HW3/hw3.py`)

### Business Scenario

This assignment implements a **Device Management System** with Object-Oriented Programming and demonstrates data handling using various Python data structures and file formats.

### Core Logic

### Part 1 - Object-Oriented Printer Class

- Defines `Printer` class with attributes:
  - `isColor`
  - `is3D`
  - `isNetwork`
- Methods:
  - `deviceName(name)`
  - `configuration()`
- Demonstrates creating and displaying multiple printer configurations.

### Part 2 - List Operations

- User builds a list of computer output devices.
- Supports dynamic insertions and slicing.
- Converts list to tuple and demonstrates tuple usage.

### Part 3 - Text File Handling

- Writes the list of devices to `device.txt`.
- Adds additional devices using `with open`.
- Reads back data and counts lines.

### Part 4 - Dictionary + Data Serialization

- Simulates a **Track Meet Registry** with:
  - `school_year` dictionary
  - `last_names` dictionary
  - `entry_fees` dictionary
- Allows user to query based on uniform number.
- Saves `last_names` dictionary using:
  - Pickle (`.txt`)
  - JSON (`.json`)
  - CSV (`.csv`)
- Demonstrates reading back each format.

### Part 5 - Set Operations

- Builds a set of devices.
- Updates the set with letters of a favorite sport.
- Demonstrates safe vs. unsafe removal methods.

---

## Key Concepts Demonstrated

- **Control Flow**: Loops, Conditionals, Functions
- **OOP**: Class design and instance methods
- **File I/O**: Text, CSV, JSON, Pickle
- **Data Structures**: Lists, Tuples, Dictionaries, Sets
- **Exception Handling** (partially in set management)
- **User Interaction**: CLI-based

---

## How to Run

You can run each Python file individually:

```bash
# Run HW 2 Bookstore App
python "HW2/hw2.py"

# Run HW 3 Device Management App
python HW3/hw3.py
```

Python 3.x is required.
