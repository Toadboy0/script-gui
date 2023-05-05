#GUI for running automation scripts using tkinter
import tkinter as tk
#Define the functions for each script
def run_script_1():
    print("Running [script name]")
    # Add the script to be run here

def run_script_2():
    print("Running [script name]")
    # Add the script to be run here

def run_script_3():
    print("Running Script 3")
    # Add the script to be run here

def main():
    # Generate the GUI
    root = tk.Tk()
    root.title("Automation Scripts Runner")

    # Create buttons for each script
    script_1_button = tk.Button(root, text="Run [script name]", command=run_script_1)
    script_1_button.pack(pady=10)

    script_2_button = tk.Button(root, text="Run [script name]", command=run_script_2)
    script_2_button.pack(pady=10)

    script_3_button = tk.Button(root, text="Run [script name]", command=run_script_3)
    script_3_button.pack(pady=10)

    # Quit the application
    quit_button = tk.Button(root, text="Quit", command=root.quit)
    quit_button.pack(pady=10)

    # initialize the main loop
    root.mainloop()

if __name__ == "__main__":
    main()
