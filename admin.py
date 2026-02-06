from RestaurantMenu import RestaurantMenu

def admin_menu(menu):
        uid = input("Enter user ID: ")
        pass1 = input("Enter password: ")
        if uid == "yash" and pass1 == "1234":
            try:
                while True:
                    print("\n-----Admin Menu-----")
                    print("1. Add Food")
                    print("2. Display Food")
                    print("3. Update Food")
                    print("4. Delete Food")
                    print("5. Total Revenue")
                    print("6. Exit")
                    choice = int(input("Enter Choice: "))

                    if choice == 1:
                        menu.add_food()
                    elif choice == 2:
                        menu.display_food()
                    elif choice == 3:
                        menu.update_food()
                    elif choice == 4:
                        menu.delete_food()
                    elif choice == 5:
                        menu.revenue()
                    elif choice == 6:
                        break
                    else:
                        print("Invalid choice! Please try again.")
            except ValueError:
                print("Value Error")
        else:
            print("Invalid user ID or Password")