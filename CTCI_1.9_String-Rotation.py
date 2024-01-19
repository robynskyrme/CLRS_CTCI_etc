# 19.1.2024
# CTCI Chapter 1 Q1.9

####### QUESTION: Assume you have a method isSubstring which checks if one word is a substring of another.
#######           Given s1 and s2 , write code to check if s2 is a rotation of s1 using only one call to isSubstring
#######           e.g. 'waterbottle' is a rotation of 'erbottlewat'


s1 = "waterbottle"
s2 = "erbottlewat"



def isRotation(s1,s2):
                            # Check they're the same length
    if len(s1) != len (s2):
        return False
                            # If they're identical, I guess that's a rotation of... len(s1). Or a 'do nothing' rotation
    if s1 == s2:
        return True

    length = len(s1)

    s1_last = s1[length-1]
    s1_first = s1[0]

    FoundFirstNextToLastInS2 = []


                            # List of occurences where the first and last of s1 ('WaterbottlE') appear (as 'EW')_ in s2...
    for char in range(length):
        if s2[char] == s1_last and s2[char+1] == s1_first:
            FoundFirstNextToLastInS2.append(char)

                            # If there are no such occurences, it's not a rotation, so quit
    if FoundFirstNextToLastInS2 == []:
        return False

                            # For each occurrence, check that what remains (in this case 'aterbottl') is a substring of s1
    for pos in FoundFirstNextToLastInS2:
        checkstring = s2[pos+2:length] + s2[0:pos]
#        print(checkstring)

                            # This would be the "one call" to isSubstring except that it's in a for loop of potential substrings...
        if isSubstring(s1,checkstring):
            return True

                            # If that never happens, it can't be a rotation
    return False


if __name__ == "__main__":
    isRotation("waterbottle","erbottlewat")