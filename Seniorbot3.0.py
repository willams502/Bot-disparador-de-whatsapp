from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import time
from random import randint
import urllib
import pandas as pd 
import pyautogui
contatos_df = pd.read_excel(r"C:\Users\Dell\Desktop\sn\Enviar.xlsx")
navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")
time.sleep(4)
while len(navegador.find_elements_by_id("side")) <1:
    time.sleep(1)

    for i,mensagem in enumerate(contatos_df['Mensagem']):
        pessoa = contatos_df.loc[i, "Pessoa"]
        numero = contatos_df.loc[i, "Número"]
        texto = urllib.parse.quote(f"Oi {pessoa}, {mensagem}.")
        link = (f"http://web.whatsapp.com/send?phone=55{numero}&text={texto}")
        sleep(randint(5,8))
        navegador.get(link)
        try:
            while len(navegador.find_elements_by_id("side")) < 1:
                time.sleep(10)

            navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]').send_keys(Keys.ENTER)
            #navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)
        except NoSuchElementException:
            pass

        time.sleep(4)
