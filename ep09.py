import math

class Trigonometria:

    def __init__(self, angulo):
        self.angulo = angulo
    
    def __str__(self):
        rad = math.radians(self.angulo)
        return (
        f"Seno: {(math.sin(rad)):.2f}"
        f"\nCosseno: {(math.cos(rad)):.2f}"
        f"\nTangente: {(math.tan(rad)):.2f}"
        )

angulo1 = Trigonometria(30)
print(angulo1)
