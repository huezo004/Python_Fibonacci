'''def main():'''

class Fibonacci: 

   def __init__(self, num):
     self.num=num 
     self.n=0
     self.num0=0
     self.num1=1

   def __iter__(self):
	return self
 
   def next(self):
    f=self.num0
    if self.n > self.num-1:
	raise StopIteration
    self.num0, self.num1=self.num1, self.num0+self.num1
    self.n+=1
    return f
         	
   def get_nums(self):
     num0=0
     num1=1
     l1=[0,1]
     n=0

     while n != self.num-2:
	l1.append(l1[num0]+l1[num1])
 	num0+=1
        num1+=1
	n+=1 
     return l1

   def __str__(self):
    return "The first " + str(self.num) + " Fibonacci numbers are " +str(self.get_nums())



def fibonacci_gen(nums):
     num0=0
     na,nb= 0,1 
     while num0 != nums:
	yield na
	na, nb = nb, na+nb
        num0+=1

"""	
f= Fibonacci(3) 
print 

for i in fibonacci_gen(12):
   print i, 


if __name__=="__main__":
	main()
"""	
