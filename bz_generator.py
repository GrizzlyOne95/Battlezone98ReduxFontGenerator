import os
import sys
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont

# --- PYINSTALLER PATH HELPER ---
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def draw_custom_caret(draw, x, y, w, h, color=(255, 255, 255)):
    padding_x = w * 0.25
    top_y = y + (h * 0.3)
    bottom_y = y + (h * 0.6)
    left_x = x + padding_x
    right_x = x + w - padding_x
    mid_x = x + (w / 2)
    draw.line([(left_x, bottom_y), (mid_x, top_y)], fill=color, width=4)
    draw.line([(mid_x, top_y), (right_x, bottom_y)], fill=color, width=4)

def generate_bzone(letter_font_path, fallback_font_path):
    width, height = 1024, 1024
    output_dir = os.path.dirname(sys.executable if getattr(sys, 'frozen', False) else __file__)
    output_sheet = os.path.join(output_dir, "bzone.png") # UPDATED FILENAME
    
    new_img = Image.new("RGBA", (width, height), (0, 0, 0, 255))
    draw = ImageDraw.Draw(new_img)
    font_size = 55  
    
    row1_y, row2_y = 13, 93
    row3_upper_y, row3_lower_y = 173, 187
    row4_alpha_y, row4_symbol_y = 266, 254 

    manual_data = {
        "!": (28, 16, 62), "\"": (43, 35, 62), "#": (80, 41, 62), "$": (128, 41, 62),
        "%": (176, 41, 62), "&": (225, 41, 62), "'": (270, 23, 62), "(": (295, 32, 62),
        ")": (322, 32, 62), "*": (358, 45, 62), "+": (405, 45, 62), ",": (452, 25, 62),
        "-": (482, 34, 62), ".": (525, 13, 62), "/": (543, 42, 62), "0": (591, 42, 62),
        "1": (638, 42, 62), "2": (685, 42, 62), "3": (734, 42, 62), "4": (783, 42, 62),
        "5": (832, 42, 62), "6": (877, 42, 62), "7": (931, 42, 62), "8": (975, 42, 62),
        "9": (0, 42, 62), ":": (43, 17, 62), ";": (60, 17, 62), "<": (79, 27, 62),
        "=": (108, 48, 62), ">": (157, 32, 62), "?": (188, 48, 61), "@": (239, 48, 61),
        "A": (284, 48, 61), "B": (332, 48, 61), "C": (380, 48, 61), "D": (427, 48, 61),
        "E": (477, 48, 61), "F": (523, 48, 61), "G": (572, 48, 61), "H": (620, 48, 61),
        "I": (665, 23, 61), "J": (686, 47, 61), "K": (734, 47, 61), "L": (779, 47, 61),
        "M": (829, 47, 61), "N": (878, 47, 61), "O": (926, 47, 61), "P": (972, 47, 61),
        "Q": (0, 47, 61), "R": (44, 47, 61), "S": (93, 47, 61), "T": (141, 47, 61),
        "U": (187, 47, 61), "V": (236, 47, 61), "W": (285, 47, 61), "X": (333, 47, 61),
        "Y": (381, 47, 61), "Z": (428, 47, 61), "[": (477, 31, 61), "\\": (511, 42, 61),
        "]": (558, 28, 61), "^": (592, 41, 61), "_": (639, 48, 61), "`": (688, 21, 61),
        "a": (709, 46, 49), "b": (756, 46, 49), "c": (807, 46, 49), "d": (854, 46, 49),
        "e": (902, 46, 49), "f": (949, 46, 49),
        "g": (0, 46, 49), "h": (46, 46, 49), "i": (92, 17, 49), "j": (110, 44, 49),
        "k": (160, 44, 49), "l": (207, 44, 49), "m": (254, 44, 49), "n": (300, 44, 49),
        "o": (350, 44, 49), "p": (397, 44, 49), "q": (446, 44, 49), "r": (493, 44, 49),
        "s": (542, 44, 49), "t": (590, 44, 49), "u": (640, 44, 49), "v": (685, 44, 49),
        "w": (734, 44, 49), "x": (781, 44, 49), "y": (831, 44, 49), "z": (878, 44, 49),
        "{": (927, 29, 60), "|": (955, 20, 60), "}": (974, 29, 60)
    }
    
    rows_data = ["!\"#$%&'()*+,-./012345678", "9:;<=>?@ABCDEFGHIJKLMNOP", "QRSTUVWXYZ[\\\\]^_abcdef`", "ghijklmnopqrstuvwxyz{|}~"]

    for r_idx, row_text in enumerate(rows_data):
        for char in row_text:
            if char not in manual_data: continue
            
            current_font_path = letter_font_path if char.isalpha() else fallback_font_path
            try: font = ImageFont.truetype(current_font_path, font_size)
            except: font = ImageFont.load_default()

            x, target_w, target_h = manual_data[char]
            
            if r_idx == 0: y = row1_y
            elif r_idx == 1: y = row2_y
            elif r_idx == 2: y = row3_lower_y if char in "abcdef" else row3_upper_y
            else: y = row4_symbol_y if char in "{|}" else row4_alpha_y

            if char == "^":
                draw_custom_caret(draw, x, y, target_w, target_h)
                continue

            bbox = draw.textbbox((0, 0), char, font=font)
            text_w, text_h = bbox[2] - bbox[0], bbox[3] - bbox[1]
            draw_x = x + (target_w - text_w) // 2 - bbox[0]
            
            if char.islower() and char not in "{|}~":
                draw_y = y + target_h - text_h - bbox[1]
            else:
                draw_y = y + (target_h - text_h) // 2 - bbox[1]

            draw.text((draw_x, draw_y), char, fill=(255, 255, 255), font=font)

    new_img.save(output_sheet)
    
    if messagebox.askyesno("Success", f"Sheet 'bzone.png' Generated!\n\nOpen output folder?"):
        if sys.platform == "win32":
            os.startfile(output_dir)
        else:
            subprocess.Popen(["open" if sys.platform == "darwin" else "xdg-open", output_dir])

class BzoneApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Battlezone 98 Redux Font Sheet Generator")
        self.root.geometry("440x450")
        self.root.resizable(False, False)
        
        self.default_f = resource_path("Orbitron-Bold.ttf")
        self.letter_font = self.default_f
        self.symbol_font = self.default_f

        tk.Label(root, text="Battlezone Atlas Generator", font=("Arial", 14, "bold")).pack(pady=15)
        
        # Letter Section
        tk.Label(root, text="Letter Font (A-Z):", font=("Arial", 10, "bold")).pack()
        self.lbl_letter = tk.Label(root, text="Default (Orbitron)", fg="#555")
        self.lbl_letter.pack()
        tk.Button(root, text="Select Font", command=self.set_let, width=15).pack(pady=5)

        # Symbol Section
        tk.Label(root, text="Numbers & Symbols Font:", font=("Arial", 10, "bold")).pack(pady=(15,0))
        self.lbl_sym = tk.Label(root, text="Default (Orbitron)", fg="#555")
        self.lbl_sym.pack()
        tk.Button(root, text="Select Font", command=self.set_sym, width=15).pack(pady=5)

        # Final Run
        tk.Button(root, text="GENERATE BZONE.PNG", bg="#1a73e8", fg="white", font=("Arial", 11, "bold"),
                  height=2, width=25, command=lambda: generate_bzone(self.letter_font, self.symbol_font)).pack(pady=20)

        # About Button
        tk.Button(root, text="About / Credits", font=("Arial", 9), command=self.show_about).pack(pady=10)

    def show_about(self):
        about_text = (
            "Battlezone 98 Redux Font Sheet Generator\n"
            "------------------------------------------\n"
            "This tool generates a 1024x1024 bzone.png atlas \n"
            "compatible with the Redux engine.\n\n"
            "Instructions:\n"
            "1. Select a .ttf or .otf font for letters.\n"
            "2. Select a font for numbers/symbols (or keep Orbitron).\n"
            "3. Click Generate. The file 'bzone.png' will be created\n"
            "   in the same folder as this application.\n"
            "4. Replace the existing bzone.png in your game assets.\n\n"
            "Note: Currently only standard alpha-numeric characters are supported.\n\n"
            "Credits: GrizzlyOne95"
        )
        messagebox.showinfo("About / Instructions", about_text)

    def set_let(self):
        f = filedialog.askopenfilename(filetypes=[("Fonts", "*.ttf *.otf")])
        if f: 
            self.letter_font = f
            self.lbl_letter.config(text=os.path.basename(f), fg="#1a73e8")

    def set_sym(self):
        f = filedialog.askopenfilename(filetypes=[("Fonts", "*.ttf *.otf")])
        if f: 
            self.symbol_font = f
            self.lbl_sym.config(text=os.path.basename(f), fg="#1a73e8")

if __name__ == "__main__":
    root = tk.Tk()
    app = BzoneApp(root)
    root.mainloop()