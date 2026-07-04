import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.set_aspect('equal')

# axes
ax.plot([-1, 1], [0, 0])
ax.plot([0, 0], [-1, 1])

# unit circle
t = np.linspace(0, 2 * np.pi, 200)
ax.plot(np.cos(t), np.sin(t))

# initial point
theta = 0
x = np.cos(theta)
y = np.sin(theta)

point, = ax.plot([x], [y], 'ro')

cos_line, = ax.plot([], [], 'b-')
sin_line, = ax.plot([], [], 'r-')
hyp_line, = ax.plot([], [], 'g-')

# animation test
# for i in range(50):
#     theta += 0.05

#     x = np.cos(theta)
#     y = np.sin(theta)

#     point.set_data([x], [y])

#     plt.pause(0.02)

# capture mouse movement
def on_move(event):
    if event.xdata is None or event.ydata is None:
        return
    
    x = event.xdata
    y = event.ydata

    theta = np.arctan2(y, x)

    x_unit = np.cos(theta)
    y_unit = np.sin(theta)

    hyp_line.set_data([0, x_unit], [0, y_unit])
    cos_line.set_data([0, x_unit], [0, 0])
    sin_line.set_data([x_unit, x_unit], [0, y_unit])

    fig.canvas.draw_idle()

    point.set_data([x_unit], [y_unit])
    fig.canvas.draw_idle()

    # print(event.xdata, event.ydata)

fig.canvas.mpl_connect('motion_notify_event', on_move)

plt.show()