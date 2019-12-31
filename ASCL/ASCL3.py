import math


# Checks if the block is outside of the right boundary
def in_row_lr(row, number_start, number_end):
    # Finds the row of the starting number
    current_row = math.ceil(float(number_start) / float(row))
    # Checks if the starting or ending number is greater than the last number in the row
    if (number_end <= current_row * row) & (number_start <= current_row * row):
        return 1
    else:
        return 0


# Checks if the block is outside of the left boundary
def in_row_rl(row, number_start, number_end):
    # Finds the row above the starting number
    current_row = math.ceil(float(number_start) / float(row) - 1)
    # Check if the starting or ending number is in the previous row
    if (number_end >= current_row * row) & (number_start >= current_row * row):
        return 1
    else:
        return 0


# Checks if the numbers are greater than the largest number on the grid
def in_col_ud(row, column, number_start, number_end):
    if (number_end > column * row) or (number_start > column * row):
        return 0
    else:
        return 1


# Checks if the numbers are less than zero
def in_col_du(number_start, number_end):
    if (number_end < 0) or (number_start < 0):
        return 0
    else:
        return 1


# Checks if piece A can be placed from left to right and whether or not it is blocked
def try_A_lr(start, row, column, block):
    # Ending tile
    end = -1
    # Indicates if the finishing tile works and does not run into a block
    fin_works = 1
    works = 0
    # Checks if there are blocks
    if len(block) > 0:
        # Checks if the piece is in boundary and does not run into a block, returns an ending tile if it works
        for i in block:
            j = int(i)
            if (start != j) & (start + 1 != j) & (start + 2 != j) & in_row_lr(row, start, start +2):
                works = 1
                end = start + 2
            else:
                fin_works = 0
    else:
        # Checks if the piece is in boundary, returns an ending tile if it works
        if in_row_lr(row, start, start + 2):
            works = 1
            end = start + 2
        else:
            fin_works = 0
    works = fin_works * works
    # Returns the ending tile and whether or not the block worked
    result = [end, works]
    return result


# Checks if piece B can be placed from left to right and whether or not it is blocked
def try_B_lr(start, row, column, block):
    end = -1
    fin_works = 1
    works = 0
    if len(block) > 0:
        for i in block:
            j = int(i)
            if (start != j) & (start + row != j) & (start + row + 1 != j) & in_col_ud(row, column, start, start + row) & in_row_lr(row, start + row, start + row + 1):
                works = 1
                end = start + row + 1
            else:
                fin_works = 0
    else:
        if in_col_ud(row, column, start, start + row) & in_row_lr(row, start + row, start + row + 1):
            works = 1
            end = start + row + 1
        else:
            fin_works = 0
    works = fin_works * works
    result = [end, works]
    return result


# Checks if piece C can be placed from left to right and whether or not it is blocked, returns ending tile if it works
def try_C_lr(start, row, column, block):
    end = -1
    fin_works = 1
    works = 0
    if len(block) > 0:
        for i in block:
            j = int(i)
            if (start != j) & (start + 1 != j) & (start + row + 1 != j) & (start + row * 2 + 1 != j) & in_col_ud(row, column, start, start + row * 2 + 1) & in_row_lr(row, start, start + 1):
                works = 1
                end = start + row * 2 + 1
            else:
                fin_works = 0
    else:
        if in_col_ud(row, column, start, start + row * 2 + 1) & in_row_lr(row, start, start + 1):
            works = 1
            end = start + row * 2 + 1
        else:
            fin_works = 0
    works = fin_works * works
    result = [end, works]
    return result


# Checks if piece A can be placed from right to left and whether or not it is blocked, returns ending tile if it works
def try_A_rl(start, row, column, block):
    end = -1
    fin_works = 1
    works = 0
    if len(block) > 0:
        for i in block:
            j = int(i)
            if (start != j) & (start - 1 != j) & (start - 2 != j) & in_row_rl(row, start, start - 2):
                works = 1
                end = start - 2
            else:
                fin_works = 0
    else:
        if in_row_rl(row, start, start - 2):
            works = 1
            end = start - 2
        else:
            fin_works = 0
    works = fin_works * works
    result = [end, works]
    return result


# Checks if piece B can be placed from right to left and whether or not it is blocked, returns ending tile if it works
def try_B_rl(start, row, column, block):
    end = -1
    fin_works = 1
    works = 0
    if len(block) > 0:
        for i in block:
            j = int(i)
            if (start != j) & (start - 1 != j) & (start - row - 1 != j) & in_col_du(start, start - row - 1) & in_row_rl(row, start, start - 1):
                works = 1
                end = start - row - 1
            else:
                fin_works = 0
    else:
        if in_col_du(start, start - row -1) & in_row_rl(row, start, start - 1):
            works = 1
            end = start - row - 1
        else:
            fin_works = 0
    works = fin_works * works
    result = [end, works]
    return result


# # Checks if piece C can be placed from right to left and whether or not it is blocked, returns ending tile if it works
def try_C_rl(start, row, column, block):
    end = -1
    fin_works = 1
    works = 0
    if len(block) > 0:
        for i in block:
            j = int(i)
            if (start != j) & (start - row != j) & (start - row * 2 != j) & (start - row * 2 - 1 != j) & in_col_du(start, start - row * 2 - 1) & in_row_rl(row, start, start - 1):
                works = 1
                end = start - row * 2 - 1
            else:
                fin_works = 0
    else:
        if in_col_du(start, start - row * 2 - 1) & in_row_rl(row, start, start - 1):
            works = 1
            end = start - row * 2 - 1
        else:
            fin_works = 0
    works = fin_works * works
    result = [end, works]
    return result


# Returns the letter sequence when the pieces start from the right
def try_rl(start, row, column, block):
    result = ""
    i = -100
    # Tries which piece works at the start. Goes in order from A to B to C
    if try_A_rl(start, row, column, block)[1]:
        # Adds the working piece to the result string
        result = result + "A"
        # Tracks the current tile to start from A
        crt_tile = try_A_rl(start, row, column, block)[0]
        # Generates the rest of the sequence
        while i < 15:
            # Checks if each piece works continuing from A
            if try_B_rl(crt_tile - 1, row, column, block)[1]:
                result = result + "B"
                # Updates current tile
                crt_tile = try_B_rl(crt_tile - 1, row, column, block)[0]
                # Checks if the pieces have reached the end
                if crt_tile % row == 1:
                    return result
            if try_C_rl(crt_tile - 1, row, column, block)[1]:
                result = result + "C"
                crt_tile = try_C_rl(crt_tile - 1, row, column, block)[0]
                if crt_tile % row == 1:
                    return result
            if try_A_rl(crt_tile - 1, row, column, block)[1]:
                result = result + "A"
                crt_tile = try_A_rl(crt_tile - 1, row, column, block)[0]
                if crt_tile % row == 1:
                    return result
            i = i + 1
    else:
        if try_B_rl(start, row, column, block)[1]:
            result = result + "B"
            crt_tile = try_B_rl(start, row, column, block)[0]
            while i < 15:
                if try_C_rl(crt_tile - 1, row, column, block)[1]:
                    result = result + "C"
                    crt_tile = try_C_rl(crt_tile - 1, row, column, block)[0]
                    if crt_tile % row == 0:
                        return result
                if try_A_rl(crt_tile - 1, row, column, block)[1]:
                    result = result + "A"
                    crt_tile = try_A_rl(crt_tile - 1, row, column, block)[0]
                    if crt_tile % row == 0:
                        return result
                if try_B_rl(crt_tile - 1, row, column, block)[1]:
                    result = result + "B"
                    crt_tile = try_B_rl(crt_tile - 1, row, column, block)[0]
                    if crt_tile % row == 0:
                        return result
                i = i + 1
        else:
            if try_C_rl(start, row, column, block)[1]:
                result = result + "C"
                crt_tile = try_C_rl(start, row, column, block)[0]
                while i < 15:
                    if try_A_rl(crt_tile - 1, row, column, block)[1]:
                        result = result + "A"
                        crt_tile = try_A_rl(crt_tile - 1, row, column, block)[0]
                        if crt_tile % row == 0:
                            return result
                    if try_B_rl(crt_tile - 1, row, column, block)[1]:
                        result = result + "B"
                        crt_tile = try_B_rl(crt_tile - 1, row, column, block)[0]
                        if crt_tile % row == 0:
                            return result
                    if try_C_rl(crt_tile - 1, row, column, block)[1]:
                        result = result + "C"
                        crt_tile = try_C_rl(crt_tile - 1, row, column, block)[0]
                        if crt_tile % row == 0:
                            return result
                    i = i + 1


# Returns the letter sequence when the pieces start from the left
def try_lr(start, row, column, block):
    result = ""
    i = 1
    if try_A_lr(start, row, column, block)[1]:
        result = result + "A"
        crt_tile = try_A_lr(start, row, column, block)[0]
        while i < 15:
            if try_B_lr(crt_tile + 1, row, column, block)[1]:
                result = result + "B"
                crt_tile = try_B_lr(crt_tile + 1, row, column, block)[0]
                if crt_tile % row == 0:
                    return result
            if try_C_lr(crt_tile + 1, row, column, block)[1]:
                result = result + "C"
                crt_tile = try_C_lr(crt_tile + 1, row, column, block)[0]
                if crt_tile % row == 0:
                    return result
            if try_A_lr(crt_tile + 1, row, column, block)[1]:
                result = result + "A"
                crt_tile = try_A_lr(crt_tile + 1, row, column, block)[0]
                if crt_tile % row == 0:
                    return result
            i = i + 1
    else:
        if try_B_lr(start, row, column, block)[1]:
            result = result + "B"
            crt_tile = try_B_lr(start, row, column, block)[0]
            while i < 15:
                if try_C_lr(crt_tile + 1, row, column, block)[1]:
                    result = result + "C"
                    crt_tile = try_C_lr(crt_tile + 1, row, column, block)[0]
                    if crt_tile % row == 0:
                        return result
                if try_A_lr(crt_tile + 1, row, column, block)[1]:
                    result = result + "A"
                    crt_tile = try_A_lr(crt_tile + 1, row, column, block)[0]
                    if crt_tile % row == 0:
                        return result
                if try_B_lr(crt_tile + 1, row, column, block)[1]:
                    result = result + "B"
                    crt_tile = try_B_lr(crt_tile + 1, row, column, block)[0]
                    if crt_tile % row == 0:
                        return result
                i = i + 1
        else:
            if try_C_lr(start, row, column, block)[1]:
                result = result + "C" + str(start)
                crt_tile = try_C_lr(start, row, column, block)[0]
                while i < 15:
                    if try_A_lr(crt_tile + 1, row, column, block)[1]:
                        result = result + "A"
                        crt_tile = try_A_lr(crt_tile + 1, row, column, block)[0]
                        if crt_tile % row == 0:
                            return result
                    if try_B_lr(crt_tile + 1, row, column, block)[1]:
                        result = result + "B"
                        crt_tile = try_B_lr(crt_tile + 1, row, column, block)[0]
                        if crt_tile % row == 0:
                            return result
                    if try_C_lr(crt_tile + 1, row, column, block)[1]:
                        result = result + "C"
                        crt_tile = try_C_lr(crt_tile + 1, row, column, block)[0]
                        if crt_tile % row == 0:
                            return result
                    i = i + 1


# Generates results from input
def int_stretch():
    # Asks for input
    input_data = input("number of rows, number of columns, start, blocks: ").split(" ")
    # Take the first variables out of the list so only blocked tiles are left
    column = int(input_data.pop(0))
    row = int(input_data.pop(0))
    start = int(input_data.pop(0))
    input_data.pop(0)
    block = input_data
    # Checks if the pieces start from left or right
    if start % row == 0:
        return str(try_rl(start, row, column, block))[::-1]
    else:
        return try_lr(start, row, column, block)


# Runs the int_stretch() function 5 times
for _ in range(0, 5):
    print(int_stretch())
