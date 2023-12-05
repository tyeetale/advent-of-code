import re

# get the file
file = open('puzzle_input.txt', mode="r", buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
content = file.read()

# print(content)
# read each line and retroactively get just the numbers with regex
lines = content.split('\n')
final_numbers = []

for line in lines:
    # create an list of numbers
    line_numbers = re.findall(r'\d', line)
    # print(line_numbers)
    # get the first and last values
    final_line_numbers = line_numbers[0] + line_numbers[-1]
    final_numbers.append(
        final_line_numbers
    )

final_answer = sum(int(x) for x in final_numbers)
print(final_answer)