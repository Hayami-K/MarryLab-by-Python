import tkinter as tk
from tkinter import filedialog

from marrylab.config_manager import ConfigManager
from marrylab.csv_manager import CSVManager

class Application:
    def __init__(self):
        self.config_path = None
    def run(self):
        self.select_config_file()
        self.load_data()
        self.match_students()
        self.export_results()

    def select_config_file(self):
        root = tk.Tk()
        root.withdraw()

        self.config_path = filedialog.askopenfilename(
            title="Select the configuration file",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )

        if self.config_path:
            print("Config file selected:")
        else:
            print("No config file selected")
            return
    
    def load_data(self):
        self.config_manager = ConfigManager(self)
        self.csv_manager = CSVManager(self)
    def match_students(self):
        pass

    def export_results(self):
        pass

if __name__ == "__main__":
    app = Application()
    app.run()
