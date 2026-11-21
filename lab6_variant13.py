# Laboratory work 6 — Dictionaries and Sets
# Variant 13: tasks 530, 531, 562, 563, 594, 595


def task_530():
    teams = {
        "BOSTON CELTICS": [3, 2, 0, 1, 8],
        "NEW YORK KNICKS": [10, 3, 3, 4, 19],
        "INDIANA PACERS": [4, 2, 2, 0, 11],
        "MIAMI HEAT": [12, 2, 5, 5, 9],
        "ATLANTA HAWKS": [5, 2, 2, 1, 10],
        "CHICAGO BULLS": [25, 10, 9, 6, 38]
    }

    for team, statistics in teams.items():
        print(team, *statistics)


def task_531():
    # The example in the assignment uses the interval 12.2014–6.2019.
    # Input format: year, then month (each on a separate line).
    start_date = (2014, 12)
    end_date = (2019, 6)

    year = int(input("Enter year: "))
    month = int(input("Enter month: "))

    entered_date = (year, month)

    if 1 <= month <= 12 and start_date <= entered_date <= end_date:
        print("YES")
    else:
        print("NO")


def task_562():
    entered = list(map(int, input("Enter numbers separated by spaces: ").split()))
    numbers = set(entered)

    # Compare the number of entered values with the number of unique values.
    if len(entered) == len(numbers):
        print("is unique sequence")
    else:
        print("duplicate list")


def task_563():
    words = input("Enter a line of text: ").split()
    counts = {}
    result = []

    for word in words:
        result.append(str(counts.get(word, 0)))
        counts[word] = counts.get(word, 0) + 1

    print(" ".join(result))


def task_594():
    position = input("Enter the king position (for example, c5): ").strip().lower()
    column = ord(position[0]) - ord("a")
    row = int(position[1]) - 1

    for current_row in range(7, -1, -1):
        line = []
        for current_column in range(8):
            if current_row == row and current_column == column:
                line.append("K")
            elif abs(current_row - row) <= 1 and abs(current_column - column) <= 1:
                line.append("*")
            else:
                line.append(".")
        print(" ".join(line))


def task_595():
    position = input("Enter a square position (for example, b6): ").strip().lower()
    column = ord(position[0]) - ord("a")
    row = int(position[1]) - 1

    for current_row in range(7, -1, -1):
        line = []
        for current_column in range(8):
            if current_row == row and current_column == column:
                color = "B" if (column + row) % 2 == 0 else "W"
                line.append(color)
            else:
                line.append(".")
        print(" ".join(line))


def main():
    print("Laboratory work 6 — Variant 13")
    print("Tasks: 530, 531, 562, 563, 594, 595")
    print("1 — task 530")
    print("2 — task 531")
    print("3 — task 562")
    print("4 — task 563")
    print("5 — task 594")
    print("6 — task 595")

    choice = input("Choose task (1-6): ").strip()
    tasks = {
        "1": task_530,
        "2": task_531,
        "3": task_562,
        "4": task_563,
        "5": task_594,
        "6": task_595
    }

    if choice in tasks:
        tasks[choice]()
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
