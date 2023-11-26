# Import the 'sub' function from the 're' module for regular expression substitution
from re import sub

# Define a function to convert a string to snake case
def snake_case(string):
    # Replace hyphens with spaces, then apply regular expression substitutions for title case conversion
    # and add an underscore between words, finally convert the result to lowercase
    return '_'.join(
        sub('([A-Z][a-z]+)', r' \1',
        sub('([A-Z]+)', r' \1',
        string.replace('-', ' '))).split()).lower()