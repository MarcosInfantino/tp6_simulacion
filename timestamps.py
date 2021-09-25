from datetime import datetime
from datetime import timedelta
from random import randint

cota_sup = 70 * 60
cota_sup_media = 65*60
cota_inf_media = 55*60
cota_inf = 50 * 60

randoms = []
fechas = []
fecha_inicial = datetime(2021, 9, 9, 0, 0)

print(fecha_inicial)
fechas.append(fecha_inicial)
fechas.append(fecha_inicial)
while fecha_inicial.day < 15:
    r = randint(cota_inf, cota_inf_media)
    randoms.append(r)
    fecha_inicial = fecha_inicial + timedelta(seconds=r)
    fechas.append(fecha_inicial)

    r = randint(cota_inf_media, cota_sup_media)
    randoms.append(r)
    fecha_inicial = fecha_inicial + timedelta(seconds=r)
    fechas.append(fecha_inicial)

    r = randint(cota_inf_media, cota_sup_media)
    randoms.append(r)
    fecha_inicial = fecha_inicial + timedelta(seconds=r)
    fechas.append(fecha_inicial)

    r = randint(cota_inf_media, cota_sup_media)
    randoms.append(r)
    fecha_inicial = fecha_inicial + timedelta(seconds=r)
    fechas.append(fecha_inicial)

    r = randint(cota_sup_media, cota_sup)
    randoms.append(r)
    fecha_inicial = fecha_inicial + timedelta(seconds=r)
    fechas.append(fecha_inicial)

    r = randint(cota_inf, cota_sup)
    randoms.append(r)
    fecha_inicial = fecha_inicial + timedelta(seconds=r)
    fechas.append(fecha_inicial)



for x in fechas:
    print(x)


print("Mínimo: " + str(min(randoms)))
print("Máximo: " + str(max(randoms)))