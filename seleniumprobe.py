from selenium import webdriver
import os, time

driver = webdriver.Chrome(executable_path=r"C:\Users\CajaCVS\Desktop\notas\chromedriver.exe")
#driver.get("https://web.whatsapp.com/")
#time.sleep(10)

celular = "573012234677"
mensaje = "Mao te saluda desde SELENIUM!!!"
driver.get("https://wa.me/"+celular+"?text="+mensaje)
time.sleep(10)
enviar = driver.find_elements_by_xpath("//*[@id='action-button']")[0]
enviar.click()

driver.close()
