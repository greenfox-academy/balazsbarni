# Write a program that opens a file called "my-file.txt", then prints
# each of lines form the file.
# If the program is unable to read the file (for example it does not exists),
# then it should print an error message like: "Unable to read file: my-file.txt"


try:
    to_open = open("my-file.txt" , "r")
    print(to_open)
except FileNotFoundError:
    print("Unable to read file: my-file.txt")

