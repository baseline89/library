from faker import Faker
from books.models import Book
from authors.models import Author

fake = Faker()

# Insert 6 authors
authors = []
for _ in range(6):
    author = Author.objects.create(
        name=fake.name(),
        dob=fake.date_of_birth().strftime("%Y-%m-%d")
    )
    authors.append(author)

# Insert 6 books for each author
for author in authors:
    for _ in range(6):
        book = Book.objects.create(
            title=fake.sentence(nb_words=4),
            pubdate=fake.date_between(start_date="-1y", end_date="today").strftime("%Y-%m-%d"),
            author=author
        )


# 
# Retrieve all authors
all_authors = Author.objects.all()
print("Authors:")
for author in all_authors:
    print(author.name, "-", author.dob)

# Retrieve all books
all_books = Book.objects.all()
print("\nBooks:")
for book in all_books:
    print(book.title, "-", book.pubdate, "-", book.author.name)
