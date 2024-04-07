# gui_app.py

import tkinter as tk
from tkinter import scrolledtext
import subprocess

class GUIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Elevate-Chat bot Training")

        self.outputTextBox = scrolledtext.ScrolledText(root, wrap="word", width=40, height=10)
        self.outputTextBox.pack(padx=10, pady=10, fill="both", expand=True)

        self.trainingButton = tk.Button(root, text="Run Script", command=self.runTraining)
        self.trainingButton.pack(pady=5)

    def runTraining(self):
        self.process = subprocess.Popen(["python", "Training.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                        universal_newlines=True)
        self.updateOutput()

    def updateOutput(self):
        try:
            output = self.process.stdout.readline()
            if output:
                self.outputTextBox.insert(tk.END, output)
                self.outputTextBox.see(tk.END)  # Auto-scroll to the end
            if self.process.poll() is None:
                self.root.after(100, self.updateOutput)  # Update every 100 milliseconds
        except Exception as e:
            self.outputTextBox.insert(tk.END, "Error: " + str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = GUIApp(root)
    root.mainloop()
