

height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Noone is that tall.")

bmi = weight/height ** 2
print(bmi)