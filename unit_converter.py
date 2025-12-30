# Let me create a quick interactive demo
print("Quick Interactive Demo\n")

# Simple conversion function
def convert_units():
    print("Choose conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Meters to Feet")
    
    choice = input("\nEnter choice (1 or 2): ")
    
    if choice == "1":
        try:
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius}°C = {fahrenheit}°F")
        except ValueError:
            print("Please enter a valid number!")
    
    elif choice == "2":
        try:
            meters = float(input("Enter length in meters: "))
            feet = meters / 0.3048
            print(f"{meters} m = {feet:.2f} ft")
        except ValueError:
            print("Please enter a valid number!")
    
    else:
        print("Invalid choice!")

# Run the demo
convert_units()
