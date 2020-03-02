#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Take input
file_name = input()
# file_name = "/home/atb00ker/Downloads/bin/hashcode/Hashcode2020/a_example"
# file_name = "/home/atb00ker/Downloads/bin/hashcode/Hashcode2020/b_read_on"
# file_name = "/home/atb00ker/Downloads/bin/hashcode/Hashcode2020/c_incunabula"
# file_name = "/home/atb00ker/Downloads/bin/hashcode/Hashcode2020/d_tough_choices"
# file_name = "/home/atb00ker/Downloads/bin/hashcode/Hashcode2020/e_so_many_books"
# file_name = "/home/atb00ker/Downloads/bin/hashcode/Hashcode2020/f_libraries_of_the_world"
ioInput = file_name + ".txt"
with open(ioInput, 'r') as file:
    books, libs, days = map(int, (file.readline()).split())
    scores = list(map(int, (file.readline()).split()))
    lib_info = [[] for _ in range(libs)]
    for i in range(libs):
        lbooks, lsign, lship = map(int, (file.readline()).split())
        lbooks_list = list(map(int, (file.readline()).split()))
        lib_info[i] = [lbooks, lsign, lship, lbooks_list, 0]


# In[2]:


# Associate Cost
for i in range(len(lib_info)):
    lib_tup = []
    for book in lib_info[i][3]:
        cost = scores[book]
        lib_tup.append(tuple([cost, book]))
    lib_info[i][3] = lib_tup


# In[3]:


# Sort books with cost / lib
for i in range(len(lib_info)):
    mbooks = lib_info[i][3]
    lib_info[i][3] = sorted(mbooks, key=lambda mbooks: mbooks[0], reverse=True)


# In[4]:


# Trim lists & get total profit
def calc_next_lib():
    max_profit = 0
    max_profit_index = 0
    for i in range(len(lib_info)):
        # Declare
        total_profit = 0
        mbooks = lib_info[i][3]
        ship = lib_info[i][2]
        sign = lib_info[i][1]
        # Trim
        can_ship = (days-sign) * ship
        mbooks = mbooks[:can_ship]
        # Profit
        for mbook in lib_info[i][3]:
            total_profit += mbook[0]
        # Enter back
        lib_info[i][3] = mbooks
        lib_info[i][4] = total_profit
        if max_profit < total_profit:
            max_profit = max(max_profit, total_profit)
            max_profit_index = i
    return max_profit_index


# In[5]:


# Decide libraries to send
send_lib = []
while days > 0:
    lib_index = calc_next_lib()
    sbook = lib_info[lib_index][3]
    if lib_info[lib_index][3] == [(0, 0)]:
        break
    if len(sbook) > 0:
        print (sbook)
        send_lib.append(tuple([lib_index, len(sbook), [book[1] for book in sbook]]))
    days = days - lib_info[lib_index][1]
    lib_info[lib_index][3] = [(0, 0)]


# In[6]:


# Create output
ioOutput = file_name + "_out.txt"
with open(ioOutput, 'w') as file:
    file.write(str(len(send_lib)) + "\n")
    for i in range(len(send_lib)):
        file.write(str(send_lib[i][0]) + " " + str(send_lib[i][1]) + "\n")
        fbooks = list(map(str, send_lib[i][2]))
        file.write(' '.join(fbooks) + "\n")
