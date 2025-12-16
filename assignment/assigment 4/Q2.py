km_to_m = lambda km: km * 1000
m_to_cm = lambda m: m * 100
cm_to_mm = lambda cm: cm * 10
feet_to_inches = lambda feet: feet * 12
inches_to_cm = lambda inches: inches * 2.54


def distance_converter(distance,conversion_type,func):
    result = func(distance)
    print(f"{distance} {conversion_type} = {result}")

distance = float(input("Enter distance value: "))

print("\nconversions:")
distance_converter(distance,"km_to_m", km_to_m)
distance_converter(distance,"m_to_cm", m_to_cm)
distance_converter(distance,"cm_to_mm", cm_to_mm)
distance_converter(distance,"feet_to_inches", feet_to_inches)
distance_converter(distance,"inches_to_cm", inches_to_cm)