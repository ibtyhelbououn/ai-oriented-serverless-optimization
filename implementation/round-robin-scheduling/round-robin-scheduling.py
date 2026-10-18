def round_robin(tasks, time_quantum):
    """
    Simulates Round-Robin Scheduling.

    Args:
        tasks (list): A list of tasks, each represented as a tuple (task_name, execution_time).
        time_quantum (int): The time each task gets to execute before switching.

    Returns:
        None
    """
    if time_quantum <= 0:
        raise ValueError("Time quantum must be greater than zero.")

    for task_name, execution_time in tasks:
        if execution_time < 0:
            raise ValueError("Task execution time cannot be negative.")
        
    queue = tasks.copy() 
    time_elapsed = 0

    print("Starting Round-Robin Scheduling...")
    while queue:
        task_name, execution_time = queue.pop(0)  
        if execution_time <= time_quantum:
            # Task completes within the quantum
            time_elapsed += execution_time
            print(f"Task {task_name} completed at time {time_elapsed}.")
        else:
            # Task exceeds the quantum; move it to the back of the queue
            time_elapsed += time_quantum
            queue.append((task_name, execution_time - time_quantum))
            print(f"Task {task_name} executed for {time_quantum} units. Remaining: {execution_time - time_quantum}.")

if __name__ == "__main__":
    tasks = [("Task1", 10), ("Task2", 4), ("Task3", 7)]
    time_quantum = 3
    round_robin(tasks, time_quantum)
