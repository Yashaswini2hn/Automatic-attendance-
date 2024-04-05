import os
import cv2
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog, simpledialog

class DatasetCreator:
        def __init__(self, master):
            self.master = master
            self.master.title("Dataset Creator")
            self.master.geometry("800x500")
            self.master.resizable(False, False)

            # create video frame
            self.video_frame = tk.Frame(self.master, relief=tk.SUNKEN, bd=2)
            self.video_frame.place(x=10, y=10, width=640, height=480)

            # create canvas for displaying video
            self.canvas = tk.Canvas(self.video_frame, bg='black', width=640, height=480)
            self.canvas.pack()

            # create widgets
            self.button_capture = tk.Button(self.master, text="Capture Image", command=self.capture_image,bg="red",activebackground="green",borderwidth=10)
            self.button_new_person = tk.Button(self.master, text="New Person..", command=self.new_person,bg="red",activebackground="green",borderwidth=10)

            # arrange widgets
            self.button_capture.place(x=670, y=200)
            self.button_new_person.place(x=670, y=300)

            # initialize video capture
            self.cap = cv2.VideoCapture(1)

            # Automatically create a dataset folder
            self.dataset_folder = "dataset"
            os.makedirs(self.dataset_folder, exist_ok=True)

            # Set the person's name for the dataset
            self.set_person_name()

            self.play()

        def set_person_name(self):
            while True:
                self.person_name = simpledialog.askstring("Input", "Enter the person's name for the dataset:")
                if self.person_name:
                    break
            self.image_counter = 0

        def new_person(self):
            self.set_person_name()

        def capture_image(self):
            if self.person_name:
                person_dir = os.path.join(self.dataset_folder, self.person_name)
                os.makedirs(person_dir, exist_ok=True)

                ret, frame = self.cap.read()
                if ret:
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    image_filename = f"{self.person_name}_{self.image_counter}.png"
                    image_path = os.path.join(person_dir, image_filename)
                    cv2.imwrite(image_path, frame)

                    self.image_counter += 1

        def play(self):
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = cv2.resize(frame, (640, 480))

                image = Image.fromarray(frame)
                photo = ImageTk.PhotoImage(image)
                self.canvas.create_image(0, 0, image=photo, anchor=tk.NW)
                self.canvas.image = photo
                self.master.after(10, self.play)

if __name__ == '__main__':
        root = tk.Tk()
        app = DatasetCreator(root)
        root.mainloop()