from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_faktorial(numbertest, input, KETERANGAN):
    print("---TEST " + numbertest +" "+ KETERANGAN + "---")
    driver = webdriver.Chrome()

    driver.get("https://qa.putraprima.id")

    print("web bisa terbuka")
    

    driver.implicitly_wait(0.5)

    input_box = driver.find_element(by=By.ID, value="input")
    submit_button = driver.find_element(by=By.ID, value="hitung")
    
    try:
        input_box.send_keys(input)
        print("masukkan input berhasil")
    except:
        print("input yang dimasukkan error") 

    check_integer = input_box.get_attribute('value')
    
    if(isinstance(check_integer, int)):
        print("input benar integer")
    else:
        print("input bukan integer")

    try:
        submit_button.click()
        print("tombol berhasil di klik")
    except:
        print("tombol gagal di klik")


    time.sleep(2)
    message = driver.find_element(by=By.ID, value="result")
    value = message.text
    
    try:    
        assert value == "Faktorial dari 12 adalah: 479001600"
        print("Hasil faktorial sesuai")
    except:
        print("Hasil faktorial tidak sesuai")

    driver.quit()

test_faktorial("PERTAMA", 12, "ANGKA")
test_faktorial("KEDUA", "aku", "HURUF")
test_faktorial("KETIGA", "./", "SIMBOL")
test_faktorial("KEEMPAT", "", "KOSONG")