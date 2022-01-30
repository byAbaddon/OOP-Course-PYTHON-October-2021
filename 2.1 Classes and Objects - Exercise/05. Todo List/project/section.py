# import os
# os.system('clear')
# from task import Task

class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task not in self.tasks:  
            self.tasks.append(new_task)
            return f'Task {new_task.details()} is added to the section'     
        return f'Task is already in the section {self.name}' 

    def complete_task(self, task_name):
        if task_name not in [x.name for x in self.tasks]:
            return f'Could not find task with the name {task_name}'
        result_task = [x for x in self.tasks if x.name == task_name][0]
        result_task.completed = True
        return f'Completed task {task_name}'

    def clean_section(self):
        count_completed_tasks = len([x for x in self.tasks if x.completed])
        self.task = [x for x in self.tasks if not x.completed]
       
        return f'Cleared {count_completed_tasks} tasks.'
    
    def view_section(self):
        section = f'Section {self.name}:\n'
        return section  + '\n'.join([x.details() for x in self.tasks])


# task = Task("Make bed", "27/05/2020")
# print(task.change_name("Go to University"))
# print(task.change_due_date("28.05.2020"))
# task.add_comment("Don't forget laptop")
# print(task.edit_comment(0, "Don't forget laptop and notebook"))
# print(task.details())
# section = Section("Daily tasks")
# print(section.add_task(task))
# second_task = Task("Make bed", "27/05/2020")
# section.add_task(second_task)
# # section.complete_task("Make bed")

# print(section.clean_section())
# print(section.view_section())
