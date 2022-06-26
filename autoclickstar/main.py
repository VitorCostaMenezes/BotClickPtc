
# from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from anticaptchaofficial.recaptchav2proxyless import *
from anticaptchaofficial.imagecaptcha import *
import time
from chave import chave_api


username = input('Digite o usuário? ')
senha = input('Digite a sua senha? ')
limite = int(input('Deseja executar quantas vezes? '))
CONT_GLOBAL = int(0)
time.sleep(3)

# username = 'ladydipaula1987@gmail.com'
# senha = 'Fa158__@@'
# # limite = int(141)
# limite = int(input('Deseja executar quantas vezes? '))

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


    link = "https://www.star-clicks.com/login"
    navegador.get(link)


    time.sleep(8)
    print('0 - tela de login')
    time.sleep(5)

    navegador.find_element(By.CSS_SELECTOR, '#Email').send_keys(username)
    navegador.find_element(By.CSS_SELECTOR, '#Password').send_keys(senha)
    time.sleep(2)
    navegador.execute_script((f"window.scroll(0, 300)"))
    time.sleep(5)
    imagem = navegador.find_element(By.CSS_SELECTOR, '#Captcha2_CaptchaImage')
    time.sleep(2)
    imagem.screenshot('image.jpg')
    time.sleep(5)

    solver = imagecaptcha()
    solver.set_verbose(1)
    solver.set_key(chave_api)

    solver.set_soft_id(0)

    captcha_text = solver.solve_and_return_solution('image.jpg')

    if captcha_text != 0:
        print("captcha text " + captcha_text)


        time.sleep(2)
        navegador.find_element(By.CSS_SELECTOR, '#Captcha2_CaptchaTextBox').send_keys(captcha_text)
        time.sleep(6)

        navegador.find_element(By.CSS_SELECTOR, '#Button1_input').click()

        print('TELA PORTAL')
        time.sleep(10)

        navegador.find_element(By.CSS_SELECTOR, '#minimizeDiv > li:nth-child(3) > a').click()

        time.sleep(10)

        original_window = navegador.current_window_handle

        def clicks():


            time.sleep(10)
            navegador.execute_script((f"window.scroll(0, 200)"))
            time.sleep(5)


            navegador.find_element(By.CSS_SELECTOR, '#BasicModulem9_11 > div.panel-body > a').click()
            time.sleep(10)

            navegador.switch_to.window(original_window)
            time.sleep(2)

            linkptcstar = 'https://www.star-clicks.com/portal/ads'
            navegador.get(linkptcstar)
            time.sleep(5)

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
