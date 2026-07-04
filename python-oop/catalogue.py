class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    def total_value(self):
        return self.price * self.quantity

    def display(self):
        print("-" * 40)
        print(f"Product  : {self.name}")
        print(f"Price    : ₹{self.price}")
        print(f"Quantity : {self.quantity}")
        print(f"Total    : ₹{self.total_value()}")


def main():

    catalogue = []

    while True:

        print("\n===== Product Catalogue =====")
        print("1. Add Product")
        print("2. View Catalogue")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":

            try:
                name = input("Product Name: ")
                price = float(input("Price: "))
                quantity = int(input("Quantity: "))

                product = Product(name, price, quantity)

                catalogue.append(product)

                print("Product Added Successfully.")

            except ValueError as e:
                print("Error:", e)

        elif choice == "2":

            if not catalogue:
                print("Catalogue is empty.")
            else:
                for product in catalogue:
                    product.display()

        elif choice == "3":

            print("Thank You")
            break

        else:

            print("Invalid Choice")


main()