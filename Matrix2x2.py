
class represent2𝑥2matrice:
    def __init__(self ,a00=0,a01=0,a10=0,a11=0):
        self.a00=a00
        self.a01=a01
        self.a10=a10
        self.a11=a11
    def display(self):
        return '{}\t{}\n{}\t{}'.format(self.a00,self.a01,self.a10,self.a11)
    def __add__(self, other):
        a00=self.a00+other.a00
        a01=self.a01+other.a01
        a10=self.a10+other.a10
        a11=self.a11+other.a11
        return represent2𝑥2matrice(a00, a01, a10, a11)
    def add(self,other):
        a00 = self.a00 + other.a00
        a01 = self.a01 + other.a01
        a10 = self.a10 + other.a10
        a11 = self.a11 + other.a11
        return represent2𝑥2matrice(a00, a01, a10, a11)

    def __str__(self):
        return '{}\t{}\n{}\t{}'.format(self.a00,self.a01,self.a10,self.a11)
    def prod(self,other):
        a00 = self.a00*other.a00 + self.a01*other.a10
        a01 = self.a00*other.a01 + self.a01*other.a11
        a10 = self.a10*other.a00 + self.a11*other.a10
        a11 = self.a10*other.a01 + self.a11*other.a11
        return represent2𝑥2matrice(a00, a01, a10, a11)
    def __mul__(self, other):
        a00 = self.a00 * other.a00 + self.a01 * other.a10
        a01 = self.a00 * other.a01 + self.a01 * other.a11
        a10 = self.a10 * other.a00 + self.a11 * other.a10
        a11 = self.a10 * other.a01 + self.a11 * other.a11
        return represent2𝑥2matrice(a00, a01, a10, a11)




