import csv
import re
from unidecode import unidecode
from django.core.management.base import BaseCommand
from book.models import Book


class Command(BaseCommand):
    """Import books from a CSV file into the Book model
    """

    def find_non_utf8_characters(self, file_path):
        """Dictionary to store problematic characters and their replacements
        """
        non_ascii_chars = {}

        with open(file_path, mode='r', encoding='ISO-8859-1') as file:
            reader = csv.reader(file, delimiter=';')
            for line_num, row in enumerate(reader, start=1):
                for field in row:
                    non_ascii = re.findall(r'[^\x00-\x7F]', field)
                    for char in non_ascii:
                        if char not in non_ascii_chars:
                            replacement = unidecode(char)
                            non_ascii_chars[char] = replacement

        return non_ascii_chars

    def replace_non_utf8(self, text, non_utf8_chars):
        for original, replacement in non_utf8_chars.items():
            text = text.replace(original, replacement)
        return text

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        non_utf8_chars = self.find_non_utf8_characters(csv_file)
        
        with open(csv_file, mode='r', encoding='ISO-8859-1') as file:
            reader = csv.DictReader(file, delimiter=';')
            books_created = 0

            for row in reader:
                print(f"\rLoading Book # {books_created}", end="")
                try:
                    isbn = self.replace_non_utf8(row['ISBN'], non_utf8_chars)
                    book_title = self.replace_non_utf8(row['Book-Title'], non_utf8_chars)
                    book_author = self.replace_non_utf8(row['Book-Author'], non_utf8_chars)
                    publication_year = self.replace_non_utf8(row['Year-Of-Publication'], non_utf8_chars)
                    publisher = self.replace_non_utf8(row['Publisher'], non_utf8_chars)

                    book, created = Book.objects.update_or_create(
                        isbn=isbn,
                        defaults={
                            'book_title': book_title,
                            'book_author': book_author,
                            'publication_year': publication_year,
                            'publisher': publisher,
                        }
                    )
                    if created:
                        books_created += 1
                except Exception as e:
                    print(f"\nERROR LOADING {book_title}: {e}")

        self.stdout.write(self.style.SUCCESS(f"Successfully imported {books_created} books."))
