import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib as mpl
import matplotlib.patches as mpatches
import csv

def update(num, xx, yy, lin):
    lin.set_data(xx[:num], yy[:num])
    plt.axis([0, 9000, 0, 2000])
    print(str(yy[num]))
    ax.set_title('Nº total de infetados: ' + str(yy[num]))
    fig.canvas.draw()
    return lin,

mpl.rcParams['animation.ffmpeg_path'] = r'C:\ffmpeg\bin\ffmpeg.exe'

count = 0
inf = []
i = 0

with open('infected_colors.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        count = 0
        i += 1
        for j in row:
            if j == 'red':
                count += 1
        print(count)
        inf.append(count)

x = np.array(range(0, 8640))
y = np.array(inf)

fig, ax = plt.subplots()
line, = ax.plot(x, y, color='blue')
blue_patch = mpatches.Patch(color='blue', label='Número de Táxis Infetados')
plt.legend(handles=[blue_patch])
ax.set_title('Nº total de infetados: ' + str(0))
ani = animation.FuncAnimation(fig, update, len(x), fargs=[x, y, line], interval=0.001, blit=True)


f = r'C:\Users\maria\Documents\TABB - praticas\aula 3\Project\video3.mov'
writervideo = animation.FFMpegWriter(fps=60)
ani.save(f, writer=writervideo)
plt.show()
