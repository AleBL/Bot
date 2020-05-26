# -*- coding: utf-8 -*-

from selenium import webdriver
import time

class Bot:
    def __init__(self):
        nEmpresa = 2710
        nLogin = david.rocha
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver')

    def Login:
        driver.get("https://www.promobank.com.br")
        time.sleep(30)
        iframe = driver.find_element(By.CSS_SELECTOR, "input type="text" name="emp_senha" style="-webkit-text-security: disc;" class="form-control rounded-pill bg-pb-dark-blue text-white login-input border-pb-light-blue" id="loginEmpresa" placeholder="Código da empresa" > Empresa")
        driver.switch_to.frame(Empresa)
        imput.send_keys(nEmpresa)
        iframe = driver.find_element(By.CSS_SELECTOR, "input type="text" name="usu_login" autocomplete="username" class="form-control rounded-pill bg-pb-dark-blue text-white login-input border-pb-light-blue" id="loginUsuario" placeholder="Seu login" > Login")
        driver.switch_to.frame(Login)
        imput.send_keys(nLogin)
