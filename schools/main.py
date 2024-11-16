import tkinter as tk
from tkinter import ttk
from schools import SchoolsWindow  # Import the SchoolsWindow class

class MainApp:
    def __init__(self, root):
        """
        Initialize the main application controller.
        :param root: The main tkinter root.
        """
        self.root = root
        self.root.title("Main Application")

        # Dictionary to track all windows
        self.windows = {}

        # Create main window widgets
        ttk.Label(root, text="Main Application").pack(pady=10)
        ttk.Button(root, text="Open Schools Window", command=lambda: self.show_window("Schools")).pack(pady=10)
        ttk.Button(root, text="Close All", command=self.hide_all_windows).pack(pady=10)

        # Create other windows
        self.create_windows()

    def create_windows(self):
        """Initialize all secondary windows."""
        self.windows["Schools"] = SchoolsWindow(self.root, self)

    def show_window(self, window_name):
        """Show a specific window by name."""
        if window_name in self.windows:
            self.windows[window_name].show_window()

    def hide_all_windows(self):
        """Hide all secondary windows."""
        for window in self.windows.values():
            window.hide_window()

def main():
    """Start the application."""
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()