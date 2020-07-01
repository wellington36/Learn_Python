from math import sin 
from math import cos 
from math import tan 
from math import radians

a = float(input('Digite um ângulo: '))

print('sen{} = {:.3f} ; cos{} = {:.3f} e tan{} = {:.3f}'.format(a, sin(radians(a)), a, cos(radians(a)), a, tan(radians(a))))
