

class mineSwaper :
    maps = [] 
    def __init__(self , row , col ):
        
        self.row = row
        self.col = col 

        for i in range(self.col) :
            mineSwaper.maps.append([])
            for j in range(self.row):
                mineSwaper.maps[i].append(0)
            

    def getList(self):
        return mineSwaper.maps 

    def BombIt(self ,x ,y):
        mineSwaper.maps[x][y] = "*"
        mineSwaper.up_adjacent(self,x,y)
        pass



    def up_adjacent(self,x,y) :
         pos = [-1, 0, 1]
         for i in pos:
                for j in pos:
                    if i != 0 or j != 0:
                        if ((x + i) >= 0 and (x + i) < self.col ) and ( (y+j) >= 0 and (y+j) < self.row ):
                            if mineSwaper.maps[x+i][y+j] != "*" :
                                 mineSwaper.maps[x+i][y+j] += 1
       
        
x = int(input())
y = int(input())

mswap = mineSwaper(x,y) 
mswap.BombIt(3,3)
mswap.BombIt(0,2)
mswap.BombIt(1,2)
mswap.BombIt(1,0)
mswap.BombIt(0,0)
# mswap.BombIt(1,1)
res = mswap.getList()

for  i in range(y) :
    for  j in range(x) :
        print(res[j][i],' ' , end='')
    print()




