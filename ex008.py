#digite uma distancia em metros e converta para cm e mm
metros = float(input("digite uma distancia em metros: "))
cm = metros * 100
mm = metros * 1000

print(f"a medida de {metros}m corresponde a {cm:.1f}cm e {mm:.1f}mm")
