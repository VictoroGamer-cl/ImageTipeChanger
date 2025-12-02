import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image
import os


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class ConversorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Conversor de Imágenes (PNG, JPEG, ICO)")
        self.geometry("600x500")
        self.resizable(False, False)


        self.ruta_imagen_origen = ""
        self.ruta_carpeta_destino = ""


        self.frame_titulo = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_titulo.pack(pady=20)
        
        self.lbl_titulo = ctk.CTkLabel(
            self.frame_titulo, 
            text="🖼️ Conversor Rápido", 
            font=("Arial", 26, "bold")
        )
        self.lbl_titulo.pack()

        self.frame_origen = ctk.CTkFrame(self)
        self.frame_origen.pack(pady=10, padx=20, fill="x")

        self.btn_importar = ctk.CTkButton(
            self.frame_origen, 
            text="📂 Cargar Imagen", 
            command=self.seleccionar_imagen,
            width=150
        )
        self.btn_importar.pack(side="left", padx=15, pady=15)

        self.lbl_origen_info = ctk.CTkLabel(
            self.frame_origen, 
            text="Sin archivo...", 
            text_color="gray"
        )
        self.lbl_origen_info.pack(side="left", padx=5)
        self.frame_config = ctk.CTkFrame(self)
        self.frame_config.pack(pady=10, padx=20, fill="x")

        self.lbl_formato = ctk.CTkLabel(
            self.frame_config, 
            text="Formato:", 
            font=("Arial", 14, "bold")
        )
        self.lbl_formato.pack(side="left", padx=15, pady=15)

        # SOLO LOS FORMATOS SOLICITADOS
        self.opciones_formato = ["PNG", "JPEG", "ICO"]
        self.combo_formato = ctk.CTkOptionMenu(
            self.frame_config, 
            values=self.opciones_formato,
            width=150
        )
        self.combo_formato.pack(side="left", padx=5)
        self.combo_formato.set("PNG")

        self.frame_destino = ctk.CTkFrame(self)
        self.frame_destino.pack(pady=10, padx=20, fill="x")

        self.btn_carpeta = ctk.CTkButton(
            self.frame_destino, 
            text="💾 Guardar en...", 
            command=self.seleccionar_carpeta,
            width=150,
            fg_color="#E67E22", 
            hover_color="#D35400"
        )
        self.btn_carpeta.pack(side="left", padx=15, pady=15)

        self.lbl_destino_info = ctk.CTkLabel(
            self.frame_destino, 
            text="Carpeta actual (por defecto)", 
            text_color="gray"
        )
        self.lbl_destino_info.pack(side="left", padx=5)
        self.btn_convertir = ctk.CTkButton(
            self, 
            text="⚡ CONVERTIR AHORA", 
            command=self.convertir_imagen,
            width=250,
            height=50,
            font=("Arial", 16, "bold"),
            fg_color="#2ECC71",
            hover_color="#27AE60"
        )
        self.btn_convertir.pack(pady=30)

    def seleccionar_imagen(self):
        tipos = [("Imágenes", "*.png;*.jpg;*.jpeg;*.webp;*.bmp"), ("Todos", "*.*")]
        ruta = filedialog.askopenfilename(title="Selecciona tu imagen", filetypes=tipos)
        if ruta:
            self.ruta_imagen_origen = ruta
            nombre = os.path.basename(ruta)
            display_name = (nombre[:25] + '...') if len(nombre) > 25 else nombre
            self.lbl_origen_info.configure(text=display_name, text_color=("black", "white"))

    def seleccionar_carpeta(self):
        ruta = filedialog.askdirectory(title="Dónde guardar el archivo")
        if ruta:
            self.ruta_carpeta_destino = ruta
            display_name = (ruta[:30] + '...') if len(ruta) > 30 else ruta
            self.lbl_destino_info.configure(text=display_name, text_color=("black", "white"))

    def convertir_imagen(self):
        if not self.ruta_imagen_origen:
            messagebox.showwarning("Falta imagen", "Por favor, selecciona una imagen primero.")
            return
        try:
            img = Image.open(self.ruta_imagen_origen)
            nombre_base = os.path.splitext(os.path.basename(self.ruta_imagen_origen))[0]
            formato = self.combo_formato.get().lower()
            
            dir_salida = self.ruta_carpeta_destino if self.ruta_carpeta_destino else os.path.dirname(self.ruta_imagen_origen)
            
            nombre_salida = f"{nombre_base}_new.{formato}"
            ruta_completa = os.path.join(dir_salida, nombre_salida)
            if formato == "jpeg":

                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")
            
            elif formato == "ico":
                if img.size[0] > 256 or img.size[1] > 256:
                    img = img.resize((256, 256), Image.Resampling.LANCZOS)
                
                img.save(ruta_completa, format='ICO', sizes=[(256, 256)])
                messagebox.showinfo("¡Éxito!", f"Icono guardado en:\n{ruta_completa}")
                return
            img.save(ruta_completa)
            messagebox.showinfo("¡Éxito!", f"Imagen convertida y guardada en:\n{ruta_completa}")

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al convertir:\n{str(e)}")

if __name__ == "__main__":
    app = ConversorApp()
    app.mainloop()