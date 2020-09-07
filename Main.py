# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# KSinkevitch,09/05/20,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
if __name__ == "__main__":
    import DataClasses as Data  # Data classes
    import ProcessingClasses as Process  # Processing classes
    import IOClasses as IO  # IO classes
else:
    raise Exception("This file was not created to be imported")

# Main Body of Script  ---------------------------------------------------- #

file_name = "EmployeeData.txt"
list_employees = []  # List of employee rows
choice = ""  # (string) Captures the user option selection

# Load data from file into a list of employee objects when script starts
list_file_employee_object = Process.FileProcessor.read_data_from_file(file_name)
list_employees.clear()
# Create a row of employee data by reading each Employee object and appending to a list
for row in list_file_employee_object:
    e = Data.Employee(row[0], row[1], row[2])
    list_employees.append(e)  # Add object info to row in list

while True:
    # Show user a menu of options
    # Get user's menu option choice
    # Show user current data in the list of employee objects
    # Let user add data to the list of employee objects
    # let user save current data to file
    # Let user exit program
    IO.EmployeeIO.print_menu_items()  # Show menu
    choice = IO.EmployeeIO.input_menu_options()  # Get menu option

    # Step 4 - Process user's menu choice
    if choice.strip() == '1':  # View current items
        IO.EmployeeIO.print_current_list_items(list_employees)  # Show current data in the list
        continue  # To show the menu

    elif choice.strip() == '2':  # Add a new item
        new_employee = IO.EmployeeIO.input_employee_data()  # Get employee info
        list_employees.append(new_employee)
        continue  # To show the menu

    elif choice.strip() == '3':  # Remove an existing item
        employee_id = IO.EmployeeIO.input_id_to_remove()  # Get employee id to remove from list
        # Remove item from list
        list_employees, status = Process.FileProcessor.remove_data_from_list(employee_id, list_employees)
        print(status)  # Provide status message
        continue  # To show the menu

    elif choice.strip() == '4':  # Save data to file
        # Verify user wants to save to file
        yes_no = IO.EmployeeIO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if yes_no.lower() == "y":
            status = Process.FileProcessor.save_data_to_file(file_name, list_employees)  # Save data to file
            print(status)
        continue  # To show the menu

    elif choice.strip() == "5":  # Exit program
        print("Thank you, exiting now....")
        break

    else:
        print("Please choose a number 1 through 5")  # Request user provide correct input

# Main Body of Script  ---------------------------------------------------- #
