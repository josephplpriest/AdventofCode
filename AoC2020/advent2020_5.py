def find_row_number(ticket_start:str) -> int:
    nums = list(range(0,128))

    for letter in ticket_start:
        if letter == "F":
            nums = nums[:len(nums)//2]
        else:
            nums = nums[len(nums)//2:]

    return nums[0] * 8

def find_col_number(ticket_end:str) -> int:
    nums = list(range(0,8))

    for letter in ticket_end:
        if letter == "L":
            nums = nums[:len(nums)//2]
        else:
            nums = nums[len(nums)//2:]

    return nums[0]

with open("input5.txt") as file:
    tickets = file.read().splitlines()

max_seat_num = 0
seat_list = []

for ticket in tickets:
    row_num = find_row_number(ticket[0:7])
    col_num = find_col_number(ticket[7:])
    seat_num = row_num + col_num
    if seat_num > max_seat_num:
        max_seat_num = seat_num
    seat_list.append(seat_num)


possible_seats = set([x+y*8 for x in range(7) for y in range(128)])

s = sorted(seat_list)

for i in range(1000):
    if i not in seat_list:
        print(i)