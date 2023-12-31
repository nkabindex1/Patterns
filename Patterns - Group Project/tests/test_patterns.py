import unittest
from io import StringIO
import sys
from unittest.mock import patch
from patterns import *

class MyTestCase(unittest.TestCase):

    def test_1_shape(self):
           #Mocking to test if all lower cases are returned
        sys.stdin = StringIO("TriAngLe\n")
        self.assertEqual(get_shape(), "triangle")

        sys.stdin = StringIO("SquAre\n")
        self.assertEqual(get_shape(), "square")

        sys.stdin = StringIO("PyRamiD\n")
        self.assertEqual(get_shape(), "pyramid")

    

    # Test if get_shape only returns numbers below 80 only
    @patch('builtins.input', side_effect = ["85","70", "100"])
    def test_get_height(self,mock_input):
        self.assertEqual(get_height(),70)


    @patch('builtins.input', side_effect=['abc', 'xyz', '@', '/'])
    def test_get_height(self, mock_input):
        with self.assertRaises(ValueError):
            get_height()

    def test_4_square(self):
        text_capture = StringIO()
        sys.stdout = text_capture
        draw_square(4)

        self.assertEqual("""****
****
****
****
""",text_capture.getvalue())

    def test_5_square(self):

        text_capture = StringIO()
        sys.stdout = text_capture
        draw_square(10)

        self.assertEqual("""**********
**********
**********
**********
**********
**********
**********
**********
**********
**********
""",text_capture.getvalue())

    def test_6_triangle(self):
        """
        test for reversed triangle with height 0f 3
        """
        with patch("sys.stdout", StringIO("1 1 1 \n2 2 \n3 \n")) as mock_stdout:
            draw_triangle_reversed(3)
            self.assertEqual(mock_stdout.getvalue(), "1 1 1 \n2 2 \n3 \n")
    

    def test_7_triangle(self):
        """
        test for reversed triangle
        """
        with patch("sys.stdout", StringIO("1 1 1 1 1 \n2 2 2 2 \n3 3 3 \n4 4 \n5 ")) as mock_stdout:
            draw_triangle_reversed(5)
            self.assertEqual(mock_stdout.getvalue(), "1 1 1 1 1 \n2 2 2 2 \n3 3 3 \n4 4 \n5 \n")

    def test_8_triangle(self):
        
        text_capture = StringIO()
        sys.stdout = text_capture
        draw_triangle(3)

        self.assertEqual("""1 
1 2 
1 2 3 
""",text_capture.getvalue())
    def test_9_triangle(self):
        text_capture = StringIO()
        sys.stdout = text_capture
        draw_triangle(5)

        self.assertEqual("""1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
""",text_capture.getvalue())
        
    

    def test_10_triangle_multiplication(self):
        """
        test for an increamenting multiplication triangle 
        """
        with patch("sys.stdout", StringIO("1 \n2 4 \n3 6 9 \n4 8 12 16 \n")) as mock_stdout:
            draw_triangle_multiplication(4)
            self.assertEqual(mock_stdout.getvalue(), "1 \n2 4 \n3 6 9 \n4 8 12 16 \n")
        

    def test_11_triangle_multiplication(self):
        """
        test for an increamenting multiplication triangle 
        """

        with patch("sys.stdout", StringIO("1 \n2 4 \n3 6 9 \n4 8 12 16 \n5 10 15 20 25 \n6 12 18 24 30 36 \n")) as mock_stdout:
            draw_triangle_multiplication(6)
            self.assertEqual(mock_stdout.getvalue(), "1 \n2 4 \n3 6 9 \n4 8 12 16 \n5 10 15 20 25 \n6 12 18 24 30 36 \n")


    def test_12_pyramid(self):
        
        text_capture = StringIO()
        sys.stdout = text_capture
        draw_pyramid(3)

        self.assertEqual("""  *
 ***
*****
""",text_capture.getvalue())

    def test_13_pyramid(self):
        
        text_capture = StringIO()
        sys.stdout = text_capture
        draw_pyramid(5)

        self.assertEqual("""    *
   ***
  *****
 *******
*********
""",text_capture.getvalue())


    def test_14_primes_numbers(self):
        ''' This test test whether our function returns only
            prime numbers only
        '''
        # Test Case for prime numbers
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(47))
        self.assertTrue(is_prime(193))

        # Test Case for non-prime numbers
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(60))
        self.assertFalse(is_prime(200))
        
        
    @patch('sys.stdout', new_callable=StringIO)
    def test_15_prime(self, mock_stdout):
        ''' This tests tests whether our function prints out a
            right angled triangle'''

        draw_triangle_prime(3)
        output = mock_stdout.getvalue()
        expected_output = "2 \n3 5 \n7 11 13 \n"
        self.assertEqual(output, expected_output)
        
    def assertValidHanoiMoves(self, n, source, auxiliary, target, moves):
        expected_moves = 2 ** n - 1
        self.assertEqual(len(moves), expected_moves)


    """
        *This function tests how the rings move from one pole to the next.
        it uses an instance of n=1 to check if the poles are ordered from biggest pole to
        smallest pole. 
    """    
    def test_tower_of_hanoi_1(self):
        n = 1
        source, auxiliary, target = 'A', 'B', 'C'
        moves = tower_of_hanoi(n, source, auxiliary, target)
        self.assertValidHanoiMoves(n, source, auxiliary, target, moves)


    """
        *This function tests how the rings move from one pole to the next.
        it uses an instance of n=2 to check if the poles are ordered from biggest pole to
        smallest pole. 
    """
    def test_tower_of_hanoi_2(self):
        n = 2
        source, auxiliary, target = 'A', 'B', 'C'
        moves = tower_of_hanoi(n, source, auxiliary, target)
        self.assertValidHanoiMoves(n, source, auxiliary, target, moves)


    """
        *This function tests how the rings move from one pole to the next.
        it uses an instance of n=3 to check if the poles are ordered from biggest pole to
        smallest pole. 
    """
    def test_tower_of_hanoi_3(self):
        n = 3
        source, auxiliary, target = 'A', 'B', 'C'
        moves = tower_of_hanoi(n, source, auxiliary, target)
        self.assertValidHanoiMoves(n, source, auxiliary, target, moves)


    """
        *This function tests how the rings move from one pole to the next.
        it uses an instance of n=4 to check if the poles are ordered from biggest pole to
        smallest pole. 
    """
    def test_tower_of_hanoi_4(self):
        n = 4
        source, auxiliary, target = 'A', 'B', 'C'
        moves = tower_of_hanoi(n, source, auxiliary, target)
        self.assertValidHanoiMoves(n, source, auxiliary, target, moves)


    """
        *This function tests how the rings move from one pole to the next.
        it uses an instance of n=5 to check if the poles are ordered from biggest pole to
        smallest pole. 
    """
    def test_tower_of_hanoi_5(self):
        n = 5
        source, auxiliary, target = 'A', 'B', 'C'
        moves = tower_of_hanoi(n, source, auxiliary, target)
        self.assertValidHanoiMoves(n, source, auxiliary, target, moves)

        
    
if __name__ == '__main__':
    unittest.main()