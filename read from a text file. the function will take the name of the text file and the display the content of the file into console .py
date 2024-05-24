
def read_the_content_in_the_file(filename):
    try:
        with open(filename,"r")as filename:
            cotent = filename.read()
        print(cotent)
    except FileNotFoundError:
        print(f"The given file {filename} as not found")

read_the_content_in_the_file('The countent file.txt')