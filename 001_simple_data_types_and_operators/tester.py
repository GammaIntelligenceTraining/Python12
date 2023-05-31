# Ask user to enter sides of a triangle
side_a = float(input('Enter side A: '))
side_b = float(input('Enter side B: '))
side_c = float(input('Enter side C: '))

# Find half perimeter
half_perimeter = (side_a + side_b + side_c) / 2
triangle_area = (half_perimeter * (half_perimeter - side_a) * (half_perimeter - side_b) *
                 (half_perimeter - side_c)) ** 0.5
print('Area of a triangle is', triangle_area)

# end of program