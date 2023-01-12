import matplotlib.pyplot as plt
import psycopg2
import csv
import pandas as pd
import matplotlib
import bar_chart_race as bcr

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


l11, l22, l33, l44, l55, l66, l77, l88, l99, l1010 = \
    [], [], [], [], [], [], [], [], [], []

for i in range(8639):
    l11.append(l1[i][1])
    l22.append(l2[i][1])
    l33.append(l3[i][1])
    l44.append(l4[i][1])
    l55.append(l5[i][1])
    l66.append(l6[i][1])
    l77.append(l7[i][1])
    l88.append(l8[i][1])
    l99.append(l9[i][1])
    l1010.append(l10[i][1])

distritos = {'Porto': l11, 'Lisboa': l22, 'Coimbra': l33, 'Braga': l44, 'Santarem': l55,
             'Viana do Castelo': l66, 'Leiria': l77, 'Aveiro': l88, 'Castelo Branco': l99,
             'Setubal': l1010}

df = pd.DataFrame(distritos, columns= ["Porto", "Lisboa", "Coimbra", "Braga",
              "Santarem", "Viana do Castelo", "Leiria", "Aveiro", "Castelo Branco", "Setubal"])

df.to_csv(r'C:\Users\maria\Documents\TABB - praticas\aula 3\Project\df.csv')

matplotlib.rcParams['animation.embed_limit'] = 2**128
bcr.bar_chart_race(df=df,
                   title="Crescimento do Número de Infetados",
                   n_bars = 10,
                   orientation = 'v',
                   cmap='prism')
plt.show()