import tracker

def main():
    choice = ""

    while choice != "4":
        print("\n=== Sleep Log Tracker ===")
        print("1. Add Sleep Entry")
        print("2. View All Entries")
        print("3. View Summary")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            tracker.add_sleep_entry()
        elif choice == "2":
            tracker.view_all_entries()
        elif choice == "3":
            tracker.view_summary()
        elif choice == "4":
            print("Exiting program.")
        else:
            print("Invalid choice.")

main()
