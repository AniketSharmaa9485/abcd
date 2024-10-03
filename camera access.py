import cv2
import tkinter as tk
from tkinter import Label

class CameraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Camera Access App")

        # Create a label widget to display instructions
        self.label = Label(root, text="Press 'q' to quit the camera view.")
        self.label.pack()

        # Button to start camera
        self.start_button = tk.Button(root, text="Start Camera", command=self.start_camera)
        self.start_button.pack()

    def start_camera(self):
        cap = cv2.VideoCapture(0)  # Open the default camera

        if not cap.isOpened():
            print("Cannot open camera")
            return

        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()

            # If frame reading was not successful, break the loop
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break

            # Display the resulting frame
            cv2.imshow('Camera', frame)

            # Exit the camera view when 'q' key is pressed
            if cv2.waitKey(1) == ord('q'):
                break

        # Release the camera and close all OpenCV windows
        cap.release()
        cv2.destroyAllWindows()

# The main function
if __name__ == "__main__":
    root = tk.Tk()  # Create the Tkinter root window
    app = CameraApp(root)  # Instantiate the CameraApp class with the Tkinter root
    root.mainloop()  # Start the Tkinter event loop
