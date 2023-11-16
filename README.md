# script-gui
A simple GUI for running routine python scripts


main.py can be edited to change button labels. More functions can be created quickly to expand the number of scripts that can be used from the GUI.

To do this, add a new definition for a script, such as:
def run_script_4():
  print("running [script name]"
  
Note: also make sure to add a button for the new script to the def main(), ex:
def main():
script_4_button = tk.Button(root, text="Run [script name]", command=run_script_3)
    script_3_button.pack(pady=10)
