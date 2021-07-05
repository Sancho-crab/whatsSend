from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas
import pyautogui
import time
import csv

driver = webdriver.Chrome(ChromeDriverManager().install())

def mandarwhatsapp (numero, nombres):

    for i, j in zip(numero, nombres):

        driver.get("https://api.whatsapp.com/send?phone=%d&text=Hola %s, esto es una prueba" % (i,j))
                
        time.sleep(2)

        try:

            coords = pyautogui.locateCenterOnScreen("salir.png")
            pyautogui.click(coords[0], coords[1])
        
        except:
            
            pass
                
        time.sleep(2)

        coords = pyautogui.locateCenterOnScreen("continuarwhatsapp.png")
        pyautogui.click(coords[0], coords[1])

        time.sleep(2)


        coords = pyautogui.locateCenterOnScreen("usarwhatsappweb.png")
        pyautogui.click(coords[0], coords[1])

        time.sleep(8)

        coords = pyautogui.locateCenterOnScreen("send.png")
        pyautogui.click(coords[0], coords[1])

        time.sleep(2)

colnames = ['Nombre', 'Telf']
data = pandas.read_csv('mandar.csv', names = colnames)

nombres = data.Nombre.tolist()
numeros = data.Telf.tolist()

mandarwhatsapp(numeros, nombres)