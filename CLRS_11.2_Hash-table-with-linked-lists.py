# 25.1.2024
# Adding to code from CLRS 11.1_Simple-hash-array
# (which assigns index in array based on position of first character in alphabet (0-25))
# Uses linked lists per slot to handle collisions. A value which hashes to the same slot is added to the HEAD of the list


table = []

class dll_node:             # Doubly linked list NODE class
    def __init__(self,value):
        self.data = value
        self.back = None
        self.forward = None


class dll:                  # Doubly linked list class
    def __init__(self):
        self.head = None

    def is_empty(self):
        if not self.head:
            return True
        return False


                            # BREAKING for today: there is a problem in this method
    def return_array(self):
        index = self.head
        output = []
        while index != None:
            index = index.forward
            output.append(index.data)
        return output

    def search(self, value):
        index = self.head
        found = False
        while temp != None:
            if temp.data == value:
                found = True
                break
            temp = temp.forward
        return found

                            # Add an item to the list, replacing the head with it

    def insert_head(self, value):
        new = dll_node(value)
        if self.is_empty():
            self.head = new
        else:
            new.forward = self.head
            self.head.back = new
            self.head = new



                            # Checks first character of value is a letter and treats it as if uppercase
def ascii_uppercase(char):
    ascii = ord(char)
    if ascii > 90:
        ascii -= 32

    if ascii <= 64 or ascii > 90:
        return None

    return ascii

                            # Checks value isn't empty, takes output of ascii_uppercase and converts that to 0-25
def get_index(value):

    if not value:
        return None

    firstchar = value[0]

    ascii = ascii_uppercase(firstchar)

    if not ascii:
        return None

    return ascii-65


                            # Fills table with null/None
def initialize(n):
    for slot in range(n):
        table.append(None)


                            # Adds given value to table using get_index to assign it a place
def addtotable(value):
    key = get_index(value)
    if not table[key]:
        table[key] = dll()
    table[key].insert_head(value)

                            # Outputs only those fields which are not empty
def display_table():
    for slot in range(len(table)):
        if table[slot]:
            output = chr(slot+65) + ": " + table[slot].return_array()
            print(output)




if __name__ == "__main__":

                            # Initialize the table with space for alphabetical filing
    initialize(26)
                            # Collisions! Joshua will be entered, but immediately overwritten... TO BE CONTINUED
    for name in ["Sage","Joshua","Robyn","Jason Donovan"]:
        addtotable(name)

    print(table)
    display_table()
