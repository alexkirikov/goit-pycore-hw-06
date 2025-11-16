from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        self.validate(value)
        super().__init__(value)

    @staticmethod
    def validate(value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must contain exactly 10 digits.")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # --- Додавання телефону --- #
    def add_phone(self, phone):
        new_phone = Phone(phone)
        self.phones.append(new_phone)

    # --- Видалення телефону --- #
    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return True
        return False

    # --- Пошук телефону --- #
    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    # --- Редагування телефону --- #
    def edit_phone(self, old, new):
        phone_obj = self.find_phone(old)
        if phone_obj:
            phone_obj.value = Phone(new).value
            return True
        return False

    def __str__(self):
        phones = "; ".join(phone.value for phone in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones}"


class AddressBook(UserDict):

    # --- Додавання запису --- #
    def add_record(self, record):
        self.data[record.name.value] = record

    # --- Пошук запису --- #
    def find(self, name):
        return self.data.get(name)

    # --- Видалення запису --- #
    def delete(self, name):
        if name in self.data:
            del self.data[name]
