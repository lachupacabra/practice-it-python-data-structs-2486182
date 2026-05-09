from collections import deque

# def completed():


class Task:
    def __init__(self, taskDesc: str, hasPriority: bool = False):
        self.taskDesc = taskDesc
        self.hasPriority = hasPriority

    def __str__(self):
        return f"{self.taskDesc} has a Priority:{self.hasPriority}"


task_queue = deque()


def add_task(task):
    task_queue.appendleft(task) if task.hasPriority else task_queue.append(task)

def do_task():
    return task_queue.popleft()

def print_queue():
    for i,task in enumerate(task_queue,start=1):
        print(f"{i} task :{task.taskDesc}  with {task.hasPriority} priority")

def main():
    add_task(Task("make a list"))
    add_task(Task("make breakfast"))
    add_task(Task("respond to email", True))
    print_queue()
    print(do_task())
    return


if __name__ == "__main__":
    main()
