import tkinter as tk
from tkinter import ttk
import csv
def register_book():
    # Retrieve the input values
    book_name = title_entry.get()
    price = price_entry.get()
    isbn = isbn_entry.get()
    pages = pages_entry.get()
    book_type = type_combobox.get()

    # Add the book information to the treeview
    book_treeview.insert("", "end", values=(book_name, price, isbn, pages, book_type))

    # Add the book information to the list
    book_data.append((book_name, price, isbn, pages, book_type))

    # Clear the input fields
    title_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    isbn_entry.delete(0, tk.END)
    pages_entry.delete(0, tk.END)
    type_combobox.set("")


def save_book_data():
    # Open the CSV file in write mode
    with open("book_data.csv", "w", newline="") as file:
        writer = csv.writer(file)

        # Write the column headings
        writer.writerow(columns)

        # Write each row of book data
        for book in book_data:
            writer.writerow(book)
def delete_book():
    # Get the selected book's ID
    selected_item = book_treeview.selection()[0]
    book_id = book_treeview.index(selected_item)

    # Delete the book from the treeview and book_data list
    book_treeview.delete(selected_item)
    del book_data[book_id]

# Define the column names for the treeview widget
columns = ("Book Name", "Price", "ISBN", "Pages", "Type", "Cover")

# Create an empty list to store the book information
book_data = []

# Create the GUI
root = tk.Tk()
root.title("Book Register")

# Create the input labels and fields
title_label = tk.Label(root, text="Book Name:")
title_label.grid(row=0, column=0, padx=5, pady=5)
title_entry = tk.Entry(root)
title_entry.grid(row=0, column=1, padx=5, pady=5)

price_label = tk.Label(root, text="Price:")
price_label.grid(row=1, column=0, padx=5, pady=5)
price_entry = tk.Entry(root)
price_entry.grid(row=1, column=1, padx=5, pady=5)

isbn_label = tk.Label(root, text="ISBN:")
isbn_label.grid(row=2, column=0, padx=5, pady=5)
isbn_entry = tk.Entry(root)
isbn_entry.grid(row=2, column=1, padx=5, pady=5)

pages_label = tk.Label(root, text="Pages:")
pages_label.grid(row=3, column=0, padx=5, pady=5)
pages_entry = tk.Entry(root)
pages_entry.grid(row=3, column=1, padx=5, pady=5)

type_label = tk.Label(root, text="Type:")
type_label.grid(row=4, column=0, padx=5, pady=5)
type_combobox = ttk.Combobox(root, values=["Business", "Computer", "Physics"])
type_combobox.grid(row=4, column=1, padx=5, pady=5)

cover_label = tk.Label(root, text="Cover:")
cover_label.grid(row=5, column=0, padx=5, pady=5)
cover_var = tk.StringVar()
cover_radiobutton1 = tk.Radiobutton(root, text="Hardcover", variable=cover_var, value="Hardcover")
cover_radiobutton2 = tk.Radiobutton(root, text="Paperback", variable=cover_var, value="Paperback")
cover_radiobutton1.grid(row=5, column=1, padx=5, pady=5)
cover_radiobutton2.grid(row=5, column=2, padx=5, pady=5)

# Create the treeview widget
book_treeview = ttk.Treeview(root, columns=columns, show="headings")

# Set the column headings
for column in columns:
    book_treeview.heading(column, text=column)

# Insert the book data into the treeview
for book in book_data:
    book_treeview.insert("", "end", values=book)

book_treeview.grid(row=6, column=0, columnspan=3, padx=5, pady=5)

# Create the buttons
register_button = tk.Button(root, text="Register", command=lambda: register_book())
register_button.grid(row=7, column=0, padx=5, pady=5)

delete_button = tk.Button(root, text="Delete", command=lambda:delete_book())
delete_button.grid(row=7, column=1, padx=5, pady=5)

save_button = tk.Button(root, text="Save", command=lambda: save_book_data())
save_button.grid(row=7, column=2, padx=5, pady=5)



root.mainloop()