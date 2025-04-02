# Ask the user for a filename
input_filename = input("Enter the filename to read: ")

try:
    # Open the file in read mode
    with open(input_filename, 'r') as infile:
        content = infile.read()
    
    # Modify the content (e.g., converting text to uppercase)
    modified_content = content.upper()

    # Write the modified content to a new file
    output_filename = 'modified_' + input_filename
    with open(output_filename, 'w') as outfile:
        outfile.write(modified_content)

    print(f"Modified content has been written to {output_filename}")

except FileNotFoundError:
    print(f"Error: The file '{input_filename}' does not exist.")
except PermissionError:
    print(f"Error: The file '{input_filename}' cannot be accessed due to insufficient permissions.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
