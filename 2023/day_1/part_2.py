import re

# get the file
file = open('puzzle_input.txt', mode="r", buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
content = file.read()

spelled_out_numbers = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'zero': 0
}

# read each line and retroactively get just the numbers with regex
lines = content.split('\n')
final_numbers = []
for line in lines:
    # replace spelled out numbers with their digits
    for key, value in spelled_out_numbers.items(): 
        line = line.replace(key, str(value))

    # create an list of numbers
    line_numbers = re.findall(r'\d', line)

    # get the first and last values
    final_line_numbers = line_numbers[0] + line_numbers[-1]
    final_numbers.append(
        final_line_numbers
    )

final_answer = sum(int(x) for x in final_numbers)
print(final_answer)