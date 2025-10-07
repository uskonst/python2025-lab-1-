import  time

CSI = '\x1b['
RESET = f'{CSI}0m'
ZERO = f'{CSI}0G'
ERASE = f'{CSI}2K'


def loading():
    print("Loading...")
    for i in range(100):
        print(f"{CSI}0G{i+1}%", end="", flush=True)
        time.sleep(2)

def draw_progressbar(num_tasks, width):
    for task in range(1, num_tasks+1):
        for filled in range(width):
            bar = f"{'#'*filled}{'-' * (width - filled -1)}"
            print(f"{ZERO}{ERASE}Задача {task}/{num_tasks} {bar}",
                  end="",
                  flush=True)
            time.sleep(2)

if __name__ == '__main__':
    draw_progressbar(3, 10)