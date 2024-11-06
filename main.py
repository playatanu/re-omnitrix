from customtkinter import *
import customtkinter as tk
from tkinter import filedialog
from PIL import Image
import pygame

from helper import make_rounded_image, resource_path
from model import predict

OMNITRIX_IMAGE_PATH = 'assets/images/omnitrix.png'
OMNITRIX_LOAD_SOUND = 'assets/sounds/omnitrix-load.mp3'
OMNITRIX_LOAD_END_SOUND = 'assets/sounds/omnitrix-load-end.mp3'

pygame.mixer.init()

tk.set_appearance_mode('system')
tk.set_default_color_theme('./themes/ben10_theme.json')

app = tk.CTk()
app.geometry("350x500")
app.title('RE Omnitrix')

app.iconbitmap("assets/images/omnitrix.ico")

app.grid_propagate(True)

frame = CTkFrame(app)
frame.pack(expand=True)

app.configure(fg_color="black") 
frame.configure(fg_color="black")


# Omnitrix 
omnitrix_image = CTkImage(light_image= Image.open(resource_path(OMNITRIX_IMAGE_PATH)).resize((300,300)), size=(300,300))

omnitrix_image_bar = CTkFrame(frame, fg_color="black", height=350)
omnitrix_image_bar.grid(row=0, column=0, pady=10)

omnitrix_image_label = CTkLabel(omnitrix_image_bar, text="",  image=omnitrix_image,  width=300, height=300)
omnitrix_image_label.pack(pady=20, padx=20)

omnitrix_image_text = CTkLabel(omnitrix_image_bar,text="Omnitrix", font=("Helvetica", 18, "bold"),)
omnitrix_image_text.pack()

# Bottom Bar Start
bottom_bar = CTkFrame(frame, fg_color="black", height=100)

clear_button = CTkButton(bottom_bar, text="CLEAR", font=("Arial", 12, "bold"), fg_color= "#BCC0BE", hover="#BCC0BE", text_color= "#000000")
clear_button.pack(side="left", padx=10)

submit_button = CTkButton(bottom_bar, text="SUBMIT", font=("Arial", 12, "bold"), fg_color= "#8BE308", hover="#619e05", text_color= "#000000")
submit_button.pack(side="right", padx=10)
# Buttom Bar End


################################### Functions

def upload_image():
    play_sound(resource_path(OMNITRIX_LOAD_SOUND))
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    
    if file_path:
        image = make_rounded_image(file_path)
        result = predict(image)
 
        img_tk = CTkImage(image, size=(300,300))
        
        omnitrix_image_text.configure(text=result.upper())

        omnitrix_image_label.configure(image=img_tk)
        omnitrix_image_label.image = img_tk
            
        # bottom_bar.pack(side="bottom", fill="x", padx=20, pady=20)  
        bottom_bar.grid(row=1, column=0, pady=10)
        play_sound(resource_path(OMNITRIX_LOAD_END_SOUND))
        
def on_image_label_click(event):
        upload_image() 
    
def on_clear_click():
    bottom_bar.grid_forget()
    omnitrix_image_label.configure(image=omnitrix_image)
    omnitrix_image_text.configure(text='Omnitrix')
       
def on_submit_click():
    upload_image()

def play_sound(sound):
    sound = pygame.mixer.Sound(sound)
    sound.play()
          
omnitrix_image_label.bind("<Button-1>", on_image_label_click)
submit_button.configure(command=on_submit_click)
clear_button.configure(command=on_clear_click)

app.mainloop()