

# Functions to complete:


## Get a list of uncompleted tasks
def get_uncompleted_tasks(list):
    return get_tasks_by_status(list, False)
    # uncompleted_tasks = []
    # for task in list:
    #     if task["completed"] == False:
    #         uncompleted_tasks.append(task)
    # return uncompleted_tasks

## Get a list of completed tasks
def get_completed_tasks(list):
    return get_tasks_by_status(list, True)
    # completed_tasks = []
    # for task in list:
    #     if task["completed"] == True:
    #         completed_tasks.append(task)
    # return completed_tasks

## Get tasks where time_taken is at least a given time
def get_tasks_taking_at_least(list, time):
    long_tasks = []
    for task in list:
        if task["time_taken"] >= time:
            long_tasks.append(task)
    return long_tasks

## Find a task with a given description
def get_task_with_description(list, description):
    for task in list:
        if task["description"] == description:
            return task

# Extention (Function):     

## Get a list of tasks by status
def get_tasks_by_status(list, status):
    task_status_list = []
    for task in list:
        if task["completed"] == status:
            task_status_list.append(task)
    return task_status_list

def mark_task_complete(task):
    task["completed"] = True

def create_task(description, time_taken):
    task = {}
    task["description"] = description
    task["completed"] = False
    task["time_taken"] = time_taken

    return task

def add_to_list(list, task):
    list.append(task)




