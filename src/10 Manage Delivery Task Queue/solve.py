from collections import deque, namedtuple


DeliveryTask = namedtuple(
    "DeliveryTask", ["order_id", "customer_id", "priority", "minutes_waiting"]
)


def add_task(task_queue, task):
    if task.priority:
        task_queue.appendleft(task)
    else:
        task_queue.append(task)


def cancel_task(task_queue, order_id):
    canceled = False
    original_length = len(task_queue)

    for _ in range(original_length):
        task = task_queue.popleft()
        if not canceled and task.order_id == order_id:
            canceled = True
            continue
        task_queue.append(task)

    return canceled


def complete_next(task_queue):
    if not task_queue:
        return None
    return task_queue.popleft()


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
