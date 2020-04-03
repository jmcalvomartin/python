# -*- coding: utf-8 -*-

import pymsteams
import xlrd
import time
from random import randint

url = "" #Ponemos el link de nuestro Webhook

preguntas=("preguntas.xlsx")
excel = xlrd.open_workbook(preguntas) 
hoja = excel.sheet_by_index(0) 

myTeamsMessage = pymsteams.connectorcard(url)
# Creamos una sección
Section = pymsteams.cardsection()

# Titulo de la sección
Section.title("Preguntas de Matemáticas")

# Añadimos la informaciónd e la actividad
Section.activityTitle("Responde a las preguntas lo más rápido que puedas")
Section.activitySubtitle("Empezamos en 10 segundos")

# Ponemos una imagen 
Section.addImage("https://blog.tcea.org/wp-content/uploads/2019/09/question_mark_PNG128.png", ititle="Preguntas")

# conectamos la sección que hemos creado con el Mensaje
myTeamsMessage.addSection(Section)

# Añadimo el texto al mensaje
myTeamsMessage.text("Actividad de preguntas en nuestro canal de Microsoft Teams")

# Enviamos a Teams
myTeamsMessage.send()
time.sleep(10)

for q in range (hoja.nrows):
    
    alumno=randint(0.10)
    myTeamsMessage = pymsteams.connectorcard(url)
    # create the section
    myMessageSection = pymsteams.cardsection()

    # Añadimos las preguntas celda por celda, si queremos aleatorio los nombres debemos sustituir la q de la siguiente liena por la variable alumno
    myMessageSection.title("Esta pregunta es para: " + str(hoja.cell_value(q, 1))) 
    myMessageSection.activityTitle(hoja.cell_value(q, 0))
    myMessageSection.activitySubtitle("El tiempo para responder es " + str(hoja.cell_value(q, 2)) + " segundos")
    
    # Añadimos las preguntas y el texto del tiempo a la sección
    myTeamsMessage.addSection(myMessageSection)
    # Colocamos un texto al mensaje
    myTeamsMessage.text("Vamos a por la pregunta " + str(q + 1))

    # Envio a Microsoft Teams
    myTeamsMessage.send()
    time.sleep(int(hoja.cell_value(q, 2)))
    
    