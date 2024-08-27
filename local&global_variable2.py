import os

# Print the current working directory
print("Current working directory:")
print(os.getcwd())

# List all files and directories in the current working directory
print("\nFiles and directories in the current working directory:")
print(os.listdir())

# Create a new directory called test_dir
os.mkdir('test_dir')
print("\nCreated directory: test_dir")

# Change the working directory to test_dir
os.chdir('test_dir')
print("\nChanged working directory to:")
print(os.getcwd())

# Create a new file named test_file.txt inside test_dir
with open('test_file.txt', 'w') as f:
    f.write('This is a test file.')
print("\nCreated file: test_file.txt")

# Clean up: delete test_file.txt and test_dir
os.remove('test_file.txt')
print("\nDeleted file: test_file.txt")

os.chdir('..')  # Go back to the previous directory
os.rmdir('test_dir')
print("Deleted directory: test_dir")
