import tkinter as tk
from tkinter import messagebox

# Initialize Tkinter
root = tk.Tk()
root.title("Codex Bank App")

# Create frames for each screen
login_frame = tk.Frame(root)
signup_frame = tk.Frame(root)
bank_frame = tk.Frame(root)

# Declare balance as a global variable
balance = 0

# Function to raise a frame to the top
def raise_frame(frame):
    frame.tkraise()

username = ''

# Login Functionality
def login():
    global username
    global balance  
    username = username_entry.get()
    password = password_entry.get()

    # Check if user exists in user_info.txt
    with open('user_info.txt', 'r') as file:
        users = file.readlines()
        for user in users:
            user_info = user.split(',')
            if user_info[0] == username and user_info[1].strip() == password:
                if len(user_info) > 2:  # Check if balance exists
                    balance = int(user_info[2])  # Update balance from user_info.txt
                else:
                    balance = 0  # Set balance to 0 if it doesn't exist
                balance_label.config(text=f"Balance: ${balance}")  # Update balance label
                raise_frame(bank_frame)
                return

    messagebox.showerror("Error", "Invalid username or password")

# Function to handle signup
def signup():
    username = new_username_entry.get()
    password = new_password_entry.get()

    # Save new user to user_info.txt
    with open('user_info.txt', 'a') as file:
        file.write(f"{username},{password},0\n")  # Initialize balance to 0
    raise_frame(login_frame)

# Function to handle forgot password
def forgot_password():
    username = username_entry.get()

    # Check if user exists in user_info.txt
    with open('user_info.txt', 'r') as file:
        users = file.readlines()
        for user in users:
            user_info = user.split(',')
            if user_info[0] == username:
                messagebox.showinfo("Password", f"Your password is {user_info[1].strip()}")
                return

    messagebox.showerror("Error", "Invalid username")

# Function to handle password reset
# def reset_password():
#     username = username_entry.get()
#     new_password = new_password_entry.get()

#     # Check if user exists in user_info.txt
#     with open('user_info.txt', 'r') as file:
#         users = file.readlines()
#     with open('user_info.txt', 'w') as file:
#         for user in users:
#             user_info = user.split(',')
#             if user_info[0] == username:
#                 file.write(f"{username},{new_password},{user_info[2]}")
#             else:
#                 file.write(user)

#     messagebox.showinfo("Success", "Your password has been reset")

# Function to handle deposit
def deposit():
    global username
    global balance  # Use the global balance variable
    amount = int(deposit_entry.get())
    balance += amount
    balance_label.config(text=f"Balance: ${balance}")  # Update balance label
    with open('transaction_log.txt', 'a') as file:
        file.write(f"{username} deposited ${amount}\n")

# Function to handle withdrawal
def withdraw():
    global balance  # Use the global balance variable
    amount = int(withdraw_entry.get())
    if amount > balance:
        messagebox.showerror("Error", "Insufficient funds")
    else:
        balance -= amount
        balance_label.config(text=f"Balance: ${balance}")  # Update balance label
        with open('transaction_log.txt', 'a') as file:
            file.write(f"{username} withdrew ${amount}\n")

# Function to handle signup
def signup():
    username = new_username_entry.get()
    password = new_password_entry.get()

    # Save new user to user_info.txt
    with open('user_info.txt', 'a') as file:
        file.write(f"{username},{password}\n")

    raise_frame(login_frame)

# Function to handle logout
def logout():
    global username  # Use the global username variable
    global balance  # Use the global balance variable

    # Update balance in user_info.txt
    with open('user_info.txt', 'r') as file:
        users = file.readlines()
    with open('user_info.txt', 'w') as file:
        for user in users:
            user_info = user.split(',')
            if user_info[0] == username:
                file.write(f"{username},{user_info[1].strip()},{balance}\n")
            else:
                file.write(user)

    raise_frame(login_frame)

# Login screen
username_label = tk.Label(login_frame, text="Username")
username_entry = tk.Entry(login_frame)
password_label = tk.Label(login_frame, text="Password")
password_entry = tk.Entry(login_frame, show="*")
login_button = tk.Button(login_frame, text="Login", command=login)
signup_button = tk.Button(login_frame, text="Signup", command=lambda: raise_frame(signup_frame))

# Login screen
# new_password_label = tk.Label(login_frame, text="New Password")
# new_password_entry = tk.Entry(login_frame, show="*")
# reset_password_button = tk.Button(login_frame, text="Reset Password", command=reset_password)

# new_password_label.pack()
# new_password_entry.pack()
# reset_password_button.pack()

username_label.pack()
username_entry.pack()
password_label.pack()
password_entry.pack()
login_button.pack()
signup_button.pack()

forgot_password_button = tk.Button(login_frame, text="Forgot Password", command=forgot_password)
forgot_password_button.pack()

# Signup screen
new_username_label = tk.Label(signup_frame, text="New Username")
new_username_entry = tk.Entry(signup_frame)
new_password_label = tk.Label(signup_frame, text="New Password")
new_password_entry = tk.Entry(signup_frame, show="*")
create_account_button = tk.Button(signup_frame, text="Create Account", command=signup)

new_username_label.pack()
new_username_entry.pack()
new_password_label.pack()
new_password_entry.pack()
create_account_button.pack()

# Bank screen
welcome_label = tk.Label(bank_frame, text="Welcome to Codex Bank!")
balance_label = tk.Label(bank_frame, text="Balance: $0")  # Display the user's balance
deposit_entry = tk.Entry(bank_frame)  # Entry field for deposit amount
withdraw_entry = tk.Entry(bank_frame)  # Entry field for withdrawal amount
deposit_button = tk.Button(bank_frame, text="Deposit", command=deposit)  # Button to deposit money
withdraw_button = tk.Button(bank_frame, text="Withdraw", command=withdraw)  # Button to withdraw money
logout_button = tk.Button(bank_frame, text="Logout", command=logout)

welcome_label.pack()
balance_label.pack()
deposit_entry.pack()
deposit_button.pack()
withdraw_entry.pack()
withdraw_button.pack()
logout_button.pack()

# Add frames to window
for frame in (login_frame, signup_frame, bank_frame):
    frame.grid(row=0, column=0, sticky='news')

# Start on login screen
raise_frame(login_frame)

root.mainloop()
