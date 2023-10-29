import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def calcular_punto_equilibrio():
    try:
        precio_venta = float(precio_venta_entry.get())
        costos_variables = float(costos_variables_entry.get())
        costos_fijos = float(costos_fijos_entry.get())

        margen_contribucion = precio_venta - costos_variables
        unidades_vendidas = costos_fijos / margen_contribucion
        unidades_vendidas_Q = unidades_vendidas * precio_venta

        resultado_unidades_label.config(text=f"Punto de Equilibrio en Unidades: {unidades_vendidas:.2f}")
        resultado_quetzales_label.config(text=f"Punto de Equilibrio en Quetzales: Q{unidades_vendidas_Q:.2f}")

        # Crear una gráfica
        unidades = range(0, int(unidades_vendidas) + 10)
        ingresos = [unidad * precio_venta for unidad in unidades]
        costos_totales = [costos_fijos + (unidad * costos_variables) for unidad in unidades]

        plt.figure()
        plt.plot(unidades, ingresos, label='Ingresos')
        plt.plot(unidades, costos_totales, label='Costos Totales')
        plt.axvline(x=unidades_vendidas, color='r', linestyle='--', label='Punto de Equilibrio')
        plt.xlabel('Unidades Vendidas')
        plt.ylabel('Monto (Quetzales)')
        plt.title('Punto de Equilibrio')
        plt.legend()

        # Mostrar la gráfica en la ventana de Tkinter
        canvas = FigureCanvasTkAgg(plt.gcf(), master=window)
        canvas.get_tk_widget().pack()

    except ValueError:
        resultado_unidades_label.config(text="Ingrese números válidos.")
        resultado_quetzales_label.config(text="")

# Configuración de la ventana
window = tk.Tk()
window.title("Punto de Equilibrio")

# Etiquetas y entradas
tk.Label(window, text="Precio de Venta por Unidad (Quetzales):").pack()
precio_venta_entry = tk.Entry(window)
precio_venta_entry.pack()

tk.Label(window, text="Costos Variables por Unidad (Quetzales):").pack()
costos_variables_entry = tk.Entry(window)
costos_variables_entry.pack()

tk.Label(window, text="Costos Fijos (Quetzales):").pack()
costos_fijos_entry = tk.Entry(window)
costos_fijos_entry.pack()

# Botón para calcular el punto de equilibrio
calcular_button = tk.Button(window, text="Calcular Punto de Equilibrio", command=calcular_punto_equilibrio)
calcular_button.pack()

# Resultados
resultado_unidades_label = tk.Label(window, text="", font=("Arial", 12))
resultado_unidades_label.pack()

resultado_quetzales_label = tk.Label(window, text="", font=("Arial", 12))
resultado_quetzales_label.pack()

window.mainloop()
