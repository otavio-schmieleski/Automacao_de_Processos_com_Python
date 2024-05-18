from selenium import webdriver
import time
import pyautogui
import os
import shutil

# drive = webdriver.Chrome()
# drive.get('https://br.financas.yahoo.com/quote/%5EBVSP?p=%5EBVSP')
# time.sleep(10)
# drive.find_element('xapth','//*[@id="ybar-sbq"]').click()
# drive.find_element('xpath','//*[@id="ybar-sbq"]').send_keys('ITUB3.SA')
# time.sleep(60)

ROOT_ORIGINAL = "C://Users//otavi//Downloads"
ROOT_DESTINO = "D://unimater//3º Período//Ciências de Dados//Pipeline_python//CSV"

arquivos = os.listdir(ROOT_ORIGINAL)
for arquivo in arquivos:
    if arquivo.endswith('.csv'):
        caminho_original = os.path.join(ROOT_ORIGINAL, arquivo)
        caminho_destino = os.path.join(ROOT_DESTINO, arquivo)
        shutil.move(caminho_original,caminho_destino)