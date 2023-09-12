import tkinter as tk


def calculate_rent():
    Amount = int(entry_amount.get())
    Days = int(entry_days.get())

    Rent_in_Advance = round((Amount * 12 / 365) * Days, 2)

    if Days > 31:
        extra_days = Days - 30
        extra_rent = round((Amount * 12 / 365) * extra_days, 2)
    else:
        extra_days = 0
        extra_rent = 0.0

    Holding_Deposit = round((Amount * 12 / 52), 2)
    security_deposit = round((Amount * 12 / 52) * 5, 2)

    Total = round(Rent_in_Advance + security_deposit, 2)
    Amended_Total_Rent = round(Total - Holding_Deposit, 2)

    if Days > 31:
        total_rent_in_advance = round(Amount + extra_rent, 2)
        result_label_total_rent_in_advance.config(
            text=f"Total Rent in Advance is {total_rent_in_advance}")
        Total = round(total_rent_in_advance + security_deposit, 2)
    else:
        Total = round(Rent_in_Advance + security_deposit, 2)

    result_label_security_deposit.config(
        text=f"Security Deposit is {security_deposit}")
    result_label_total_rent_in_advance.config(
        text=f"Rent in Advance is {Rent_in_Advance}")
    result_label_total.config(text=f"Total Rent is {Total}")
    result_label_holding_deposit.config(
        text=f"Holding Deposit is {Holding_Deposit}")
    result_label_Amended_Total_Rent.config(
        text=f"Amended Total Rent is {Amended_Total_Rent}")


# Create a Tkinter window
window = tk.Tk()
window.title("Rent Calculator")

# Create labels, entry widgets, and a calculate button
label_amount = tk.Label(window, text="Enter Rent:")
label_days = tk.Label(window, text="Enter Days:")
entry_amount = tk.Entry(window)
entry_days = tk.Entry(window)
calculate_button = tk.Button(window, text="Calculate", command=calculate_rent)
result_label_total_rent_in_advance = tk.Label(
    window, text=" Rent in Advance is:")
result_label_total = tk.Label(window, text="Total Rent is:")
result_label_security_deposit = tk.Label(window, text="Security Deposit is:")
result_label_holding_deposit = tk.Label(window, text="Holding Deposit is:")
result_label_Amended_Total_Rent = tk.Label(
    window, text="Amended Total Rent is:")

# Function to trigger the "Calculate" button when Enter key is pressed


def on_enter_pressed(event):
    calculate_button.invoke()


# Place widgets on the window
label_amount.grid(row=0, column=0)
entry_amount.grid(row=0, column=1)
label_days.grid(row=1, column=0)
entry_days.grid(row=1, column=1)
result_label_Amended_Total_Rent.grid(row=7, column=0, columnspan=2)
calculate_button.grid(row=2, columnspan=2)
result_label_total_rent_in_advance.grid(row=3, column=0, columnspan=2)
result_label_total.grid(row=4, column=0, columnspan=2)
result_label_security_deposit.grid(row=5, column=0, columnspan=2)
result_label_holding_deposit.grid(row=6, column=0, columnspan=2)

window.geometry("400x300")

# Bind the Enter key event to the "Calculate" button
window.bind('<Return>', on_enter_pressed)
# Start the Tkinter main loop
window.mainloop()
