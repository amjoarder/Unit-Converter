def convert_length():
    print("\nLength Conversion:")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    choice = input("Choose an option (1/2): ").strip()
    if choice == "1":
        km = float(input("Enter distance in kilometers: "))
        print(f"{km} km = {km * 0.621371} miles")
    elif choice == "2":
        miles = float(input("Enter distance in miles: "))
        print(f"{miles} miles = {miles / 0.621371} kilometers")
    else:
        print("Invalid choice.")

def convert_weight():
    print("\nWeight Conversion:")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    choice = input("Choose an option (1/2): ").strip()
    if choice == "1":
        kg = float(input("Enter weight in kilograms: "))
        print(f"{kg} kg = {kg * 2.20462} pounds")
    elif choice == "2":
        pounds = float(input("Enter weight in pounds: "))
        print(f"{pounds} pounds = {pounds / 2.20462} kilograms")
    else:
        print("Invalid choice.")

def convert_temperature():
    print("\nTemperature Conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Choose an option (1/2): ").strip()
    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius}°C = {(celsius * 9/5) + 32}°F")
    elif choice == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{fahrenheit}°F = {(fahrenheit - 32) * 5/9}°C")
    else:
        print("Invalid choice.")

def main():
    print("Welcome to the Unit Converter!")
    while True:
        print("\n--- Conversion Options ---")
        print("1. Length Conversion")
        print("2. Weight Conversion")
        print("3. Temperature Conversion")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            convert_length()
        elif choice == "2":
            convert_weight()
        elif choice == "3":
            convert_temperature()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
