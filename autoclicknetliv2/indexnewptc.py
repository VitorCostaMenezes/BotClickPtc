import errno
from asyncio import exceptions

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from anticaptchaofficial.recaptchav2proxyless import *
import time
import pyautogui

username = input('Digite o usuário? ')
senha = input('Digite a sua senha? ')
limite = int(input('Deseja executar quantas vezes? '))
CONT_GLOBAL = int(0)
time.sleep(3)


def viewcont ():
    print(CONT_GLOBAL)

def glob():
    navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    link = "https://ptc.newsbp24.com/user/login"
    navegador.get(link)

    def contexto():
        try:
            navegador.execute_script((f"window.scroll(0, 300)"))
            time.sleep(5)

            navegador.execute_script(
                f"document.querySelector('body > div.page-wrapper > section.cmn-section > div > div > div:nth-child(1) > div > div > div > div.col-4.text-end > a').removeAttribute('target')")

            time.sleep(5)

            navegador.find_element_by_css_selector(
                'body > div.page-wrapper > section.cmn-section > div > div > div:nth-child(1) > div > div > div > div.col-4.text-end > a').click()

            time.sleep(60)

            um = navegador.find_element(By.CSS_SELECTOR, '#cap_number_1')
            captcha_um = um.get_attribute('value')

            time.sleep(10)
            dois = navegador.find_element(By.CSS_SELECTOR, '#cap_number_2')
            captcha_dois = dois.get_attribute('value')

            result_captcha = int(captcha_um) + int(captcha_dois)

            time.sleep(5)
            navegador.find_element(By.ID, 'cap_result').send_keys(result_captcha)
            time.sleep(5)
            navegador.find_element(By.ID, 'confirm').click()

            time.sleep(10)

            # global CONT_GLOBAL
            #
            # CONT_GLOBAL =+ 1

        except:

            # global CONT_GLOBAL
            print(CONT_GLOBAL)
            navegador.close()

            time.sleep(10)


    time.sleep(10)
    pyautogui.click(285, 633)

    # Point(x=283, y=633)

    time.sleep(5)
    navegador.execute_script((f"window.scroll(0, 600)"))

    time.sleep(5)
    navegador.find_element(By.CSS_SELECTOR, '[type="username"]').send_keys(username)
    navegador.find_element(By.CSS_SELECTOR, '[type="password"]').send_keys(senha)
    navegador.find_element(By.CSS_SELECTOR, '#remember').click()
    # time.sleep(10)
    navegador.find_element(By.CSS_SELECTOR, '[type=\"submit\"]').click()

    time.sleep(15)
    navegador.maximize_window()
    time.sleep(10)
    navegador.execute_script((f"window.scroll(0, 2000)"))
    time.sleep(5)
    navegador.find_element_by_css_selector('body > div.page-wrapper > section.cmn-section > div > div > a:nth-child(7)').click()
    time.sleep(10)

    # index_position = pyautogui.position()
    # time.sleep(1)
    # print(index_position)

    pyautogui.click(715, 465)

    time.sleep(5)
    global CONT_GLOBAL
    cont = CONT_GLOBAL

    while cont <= limite:
        contexto()
        cont += 1
        CONT_GLOBAL = cont
        viewcont()


def check_internet():
    ''' checar conexão de internet '''
    url = 'https://ptc.newsbp24.com/user/login'
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
        print('Testando a exceção!')
        a = False

        while a != True:
            time.sleep(10)
            print('Teste de conexão!')
            a = check_internet()
            print('Erro de conexxão')


