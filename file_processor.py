def process_file():
    """
    Reads a file, modifies its content, and writes to a new file.
    Handles errors if the file doesn't exist or can't be read.
    """
    # Ask user for input filename
    input_filename = input("Enter the name of the file to read: ")
    
    try:
        # Try to open and read the file
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
            
            # Print confirmation and file stats
            print(f"\nSuccessfully read file: {input_filename}")
            print(f"File contains {len(content)} characters and {len(content.split())} words.")
            
            # Ask for output filename
            output_filename = input("\nEnter the name for the modified output file: ")
            
            # Ask for modification type
            print("\nChoose a modification to apply:")
            print("1. Convert to uppercase")
            print("2. Convert to lowercase")
            print("3. Add line numbers")
            print("4. Replace a word")
            
            choice = input("Enter your choice (1-4): ")
            
            # Apply the selected modification
            if choice == '1':
                modified_content = content.upper()
                modification_type = "Converted to uppercase"
            elif choice == '2':
                modified_content = content.lower()
                modification_type = "Converted to lowercase"
            elif choice == '3':
                lines = content.split('\n')
                modified_content = '\n'.join(f"{i+1}: {line}" for i, line in enumerate(lines))
                modification_type = "Added line numbers"
            elif choice == '4':
                word_to_replace = input("Enter the word to replace: ")
                replacement_word = input("Enter the replacement word: ")
                modified_content = content.replace(word_to_replace, replacement_word)
                modification_type = f"Replaced '{word_to_replace}' with '{replacement_word}'"
            else:
                print("Invalid choice. Using original content.")
                modified_content = content
                modification_type = "No modification (invalid choice)"
            
            # Write modified content to output file
            try:
                with open(output_filename, 'w') as output_file:
                    output_file.write(modified_content)
                print(f"\nSuccess! {modification_type}.")
                print(f"Modified content written to: {output_filename}")
            except IOError as e:
                print(f"\nError writing to output file: {e}")
                
    except FileNotFoundError:
        print(f"\nError: The file '{input_filename}' was not found.")
        print("Please check that the filename is correct and try again.")
    except PermissionError:
        print(f"\nError: You don't have permission to read '{input_filename}'.")
    except IOError as e:
        print(f"\nError reading file: {e}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
    finally:
        print("\nFile processing operation completed.")

if __name__ == "__main__":
    print("=== File Read & Write Challenge with Error Handling ===")
    process_file()
    
    # Ask if user wants to process another file
    while input("\nWould you like to process another file? (y/n): ").lower() == 'y':
        process_file()
    
    print("\nThank you for using the File Processor. Goodbye!")
