def counting_words(filename):
    try:
        #from the other lab, the below reads the demonstrates reading from a file:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
        # now we have to find the how many words are in the file. So do so, we using: The split() method splits a string into a list.
        # https://www.w3schools.com/PYTHON/ref_string_split.asp
        # content.split() splits the string content into a list of words based on whitespace
            total_words = content.split()
        # to find the length of the list we use len(). len()  counts how many words are in that list.
            return len(total_words)
    except FileNotFoundError:
        print(f"Error: '{filename}' was not found.")
        return 

print(f"File contains: {counting_words('sample.txt')} words")
print(counting_words('new_sample.txt'))


def writing_lines_with_scripts(*words):
#Take a list of strings.
    with open("output.txt", "w") as file:
    #Write each string to a new line in a file named output.txt.
    # we are using a loop to through the string so that it then appends the text to the file. 
        for word in words:
            file.write(word + "\n") 
        #This writes the current string to the file, followed by a newline character ("\n"). The newline character ensures each string is written on a separate line. 

writing_lines_with_scripts("Hello, world!", "Python is better than c++.")
