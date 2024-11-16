import tkinter as tk
from tkinter import ttk

class ComposersWindow:
    def __init__(self, root, controller):
        """
        Initialize the Composers window.
        :param root: The main tkinter root or parent.
        :param controller: A reference to the main application controller.
        """
        self.root = root
        self.controller = controller

        # Create the Toplevel window for Composers
        self.window = tk.Toplevel(self.root)
        self.window.title("Composers")
        self.window.geometry("300x200")
        self.window.withdraw()  # Start hidden

        # Add widgets to the Composers window
        self._build_widgets()

    def _build_widgets(self):
        """Create widgets for the Composers window."""
        ttk.Label(self.window, text="Welcome to the Composers window.").pack(pady=10)

        # Add a listbox for displaying composers
        self.composer_list = tk.Listbox(self.window, height=5)
        self.composer_list.pack(pady=10)

        # Add composers to the listbox
        composers = ["Beethoven", "Mozart", "Bach", "Chopin", "Tchaikovsky"]
        for composer in composers:
            self.composer_list.insert(tk.END, composer)

        # Add buttons
        ttk.Button(self.window, text="Close", command=self.hide_window).pack(pady=5)
        ttk.Button(self.window, text="Go Back to Main", command=self.controller.hide_all_windows).pack(pady=5)

    def show_window(self):
        """Show the Composers window and hide all others."""
        self.controller.hide_all_windows()  # Collapse other windows
        self.window.deiconify()

    def hide_window(self):
        """Hide the Composers window."""
        self.window.withdraw()
