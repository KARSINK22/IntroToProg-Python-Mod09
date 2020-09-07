# ---------------------------------------------------------- #
# Title: Test Harness
# Description: A main module for testing
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# KSinkevitch, 9/5/20, Modified script for Assignment 09
# ---------------------------------------------------------- #
if __name__ == "__main__":
    import DataClasses as D  # Data classes
    import ProcessingClasses as P  # Processing classes
    import IOClasses as IO  # IO classes
else:
    raise Exception("This file was not created to be imported")

# ---------------- Test Data Module --------------------
# Test Person class
object_person1 = D.Person("Ricky", "Sinkevitch")  # Create a Person object
object_person2 = D.Person("Nellie", "Sinkevitch")  # Create a Person object
list_of_person_objects = [object_person1, object_person2]  # Add Person objects to a list of objects
# Print list of objects
print("Person Class:")
for row in list_of_person_objects:
    print(row.to_string(), type(row))
# Test error handling
# object_person1.first_name = "124"
# object_person2.last_name = "456"

# Test Employee class
object_emp1 = D.Employee(1, "Ricky", "Sinkevitch")  # Create a Employee object
object_emp2 = D.Employee(2, "Nellie", "Sinkevitch")  # Create a Employee object
list_of_employee_objects = [object_emp1, object_emp2]  # Add Employee objects to a list of objects
# Print list of objects
print("\nEmployee Class:")
for row in list_of_employee_objects:
    print(row.to_string(), type(row))
# Test error handling
# object_emp1.employee_id = "12f"

# ---------------- Test Processing Module --------------------
# Test FileProcessor class with person data
P.FileProcessor.save_data_to_file("PersonData.txt", list_of_person_objects)
list_file_data = P.FileProcessor.read_data_from_file("PersonData.txt")
# Print list of objects
print("\nFile Processor Class with Person Data:")
for row in list_file_data:
    p = D.Person(row[0], row[1])
    print(p.to_string().strip(), type(p))

# Test FileProcessor class with employee data
P.FileProcessor.save_data_to_file("EmployeeData.txt", list_of_employee_objects)

list_file_data = P.FileProcessor.read_data_from_file("EmployeeData.txt")
# Print list of objects
print("\nFile Processor Class with Employee Data:")
list_table = []
list_table.clear()
for row in list_file_data:
    e = D.Employee(row[0], row[1], row[2])
    list_table.append(e)  # Add object info to row in list
    print(e.to_string().strip(), type(e))

# ---------------- Test IO Module --------------------
# Test FileProcessor class with person data
print("\nTest EmployeeIO Print Menu Items:")
IO.EmployeeIO.print_menu_items()

print("Test EmployeeIO Input Menu Options:")
choice = IO.EmployeeIO.input_menu_options()
print('Choice: ', choice)

print("\nTest EmployeeIO Print Current List Items:")
IO.EmployeeIO.print_current_list_items(list_table)

print("\nTest EmployeeIO Input Employee Data:")
test_employee = IO.EmployeeIO.input_employee_data()
print(test_employee.to_string().strip(), type(test_employee))
