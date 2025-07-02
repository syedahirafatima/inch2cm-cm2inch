# Inch-Centimeter Conversion Program

print("Length Converter")
print("1. Inches to Centimeters")
print("2. Centimeters to Inches")

choice = input("Enter 1 or 2 to choose conversion: ")

if choice == "1":
    inches = float(input("Enter length in inches: "))
    cm = inches * 2.54
    print(inches, "inches is", round(cm, 2), "centimeters.")

elif choice == "2":
    cm = float(input("Enter length in centimeters: "))
    inches = cm / 2.54
    print(cm, "centimeters is", round(inches, 2), "inches.")

else:
    print("Invalid choice. Please enter 1 or 2.")
