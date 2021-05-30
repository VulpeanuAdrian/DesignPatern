

'''
Problema de implementat
 Create a console application that iterates through a list of shapes (at least three
different shape types (e.g., triangle, circle, and rectangle)) and displays the following
message: &quot;area of &lt;shape type&gt; is calculated using this &lt;formula&gt;&quot;.

- Problema trebuie implementata intr-un limbaj OOP (C#, Java sau C++) si pusa pe source
control; proiectul trebuie sa fie compilabil
- Problema trebuie sa aiba o implementare initiala pana in 1 Iunie; nerespectarea termenului
va duce la injumatatirea punctelor care pot fi primite pentru acest proiect
- Problema trebuie sa aiba cel putin o iteratie de refactoring (pana la data examenului)
'''

import collections
import time
import functools
def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):

         t0 = time.time()
         result = func(*args, **kwargs)
         elapsed = time.time() - t0
         name = func.__name__
         arg_lst = []
         if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
         if kwargs:
             pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
             arg_lst.append(', '.join(pairs))
         arg_str = ', '.join(arg_lst)
         print('[%0.8fs] %s(%s) -> %r ' % (elapsed, name, arg_str, result))
         return result

    return clocked


'''First Project already refactored'''
Shapes = collections.namedtuple('Shape', ['figure', 'formula'])


class ShapesFormula:
    figures=["circle","triangle","cube"]
    formulas='A = π r² , A = 1/2 × b × h , 6a2'.split(",")
    def __init__(self):
        self._shapes = [Shapes(figure, formula) for formula in self.formulas
                       for figure in self.figures]

    def __len__(self):
        return len(self._shapes)

    def __getitem__(self, position):
        return self._shapes[position]
    
    def shuffle(self):
        return random.shuffle(_shapes)
        


m=ShapesFormula()

print(len(m))

for i in range(3):
    print(m[i])



