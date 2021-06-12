from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import urllib

pyautogui.alert("Eu sou o SeniorBot e Vou começar a trabalhar.")

contatos_df = pd.read_excel("D:\Seniorbot 2.4 Finalmente funcionou\Enviar.xlsx")
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
        time.sleep(5)
        navegador.get(link)
        try:
            while len(navegador.find_elements_by_id("side")) < 1:
                time.sleep(10)
            navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)
        except NoSuchElementException:
            pass

        time.sleep(4)
