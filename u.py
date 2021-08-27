from math import sqrt, fsum

AU = 149597870700.0     # Астрономическая единица (м)
G = 6.67408E-11         # Гравитационная постоянная ((м**3)*(кг**-1)*(с**-2))    
EPS = 1.0E-3               # Окрестность нуля (м)

class Vector:
    
    @staticmethod
    def length(r):
        """ Вычислить длину вектора. """
      
        return sqrt(fsum((x**2 for x in r)))


    @staticmethod
    def subtract(r1, r2):
        """ Вычислить разность векторов. """

        return tuple(x1 - x2 for x1, x2 in zip(r1, r2))

    @staticmethod
    def add(r1, r2):
        """ Сложить векторы. """

        return tuple(x1 + x2 for x1, x2 in zip(r1, r2))


    @staticmethod
    def init(v, r):
        """ Создать вектор с одинаковыми компонентами. """
        
        return tuple(v for x in r)

    @staticmethod
    def divide(r, v):
        """ Разделить вектор на скаляр. """

        return tuple(x/v for x in r)

class Body:
    """ Материальное тело с меткой label. """
    
    def __init__(self, label):
        """ Создать материальное тело. """
        
        self.label = label

    def __str__(self):
        """ Получить метку материального тела. """
        
        return self.label
        
class Mass(Body):
    """ Материальная точка с массой M. """
    
    def __init__(self, label, M):
        """ Создать материальную точку. """    
        
        super().__init__(label)
        self.M = M
        self.K = G*M
        
    def __str__(self):
        """ Получить строковое описание материальной точки. """
        
        return "{}(M = {}, K = {})".format(super().__str__(), self.M, self.K)

    def U(self, r):
        
        return self.K/r if abs(r) > EPS else float("+inf")


def F(b1, b2, r):
    """ Вычислить модуль силы притяжения тел m1 и m2 на расстоянии r. """

    return G*b1.M*b2.M/r**2
        
Sun = Mass("Sun", 1.9985E+30)         
Earth = Mass("Earth", 5.9726E+24)
Moon = Mass("Moon", 7.3477E+22)
Jupiter = Mass("Jupiter", 1.898E+27)

class System:
    """ Система материальных тел. """
    
    def __init__(self, body):
        """ Создать систему. """
        
        self.body = dict(body)
    
    def __str__(self):
        """ Получить строковое представление системы. 
        
        """
        return "\n".join(map(
            lambda b: str(b) + ':' + str(self.body[b]), 
            sorted(self.body, key = lambda b: Vector.length(self.body[b]))
            ))
            
    def U(self, r):
        """ Рассчитать потенциал системы тел в точке r. """
        
        u = 0.0
        for b in sorted(self.body, key = lambda b: b.M):
            u += b.U(Vector.length(Vector.subtract(r, self.body[b])))
        return u

    @staticmethod
    def next(r, dr, r1, r2):

        if r == ():
            raise StopIteration

        if r[0] + dr[0] > r2[0]:
            return (r1[0],) + System.next(r[1:], dr[1:], r1[1:], r2[1:])

        return (r[0] + dr[0],) + r[1:]


    @staticmethod
    def grid(r1, r2, n):

        dr = tuple(x/n for x, n in zip(Vector.subtract(r2, r1), n))
        r1 = r1
        r2 = r2
        r = (r1[0] - dr[0],) + r1[1:]

        try:
            while True:
                r = System.next(r, dr, r1, r2)
                yield r
        except StopIteration:
            pass


print(F(Sun, Moon, 150E+9)/F(Earth, Moon, 384402E+3))

s = System([
    (Sun, (-AU,)), 
    (Earth, (0.0,)), 
    (Moon, (384402E+3,)),
    (Jupiter, (778500000E+3 - AU,))
    ])


X = [r[0] for r in System.grid((-700000E+3,), (700000E+3,), (1000,))]
Y = [s.U(r) for r in System.grid((-700000E+3,), (700000E+3,), (1000,))]    

import plotly.graph_objects as go

f = go.Figure(go.Scatter(x = X, y = Y))
f.show()

