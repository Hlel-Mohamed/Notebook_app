from tkinter.constants import LEFT, RIGHT
from tkinter.ttk import Notebook

from customtkinter import CTkTextbox, set_appearance_mode, set_default_color_theme, CTk, CTkButton, CTkFrame


def add_new_tab():
    new_tab = CTkFrame(notebook)
    notebook.add(new_tab, text=f'Notebook Tab {notebook.index("end") + 1}')
    notebook.select(new_tab)
    text_widget = CTkTextbox(new_tab)
    text_widget.pack(expand=True, fill="both")


def delete_tab():
    notebook.forget(notebook.select())
    count = 0
    for tab in notebook.tabs():
        count += 1
        notebook.tab(tab, text=f'Notebook Tab {count}')


set_appearance_mode("dark")
set_default_color_theme("dark-blue")

root = CTk()

root.geometry("500x400")
root.title("Unit Converter App")
root.resizable(False, False)

frame = CTkFrame(master=root)
frame.pack(padx=20, pady=20, fill="both", expand=True)

buttons_frame = CTkFrame(master=frame, height=20)
buttons_frame.pack(fill="both")

add_button = CTkButton(master=buttons_frame, text="Add Tab", command=add_new_tab)
add_button.pack(padx=40, pady=10, side=LEFT)

delete_button = CTkButton(master=buttons_frame, text="Delete Tab", command=delete_tab)
delete_button.pack(padx=40, pady=10, side=RIGHT)

notebook = Notebook(master=frame)
tab1 = CTkFrame(notebook)
tab2 = CTkFrame(notebook)
notebook.add(tab1, text='Notebook Tab 1')
notebook.add(tab2, text='Notebook Tab 2')
notebook.pack(expand=True, fill="both")

text_widget_t1 = CTkTextbox(master=tab1)
text_widget_t1.pack(expand=True, fill="both")
text_widget_t2 = CTkTextbox(master=tab2)
text_widget_t2.pack(expand=True, fill="both")

root.mainloop()
