def miles_to_km(miles):
    return miles * 1.60934

def km_to_miles(km):
    return km * 0.621371

def inches_to_cm(inches):
    return inches * 2.54

def cm_to_inches(cm):
    return cm * 0.393701

# Main logic
print("Choose conversion: ")
print("1. Miles to Km")
print("2. Km to Miles")
print("3. Inches to Cm")
print("4. Cm to Inches")

choice = int(input("Enter choice: "))
value = float(input("Enter value: "))

if choice == 1:
    print(f"{value} miles = {miles_to_km(value)} km")
elif choice == 2:
    print(f"{value} km = {km_to_miles(value)} miles")
elif choice == 3:
    print(f"{value} inches = {inches_to_cm(value)} cm")
elif choice == 4:
    print(f"{value} cm = {cm_to_inches(value)} inches")
else:
    print("Invalid choice")
