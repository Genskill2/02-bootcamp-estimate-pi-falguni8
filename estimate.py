import math
import unittest

class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    
if __name__ == "__main__":
    unittest.main()

def wallis(n):
    o=int(n)
    z=1
    pi=1
    for n in range(o):
        w=4*z*z
        pi*=w/(w-1)
        z+=1
    return 2*pi 
 

def monte_carlo(n):
    ic=0
    oc=0
    o=int(n)
    for n in range(o):
        x=random.random()
        y=random.random()
        if (((x**2+y**2)**0.5)>1) :
            oc+=1
        else:
            ic+=1
    pi=4*(ic/(oc+ic))
    return pi    
