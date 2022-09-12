#PROGRAMA HECHO POR MATÍAS OTÁROLA Q
#IMPORTACIÓN DE MALLAS EN FORMATO CSV A AUTOCAD

import pandas as pd
from pyautocad import Autocad,APoint

#INSTRUCCIONES:
# 1. DEBE GUARDAR EL ARCHIVO CSV EN LA CARPETA "CSV TO AUTOCAD", LUEGO, DEBE ABRIR EL PROGRAMA EN VISUAL STUDIO CODE Y ESCRIBIR EL NOMBRE DEL ARCHIVO
# 2. ESCRIBA EL NOMBRE DEL ARCHIVO EN "file", DENTRO DEL PARÉNTESIS Y LUEGO DE LA LETRA r.
# 3. EL NOMBRE DEL ARCHIVO DEBE ESTAR ENTRE COMILLAS Y DEBE INCLUIR LA EXTENSIÓN .CSV EJEMPLO: file = pd.read_csv(r"nombrearchivo.csv")

file = pd.read_csv(r"B_2015_02_DEL.csv")

# 4. DEBE CONSIDERAR QUE EL ARCHIVO TENGA COMO NOMBRE DE ENCABEZADO: HOLEID|EAST|NORTH|ELEVATION.
# 5. VERIFIQUE ADEMÁS QUE EL ARCHIVO ESTÁ DELIMITADO POR COMAS "," PARA ELLO, DE CLICK DERECHO EN EL ARCHIVO, ABRIR CON BLOC DE NOTAS Y VERIFICAR,
#    EN EL CASO QUE NO ESTÉ DELIMITADO POR COMAS "," VAYA A EDICIÓN Y REEMPLACE EL CARACTER POR COMAS ",".
# 5. VUELVA A VISUAL STUDIO CODE, PRESIONE CTRL+S PARA GUARDAR LOS CAMBIOS, O BIEN GUARDELOS EN -> ARCHIVO Y GUARDAR.
# 6. ABRIR AUTOCAD Y CREAR UNA NUEVA PESTAÑA DE DIBUJO.
# 7. CORRA EL PROGRAMA EN VISUAL STUDIO CODE HACIENDO CLICK DERECHO Y SELECCIONANDO "EJECUTAR EL ARCHIVO DE PYTHON EN TERMINAL".
# 8. SI APARECE EL MENSAJE "LA MALLA EN FORMATO CSV HA SIDO IMPORTADA A AUTOCAD EXITOSAMENTE..." DEBERÁ IR A AUTOCAD Y HACER ZOOM EXTENS PARA
#    VISUALIZAR LA MALLA. SI ESTE NO APARECE, DEBERÁ REVISAR QUE EL ENCABEZADO DE LOS ARCHIVOS ESTÉ CORRECTO Y QUE ESTÉ DELIMITADO POR COMAS.

# NOTA ADICIONAL PARA ARCHIVOS (2) DE SMARTSHEET
# SI VA A LEER LOS FORMATOS (2) .CSV EN SMARTSHEET, DEBERÁ ABRIR EL PROGRAMA "CSV to AutoCAD(NORTE,ESTE,PISO)".py

#NOTA ADICIONAL INSTALACIÓN LIBRERÍAS DE PYTHON
# PARA INSTALAR LAS LIBRERÍAS DE PYTHON DEBERÁ ESCRIBIR "pip install "nombre librería"" por ejemplo, para instalar pandas: pip install pandas
# y para instalar la de autocad es: pip install pyautocad.

df = pd.DataFrame(file)

x=df["EAST"]
y=df["NORTH"]
z=df["ELEVATION"]

listx=[]
listy=[]
listz=[]


for i in x:
    listx.append(i)
    
for j in y:
    listy.append(j)
    
for k in z:
    listz.append(k)

#pasar a objeto
union = zip(listx,listy,listz)

#pasar de objeto a tupla -> (x,y,z)
coordenadas = list(union)

acad = Autocad()

#p=punto r=radio
def circulo(p,r):
    acad.model.AddCircle(p,r)

def punto(c):
    acad.model.AddPoint(c)
    
#acad.model.AddCircle((x,y,z),r)
#acad.model.AddPoint((x,y,z))
#acad.model.AddLine((x0,y0,z0),(x1,y1,z1))
#(x,y,z) son tuplas, hay que pasar de listas a tuplas

for q in coordenadas:
    puntos=APoint(q)
    circulo(puntos,0.3)
    punto(puntos)

print("La malla en formato CSV ha sido importada a AutoCAD existosamente, presione <Zoom Extents> en AutoCAD para ubicar la malla en el plano")