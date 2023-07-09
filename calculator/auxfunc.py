from math import log
from statistics import mean, pstdev

def calculo_f2(dis_ref, dis_pf):
  '''
  + dis_ref: Lista de int. Concentraciones Promedio en el tiempo, del referente
  + dis_pf: Lista de int. Concentraciones Promedio en el tiempo, de la fórmula avealuar   
  '''
  if len(dis_ref) != len(dis_pf):
    print('''La cantidad de datos de disolución del referente deben coincidir 
    con la cantidad de datos de la prueba de formulación.''')
  else:
    n = len(dis_ref)
    diferencias =[(int(dis_ref[f'{i}']) - int(dis_pf[f'{i}']))**2 for i in range(1, n+1)]
    f2 = 50 * log(((1+(sum(diferencias)/n))**-0.5)*100, 10)
    return round(f2,2)