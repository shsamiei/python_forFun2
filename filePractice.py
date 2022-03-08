
def solve(address_of_file) :
    mylist = []
    with open(address_of_file , 'r') as f :
        while True : 
            current_line = f.readline()
            if not current_line : 
                break
            mylist.append(current_line)

    myClear_list = making_file_clear(mylist)
    number_of_meaningful_lines = counter_of_meaningful_lines(myClear_list)
    return number_of_meaningful_lines


def counter_of_meaningful_lines(yourlist):
    import re 
    my_regex_algo = '^[#\n]+'
    counter = 0
    for i in range(len(yourlist)) :
        if(re.search(my_regex_algo,yourlist[i])):
            counter += 1 
    return len(yourlist) - counter
    
    


def making_file_clear(yourlist):
    for i in range(len(yourlist)) :
        mystring = yourlist[i].strip()
        mystring += "\n"
        yourlist[i] = mystring
    return yourlist



print(solve("text_for_practice.txt"))