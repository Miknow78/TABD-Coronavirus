import json

import numpy as np
from postgis.psycopg import register
import random
import matplotlib.pyplot as plt
import psycopg2
from matplotlib.animation import FuncAnimation
import datetime
from postgis import Polygon, MultiPolygon
import csv
from scipy.spatial import distance

conn = psycopg2.connect("dbname=taxis user=postgres")
register(conn)
cursor_psql = conn.cursor()

# criar o vetor inf [[0,0,0,0,0,...],[0,0,0,0,0,...],...]
m = 8640
n = 1661

random.seed()
# obter limites dos distritos
query_porto = '''
SELECT st_union(proj_boundary), 
min(st_xmin(proj_boundary)) as xmin, 
max(st_xmax(proj_boundary)) as xmax, 
min(st_ymin(proj_boundary)) as ymin, 
max(st_ymax(proj_boundary)) as ymax 
FROM cont_aad_caop2018 where distrito = 'PORTO'; 
'''
cursor_psql.execute(query_porto)
results = cursor_psql.fetchall()

for row in results:
    porto_xmin = row[1]
    porto_xmax = row[2]
    porto_ymin = row[3]
    porto_ymax = row[4]

query_lisboa = '''
SELECT st_union(proj_boundary), 
min(st_xmin(proj_boundary)) as xmin, 
max(st_xmax(proj_boundary)) as xmax, 
min(st_ymin(proj_boundary)) as ymin, 
max(st_ymax(proj_boundary)) as ymax 
FROM cont_aad_caop2018 where distrito = 'LISBOA'; 
'''
cursor_psql.execute(query_lisboa)
results = cursor_psql.fetchall()
for row in results:
    lisboa_xmin = row[1]
    lisboa_xmax = row[2]
    lisboa_ymin = row[3]
    lisboa_ymax = row[4]

# Arranjar um aleatorio

porto_infected = False
lisboa_infected = False

def check_if_porto(coord):
    if porto_xmin <= coord[0] <= porto_xmax and coord[1] >= porto_ymin and coord[1] <= porto_ymax:
        return True
    else:
        return False


def check_if_lisboa(coord):
    if lisboa_xmin <= coord[0] <= lisboa_xmax and lisboa_ymin <= coord[1] <= lisboa_ymax:
        return True
    else:
        return False

def check_if_all_infected(l):
    for i in l:
        if i == 0:
            return False
    return True

def list_to_string(l):
    line = ','.join(str(ix) for ix in l)
    line += '\n'
    return line

outfile = open('infected.csv', 'a')
linha = 0

infected_taxis = [0 for _ in range(0, 1660)]

with open('offsets3.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for ts in reader:  # para cada ts
        tx_i = 0  # col
        print("[!] Linha ", linha)
        for taxi in ts:
            x, y = taxi.split()
            x = float(x)
            y = float(y)
            if not porto_infected and check_if_porto([x, y]):
                infected_taxis[tx_i] = 1
                porto_infected = True
                # print("[!] Infected taxi on Porto - ", tx_i)
                tx_i += 1
                continue
            if not lisboa_infected and check_if_lisboa([x, y]):
                infected_taxis[tx_i] = 1
                lisboa_infected = True
                # print("[!] Infected taxi on Lisboa - ", tx_i)
                tx_i += 1
                continue
            if porto_infected or lisboa_infected:
                if infected_taxis[tx_i] == 1:
                    for taxi_j in range(0, len(ts) - 1):
                        if tx_i == taxi_j:
                            continue
                        if infected_taxis[taxi_j] == 1:
                            continue
                        x2, y2 = ts[taxi_j].split()
                        x2 = float(x2)
                        y2 = float(y2)
                        if (x == 0.0 and y == 0.0) or (x2 == 0.0 and y2 == 0.0):
                            continue
                        dst = distance.euclidean([x, y], [x2, y2])
                        if dst <= 50:
                            # print('[!] Two taxis in range and near a infected one')
                            chance = random.randint(1, 10)
                            if chance == 1:
                                # print('[!] 10% chance success! Infected taxi!')
                                infected_taxis[taxi_j] = 1
                                infected_taxis[tx_i] = 1
            tx_i += 1

        if check_if_all_infected(infected_taxis):
            outfile.write(list_to_string(infected_taxis))
            exit(0)

        outfile.write(list_to_string(infected_taxis))
        tx_i = 0
        linha += 1
