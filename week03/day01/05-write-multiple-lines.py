# Create a function that takes 3 parameters: a path, a word and a number,
# than it should write to a file.
# The path parameter should be a string, that describes the location of the file.
# The word parameter should be a string, that will be written to the file as lines
# The number paramter should describe how many lines the file should have.
# So if the word is "apple" and the number is 5, than it should write 5 lines
# to the file and each line should be "apple"
# The function should not raise any error if it could not write the file.


def write_to_file():
    try:
        path_parameter = input('Enter path: ')
        word_parameter = str(input("Enter the text: "))
        line_parameter = int(input("Enter the number of lines: "))
        created_file = open(path_parameter, "a")
        for i in range(line_parameter):
            created_file.write(word_parameter)
            created_file.write("\n")
    except Exception:
        print("")

write_to_file()
