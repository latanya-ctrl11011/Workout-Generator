from tkinter import *
from PIL import Image, ImageTk

# create Tkinter window
root = Tk()
root.geometry('925x500')
root.configure(bg='pink')

# open image file
image_file = Image.open("runnersHigh.png")

# resize image
resized_image = image_file.resize((300, 300), Image.ANTIALIAS)

# convert image to Tkinter PhotoImage
tk_image = ImageTk.PhotoImage(resized_image)

# create label with image
label = Label(root, image=tk_image, anchor="w", bg='pink')
label.pack(side=LEFT, fill=Y)

canvas = Canvas(root, width=300, height=300, bg="white")
canvas.pack(side=RIGHT, fill=Y)

username_label = Label(canvas, text="Username:", bg="white")
username_label.pack()
canvas.create_window(100, 50, window=username_label)

# create Entry widget for username
username_entry = Entry(canvas)
username_entry.pack()
canvas.create_window(100, 80, window=username_entry)

# create Label widget for password
password_label = Label(canvas, text="Password:", bg="white")
password_label.pack()
canvas.create_window(100, 110, window=password_label)

# create Entry widget for password
password_entry = Entry(canvas, show="*")
password_entry.pack()
canvas.create_window(100, 140, window=password_entry)

# signin button
signin_button = Button(canvas, text="Sign In", bg="white")
signin_button.pack()
canvas.create_window(100, 170, window=signin_button)


# check credentials 
def check_login():
    try:
        username = username_entry.get()
        password = password_entry.get()
        if username == "admin" and password == "password":
            # switch to new screen
            canvas.delete("all")
            canvas.create_text(100, 100, text="Welcome, " + username + "!", font=("Helvetica", 18))
    except Exception as e:
        print("An error occurred:", e)


# run Tkinter event loop
root.mainloop()