# Invoice Total Calculator

def print_invoice(items, subtotal, gst_amount, grand_total):
    print("\n")
    print("=" * 50)
    print("                INVOICE")
    print("=" * 50)

    print("{:<20} {:>8} {:>8} {:>10}".format("Item", "Price", "Qty", "Total"))
    print("-" * 50)

    for item in items:
        print("{:<20} {:>8.2f} {:>8} {:>10.2f}".format(
            item["name"],
            item["price"],
            item["quantity"],
            item["total"]
        ))

    print("-" * 50)
    print(f"Subtotal      : ₹ {subtotal:.2f}")
    print(f"GST Amount    : ₹ {gst_amount:.2f}")
    print(f"Grand Total   : ₹ {grand_total:.2f}")
    print("=" * 50)


def main():

    print("=" * 50)
    print("      Invoice Total Calculator")
    print("=" * 50)

    items = []

    n = int(input("Enter number of items: "))

    for i in range(n):

        print(f"\nItem {i+1}")

        name = input("Item Name : ")

        price = float(input("Price     : "))

        quantity = int(input("Quantity  : "))

        total = price * quantity

        item = {
            "name": name,
            "price": price,
            "quantity": quantity,
            "total": total
        }

        items.append(item)

    gst_percent = float(input("\nEnter GST Percentage : "))

    subtotal = 0

    for item in items:
        subtotal += item["total"]

    gst_amount = subtotal * gst_percent / 100

    grand_total = subtotal + gst_amount

    print_invoice(items, subtotal, gst_amount, grand_total)


main()