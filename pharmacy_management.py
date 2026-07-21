class Medicine:
    def __init__(self, name, quantity, day, month, year):
        self.name = name
        self.quantity = quantity
        self.day = day
        self.month = month
        self.year = year
        self.next = None


head = None


# Create Medicine Node
def createMedicine(name, quantity, day, month, year):
    return Medicine(name, quantity, day, month, year)


# Add Medicine
def addMedicine():
    global head

    name = input("\nEnter medicine name: ")
    quantity = int(input("Enter quantity: "))
    day, month, year = map(int, input("Enter expiry date (DD MM YYYY): ").split())

    newNode = createMedicine(name, quantity, day, month, year)

    if head is None:
        head = newNode
    else:
        temp = head
        while temp.next:
            temp = temp.next
        temp.next = newNode

    print("\nMedicine added successfully!")


# Display Medicines
def displayMedicines():
    temp = head

    if temp is None:
        print("\nNo medicines in inventory.")
        return

    print("\n------ Medicine Inventory ------")

    while temp:
        print(f"\nName      : {temp.name}")
        print(f"Quantity  : {temp.quantity}")
        print(f"Expiry    : {temp.day:02d}/{temp.month:02d}/{temp.year}")

        temp = temp.next


# Search Medicine
def searchMedicine():
    searchName = input("\nEnter medicine name to search: ")

    temp = head

    while temp:

        if temp.name.lower() == searchName.lower():

            print("\nMedicine Found!")
            print(f"Name      : {temp.name}")
            print(f"Quantity  : {temp.quantity}")
            print(f"Expiry    : {temp.day:02d}/{temp.month:02d}/{temp.year}")
            return

        temp = temp.next

    print("\nMedicine not found.")


# Delete Medicine
def deleteMedicine():
    global head

    deleteName = input("\nEnter medicine name to delete: ")

    temp = head
    prev = None

    while temp:

        if temp.name.lower() == deleteName.lower():

            if prev is None:
                head = temp.next
            else:
                prev.next = temp.next

            print("\nMedicine deleted successfully!")
            return

        prev = temp
        temp = temp.next

    print("\nMedicine not found.")


# Check Expiry
def checkExpiry():

    cDay, cMonth, cYear = map(
        int,
        input("\nEnter today's date (DD MM YYYY): ").split()
    )

    temp = head

    print("\n------ Expiry Report ------")

    found = False

    while temp:

        # Expired
        if (
            temp.year < cYear or
            (temp.year == cYear and temp.month < cMonth) or
            (temp.year == cYear and temp.month == cMonth and temp.day < cDay)
        ):

            print(f"{temp.name} is EXPIRED!")
            found = True

        # Near Expiry
        elif (
            temp.year == cYear and
            temp.month == cMonth and
            (temp.day - cDay) <= 7
        ):

            print(f"{temp.name} is NEAR EXPIRY!")
            found = True

        temp = temp.next

    if not found:
        print("No expiry alerts.")


# Main Function
def main():

    while True:

        print("\n========== Pharmacy Drug Inventory System ==========")
        print("1. Add Medicine")
        print("2. Display Medicines")
        print("3. Search Medicine")
        print("4. Delete Medicine")
        print("5. Check Expiry Alerts")
        print("6. Exit")

        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("\nPlease enter a valid number.")
            continue

        if choice == 1:
            addMedicine()

        elif choice == 2:
            displayMedicines()

        elif choice == 3:
            searchMedicine()

        elif choice == 4:
            deleteMedicine()

        elif choice == 5:
            checkExpiry()

        elif choice == 6:
            print("\nThank You!")
            break

        else:
            print("\nInvalid Choice.")


if __name__ == "__main__":
    main()
