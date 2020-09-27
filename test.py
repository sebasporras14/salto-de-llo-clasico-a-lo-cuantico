import unittest
from clasicoacuantico import*
from operacionesmatrices import*

class TestStringMethods(unittest.TestCase):

    def testcanicas(self):
        matriz= [[1, 0, 0, 0, 1],[0,0,1,1,0],[0,0, 0, 1,0],[0, 1, 0, 0, 1],[0,0,0,1,1]]
        estado = [1, 0, 1, 0, 0]
        clicks = 2

        self.assertEqual(canicas(matriz, estado, clicks), ['True', 'True', 'True', 'False', 'False'] )
    def testgrafico(self):
        vector = [0.25, 0.15, 0.6]
        self.assertEqual(grafica(vector), None )
        
    def test_clasicoproba(self):
        matriz= [[0,1/3,2/3],[1/6,1/2,1/3],[5/6,1/6,0]]
        estado = [1/6,1/6,2/3]
        clicks = 3
        self.assertEqual(probclasico(matriz, estado, clicks), [0.4513888888888889, 0.3125, 0.2361111111111111])
        
if __name__ == '__main__':
    unittest.main()
