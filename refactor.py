<<<<<<< HEAD
=======
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
>>>>>>> origin/master

import collections
import functools

'''First Project already refactored'''
Shapes = collections.namedtuple('Shape', ['figure', 'formula'])


class ShapesFormula:
    figures = ["circle", "triangle", "cube"]
    formulas = 'A = π r² , A = 1/2 × b × h , 6a2'.split(",")

    def __init__(self):
        self._shapes = [Shapes(figure, formula) for formula in self.formulas
                        for figure in self.figures]

    def __len__(self):
        return len(self._shapes)

    def __getitem__(self, position):
        return self._shapes[position]

    def shuffle(self):
        return random.shuffle(_shapes)


m = ShapesFormula()

print(len(m))

for i in range(3):
    print(m[i])


####################################################################
# Second refactor after teacher's feedback
##################################################################

class ShapeFormula():
    '''
    Class created in order to get a formula from a specific set of items,
    the constructor can receive as a input a unlimited number of shapes(from
    the possible shapes dict, if a shape which does not exit is add-> print
    error will pop out)
    '''
    shapes = {"circle": "A = π r²", "triangle": "A = 1/2 × b × h",
              "cube": "6a2", "square": "l2"}

    def __init__(self, *args):
        self.args = list(args)
        print(self.args)
        my_shapes = list(self.shapes.keys())
        print(my_shapes)
        for i in range(len(self.args)):
            if self.args[i] not in my_shapes:
                print("Wrong shape,possible shapes are " + str(my_shapes))
                break
            else:
                print("Shape: " + str(self.args[i]) +
                      " Formula " + str(self.shapes[self.args[i]]))






first_object = ShapeFormula("circle", "triangle")

second_object = ShapeFormula("Octagon")


import pytest


possible_shapes={0:"triangle",1:"circle",2:"Octagon",3:["circle","triangle"]}

@pytest.mark.parametrize("current_object", possible_shapes)
def test_possbile_outputs(current_object):
    object=ShapeFormula(possible_shapes[current_object])



