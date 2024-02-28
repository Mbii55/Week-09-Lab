import unittest
from book_manager import Book, BookManager

class TestBookManager(unittest.TestCase):
    def setUp(self):
        self.manager = BookManager()
        
        self.book1 = Book("ISBN1", "Social Machines", "Vanilson")
        self.book2 = Book("ISBN2", "An Architecture and Guiding Framework for the Social Enterprise", "Vanilson")
        self.book3 = Book("ISBN3", "Introduction to Python", "Mohamed")
        
        self.manager.add_book(self.book1)
        self.manager.add_book(self.book2)

    def test_add_book(self):
        self.manager.add_book(self.book3)
        self.assertIn(self.book3, self.manager.list_books(), "Book3 should be added to the manager.")

    def test_preventing_duplicate_isbn(self):
        duplicate = Book("ISBN1", "New Title", "New Author") 
        self.manager.add_book(duplicate)
        self.assertEqual(len(self.manager.list_books()), 2, "No additional book should be added.")
        self.assertIn(self.book1, self.manager.list_books(), "Original book should remain in the manager.")

    def test_remove_book_by_isbn(self):
        self.manager.remove_book("ISBN1")
        self.assertNotIn(self.book1, self.manager.list_books(), "Book1 should be removed from the manager.")

    def test_list_books(self):
        self.assertIn(self.book1, self.manager.list_books(), "Book1 should be listed.")
        self.assertIn(self.book2, self.manager.list_books(), "Book2 should be listed.")
        self.assertEqual(len(self.manager.list_books()), 2, "There should be exactly 2 books listed.")

if __name__ == '__main__':
    unittest.main()
