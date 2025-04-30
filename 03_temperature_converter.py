def convert_temperature():
    print("\nTemperature Converter")
    while True:
        try:
            temp = float(input("Enter temperature: "))
            unit = input("Convert to (C/F): ").strip().upper()

            if unit == 'C':
                result = (temp - 32) * 5 / 9
                print(f"{temp}°F is {result:.2f}°C")
            elif unit == 'F':
                result = (temp * 9 / 5) + 32
                print(f"{temp}°C is {result:.2f}°F")
            else:
                print("Invalid unit! Use C or F.")
                continue

            again = input("Convert another? (y/n): ")
            if again.lower() != 'y':
                break

        except ValueError:
            print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    convert_temperature()
