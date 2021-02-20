import math
import random

class Vector:
    x1 = 0
    y1 = 0
    z1 = 0

    def __init__(self, x, y, z):
        self.x1 = x
        self.y1 = y
        self.z1 = z

    def vectorLength(self, x2=float('nan'), y2=float('nan'), z2=float('nan')):
        if(math.isnan(x2) and math.isnan(y2) and math.isnan(z2)):
            return math.sqrt(math.pow(self.x1, 2) + math.pow(self.y1, 2) + math.pow(self.z1, 2))
        else:
            return math.sqrt(math.pow(x2, 2) + math.pow(y2, 2) + math.pow(z2, 2))

    def scalarMultiplication(self, x2, y2, z2):
        return self.x1*x2+self.y1*y2+self.z1*z2

    def vectorData(self):
        return self.x1, self.y1, self.z1

    def multiplicationOf_a_VectorWithAnotherVector(self, x2, y2, z2):
        return self.y1*z2-self.z1*y2, self.z1*x2-self.x1*z2, self.x1*y2-self.y1*x2

    def angle(self, x, y, z):
        return math.degrees(math.acos((self.scalarMultiplication(x, y, z))/(math.fabs(self.vectorLength())*math.fabs(self.vectorLength(x2=x, y2=y, z2=z)))))

    def sumVector(self, x2, y2, z2):
        return self.x1+x2, self.y1+y2, self.z1+z2

    def differenceVector(self, x2, y2, z2):
        return self.x1-x2, self.y1-y2, self.z1-z2
def vectorGenerate(count):
    massive=[]
    for i in range(count):
        
        x=random.uniform(-100,100)
        y=random.uniform(-100,100)
        z=random.uniform(-100,100)
        massive.append([x,y,z])
    return massive

print(vectorGenerate(5))