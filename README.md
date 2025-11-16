#  goit-pycore-hw-06 - Address Book 

This project implements a simple **Address Book system** using Object-Oriented Programming principles in Python.
It includes entities for contacts, phone validation, records management, and a collection class for storing and searching records.

The project also comes with a full suite of **unit tests** to ensure all functionality works as expected.

---

## Structure

```
project/
│
├── address_book.py     # Main implementation
├── tests.py# Unit tests (unittest)
└── README.md
```

---

## Features

### **Field Classes**
- `Field` — base class for all fields.
- `Name` — represents a contact’s name.
- `Phone` — represents a phone number with validation (must contain exactly **10 digits**).

### **Record**
Stores:
- a `Name` instance
- a list of `Phone` objects

Supports:
- `add_phone()`
- `remove_phone()`
- `edit_phone()`
- `find_phone()`

### **AddressBook**
Extends `UserDict` and supports:
- `add_record()`
- `find()`
- `delete()`

---

## Example Usage

```python
from address_book import AddressBook, Record

# Create book
book = AddressBook()

# Create John record
john = Record("John")
john.add_phone("1234567890")
john.add_phone("5555555555")

book.add_record(john)

# Edit John phone
john.edit_phone("1234567890", "1112223333")

print(john)
# Output: Contact name: John, phones: 1112223333; 5555555555

# Find a specific phone
found = john.find_phone("5555555555")
print(found.value)   # 5555555555

# Delete another record
book.delete("Jane")
```

---

## Running the Tests

Unit tests are located in:

```
tests.py
```

### Run all tests:

```bash
python -m unittest tests.py
```

or simply:

```bash
pytest
```

(if `pytest` is installed)

The test suite covers:

✔ Phone validation  
✔ Adding/removing/editing phones  
✔ Searching phones  
✔ Adding/finding/deleting records in AddressBook  
✔ Edge cases (invalid phone formats, missing entries)

---

## Requirements

- Python **3.10+**
- No external libraries required — everything uses the Python standard library.

---

## License

This project is free to use for educational purposes.
