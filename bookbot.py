import sys
#TODO: Cleanup the code

# Check number of passed arguments
if len(sys.argv) < 2:
    print("Usage: python bookbot.py <path_to_file>")
    sys.exit(1)
elif len(sys.argv) > 2:
    # print("Too many arguments.\nExpected: 1 argument\nActual: " + str(len(sys.argv) - 1) + " arguments(" + str(sys.argv[1:]) + ")")
    print(f"Too many arguments.\nExpected: 1 argument\nActual: {(len(sys.argv) - 1)} arguments ({sys.argv[1:]})")
    sys.exit(1)

# Set the path to the file
# TODO: Add config file which contains default books/ directory, so that the user can type just the filename
path_to_file = sys.argv[1]  

# Read the file
with open(path_to_file) as f:
    file_contents = f.read()

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

# Debugging
# print(f"Word count test: {word_count(file_contents)}")
# print(f"Letter count test: {letter_count(file_contents)}")

print(f"--- Begin report of {path_to_file} ---")
print(f"{word_count(file_contents)} words found in the file.\n")
for letter in sorted(letter_count(file_contents), reverse=True, key=letter_count(file_contents).get):
    print(f"{letter} found {letter_count(file_contents)[letter]} times.")
print("--- End of report ---")

    
