"""Autor: Matheus Lima de Souza Ramires

Resumo: Sistema que converte texto para voz utilizando o modulo pyttsx3 do python
"""

import pyttsx3
import datetime

dthr = datetime.datetime.now().time() #horário brasilia
cidade = 'Brasília'
mensagem_hora = f"São {dthr.hour} horas e {str(dthr.minute)} minutos  "

robo = pyttsx3.init()

if (str(dthr) >= '05:30:00.00' and str(dthr) <= '11:59:59.00'):
    robo.say(f"bom dia! {mensagem_hora} da manhã em {cidade}.")

elif (str(dthr) >= '12:00:00.00' and str(dthr) < '18:00:00.00'):
    robo.say(f"boa tarde. {mensagem_hora} da tarde em {cidade}.")

elif (str(dthr) >= '18:00:00.00' and str(dthr) <= '23:59:59.00'):
    robo.say(f"boa noite. {mensagem_hora} da noite em {cidade}.")

elif (str(dthr) >= '00:00:00.00' and str(dthr) < '05:30:00.00'):
    robo.say(f"boa madrugada. {mensagem_hora} da madrugada em {cidade}.")

robo.runAndWait()