# my method but it I din't add the function
# String = input("Enter the string, which you want to reverse:")
# reverseString = String[::-1]
# print(reverseString)
def reverseString(String):
    String = String[::-1]
    return String

def reverseStringTwo(String):
    StringTwo =""
    for i in String:
        StringTwo = i +StringTwo
    return StringTwo

