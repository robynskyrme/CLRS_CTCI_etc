# 23.1.2024
# First step of hash tables
# Assigns index in array based on position of first character in alphabet (0-25)


table = []

                            # Checks first character of value is a letter and treats it as if uppercsae
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
    table[key] = value

                            # Outputs only those fields which are not empty
def display_table():
    for slot in range(len(table)):
        if table[slot]:
            output = chr(slot+65) + ": " + table[slot]
            print(output)




if __name__ == "__main__":
                            # Initialize the table with space for alphabetical filing
    initialize(26)
                            # Collisions! Joshua will be entered, but immediately overwritten... TO BE CONTINUED
    for name in ["Sage","Joshua","Robyn","Jason Donovan"]:
        addtotable(name)

    print(table)
    display_table()