import tkinter as tk
from tkinter import ttk

class SchoolsWindow:
    def __init__(self, root, controller):
        """
        Initialize the Schools window.
        :param root: The main tkinter root or parent.
        :param controller: A reference to the main application controller.
        """
        self.root = root
        self.controller = controller

        # Create the Toplevel window for Schools
        self.window = tk.Toplevel(self.root)
        self.window.title("Schools")
        self.window.geometry("300x200")
        self.window.withdraw()  # Start hidden

        # Add widgets to the Schools window
        self._build_widgets()

    def _build_widgets(self):
        """Create widgets for the Schools window."""
        ttk.Label(self.window, text="Welcome to the Schools window.").pack(pady=10)
        ttk.Button(self.window, text="Close", command=self.hide_window).pack(pady=10)
        ttk.Button(self.window, text="Go Back to Main", command=self.controller.hide_all_windows).pack(pady=10)

    def show_window(self):
        """Show the Schools window and hide all others."""
        self.controller.hide_all_windows()  # Collapse other windows
        self.window.deiconify()

    def hide_window(self):
        """Hide the Schools window."""
        self.window.withdraw()