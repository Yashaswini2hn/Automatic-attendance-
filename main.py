import tkinter as tk
from PIL import Image, ImageTk
import subprocess
root = tk.Tk()
root.resizable(False, False)
root.title("AMS")

# open the gif file using PIL
gif = Image.open('new.gif')

# create a sequence of PhotoImage objects for each frame of the gif
frames = []
for frame in range(0, gif.n_frames):
    gif.seek(frame)
    frame_image = ImageTk.PhotoImage(gif)
    frames.append(frame_image)

# create a canvas widget on top of the gif
canvas = tk.Canvas(root, width=gif.width, height=gif.height)
canvas.pack()
canvas.create_image(0, 0, anchor="nw", image=frames[0])
canvas.create_text(400,40, text="Attendance Management System", font=("Helvetica", 35,"bold"),activefill="red",fill="yellow",justify="center")
canvas.create_text(400,80, text="Say Bye Bye To REGISTER", font=("Helvetica", 15,"bold"),activefill="red",fill="yellow",justify="center",)
canvas.create_text(680,500, text="Developed BY:-\nPrathap J\nYashaswini H N\nVarsha S\nMD Ibrahim\n\nGuide:-Ambika K B", font=("Arial", 12,"bold"), fill="white",activefill="orange",justify="left")


# define a function to animate the gif
def animate(frame):
    canvas.itemconfig(1, image=frames[frame])
    frame += 1
    if frame == len(frames):
        frame = 0
    root.after(50, animate, frame)

# start the animation
animate(0)
#offline button page 3
def offline():
    subprocess.Popen(["python", "offline.py"]) 

#CRETAE DATASET
def dataset():
    subprocess.Popen(["python","datasetpg.py"])
def online():
    subprocess.Popen(["python","online.py"])
    #admin
def start_button():
    import tkinter as tk
    import subprocess
    from tkinter import font
    from tkinter import font, simpledialog, messagebox
    import os

    def create_default_user():
        default_username = "admin"
        default_password = "123"
        users_folder = 'users'

        if not os.path.exists(users_folder):
            os.makedirs(users_folder)

        user_file_path = os.path.join(users_folder, f'{default_username}.txt')

        if not os.path.exists(user_file_path):
            with open(user_file_path, 'w') as user_file:
                user_file.write(default_password)

    def submit_login():
        # Check if the username and password are correct
        def check_credentials(username, password):
            users_folder = 'users'
            user_file_path = os.path.join(users_folder, f'{username}.txt')

            if os.path.exists(user_file_path):
                with open(user_file_path, 'r') as user_file:
                    stored_password = user_file.read()

                return password == stored_password
            else:
                return False

        # Check if the username and password are correct
        if check_credentials(username_entry.get(), password_entry.get()):
            # Close the login window and open the method window
            login_root.destroy()
            method_window()
        else:
            # Clear the entry widgets and display an error message
            username_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
            error_label.config(text="Incorrect username or password", fg="red")

# Create the default user and password
    create_default_user()
    
     #method page2   
    def method_window():
        # Create a new tkinter window for the method selection
        method_root = tk.Tk()
        method_root.title("Method Selection")
        method_root.geometry("600x400")
        method_root.configure(bg="BLACK")
        method_root.resizable("false","false")

        # Add the method selection widgets
        label = tk.Label(method_root, text="Choose the Method", font=("Arial", 20,"bold"), fg="blue", bg="BLACK")
        label.place(x="160", y="40")
        button1 = tk.Button(method_root, text="Offline", borderwidth="10", bg="DARKRED", fg="WHITE", font=("Helvetica", 20,"bold"), activebackground="DARKGREEN", command=offline)
        button1.pack(side=tk.LEFT, padx=100)
        button1.place(x="65", y="180")
        button2 = tk.Button(method_root, text="Online", borderwidth="10", bg="DARKGREEN", fg="WHITE", font=("Helvetica", 20,"bold"), activebackground="DARKRED", command=online)
        button2.pack(side=tk.RIGHT, padx=100)
        button2.place(x="400", y="180")
        button3 = tk.Button(method_root, text="Create Dataset", borderwidth="10", bg="DARKBLUE", fg="WHITE", font=("Helvetica", 20,"bold"), activebackground="DARKRED", command=dataset)
        button3.pack(side=tk.RIGHT, padx=100)
        button3.place(x="180", y="300")

        method_root.mainloop()

    # Create a new tkinter window for the login screen


    def add_user():
        default_username = "admin"
        default_password = "123"
        
        entered_default_username = simpledialog.askstring("Default User", "Enter the default username:")
        entered_default_password = simpledialog.askstring("Default User", "Enter the default password:", show="*")
        
        if entered_default_username == default_username and entered_default_password == default_password:
            new_username = simpledialog.askstring("New User", "Enter the new username:")
            new_password = simpledialog.askstring("New User", "Enter the new password:", show="*")
            
            if new_username and new_password:
                users_folder = 'users'
                if not os.path.exists(users_folder):
                    os.makedirs(users_folder)
                
                with open(os.path.join(users_folder, f'{new_username}.txt'), 'w') as user_file:
                    user_file.write(new_password)
                
                messagebox.showinfo("Success", "New user created successfully.")
            else:
                messagebox.showerror("Error", "Both username and password are required.")
        else:
            messagebox.showerror("Error", "Invalid default username or password.")

    def delete_user():
        default_username = "admin"
        default_password = "123"
        
        entered_default_username = simpledialog.askstring("Default User", "Enter the default username:")
        entered_default_password = simpledialog.askstring("Default User", "Enter the default password:", show="*")
        
        if entered_default_username == default_username and entered_default_password == default_password:
            username_to_delete = simpledialog.askstring("Delete User", "Enter the username to delete:")
            
            if username_to_delete:
                users_folder = 'users'
                user_file_path = os.path.join(users_folder, f'{username_to_delete}.txt')
                
                if os.path.exists(user_file_path):
                    os.remove(user_file_path)
                    messagebox.showinfo("Success", "User deleted successfully.")
                else:
                    messagebox.showerror("Error", "User not found.")
            else:
                messagebox.showerror("Error", "Username is required.")
        else:
            messagebox.showerror("Error", "Invalid default username or password.")


    login_root = tk.Tk()
    login_root.title("Login")
    login_root.geometry("450x350")
    login_root.resizable(False, False)
    login_root.configure(bg="#2E3440")

    # Custom fonts
    label_font = font.Font(family="Helvetica", size=14, weight="bold")
    entry_font = font.Font(family="Helvetica", size=12)
    button_font = font.Font(family="Helvetica", size=12, weight="bold")

    # Add the login widgets
    username_label = tk.Label(login_root, text="Username:", bg="#2E3440", fg="#ECEFF4", font=label_font)
    username_label.pack(pady=20)
    username_entry = tk.Entry(login_root, font=entry_font)
    username_entry.pack(pady=5)
    password_label = tk.Label(login_root, text="Password:", bg="#2E3440", fg="#ECEFF4", font=label_font)
    password_label.pack(pady=20)
    password_entry = tk.Entry(login_root, show="*", font=entry_font)
    password_entry.pack(pady=5)
    submit_button = tk.Button(login_root, text="Submit", command=submit_login, bg="#5E81AC", fg="#ECEFF4", font=button_font)
    submit_button.place(x=200, y=240)
    add_user_button = tk.Button(login_root, text="Add User", command=add_user, bg="#88C0D0", fg="#2E3440", font=button_font)
    add_user_button.place(x=105, y=290)
    delete_user_button = tk.Button(login_root, text="Delete User", command=delete_user, bg="#BF616A", fg="#ECEFF4", font=button_font)
    delete_user_button.place(x=280, y=290)
    error_label = tk.Label(login_root, text="", bg="#2E3440", fg="#BF616A")
    error_label.pack()

    login_root.mainloop()


#main start button
button_image = tk.PhotoImage(file="start.png")
button = tk.Button(root,command=start_button, image=button_image,borderwidth="6",bg="skyblue",height="80",width="220")
button.place(x=40, y=450)
root.mainloop()
