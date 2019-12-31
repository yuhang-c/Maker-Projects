# Generates the outputs
def digi_dis():
    # Gets the inputs
    number, digit = input("Number, Digit: ").split()
    # Creates variable and make sure their types are correct
    # Converts the number to a string
    num_str = str(number)
    # Makes the digit an integer
    dig_ct = int(digit)
    # Finds the length of the given number
    num_len = len(num_str)
    num_list = []
    # Finds the repetitions needed to get number segments
    i = num_len - dig_ct + 1
    j = 0
    # The result
    num_fin = 0
    # Loops through every segment in the number
    while j < i:
        # Get segments from the number string and convert it to int
        num_list.append(int(num_str[j:j+dig_ct]))
        j = j + 1
    # Adds together all numbers in num_list
    for x in num_list:
        num_fin = num_fin + x
    return 'Output: ' + str(num_fin) + '\nSegment List: ' + str(num_list)


# Runs the function 5 times
for _ in range(0, 5):
    print(digi_dis())
