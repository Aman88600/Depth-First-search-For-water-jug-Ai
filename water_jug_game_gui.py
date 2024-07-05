#1 Fill the left jug completely
#2 Fill the right jug completely
#3 Empty the left jug
#4 Empty the right jug
#5 Fill the left jug from the right jug
#6 Fill the right jug from the right jug

from tkinter import *
root = Tk()
import os
import subprocess



left_jug_capacity_label = Label(root, text = "Left Jug capacity")
left_jug_capacity_label.grid(row = 0, column = 0)
left_jug_capacity = Entry(root)
left_jug_capacity.grid(row = 0, column = 1)

right_jug_capacity_label = Label(root, text = "Right Jug capacity")
right_jug_capacity_label.grid(row = 1, column = 0)
right_jug_capacity = Entry(root)
right_jug_capacity.grid(row = 1, column = 1)

initial_left_jug_label = Label(root, text = "Initial Left Jug")
initial_left_jug_label.grid(row = 2, column = 0)
initial_left_jug = Entry(root)
initial_left_jug.grid(row = 2, column = 1)

initial_right_jug_label = Label(root, text = "Initial right Jug")
initial_right_jug_label.grid(row = 3, column = 0)
initial_right_jug = Entry(root)
initial_right_jug.grid(row = 3, column = 1)

final_left_jug_label = Label(root, text = "Final Left Jug")
final_left_jug_label.grid(row = 4, column = 0)
final_left_jug = Entry(root)
final_left_jug.grid(row = 4, column = 1)


final_right_jug_label = Label(root, text = "Final right Jug")
final_right_jug_label.grid(row = 5, column = 0)
final_right_jug = Entry(root)
final_right_jug.grid(row = 5, column = 1)

la = Label(root)
la.grid(row = 10, column = 0)


def button_function():
    left_jug_capacity_entry = int(left_jug_capacity.get())
    right_jug_capacity_entry = int(right_jug_capacity.get())
    initial_left_jug_entry = int(initial_left_jug.get())
    initial_right_jug_entry = int(initial_right_jug.get())
    final_left_jug_entry = int(final_left_jug.get())
    final_right_jug_entry = int(final_right_jug.get())
    print(f"left_jug_capacity_entry = {left_jug_capacity_entry}")
    print(f"right_jug_capacity_entry = {right_jug_capacity_entry}")
    print(f"initial_left_jug_entry = {initial_left_jug_entry}")
    print(f"initial_right_jug_entry = {initial_right_jug_entry}")
    print(f"final_left_jug_entry = {final_left_jug_entry}")
    print(f"final_right_jug_entry = {final_right_jug_entry}")
    result = subprocess.run(
        ["python", "DFS_water_jug.py", str(left_jug_capacity_entry), str(right_jug_capacity_entry),
         str(initial_left_jug_entry), str(initial_right_jug_entry), str(final_left_jug_entry), str(final_right_jug_entry)],
        capture_output=True, text=True
    )
    
    # Display the captured output in the label
    la.config(text=result.stdout)



ok_button = Button(root, text = "click", command = button_function)
ok_button.grid(row = 7, column = 0)
root.mainloop()