# Define arrays to store item information
case_items = [("A1", "Compact", 75.00), ("A2", "Tower", 150.00)]
ram_items = [("B1", "8 GB", 79.99), ("B2", "16 GB", 149.99), ("B3", "32 GB", 299.99)]
hdd_items = [("C1", "1 TB HDD", 49.99), ("C2", "2 TB HDD", 89.99), ("C3", "4 TB HDD", 129.99)]
ssd_items = [("D1", "240 GB SSD", 59.99), ("D2", "480 GB SSD", 119.99)]
second_hdd_items = [("E1", "1 TB HDD", 49.99), ("E2", "2 TB HDD", 89.99), ("E3", "4 TB HDD", 129.99)]
optical_drive_items = [("F1", "DVD/Blu-Ray Player", 50.00), ("F2", "DVD/Blu-Ray Re-writer", 100.00)]
os_items = [("G1", "Standard Version", 100.00), ("G2", "Professional Version", 175.00)]

# Initialize selected item variables
selected_case = None
selected_ram = None
selected_hdd = None
selected_ssd = None
selected_second_hdd = None
selected_optical_drive = None
selected_os = None

# Function to display a menu and get user choice
def get_user_choice(items, category):
    print(f"Select a {category} item:")
    for i, item in enumerate(items):
        item_code, description, price = item
        print(f"{i + 1}. {description} - ${price:.2f}")
    while True:
        try:
            choice = int(input(f"Enter the number of your {category} choice: "))
            if 1 <= choice <= len(items):
                return items[choice - 1]
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Task 1 - Setting up the system and ordering the main items
print("Task 1 - Setting up the system and ordering the main items")
print("Choose the main components for your computer:")

selected_case = get_user_choice(case_items, "case")
selected_ram = get_user_choice(ram_items, "RAM")
selected_hdd = get_user_choice(hdd_items, "Main Hard Disk Drive")

# Calculate the price of the computer
computer_price = 200.00  # Basic set of components cost
computer_price += selected_case[2] + selected_ram[2] + selected_hdd[2]

print("\nChosen items:")
print(f"Case: {selected_case[1]} - ${selected_case[2]:.2f}")
print(f"RAM: {selected_ram[1]} - ${selected_ram[2]:.2f}")
print(f"Main Hard Disk Drive: {selected_hdd[1]} - ${selected_hdd[2]:.2f}")
print(f"Total Price: ${computer_price:.2f}")

# Task 2 - Ordering additional items
print("\nTask 2 - Ordering additional items")
print("Do you want to purchase additional items?")
additional_items_price = 0.0

while True:
    choice = input("Enter 'Y' for Yes or 'N' for No: ").strip().lower()
    if choice == 'n':
        break
    elif choice == 'y':
        print("Choose an additional category:")
        print("1. Solid State Drive")
        print("2. Second Hard Disk Drive")
        print("3. Optical Drive")
        print("4. Operating System")
        additional_category = int(input("Enter the number of the category you want to choose: "))

        if additional_category == 1:
            selected_ssd = get_user_choice(ssd_items, "Solid State Drive")
            additional_items_price += selected_ssd[2]
        elif additional_category == 2:
            selected_second_hdd = get_user_choice(second_hdd_items, "Second Hard Disk Drive")
            additional_items_price += selected_second_hdd[2]
        elif additional_category == 3:
            selected_optical_drive = get_user_choice(optical_drive_items, "Optical Drive")
            additional_items_price += selected_optical_drive[2]
        elif additional_category == 4:
            selected_os = get_user_choice(os_items, "Operating System")
            additional_items_price += selected_os[2]
        else:
            print("Invalid choice. Please enter a valid number.")
    else:
        print("Invalid choice. Please enter 'Y' for Yes or 'N' for No.")

computer_price += additional_items_price

print("\nAdditional items:")
if selected_ssd:
    print(f"Solid State Drive: {selected_ssd[1]} - ${selected_ssd[2]:.2f}")
if selected_second_hdd:
    print(f"Second Hard Disk Drive: {selected_second_hdd[1]} - ${selected_second_hdd[2]:.2f}")
if selected_optical_drive:
    print(f"Optical Drive: {selected_optical_drive[1]} - ${selected_optical_drive[2]:.2f}")
if selected_os:
    print(f"Operating System: {selected_os[1]} - ${selected_os[2]:.2f}")

print(f"Total Price (with additional items): ${computer_price:.2f}")

# Task 3 - Offering discounts
print("\nTask 3 - Offering discounts")
discounted_price = computer_price
num_additional_items = sum(item is not None for item in [selected_ssd, selected_second_hdd, selected_optical_drive, selected_os])

if num_additional_items == 1:
    discounted_price *= 0.95  # 5% discount for one additional item
elif num_additional_items >= 2:
    discounted_price *= 0.90  # 10% discount for two or more additional items

money_saved = computer_price - discounted_price

print(f"Amount of money saved: ${money_saved:.2f}")
print(f"New Price (after discount): ${discounted_price:.2f}")
