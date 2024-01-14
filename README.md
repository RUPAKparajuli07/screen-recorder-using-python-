## Screen Recorder Documentation

### Overview
This Python script utilizes the OpenCV, PyAutoGUI, Tkinter, and PIL libraries to create a simple screen recorder application. The application allows users to record their screen along with optional microphone and speaker audio. The recorded video is saved in MP4 format.

### Dependencies
- OpenCV: Used for capturing the screen and saving the recorded frames.
- PyAutoGUI: Used for taking screenshots and capturing the screen.
- Tkinter: Used for creating the graphical user interface.
- PIL (Pillow): Used for image processing and displaying screenshots in the Tkinter window.

### Installation
Ensure that you have the necessary libraries installed by running the following command:
```bash
pip install opencv-python pyautogui Pillow
```

### Usage

#### 1. Run the Script
Run the script, and a Tkinter window titled "Screen Recorder" will appear.

#### 2. GUI Elements

- **Recording Status Label:** Displays the current recording status ("Not Recording" or "Recording").
- **Microphone Checkbox:** Allows the user to enable or disable recording of the microphone audio.
- **Speaker Checkbox:** Allows the user to enable or disable recording of the speaker audio.
- **Start Recording Button:** Initiates the screen recording process.
- **Stop Recording Button:** Stops the screen recording process.

#### 3. Start Recording
Click the "Start Recording" button to begin the screen recording process. A file dialog will prompt you to select the location to save the recorded video. Choose a location and provide a filename with the ".mp4" extension.

#### 4. Recording
Once started, the script continuously captures the screen at a rate of 30 frames per second. The OpenCV window titled "Screen Recording" will display the recording in real-time.

#### 5. Stop Recording
Click the "Stop Recording" button or press the 'q' key while the recording is in progress to stop the screen recording. The OpenCV window will close, and a message box will confirm that the recording has stopped. The recorded video will be saved to the specified location.

### Notes
- Ensure that you have the necessary permissions to write to the selected file location.
- The recording can be stopped by clicking the "Stop Recording" button or pressing the 'q' key while the recording is in progress.

### Troubleshooting
- If the script encounters any issues during recording, such as a failure to save the file, check the console for error messages.
- Ensure that the required libraries are installed, and the script is run in a Python environment that has the necessary permissions.

### Disclaimer
This script is provided as-is, and the developer holds no responsibility for any misuse or unintended consequences resulting from its use. Use this script responsibly and adhere to relevant laws and regulations regarding screen recording and privacy.
