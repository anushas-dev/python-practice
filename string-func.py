# Find char's codepiont
ch = input("Enter a character: ")
print("Codepoint for",ch, "is",ord(ch))

# Find the char at its codepoint
cp = int(input("Enter the codepoint: "))
print("Char for",cp, "is",chr(cp))

# capitalize the given string
str1 = input("Enter a string to capitalize: ")
print(str1.capitalize())

# pad the string with char
str2 = input("Enter a string to pad: ")
print(str2.center(len(str2)+6,'*'))

# check whether provided string in alpha numeric, just alpha or numeric
str3 = input("Enter any string: ")
if(str3.isalnum() and not (str3.isalpha() or str3.isdigit())):
    print("The given string is alpha numeric")
if(str3.isalpha()):
    print("The given string contains alpha only")
if(str3.isdigit()):
    print("The given string is numeric only")
