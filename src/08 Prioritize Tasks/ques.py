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
    # TODO:
    # Add priority tasks to the front and normal tasks to the back.
    return


def do_task():
    # TODO:
    # Complete and return the next task from the front of the queue.
    return None


def print_queue():
    # TODO:
    # Print the current tasks in queue order.
    return


def main():
    add_task(Task("make a list"))
    add_task(Task("make breakfast"))
    add_task(Task("respond to email", True))
    print_queue()
    print(do_task())
    return


if __name__ == "__main__":
    main()
