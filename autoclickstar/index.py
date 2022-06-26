from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from anticaptchaofficial.recaptchav2proxyless import *
import time
from chave import chave_api


username = input('Digite o usuário? ')
senha = input('Digite a sua senha? ')
limite = int(input('Deseja executar quantas vezes? '))
CONT_GLOBAL = int(0)
time.sleep(3)

# username = ''
# senha = ''
# limite = int(100)
# CONT_GLOBAL = int(0)
# time.sleep(3)


def viewcont ():
    print('CLICKS CONFIRMADOS: ', CONT_GLOBAL)


def glob():

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    # navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # navegador.set_window_position(450, 1)
    # navegador.set_window_size(400, 700)
    link = "https://nettli.com/login"
    navegador.get(link)

    def contexto():
        try:
            print('5 - scroll em PTC')
            navegador.execute_script((f"window.scroll(0, 200)"))
            time.sleep(10)

            navegador.execute_script(
                f"document.querySelector('body > div.page-wrapper > section.cmn-section > div > div > div > div > div > div > table > tbody > tr:nth-child(1) > td:nth-child(2) > a').removeAttribute('target')")

            time.sleep(10)

            navegador.find_element_by_css_selector(
                'body > div.page-wrapper > section.cmn-section > div > div > div > div > div > div > table > tbody > tr:nth-child(1) > td:nth-child(2) > a').click()

            print('6 - tela propaganda / incio dos 60 segundo de espera')

            time.sleep(60)

            try:
                navegador.execute_script((f"window.scroll(0, -300)"))
                time.sleep(1)

                um = navegador.find_element(By.CSS_SELECTOR, '#cap_number_1')
                captcha_um = um.get_attribute('value')
                print('6.1 - cap val 1')
                time.sleep(5)

                navegador.execute_script((f"window.scroll(0, -300)"))
                time.sleep(1)
                dois = navegador.find_element(By.CSS_SELECTOR, '#cap_number_2')
                captcha_dois = dois.get_attribute('value')
                print('6.2 - cap val 2')

                result_captcha = int(captcha_um) + int(captcha_dois)

                time.sleep(5)

                navegador.execute_script((f"window.scroll(0, -300)"))
                time.sleep(1)
                navegador.find_element(By.ID, 'cap_result').send_keys(result_captcha)
                print('6.3 - insert result')

                time.sleep(5)

                navegador.execute_script((f"window.scroll(0, -300)"))
                time.sleep(1)
                navegador.find_element(By.ID, 'confirm').click()
                print('6.4 - confirm result')

            except:
                navegador.back()
                print('6.ERROR - retornou para a pagina de linkPTC')

            # time.sleep(2)
            # navegador.set_window_size(750, 700)
            # time.sleep(2)
            #
            # navegador.set_window_size(400, 700)

            time.sleep(3)

            linkptc = "https://nettli.com/user/ptc"
            navegador.get(linkptc)
            # CONT_GLOBAL + 1
            time.sleep(10)

        except:

            # contexto()
            print('CLICKS CONFIRMADOS: ', CONT_GLOBAL)
            navegador.close()

    time.sleep(10)
    print('0 - tela de login')
    navegador.execute_script((f"window.scroll(0, 600)"))
    time.sleep(5)

    navegador.find_element(By.CSS_SELECTOR, '[type="username"]').send_keys(username)
    navegador.find_element(By.CSS_SELECTOR, '[type="password"]').send_keys(senha)

    # navegador.find_element(By.CSS_SELECTOR, '[type=\"submit\"]').click()
    chave_captcha = navegador.find_element(By.CLASS_NAME, 'g-recaptcha').get_attribute('data-sitekey')

    solver = recaptchaV2Proxyless()
    solver.set_verbose(1)
    solver.set_key(chave_api)
    solver.set_website_url(link)
    solver.set_website_key(chave_captcha)

    resposta = solver.solve_and_return_solution()

    if resposta != 0:
    # if 0 == 0:

        print(resposta)
        navegador.execute_script(f"document.getElementById('g-recaptcha-response').innerHTML = '{resposta}'")
        navegador.find_element(By.CLASS_NAME, 'g-recaptcha').click()
        # time.sleep(30)

        navegador.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

        print('1 - dasboard')
        time.sleep(10)

        navegador.maximize_window()
        time.sleep(10)
        navegador.execute_script((f"window.scroll(0, 2000)"))
        print('2 - scroll em dasboard')
        time.sleep(10)

        navegador.find_element_by_css_selector('body > div.page-wrapper > section.cmn-section > div > div > a:nth-child(6)').click()
        print('3 Mudando para tela PTC')
        time.sleep(10)

        time.sleep(5)
        global CONT_GLOBAL
        cont = CONT_GLOBAL

        while cont <= limite:
            contexto()
            cont += 1
            CONT_GLOBAL = cont
            viewcont()


    else:
        print(solver.err_string)

    time.sleep(1)


def check_internet():
    ''' checar conexão de internet '''
    url = 'https://nettli.com/login'
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
