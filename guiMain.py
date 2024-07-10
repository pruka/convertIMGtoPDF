import tkinter as tk
from tkinter import filedialog, messagebox
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image
import img2pdf

class ImageToPdfConverter(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()
        self.title("Image to PDF Converter")
        self.geometry("600x500")
        
        self.label = tk.Label(self, text="Drag and drop images here", bg="white", relief="solid", width=80, height=20)
        self.label.pack(pady=20)
        
        self.convert_button = tk.Button(self, text="Convert to PDF", command=self.convert_to_pdf, background="#7FFF7F")
        self.convert_button.pack(pady=20)
        
        self.label.bind("<Button-1>", self.browse_files)
        
        self.image_paths = []

        self.drop_target_register(DND_FILES)
        self.dnd_bind('<<Drop>>', self.on_drop)

    def on_drop(self, event):
        files = self.tk.splitlist(event.data)
        for file in files:
            if file.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp')):
                self.image_paths.append(file)
                self.label.config(text=f"{len(self.image_paths)} image(s) added")
            else:
                messagebox.showerror("Error", f"{file} is not a valid image file.")

    def browse_files(self, event):
        file_paths = filedialog.askopenfilenames(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
        self.image_paths.extend(file_paths)
        self.label.config(text=f"{len(self.image_paths)} image(s) added")

    def convert_to_pdf(self):
        if not self.image_paths:
            messagebox.showerror("Error", "No images selected")
            return

        output_pdf_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if not output_pdf_path:
            return

        try:
            self._convert_images_to_pdf(self.image_paths, output_pdf_path)
            messagebox.showinfo("Success", f"PDF created successfully: {output_pdf_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _convert_images_to_pdf(self, image_paths, output_pdf_path):
        images = []
        for image_path in image_paths:
            with open(image_path, 'rb') as f:
                images.append(f.read())
        
        with open(output_pdf_path, 'wb') as f:
            f.write(img2pdf.convert(images))

if __name__ == "__main__":
    app = ImageToPdfConverter()
    app.mainloop()
