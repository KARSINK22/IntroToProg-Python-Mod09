# ---------------------------------------------------------- #
# Title: IO Classes
# Description: A module of IO classes
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# KSinkevitch, 09/07/20, Modified for assignment 09
# ---------------------------------------------------------- #
if __name__ == "__main__":
    raise Exception("This file is not meant to run by itself")
else: 
    import DataClasses as D

class EmployeeIO:
    """  A class for performing Employee Input and Output

    methods:
        print_menu_items():

        input_menu_options(): -> (choice)

        print_current_list_items(list_of_rows):

        input_employee_data():

        input_yes_no_choice(): -> (str)

        input_id_to_remove(): -> (io_employee_id)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class:
    """
    @staticmethod
    def print_menu_items():
        """ Print a menu of choices to the user  """
        print('''
        Menu of Options
        1) Show current employee data
        2) Add new employee data
        3) Remove an item
        4) Save employee data to file
        5) Exit program
        ''')

    @staticmethod
    def input_menu_options():
        """ Gets the menu choice from a user

        :return: string (choice)
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_list_items(list_of_objects: list):
        """ Print the current items in the list of Employee rows

        :param list_of_objects: (list) of rows you want to display
        """
        print("******* The current items employees are: *******")
        for row in list_of_objects:
            print(str(row.employee_id)
                 + ","
                 + row.first_name
                 + ","
                 + row.last_name.strip())
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_employee_data():
        """ Gets data for a employee object

        :return: (object) employee object
        """
        emp = None
        try:
            employee_id = (input("What is the employee Id? - ").strip())
            first_name = str(input("What is the employee First Name? - ").strip())
            last_name = str(input("What is the employee Last Name? - "))
            print()  # Add an extra line for looks
            emp = D.Employee(employee_id, first_name, last_name)
        except Exception as e:
            print(e)
        return emp

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: (string) message
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_id_to_remove():
        """ Input an employee id to remove from list

        :param:  none
        :return: (string) employee id
        """

        io_employee_id = input("Enter employee id to remove from list: ")  # Prompt user for id to remove
        return io_employee_id
