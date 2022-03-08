from curses.ascii import isdigit


def process(path):
    my_alt_list = []
    #myList = []  
    with open(path) as csv :
        while True : 
            currentLine = csv.readline().rstrip().split(", ")
            print(currentLine)
            if not currentLine :
                break
            my_alt_list.append(currentLine)

    print(my_alt_list)
    

        # for i in range(len(my_alt_list)):
        #     for j in range(len(my_alt_list[i])):
        #         if isdigit(my_alt_list[i][j]):
        #             myList.append(int(my_alt_list[i][j]))
           
    # number_of_each_row = len(my_alt_list[i].rstrip().split(', '))
    # number_of_col = len(my_alt_list)

    # with open("ans.csv" ,'w') as csvFile :
    #      print(number_of_col * number_of_each_row)
    #      sum = 0 
    #      for j in range(number_of_each_row * number_of_col):
    #             sum += myList[j]
    #             if j % number_of_each_row == 0 and j != 0 :
    #                 csvFile.write(str(sum))
    #                 csvFile.write("\n")
    #                 sum = 0 
    #                 pass
        
    #             csvFile.write(str(myList[j]))
    #             csvFile.write(", ")
                
  


process("test.csv")


    