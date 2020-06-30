sequence = "AAATTCGGcaTTGCGgaaATcGAACGTAA"

# Logical Methods
print("All characters of sequence are alphabetic: ", sequence.isalpha())
print("All characters of sequence are alphanumeric: ", sequence.isalnum())
print("All characters of sequence are digits: ", sequence.isdigit())
print("All characters of sequence are numeric (including Unicode): ", sequence.isnumeric())
print("All characters of sequence are decimal-radix numbers (including Unicode): ", sequence.isdecimal())
print("All characters of sequence are lowercase: ", sequence.islower())
print("All characters of sequence are uppercase: ", sequence.isupper())
print("sequence starts with 'A': ", sequence.startswith("A"))
print("sequence ends with 'G': ", sequence.endswith("G"))

# Searching Methods
print("First index of 'ATTC' in sequence: ", sequence.find("ATTC"))  # returns -1 if it is not found
print("Last index of 'ATTC' in sequence: ", sequence.rfind("ATTC"))  # returns -1 if it is not found
print("First index of 'ATTC' in sequence: ", sequence.index("ATTC"))  # returns ValueError if it is not found
print("Last index of 'ATTC' in sequence: ", sequence.rindex("ATTC"))  # returns ValueError if it is not found
print("Number of occurrences of 'AT' in sequence: ", sequence.count("AT"))  # returns -1 if it is not found

# Replacing Methods
print("Replace 'AT' with 'GT' in sequence , "
      "\nOld sequence: ", sequence,
      "\nNew sequence: ", sequence.replace("AT", "GT"))
print("Replace 'AT' with 'GT' and delete 'C' in sequence: ",
      "\nOld sequence: ", sequence,
      "\nNew sequence: ",
      sequence.translate(sequence.maketrans("AT", "GT", "C")))  # Replaces 'AT' with 'GT' and deletes 'C'

# Changing Case Methods
print("Convert all characters of sequence to lowercase: ", sequence.lower())
print("Convert all characters of sequence to uppercase: ", sequence.upper())
print("Convert first character of sequence to uppercase: ", sequence.capitalize())
print("Each word in sequence beginning with an uppercase and the rest lowercase: ", sequence.title())
print("Convert lowercase character of sequence to uppercase, vice versa: ", sequence.swapcase())

# Reformatting Methods
print("Delete all the leading characters of 'A' in sequence", sequence.lstrip("A"))
print("Delete all the trailing characters of 'A' in sequence", sequence.rstrip("A"))
print("Delete all the leading and trailing characters of 'AT' in sequence", sequence.strip("AT"))
