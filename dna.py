from sys import argv, exit
import sys
import csv

# Check command-line arguments
if len(argv) != 3:
    print("missing command-line argument")
    exit(1)

# Open and read files
database_file = open(argv[1], "r")
sequences_file = open(argv[2], "r")

database_reader = csv.DictReader(database_file)
sequences = sequences_file.read()

database = [r for r in database_reader]

str_list = list(database[0])[1:]

# Close files
database_file.close()
sequences_file.close()


# Find longest_consecutive_substring
def longest_consecutive_substring(string, substring):
    current = 0
    longest = 0

    i = 0
    while i < len(string) - len(substring):
        if string[i:i + len(substring)] != substring:
            current = 0
            i += 1
            continue
        current += 1
        i += len(substring)
        if current > longest:
            longest = current
    return longest

sequence_dict = {}
for str_value in str_list:
    count = longest_consecutive_substring(sequences, str_value)
    sequence_dict[str_value] = count

# Print matching result
for person in database:
    for str_value in str_list:
        if person[str_value] != str(sequence_dict[str_value]):
            break
    else:
        print(person['name'])

        exit(0)

    continue

print("No match")

exit(0)
