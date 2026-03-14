import data

def add_sleep_entry():
    print("\n--- Add Sleep Entry ---")

    date = input("Enter the date: ").strip()

    hours = float(input("Enter hours slept: "))

    quality = int(input("Enter sleep quality (1-5): "))

    note = input("Enter notes: ").strip()

    data.dates.append(date)
    data.hours_slept.append(hours)
    data.sleep_quality.append(quality)
    data.notes.append(note)

    print("Sleep entry added successfully.")


def view_all_entries():
    print("\n--- View All Entries ---")

    if len(data.dates) == 0:
        print("No sleep entries found.")
    else:
        for i in range(len(data.dates)):
            print("\nEntry", i + 1)
            print("Date:", data.dates[i])
            print("Hours Slept:", data.hours_slept[i])
            print("Sleep Quality:", data.sleep_quality[i])
            print("Notes:", data.notes[i])


def view_summary():
    print("\n--- View Summary ---")

    if len(data.dates) == 0:
        print("No sleep entries found.")
    else:
        total_hours = 0
        total_quality = 0

        for i in range(len(data.hours_slept)):
            total_hours += data.hours_slept[i]
            total_quality += data.sleep_quality[i]

        average_hours = total_hours / len(data.hours_slept)
        average_quality = total_quality / len(data.sleep_quality)

        print("Total Entries:", len(data.dates))
        print("Average Hours Slept:", round(average_hours, 2))
        print("Average Sleep Quality:", round(average_quality, 2))
