def greeting():
    print ("hi there")


def calculate_pi(digits=5):
    """
    Calculate pi to the specified number of decimal digits using the Machin formula.
    
    Machin's formula: pi/4 = 4*arctan(1/5) - arctan(1/239)
    
    Args:
        digits: Number of decimal digits to calculate (default: 5)
    
    Returns:
        float: Approximation of pi
    """
    def arctan(x, num_terms):
        """Calculate arctan using Taylor series expansion."""
        result = 0
        x_squared = x * x
        x_power = x
        
        for n in range(num_terms):
            sign = (-1) ** n
            result += sign * x_power / (2 * n + 1)
            x_power *= x_squared
        
        return result
    
    # Number of terms needed for accuracy (more terms = more precision)
    # For 5 decimal places, we need enough terms
    num_terms = 500
    
    # Machin's formula: pi/4 = 4*arctan(1/5) - arctan(1/239)
    pi_over_4 = 4 * arctan(1/5, num_terms) - arctan(1/239, num_terms)
    pi_estimate = 4 * pi_over_4
    
    # Round to the specified number of digits
    return round(pi_estimate, digits)


def calculate_pi_leibniz(iterations=1000000):
    """
    Calculate pi using the Leibniz formula (slower convergence).
    
    Leibniz formula: pi/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - ...
    
    Args:
        iterations: Number of iterations (default: 1000000)
    
    Returns:
        float: Approximation of pi
    """
    pi_estimate = 0
    
    for i in range(iterations):
        sign = (-1) ** i
        pi_estimate += sign / (2 * i + 1)
    
    return 4 * pi_estimate