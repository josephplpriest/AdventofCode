## Part 1
"""Read in password requirements and passwords and determine if they are valid.
Format:
--n chars required--  --char--      --pwd--
        1-3             x:          x;lkjasdfxx          #valid pwd as it contains 3 'x' chars
        3-5             a:          a;lkjfda            #invalid pwd as it only has 2 'a' chars

Return:
number of valid passwords from the list of reqs and pwds
"""


# with open("input2.txt") as file:
#     passwords = file.readlines()


# passwords = [pwd.split(' ') for pwd in passwords]

# start_end = [tuple(map(int, line[0].split('-'))) for line in passwords]

# chars = [line[1].strip(":") for line in passwords]

# pwds = [line[-1].strip() for line in passwords]

# valid_pwds = 0

# for s_e, char, pwd, i in zip(start_end, chars, pwds, range(len(pwds))):
#     start, end = s_e

#     n_chars = pwd.count(char)
#     if start <= n_chars <= end:
#         valid_pwds += 1
#         print(passwords[i])


# print(valid_pwds)



##Part 2
"""
Instead, the numbers refer to indices in the password and 
exactly ONE of the two locations must contain the char. They
do NOT use zero indexing to the 0th character will be the first.

New Format:
--n chars required--  --char--      --pwd--
        1-3             x:          x;lkjasdfxx          #valid pwd as it 'x' char at position 1
        3-5             a:          a;lkjfda            #invalid pwd as it only has 2 'a' chars

Return:
number of valid passwords from the list of reqs and pwds

"""


with open("input2.txt") as file:
    passwords = file.readlines()


passwords = [pwd.split(' ') for pwd in passwords]



start_end = [tuple(map(int, line[0].split('-'))) for line in passwords]

chars = [line[1].strip(":") for line in passwords]

pwds = [line[-1].strip() for line in passwords]

valid_pwds = 0

for s_e, char, pwd, i in zip(start_end, chars, pwds, range(len(pwds))):
    start, end = s_e
    start -= 1
    end -= 1
    if (int(pwd[start]==char) + int(pwd[end]==char)) == 1:
        valid_pwds += 1
    

print(valid_pwds)