# This Python script processes text from an input file (`clumped.txt`) to improve pronunciation of acronyms, and saves the modified text to an output file (`unclumped.txt`). Here’s a step-by-step explanation:

# 1. **Reading Input File**:
#    - Opens `clumped.txt` in read mode (`'r'`).
#    - Reads the entire content of the file into the `content` variable using `input_file.read()`.

# 2. **Function Definition (`separate_acronyms`)**:
#    - Defines a function `separate_acronyms(match)` that takes a regular expression match object (`match`) as input.
#    - This function joins the characters of the matched acronym (`match.group(0)`) with spaces, effectively separating each letter of the acronym with a space.

# 3. **Regular Expression Setup**:
#    - Imports the `re` module for regular expression operations.
#    - Defines a regular expression pattern (`pattern`) to find sequences of uppercase letters (`[A-Z]+`) that are bounded by word boundaries (`\b`).

# 4. **Substitution**:
#    - Uses `re.sub(pattern, separate_acronyms, content)` to perform a substitution operation on `content`.
#    - The `sub` function replaces each match of `pattern` in `content` with the result of `separate_acronyms(match)`, effectively inserting spaces between the letters of each acronym found.

# 5. **Writing Output File**:
#    - Opens `unclumped.txt` in write mode (`'w'`).
#    - Writes the modified `content`, where acronyms are separated by spaces, to `output_file`.

# 6. **Final Output**:
#    - Prints a message confirming that acronyms have been separated and saved in `unclumped.txt`.

# ### Summary:
# This script is useful for improving the pronunciation of acronyms by inserting spaces
#  between the letters of each acronym found in the input text file (`clumped.txt`). 
#  It uses regular expressions to identify and modify the text,
#  ensuring that each acronym is easier to pronounce in AI-generated voiceovers or other text-to-speech applications.




# Open the input file for reading
with open('clumped.txt', 'r') as input_file:
    # Read the content of the file
    content = input_file.read()

# Function to separate acronyms
def separate_acronyms(match):
    return ' '.join(match.group(0))

# Import the regular expression module
import re

# Use a regular expression to find capitalized acronyms
pattern = r'\b([A-Z]+)\b'
content = re.sub(pattern, separate_acronyms, content)

# Open the output file for writing
with open('unclumped.txt', 'w') as output_file:
    # Write the modified content to the output file
    output_file.write(content)

print("Acronyms separated and saved in unclumped.txt")
