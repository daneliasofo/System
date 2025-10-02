##System

## User
first_name– მომხმარებლის სახელი
last_name – მომხმარებლის გვარი
email – ელფოსტა
tasks – დავალებების სია
assign_task(task) – მომხმარებელზე დავალების მიბმა
unassign_task(task) – დავალების მოხსნა

## Task
title – დავალების სახელი
priority – პრიორიტეტი (High, Medium, Low)
status – სტატუსი (Pending, In Progress, Completed)
assigned_to – რომელი User-ზეა მიბმული
mark_status(new_status) – სტატუსის შეცვლა

## Project
name – პროექტის სახელი
description– პროექტის აღწერა
users – პროექტის მონაწილე მომხმარებლები
tasks – პროექტში არსებული დავალებები
add_user(user) – მომხმარებლის დამატება
add_task(task) – დავალების დამატება
