from selenium import webdriver

from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
service = Service(GeckoDriverManager().install())

navegador = webdriver.Firefox(service=service)

navegador.get("https://aluno.universonarrado.com.br/login?returnUrl=%2Fdashboard%3FcontractsSigned%3D1764072221302")

navegador.find_element('xpath','/html/body/div[2]/div/section/section/form/fieldset[1]/div/input').send_keys("zavazza1314@gmail.com")
navegador.find_element('xpath', '/html/body/div[2]/div/section/section/form/fieldset[2]/div/input').send_keys("109710Pj!")
navegador.find_element('xpath', '/html/body/div[2]/div/section/section/form/button').click()