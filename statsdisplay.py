
print("----------------------")
print("Statistics Exporter:")

# Function to check if the value entered is a value.
def validity_checknum(prompt, data_type=float):
  while True:
    try:
      return data_type(input(prompt))
    except ValueError:
         print("Incorrect input type, enter a value.")

# Initialising the final list displayed at the end of the program 
# (done here so the function below can recognise the variable)  
numlist = []

# Procedure to make values be repeatedly entered / or for exiting the program.
def repeat(numlist):
  repeat_val = validity_repeat()
  while repeat_val == "y":
    numlist.append(validity_checknum("Enter the next value you wish to record: ", float))
    repeat_val = validity_repeat()

# Function to find the median of the values entered. (I swear this took way too long)
def median(numlist):
  if not numlist:
   raise ValueError("Cannot find the median of an empty list.")
  
  listtemp = sorted(numlist)
  length = len(numlist)
  if length % 2 == 0:
    median_index1 = length // 2
    first_med = listtemp[median_index1 - 1]
    second_med = listtemp[median_index1]
    midpoint = (second_med - first_med) / 2
    return first_med + midpoint
  else: 
   median_index = length // 2
   return listtemp[median_index]


# Function to output list statistics when program is finished [for values with no assigned meaning].
def exit_program_numbers(numlist):
  sorted_version = sorted(numlist)
  highest_num = max(numlist)
  lowest_num = min(numlist)
  avg = sum(numlist) / len(numlist)
  median_val = median(numlist)
  num_range = highest_num - lowest_num
  print("A list of values recorded: ", numlist)
  print("Sorted version:", sorted_version)
  print("Largest value: ", highest_num)
  print("Smallest value: ", lowest_num)
  print("Median of values:", median_val)
  print("Mean of values:", avg)
  print("Range of values:", num_range)
  print("Logging complete, exiting program.")

def exit_program_currency(numlist):
  i = 0
  while i != len(numlist) - 1:
    numlist[i] = "£" + numlist[i]
    i += 1
  sorted_version = sorted(numlist)
  highest_num = max(numlist)
  lowest_num = min(numlist)
  avg = sum(numlist) / len(numlist)
  median_val = median(numlist)
  num_range = highest_num - lowest_num
  print("A list of values recorded: ", numlist)
  print("Sorted version:", sorted_version)
  print("Largest value: ", highest_num)
  print("Smallest value: ", lowest_num)
  print("Median of values:", median_val)
  print("Mean of values:", avg)
  print("Range of values:", num_range)
  print("Logging complete, exiting program.")


# Function to handle incorrect inputs by the user for the repeat variable.
def validity_repeat():
  while True:
    try:
      repeat = input("Would you like to enter another value? (y/n): ").strip().lower()
      if repeat == "y" or repeat == "n":
        return repeat
      else:
        raise ValueError("input must be either y or n.")
    except ValueError:
      print("Incorrect value entered, please enter either y or n.")


# The actual program.
decision = input("If you have the values stored in a text file, please paste in the file path here [If not, enter 0]: ")
if decision != 0:
  with open(decision, "r") as file:
    numlist = []
    for line in file:
        cleaned_line = line.strip()
        try:
            # Try to convert to float and add to the list
            numlist.append(float(cleaned_line))
        except ValueError:
            # If it's text or empty, ignore it and skip to the next line
            continue
  mode = input("What is the unit of measure used? [Enter c, t, d, or 0 for no unit of measure]: ")
  if mode == c:

  elif mode == t:
  
  elif mode == d:
  
  else:
    input_num = validity_checknum("Enter the value you wish to record: ", float)
    numlist.append(input_num)
    repeat(numlist)
    exit_program_numbers(numlist) 
else:
  mode = input("What is the unit of measure used? [Enter c, t, d, or 0 for no unit of measure]: ")
  if mode == c:

  elif mode == t:
  
  elif mode == d:
  
  else:
    input_num = validity_checknum("Enter the value you wish to record: ", float)
    numlist.append(input_num)
    repeat(numlist)
    exit_program_numbers(numlist) 

print("----------------------")
print("----------------------")
# The bars before and after the entire program don't actually do anything they just make everything look nice.