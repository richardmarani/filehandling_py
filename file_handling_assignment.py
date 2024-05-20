# file_handling_assignment.py
def write_to_file(filename):
    try:
        # Try to create a new file and open it in write mode ('w')
        with open(filename, "w") as file:
            # Write three lines of text to the file
            file.write("This is a weekend special.\n")
            file.write("Here is the number 123.\n")
            file.write("Python file handling is fun!\n")
    except FileNotFoundError:
        # Handle any file-related errors (e.g., file not found or permission denied)
        print(f"Error: file '{filename}' not found")
    except PermissionError:
        # This block always executes, even if an error occurs
        print("F Error: permission denied to write to '{filename}'.")
    except Exception as e:
        print (f"Error:{e}")
    else:
        print('File created and written succesfully.')
        
def read_and_display(filename):
    try:
        with open(filename, 'r') as f:
            contents = f.read()
            print("contents of 'my_file.txt':")
        # Print the content of the file to the console
        print(contents)
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print(f"Error: permission denied to read from '{filename}'.")
    except PermissionError as e:
        # Handle permission errors
        print(f"Error:{e}")
    
def append_to_file(filename):
    try:
        # Try to open the file in append mode ('a')
        with open(filename, 'a') as file:
            # Append three additional lines of text to the file
            file.write("Appending a new line.\n")
            file.write("Another line with number 456.\n")
            file.write("File handling in Python is powerful.\n")
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print(f"Error: File '{filename}' not found")
    except PermissionError:
        # Handle permission errors
        print(f"Error:{e}") # type: ignore
    else:
        print("File appended successfully")
        # This block always executes, even if an error occurs
        print("Exiting append_to_file function.")
# Check if this script is being run directly (not imported as a module)
if __name__ == "__main__":
    filename = "my file.txt"
    write_to_file(filename) 
    
    # Reading and displaying the file
    read_and_display(filename) # type: ignore

    # Append in the file
    append_to_file(filename)


