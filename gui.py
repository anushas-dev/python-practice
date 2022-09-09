# More to learn from : https://www.pythontutorial.net/tkinter/
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('500x250')
        self.title('My App')

        # Menubutton variable
        self.selected_msg = tk.StringVar()
        self.selected_msg.trace("w", self.menu_item_selected)

        # create the menu button
        self.create_menu_button()

    def menu_item_selected(self, *args):
        """ handle menu selected event """
        self.config(showinfo(message=self.selected_msg.get()))

    def create_menu_button(self):
        """ create a menu button """
        # menu variable
        messages = ('Good morning!', 'Good afternoon!', 'Good evening!')

        # create the Menubutton
        menu_button = ttk.Menubutton(
            self,
            text='Select a message')

        # create a new menu instance
        menu = tk.Menu(menu_button, tearoff=0)

        for msg in messages:
            menu.add_radiobutton(
                label=msg,
                value=msg,
                variable=self.selected_msg)

        # associate menu with the Menubutton
        menu_button["menu"] = menu

        menu_button.pack(expand=True)


if __name__ == "__main__":
    app = App()
    app.mainloop()