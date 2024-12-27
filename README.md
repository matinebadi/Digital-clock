![digital_clocke](https://github.com/user-attachments/assets/34da19c0-cf73-438c-8500-f8b68b5b212d)


# Digital Watch - Tehran Time

A simple digital clock application developed in Python using Tkinter. This project displays the current time in Tehran, Iran with a modern, minimalistic interface.

## Features

- **Live Clock:** Displays the current time in Tehran (UTC+3:30).
- **Digital Display:** Uses a clear, readable font for time and date.
- **Background Image:** A black background with adjustable opacity.
- **Responsive Font:** The font size adjusts based on the window size to maintain readability.

## Requirements

- Python 3.x
- Tkinter
- Pillow (PIL)

You can install the required libraries using pip:

```bash
pip install pillow

How to Run

1. Clone or download the project.


2. Open a terminal and navigate to the project directory.


3. Run the script:



python digital_watch.py

Code Explanation

Tkinter Window Setup

The window is created using Tkinter with specific properties:

Title: Digital Watch - Tehran Time

Dimensions: 240x100

Transparency: The window has a slight transparency with alpha = 0.7.

Resizable: The window can be resized to adjust the font size dynamically.


Time Calculation

The script calculates the current time in Tehran by adding 3 hours and 30 minutes to UTC time. It uses the datetime library to format the time and date.

Fonts and Labels

The main clock is displayed using the Times New Roman font with a size dynamically adjusted to the window height.

The date and day are displayed in a smaller font, with a contrasting color for readability.


Loop and Update

The clock updates every second using the after() method of Tkinter, ensuring the time is always current.

