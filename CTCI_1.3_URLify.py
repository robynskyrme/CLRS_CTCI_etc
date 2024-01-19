# 19.1.2024
# CTCI Chapter 1 Q1.3

####### QUESTION: Write a method to replace all spaces in a string with '%20'

                            # There is a library function in Python to do this: $string.replace(" ","%20")
                            # e.g.
# def URLify(stringX):
#     stringX = stringX.replace(" ","%20")
#     return stringX

                            # Without using that function:

def URLify(stringX):
                            # create empty string
    newstring = ""
                            # just go through the string character by character
    for char in stringX:
                            # if a sppace is found, add the escape code
        if char == " ":
            newstring += "%20"
                            # otherwise just copy exactly
        else:
            newstring += char

    return newstring

if __name__ == "__main__":
    X = "What We Do Is Secret"

    print(URLify(X))