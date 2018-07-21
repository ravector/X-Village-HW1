import random

class Matrix:

    matrix=[]
    nrow=0
    ncol=0
    
    def __init__(self,nrow,ncol):
        self.nrow=nrow
        self.ncol=ncol
        self.matrix = [[random.randint(0, 9) for j in range(self.ncol)] for i in range(self.nrow)]
    
    def add(self,b):
        
        if self.nrow !=b.nrow or self.ncol !=b.ncol:
            print('Matrixs\' size should be in the same size')
                     
        else:
            self.matrix = [[self.matrix[i][j]+b.matrix[i][j] for j in range(self.ncol)] for i in range(self.nrow)]
            return self
    
    def sub(self,b):
        
        if self.nrow !=b.nrow or self.ncol !=b.ncol:
            print('Matrixs\' size should be in the same size')
        else:
            self.matrix = [[self.matrix[i][j]-b.matrix[i][j] for j in range(self.ncol)] for i in range(self.nrow)]
            return self
              
    def mul(self, b):
        
        if self.ncol !=b.nrow :
            print('不能相乘')
        
        else:
            e=Matrix(b.nrow,self.ncol)
            
            for i in range(self.nrow):
                for j in range(b.ncol):
                    value=0
                    for k in range(b.nrow):
                        value+=self.matrix[i][k]*b.matrix[k][j]
                        e.matrix[i][j]=value
            return e
        
    def transpose(self):
        
        f=Matrix(self.ncol,self.nrow)
        
        for i in range(self.nrow):
            for j in range(self.ncol):
                f.matrix[j][i]=self.matrix[i][j]
        return f

  
    def display(self):
        
        for i in range(self.nrow):
            for j in range(self.ncol):
                print(self.matrix[i][j],end='  ')
            print(' ')
        
a=int(input('enter A matrix\'s rows'))
b=int(input('enter A matrix\'s cols'))
A=Matrix(a,b)
A.display()
print(' ')
c=int(input('enter B matrix\'s rows'))
d=int(input('enter B matrix\'s cols'))
B=Matrix(c,d)
B.display()
print(' ')
print('------A+B=------')
C=A.add(B)
if a==c and b==d:
    C.display()
print('------A-B=------')
D=A.sub(B)
if a==c and b==d:
    D.display()
print('------A*B=------')
F=A.mul(B)
if b==c :
    F.display()
print('------the transpose of A*B=------')
if b==c :
    E=F.transpose()
    E.display()
else:
    print('(*´ー`)')  