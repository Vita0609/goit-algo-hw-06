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
        super().__init__(value)
        if len(value) != 10 or not value.isdigit():
             raise ValueError("Номер повинен містити 10 цифр")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, number):
        self.phones.append(Phone(number))

    def remove_phone(self, remnum):
        for phone in self.phones:
            if phone.value == remnum:
                 self.phones.remove(phone)
                 return print(f"Запис з номером '{remnum}' видалено.")
        return print(f"Запис з номером '{remnum}' не знайдено.")

    def edit_phone(self, oldnum, newnum):
        if len(newnum) != 10 or not newnum.isdigit():
            raise ValueError("Номер повинен містити 10 цифр")
        else:
            for phone in self.phones:
                if phone.value == oldnum:
                    phone.value = newnum
                    return
                raise ValueError(f"Номер '{oldnum}' не знайдено.")
             

    def find_phone(self, phone):
        for el in self.phones:
             if el.value == phone:
                  return el
        return None

    def __str__(self):
        phone_numbers = '; '.join(p.value for p in self.phones)
        return f"{self.name}: {phone_numbers}"

class AddressBook(UserDict):
    def add_record(self, record):
        key = record.name.value
        self.data[key] = record
    
    def find(self, neededname):
        return self.data.get(neededname)

    def delete(self, rem):
        if rem in self.data:
            del self.data[rem]
        else:
            print(f"Запис з ім'ям '{rem}' не знайдено.")
    
    def __str__(self):
        records = '\n'.join(f"{record}" for name, record in self.data.items())
        return f"Address Book:\n{records}"


book = AddressBook()

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

print(book)

john = book.find("John")
if john:
    john.edit_phone("1234567890", "1112223333")
    print(john)

    found_phone = john.find_phone("5555555555")
    print(f"{john.name.value}: {found_phone}")

book.delete("Jane")
print(book)