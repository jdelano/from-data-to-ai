import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Use TkAgg backend for GUI window compatibility
plt.switch_backend('TkAgg')

# Create a figure and axis
fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 1000)
line, = ax.plot(x, np.sin(x), lw=2)
ax.set_ylim(-1.5, 1.5)
ax.set_title("Animated Sine Wave")
ax.set_xlabel("x")
ax.set_ylabel("Amplitude")

# Update function for animation
def update(frame):
    y = np.sin(x + 0.05 * frame)
    line.set_ydata(y)
    return line,

# Create the animation
ani = animation.FuncAnimation(
    fig,       # Figure to animate
    update,    # Update function
    frames=200,  # Number of frames
    interval=30, # Delay between frames in ms
    blit=True   # Only redraw changed parts
)

plt.show()