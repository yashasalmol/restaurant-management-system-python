from RestaurantMenu import RestaurantMenu

def user_menu(menu):
    try:
        while True:
            print("\n-----User Menu-----")
            print("1. Display Food")
            print("2. Place Order")
            print("3. View Order")
            print("4. Total Bill")
            print("5. Exit")

            choice = int(input("Enter Choice: "))
            if choice == 1:
                menu.display_food()
            elif choice == 2:
                menu.place_order()
            elif choice == 3:
                menu.view_order()
            elif choice == 4:
                menu.total_bill()
            elif choice == 5:
                print("Exit userr menu")
                break
            else:
                print("Invalid choice! Please try again.")
    
    except ValueError:
        print("Value Error!")