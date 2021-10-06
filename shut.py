import os 

class System_Operations:    
    def __init__(self,num):
        self.num = num
    
    def Operation(self):
        if self.num==1:
            print('-'*20, 'Restarting System', '-'*20)
            os.system('shutdown -t 5 r -f')
        
        elif self.num==2:
            print('-'*20, 'Shutting System Down', '-'*20)
            os.system('shutdown -t 5 -s -f')
        
        else:
            print('-'*20, 'Exiting', '-'*20)
            exit()


if __name__ == '__main__':
    print("Choose: \n1. Restart system \n2. Shutdown system \n3. Exit")
    option = input("Enter Your Choice: ")
    obj = System_Operations(option)
    obj.Operation()
