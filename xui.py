import curses
import time
import threading

def draw_washing_machine(screen, row, col):
    washing_machine = [
        "  _________  ",
        " /         \\ ",
        "|   O   O   |",
        "|    ___    |",
        " \\_________/ ",
    ]

    for i, line in enumerate(washing_machine):
        screen.addstr(row + i, col, line)

def animate_washing_machine(screen, row, col):
    while True:
        screen.clear()
        draw_washing_machine(screen, row, col)
        screen.refresh()
        time.sleep(0.2)

        screen.clear()
        draw_washing_machine(screen, row, col)
        draw_loading(screen, row + 5, col + 3)
        screen.refresh()
        time.sleep(0.2)

def draw_loading(screen, row, col):
    loading_symbols = ["|", "/", "-", "\\"]
    for i in range(12):
        screen.addstr(row, col, "Loading " + loading_symbols[i % 4])
        screen.refresh()
        time.sleep(0.1)

def main(screen):
    curses.curs_set(0)
    screen.clear()

    row, col = 5, 20

    washing_thread = threading.Thread(target=animate_washing_machine, args=(screen, row, col))
    washing_thread.daemon = True
    washing_thread.start()

    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass

curses.wrapper(main)