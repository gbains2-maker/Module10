from todo import Todo

class SchoolTasks(Todo):
    def addTask(self, task, task_date):
        self._task_list.append((task_date, task))

    def __str__(self):
        result = ""
        for index, (date, task) in enumerate(self._task_list, start=1):
            result += f"Task{index} Date: {date} Task: {task}\n"
        return result
