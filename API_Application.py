import requests
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageOps
import io


class StartFrame:
    def __init__(self, master, on_get_started, on_instructions):
        self.master = master
        self.master.title("The Pokemon Pokedex - Home Page")
        self.master.geometry("500x200")
        self.master.resizable(False, False)  # Disable resizing of the window
        self.master.configure(bg="#FFFFFF")  # Set background color

        # Get screen width and height
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        # Calculate the x and y coordinates to center the window
        x_coordinate = (screen_width - 500) // 2
        y_coordinate = (screen_height - 200) // 2

        self.master.geometry(f"500x200+{x_coordinate}+{y_coordinate}")

        # Load the image using PIL
        image = Image.open("assets/background.jpg")  # Replace with the actual path to your image
        image = image.resize((500, 200), Image.BICUBIC)  # Adjust the size if needed
        self.photo = ImageTk.PhotoImage(image)

        # Create a label to display the image
        self.image_label = tk.Label(self.master, image=self.photo)
        self.image_label.place(x=0, y=0, relwidth=1, relheight=1)

        label_title_start = tk.Label(self.master, text="Welcome to the Pokemon Pokedex!", font=("Arial", 18, "bold"), bg="#FFE5E5") 
        label_title_start.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        button_get_started = tk.Button(self.master, text="Get Started", command=on_get_started, font=("Arial", 16), bg="#FFE5E5", fg="BLACK", activebackground="#65e7ff", activeforeground="BLACK", highlightthickness=2, highlightbackground="#05d7ff", highlightcolor="WHITE", cursor='hand1')
        button_get_started.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        button_instructions = tk.Button(self.master, text="Instructions", command=on_instructions, font=("Arial", 16), bg="#FFE5E5", fg="BLACK", activebackground="#65e7ff", activeforeground="BLACK", highlightthickness=2, highlightbackground="#05d7ff", highlightcolor="WHITE", cursor='hand1')
        button_instructions.place(relx=0.5, rely=0.7, anchor=tk.CENTER)


class PokemonApp:
    def __init__(self, master, back_to_start_frame):
        self.master = master
        self.master.title("The Pokemon Pokedex App")
        self.master.geometry("500x600")
        self.master.resizable(False, False)  # Disable resizing of the window

        # Get screen width and height
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        # Calculate the x and y coordinates to center the window
        x_coordinate = (screen_width - 500) // 2
        y_coordinate = (screen_height - 600) // 2

        self.master.geometry(f"500x600+{x_coordinate}+{y_coordinate}")

        # Load the image using PIL
        background_image = Image.open("assets/background.jpg")  # Replace with the actual path to your image
        background_image = background_image.resize((500, 600), Image.BICUBIC)  # Adjust the size if needed
        self.background_photo = ImageTk.PhotoImage(background_image)

        # Create a label to display the background image
        background_label = tk.Label(self.master, image=self.background_photo)
        background_label.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.label_title = tk.Label(self.master, text="The Pokemon Pokedex", font=("Arial", 18, "bold"), bg="#FFE5E5")
        self.label_title.place(relx=0.5, y=10, anchor=tk.CENTER)

        self.pokemon_data = None

        self.label_input = tk.Label(self.master, text="Type Pokemon Name or ID:", font=("Arial", 14), bg="#FFE5E5")
        self.label_input.pack(pady=(30, 10), anchor=tk.CENTER)

        self.entry_pokemon = tk.Entry(self.master, width=25, font=("Arial", 12))
        self.entry_pokemon.pack(pady=10, anchor=tk.CENTER)

        self.label_name = tk.Label(self.master, text="Name:", font=("Arial", 14), bg="#FFE5E5")
        self.label_name.pack(pady=5, anchor=tk.CENTER)

        self.label_id = tk.Label(self.master, text="ID:", font=("Arial", 14), bg="#FFE5E5")
        self.label_id.pack(pady=5, anchor=tk.CENTER)

        self.label_type = tk.Label(self.master, text="Type:", font=("Arial", 14), bg="#FFE5E5")
        self.label_type.pack(pady=5, anchor=tk.CENTER)

        self.label_ability = tk.Label(self.master, text="Abilities:", font=("Arial", 14), bg="#FFE5E5")
        self.label_ability.pack(pady=5, anchor=tk.CENTER)

        self.label_height = tk.Label(self.master, text="Height:", font=("Arial", 14), bg="#FFE5E5")
        self.label_height.pack(pady=5, anchor=tk.CENTER)

        self.label_weight = tk.Label(self.master, text="Weight:", font=("Arial", 14), bg="#FFE5E5")
        self.label_weight.pack(pady=5, anchor=tk.CENTER)

        self.button_get_info = tk.Button(self.master, text="Get Pokemon Info", command=self.get_pokemon_info, font=("Helvetica", 12), bg="#FFE5E5", cursor='hand1')
        self.button_get_info.pack(pady=10, anchor=tk.CENTER)

        self.button_display_image = tk.Button(self.master, text="Display Image", command=self.display_image, font=("Helvetica", 12), bg="#FFE5E5", cursor='hand1')
        self.button_display_image.pack(pady=10, anchor=tk.CENTER)

        self.button_reset = tk.Button(self.master, text="Reset", command=self.reset, font=("Helvetica", 12), bg="#FFE5E5", cursor='hand1')
        self.button_reset.pack(pady=10, anchor=tk.CENTER)

        self.button_exit = tk.Button(self.master, text="Exit", command=self.master.destroy, font=("Helvetica", 12), bg="#FFE5E5", cursor='hand1')
        self.button_exit.pack(pady=10, anchor=tk.CENTER)

        # Load the back button image
        back_button_image = Image.open("assets/return.png")  # Replace with the actual path to your back button image
        back_button_image = back_button_image.resize((50, 50), Image.BICUBIC)  # Adjust the size if needed
        self.back_button_photo = ImageTk.PhotoImage(back_button_image)

        # Back button to return to the start frame
        self.button_back = tk.Button(self.master, image=self.back_button_photo, command=back_to_start_frame,
                                     highlightthickness=0, bd=0, bg="#FFE5E5", cursor='hand1')
        self.button_back.place(relx=0.05, rely=0.05, anchor=tk.CENTER)

        self.widgets_packed = False  # Set the flag to False initially

    def get_pokemon_info(self):
        pokemon_name = self.entry_pokemon.get().lower()

        if not pokemon_name:
            messagebox.showwarning("Warning", "Please enter a Pokemon name or ID.")
            return

        try:
            response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
            response.raise_for_status()
            self.pokemon_data = response.json()

            self.label_name["text"] = f"Name: {self.pokemon_data['name'].capitalize()}"
            self.label_id["text"] = f"ID: {self.pokemon_data['id']}"  # Display Pokemon ID

            # Update labels for additional information
            abilities = [ability['ability']['name'] for ability in self.pokemon_data['abilities']]
            abilities_text = f"Abilities: {', '.join(abilities)}"
            self.label_ability["text"] = abilities_text

            height_dm = self.pokemon_data['height']
            weight_hg = self.pokemon_data['weight']

            # Convert height to cm and weight to kg
            height_cm = height_dm * 10
            weight_kg = weight_hg / 10

            height = f"Height: {height_cm} cm"
            weight = f"Weight: {weight_kg} kg"

            self.label_height["text"] = height
            self.label_weight["text"] = weight

            self.label_type["text"] = f"Type: {', '.join([t['type']['name'] for t in self.pokemon_data['types']])}"

        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Failed to get Pokemon info: {e}")

    def display_image(self):
        if self.pokemon_data:
            image_url = self.pokemon_data["sprites"]["front_default"]
            image_response = requests.get(image_url)
            image_response.raise_for_status()

            # Create a new window for displaying the resized image
            new_window = tk.Toplevel(self.master)
            new_window.title("Pokemon Image")
            new_window.geometry("400x400")

            # Open the image using PIL
            image = Image.open(io.BytesIO(image_response.content))

            # Resize the image to fit the window
            resized_image = self.resize_image(image, (400, 400))
            resized_image_tk = ImageTk.PhotoImage(resized_image)

            # Create a label for displaying the resized image
            self.larger_image_label = tk.Label(new_window, image=resized_image_tk)
            self.larger_image_label.image = resized_image_tk
            self.larger_image_label.pack(pady=20, anchor=tk.CENTER)

    def resize_image(self, image, size):
        # Resize the image while maintaining its aspect ratio
        aspect_ratio = image.width / image.height
        new_width = int(size[0])
        new_height = int(size[0] / aspect_ratio)

        # Resize the image and return
        return image.resize((new_width, new_height), Image.BICUBIC)

    def reset(self):
        # Reset details of the Pokemon
        self.label_name["text"] = "Name:"
        self.label_type["text"] = "Type:"
        self.label_ability["text"] = "Abilities:"
        self.label_height["text"] = "Height:"
        self.label_weight["text"] = "Weight:"
        self.label_id["text"] = "ID:"
        self.entry_pokemon.delete(0, tk.END)

        # Clear the Pokemon data
        self.pokemon_data = None

        # Pack labels and entry widget only if they are not already packed
        if not self.widgets_packed:
            self.label_name.pack(pady=5, anchor=tk.CENTER)
            self.label_type.pack(pady=5, anchor=tk.CENTER)
            self.label_id.pack(pady=5, anchor=tk.CENTER)
            self.entry_pokemon.pack(pady=10, anchor=tk.CENTER)
            self.widgets_packed = True  # Update the flag

        # Destroy image labels in the new window (if any)
        new_window_children = self.master.winfo_children()
        for widget in new_window_children:
            if isinstance(widget, tk.Toplevel):
                widget.destroy()


def on_get_started():
    start_frame.master.withdraw()
    main_window = tk.Toplevel(start_frame.master)
    app = PokemonApp(main_window, back_to_start_frame=lambda: back_to_start_frame(main_window))

def on_instructions():
    messagebox.showinfo("Instructions", "1. Enter a Pokemon name or ID in the input field.\n"
                                        "2. Click 'Get Pokemon Info' to retrieve information.\n"
                                        "3. Click 'Display Image' to show the Pokemon's image.\n"
                                        "4. Click 'Reset' to clear the input and labels.\n"
                                        "5. Click 'Exit' to close the application.")


def back_to_start_frame(main_window):
    main_window.destroy()
    start_frame.master.deiconify()

root = tk.Tk()
start_frame = StartFrame(root, on_get_started, on_instructions)
root.mainloop()
