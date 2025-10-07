import  time

CSI = '\x1b['
RESET = f'{CSI}0m'
ZERO = f'{CSI}0G'
ERASE = f'{CSI}2K'


def draw_line(offset, length, color=220):
    offset_part = f'{" " * offset}'
    filed_part = f'{" " * length}'
    line = f'{offset_part}{CSI}48;5;{color}m{filed_part}{RESET}'
    print(line)


def draw_romb(heigth):
    center = heigth // 2
    offset = center
    print(center, offset)
    step = 1
    length = 1
    colors = range(16, 232)

    while True:
        for color in colors:
            for line in range(heigth):
                draw_line(offset, length, color)
                if line < center:
                    offset -= step
                    length += step*2
                else:
                    offset += step
                    length -= step*2
            print(f"{CSI}{heigth}A", end="", flush=True)
            print(f"{CSI}{offset}D", end="", flush=True)
            length = 1
            offset = center
            time.sleep(0.2)


if __name__ == '__main__':
    draw_romb(15)