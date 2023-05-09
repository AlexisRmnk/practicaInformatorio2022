from decimal import Decimal

a = Decimal("55.2")

print(f"x1: {a / Decimal('10')}")
print(f"x2: {a // Decimal('10')}")
print(f"x3: {a % Decimal('10')}")
