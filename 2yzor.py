# def yzor(width, height, rep):
#     for y in range(height):
#         line = ""
        
#         for _ in range(rep):
#             if y % 2 == 0:
#                 line += "/\\" * width
#             else:
#                 line += "\\/" * width
#             line += "  " 
            
#         print(line)

# yzor(3, 4, 4)

def colored_woven_pattern(size=2, repeats=10):
    # Цвета можно менять: 40-47 — стандартные, 100-107 — яркие
    color1 = "\033[48;5;236m"  # темно-серый фон
    color2 = "\033[48;5;240m"  # чуть светлее серый
    reset = "\033[0m"

    for y in range(size * 2):
        line = ""
        for x in range(repeats * size):
            # выбираем цвет, создавая переплетённый эффект
            if (x // size + y // size) % 2 == 0:
                line += color1 + "  "
            else:
                line += color2 + "  "
        line += reset
        print(line)

colored_woven_pattern(size=10, repeats=3)
