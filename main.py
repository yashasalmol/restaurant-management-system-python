from admin import admin_menu
from user import user_menu
from RestaurantMenu import RestaurantMenu

def main():
    try:
        menu = RestaurantMenu()

        while True:
            print("\n----Welcome to Restaurant Management System----")
            print("1. Admin")
            print("2. User")
            print("3. Exit")
            option = int(input("Enter option: "))

            if option == 1:
                admin_menu(menu)
            elif option == 2:
                user_menu(menu)
            elif option == 3:
                print("Thanku! come again")
                break
            else:
                print("Invalid option! Please try again.")
    except ValueError:
        print("Value Error!")

# Ensure that the progrm start from the main function
if __name__ == "__main__":
    main()