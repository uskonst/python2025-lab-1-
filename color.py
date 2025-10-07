CSI = '\x1b['
RESET = f'{CSI}0m'

print(f'{CSI}31;47mHello world{RESET}')