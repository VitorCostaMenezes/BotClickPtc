
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


# username = input('Digite o usuário? ')
# senha = input('Digite a sua senha? ')
# limite = int(input('Deseja executar quantas vezes? '))
# CONT_GLOBAL = int(0)
# time.sleep(3)

username = 'ladydipaula1987'
senha = 'Fa158__@@'
limite = int(141)
CONT_GLOBAL = int(0)
time.sleep(3)


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





    time.sleep(5)
    print('0 - tela de login')
    # navegador.maximize_window()
    # time.sleep(2)
    # navegador.execute_script((f"window.scroll(0, 300)"))
    # time.sleep(5)

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

    def clik():
        navegador.execute_script(
            f"document.querySelector('#col1 > td:nth-child(2) > a').removeAttribute('target')")

        navegador.find_element(By.CSS_SELECTOR, '#col1 > td:nth-child(2) > a').click()
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

        # img_quatro_crop.show()
        time.sleep(1)

        img_cinco = Image.open('img/area.png')
        img_cinco_crop = img_cinco.crop((192, 0, 240, 48))
        img_cinco_crop.save('img/cinco.png', quality=95)
        time.sleep(3)

        print('Salvou as imagens')

        # def image_difference(image_1, image_2):
        #     # Salva o shape das imagens
        #     global difference
        #     img1_shape = image_1.shape[:2]
        #     img2_shape = image_2.shape[:2]
        #     # TESTE 1: Compara a estrutura das imagens
        #     if img1_shape == img2_shape:
        #         print("O tamanho das imagens são os mesmos")
        #         # Extrai a diferença de cor entre duas imagens
        #         difference = cv.subtract(image_1, image_2)
        #         # Separa as três cores da imagem
        #         b, g, r = cv.split(difference)
        #         # TESTE 2: Compara as cores das imagens
        #         if cv.countNonZero(b) == 0 and cv.countNonZero(g) == 0 and cv.countNonZero(r) == 0:
        #             print("As cores das imagens são iguais")
        #         else:
        #             print('As cores das imagens são diferentes')
        #
        #             print('---------------------------------------------')
        #             print('---------------------------------------------')
        #
        #     else:
        #         print("As imagens tem tamanhos diferentes")
        #         # Gera uma imagem com a diferença das imagens
        #     # return cv2_imshow(difference)
        #     return difference

        # img1 = cv.imread("/img/principal.png")
        # img2 = cv.imread("/content/opencv/apple.png")

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

        navegador.close()
        time.sleep(2)
        navegador.refresh()



    # image_principal = cv2.imread('img/principal.png')
    # gray_image = cv2.cvtColor(image_principal, cv2.COLOR_BGR2GRAY)
    # histogram_principal = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
    # time.sleep(2)
    #
    # image_um = cv2.imread('img/um.png')
    # gray_image_um = cv2.cvtColor(image_um, cv2.COLOR_BGR2GRAY)
    # histogram_um = cv2.calcHist([gray_image_um], [0], None, [256], [0, 256])
    # time.sleep(2)
    #
    # image_dois = cv2.imread('img/dois.png')
    # gray_image_dois = cv2.cvtColor(image_dois, cv2.COLOR_BGR2GRAY)
    # histogram_dois = cv2.calcHist([gray_image_dois], [0], None, [256], [0, 256])
    # time.sleep(2)
    #
    # image_tres = cv2.imread('img/tres.png')
    # gray_image_tres = cv2.cvtColor(image_tres, cv2.COLOR_BGR2GRAY)
    # histogram_tres = cv2.calcHist([gray_image_tres], [0], None, [256], [0, 256])
    # time.sleep(2)
    #
    # image_quatro = cv2.imread('img/quatro.png')
    # gray_image_quatro = cv2.cvtColor(image_quatro, cv2.COLOR_BGR2GRAY)
    # histogram_quatro = cv2.calcHist([gray_image_quatro], [0], None, [256], [0, 256])
    # time.sleep(2)
    #
    # image_cinco = cv2.imread('img/cinco.png')
    # gray_image_cinco = cv2.cvtColor(image_cinco, cv2.COLOR_BGR2GRAY)
    # histogram_cinco = cv2.calcHist([gray_image_cinco], [0], None, [256], [0, 256])
    #
    # time.sleep(1)
    #
    # c1 = 0
    # i = 0
    # while i < len(histogram_principal) and i < len(histogram_um):
    #     c1 += (histogram_principal[i] - histogram_um[i]) ** 2
    #     i += 1
    # c1 = c1 ** (1 / 2)
    #
    # print(c1)
    #
    #
    # d1 = 0
    # i_dois = 0
    # while i_dois < len(histogram_principal) and i_dois < len(histogram_dois):
    #     d1 += (histogram_principal[i_dois] - histogram_dois[i_dois]) ** 2
    #     i_dois += 1
    # d1 = d1 ** (1 / 2)
    # print(d1)
    #
    # e1 = 0
    # i_tres = 0
    # while i_dois < len(histogram_principal) and i_tres < len(histogram_tres):
    #     e1 += (histogram_principal[i_tres] - histogram_tres[i_tres]) ** 2
    #     i_tres += 1
    # e1 = e1 ** (1 / 2)
    # print(e1)
    #
    #
    #
    # f1 = 0
    # i_quatro = 0
    # while i_dois < len(histogram_principal) and i_quatro < len(histogram_quatro):
    #     f1 += (histogram_principal[i_quatro] - histogram_quatro[i_quatro]) ** 2
    #     i_quatro += 1
    # f1 = f1 ** (1 / 2)
    # print(f1)
    #
    #
    #
    # g1 = 0
    # i_cinco = 0
    # while i_cinco < len(histogram_principal) and i_cinco < len(histogram_cinco):
    #     g1 += (histogram_principal[i_cinco] - histogram_cinco[i_cinco]) ** 2
    #     i_cinco += 1
    # g1 = g1 ** (1 / 2)
    # print(g1)


    # print('inicar historgramas')
    # time.sleep(1)
    #
    # print(histogram_principal)
    # time.sleep(0.2)
    #
    # print(histogram_um)
    # time.sleep(0.2)
    #
    # print(histogram_dois)
    # time.sleep(0.2)
    #
    # print(histogram_tres)
    # time.sleep(0.2)
    #
    # print(histogram_quatro)
    # time.sleep(0.2)
    #
    # print(histogram_cinco)


    #
    # if histogram_principal == histogram_um:
    #     print('A imagem 1 é igual a principal')
    #
    # elif histogram_principal == histogram_dois:
    #     print('A imagem 2 é igual a principal')
    #
    # elif histogram_principal == histogram_tres:
    #     print('A imagem 3 é igual a principal')
    #
    # elif histogram_principal == histogram_quatro:
    #     print('A imagem 4 é igual a principal')
    #
    # elif histogram_principal == histogram_cinco:
    #     print('A imagem 5 é igual a principal')
    #
    # else:
    #     print('NENHUMA CORRESPONDENCIA ENCONTRADA')

    time.sleep(2000)



    if 0 == 0:
        print("captcha text " )


        time.sleep(2)
        navegador.find_element(By.CSS_SELECTOR, '#Captcha2_CaptchaTextBox').send_keys('')
        time.sleep(6)

        navegador.find_element(By.CSS_SELECTOR, '#Button1_input').click()

        print('TELA PORTAL')
        time.sleep(10)

        navegador.find_element(By.CSS_SELECTOR, '#minimizeDiv > li:nth-child(3) > a').click()

        time.sleep(10)

        # navegador.execute_script(
        #     f"document.querySelector('#BasicModulem9_11 > div.panel-body > a').removeAttribute('target')")

        original_window = navegador.current_window_handle

        def clicks():


            time.sleep(10)
            navegador.execute_script((f"window.scroll(0, 200)"))
            time.sleep(5)


            navegador.find_element(By.CSS_SELECTOR, '#BasicModulem9_11 > div.panel-body > a').click()

            time.sleep(10)

            # Close the tab or window
            # navegador.close()
            navegador.switch_to.window(original_window)
            time.sleep(2)

            linkptcstar = 'https://www.star-clicks.com/portal/ads'
            navegador.get(linkptcstar)
            time.sleep(5)


            # navegador.switch_to.window(original_window)

        # time.sleep(5)
        global CONT_GLOBAL
        cont = CONT_GLOBAL

        while cont <= limite:
            clicks()
            cont += 1
            CONT_GLOBAL = cont
            viewcont()
            time.sleep(5)


    else:

        print("task finished with error " + solver.error_code)

        # time.sleep(300000000)

    time.sleep(1)



def check_internet():
    ''' checar conexão de internet '''
    url = 'https://www.star-clicks.com/login'
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
