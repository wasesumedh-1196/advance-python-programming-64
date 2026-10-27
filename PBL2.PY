# Program to remove blank lines from a text file

def remove_blank_lines(input_file, output_file):
    try:
        # Read the input file
        with open(input_file, "r") as file:
            lines = file.readlines()

        # Write non-blank lines to output file
        with open(output_file, "w") as file:
            for line in lines:
                if line.strip():
                    file.write(line)

        print("Blank lines removed successfully!")
        print("Cleaned content saved in", output_file)

    except FileNotFoundError:
        print("Error: Input file not found!")

    except IOError:
        print("Error while handling the file!")


# Main program
input_file = "input.txt"
output_file = "cleaned.txt"

remove_blank_lines(input_file, output_file)
