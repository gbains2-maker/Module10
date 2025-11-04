from schooltasks import SchoolTasks

class TaskTracker(SchoolTasks):
    def __init__(self, task_type):
        super().__init__()
        self.task_type = task_type

    def clearTaskList(self):
        self._task_list.clear()

    def removeTask(self, task):
        self._task_list = [t for t in self._task_list if t[1] != task]

    def addTask(self, task, task_date, complete_date=""):
        if complete_date == "":
            complete_date = "In Process"
        self._task_list.append((task_date, task, complete_date))

    def __str__(self):
        result = f"List Type: {self.task_type}\n"
        for index, (date, task, complete_date) in enumerate(self._task_list, start=1):
            result += f"Task{index} Date: {date} Task: {task} Completed: {complete_date}\n"
        return result
