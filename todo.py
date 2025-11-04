class Todo:
    def __init__(self):
        self._task_list = []

    def addTask(self, task):
        self._task_list.append(task)

    def __repr__(self):
        return str(self._task_list)
