![digital_clocke](https://github.com/user-attachments/assets/34da19c0-cf73-438c-8500-f8b68b5b212d)


1. Imports:
   - The code imports classes and functions from tkinter, datetime, and PIL libraries. 
   - tkinter is used for creating GUI applications, datetime manages date and time, and PIL (Python Imaging Library) handles image processing.

2.Window Setup: 
   - A Tk instance is created, which serves as the main application window.
   - The window title is set to "Digital Watch - Tehran Time".
   - The geometry of the window is defined as 240x100 pixels.
   - The window's transparency is adjusted to 70% with attributes('-alpha', 0.7), creating a sleek appearance.
   - The window can be resized by the user through resizable(True, True).

3.Background Image:
   - A black background image is created and set to cover the entire window using Label.
   - The background label utilizes ImageTk from PIL for proper image display.

4.Font Settings:
   - A custom font is created using tkFont.Font, specifying "Times New Roman" with a size of 60 for the time display.

5.Time Calculation:
   - The mytime() function calculates Tehran's current time by converting UTC to Tehran time (UTC +3:30).
   - The time is formatted to display hours, minutes, seconds, AM/PM style, day of the week, and date.

6.Dynamic Display Update:
   - The time and date are set to be updated every second (1000 milliseconds) using after(1000, mytime) which recursively calls the mytime function.
   - The font size is dynamically adjusted based on the height of the window with Window.winfo_height().

7. Labels for Time and Date:
   - Two labels (MyLabel and MyLabel2) display the formatted time and date information.
   - These labels are configured with specific text and styles, including font color and background.

8.Main Loop:
   - The Window.mainloop() function starts the event loop, keeping the application running and responsive to user interactions.

Summary:
This code creates a visually appealing digital watch that displays the current time and date in Tehran, complete with a transparent background and dynamic font sizing. The interface updates every second, ensuring users see the accurate current time. Perfect for anyone wanting a stylish digital clock on their screen
