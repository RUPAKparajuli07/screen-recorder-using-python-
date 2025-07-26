import cv2
import pyautogui
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import ImageTk, Image
import numpy as np

# Define the screen size and geometry
SCREEN_SIZE = (500, 600)

# Create the main GUI window
window = tk.Tk()
window.title("Screen Recorder")
window.geometry("300x200")

# Create a label to display recording status
status_label = tk.Label(window, text="Not Recording", font=("Bell MT", 30), fg="red")
status_label.pack(pady=10)

# Create the OpenCV window for displaying the screen recording
cv2.namedWindow('Screen Recording')

# Create a variable to track the microphone state
is_microphone_on = tk.BooleanVar()
is_microphone_on.set(True)

# Create a checkbox for the microphone   
microphone_checkbox = tk.Checkbutton(window, text="Microphone", font=("Arial", 12), variable=is_microphone_on)
microphone_checkbox.pack(pady=5)

# Create a variable to track the speaker state
is_speaker_on = tk.BooleanVar()
is_speaker_on.set(True)

# Create a checkbox for the speaker
speaker_checkbox = tk.Checkbutton(window, text="Speaker", font=("Arial", 12), variable=is_speaker_on)
speaker_checkbox.pack(pady=5)

def start_recording():
    # Prompt the user to select the save location
    output_file = filedialog.asksaveasfilename(defaultextension=".mp4",
                                               filetypes=[("MP4 Video Files", "*.mp4")])
    if output_file:
        # Define the codec and create a VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_file, fourcc, 30.0, SCREEN_SIZE)

        status_label.config(text="Recording")
        record_button.config(state=tk.DISABLED)
        stop_button.config(state=tk.NORMAL)

        try:
            while True:
                # Capture the screen image
                img = pyautogui.screenshot()

                # Resize the image to the defined screen geometry
                img = img.resize(SCREEN_SIZE)

                # Convert the image to BGR format
                frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

                # Write the frame to the output video file
                out.write(frame)

                # Display the resulting frame
                cv2.imshow('Screen Recording', frame)

                # Stop recording when 'q' is pressed
                if cv2.waitKey(1) == ord('q'):
                    break

        finally:
            # Release the VideoWriter and destroy the OpenCV window
            out.release()
            cv2.destroyAllWindows()

            messagebox.showinfo("Recording Complete", "Screen recording saved as '{}'".format(output_file))
            status_label.config(text="Not Recording")
            record_button.config(state=tk.NORMAL)
            stop_button.config(state=tk.DISABLED)

def stop_recording():
    cv2.destroyAllWindows()
    
    messagebox.showinfo("Recording Stopped", "Screen recording stopped")
    status_label.config(text="Not Recording")
    record_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)

# Create the record button
record_button = tk.Button(window, text="Start Recording", font=("Arial", 12), command=start_recording)
record_button.pack(pady=5)

# Create the stop button
stop_button = tk.Button(window, text="Stop Recording", font=("Arial", 12), command=stop_recording, state=tk.DISABLED)
stop_button.pack(pady=5)

# Run the GUI
window.mainloop()



