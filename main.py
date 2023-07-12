import curses
import subprocess

def main(stdscr):
    stdscr.clear()
    options = [
        "1. Create - Creates group chats",
        "2. Adder - Adds another user to the group chats",
        "3. Description - Changes description in every one of the group chats",
        "4. DM Advertiser - Sends a message in every one of the group chats",
        "5. Leaver - Leaves every one of the group chats"
    ]
    script_files = {
        "1. Create": "create.py",
        "2. Adder": "member_adder.py",
        "3. Description": "description.py",
        "4. DM Advertiser": "dm.py",
        "5. Leaver": "leaver.py"
    }
    current_option = 0
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)

    while True:
        stdscr.clear()
        for i, option in enumerate(options):
            attr = curses.color_pair(1) if i == current_option else curses.color_pair(2)
            stdscr.addstr(i, 0, option, attr)

        key = stdscr.getch()
        if key == curses.KEY_UP:
            current_option = (current_option - 1) % len(options)
        elif key == curses.KEY_DOWN:
            current_option = (current_option + 1) % len(options)
        elif key == ord('\n'):
            break

    stdscr.clear()
    selected_option = options[current_option].split(' - ')[0].strip()
    script_filename = script_files[selected_option]
    subprocess.run(['python', f"scripts/{script_filename}"])
curses.wrapper(main)
