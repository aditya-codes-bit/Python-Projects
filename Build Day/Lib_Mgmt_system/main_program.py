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

while True:
    menu()
    choice = input("Enter Your Choice From 1 To 6 ::")
    if choice == "1":
        print("Add Book")
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