# se hace las importaciones necesarias
import tkinter as tk
import subprocess #este nos permite ejecutar comandos del sistema

def abrir_google(): # el flujo de pasos que hara al precionar el boton
    subprocess.Popen(["cmd.exe", "/c", "start", "chrome"]) #aqui el wsl2 le dira a windows que inicie google chrome

#creamos el diseño de la ventana, color, tamaño
ventana = tk.Tk()
ventana.title("Shell cosmico")
ventana.geometry("400x300")
ventana.configure(bg="#8AC42D")
#creamos el boton
boton = tk.Button(ventana, text="Abrir aplicacion", font=("Arial", 16, "bold"), bg="white", relief=tk.FLAT, cursor="hand2", command=abrir_google)
# ponemos el boton en medio de la ventana
boton.pack(expand=True)

# mantenemos la ventana abierta
ventana.mainloop()
