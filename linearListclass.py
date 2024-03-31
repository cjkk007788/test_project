class LinearList():
    
    def __init__(self):
        self.list = []
    
    def add_data(self,value):
        self.list.append(None)
        size_of_l = len(self.list)
        self.list[size_of_l-1] = value
        return

    def insert(self,position,value):
        
        list_size = len(self.list)
        
        if(position < 0 or position > list_size-1):
            return
        
        self.list.append(None)

        for k in range(len(self.list)-1,position,-1):
            self.list[k] = self.list[k-1]

        self.list[position] = value
        
        return
    
    def del_data (self,position):
        
        size_of_list = len(self.list)

        if position < 0 or position > len(self.list) -1:
            return
        
        for k in range(position,len(self.list)-1):
            self.list[k] = self.list[k+1]
        
        del self.list[len(self.list)-1]
        
    def Llist(self):
        print(self.list)
    
    
l_list = LinearList()

l_list.add_data("준규")
l_list.add_data("승규")
l_list.add_data("일구")
l_list.add_data("병장")
l_list.add_data("상병")

l_list.del_data(1)
l_list.del_data(1)
l_list.del_data(1)

l_list.insert(1,"전역")
l_list.Llist()
