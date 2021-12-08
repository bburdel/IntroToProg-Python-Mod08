# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# BBurdelsky,12.5.21,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data - ------------------------------------------------------------------- #
strFileName = "products.txt"
lst_ProductObjs = []

class Product(object):
    """Stores data about a product:

        properties:
            product_name: (string) with the products's  name
            product_price: (float) with the products's standard price
        methods:
            __init__: constructor method (function) that initializes the class attributes (variables)
            __str__: string method (function) that defines the string representation of the class object/instance
        changelog: (When,Who,What)
            RRoot,1.1.2030,Created Class
            BBurdelsky,12.7.21,Modified code to complete assignment 8
        """
     # -- Constructor --
    def __init__(self, product_name, product_price):
        # -- Attributes --
        self.product_name = product_name
        self.product_price = product_price

    # -- Properties --
    # product_name
    @property
    def product_name(self):
        return str(self.__product_name).title()

    @product_name.setter
    def product_name(self, value):
        try:
            if len(value) > 25:
                raise Exception("The product name must not exceed 25 characters.")
            else:
                self.__product_name = value
        except Exception as e:
            print(e)

    # product_price
    @ property
    def product_price(self):
        return float(self.__product_price)

    @product_price.setter
    def product_price(self, value):
        if float(value) > 0:
            self.__product_price = value
        elif float(value) <= 0:
            raise Exception("The price must be greater than zero(0).")

     # -- Methods --
    def __str__(self):
        return str(self.product_name) + ", " + "%.2f" % self.product_price

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        BBurdelsky,12.7.21,Modified code to complete assignment 8
    """
    def read_data_from_file(self, file_name):
        """ Reads data from a file into a list

                :param file_name: (string) with name of file:
                :return: (list) of product objects
                """
        with open(file_name, "r") as file:
            lst_objs = file.read().splitlines()
            return lst_objs

    def save_data_to_file(self, file_name, lst_objs):
        """ Writes data to a text file

                :param file_name: (string) with name of file:
                :param list_of_rows: (list) you want to write to file:
                :return: (list) of product objects
                """
        with open(file_name, "a") as file:
            for item in lst_objs:
                file.write(str(item) + "\n")
        print("Data saved. Goodbye!")
# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Gathers data from user and outputs it back to the user:

    properties:
        choice: (str? int?) of the user's menu choice
    methods:
        show_menu_tasks(self)
        user_menu_choice(self)
    """
    def show_menu_tasks(self):
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu Options
        1) See Current Data
        2) Add Data
        3) Save & Quit        
        ''')

    def user_menu_choice(self):
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1, 2, or 3] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    def output_current_products(self, list_of_product_objects):
        """ Shows the current Products in a list

        :param list_of_product_objects: (list) of rows you want to display
        :return: nothing
        """
        print("_____The current products in the list_____")
        for each_product in list_of_product_objects:
            print(each_product)
        print("__________________________________________")

    def input_new_product(self, list_of_product_objects):
        """ Gets a new product and its price from the user

        :param list_of_product_objects: (list) of rows you want to append
        :return: appended list
        """
        try:
            product = str(input("\tEnter a product name: "))  # try/except block here?
        except Exception as e:
            print(e)
        # else:
        #     print("\tYou entered the product: ", product)
        try:
            price = float(input("\tEnter the price of that product: "))
        except Exception as e:
            print(e)
        # else:
        #     print("\tYou entered the price: ", price)
        prodObj = Product(product, price)
        list_of_product_objects.append(prodObj)
        return list_of_product_objects

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
processorObj = FileProcessor()
currentObj = processorObj.read_data_from_file(strFileName)
# print("The file was read and a list created:" + str(lst_ProductObjs))
interactiveObj = IO()

# Show user a menu of options
while True:

    # Get user's menu option choice
    interactiveObj.show_menu_tasks()
    option_select = interactiveObj.user_menu_choice()

    # Show user current data in the list of product objects
    if option_select.strip() == '1':
        interactiveObj.output_current_products(currentObj)

    # Let user add data to the list of product objects
    if option_select.strip() == '2':
        interactiveObj.input_new_product(lst_ProductObjs)

    # Let user save current data to file and exit program
    if option_select.strip() == '3':
        processorObj.save_data_to_file(strFileName, lst_ProductObjs)
        break

# Main Body of Script  ---------------------------------------------------- #

