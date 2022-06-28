import errno
from asyncio import exceptions

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from anticaptchaofficial.recaptchav2proxyless import *
import time
# import pyautogui

username = input('Digite o usuário? ')
senha = input('Digite a sua senha? ')
limite = int(input('Deseja executar quantas vezes? '))
CONT_GLOBAL = int(0)
time.sleep(2)
# username = ''
# senha = ''
# limite = 10
# CONT_GLOBAL = int(0)
# time.sleep(1)
print('carregou o codigo - 1')

def viewcont ():
    print(CONT_GLOBAL)

def glob():
    # options = webdriver.ChromeOptions()
    # options.add_argument("--headless")

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("disable-notifications")
    chrome_prefs = {}
    options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"popups": 0}
    navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    navegador.set_window_position(1, 1)
    navegador.set_window_size(400, 700)
    link = "https://ptc.newsbp24.com/user/login"
    navegador.get(link)
    print('carregou broser - 2')

    time.sleep(10)
    allow = False

    while allow == False:
        try:

            # navegador.find_element_by_css_selector(
            #     'body > div.cookies-card.text-center > div.cookies-card__btn.mt-4 > a').click()
            navegador.find_element(By.CSS_SELECTOR, 'body > div.cookies-card.text-center > div.cookies-card__btn.mt-4 > a').click()
            print('clicou em ALLOW - 3')
            allow = True
            time.sleep(2)
        except:
            print('NÃO clicou em ALLOW - 3')
            time.sleep(2)

            allow == False
    # time.sleep(3000000)
    def contexto():
        try:
            print('Tela ptc - 13')

            navegador.execute_script((f"window.scroll(0, 300)"))
            time.sleep(5)
            print('Scroll em tela ptc - 14')

            navegador.execute_script(
                f"document.querySelector('body > div.page-wrapper > section.cmn-section > div > div > div:nth-child(1) > div > div > div > div.col-4.text-end > a').removeAttribute('target')")

            time.sleep(5)

            navegador.find_element(By.CSS_SELECTOR, 'body > div.page-wrapper > section.cmn-section > div > div > div:nth-child(1) > div > div > div > div.col-4.text-end > a').click()

            print('Tela de propaganda 60 segundos de espera - 15')

            time.sleep(60)
            print('Final do time de 60s - 16')

            um = navegador.find_element(By.CSS_SELECTOR, '#cap_number_1')
            captcha_um = um.get_attribute('value')

            time.sleep(5)
            dois = navegador.find_element(By.CSS_SELECTOR, '#cap_number_2')
            captcha_dois = dois.get_attribute('value')

            result_captcha = int(captcha_um) + int(captcha_dois)

            time.sleep(5)
            navegador.find_element(By.ID, 'cap_result').send_keys(result_captcha)
            print('Inseriu resultado do verificador - 17')

            time.sleep(5)
            navegador.find_element(By.ID, 'confirm').click()
            print('Confirmou o resultado - 18')

            time.sleep(10)

            time.sleep(5)
            global CONT_GLOBAL
            cont = CONT_GLOBAL


            cont += 1
            CONT_GLOBAL = cont
            print('Incrementou')
            viewcont()

            # global CONT_GLOBAL
            #
            # CONT_GLOBAL =+ 1
            print('retorno  à Tela ptc- 19')

        except:
            print('Ocorreu um erro e entrou em except - 15')

            # global CONT_GLOBAL
            print(CONT_GLOBAL)
            navegador.close()

            time.sleep(10)


    time.sleep(2)
    # pyautogui.click(285, 633)
    #
    # # Point(x=283, y=633)
    #
    # time.sleep(5)
    navegador.execute_script((f"window.scroll(0, 600)"))
    print('fez o scroll para tela login - 4')
    time.sleep(5)
    navegador.find_element(By.CSS_SELECTOR, '[type="username"]').send_keys(username)
    navegador.find_element(By.CSS_SELECTOR, '[type="password"]').send_keys(senha)
    navegador.find_element(By.CSS_SELECTOR, '#remember').click()
    # time.sleep(10)
    navegador.find_element(By.CSS_SELECTOR, '[type=\"submit\"]').click()
    print('fez login para entrar no dashboard - 5')
    # time.sleep(15)
    # navegador.maximize_window()
    time.sleep(10)
    print('tela dasboard - 6')
    navegador.execute_script((f"window.scroll(0, 2000)"))
    print('cscroll em dasboard - 7')
    # time.sleep(3)
    # navegador.execute_script((f"window.scroll(0, -150)"))

    time.sleep(5)
    navegador.find_element(By.CSS_SELECTOR,'body > div.page-wrapper > section.cmn-section > div > div > a:nth-child(7)').click()
    print('clicou no elemento dasboard - 8')
    time.sleep(8)

    navegador.set_window_size(750, 700)
    time.sleep(2)
    print('redimensionamento 1 - 9')
    navegador.set_window_size(400, 700)
    print('redimensionamento 2 - 10')



    # try:
    #     # navegador.find_element_by_css_selector('<div id="dismiss-button" class="btn skip" aria-label="Close ad" role="button" tabindex="0"><div><svg viewBox="0 0 48 48" fill="#FFF"><path d="M38 12.83L35.17 10 24 21.17 12.83 10 10 12.83 21.17 24 10 35.17 12.83 38 24 26.83 35.17 38 38 35.17 26.83 24z"></path><path d="M0 0h48v48H0z" fill="none"></path></svg></div></div>').click()
    #     navegador.find_element_by_css_selector('<div><svg viewBox="0 0 48 48" fill="#FFF"><path d="M38 12.83L35.17 10 24 21.17 12.83 10 10 12.83 21.17 24 10 35.17 12.83 38 24 26.83 35.17 38 38 35.17 26.83 24z"></path><path d="M0 0h48v48H0z" fill="none"></path></svg></div>').click()
    #     # navegador.find_element_by_tag_name('path').click()
    # except:
    #     print('except')
    #     navegador.find_element_by_css_selector(
    #         '<div class="ns-5o7sp-e-12 button-common close-button" id="dismiss-button" x-ns-5o7sp-e="12" x-overflow-forbidden="xy" aria-label="Close ad" role="button" tabindex="0"><div class="ns-5o7sp-e-13" x-ns-5o7sp-e="13" x-overflow-forbidden="xy"><span class="ns-5o7sp-e-14" dir="auto" x-ns-5o7sp-e="14" x-score="1">Close</span></div></div>').click()

        # print('segue normal')
    # index_position = pyautogui.position()
    # time.sleep(1)
    # print(index_position)

    # pyautogui.click(715, 465)
    #
    time.sleep(5)
    global CONT_GLOBAL
    cont = CONT_GLOBAL



    while cont <= limite:
        contexto()
        # cont += 1
        # CONT_GLOBAL = cont
        # print('Incrementou - 12')
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


while CONT_GLOBAL < limite:
    try:
        glob()
    except Exception as erro:
        print('Teste de exceção!')
        a = False

        while a != True:
            print('Testando a conexão!')
            time.sleep(10)
            a = check_internet()
            print('erro de conexxão')



