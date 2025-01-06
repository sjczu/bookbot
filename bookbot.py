import sys
import json

# Check number of passed arguments
if len(sys.argv) < 2:
    print("Usage: python bookbot.py <filename>")
    sys.exit(1)
elif len(sys.argv) > 2:
    print(f"Too many arguments.\nExpected: 1 argument\nActual: {(len(sys.argv) - 1)} arguments ({sys.argv[1:]})")
    sys.exit(1)

config_path = "./config.json"

# Load the configuration file and assign bookpath value to variable
with open(config_path, 'r') as config_file:
    config = json.load(config_file)

bookpath = config.get("bookpath")

# Set the path to the file
filename = f"{sys.argv[1]}.txt"
full_path = f"{bookpath}/{filename}"

# Read the file
with open(full_path,'r') as book:
    file_contents = book.read()

# Function to count the number of words in a file
def word_count(file_contents):
    word_count = 0
    for line in file_contents.splitlines():
        for word in line.split():
            word_count += 1
    return word_count

# Function to count the number of occurences per letter in a file
def letter_count(file_contents):
    letter_count_dir = {}
    for line in file_contents.splitlines():
        for word in line.lower().split():
            for letter in word:
                if letter.isalpha():
                    if letter in letter_count_dir:
                        letter_count_dir[letter] += 1
                    else:
                        letter_count_dir[letter] = 1
    return letter_count_dir

# Book report printout
print(f"--- Begin report of {filename} ---")
print(f"{word_count(file_contents)} words found in the file.\n")
for letter in sorted(letter_count(file_contents), reverse=True, key=letter_count(file_contents).get):
    print(f"{letter} found {letter_count(file_contents)[letter]} times.")
print("--- End of report ---")

    
