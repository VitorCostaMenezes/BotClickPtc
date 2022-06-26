
# from selenium.webdriver.common.alert import Alert
import os

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from anticaptchaofficial.recaptchav2proxyless import *
from anticaptchaofficial.imagecaptcha import *
from PIL import Image
from selenium.webdriver.support.select import Select
from contextlib import suppress
import time
# Importando bibliotecas
import cv2 as cv
# from google.colab.patches import cv2_imshow
import cv2

from time import sleep
from chave import chave_api

from opencv import orb_sim
import urllib


username = input('Digite o usuário? ')
senha = input('Digite a sua senha? ')
limite = int(input('Deseja executar quantas vezes? '))
limite_gasto = int(input(' !!!! Quantos clicks ja foram realizados hoje?!!!  CASO NÃO TENHA FEITO NENHUM CLICK DIGITE O NUMERO: 0'))
CONT_GLOBAL = limite_gasto
# CONT_GLOBAL = int(0)
time.sleep(3)

# username = ''
# senha = ''
# limite = int(8)
# CONT_GLOBAL = int(0)
# time.sleep(3)

def viewcont ():
    print('CLICKS CONFIRMADOS: ', CONT_GLOBAL)


def glob():

    # options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    # navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    navegador.maximize_window()

    # navegador.set_window_position(450, 1)
    # navegador.set_window_size(400, 700)
    link = "http://www.buxinc.com/index.php?view=login&"
    navegador.get(link)



    time.sleep(8)
    print('0 - tela de login')
    navegador.find_element(By.CSS_SELECTOR, '#uUsername').send_keys(username)
    navegador.find_element(By.CSS_SELECTOR, '#uPassword').send_keys(senha)
    teste_captcha = navegador.find_element(By.CSS_SELECTOR, '#capcha > p > font').text

    print(teste_captcha)
    time.sleep(5)



    try:
        cont = 0
        controler = 2
        while cont < 1:
            try:
                time.sleep(1.5)
                print('Teste - ', controler-1)
                time.sleep(1.5)

                elemento = navegador.find_element(By.CSS_SELECTOR, '#capcha > div:nth-child('+str(controler)+') > span').get_attribute(
                    'innerText')
                elemento_edit = elemento.strip()
                if elemento_edit == teste_captcha:
                    navegador.find_element(By.CSS_SELECTOR, '#capcha > div:nth-child('+str(controler)+') > div').click()
                    cont = cont + 1
                    print('Teste - ', controler-1, ' - ACCEPT')

                controler = controler +1
            except:
                    print('TESTE ERRO: ', controler-1)

    except:
        print('erro geral no try')

    time.sleep(2)
    navegador.execute_script((f"window.scroll(0, 300)"))
    time.sleep(5)

    navegador.find_element(By.CSS_SELECTOR, '#contentWrapper > div > form > fieldset > center:nth-child(8) > button').click()

    time.sleep(6)

    navegador.find_element(By.CSS_SELECTOR, '#menu > ul > li:nth-child(2) > a').click()
    time.sleep(7)

    def clicklink():

        coluna = CONT_GLOBAL +1
        navegador.execute_script(
            f"document.querySelector('#col"+str(coluna)+" > td:nth-child(2) > a').removeAttribute('target')")

        navegador.find_element(By.CSS_SELECTOR, '#col'+str(coluna)+' > td:nth-child(2) > a').click()
        time.sleep(40)

        navegador.switch_to.frame('surftopframe')
        time.sleep(5)


        image_principal = navegador.find_element(By.CSS_SELECTOR, '#timer > img')
        time.sleep(5)
        image_principal.screenshot('img/principal.png')
        image_principal_temp = Image.open('img/principal.png')
        image_principal_temp.save('img/principal.png', quality=95)

        time.sleep(5)
        image_area = navegador.find_element(By.CSS_SELECTOR, '#buttons > ul > li > img')
        image_area.screenshot('img/area.png')
        # image_area_temp = Image.open('img/principal.png')
        # image_area_temp.save('img/principal.png', quality=95)

        time.sleep(5)

        img_um = Image.open('img/area.png')
        img_um_crop = img_um.crop((0, 0, 48, 48))
        img_um_crop.save('img/um.png', quality=95)
        time.sleep(1)

        img_dois = Image.open('img/area.png')
        img_dois_crop = img_dois.crop((48, 0, 96, 48))
        img_dois_crop.save('img/dois.png', quality=95)
        time.sleep(1)

        img_tres = Image.open('img/area.png')
        img_tres_crop = img_tres.crop((96, 0, 144, 48))
        img_tres_crop.save('img/tres.png', quality=95)
        time.sleep(1)

        img_quatro = Image.open('img/area.png')
        img_quatro_crop = img_quatro.crop((144, 0, 192, 48))
        img_quatro_crop.save('img/quatro.png', quality=95)

        time.sleep(1)

        img_cinco = Image.open('img/area.png')
        img_cinco_crop = img_cinco.crop((192, 0, 240, 48))
        img_cinco_crop.save('img/cinco.png', quality=95)
        time.sleep(3)

        print('Salvou as imagens')


        i_p_e = cv.imread("img/principal.png", 0)
        img_principal_edit = cv2.resize(i_p_e, (1200, 1200))

        img_um_e = cv.imread("img/um.png", 0)
        img_um_edit = cv2.resize(img_um_e, (1200, 1200))

        img_dois_e = cv.imread("img/dois.png")
        img_dois_edit = cv2.resize(img_dois_e, (1200, 1200))

        img_tres_e = cv.imread("img/tres.png")
        img_tres_edit = cv2.resize(img_tres_e, (1200, 1200))

        img_quatro_e = cv.imread("img/quatro.png")
        img_quatro_edit  = cv2.resize(img_quatro_e, (1200, 1200))

        img_cinco_e = cv.imread("img/cinco.png")
        img_cinco_edit  = cv2.resize(img_cinco_e, (1200, 1200))


        um = orb_sim(img_principal_edit, img_um_edit)
        dois = orb_sim(img_principal_edit, img_dois_edit)
        tres = orb_sim(img_principal_edit, img_tres_edit)
        quatro = orb_sim(img_principal_edit, img_quatro_edit)
        cinco = orb_sim(img_principal_edit, img_cinco_edit)


        print(um)
        print(dois)
        print(tres)
        print(quatro)
        print(cinco)

        # time.sleep(2)
        # navegador.switch_to.frame('surftopframe')
        time.sleep(5)

        if um >= 0.9:
            navegador.find_element(By.CSS_SELECTOR, '#buttons > map > area:nth-child(1)').click()
        elif dois >= 0.9:
            navegador.find_element(By.CSS_SELECTOR, '#buttons > map > area:nth-child(2)').click()
        elif tres >= 0.9:
            navegador.find_element(By.CSS_SELECTOR, '#buttons > map > area:nth-child(3)').click()
        elif quatro >= 0.9:
            navegador.find_element(By.CSS_SELECTOR, '#buttons > map > area:nth-child(4)').click()
        else:
            navegador.find_element(By.CSS_SELECTOR, '#buttons > map > area:nth-child(5)').click()



        time.sleep(8)

        # link = "http://www.buxinc.com/index.php?view=click&sid=151407T0RnNE1qUTJORE&sid2=15140&siduid=151407&"
        # navegador.get(link)

        navegador.back()
        time.sleep(2)
        navegador.back()
        time.sleep(2)
        navegador.back()
        time.sleep(5)
        navegador.refresh()
        time.sleep(8)


    global CONT_GLOBAL
    cont = CONT_GLOBAL

    while cont <= limite:
        clicklink()
        cont += 1
        CONT_GLOBAL = cont
        viewcont()
        time.sleep(5)

    # clicklink()


    time.sleep(1)



def check_internet():
    ''' checar conexão de internet '''
    url = 'http://www.buxinc.com/index.php?view=login&'
    timeout = 10
    try:
        requests.get(url, timeout=timeout)
        return True
    except Exception as error:
        return False


while CONT_GLOBAL <= limite:
    try:
        glob()
    except Exception as erro:
        print('Teste de erro em except')
        a = False

        while a != True:
            time.sleep(10)
            a = check_internet()
            print('Erro de conexão!')
