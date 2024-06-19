import time
import tkinter as tk
import random
from tkinter import colorchooser
from tkinter import messagebox
from pygame import mixer

# Function to play sound during sorting.
def play_sound():
    mixer.init()
    mixer.music.load("assets/audio/beep-sound-8333.mp3")
    mixer.music.set_volume(0.6)
    mixer.music.play()

# Function to disable some buttons when sorting is running.
def disable_all_buttons():
    btn_draw_lines.config(state=tk.DISABLED)
    btn_generate_new_random_numbers.config(state=tk.DISABLED)
    btn_bubble_sort.config(state=tk.DISABLED)
    btn_insertion_sort.config(state=tk.DISABLED)
    btn_selection_sort.config(state=tk.DISABLED)
    btn_gnome_sort.config(state=tk.DISABLED)
    btn_shaker_sort.config(state=tk.DISABLED)
    btn_oddeven_sort.config(state=tk.DISABLED)
    reduce_min_value_btn.config(state=tk.DISABLED)
    increase_min_value_btn.config(state=tk.DISABLED)
    reduce_max_value_btn.config(state=tk.DISABLED)
    increase_max_value_btn.config(state=tk.DISABLED)


# Function to activate the disabled buttons back when the sorting process gets completed.
def activate_all_buttons():
    btn_draw_lines.config(state=tk.NORMAL)
    btn_generate_new_random_numbers.config(state=tk.NORMAL)
    btn_bubble_sort.config(state=tk.NORMAL)
    btn_insertion_sort.config(state=tk.NORMAL)
    btn_selection_sort.config(state=tk.NORMAL)
    btn_gnome_sort.config(state=tk.NORMAL)
    btn_shaker_sort.config(state=tk.NORMAL)
    btn_oddeven_sort.config(state=tk.NORMAL)
    reduce_min_value_btn.config(state=tk.NORMAL)
    increase_min_value_btn.config(state=tk.NORMAL)
    reduce_max_value_btn.config(state=tk.NORMAL)
    increase_max_value_btn.config(state=tk.NORMAL)

# Function to create bar and bar height in the canvas 'canvas1'.
def draw_lines(arr):
    global line_objects,canvas1,bar_color,canvas_bg_color,line_value_objects
    # Delete all previous lines from the canvas.
    canvas1.delete('all')
    line_objects = []
    line_value_objects = []
    status_label.config(text="Idle")
    # Shuffle the given array 'arr'.
    random.shuffle(arr)
    last_x = 14
    # Create lines of width 15 on canvas 'canvas1' along with height of that line as text displaying below the line.
    for num in range(len(arr)):
        # Create line of width 15 with color 'bar_color'.
        line1 = canvas1.create_line(last_x, 0, last_x, arr[num], fill=bar_color, width=15)
        # Insert the created line's object to a list 'line_objects'.
        line_objects.append(line1)
        # Create a text on the canvas 'canvas1' which is actually the value of current array element from array 'arr'.
        # It denotes the height of the line 'line1'.
        line_value = canvas1.create_text(last_x,arr[num]+7,text=str(arr[num]),fill=bar_color)
        # Insert the text's object in a list 'line_value_objects'.
        line_value_objects.append(line_value)
        last_x += 23

# Function to perform bubble sort on given list 'arr'.
def bubble_sort(arr):
    # Disable all sorting buttons.
    disable_all_buttons()
    # Reset the timer text to 0.00
    time_label.config(text="0.00 seconds")
    # Show status
    status_label.config(text="Running Bubble sort..")
    # Store the current time in variable 'starting_time' as beginning time of bubble sort.
    starting_time = calculate_run_start_time()
    n = len(arr)
    for outer in range(0,n):
        for inner in range(0,n-1):
            if arr[inner]>arr[inner+1]:
                exchange(inner,inner+1)
                (arr[inner],arr[inner+1]) = (arr[inner+1],arr[inner])
    # Calculate current time because bubble sort completed now.
    ending_time = calculate_run_end_time()
    # Calculate the total time of execution of bubble sort.
    total_execution_time = find_total_time_to_sort(starting_time,ending_time)
    # Display the total time of execution.
    time_label.config(text=str(total_execution_time)+" seconds")
    # Change status_label text
    status_label.config(text="Bubble sort completed sorting")
    # Activate all the sorting buttons.
    activate_all_buttons()
def insertion_sort(arr):
    # Disable all sorting buttons.
    disable_all_buttons()
    n=len(arr)
    # Reset the timer text to 0.00
    time_label.config(text="0.00 seconds")
    # Show status
    status_label.config(text="Running Insertion sort..")
    # Store the current time in variable 'starting_time' as beginning time of insertion sort.
    starting_time = calculate_run_start_time()
    for outer in range(1,n):
        key = arr[outer]
        key_coord_point = line_objects[outer]
        # Text of bar
        key_coord_point_text = line_value_objects[outer]
        separate_key(key_coord_point,key_coord_point_text)
        inner = outer-1
        while inner>=0 and key<arr[inner]:
            exchange_insertion_sort(key_coord_point,key_coord_point_text,inner)
            arr[inner+1] = arr[inner]
            inner = inner-1
        arr[inner+1] = key
        land_key(key_coord_point,key_coord_point_text,inner+1)
    # Calculate current time because insertion sort completed now.
    ending_time = calculate_run_end_time()
    # Calculate the total time of execution of insertion sort.
    total_execution_time=find_total_time_to_sort(starting_time, ending_time)
    # Display the total time of execution.
    time_label.config(text=str(total_execution_time) + " seconds")
    # Change status_label text
    status_label.config(text="Insertion sort completed sorting")
    # Activate all the sorting buttons.
    activate_all_buttons()

# Function to make the current bar in array in holding when comparison of its predecessors happen in insertion sort.
# This function animates that specific bar to appear as a flying above all the remaining bars in red color.
def separate_key(flying,flying_text):
    global animation_speed
    canvas1.itemconfig(flying,fill="red")
    # Move the specific bar line 'flying' to appear as flying separately to denote comparison.
    canvas1.move(flying,0,250)
    canvas1.move(flying_text,0,250)
    root.update()
    time.sleep(animation_speed)

# Function to make the current bar in canvas get back to its proper place after comparison completes in insertion sort.
def land_key(key_chord_point,key_chord_point_text,land_index):
    global animation_speed,line_objects,line_value_objects
    canvas1.itemconfig(key_chord_point,fill=bar_color)
    # Make that flying bar 'key_chord' and its associated text 'key_chord_point_text' enter in proper sorted place as down.
    canvas1.move(key_chord_point,0,-250)
    canvas1.move(key_chord_point_text,0,-250)
    # Change the positions of the bars in the list of bars 'line_objects' and 'line_value_objects'.
    line_objects[land_index] = key_chord_point
    line_value_objects[land_index] = key_chord_point_text
    root.update()
    time.sleep(animation_speed)

# Function to make the specific bar on hold to move left by one bar,and also the associated text with it.
def exchange_insertion_sort(key_chord_point,key_chord_point_text,a):
    global animation_speed,canvas1,line_objects,line_value_objects
    play_sound()
    height1 = canvas1.coords(line_objects[a])[3]
    x1 = canvas1.coords(line_objects[a])[0]
    # Move one step right side.
    canvas1.move(line_objects[a], 23, 0)
    canvas1.move(line_value_objects[a],23,0)
    # Move the flying key line one step left side.
    canvas1.move(key_chord_point,-23,0)
    canvas1.move(key_chord_point_text,-23,0)
    # Reassign line objects in the array 'line_objects'.
    line_objects[a],line_objects[a+1] = None,line_objects[a]
    line_value_objects[a],line_value_objects[a+1] = None,line_value_objects[a]
    root.update()
    time.sleep(animation_speed)

# Function to swap the elements at indices 'a' and 'b' in the list 'line_objects' and 'line_value_objects'.
def exchange(a,b):
    global canvas1,line_objects,animation_speed,line_value_objects
    play_sound()
    height1 = canvas1.coords(line_objects[a])[3]
    height2 = canvas1.coords(line_objects[b])[3]
    x1 = canvas1.coords(line_objects[a])[0]
    x2 = canvas1.coords(line_objects[b])[0]
    diff = abs(x2-x1)
    if height1>height2:
        # Move the line bar at index 'a' towards right side by 'diff'.
        canvas1.move(line_objects[a],diff,0)
        # Move the text of the line bar at index 'a' towards right side by 'diff'.
        canvas1.move(line_value_objects[a],diff,0)
        # Move the line bar at index 'b' towards left side by 'diff'.
        canvas1.move(line_objects[b],-diff,0)
        # Move the text of the line bar at index 'b' towards left side by 'diff'.
        canvas1.move(line_value_objects[b],-diff,0)
        # Swapping lines in list 'line_objects', and the text of line bars in list 'line_value_objects'.
        line_objects[a],line_objects[b] = line_objects[b],line_objects[a]
        line_value_objects[a],line_value_objects[b] = line_value_objects[b],line_value_objects[a]
    root.update()
    time.sleep(animation_speed)

# Function to perform selection sort on given array 'arr'.
def selection_sort(arr):
    # Disable all sorting buttons.
    disable_all_buttons()
    n = len(arr)
    # Reset the timer text to 0.00
    time_label.config(text="0.00 seconds")
    # Show status.
    status_label.config(text="Running Selection sort...")
    # Store the current time in variable 'starting_time' as beginning time of selection sort.
    starting_time = calculate_run_start_time()
    for outer in range(n):
        min_index = outer
        for inner in range(outer+1,n):
            if arr[inner]<arr[min_index]:
                min_index = inner
        arr[outer],arr[min_index] = arr[min_index],arr[outer]
        exchange(outer,min_index)
    # Calculate current time because selection sort is completed now.
    ending_time = calculate_run_end_time()
    # Calculate the total time of execution of selection sort.
    total_execution_time = find_total_time_to_sort(starting_time, ending_time)
    # Display the total time of execution.
    time_label.config(text=str(total_execution_time) + " seconds")
    # Change status_label text
    status_label.config(text="Selection sort completed sorting")
    # Activate all the disabled buttons.
    activate_all_buttons()


# Function to perform Gnome sort on given array 'arr'.
def gnome_sort(arr):
    # Disable all sorting buttons.
    disable_all_buttons()
    n = len(arr)
    # Reset the timer text to 0.00
    time_label.config(text="0.00 seconds")
    # Show status.
    status_label.config(text="Running Gnome sort...")
    # Store the current time in variable 'starting_time' as beginning time of gnome sort.
    starting_time = calculate_run_start_time()
    curr_index=0
    while curr_index<n:
        if curr_index==0:
            curr_index += 1
        else:
            if arr[curr_index]>=arr[curr_index-1]:
                curr_index += 1
            else:
                # swap here
                arr[curr_index],arr[curr_index-1] = arr[curr_index-1],arr[curr_index]
                exchange(curr_index-1, curr_index)
                curr_index = curr_index-1
    # Calculate current time because Gnome sort is completed now.
    ending_time = calculate_run_end_time()
    # Calculate the total time of execution of Gnome sort.
    total_execution_time = find_total_time_to_sort(starting_time, ending_time)
    # Display the total time of execution.
    time_label.config(text=str(total_execution_time) + " seconds")
    # Change status_label text.
    status_label.config(text="Gnome sort completed sorting")
    # Activate all the disabled buttons.
    activate_all_buttons()

# Function to perform Shaker sort on given array 'arr'.
def shaker_sort(arr):
    # Disable all sorting buttons.
    disable_all_buttons()
    n = len(arr)
    # Reset the timer text to 0.00
    time_label.config(text="0.00 seconds")
    status_label.config(text="Running Shaker sort")
    # Store the current time in variable 'starting_time' as beginning time of Shaker sort.
    starting_time = calculate_run_start_time()
    for outer in range(0,n):
        if outer%2==0:
            for inner in range(0,n-1):
                if arr[inner]>arr[inner+1]:
                    exchange(inner,inner+1)
                    (arr[inner],arr[inner+1]) = (arr[inner+1],arr[inner])
        else:
            for inner_reverse in range(n-1,0,-1):
                if arr[inner_reverse]<arr[inner_reverse-1]:
                    exchange(inner_reverse-1,inner_reverse)
                    arr[inner_reverse],arr[inner_reverse-1]=arr[inner_reverse-1],arr[inner_reverse]
    # Calculate current time because Shaker sort is completed now.
    ending_time = calculate_run_end_time()
    # Calculate the total time of execution of Shaker sort.
    total_execution_time = find_total_time_to_sort(starting_time, ending_time)
    # Display the total time of execution.
    time_label.config(text=str(total_execution_time) + " seconds")
    # Change status_label text.
    status_label.config(text="Shaker sort completed sorting")
    # Activate all the disabled buttons.
    activate_all_buttons()


# Function to perform Odd even sort on the given array 'arr'.
def odd_even_sort(arr):
    # Disable all sorting buttons.
    disable_all_buttons()
    n = len(arr)
    swapped = True
    # Reset the timer text to 0.00
    time_label.config(text="0.00 seconds")
    status_label.config(text="Running Odd Even sort")
    # Store the current time in variable 'starting_time' as beginning time of Odd even sort.
    starting_time = calculate_run_start_time()
    while swapped==True:
        swapped = False
        # odd indices iteration
        ptr = 1
        while ptr<n:
            if (ptr+1)<n:
                if arr[ptr]>arr[ptr+1]:
                    #swap
                    exchange(ptr, ptr + 1)
                    arr[ptr],arr[ptr+1] = arr[ptr+1],arr[ptr]
                    swapped=True
            ptr = ptr+2
        # Even indices iteration
        ptr = 0
        while ptr<n:
            if (ptr+1)<n:
                if arr[ptr]>arr[ptr+1]:
                    # swap here
                    exchange(ptr,ptr+1)
                    arr[ptr],arr[ptr+1] = arr[ptr+1],arr[ptr]
                    swapped = True
            ptr = ptr+2
    # Calculate current time because Odd even sort is completed now.
    ending_time = calculate_run_end_time()
    # Calculate the total time of execution of Odd even sort.
    total_execution_time = find_total_time_to_sort(starting_time, ending_time)
    # Display the total time of execution.
    time_label.config(text=str(total_execution_time) + " seconds")
    status_label.config(text="Odd Even sort completed sorting")
    # Activate all the disabled buttons.
    activate_all_buttons()


# Function to change the fill color of all lines in the canvas 'canvas1'.
# This color is changed and displayed during next generation of new numbers, or on clicking the 'Randomize' button.
def change_bar_color():
    global bar_color,canvas_bg_color
    selected_color = colorchooser.askcolor()
    if selected_color!=(None,None):
        if selected_color[1]!=canvas_bg_color:
            bar_color = str(selected_color[1])
            canvas2.config(background=bar_color)
        else: # If the currently selected color for bar is same as the background of canvas1, do not change bar color.
            messagebox.showwarning("Same color","Same color for bar and background.\nPlease choose another color.")

# Function to change the background color of the background of the canvas 'canvas1'.
def change_canvas_background_color():
    global canvas_bg_color,bar_color
    selected_color = colorchooser.askcolor()
    if selected_color!=(None,None):
        if selected_color[1]!=bar_color:
            canvas_bg_color = str(selected_color[1])
            canvas3.config(background=canvas_bg_color)
            canvas1.config(background=canvas_bg_color)
        else: # Alerts when bar color and background color of canvas 'canvas1' is same.
            messagebox.showwarning("Same color","Same color for bar and background.\nPlease choose another color.")

# Function to change the animation speed based on the value on scale.
def change_animation_speed():
    global animation_speed
    animation_speed = scale.get()
    scale.set(scale.get())

# Function to generate new random numbers for the list 'arr'.
# The numbers in the array will be between the value of variables 'arr_min_value' and 'arr_max_value'.
def generate_random_numbers():
    global arr,arr_min_value,arr_max_value
    # Empty the array 'arr'.
    arr = []
    status_label.config(text="Idle")
    # Generate 56 numbers in array 'arr' between values 'arr_min_value' and 'arr_max_value'.
    for _ in range(0,56):
        num = random.randrange(arr_min_value,arr_max_value)
        arr.append(num)
    # Draw new bar lines in canvas 'canvas1' based on the array 'arr'.
    draw_lines(arr)


# Function to calculate current time for the beginning of a sorting process.
def calculate_run_start_time():
    milliseconds = int(time.time() * 1000)
    return milliseconds

# Function to calculate current time for the completion of a sorting process.
def calculate_run_end_time():
    milliseconds2 = int(time.time()*1000)
    return milliseconds2

# Function to calculate the difference between the given two time values in milliseconds to seconds.
def find_total_time_to_sort(start_time,end_time):
    answer = (end_time-start_time)/1000.0
    return answer  # Returning in seconds.
def subtract_min_value_of_array():
    global arr_min_value,label_min_arr_value
    if arr_min_value>10:
        arr_min_value = arr_min_value-1
        label_min_arr_value.config(text="Min: "+str(arr_min_value))
def add_min_value_of_array():
    global arr_min_value,label_min_arr_value,arr_max_value
    if arr_min_value==(arr_max_value-2):
        messagebox.showerror("Invalid", "Minimum number of array cannot be greater than the maximum number")
    elif arr_min_value<595:
        arr_min_value += 1
        label_min_arr_value.config(text="Min: " + str(arr_min_value))
def subtract_max_value_of_array():
    global arr_max_value,label_max_arr_value,arr_min_value
    if arr_max_value==(arr_min_value+2):
        messagebox.showerror("Invalid","Maximum number of array cannot be less than minimum number")
    elif arr_max_value>10:
        arr_max_value = arr_max_value-1
        label_max_arr_value.config(text="Max: "+str(arr_max_value))
def add_max_value_of_array():
    global arr_max_value,label_max_arr_value
    if arr_max_value<595:
        arr_max_value += 1
        label_max_arr_value.config(text="Max: " + str(arr_max_value))

# Function to show app about section.
def show_about():
    messagebox.showinfo("About Sorting Visualizer","Version:1.0\nDate of release:20th June 2024\nOS: Windows 10 or later\nDeveloper: Reshma Haridhas")

# GUI
root = tk.Tk()
root.geometry("1500x750")
root.minsize(width=1500,height=750)
root.title("Sorting Visualizer")
root.config(bg="#cef6ff")
frame_canvas = tk.Frame(root,background="#cef6ff")
frame_canvas.grid(row=0,column=0)
bar_color="blue"
canvas_bg_color = "#FFFFFF"
animation_speed = 0.09
arr_min_value = 10
arr_max_value = 600
stopwatch_icon = tk.PhotoImage(file="assets/images/icons8-stopwatch-64.png").subsample(2,2)
sorting_visualizer_icon = tk.PhotoImage(file="assets/images/sorting_visualizer_icon.png")
# Menu bar
menubar1 = tk.Menu(root)
root.config(menu=menubar1)
fileMenu = tk.Menu(menubar1,tearoff=0)
menubar1.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Exit",command=root.destroy)
helpMenu = tk.Menu(menubar1,tearoff=0)
menubar1.add_cascade(label="Help",menu=helpMenu)
helpMenu.add_command(label="About",command=show_about)
# UI
status_label = tk.Label(frame_canvas,text="Idle",bg="#CEF6FF",font=("Times New Roman",10,"italic"))
status_label.grid(row=0,column=0,pady=3)
# Canvas to show bars
canvas1 = tk.Canvas(frame_canvas,width=1300,height=660,background="#FFFFFF",highlightbackground="black")
canvas1.grid(row=1,column=0,padx=10,pady=5)
# Side frame
side_frame = tk.Frame(root,background="#cef6ff")
side_frame.grid(row=0,column=1)
# Frame to hold the UI controls for setting minimum value and maximum value of array.
entry_frame = tk.Frame(side_frame,background="#cef6ff")
entry_frame.grid(row=0,column=0,pady=20)
# Minimum value of array to generate.
reduce_min_value_btn = tk.Button(entry_frame,text="-",command=subtract_min_value_of_array,bg="#FFE082")
reduce_min_value_btn.grid(row=0,column=0)
label_min_arr_value = tk.Label(entry_frame,text="Min: 10",background="#cef6ff",font=("Arial",12))
label_min_arr_value.grid(row=0,column=1)
increase_min_value_btn = tk.Button(entry_frame,text="+",command=add_min_value_of_array,bg="#FFE082")
increase_min_value_btn.grid(row=0,column=2)
# Maximum value of array to generate.
reduce_max_value_btn = tk.Button(entry_frame,text="-",command=subtract_max_value_of_array,bg="#FFE082")
reduce_max_value_btn.grid(row=1,column=0,pady=7)
label_max_arr_value = tk.Label(entry_frame,text="Max: 600",background="#cef6ff",font=("Arial",12))
label_max_arr_value.grid(row=1,column=1,pady=7)
increase_max_value_btn = tk.Button(entry_frame,text="+",command=add_max_value_of_array,bg="#FFE082")
increase_max_value_btn.grid(row=1,column=2,pady=7)
# Button to choose bar line color in the canvas 'canvas1'.
color_choose_btn = tk.Button(side_frame,text="Choose Bar color",bg="#FFE082",fg="#000000",command=change_bar_color,font=("Georgia",13))
color_choose_btn.grid(row=1,column=0,pady=7)
canvas2 = tk.Canvas(side_frame,width=30,height=20,background=bar_color,highlightbackground="black")
canvas2.grid(row=2,column=0,pady=7)
# Button to choose background color of canvas 'canvas1'.
background_color_choose_btn = tk.Button(side_frame,text="Choose\nbackground color",bg="#FFE082",fg="#000000",command=change_canvas_background_color,font=("Georgia",13))
background_color_choose_btn.grid(row=3,column=0,pady=7)
canvas3 = tk.Canvas(side_frame,width=30,height=20,background=canvas_bg_color,highlightbackground="black")
canvas3.grid(row=4,column=0,pady=7)
# Button to confirm changing speed of animation by getting from scale.
button_animation_speed = tk.Button(side_frame,text="Change Speed",command=change_animation_speed,bg="#FFE082",font=("Georgia",13))
button_animation_speed.grid(row=5,column=0,pady=6)
# Scale to set the animation speed to increase or decrease between values 0.02 and 1.5.
scale = tk.Scale(side_frame,from_=0.02,to=1.5,orient=tk.HORIZONTAL,resolution=0.01,sliderlength=10,length=150,background="#cef6ff",highlightbackground="#cef6ff")
scale.grid(row=6,column=0,pady=7)
# Initially the animation speed is 0.09. Hence setting it to display in the scale.
scale.set(0.09)
tk.Label(side_frame,text="Total time",bg="#CEF6FF",font=("Georgia",13),image=stopwatch_icon,compound=tk.LEFT).grid(row=7,column=0)
time_label = tk.Label(side_frame,text="0.00",bg="#CEF6FF",font=("Georgia",13))
time_label.grid(row=8,column=0)
# Frame to hold the buttons below the canvas.
btn_frame = tk.Frame(root,background="#cef6ff")
btn_frame.grid(row=1,column=0)
btn_draw_lines = tk.Button(btn_frame,text="Randomize",bg="blue",fg="white",font=("Arial",15),activebackground="blue",command=lambda :draw_lines(arr))
btn_draw_lines.grid(row=0,column=0,padx=5)
btn_generate_new_random_numbers = tk.Button(btn_frame,text="Generate new numbers",command=generate_random_numbers,font=("Georgia",15),bg="violet")
btn_generate_new_random_numbers.grid(row=0,column=1,padx=7)
btn_bubble_sort = tk.Button(btn_frame,text="Bubble sort",bg="purple",fg="white",font=("Arial",15),activebackground="purple",command=lambda :bubble_sort(arr))
btn_bubble_sort.grid(row=0,column=2,padx=3)
btn_insertion_sort = tk.Button(btn_frame,text="Insertion sort",command=lambda :insertion_sort(arr),font=("Arial",15),bg="turquoise",activebackground="turquoise")
btn_insertion_sort.grid(row=0,column=3,padx=3)
btn_selection_sort = tk.Button(btn_frame,text="Selection sort",command=lambda :selection_sort(arr),font=("Arial",15),bg="pink",activebackground="pink")
btn_selection_sort.grid(row=0,column=4,padx=3)
btn_gnome_sort = tk.Button(btn_frame,text="Gnome sort",command=lambda :gnome_sort(arr),font=("Arial",15),bg="red",fg="white",activebackground="red")
btn_gnome_sort.grid(row=0,column=5,padx=3)
btn_shaker_sort = tk.Button(btn_frame,text="Shaker sort",command=lambda :shaker_sort(arr),bg="orange",font=("Arial",15),activebackground="orange")
btn_shaker_sort.grid(row=0,column=6,padx=5)
btn_oddeven_sort = tk.Button(btn_frame,text="Odd even sort",command=lambda :odd_even_sort(arr),bg="brown",activebackground="brown",fg="white",font=("Arial",15))
btn_oddeven_sort.grid(row=0,column=7,padx=4)
# array of numbers
arr = [64,300,100,200,150,230,50,20,77,81,90,34,44,55,13,10,130,585,444,100,270,224,68,73,85,97,250,330,210,110,125,30,40,60,600,500,530,520,93,420,400,360,340,450,550,476,170,181,190,144,140,570,504,34,122,222]
# list to hold bar (lines) in canvas 'canvas1'.
line_objects = []
#  list to hold text under each bar in canvas 'canvas1'.
line_value_objects = []
# Draw bars initially.
draw_lines(arr)
# Setting icon in the title bar of the app.
root.iconphoto(True,sorting_visualizer_icon)
root.mainloop()