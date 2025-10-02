
class User:
    def __init__(self, first_name: str, last_name: str, email: str):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.tasks = []  

    def assign_task(self, task):
        if task not in self.tasks:
            self.tasks.append(task)
            task.assigned_to = self
        else:
            pass

    def unassign_task(self, task):
       
        if task in self.tasks:
            self.tasks.remove(task)
            task.assigned_to = None
        else:
            pass



class Task:
    def __init__(self, title: str, priority: str = "Medium", status: str = "in process"):
        self.title = title
        self.priority = priority    
        self.status = status        
        self.assigned_to = None     

    def mark_status(self, new_status: str):
        self.status = new_status


class Project:
    def __init__(self, name: str, description: str = ""):
        self.name = name
        self.description = description
        self.users = []  
        self.tasks = [] 

    def add_user(self, user):
        if user not in self.users:
            self.users.append(user)

    def add_task(self, task):
        if task not in self.tasks:
            self.tasks.append(task)
