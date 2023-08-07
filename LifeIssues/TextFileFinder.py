# Step 1: Open the file
file_path = input("what is the path to the text file you want to analyze:\n")
exists = input("what would you like to know if it exists within the text file?\n")
try:
    with open(file_path, 'r') as file:
        # Step 2: Read the content of the file
        content = file.read()

        # Step 3: Check if exists exists in the text file
        if exists in content:
            print(exists, " exists in the file.")
        else:
            print(exists, " does not exist in the file.")
except FileNotFoundError:
    print("File not found or cannot be opened.")
except Exception as e:
    print("An error occurred:", e)
