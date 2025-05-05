import sys
from modules import port_scanner, brute_forcer, banner_grabber, dir_fuzzer
from colorama import Fore, Style

def main():
    print(Fore.CYAN + "\nPenetration Testing Toolkit" + Style.RESET_ALL)
    print("Select a module:")
    print("1. Port Scanner")
    print("2. Brute-Forcer")
    print("3. Banner Grabber")
    print("4. Directory/File Fuzzer")
    print("0. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        port_scanner.run()
    elif choice == '2':
        brute_forcer.run()
    elif choice == '3':
        banner_grabber.run()
    elif choice == '4':
        dir_fuzzer.run()
    elif choice == '0':
        print("Exiting.")
        sys.exit(0)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main() 