import tkinter as tk
from tkinter import messagebox
from torre_hanoi import TorreDeHanoi  # Importar la clase TorreDeHanoi

# Inicializa las Torres de Hanói con 8 discos
torre = TorreDeHanoi(8)

# Función para actualizar la visualización de las torres
def actualizar_estado():
    canvas.delete("all")  # Limpiar el canvas

    # Dibujar las varillas y las letras correspondientes
    for i, letra in enumerate(['A', 'B', 'C']):
        x = 150 * i + 75
        canvas.create_line(x, 50, x, 300, width=4)  # Dibujar la varilla
        canvas.create_text(x, 320, text=letra, font=("Arial", 16, "bold"))  # Dibujar la letra debajo de cada varilla

    # Dibujar los discos en cada varilla
    for varilla, discos in torre.varillas.items():
        if varilla == 'A':
            x_base = 75
        elif varilla == 'B':
            x_base = 225
        else:
            x_base = 375

        y_base = 300
        for disco in discos:
            ancho = disco * 20
            canvas.create_rectangle(x_base - ancho, y_base - 20, x_base + ancho, y_base, fill="blue")
            y_base -= 30

# Función para mover un disco
def mover_disco():
    origen = entry_origen.get().upper()
    destino = entry_destino.get().upper()

    if origen not in ['A', 'B', 'C'] or destino not in ['A', 'B', 'C']:
        messagebox.showerror("Error", "Las varillas deben ser A, B o C.")
        return

    valido, mensaje = torre.mover_disco(origen, destino)
    if valido:
        actualizar_estado()
        if torre.verificar_reto(destino):
            messagebox.showinfo("¡Éxito!", "Has completado el reto con éxito.")
    else:
        messagebox.showerror("Movimiento Inválido", mensaje)

# Función para reiniciar el juego
def reiniciar_juego():
    torre.reiniciar()
    actualizar_estado()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Simulación Visual de Torres de Hanói")
ventana.geometry("500x500")

# Canvas para dibujar las torres y discos
canvas = tk.Canvas(ventana, width=450, height=350)
canvas.pack()

# Etiquetas e inputs para mover los discos
label_origen = tk.Label(ventana, text="Varilla de origen (A, B, C):")
label_origen.pack(pady=5)
entry_origen = tk.Entry(ventana)
entry_origen.pack(pady=5)

label_destino = tk.Label(ventana, text="Varilla de destino (A, B, C):")
label_destino.pack(pady=5)
entry_destino = tk.Entry(ventana)
entry_destino.pack(pady=5)

# Botón para mover el disco
boton_mover = tk.Button(ventana, text="Mover Disco", command=mover_disco)
boton_mover.pack(pady=10)

# Botón para reiniciar el juego
boton_reiniciar = tk.Button(ventana, text="Reiniciar", command=reiniciar_juego)
boton_reiniciar.pack(pady=10)

# Mostrar el estado inicial de las torres
actualizar_estado()

# Ejecutar la ventana principal
ventana.mainloop()
