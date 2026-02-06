from Order import Order

class RestaurantMenu:
    
    def __init__(self):
        self.menu_file = "Menu.txt"
        self.order_file = "Order.txt"
        self.revenue_file = "Revenue.txt"


    def add_food(self):
        try:
            f_id = int(input("Enter food ID: "))
            f_name = input("Enter food name: ")
            f_price = int(input("Enter food price: "))

            if f_price <= 0:
                print("Price must be greater than zero.")
                return

            order = Order(f_id, f_name, f_price)
            with open(self.menu_file, "a") as f:
                f.write(f"{order.f_id}, {order.f_name}, {order.f_price}\n")
            print("Food added successfully.")
            
        except ValueError:
            print("Invalid input! Please enter a number for ID and Price.")


    def display_food(self):
        try:
            with open(self.menu_file, "r") as f:
                print("\n--- Menu ---")
                for s in f:
                     # Strip any extra spaces or newlines and then split
                    f_id, f_name, f_price = s.strip().split(",")
                    print(f"ID: {f_id} | Name: {f_name} | Price: Rs{f_price}")
        except FileNotFoundError:
            print("Menu file not found.")


    def update_food(self):
        container = []
        found = False
        f_id = int(input("Enter food ID to update: "))
        with open(self.menu_file, "r") as f:
            for o in f:
                list1 = o.strip().split(",")
                if list1[0] == str(f_id):
                    found = True
                    print("1. Food Name")
                    print("2. Food Price")
                    print("3. Both Name and Price")
                    ch = int(input("Enter choice: "))
                    if ch == 1:
                        f_name = input("Enter new name: ")
                        list1[1] = f_name
                    elif ch == 2:
                        f_price = int(input("Enter new price: "))
                        if f_price > 0:
                            list1[2] = str(f_price)
                        else:
                            print("Please enter a positive price.")
                    elif ch == 3:
                        f_name = input("Enter new name: ")
                        list1[1] = f_name
                        f_price = int(input('Enter new price: '))
                        if f_price > 0:
                            list1[2] = str(f_price)
                        else:
                            print("Please enter positive price")
                            break
                    # append the food to container
                    container.append(",".join(list1))
                else:
                    # keep non match record
                    container.append(o.strip())
        
        # Update menu file
        if found:
            with open(self.menu_file, "w") as f:
                for item in container:
                    f.write(item + "\n")
            print("Food updated successfully.")
        else:
            print("Food ID not found.")


    def delete_food(self):
        container = []
        found = False
        f_id = int(input("Enter food ID to delete: "))
        with open(self.menu_file, "r") as f:
            for o in f:
                list1 = o.strip().split(",")
                # f_id does not match keep it menu
                if list1[0] != str(f_id):
                    container.append(o.strip())
                else:
                    print(f"ID: {list1[0]} | Name: {list1[1]} | Price: Rs{list1[2]}")
                    print("Food has been deleted.")
                    # food find and delete
                    found = True
        # while update menu back to file
        if found:
            with open(self.menu_file, "w") as f:
                for item in container:
                    f.write(item + "\n")
        else:
            print("Food ID not found.")


    def place_order(self):
        while True:
            self.display_food() # Show the menu to the user
            f_id = int(input("\nEnter Food ID to place order (0 to stop): "))

            if f_id == 0:
                break # Exit the loop if the user enters 0

            found = False
            with open(self.menu_file, "r") as f:
                for o in f:
                    list1 = o.strip().split(",")
                    # if the f_id  matches
                    if list1[0] == str(f_id):
                        found = True
                        
                        f_qty = int(input(f"Enter quantity for {list1[1]}: "))
                        order = Order(f_id=int(list1[0]), f_name=list1[1], f_price=int(list1[2]), f_qty=f_qty)

                        # Write the order to the order file
                        with open(self.order_file, "a") as f2:
                            f2.write(f"{order.f_id}, {order.f_name}, {order.f_price}, {order.f_qty}\n")

                        # Optionally, add revenue for this order
                        with open(self.revenue_file, "a") as f3:
                            f3.write(f"{order.f_id}, {order.f_name}, {order.f_price * order.f_qty}\n")

                        print(f"Order placed successfully for {order.f_name} with quantity {f_qty}!")
                        break

            if not found:
                print("Food ID not found!")


    def view_order(self):
        try:
            with open(self.order_file, "r") as f:
                print("\n--- Order Summary ---")
                for s in f:
                    f_id, f_name, f_price, f_qty = s.strip().split(",")
                    # Calculate total price for this item
                    total = int(f_price) * int(f_qty)
                    print(f"ID: {f_id} | Name: {f_name} | Price: Rs{f_price} | Quantity: {f_qty} | Total: Rs{total}")
        # If file does not exist, this message will be shown
        except FileNotFoundError:
            print("Order file not found.")


    def revenue(self):
        total_revenue = 0
        try:
            # Open the revenue file to read the total revenue from past orders
            with open(self.revenue_file, "r") as f:
                for line in f:
                    # Each line in the revenue file has the format: f_id, f_name, f_price
                    data = line.strip().split(",")
                    if len(data) == 3:  # Ensure there are 3 parts: ID, name, price
                        try:
                            price = int(data[2])  # Extract the price
                            total_revenue += price  # Add to the total revenue
                        except ValueError:
                            print(f"Skipping invalid line in revenue file: {line}")
            print(f"Total Revenue: Rs{total_revenue}")
        except FileNotFoundError:
            print("Revenue file not found!")

    
    def total_bill(self):
        total = 0
        try:
            with open(self.order_file, "r") as f:
                for s in f:
                    f_id, f_name, f_price, f_qty = s.strip().split(",")
                    total += int(f_price) * int(f_qty)
            print(f"Total bill is: Rs{total}")
            # Clear the order file after billing
            with open(self.order_file, "w") as f:
                f.truncate(0)
            # If file does not exist
        except FileNotFoundError:
            print("Order file not found.")