# ============================================
#       LOST & FOUND ASSISTANT
#       Beginner Python Project
# ============================================

# Collections
lost_items = []
found_items = []


# --------------------------------------------
# FUNCTION 1: Report a lost item
# --------------------------------------------
def report_lost_item():
    print("\n========== REPORT LOST ITEM ==========")

    name = input("Enter your name: ")
    item = input("What did you lose? ")
    location = input("Where did you lose it? ")

    lost_item = {
        "name": name,
        "item": item,
        "location": location
    }

    lost_items.append(lost_item)

    print("\n✅ Your lost item has been recorded!")
    print("Item:", item)
    print("Location:", location)


# --------------------------------------------
# FUNCTION 2: Report a found item
# --------------------------------------------
def report_found_item():
    print("\n========== REPORT FOUND ITEM ==========")

    name = input("Enter your name: ")
    item = input("What did you find? ")
    location = input("Where did you find it? ")

    found_item = {
        "name": name,
        "item": item,
        "location": location
    }

    found_items.append(found_item)

    print("\n✅ Thank you!")
    print("The found item has been recorded.")


# --------------------------------------------
# FUNCTION 3: Search for an item
# --------------------------------------------
def search_item():
    print("\n========== SEARCH FOR ITEM ==========")

    search = input("Enter the item you are looking for: ").lower()

    found = False

    # Search through found items
    for item in found_items:

        if item["item"].lower() == search:
            print("\n🎉 GOOD NEWS!")
            print("The item was found.")
            print("Location:", item["location"])

            found = True

    if found == False:
        print("\n❌ Sorry, the item has not been found yet.")


# --------------------------------------------
# FUNCTION 4: Show lost items
# --------------------------------------------
def show_lost_items():
    print("\n========== LOST ITEMS ==========")

    if len(lost_items) == 0:
        print("There are no lost items recorded.")

    else:
        for number, item in enumerate(lost_items, start=1):
            print("\nItem", number)
            print("Name:", item["name"])
            print("Lost item:", item["item"])
            print("Location:", item["location"])


# --------------------------------------------
# FUNCTION 5: Show found items
# --------------------------------------------
def show_found_items():
    print("\n========== FOUND ITEMS ==========")

    if len(found_items) == 0:
        print("There are no found items recorded.")

    else:
        for number, item in enumerate(found_items, start=1):
            print("\nItem", number)
            print("Reported by:", item["name"])
            print("Found item:", item["item"])
            print("Location:", item["location"])


# --------------------------------------------
# FUNCTION 6: Give advice
# --------------------------------------------
def get_advice():
    print("\n========== LOST ITEM ADVICE ==========")

    print("If you lose something:")

    print("1. Stay calm.")
    print("2. Remember where you last used the item.")
    print("3. Check the place again.")
    print("4. Ask people around you.")
    print("5. Report the item as lost.")


# --------------------------------------------
# MAIN PROGRAM
# --------------------------------------------
def main():

    while True:

        print("\n")
        print("==========================================")
        print("       🔎 LOST & FOUND ASSISTANT")
        print("==========================================")

        print("1. Report Lost Item")
        print("2. Report Found Item")
        print("3. Search for an Item")
        print("4. Show Lost Items")
        print("5. Show Found Items")
        print("6. Get Advice")
        print("7. Exit")

        choice = input("\nChoose an option (1-7): ")

        # Option 1
        if choice == "1":
            report_lost_item()

        # Option 2
        elif choice == "2":
            report_found_item()

        # Option 3
        elif choice == "3":
            search_item()

        # Option 4
        elif choice == "4":
            show_lost_items()

        # Option 5
        elif choice == "5":
            show_found_items()

        # Option 6
        elif choice == "6":
            get_advice()

        # Option 7
        elif choice == "7":
            print("\n==========================================")
            print(" Thank you for using Lost & Found Assistant")
            print("==========================================")
            print("Goodbye! 👋")
            break

        # Wrong input
        else:
            print("\n❌ Invalid choice!")
            print("Please choose a number from 1 to 7.")


# --------------------------------------------
# START THE PROGRAM
# --------------------------------------------
main()