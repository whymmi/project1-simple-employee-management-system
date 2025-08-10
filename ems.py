import os
import json
from dotenv import load_dotenv


load_dotenv()
admin_pass = os.getenv("ADMIN_PASSWORD") #OPTIONAL , make a .env file and just add a custom password


if os.path.exists("data.json"):
    with open("data.json", "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
             print("⚠️ Warning: data.json is not valid JSON. Initializing empty structure.")
             data = {}
else:
    data = {}

if "employees" not in data or not isinstance(data["employees"], list):
    data["employees"] = []


def save_data():
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)
def get_valid_str(prompt):
    while True:
        value = input(prompt).strip()
        if value and value.replace(" ","").isalpha():
            return value
        print("Name/position must contain only letters!")

def get_valid_int(prompt, min_value=None,max_value=None):
    while True:
        try:
            value = int(input(prompt).strip())
            if (min_value is None or value>=min_value) and (max_value is None or value<= max_value):
                return value
            print(f"Value must be between {min_value} and {max_value}. ")
        except ValueError:
            print("Enter a valid interger.")
def get_valid_float(prompt, min_value):
    while True:
        try:
            value = float(input(prompt).strip())
            if value >= min_value:
                return value
            print(f"Salary must be more than {min_value}")

        except ValueError:
            print("Please enter a valid number.")


def add_new_employee():
    name = get_valid_str("Enter the name of the new employee: ")
    position = get_valid_str("Enter employee's position: ")
    age = get_valid_int("Enter employee's age: ", min_value=18, max_value=63)
    salary = get_valid_float("Enter employee's salary: ", min_value=20.000)
    new_employee_data = {
            "name": name,
            "position": position,
            "age": age,
            "salary": salary
        }
    
    data["employees"].append(new_employee_data)
    save_data()
    print(f"\nEmployee '{name}' added successfully.\n")

def remove_employee(name):
    for emp in data["employees"]:
        if emp["name"].lower() == name.lower():
            data["employees"].remove(emp)
            save_data()
            print(f"✅ Employee '{name}' was removed.\n")
            return
    print(f"⚠️ Employee '{name}' not found.\n")

def edit_employee_data(option_to_edit):
            if option_to_edit == "name":
                emp["name"] = get_valid_str("New Name:")
            elif option_to_edit == "salary":
                emp["salary"] = get_valid_float("New Salary: ", min_value= 20000)
            elif option_to_edit == "position":
                emp["position"] = get_valid_str("New Positon:")
            elif option_to_edit == "age":
                emp["age"] = get_valid_int("New age:", min_value=18, max_value=63)
            else:
                print("⚠️There is no such option to edit.\n ")
            save_data()
def list_employee_data():
    for emp in data["employees"]:
        print(f" - {emp['name']}")
        print(f" ---- {emp['salary']}")
        print(f" ---- {emp['age']}")
        print(f" ---- {emp['position']}")

# Main loop
running = True
print("\nEmployee Management System")
user_pass = input("Enter admin password: ")
if user_pass == admin_pass:
    print("\nAccess granted.")
    while running:

        option = input("Choose option: 1.ADD, 2.REMOVE, 3.EDIT, 4.List, 5.EXIT\n")

        if option == "1":
            add_new_employee()
        elif option == "2":
              if not data["employees"]:
                print("⚠️ No employees to remove.\n")
              else:
                print("Current employees:")
                for emp in data["employees"]:
                    print(f" - {emp['name']}")
                employee_to_remove = input("\nEnter the name of the employee to remove: ")
                remove_employee(name=employee_to_remove)

        elif option == "3":
            if not data["employees"]:
                 print("⚠️ No employees to edit.\n")
            else:
                while True:
                    name = input("Enter employees name to edit: ")
                    found = False
                    for emp in data["employees"]:
                        if emp["name"].lower() == name.lower():
                            found = True
                            print("name:", emp["name"])
                            print("salary:", emp["salary"])
                            print("position:",emp["position"])
                            print("age:",emp["age"])
                            value_to_change = input("Enter which value you want to change: " )
                            edit_employee_data(option_to_edit=value_to_change)
                            break
                    if  found:
                        break
                    print(f"⚠️ Employee '{name}' not found. Try again.\n")
        elif option == "4":
            list_employee_data()
        elif option == "5":
            print("Exiting system...")
            running = False
        else:
            print("Invalid option.\n")
else:
        print("Incorrect password. Please try again.\n")
