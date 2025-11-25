import time
import threading
import serial
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

arduino = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(2)

running = True
temperatures = []     # datos filtrados
raw_values = []       # datos sin filtrar

# Función de ventana para filtrado
def apply_window_filter(values, window_type="hamming", N=10):
    if len(values) < N:
        return sum(values) / len(values)

    x = np.array(values[-N:])

    if window_type == "rectangular":
        w = np.ones(N)
    elif window_type == "hanning":
        w = np.hanning(N)
    elif window_type == "hamming":
        w = np.hamming(N)
    elif window_type == "blackman":
        w = np.blackman(N)
    else:
        raise ValueError("Tipo de ventana no reconocido.")

    w = w / np.sum(w)
    return np.sum(x * w)

# Lectura del Arduino
def serial_reader():
    global running

    while True:
        if running:
            try:
                line = arduino.readline().decode().strip()
                if "Temperatura" in line:
                    value = float(line.split(":")[1])
                    
                    raw_values.append(value)

                    filtered = apply_window_filter(raw_values,
                                                   window_type="hamming",
                                                   N=12)

                    temperatures.append(filtered)

            except:
                pass
        
        time.sleep(0.1)

threading.Thread(target=serial_reader, daemon=True).start()

# Interfaz gráfica Tkinter
root = tk.Tk()
root.title("Monitor de Temperatura con Filtro")

def toggle_running():
    global running
    running = not running
    button.config(text="Reanudar" if not running else "Pausar")

def reset_data():
    temperatures.clear()
    raw_values.clear()

    ax.clear()
    ax.set_title("Temperatura en tiempo real (filtrada)")
    ax.set_xlabel("Muestras")
    ax.set_ylabel("°C")
    ax.set_ylim(0, 50)
    ax.grid(True)
    canvas.draw()

button = ttk.Button(root, text="Pausar", command=toggle_running)
button.pack(pady=10)

restart = ttk.Button(root, text="Reiniciar", command=reset_data)
restart.pack(pady=10)

fig, ax = plt.subplots(figsize=(12,8))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

def update_plot():
    ax.clear()
    ax.plot(temperatures, label="Temperatura filtrada")
    ax.set_title("Temperatura en tiempo real (filtrada)")
    ax.set_xlabel("Muestras")
    ax.set_ylabel("°C")
    ax.set_ylim(0, 50)

    n = len(temperatures)
    if n > 1:
        ax.set_xlim(0, n - 1)
    else:
        ax.set_xlim(0, 1)

    ax.grid(True)
    canvas.draw()
    root.after(200, update_plot)

update_plot()
root.mainloop()

