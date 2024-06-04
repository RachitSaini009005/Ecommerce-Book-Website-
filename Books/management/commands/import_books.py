# myapp/management/commands/import_books.py
import json
from django.core.management.base import BaseCommand
from Books.models import Books_author_book_registration

class Command(BaseCommand):
    help = 'Import books from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to the JSON file')

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']
        with open(json_file, 'r') as file:
            books_data = json.load(file)
            for book_data in books_data:
                book = Books_author_book_registration.objects.create(
                    title=book_data['title'],
                    authors=book_data['authors'],
                    isbn=book_data['isbn'],
                    description=book_data['description'],
                    genre=book_data['genre'],
                    publication_date=book_data['publication_date'],
                    price=book_data['price'],
                    cover_image=book_data['cover_image'],
                    publisher=book_data['publisher'],
                    language=book_data['language'],
                    pageno=book_data['pageno'],
                    format=book_data['format'],
                    edition=book_data.get('edition', ''),  # Handle optional field
                    keywords=book_data['keywords'],
                    availability=book_data['availability']
                )
                self.stdout.write(self.style.SUCCESS(f'Successfully imported book: {book.title}'))
