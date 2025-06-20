from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service # Menggunakan Service untuk Firefox
from selenium.webdriver.firefox.options import Options # Menggunakan Options untuk Firefox
import time

options = {
    'proxy': {
        'http': 'http://2766f184a8ea3245eeeb__cr.us:c586aaf043d69e45@gw.dataimpulse.com:10101',
        'https': 'https://2766f184a8ea3245eeeb__cr.us:c586aaf043d69e45@gw.dataimpulse.com:10101',
        'no_proxy': 'localhost,127.0.0.1'
    }
}

# Menggunakan FirefoxOptions alih-alih ChromeOptions
firefox_options = Options()

# Opsi headless untuk Firefox
firefox_options.add_argument("--headless")
firefox_options.add_argument("--window-size=1920, 1200") # Ukuran jendela

# Argumen yang umumnya aman dan bermanfaat untuk Firefox headless
# Beberapa argumen Chrome mungkin tidak berlaku atau memiliki sintaks yang berbeda di Firefox
firefox_options.add_argument("--disable-gpu") # Berguna untuk headless
firefox_options.add_argument("--no-sandbox") # Penting untuk lingkungan Linux/Docker
firefox_options.add_argument("--disable-dev-shm-usage") # Penting untuk lingkungan Linux/Docker
firefox_options.add_argument("--mute-audio") # Mematikan audio
firefox_options.add_argument("--private") # Mode penjelajahan pribadi (incognito)
# Untuk memblokir koneksi tertentu di Firefox, Anda mungkin perlu menggunakan preferensi
# atau mengandalkan selenium-wire untuk filter request.
# Argumen spesifik seperti --disable-extensions atau --disable-default-apps
# umumnya ditangani secara berbeda di Firefox atau tidak diperlukan untuk headless.

# Contoh setting preferensi Firefox (mirip dengan yang Anda inginkan di Chrome)
# Untuk memblokir koneksi ke Google Optimization Guide, Anda mungkin perlu lebih spesifik
# atau menggunakan selenium-wire untuk mencegat dan memblokir request.
# Contoh preferensi (tidak semua ada padanan langsung dengan Chrome):
firefox_options.set_preference("dom.push.enabled", False)
firefox_options.set_preference("media.autoplay.default", 5) # 5 = always ask (or 2 = block all)
firefox_options.set_preference("browser.safeBrowse.malware.enabled", False)
firefox_options.set_preference("browser.safeBrowse.phishing.enabled", False)
firefox_options.set_preference("network.cookie.cookieBehavior", 1) # 1 = block all 3rd party, 0 = allow all, 2 = block all
firefox_options.set_preference("geo.enabled", False) # Nonaktifkan geolokasi

# Jika GeckoDriver tidak di PATH, Anda bisa menentukannya di sini
# Misalnya: service = Service(executable_path='/usr/local/bin/geckodriver')
# Jika sudah di /usr/local/bin/ (sesuai skrip instalasi), tidak perlu ditentukan.
# service = Service(executable_path='/usr/local/bin/geckodriver') # Hapus komentar jika perlu

# Inisialisasi WebDriver dengan Firefox
# Perhatikan bahwa 'options' untuk proxy diberikan langsung ke konstruktor webdriver.Firefox,
# dan argumen browser diberikan melalui 'options=firefox_options'.
driver = webdriver.Firefox(seleniumwire_options=options, options=firefox_options) # , service=service) # Hapus komentar service jika Anda menggunakannya

driver.get("https://sepolia-faucet.pk910.de/#/mine/6740fd2a-2c2d-4099-aeed-3165e6269ef4")
time.sleep(50000)

div_element = driver.find_element(By.CLASS_NAME, "col-3")
content_text = div_element.text
print(content_text)

# WAKTU MENUNGGU MINING SELESAI
time.sleep(15000)

# Tutup browser
driver.quit()
