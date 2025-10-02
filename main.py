from models import User, Task, Project

u1 = User("sofo", "danelia", "sd@gmail.com")
u2 = User("lizi", "danelia", "ld@gmail.com")

t1 = Task("base", priority="High")
t2 = Task("main.pages dizaini", priority="Medium")
t3 = Task("testirebistvis")   


p1 = Project("System")

p1.add_user(u1)
p1.add_user(u2)
p1.add_task(t1)
p1.add_task(t2)
p1.add_task(t3)

u1.assign_task(t1)
u2.assign_task(t2)
u1.assign_task(t3)

t1.mark_status("In Progress")
t2.mark_status("Completed")

print("პროექტის სახელი:", p1.name)

print("მომხმარებლები:")
for u in p1.users:
    print(f"{u.first_name} ({u.email})")

print("დავალებები:")
for t in p1.tasks:
    assigned = t.assigned_to.first_name if t.assigned_to else "არავინ"
    print(f"{t.title} | სტატუსი: {t.status} | ვისთანაა: {assigned}")
