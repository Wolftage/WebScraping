from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import re

#Declaración de variables
a,b = 'áéíóúü','aeiouu'
transl = str.maketrans(a,b)
keyword = 'Aldo Luévano' #Entrada
keyword = keyword.translate(transl)
fuentes = list()        #Salida
textoCompleto = list()
textoLimpio = list()    #Salida

#Declaracion de funciones----------------------------------------------------------------
def Captura():
    textoExtraido = list()

    html = requests.get(driver.current_url).text.translate(transl)

    soup = BeautifulSoup(html, 'html.parser')
    textoExtraido = soup.get_text().split('\n')

    fuentes.append("Fuente: "+driver.current_url+"\n")
    for i in range(0,len(textoExtraido)):
        if re.search(keyword,textoExtraido[i]):
            textoLimpio.append(textoExtraido[i])

def Busqueda(x):
    x=str(x)
    driver.get(urlBusqueda)
    driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[5]/div[2]/div/div/div[1]/div['+x+']/div[1]/div[1]').click()
    time.sleep(2)
    Captura()


#Apertura de pagina web------------------------------------------------------------------
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
urlBusqueda = 'https://cse.google.com/cse?cx=a7424781cb666474b#gsc.tab=0&gsc.q='+keyword+'&gsc.sort='
driver.get(urlBusqueda)
time.sleep(3)
#-----------------------------------------------------------------------------------------

#Selección y guardado de HTML-------------------------------------------------------------
for i in range(1,10):
    Busqueda(i)
