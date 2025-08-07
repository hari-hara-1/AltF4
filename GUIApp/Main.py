import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox
from entry import CreditScoringApp

class BaseWindow(tb.Window):
    def __init__(self, title="App", size="400x300", theme="flatly"):
        super().__init__(title=title, themename=theme)
        self.geometry(size)
        self.resizable(False, False)


class LoginPage(BaseWindow):
    def __init__(self):
        super().__init__(title="Login Page", size="400x280")
        self.create_widgets()

    def create_widgets(self):
        # Title
        title = tb.Label(self, text="Welcome!", font=("Segoe UI", 16, "bold"))
        title.pack(pady=(20, 10))

        # Username
        tb.Label(self, text="Username:", font=("Segoe UI", 11)).pack(pady=(10, 2))
        self.username_entry = tb.Entry(self, width=30)
        self.username_entry.pack()

        # Password
        tb.Label(self, text="Password:", font=("Segoe UI", 11)).pack(pady=(10, 2))
        self.password_entry = tb.Entry(self, width=30, show="*")
        self.password_entry.pack()

        # Show Password Toggle
        self.show_password = tb.BooleanVar()
        toggle = tb.Checkbutton(
            self,
            text="Show Password",
            variable=self.show_password,
            command=self.toggle_password,
            bootstyle="secondary-toolbutton"
        )
        toggle.pack(pady=(5, 10))

        # Login Button
        login_btn = tb.Button(self, text="Login", width=20, command=self.login, bootstyle=PRIMARY)
        login_btn.pack(pady=(10, 20))

    def toggle_password(self):
        if self.show_password.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    def login(self):
        user = self.username_entry.get()
        pw = self.password_entry.get()
        if user == "admin" and pw == "password":
            messagebox.showinfo("Success", f"Welcome, {user}!")
            self.cApp = CreditScoringApp()
            self.cApp.mainloop()
        else:
            messagebox.showerror("Error", "Invalid username or password.")


if __name__ == "__main__":
    app = LoginPage()
    app.mainloop()
