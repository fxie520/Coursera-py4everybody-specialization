import re


if __name__ == '__main__':
    s = 0  # Sum of numbers in the file
    with open('/Users/xiefeilian/PycharmProjects/Coursera'
              '/Py4Everybody/AssignmentData/Data_nb_extraction_real.txt', 'r') as file:
        for line in file:
            numbers = re.findall('[0-9]+', line)
            if numbers:
                numbers = [int(nb) for nb in numbers]
                s += sum(numbers)
    print(f"Sum of numbers = {s}")
