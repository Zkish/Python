# Step 1: Open the file
file_path = "path to the text file"
try:
    with open(file_path, 'r') as file:
        # Step 2: Read the content of the file
        content = file.read()

        # Step 3: Check if 'Python' exists in the content
        # edit the if statement with what you want to know if it exists within the file.
        if 'enter what to find here' in content:
            print("'Python' exists in the file.")
        else:
            print("'Python' does not exist in the file.")
except FileNotFoundError:
    print("File not found or cannot be opened.")
except Exception as e:
    print("An error occurred:", e)
