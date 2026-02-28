import calendar
import datetime


def display_month(year: int, month: int) -> None:
    """Print the calendar for a specific month and year."""
    cal = calendar.TextCalendar(calendar.SUNDAY)
    print(cal.formatmonth(year, month))


def run_interactive_calendar() -> None:
    """Run a simple terminal-based interactive calendar viewer.

    The user can navigate to the previous or next month by typing
    `p` or `n` respectively, and quit with `q`.
    """
    today = datetime.date.today()
    year, month = today.year, today.month

    while True:
        # clear screen for nicer display
        try:
            import os
            os.system('cls' if os.name == 'nt' else 'clear')
        except Exception:
            pass

        display_month(year, month)
        print("Controls: [p]revious month  [n]ext month  [q]uit")
        choice = input("Enter command: ").strip().lower()
        if choice == 'q':
            break
        elif choice == 'n':
            # increment month
            if month == 12:
                month = 1
                year += 1
            else:
                month += 1
        elif choice == 'p':
            # decrement month
            if month == 1:
                month = 12
                year -= 1
            else:
                month -= 1
        else:
            # ignore other input
            continue


if __name__ == '__main__':
    run_interactive_calendar()
