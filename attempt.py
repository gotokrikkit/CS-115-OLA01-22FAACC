from tkinter import filedialog, messagebox


def path_of_file():
  #  root = ask.Tk()
   # root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path


messagebox.showinfo(
    'Instructions', 'Please select inside the next window a txt file containing numbers in column\n' +
    '\nThis program will calculate the sum and the average of the numbers in the file')

# Function to open file dialog box and return the path of the selected file
file_path = path_of_file()

# Print the path of the selected file for the user
print(f"You selected {file_path}")
messagebox.showinfo(
    f'Info', f"You selected  {file_path}  \nPress OK to continue with the calculation")
with (open(file_path, 'r')) as file:  # Opens the file in read mode
    print(file.read())  # Prints the content of the file
    file.close()  # I need the file to be available for the next part

with (open(file_path, 'r')) as file:  # Same as before
    total = 0  # Variable to hold the aggregation for the sum
    count = 0  # Variable to hold the aggregation for the average
    totalav = 0.0   # Variable to hold the aggregation for the average
    for lines in file.readlines():  # loop aggregator with function call, it saves me one variable ;)
        # primitive incremental, yes I started my career with Commodore Basic
        count = count + 1   # Counting the numbers for the average
        total = total + int(lines)  # Summing the numbers for the total sum
    totalav = total/count   # Calculating the average
messagebox.showinfo(f"Results", f"The sum of all the numbers inside the file is {total}\n" +
                    f"the average of all the numbers inside the file is {totalav:.2f}")
print(
    f"\nThe sum of all the numbers inside the file is {total} and the average is {totalav:.2f}")  # Print the sum and the average
file.close()  # This makes sure the file is closed and available for the OS
