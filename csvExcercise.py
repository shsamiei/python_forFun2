


from curses.ascii import isdigit


def process(path) :
        def csv_reader(path):
             with open(path) as csv:
              for row in csv.readlines():
                yield row.rstrip().split(', ')
     
        my_alt_list = []

        for i in csv_reader(path) : 
         my_alt_list.append(i)


        for  i in range(len(my_alt_list)):
            sum = 0 
            for j in range(len(my_alt_list[i])):
                sum += int(my_alt_list[i][j])
            my_alt_list[i].append(str(sum))


        with open("ans.csv" , 'w') as f:

            for i in range(len(my_alt_list)):
                for j in range(len(my_alt_list[i])):
                    f.write(my_alt_list[i][j])
                    if j != len(my_alt_list[i]) - 1 :
                        f.write(", ")
                pass
                f.write('\n')

            
process("test.csv")