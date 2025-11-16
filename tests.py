import unittest
from address_book import Field, Name, Phone, Record, AddressBook


class TestFieldClasses(unittest.TestCase):

    def test_name_creation(self):
        n = Name("John")
        self.assertEqual(n.value, "John")

    def test_phone_valid(self):
        p = Phone("1234567890")
        self.assertEqual(p.value, "1234567890")

    def test_phone_invalid_length(self):
        with self.assertRaises(ValueError):
            Phone("12345")

    def test_phone_invalid_chars(self):
        with self.assertRaises(ValueError):
            Phone("12345abcde")


class TestRecord(unittest.TestCase):

    def setUp(self):
        self.record = Record("John")

    def test_add_phone(self):
        self.record.add_phone("1234567890")
        self.assertEqual(len(self.record.phones), 1)
        self.assertEqual(self.record.phones[0].value, "1234567890")

    def test_remove_phone(self):
        self.record.add_phone("1234567890")
        self.record.add_phone("5555555555")
        removed = self.record.remove_phone("5555555555")
        self.assertTrue(removed)
        self.assertEqual(len(self.record.phones), 1)

    def test_remove_phone_not_found(self):
        self.record.add_phone("1234567890")
        removed = self.record.remove_phone("1111111111")
        self.assertFalse(removed)

    def test_find_phone(self):
        self.record.add_phone("1234567890")
        phone = self.record.find_phone("1234567890")
        self.assertIsNotNone(phone)
        self.assertEqual(phone.value, "1234567890")

    def test_find_phone_not_found(self):
        self.record.add_phone("1234567890")
        phone = self.record.find_phone("9999999999")
        self.assertIsNone(phone)

    def test_edit_phone(self):
        self.record.add_phone("1234567890")
        self.record.edit_phone("1234567890", "1112223333")
        self.assertEqual(self.record.phones[0].value, "1112223333")

    def test_edit_phone_not_exists(self):
        self.record.add_phone("1234567890")
        result = self.record.edit_phone("9999999999", "1112223333")
        self.assertFalse(result)


class TestAddressBook(unittest.TestCase):

    def setUp(self):
        self.book = AddressBook()
        self.john = Record("John")
        self.john.add_phone("1234567890")

    def test_add_record(self):
        self.book.add_record(self.john)
        self.assertIn("John", self.book.data)

    def test_find_record(self):
        self.book.add_record(self.john)
        rec = self.book.find("John")
        self.assertEqual(rec.name.value, "John")

    def test_find_record_not_exists(self):
        rec = self.book.find("Jane")
        self.assertIsNone(rec)

    def test_delete_record(self):
        self.book.add_record(self.john)
        self.book.delete("John")
        self.assertNotIn("John", self.book.data)

    def test_delete_record_not_exists(self):
        # should not raise exception
        self.book.delete("Someone")
        self.assertEqual(len(self.book.data), 0)


if __name__ == "__main__":
    unittest.main()
