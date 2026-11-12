from colorama import Fore, Back, Style, init

def menu():
    init(autoreset=True)
    print(Fore.CYAN + '''╔══════════════════════════════════════════════╗
║                                              ║
║        📚  LIBRARY MANAGEMENT SYSTEM  📚     ║
║                                              ║
╚══════════════════════════════════════════════╝''')
    print(Fore.GREEN + '''1. Add Book
2. View Books
3. Search Book
4. Register User
5. Issue Book
6. Exit''')

def read_book():
    with open(r"C:\Users\Aditya Misal\Desktop\build\book_data.txt", "r") as file:
        book_data = file.readline()
    return book_data

def add_book():
    """This is function where it takes Book Id, Book Name, Author, Quantity, as Input"""
    book_data = read_book()
    print(Fore.GREEN + "--- ADD BOOK ---")
    while True:
        book_id = input("Enter Book Id ::").strip()
        if book_id.isdigit():
            book_id = int(book_id)
            break
        else:
            print(Fore.RED + "Invalid Book Id It Should Be A Number Only.")

    book_name = input("Enter The Book Name ::")
    book_author = input("Enter Author Name ::")
    while True:
        book_quantity = input("Enter Quantity ::").strip()
        if book_quantity <= "0":
            print(Fore.RED + "Please Enter a Valid Quantity.") 
        elif book_quantity.isdigit():
            book_quantity = int(book_quantity)
            break
        else:
            print(Fore.RED + "Please Enter A Valid Input.")
    print(Fore.GREEN + f'{"Book Added Successfully.":^100}')

    with open("book_data.txt", "a") as file:
        file.write(f"{book_id}, {book_name}, {book_author}, {book_quantity} \n")


while True:
    menu()
    choice = input("Enter Your Choice From 1 To 6 ::")
    if choice == "1":
        add_book()
    elif choice == "2":
        print("View Book")
    elif choice == "3":
        print("Search Book")
    elif choice == "4":
        print("Register Book")
    elif choice == "5":
        print("Issue Book")
    elif choice == "6":
        print(Fore.YELLOW + "Thank You for using our System Vist Again!")
        break
    else:
        print(Fore.RED + "Invalid Choice")