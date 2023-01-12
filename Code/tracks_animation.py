import matplotlib.pyplot as plt
import psycopg2
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
import datetime
import csv
from postgis import Polygon, MultiPolygon
from postgis.psycopg import register
import matplotlib as mpl
import numpy as np
mpl.rcParams['animation.ffmpeg_path'] = r'C:\ffmpeg\bin\ffmpeg.exe'

def animate(ix):
    print(ix)
    ax.set_title(datetime.datetime.utcfromtimestamp(ts_i + ix * 10))
    scat.set_offsets(offsets[ix])
    scat.set_color(infected[ix])

ts_i = 1570665600

scale = 1 / 3000000
conn = psycopg2.connect("dbname=taxis user=postgres password=mariana")
register(conn)

xs_min, xs_max, ys_min, ys_max = -120000, 165000, -310000, 285000
width_in_inches = (xs_max - xs_min) / 0.0254 * 1.1
height_in_inches = (ys_max - ys_min) / 0.0254 * 1.1

fig, ax = plt.subplots(figsize=(width_in_inches * scale, height_in_inches * scale))
ax.axis('off')
ax.set(xlim=(xs_min, xs_max), ylim=(ys_min, ys_max))

cursor_psql = conn.cursor()
sql = "select distrito,st_union(proj_boundary) from cont_aad_caop2018 group by distrito"

cursor_psql.execute(sql)
results = cursor_psql.fetchall()
xs, ys = [], []
for row in results:
    geom = row[1]
    if type(geom) is MultiPolygon:
        for pol in geom:
            xys = pol[0].coords
            xs, ys = [], []
            for (x, y) in xys:
                xs.append(x)
                ys.append(y)
            ax.plot(xs, ys, color='black', lw='0.2')
    if type(geom) is Polygon:
        xys = geom[0].coords
        xs, ys = [], []
        for (x, y) in xys:
            xs.append(x)
            ys.append(y)
        ax.plot(xs, ys, color='black', lw='0.2')

offsets = []
inf = []
print('Finished Map Query!')

with open('Csv files\offsets3.csv', 'r') as csvFile1:
    reader = csv.reader(csvFile1)
    i = 0
    for row in reader:
        l1 = []
        for j in row:
            x, y = j.split()
            x = float(x)
            y = float(y)
            l1.append([x, y])
        offsets.append(l1)

infected = []
with open('Csv files\infected_colors.csv', 'r') as csvFile2:
    reader = csv.reader(csvFile2)
    i = 0
    for row in reader:
        l2 = []
        for j in row:
            l2.append(str(j))
        infected.append(l2)

x, y = [], []
print(len(offsets))
for i in offsets[0]:
    x.append(i[0])
    y.append(i[1])

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)


t1 = np.arange(0.0, 3.0, 0.01)

ax1 = plt.subplot(212)
ax1.margins(0.05)           # Default margin is 0.05, value 0 means fit
ax1.plot(t1, f(t1))

ax2 = plt.subplot(221)
ax2.margins(2, 2)           # Values >0.0 zoom out
ax2.plot(t1, f(t1))
ax2.set_title('Zoomed out')

ax3 = plt.subplot(222)
ax3.margins(x=0, y=-0.25)   # Values in (-0.5, 0.0) zooms in to center
ax3.plot(t1, f(t1))
ax3.set_title('Zoomed in')

scat = ax.scatter(x, y, s=2, color='orange')
anim = FuncAnimation(fig, animate, interval=5, frames=len(offsets) - 1, repeat=False)
plt.show()

#f = r'C:\Users\maria\Documents\TABB - praticas\aula 3\Project\porto.mov'
#writervideo = animation.FFMpegWriter(fps=60)
#anim.save(f, writer=writervideo)

