from math import gcd

class Fraction:
    def __init__(self, hamarich, haytarar):
        self.hamarich = hamarich
        self.haytarar = haytarar

        if self.haytarar == 0:
            raise ValueError("Haytarar@ petq e 0 chlini")
        if not isinstance(self.hamarich, int):
            raise ValueError("Hamarich@ piti amboxj tiv lini")
        if not isinstance(self.haytarar, int):
            raise ValueError("Haytarar@ piti amboxj tiv lini")
        
        self.simplify()


    def __str__(self):
        return f"{self.hamarich}/{self.haytarar}"


    def __add__(self, other):
        hamarich_1 = self.hamarich * other.haytarar
        hamarich_2 = other.hamarich * self.haytarar
        hamarich = hamarich_1 + hamarich_2
        yndhanur_haytarar = self.haytarar * other.haytarar
        result = Fraction(hamarich, yndhanur_haytarar)
        return result


    def __sub__(self, other):
        hamarich_2 = -1 * other.hamarich
        new_other = Fraction(hamarich_2, other.haytarar)
        result = self.__add__(new_other)
        return result


    def __mul__(self, other):
        hamarich = self.hamarich * other.hamarich
        haytarar = self.haytarar * other.haytarar
        result = Fraction(hamarich, haytarar)
        return result


    def __truediv__(self, other):
        hamarich = self.hamarich * other.haytarar
        haytarar = self.haytarar * other.hamarich
        result = Fraction(hamarich, haytarar)
        return result


    def simplify(self):
        yndhanur_haytarar = gcd(self.hamarich, self.haytarar)
        if yndhanur_haytarar > 0:
            self.hamarich //= yndhanur_haytarar
            self.haytarar //= yndhanur_haytarar

    
    def __lt__(self, other):
        # hamarich_1 = self.hamarich * other.haytarar
        # hamarich_2 = other.hamarich * self.haytarar
        # return hamarich_1 < hamarich_2
        return (self.hamarich / self.haytarar) < (other.hamarich / other.haytarar)
    
    def __eq__(self, other):
        return self.hamarich == other.hamarich and self.haytarar == other.haytarar

# Create fraction objects
fraction1 = Fraction(7, 8)
fraction2 = Fraction(4, 4)

# Perform operations
sum_fraction = fraction1 + fraction2
difference_fraction = fraction1 - fraction2
product_fraction = fraction1 * fraction2
division_fraction = fraction1 / fraction2

print(sum_fraction)
print(difference_fraction)
print(product_fraction)
print(division_fraction)

# Compare fractions
if fraction1 == fraction2:
    print("Fractions are equal.")
elif fraction1 > fraction2:
    print("Fraction 1 is greater.")
else:
    print("Fraction 2 is greater.")

# Display simplified fractions
fraction1.simplify()
print("Simplified Fraction 1:", fraction1)
fraction2.simplify()
print("Simplified Fraction 2:", fraction2)

