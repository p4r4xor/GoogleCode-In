import math
horizontal_pixels = int(input("No. of pixels horizontally: "))
vertical_pixels = int(input("No. of pixels vertically: "))
inches = int(input("Size of the screen diagonally in inches: "))
sum_of_squares = pow(horizontal_pixels,2)+pow(vertical_pixels,2)
square_root = math.sqrt(sum_of_squares)
answer = square_root/inches
gcd_of_pixels = math.gcd(horizontal_pixels,vertical_pixels)
first_aspect = horizontal_pixels/gcd_of_pixels
second_aspect = vertical_pixels/gcd_of_pixels
print('DPI/PPI is: ', answer)
print("Aspect ratio: ", first_aspect, ":", second_aspect)