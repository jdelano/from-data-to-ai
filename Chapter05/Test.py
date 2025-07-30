import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Ensure TkAgg backend is used for interactivity on Mac
plt.switch_backend('TkAgg')

# Initial parameters
init_freq = 1.0
x = np.linspace(0, 2 * np.pi, 1000)

# Create the figure and the line that we will manipulate
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)
line, = ax.plot(x, np.sin(init_freq * x), lw=2)
ax.set_title("Interactive Sine Wave")
ax.set_xlabel("x")
ax.set_ylabel("Amplitude")

# Slider axis: [left, bottom, width, height]
slider_ax = plt.axes([0.25, 0.1, 0.65, 0.03])
freq_slider = Slider(
    ax=slider_ax,
    label='Frequency',
    valmin=0.1,
    valmax=5.0,
    valinit=init_freq,
)

# Update function to change the line
def update(val):
    freq = freq_slider.val
    line.set_ydata(np.sin(freq * x))
    fig.canvas.draw_idle()

# Connect the slider to the update function
freq_slider.on_changed(update)

# Show the plot
plt.show()