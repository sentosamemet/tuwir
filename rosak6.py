
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

options = {
    'proxy': {
        'http': 'http://f8b63c8e258036c5d467__cr.ca:8ce45793d5cf918a@gw.dataimpulse.com:10006',
        'https': 'http://f8b63c8e258036c5d467__cr.ca:8ce45793d5cf918a@gw.dataimpulse.com:10006',
        'no_proxy': 'localhost,127.0.0.1'
    }
}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--verbose")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--window-size=1920, 1200")
# Hapus '--headless' untuk melihat apakah ekstensi berjalan dengan benar dalam mode normal
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--disable-background-networking")  # Mencegah koneksi jaringan di latar belakang
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument("--disable-client-side-phishing-detection")  # Nonaktifkan deteksi phishing
chrome_options.add_argument("--disable-default-apps")  # Nonaktifkan aplikasi bawaan Chrome
chrome_options.add_argument("--disable-features=NetworkPrediction")  # Nonaktifkan prediksi jaringan
chrome_options.add_argument("--disable-sync")  # Nonaktifkan sinkronisasi
chrome_options.add_argument("--metrics-recording-only")  # Nonaktifkan pengumpulan data
chrome_options.add_argument("--safebrowsing-disable-auto-update")  # Nonaktifkan pembaruan otomatis Safe Browsing
chrome_options.add_argument("--disable-component-update")  # Nonaktifkan pembaruan komponen
chrome_options.add_argument("--disable-domain-reliability")  # Nonaktifkan keandalan domain

driver = webdriver.Chrome(seleniumwire_options=options, options=chrome_options)

driver.get("https://sepolia-faucet.pk910.de/#/mine/89baa734-8bbc-48e4-9b9e-087f38859fcf")
time.sleep(50000)

div_element = driver.find_element(By.CLASS_NAME, "col-3")
content_text = div_element.text
print(content_text)

#WAKTU MENUNGGU MINING SELESAI
time.sleep(15000)

# Tutup browser
driver.quit()
