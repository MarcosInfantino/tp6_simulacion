import random
import math
from scipy import special


e = math.exp(1)


## DATOS



def ia():
    r = random.random()
    return 1713.9477 + 281.3620 * (math.pow(2, (1 / 2))) * special.erfinv(2 * r - 1)

def ta1():
    r = random.random()
    return 2546.4755+230.1838*(math.pow(2, (1/2)))*special.erfinv(2*r-1)

def ta2():
    r = random.random()
    return 1175*r + 3004



## VARIABLES DE CONTROL
m = 15
n = m
c = 3

## CONDICIONES INICIALES
tf = 8640000  ##10 dias 864000
hv = tf + 1
t = 0
tpll = 0
tps = []
for i in range(c):
    tps.append(hv)
tpsp = hv
sps = 0
nt = 0
ns1 = 0
ns2 = 0
sto = []
for i in range(c):
    sto.append(0)
ito = []
for i in range(c):
    ito.append(0)
sta = 0
ttep = 0
tant = 0
nc1 = 0
nc2 = 0


## ALGORITMO

def buscar_puesto_libre():
    for x in range(c):

        if tps[x] == hv:
            return x



def llegada():
    global t, sps, tpll, nt, ns1, ns2, hv, tps1, tpsp, sto, ito, sta, ttep

    t = tpll
    sps = sps + (t - tant) * (ns1 + ns2)
    _ia = ia()
    tpll = t + _ia
    r = random.random()
    nt = nt + 1
    if r <= 0.35:
        ns1 = ns1 + 1
    else:
        ns2 = ns2 + 1
    if (ns1 + ns2 <= c and tpsp == hv) or (ns1 + ns2 <= c + 1 and tpsp != hv):

        x = buscar_puesto_libre()
        _ta1 = ta1()
        tps[x] = t + _ta1
        sto[x] = sto[x] + t - ito[x]
        sta = sta + _ta1
        return
    else:
        if ns1 + ns2 == m + 2 and tpsp == hv:

            _ta2 = ta2()
            tpsp = t + _ta2
            sta = sta + _ta2
            ttep = ttep + _ta2
            return
        else:
            return


def menor_tps():
    menor = 0
    for i in range(c):
        if tps[menor] > tps[i]:
            menor = i
    return menor


while t < tf:
    i = menor_tps()
    tant = t
    if tps[i] <= tpsp:
        if tpll <= tps[i]:
            llegada()
        else:
            t = tps[i]
            sps = sps + (t - tant) * (ns1 + ns2)

            if ns1 > 0:
                ns1 = ns1 - 1
            else:
                ns2 = ns2 - 1
            if ns1 + ns2 > c or (ns1 + ns2 == c and tpsp == hv):
                __ta1 = ta1()
                tps[i] = t + __ta1
                sta = sta + __ta1
            else:
                tps[i] = hv
                ito[i] = t
    else:
        if tpll <= tpsp:
            llegada()
        else:
            t = tpsp
            sps = sps + (t - tant) * (ns1 + ns2)

            if ns1 > 0:
                ns1 = ns1 - 1
            else:
                ns2 = ns2 - 1
            if ns1 + ns2 > n:
                __ta2 = ta2()
                tpsp = t + __ta2
                sta = sta + __ta2
                ttep = ttep + __ta2
            else:
                tpsp = hv

pec = (sps - sta) / nt
if pec <0:
    pec = 0.0

pto = []

for i in range(c):
    pto.append((100 * sto[i]) / t)

pttep = (100 * ttep) / t
ppct = 100 * (nc1 + nc2) / nt
ppc1 = 100 * (nc1) / nt
ppc2 = 100 * (nc2) / nt
print("Variable de control C: " + str(c))
print("Variable de control M: " + str(m))
print("Variable de control N: " + str(n))
print("PEC(minutos): " + str(pec / 60))
for i in range(c):
    print("PTO " + str(i + 1) + ": " + str(pto[i]))
print("PTTEP: " + str(pttep))


