import random
import math

e = math.exp(1)


## DATOS

def fdp_ia(x):
    ##exp = math.pow(((x - 1221.2273) / 402.7004), 2)
    return (math.pow(e, ((-1 / 2) * math.pow(((x - 1221.2273) / 402.7004), 2)))) / (
            402.7004 * math.pow(6.2838, (1 / 2)))


def ia():
    max_ia = 0.001
    r1 = random.random()
    r2 = random.random()
    x1 = 900 + 1500 * r1
    y1 = max_ia * r2
    if y1 <= fdp_ia(x1):
        return x1
    else:
        return 0.7 * ia()


def fdp_ta1(x):
    ##exp = math.pow(((x - 2436.0588) / 251.2740), 2)
    return (math.pow(e, ((-1 / 2) * math.pow(((x - 2436.0588) / 251.2740), 2)))) / (
            251.2740 * math.pow(6.2838, (1 / 2)))


def ta1():
    max_ta1 = 0.0016
    r1 = random.random()
    r2 = random.random()
    x1 = 1996 + 1050 * r1
    y1 = max_ta1 * r2
    if y1 <= fdp_ta1(x1):
        return x1
    else:
        return ta1()


def fdp_ta2(x):
    ##exp = math.pow((x - 3579.8636) / 401.6324, 2)
    return (math.pow(e, ((-1 / 2) * math.pow((x - 3579.8636) / 401.6324, 2)))) / (401.6324 * math.pow(6.2838, (1 / 2)))


def ta2():
    max_ta2 = 0.001
    r1 = random.random()
    r2 = random.random()
    x1 = 2505 + 1695 * r1
    y1 = max_ta2 * r2

    if y1 <= fdp_ta2(x1):
        return x1
    else:
        return ta2()


## VARIABLES DE CONTROL
m = 30
n = m
c = 2

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
        print(str(x) + " " + str(tps[x]))
        if tps[x] == hv:
            return x
        ##else:
        # print("la cague")


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
        ##print("ns " + str(ns1+ns2)+ " " + str((ns1 + ns2 <= c and tpsp == hv)) + " " + str((ns1 + ns2 <= c + 1 and tpsp != hv)))
        x = buscar_puesto_libre()
        _ta1 = ta1()
        tps[x] = t + _ta1
        sto[x] = sto[x] + t - ito[x]
        sta = sta + _ta1
        return
    else:
        if ns1 + ns2 == m + 2 and tpsp == hv:
            ##print("ns " + str(ns1 + ns2))
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
##print(sps)
##print(sta)

pto = []

for i in range(c):
    pto.append((100 * sto[i]) / t)

pttep = (100 * ttep) / t
ppct = 100 * (nc1 + nc2) / nt
ppc1 = 100 * (nc1) / nt
ppc2 = 100 * (nc2) / nt
print("Variable de control M: " + str(m))
print("Variable de control N: " + str(n))
print("PEC(minutos): " + str(pec / 60))
for i in range(c):
    print("PTO " + str(i + 1) + ": " + str(pto[i]))
print("PTTEP: " + str(pttep))

print(ns1+ns2)
##print("PPCT: "+ str(ppct))
##print("PPC1: "+ str(ppc1))
##print("PPC2: "+ str(ppc2))
