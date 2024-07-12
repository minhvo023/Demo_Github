import math

def solve_quadratic(a, b, c):
    # Tính delta
    delta = b**2 - 4*a*c
    
    # Kiểm tra giá trị của delta
    if delta > 0:
        root1 = (-b + math.sqrt(delta)) / (2*a)
        root2 = (-b - math.sqrt(delta)) / (2*a)
        return (root1, root2)
    elif delta == 0:
        root = -b / (2*a)
        return (root,)
    else:
        return "Phương trình vô nghiệm"

# Ví dụ
a = 1
b = -3
c = 200

kết_quả = solve_quadratic(a, b, c)
print("Nghiệm của phương trình là:", kết_quả)
