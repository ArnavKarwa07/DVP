from datetime import date, datetime

def age(birth_date):
    today = date.today()
    years = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        years -= 1
    return years

def save_to_file(name, birth_date, age_val):
    with open("age_data.txt", "a") as f:
        f.write(f"Name: {name}, Birthdate: {birth_date}, Age: {age_val}\n")

def main():
    try:
        name = input("Enter your name: ")
        birth_year = int(input("Enter birth year (YYYY): "))
        birth_month = input("Enter birth month (MM or Month name): ").strip()

        # Convert month input to number
        if not birth_month.isdigit():
            try:
                if len(birth_month) > 3:  # Full month name
                    birth_month = datetime.strptime(birth_month, "%B").month
                else:  # Short month name
                    birth_month = datetime.strptime(birth_month, "%b").month
            except ValueError:
                print("❌ Invalid month name! Please try again.")
                return
        else:
            birth_month = int(birth_month)

        birth_day = int(input("Enter birth day (DD): "))

        # Validate the date
        birth_date = date(birth_year, birth_month, birth_day)
        age_val = age(birth_date)
        print(f"✅ {name}, your age is: {age_val} years.")

        # Save to file
        save_to_file(name, birth_date, age_val)

    except ValueError:
        print("❌ Invalid date entered! Please check your input.")

if __name__ == "__main__":
    main()