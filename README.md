# 🌡️ RealTimeTemperatureDAQ  
### Monitor de Temperatura en Tiempo Real con Arduino + Python + Filtro por Ventana (Hamming)

---

## 📌 Descripción del Proyecto

Este proyecto es un **sistema de adquisición de datos (DAQ)** enfocado en la medición y visualización de temperatura en tiempo real.  
Incluye:

- 🔌 **Arduino** como dispositivo sensor  
- 🖥️ **Python** como sistema de procesamiento y visualización  
- 🎛️ **Filtro digital por ventana (Hamming)** para suavizar la señal  
- 📊 **Gráfica en tiempo real** integrada con Tkinter + Matplotlib  
- 🔵🔴 **Indicadores LED** (calor/frío)

Ideal para prácticas de instrumentación, electrónica y procesamiento de señales.

---


## 🚀 Características

- 🧩 Lectura continua desde puerto serial  
- 🎚️ Filtros digitales (Hamming, Hanning, Blackman, Rectangular)  
- 📉 Gráfica dinámica en una interfaz Tkinter  
- ⏯️ Botón de Pausar/Reanudar  
- 🔄 Reinicio de datos sin cerrar la aplicación  
- 🔴 LED → temperatura cálida  
- 🔵 LED → temperatura fría  

---


## 👨‍💻 Créditos del Código

Código desarrollado en colaboración con:  
**Aniel Castañeda** — [@xdanep](https://gitlab.com/xdanep)  
Licencia: **GNU GPL v3**

---

## 🛠️ Tecnologías Usadas

### **Hardware**
- Arduino (Uno / Nano / Leonardo)
- Sensor de temperatura (LM35, TMP36, termistor)
- LEDs rojo y azul
- Resistencias de 220Ω

### **Software**
- Python 3  
- Tkinter  
- Matplotlib  
- NumPy  
- PySerial  

---

## 📂 Estructura del Proyecto

