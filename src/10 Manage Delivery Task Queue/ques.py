from collections import deque, namedtuple


DeliveryTask = namedtuple(
    "DeliveryTask", ["order_id", "customer_id", "priority", "minutes_waiting"]
)


def add_task(task_queue, task):
    # TODO:
    # Priority tasks should be added to the front of the deque.
    # Normal tasks should be added to the back.
    return


def cancel_task(task_queue, order_id):
    # TODO:
    # Remove the first task matching order_id while preserving the order
    # of every other task.
    # Return True if a task was canceled; otherwise False.
    return False


def complete_next(task_queue):
    # TODO:
    # Complete and return the next task.
    # Return None when the queue is empty.
    return None


def main():
    tasks = deque()
    add_task(tasks, DeliveryTask("O1001", 100, False, 4))
    add_task(tasks, DeliveryTask("O1002", 101, False, 7))
    add_task(tasks, DeliveryTask("O1003", 102, True, 2))
    add_task(tasks, DeliveryTask("O1004", 103, False, 1))

    print(cancel_task(tasks, "O1002"))
    print(complete_next(tasks))
    print(list(tasks))
    return


if __name__ == "__main__":
    main()
