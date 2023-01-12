import matplotlib.pyplot as plt
import matplotlib as mpl
import psycopg2
import csv
import numpy as np

conn = psycopg2.connect("dbname=taxis user=postgres password=mariana")
cursor = conn.cursor()
sql = "select distrito,st_union(proj_boundary) from cont_aad_caop2018 group by distrito"
cursor.execute(sql)
results = cursor.fetchall()

def check_if_porto(coord):
    if porto_xmin <= coord[0] and porto_xmax >= coord[0] and porto_ymin <= coord[1] and porto_ymax >= coord[1]:
        return True
    else:
        return False

def check_if_lisboa(coord):
    if lisboa_xmin <= coord[0] and lisboa_xmax >= coord[0] and lisboa_ymin <= coord[1] and lisboa_ymax >= coord[1]:
        return True
    else:
        return False

def check_if_braga(coord):
    if braga_xmin <= coord[0] and braga_xmax >= coord[0] and braga_ymin <= coord[1] and braga_ymax >= coord[1]:
        return True
    else:
        return False

def check_if_coimbra(coord):
    if coimbra_xmin <= coord[0] and coimbra_xmax >= coord[0] and coimbra_ymin <= coord[1] and coimbra_ymax >= coord[1]:
        return True
    else:
        return False

def check_if_leiria(coord):
    if leiria_xmin <= coord[0] and leiria_xmax >= coord[0] and leiria_ymin <= coord[1] and leiria_ymax >= coord[1]:
        return True
    else:
        return False

def check_if_santarem(coord):
    if santarem_xmin <= coord[0] and santarem_xmax >= coord[0] and santarem_ymin <= coord[1] and santarem_ymax >= coord[1]:
        return True
    else:
        return False

def check_if_viana(coord):
    if viana_xmin <= coord[0] and viana_xmax >= coord[0] and viana_ymin <= coord[1] and viana_ymax >= coord[1]:
        return True
    else:
        return False

def check_if_castelo(coord):
    if castelo_xmin <= coord[0] and castelo_xmax >= coord[0] and castelo_ymin <= coord[1] and castelo_ymax >= coord[1]:
        return True
    else:
        return False

def check_if_aveiro(coord):
    if aveiro_xmin <= coord[0] and aveiro_xmax >= coord[0] and aveiro_ymin <= coord[1] and aveiro_ymax >= coord[1]:
        return True
    else:
        return False

def check_if_setubal(coord):
    if setubal_xmin <= coord[0] and setubal_xmax >= coord[0] and setubal_ymin <= coord[1] and setubal_ymax >= coord[1]:
        return True
    else:
        return False

query_district = '''
SELECT st_union(proj_boundary), 
min(st_xmin(proj_boundary)) as xmin, 
max(st_xmax(proj_boundary)) as xmax, 
min(st_ymin(proj_boundary)) as ymin, 
max(st_ymax(proj_boundary)) as ymax 
FROM cont_aad_caop2018 where distrito = 'PORTO'; 
'''
cursor.execute(query_district)
results = cursor.fetchall()

for row in results:
    porto_xmin = row[1]
    porto_xmax = row[2]
    porto_ymin = row[3]
    porto_ymax = row[4]

query_district = '''
SELECT st_union(proj_boundary), 
min(st_xmin(proj_boundary)) as xmin, 
max(st_xmax(proj_boundary)) as xmax, 
min(st_ymin(proj_boundary)) as ymin, 
max(st_ymax(proj_boundary)) as ymax 
FROM cont_aad_caop2018 where distrito = 'LISBOA'; 
'''
cursor.execute(query_district)
results = cursor.fetchall()

for row in results:
    lisboa_xmin = row[1]
    lisboa_xmax = row[2]
    lisboa_ymin = row[3]
    lisboa_ymax = row[4]

query_district = '''
SELECT st_union(proj_boundary), 
min(st_xmin(proj_boundary)) as xmin, 
max(st_xmax(proj_boundary)) as xmax, 
min(st_ymin(proj_boundary)) as ymin, 
max(st_ymax(proj_boundary)) as ymax 
FROM cont_aad_caop2018 where distrito = 'BRAGA'; 
'''
cursor.execute(query_district)
results = cursor.fetchall()

for row in results:
    braga_xmin = row[1]
    braga_xmax = row[2]
    braga_ymin = row[3]
    braga_ymax = row[4]

query_district = '''
SELECT st_union(proj_boundary), 
min(st_xmin(proj_boundary)) as xmin, 
max(st_xmax(proj_boundary)) as xmax, 
min(st_ymin(proj_boundary)) as ymin, 
max(st_ymax(proj_boundary)) as ymax 
FROM cont_aad_caop2018 where distrito = 'COIMBRA'; 
'''
cursor.execute(query_district)
results = cursor.fetchall()

for row in results:
    coimbra_xmin = row[1]
    coimbra_xmax = row[2]
    coimbra_ymin = row[3]
    coimbra_ymax = row[4]

query_district = '''
SELECT st_union(proj_boundary), 
min(st_xmin(proj_boundary)) as xmin, 
max(st_xmax(proj_boundary)) as xmax, 
min(st_ymin(proj_boundary)) as ymin, 
max(st_ymax(proj_boundary)) as ymax 
FROM cont_aad_caop2018 where distrito = 'SANTARÉM'; 
'''
cursor.execute(query_district)
results = cursor.fetchall()

for row in results:
    santarem_xmin = row[1]
    santarem_xmax = row[2]
    santarem_ymin = row[3]
    santarem_ymax = row[4]

query_district = '''
SELECT st_union(proj_boundary), 
min(st_xmin(proj_boundary)) as xmin, 
max(st_xmax(proj_boundary)) as xmax, 
min(st_ymin(proj_boundary)) as ymin, 
max(st_ymax(proj_boundary)) as ymax 
FROM cont_aad_caop2018 where distrito = 'CASTELO BRANCO'; 
'''
cursor.execute(query_district)
results = cursor.fetchall()

for row in results:
    castelo_xmin = row[1]
    castelo_xmax = row[2]
    castelo_ymin = row[3]
    castelo_ymax = row[4]

query_district = '''
SELECT st_union(proj_boundary), 
min(st_xmin(proj_boundary)) as xmin, 
max(st_xmax(proj_boundary)) as xmax, 
min(st_ymin(proj_boundary)) as ymin, 
max(st_ymax(proj_boundary)) as ymax 
FROM cont_aad_caop2018 where distrito = 'VIANA DO CASTELO'; 
'''
cursor.execute(query_district)
results = cursor.fetchall()

for row in results:
    viana_xmin = row[1]
    viana_xmax = row[2]
    viana_ymin = row[3]
    viana_ymax = row[4]

query_district = '''
SELECT st_union(proj_boundary), 
min(st_xmin(proj_boundary)) as xmin, 
max(st_xmax(proj_boundary)) as xmax, 
min(st_ymin(proj_boundary)) as ymin, 
max(st_ymax(proj_boundary)) as ymax 
FROM cont_aad_caop2018 where distrito = 'AVEIRO'; 
'''
cursor.execute(query_district)
results = cursor.fetchall()

for row in results:
    aveiro_xmin = row[1]
    aveiro_xmax = row[2]
    aveiro_ymin = row[3]
    aveiro_ymax = row[4]

query_district = '''
SELECT st_union(proj_boundary), 
min(st_xmin(proj_boundary)) as xmin, 
max(st_xmax(proj_boundary)) as xmax, 
min(st_ymin(proj_boundary)) as ymin, 
max(st_ymax(proj_boundary)) as ymax 
FROM cont_aad_caop2018 where distrito = 'LEIRIA'; 
'''
cursor.execute(query_district)
results = cursor.fetchall()

for row in results:
    leiria_xmin = row[1]
    leiria_xmax = row[2]
    leiria_ymin = row[3]
    leiria_ymax = row[4]

query_district = '''
SELECT st_union(proj_boundary), 
min(st_xmin(proj_boundary)) as xmin, 
max(st_xmax(proj_boundary)) as xmax, 
min(st_ymin(proj_boundary)) as ymin, 
max(st_ymax(proj_boundary)) as ymax 
FROM cont_aad_caop2018 where distrito = 'SETÚBAL'; 
'''
cursor.execute(query_district)
results = cursor.fetchall()

for row in results:
    setubal_xmin = row[1]
    setubal_xmax = row[2]
    setubal_ymin = row[3]
    setubal_ymax = row[4]

offsets = []
inf = []
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
for i in offsets[0]:
    x.append(i[0])
    y.append(i[1])

l1, l2, l3, l4, l5, l6, l7, l8, l9, l10 = [], [], [], [], [], [], [], [], [], []
linha = -1
coluna = -1
for row in offsets:
    totalporto = 0
    totalcoimbra = 0
    totallisboa = 0
    totalbraga = 0
    totalsantarem = 0
    totalviana = 0
    totalaveiro = 0
    totalcastelo = 0
    totalleiria = 0
    totalsetubal = 0
    linha += 1
    coluna = -1
    for j in row:
        coluna += 1
        if coluna > 1659:
            continue
        x = j[0]
        y = j[1]
        if infected[linha][coluna] == 'red':
            if check_if_porto([x, y]):
                totalporto += 1
            elif check_if_lisboa([x, y]):
                totallisboa += 1
            elif check_if_coimbra([x, y]):
                totalcoimbra += 1
            elif check_if_braga([x, y]):
                totalbraga += 1
            elif check_if_santarem([x, y]):
                totalsantarem += 1
            elif check_if_viana([x, y]):
                totalviana += 1
            elif check_if_leiria([x, y]):
                totalleiria += 1
            elif check_if_aveiro([x, y]):
                totalaveiro += 1
            elif check_if_castelo([x, y]):
                totalcastelo += 1
            elif check_if_setubal([x, y]):
                totalsetubal += 1

    l1.append([linha, totalporto])
    l2.append([linha, totallisboa])
    l3.append([linha, totalcoimbra])
    l4.append([linha, totalbraga])
    l5.append([linha, totalsantarem])
    l6.append([linha, totalviana])
    l7.append([linha, totalleiria])
    l8.append([linha, totalaveiro])
    l9.append([linha, totalcastelo])
    l10.append([linha, totalsetubal])



distritos = ["Porto", "Lisboa", "Coimbra", "Braga",
             "Santarem", "Viana do Castelo", "Leiria", "Aveiro", "Castelo Branco", "Setúbal"]
ts = ["Ts: 0:00", "Ts: 5:00", "Ts: 10:00", "Ts: 12:00",
      "Ts: 15:00", "Ts: 17:00", "Ts: 20:00", "Ts: 22:00", "Ts: 23:59"]

infetados = np.array(
    [[l1[0][1], l1[1800][1], l1[3600][1], l1[4320][1], l1[5400][1], l1[6120][1], l1[7200][1], l1[7920][1], l1[8639][1]],
     [l2[0][1], l2[1800][1], l2[3600][1], l2[4320][1], l2[5400][1], l2[6120][1], l2[7200][1], l2[7920][1], l2[8639][1]],
     [l3[0][1], l3[1800][1], l3[3600][1], l3[4320][1], l3[5400][1], l3[6120][1], l3[7200][1], l3[7920][1], l3[8639][1]],
     [l4[0][1], l4[1800][1], l4[3600][1], l4[4320][1], l4[5400][1], l4[6120][1], l4[7200][1], l4[7920][1], l4[8639][1]],
     [l5[0][1], l5[1800][1], l5[3600][1], l5[4320][1], l5[5400][1], l5[6120][1], l5[7200][1], l5[7920][1], l5[8639][1]],
     [l6[0][1], l6[1800][1], l6[3600][1], l6[4320][1], l6[5400][1], l6[6120][1], l6[7200][1], l6[7920][1], l6[8639][1]],
     [l7[0][1], l7[1800][1], l7[3600][1], l7[4320][1], l7[5400][1], l7[6120][1], l7[7200][1], l7[7920][1], l7[8639][1]],
     [l8[0][1], l8[1800][1], l8[3600][1], l8[4320][1], l8[5400][1], l8[6120][1], l8[7200][1], l8[7920][1], l8[8639][1]],
     [l9[0][1], l9[1800][1], l9[3600][1], l9[4320][1], l9[5400][1], l9[6120][1], l9[7200][1], l9[7920][1], l9[8639][1]],
     [l10[0][1], l10[1800][1], l10[3600][1], l10[4320][1], l10[5400][1], l10[6120][1], l10[7200][1], l10[7920][1],
      l10[8639][1]]])

plt.rcParams['figure.figsize'] = [10, 5]
fig, ax = plt.subplots()
im = ax.imshow(infetados)
ax.set_xticks(np.arange(len(ts)))
ax.set_yticks(np.arange(len(distritos)))

ax.set_xticklabels(ts)
ax.set_yticklabels(distritos)

plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

for i in range(len(distritos)):
    for j in range(len(ts)):
        text = ax.text(j, i, infetados[i, j],
                       ha="center", va="center", color="w")

ax.set_title("Número de Infetados por Distrito ao Longo do Dia")
plt.show()