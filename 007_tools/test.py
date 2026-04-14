import unittest
import math
from main import calculate_pi, calculate_pi_leibniz


class TestPiCalculation(unittest.TestCase):
    """Test suite for pi calculation functions."""
    
    def test_calculate_pi_default_5_digits(self):
        """Test that calculate_pi with default parameter returns pi to 5 decimal places."""
        result = calculate_pi()
        expected = 3.14159
        self.assertEqual(result, expected, 
                         f"Expected pi to 5 digits: {expected}, got: {result}")
    
    def test_calculate_pi_accuracy_5_digits(self):
        """Test that calculate_pi(5) is accurate to 5 decimal places."""
        result = calculate_pi(5)
        actual_pi = math.pi
        # The result should be within 0.000005 of the actual value
        self.assertAlmostEqual(result, actual_pi, places=5,
                              msg=f"Pi calculation not accurate to 5 digits")
    
    def test_calculate_pi_3_digits(self):
        """Test calculate_pi with 3 decimal places."""
        result = calculate_pi(3)
        expected = 3.142
        self.assertEqual(result, expected,
                        f"Expected pi to 3 digits: {expected}, got: {result}")
    
    def test_calculate_pi_2_digits(self):
        """Test calculate_pi with 2 decimal places."""
        result = calculate_pi(2)
        expected = 3.14
        self.assertEqual(result, expected,
                        f"Expected pi to 2 digits: {expected}, got: {result}")
    
    def test_calculate_pi_1_digit(self):
        """Test calculate_pi with 1 decimal place."""
        result = calculate_pi(1)
        expected = 3.1
        self.assertEqual(result, expected,
                        f"Expected pi to 1 digit: {expected}, got: {result}")
    
    def test_calculate_pi_0_digits(self):
        """Test calculate_pi with 0 decimal places (integer)."""
        result = calculate_pi(0)
        expected = 3.0
        self.assertEqual(result, expected,
                        f"Expected pi to 0 digits: {expected}, got: {result}")
    
    def test_calculate_pi_return_type(self):
        """Test that calculate_pi returns a numeric type."""
        result = calculate_pi(5)
        self.assertIsInstance(result, (int, float),
                            "calculate_pi should return a numeric value")
    
    def test_calculate_pi_positive(self):
        """Test that calculate_pi returns a positive value."""
        result = calculate_pi(5)
        self.assertGreater(result, 0,
                          "Pi should be positive")
    
    def test_calculate_pi_range(self):
        """Test that calculate_pi returns a value in the expected range."""
        result = calculate_pi(5)
        self.assertGreater(result, 3.0,
                          "Pi should be greater than 3")
        self.assertLess(result, 4.0,
                       "Pi should be less than 4")
    
    def test_calculate_pi_leibniz_accuracy(self):
        """Test that calculate_pi_leibniz produces a reasonable approximation."""
        result = calculate_pi_leibniz(1000000)
        actual_pi = math.pi
        # Leibniz converges slowly, so we check with less precision
        self.assertAlmostEqual(result, actual_pi, places=5,
                              msg="Leibniz formula should approximate pi")
    
    def test_calculate_pi_leibniz_return_type(self):
        """Test that calculate_pi_leibniz returns a numeric type."""
        result = calculate_pi_leibniz(1000)
        self.assertIsInstance(result, (int, float),
                            "calculate_pi_leibniz should return a numeric value")
    
    def test_calculate_pi_leibniz_positive(self):
        """Test that calculate_pi_leibniz returns a positive value."""
        result = calculate_pi_leibniz(1000)
        self.assertGreater(result, 0,
                          "Pi should be positive")
    
    def test_calculate_pi_leibniz_range(self):
        """Test that calculate_pi_leibniz returns a value in the expected range."""
        result = calculate_pi_leibniz(100000)
        self.assertGreater(result, 3.0,
                          "Pi should be greater than 3")
        self.assertLess(result, 4.0,
                       "Pi should be less than 4")
    
    def test_calculate_pi_leibniz_convergence(self):
        """Test that more iterations lead to better approximation."""
        result_low = calculate_pi_leibniz(1000)
        result_high = calculate_pi_leibniz(100000)
        actual_pi = math.pi
        
        # Higher iterations should be closer to actual pi
        error_low = abs(result_low - actual_pi)
        error_high = abs(result_high - actual_pi)
        
        self.assertLess(error_high, error_low,
                       "More iterations should yield better approximation")
    
    def test_compare_methods(self):
        """Test that both methods produce similar results."""
        machin_result = calculate_pi(5)
        leibniz_result = calculate_pi_leibniz(1000000)
        
        # Both should be close to each other (within 0.00001)
        self.assertAlmostEqual(machin_result, leibniz_result, places=4,
                              msg="Both methods should produce similar results")


if __name__ == '__main__':
    unittest.main()
