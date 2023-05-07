import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import requests


def generate():
    
    url=f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={username_entry}"
    r=requests.get(url)
    with open("image.jpg", "wb") as f:
        f.write(r.content)
        print("!!!   Successfully Generated   !!!")
    photo = PhotoImage(file="image.jpg")
    image_label = tk.Label(image=photo)
    image_label.pack(pady=20)

    img = Image.open("G:/Python/Practice/image.jpg")
    # pixels = img.load() 
    img.show()

    


# Create a new tkinter window
window = Tk()
window.geometry("400x400")
window.title=("QR Generator")
window.config(bg="#856ff8")
# Create username label and entry widget
username_label = tk.Label(window, text="Enter The URL : ",bg="#856ff8",fg="White",font= ('Sans Serif', 15, 'italic bold'))
username_entry = tk.Text(window,height=1.25,width=40,font= ('Sans Serif', 10, 'italic bold'))



# Create login button
login_button = tk.Button(window, text="Generate",command=generate,activebackground="#7F7FFF",bg="#7676EE",fg="White",font= ('Sans Serif', 10, 'bold'))



# Pack the widgets onto the window
username_label.pack(pady=20)
username_entry.pack(pady=20)
login_button.pack()
# Run the main event loop
window.mainloop()