import os
import datetime
import json

# ==================== UTILITY FUNCTIONS ====================
def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header():
    """Display program header"""
    print("=" * 60)
    print("            U N I T   C O N V E R T E R")
    print("=" * 60)

def save_history(conversion_type, from_unit, to_unit, value, result):
    """Save conversion to history file"""
    history_entry = {
        'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'type': conversion_type,
        'from': from_unit,
        'to': to_unit,
        'value': value,
        'result': result
    }
    
    try:
        # Read existing history
        if os.path.exists("conversion_history.json"):
            with open("conversion_history.json", "r") as file:
                history = json.load(file)
        else:
            history = []
        
        # Add new entry (limit to 100 entries)
        history.append(history_entry)
        if len(history) > 100:
            history = history[-100:]
        
        # Save back to file
        with open("conversion_history.json", "w") as file:
            json.dump(history, file, indent=4)
    except:
        # Fallback to text file if JSON fails
        try:
            with open("conversion_history.txt", "a") as file:
                file.write(f"{history_entry['timestamp']} | {conversion_type} | "
                          f"{value} {from_unit} = {result} {to_unit}\n")
        except:
            pass

# ==================== CONVERSION FUNCTIONS ====================
def temperature_converter():
    """Convert between temperature units"""
    clear_screen()
    display_header()
    print("\n🌡️  TEMPERATURE CONVERTER")
    print("-" * 40)
    
    units = {
        "1": ("Celsius", "C"),
        "2": ("Fahrenheit", "F"),
        "3": ("Kelvin", "K")
    }
    
    print("Choose source unit:")
    for key, (name, symbol) in units.items():
        print(f"  {key}. {name} ({symbol})")
    
    try:
        choice1 = input("\nEnter choice (1-3): ")
        if choice1 not in units:
            print("Invalid choice!")
            return
        
        choice2 = input("Enter target unit (1-3, different from source): ")
        if choice2 not in units or choice1 == choice2:
            print("Invalid choice!")
            return
        
        value = float(input(f"\nEnter temperature in {units[choice1][0]}: "))
        
        # Convert to Celsius first
        if choice1 == "1":  # Celsius
            celsius = value
        elif choice1 == "2":  # Fahrenheit
            celsius = (value - 32) * 5/9
        else:  # Kelvin
            celsius = value - 273.15
        
        # Convert from Celsius to target
        if choice2 == "1":  # Celsius
            result = celsius
        elif choice2 == "2":  # Fahrenheit
            result = (celsius * 9/5) + 32
        else:  # Kelvin
            result = celsius + 273.15
        
        print(f"\n✅ {value} {units[choice1][1]} = {result:.2f} {units[choice2][1]}")
        save_history("Temperature", units[choice1][1], units[choice2][1], value, result)
        
    except ValueError:
        print("Invalid input! Please enter a number.")
    
    input("\nPress Enter to continue...")

def length_converter():
    """Convert between length units"""
    clear_screen()
    display_header()
    print("\n📏 LENGTH CONVERTER")
    print("-" * 40)
    
    # Conversion factors to meters
    units = {
        "1": ("Millimeters", "mm", 0.001),
        "2": ("Centimeters", "cm", 0.01),
        "3": ("Meters", "m", 1.0),
        "4": ("Kilometers", "km", 1000.0),
        "5": ("Inches", "in", 0.0254),
        "6": ("Feet", "ft", 0.3048),
        "7": ("Yards", "yd", 0.9144),
        "8": ("Miles", "mi", 1609.34)
    }
    
    print("Choose source unit:")
    for key, (name, symbol, _) in units.items():
        print(f"  {key}. {name} ({symbol})")
    
    try:
        choice1 = input("\nEnter choice (1-8): ")
        if choice1 not in units:
            print("Invalid choice!")
            return
        
        choice2 = input("Enter target unit (1-8): ")
        if choice2 not in units:
            print("Invalid choice!")
            return
        
        value = float(input(f"\nEnter length in {units[choice1][1]}: "))
        
        # Convert to meters then to target unit
        meters = value * units[choice1][2]
        result = meters / units[choice2][2]
        
        print(f"\n✅ {value} {units[choice1][1]} = {result:.6f} {units[choice2][1]}")
        save_history("Length", units[choice1][1], units[choice2][1], value, result)
        
    except ValueError:
        print("Invalid input! Please enter a number.")
    
    input("\nPress Enter to continue...")

def weight_converter():
    """Convert between weight units"""
    clear_screen()
    display_header()
    print("\n⚖️  WEIGHT CONVERTER")
    print("-" * 40)
    
    # Conversion factors to grams
    units = {
        "1": ("Milligrams", "mg", 0.001),
        "2": ("Grams", "g", 1.0),
        "3": ("Kilograms", "kg", 1000.0),
        "4": ("Ounces", "oz", 28.3495),
        "5": ("Pounds", "lb", 453.592),
        "6": ("Metric Tons", "t", 1000000.0)
    }
    
    print("Choose source unit:")
    for key, (name, symbol, _) in units.items():
        print(f"  {key}. {name} ({symbol})")
    
    try:
        choice1 = input("\nEnter choice (1-6): ")
        if choice1 not in units:
            print("Invalid choice!")
            return
        
        choice2 = input("Enter target unit (1-6): ")
        if choice2 not in units:
            print("Invalid choice!")
            return
        
        value = float(input(f"\nEnter weight in {units[choice1][1]}: "))
        
        # Convert to grams then to target unit
        grams = value * units[choice1][2]
        result = grams / units[choice2][2]
        
        print(f"\n✅ {value} {units[choice1][1]} = {result:.6f} {units[choice2][1]}")
        save_history("Weight", units[choice1][1], units[choice2][1], value, result)
        
    except ValueError:
        print("Invalid input! Please enter a number.")
    
    input("\nPress Enter to continue...")

def currency_converter():
    """Convert between currencies (using fixed rates)"""
    clear_screen()
    display_header()
    print("\n💰 CURRENCY CONVERTER")
    print("-" * 40)
    print("Note: Rates are fixed for demo. Real app would use API")
    
    # Fixed exchange rates (to USD)
    currencies = {
        "1": ("US Dollar", "USD", 1.0),
        "2": ("Euro", "EUR", 0.92),
        "3": ("British Pound", "GBP", 0.79),
        "4": ("Japanese Yen", "JPY", 150.0),
        "5": ("Indian Rupee", "INR", 83.0),
        "6": ("Australian Dollar", "AUD", 1.52),
        "7": ("Canadian Dollar", "CAD", 1.35)
    }
    
    print("\nChoose source currency:")
    for key, (name, code, _) in currencies.items():
        print(f"  {key}. {name} ({code})")
    
    try:
        choice1 = input("\nEnter choice (1-7): ")
        if choice1 not in currencies:
            print("Invalid choice!")
            return
        
        choice2 = input("Enter target currency (1-7): ")
        if choice2 not in currencies:
            print("Invalid choice!")
            return
        
        value = float(input(f"\nEnter amount in {currencies[choice1][1]}: "))
        
        # Convert to USD first, then to target
        usd_value = value / currencies[choice1][2]
        result = usd_value * currencies[choice2][2]
        
        print(f"\n✅ {value} {currencies[choice1][1]} = {result:.2f} {currencies[choice2][1]}")
        save_history("Currency", currencies[choice1][1], currencies[choice2][1], value, result)
        
    except ValueError:
        print("Invalid input! Please enter a number.")
    
    input("\nPress Enter to continue...")

def data_storage_converter():
    """Convert between digital storage units"""
    clear_screen()
    display_header()
    print("\n💾 DATA STORAGE CONVERTER")
    print("-" * 40)
    
    # Conversion factors to bytes
    units = {
        "1": ("Bytes", "B", 1),
        "2": ("Kilobytes", "KB", 1024),
        "3": ("Megabytes", "MB", 1024**2),
        "4": ("Gigabytes", "GB", 1024**3),
        "5": ("Terabytes", "TB", 1024**4),
        "6": ("Petabytes", "PB", 1024**5)
    }
    
    print("Choose source unit:")
    for key, (name, symbol, _) in units.items():
        print(f"  {key}. {name} ({symbol})")
    
    try:
        choice1 = input("\nEnter choice (1-6): ")
        if choice1 not in units:
            print("Invalid choice!")
            return
        
        choice2 = input("Enter target unit (1-6): ")
        if choice2 not in units:
            print("Invalid choice!")
            return
        
        value = float(input(f"\nEnter storage in {units[choice1][1]}: "))
        
        # Convert to bytes then to target
        bytes_value = value * units[choice1][2]
        result = bytes_value / units[choice2][2]
        
        print(f"\n✅ {value} {units[choice1][1]} = {result:.6f} {units[choice2][1]}")
        save_history("Data Storage", units[choice1][1], units[choice2][1], value, result)
        
    except ValueError:
        print("Invalid input! Please enter a number.")
    
    input("\nPress Enter to continue...")

def time_converter():
    """Convert between time units"""
    clear_screen()
    display_header()
    print("\n⏰ TIME CONVERTER")
    print("-" * 40)
    
    # Conversion factors to seconds
    units = {
        "1": ("Seconds", "sec", 1),
        "2": ("Minutes", "min", 60),
        "3": ("Hours", "hr", 3600),
        "4": ("Days", "day", 86400),
        "5": ("Weeks", "wk", 604800),
        "6": ("Months (30 days)", "mo", 2592000),
        "7": ("Years (365 days)", "yr", 31536000)
    }
    
    print("Choose source unit:")
    for key, (name, symbol, _) in units.items():
        print(f"  {key}. {name} ({symbol})")
    
    try:
        choice1 = input("\nEnter choice (1-7): ")
        if choice1 not in units:
            print("Invalid choice!")
            return
        
        choice2 = input("Enter target unit (1-7): ")
        if choice2 not in units:
            print("Invalid choice!")
            return
        
        value = float(input(f"\nEnter time in {units[choice1][1]}: "))
        
        # Convert to seconds then to target
        seconds = value * units[choice1][2]
        result = seconds / units[choice2][2]
        
        print(f"\n✅ {value} {units[choice1][1]} = {result:.6f} {units[choice2][1]}")
        save_history("Time", units[choice1][1], units[choice2][1], value, result)
        
    except ValueError:
        print("Invalid input! Please enter a number.")
    
    input("\nPress Enter to continue...")

# ==================== HISTORY VIEWER ====================
def view_conversion_history():
    """Display conversion history from file"""
    clear_screen()
    display_header()
    print("\n📜 CONVERSION HISTORY")
    print("-" * 60)
    
    try:
        if os.path.exists("conversion_history.json"):
            with open("conversion_history.json", "r") as file:
                history = json.load(file)
                
            if not history:
                print("No conversion history found.")
            else:
                print(f"Total conversions: {len(history)}\n")
                for entry in history[-10:]:  # Show last 10 entries
                    print(f"{entry['timestamp']} | {entry['type']}")
                    print(f"  {entry['value']} {entry['from']} → {entry['result']:.4f} {entry['to']}")
                    print("-" * 40)
        elif os.path.exists("conversion_history.txt"):
            with open("conversion_history.txt", "r") as file:
                lines = file.readlines()
                
            if not lines:
                print("No conversion history found.")
            else:
                print(f"Total conversions: {len(lines)}\n")
                for line in lines[-10:]:  # Show last 10 entries
                    print(line.strip())
                    print("-" * 40)
        else:
            print("No conversion history found.")
            
    except Exception as e:
        print(f"Error reading history: {e}")
    
    input("\nPress Enter to continue...")

def clear_history():
    """Clear the conversion history"""
    clear_screen()
    display_header()
    print("\n🗑️  CLEAR HISTORY")
    print("-" * 40)
    
    confirm = input("Are you sure you want to clear all history? (yes/no): ")
    
    if confirm.lower() == 'yes':
        try:
            if os.path.exists("conversion_history.json"):
                os.remove("conversion_history.json")
            if os.path.exists("conversion_history.txt"):
                os.remove("conversion_history.txt")
            print("✓ History cleared successfully!")
        except:
            print("✗ Error clearing history.")
    else:
        print("Operation cancelled.")
    
    input("\nPress Enter to continue...")

# ==================== STATISTICS ====================
def show_statistics():
    """Show conversion statistics"""
    clear_screen()
    display_header()
    print("\n📊 CONVERSION STATISTICS")
    print("-" * 60)
    
    try:
        if os.path.exists("conversion_history.json"):
            with open("conversion_history.json", "r") as file:
                history = json.load(file)
                
            if not history:
                print("No data available.")
                return
            
            # Count by conversion type
            type_count = {}
            for entry in history:
                conv_type = entry['type']
                type_count[conv_type] = type_count.get(conv_type, 0) + 1
            
            print(f"Total Conversions: {len(history)}")
            print(f"First Conversion: {history[0]['timestamp']}")
            print(f"Last Conversion: {history[-1]['timestamp']}")
            
            print("\nConversions by Type:")
            for conv_type, count in type_count.items():
                print(f"  {conv_type}: {count}")
                
        elif os.path.exists("conversion_history.txt"):
            with open("conversion_history.txt", "r") as file:
                lines = file.readlines()
            
            if not lines:
                print("No data available.")
                return
            
            print(f"Total Conversions: {len(lines)}")
            if lines:
                print(f"First Conversion: {lines[0].split('|')[0].strip()}")
                print(f"Last Conversion: {lines[-1].split('|')[0].strip()}")
                
        else:
            print("No data available.")
            
    except Exception as e:
        print(f"Error reading statistics: {e}")
    
    input("\nPress Enter to continue...")

# ==================== MAIN HOME PAGE ====================
def main_homepage():
    """Main unit converter homepage"""
    while True:
        clear_screen()
        display_header()
        
        print("\n" + "=" * 60)
        print("             MAIN MENU")
        print("=" * 60)
        
        print("\n📋 CONVERSION CATEGORIES:")
        print("  1. 🌡️  Temperature Converter")
        print("  2. 📏 Length Converter")
        print("  3. ⚖️  Weight/Mass Converter")
        print("  4. 💰 Currency Converter")
        print("  5. 💾 Data Storage Converter")
        print("  6. ⏰ Time Converter")
        
        print("\n📊 TOOLS & HISTORY:")
        print("  7. 📜 View Conversion History")
        print("  8. 📊 View Statistics")
        print("  9. 🗑️  Clear History")
        print("  0. 🚪 Exit Program")
        
        print("\n" + "=" * 60)
        
        choice = input("\nEnter your choice (0-9): ")
        
        if choice == "1":
            temperature_converter()
        elif choice == "2":
            length_converter()
        elif choice == "3":
            weight_converter()
        elif choice == "4":
            currency_converter()
        elif choice == "5":
            data_storage_converter()
        elif choice == "6":
            time_converter()
        elif choice == "7":
            view_conversion_history()
        elif choice == "8":
            show_statistics()
        elif choice == "9":
            clear_history()
        elif choice == "0":
            clear_screen()
            print("\nThank you for using Unit Converter!")
            print("Goodbye! 👋\n")
            break
        else:
            print("Invalid choice! Please try again.")
            input("\nPress Enter to continue...")

# ==================== PROGRAM START ====================
if __name__ == "__main__":
    # Create a welcome message file if it doesn't exist
    if not os.path.exists("welcome.txt"):
        with open("welcome.txt", "w") as file:
            file.write("Welcome to Unit Converter!\n")
            file.write("Your conversions will be saved to history.\n")
            file.write(f"First run: {datetime.datetime.now()}\n")
    
    # Display welcome message
    clear_screen()
    print("╔" + "═" * 58 + "╗")
    print("║" + " " * 58 + "║")
    print("║" + " " * 20 + "UNIT CONVERTER" + " " * 23 + "║")
    print("║" + " " * 58 + "║")
    print("║" + " " * 12 + "Convert between multiple units easily!" + " " * 9 + "║")
    print("║" + " " * 58 + "║")
    print("╚" + "═" * 58 + "╝")
    
    print("\n" + "-" * 60)
    print("Features:")
    print("  • 6 different conversion categories")
    print("  • Conversion history tracking")
    print("  • Statistics and analytics")
    print("  • File-based data storage")
    print("-" * 60)
    
    input("\nPress Enter to start converting...")
    
    # Start the main program
    main_homepage()
