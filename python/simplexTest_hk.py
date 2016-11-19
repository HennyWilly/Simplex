import unittest
import numpy as np

import simplex_hk

class SimplexTest(unittest.TestCase):
    def assertNpEquals(self, actual, expected):
        actual = np.array(actual)
        expected = np.array(expected)
        #print expected.shape
        
        self.assertEqual(actual.ndim, expected.ndim)
        for i in range(actual.ndim):
            self.assertEqual(actual.shape[i], expected.shape[i])
        
        #print expected - actual
        
        self.assertTrue(np.allclose(actual,expected, atol=1e-06))  # test if nearly same elements values

    def test_shouldNotDoSimplex_fNotHasEnoughEntries(self):
        A = [1,2,3]
        b = [1]
        f = [1]
        self.assertRaises(ValueError, simplex.simplex, A, b, f)
    
    def test_shouldNotDoSimplex_bHasNotEnoughEntries(self):
        A = [[1],[2],[3]]
        b = [1]
        f = [1]
        self.assertRaises(ValueError, simplex.simplex, A, b, f)
    
    def test_shouldNotDoSimplex_bContainsNegativeValues(self):
        A = [1,2,3]
        b = [-1]
        f = [1,-1, 2]
        self.assertRaises(ValueError, simplex.simplex, A, b, f)
    
    def test_shouldDoSimplex_A1_2(self):
        A = [[1,2,1,0,1,1,0,0],[0,1,1,1,1,0,1,0],[1,0,1,1,0,0,0,1]]
        b = [100,80,50]
        f = [-2,-1, -3,-1,-2,0,0,0]
        
        (ARes, bRes, fRes, res) = simplex.simplex(A, b, f)
        self.assertNpEquals(ARes, [[1,1,0,-1,0,1,-1,0],[0,2,0,-1,1,1,0,-1],[0,-1,1,2,0,-1,1,1]])
        self.assertNpEquals(bRes, [20,50,30])
        self.assertNpEquals(fRes, [0,2,0,1,0,1,1,1])
        self.assertEqual(res, 230)
    
    def test_shouldDoSimplex_A1_3(self):
        A = [[1,1,1,0,0],[6,9,0,1,0],[0,1,0,0,1]]
        b = [100,720,60]
        f = [-10,-20,0,0,0]
        
        (ARes, bRes, fRes, res) = simplex.simplex(A, b, f)
        self.assertNpEquals(ARes, [[0,0,1,-1.0/6,1.0/2],[1,0,0,1.0/6,-3.0/2],[0,1,0,0,1]])
        self.assertNpEquals(bRes, [10,30,60])
        self.assertNpEquals(fRes, [0,0,0,5.0/3,5])
        self.assertEqual(res, 1500)
    
    def test_shouldDoSimplex_Example_MatheBibel_de(self):
        A = [[16,6,1,0],[4,12,0,1]]
        b = [252,168]
        f = [-150,-100,0,0]
        
        (ARes, bRes, fRes, res) = simplex.simplex(A, b, f)
        self.assertNpEquals(ARes, [[1,0,1.0/14,-1.0/28],[0,1,-1.0/42,2.0/21]])
        self.assertNpEquals(bRes, [12,10])
        self.assertNpEquals(fRes, [0,0,25.0/3,25.0/6])
        self.assertEqual(res, 2800)

if __name__ ==  "__main__":
    unittest.main()