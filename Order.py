class Order:
    def __init__(self, f_id=0, f_name="", f_price=0, f_qty=1):
        self.f_id = f_id
        self.f_name = f_name
        self.f_price = f_price
        self.f_qty = f_qty
    
    def __str__(self):
        # Return string representation of the order
        return f"{self.f_id}, {self.f_name}, {self.f_price}, {self.f_qty}"

    def total_price(self):
        # Calculate total price of the order based on the quantity provided during ordering
        return self.f_price * self.f_qty
