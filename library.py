
import json
import os

FILE_NAME = "books.json"


def load_books():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        return []


def save_books(books):
    with open(FILE_NAME, "w") as file:
        json.dump(books, file, indent=4)


def add_book(books):
    book_id = input("Enter Book ID: ").strip()

    if not book_id or any(book["id"] == book_id for book in books):
        print("Invalid or duplicate Book ID!")
        return

    title = input("Enter Book Title: ").strip()
    author = input("Enter Author Name: ").strip()

    if not title or not author:
        print("Title and author cannot be empty!")
        return

    books.append({
        "id": book_id,
        "title": title,
        "author": author,
        "issued": False
    })

    save_books(books)
    print("Book added successfully!")


def view_books(books):
    if not books:
        print("No books found.")
        return

    print("\n--- Book Records ---")
    for book in books:
        status = "Issued" if book["issued"] else "Available"
        print(
            f'ID: {book["id"]} | Title: {book["title"]} | '
            f'Author: {book["author"]} | Status: {status}'
        )


def search_book(books):
    keyword = input("Enter Book ID or Title: ").strip().lower()

    matches = [
        book for book in books
        if keyword == book["id"].lower()
        or keyword in book["title"].lower()
    ]

    if matches:
        for book in matches:
            status = "Issued" if book["issued"] else "Available"
            print(book["id"], book["title"], book["author"], status)
    else:
        print("Book not found.")


def issue_book(books):
    book_id = input("Enter Book ID to issue: ").strip()

    for book in books:
        if book["id"] == book_id:
            if book["issued"]:
                print("This book is already issued.")
            else:
                book["issued"] = True
                save_books(books)
                print("Book issued successfully!")
            return

    print("Book ID not found.")


def return_book(books):
    book_id = input("Enter Book ID to return: ").strip()

    for book in books:
        if book["id"] == book_id:
            if not book["issued"]:
                print("This book is already available.")
            else:
                book["issued"] = False
                save_books(books)
                print("Book returned successfully!")
            return

    print("Book ID not found.")


def main():
    books = load_books()

    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book(books)
        elif choice == "2":
            view_books(books)
        elif choice == "3":
            search_book(books)
        elif choice == "4":
            issue_book(books)
        elif choice == "5":
            return_book(books)
        elif choice == "6":
            print("Thank you for using the Library System!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
