#To Create the Student class which takes the names and numbers of 3 subjects as arguements in constructor.
#Then create a method to print the average

class Student:
    def __init__(self,name,num):
        self.name =name
        self.numbers=num
    
    #Average method
    def avg(self):
        total_num=0
        for val in self.numbers:
           total_num+=val          
        print( "Hi",self.name,"Your Average No. is:", total_num/3)

s1 =Student("Suhev Saifi",[78,89,91])  
'''print(s1.name)  
print(s1.numbers)  '''  
s1.avg()