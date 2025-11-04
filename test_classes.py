from todo import Todo

def main():
    todo = Todo()
    todo.addTask("Buy groceries")
    todo.addTask("Finish homework")
    todo.addTask("Read a book")

    print(repr(todo))  # ['Buy groceries', 'Finish homework', 'Read a book']

if __name__ == "__main__":
    main()

from schooltasks import SchoolTasks

def main():
    school = SchoolTasks()
    school.addTask("Write Essay", "11/4/2025")
    school.addTask("Read Chapter 10", "11/04/2025")
    school.addTask("Complete Online Programming Quiz", "11/7/2025")

    print(str(school))
    print(repr(school))

if __name__ == "__main__":
    main()

from tasktracker import TaskTracker

def main():
    tracker = TaskTracker("Workout for the day")
    tracker.addTask("Run 3 miles", "11/01/2025", "11/01/2025")
    tracker.addTask("Swim 50 laps", "11/03/2025")
    tracker.addTask("HIIT training", "11/05/2025", "11/05/2025")
    tracker.addTask("Yoga session", "11/06/2025")

    print(repr(tracker))  # see internal data
    tracker.removeTask("Yoga session")
    print(repr(tracker))
    print(str(tracker))

if __name__ == "__main__":
    main()

def generate_list(t):
    from todo import Todo
    if not isinstance(t, Todo):
        print("Not Todo Class")
        return NotImplemented
    print(t)

