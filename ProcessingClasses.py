# ---------------------------------------------------------- #
# Title: Processing Classes
# Description: A module of multiple processing classes
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# KSinkevitch, 09/05/20, Modified for assignment 09
# ---------------------------------------------------------- #
if __name__ == "__main__":
    raise Exception("This file is not meant to ran by itself")

class FileProcessor:
    """Processes data to and from a file and a list of objects:

    methods:
        save_data_to_file(file_name,list_of_objects):

        read_data_from_file(file_name): -> (a list of objects)

        remove_data_from_list(fp_employee_id, list_of_objects): -> (a list of objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
    """

    @staticmethod
    def save_data_to_file(file_name: str, list_of_objects: list):
        """ Write data to a file from a list of object rows

        :param file_name: (string) with name of file
        :param list_of_objects: (list) of objects data saved to file
        :return: (bool) with status of success status
        """
        success_status = ""
        try:
            file = open(file_name, "w")
            for row in list_of_objects:
                file.write(row.__str__())
            file.close()
            success_status = "File saved!"
        except Exception as e:
            print("There was a general error!")
            print(e, e.__doc__, type(e), sep='\n')
        return success_status

    @staticmethod
    def read_data_from_file(file_name: str):
        """ Reads data from a file into a list of object rows

        :param file_name: (string) with name of file
        :return: (list) of object rows
        """
        list_of_rows = []
        try:
            file = open(file_name, "r")
            for line in file:
                row = line.split(",")
                list_of_rows.append(row)
            file.close()
        except Exception as e:
            print("There was a general error!")
            print(e, e.__doc__, type(e), sep='\n')
        return list_of_rows

    @staticmethod
    def remove_data_from_list(fp_employee_id: int, list_of_objects: list):
        """ Removes a row of data in a list of dictionary rows

        :param fp_employee_id: (string) description of product:
        :param list_of_objects: (list) you want to remove data from:
        :return: (list) of Product class instances, (string) status message
        """
        list_of_items_to_keep = []  # Initialize new list of items to be kept
        message = "Item not found"  # Initialize return message

        for obj in list_of_objects:  # For every row in the list, only copy the rows to be kept into new list
            # Check if the row's Product value is not equal to the value to delete
            if obj.employee_id != fp_employee_id:
                list_of_items_to_keep.append(obj)  # Create new list of rows that should be kept
            else:
                message = 'Employee removed!'  # Value is found and not added to new list (i.e., deleted)
        list_of_obj = list_of_items_to_keep  # Set list_of_rows address to the new list of items to keep
        return list_of_obj, message


class DatabaseProcessor:
    pass
