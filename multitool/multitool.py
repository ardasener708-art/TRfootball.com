import os
import platform
import random
import socket
import string
import sys
import time
import webbrowser
import subprocess

# Windows terminali için başlık (Title) ve renk ayarı
if os.name == 'nt':
    os.system('title MultiToll-by X Man')
    os.system('color 2')

# ANSI Renk Kodları
YESIL = "\033[92m"
KIRMIZI = "\033[91m"
MAVI = "\033[94m"
RENK_SIFIRLA = "\033[0m"

# Fasciat ASCII Sanatı Logo
LOGO = YESIL + """
 $$$$$$\                               $$\            $$\               
$$  __$$\                              \__|           $$ |              
$$ /  \__|$$$$$$$\  $$$$$$\   $$$$$$$\ $$\  $$$$$$\ $$$$$$\   $$\   $$\ 
$$$$\    $$  _____|$$  __$$\ $$  _____|$$ | \____$$\\_$$  _|  $$ |  $$ |
$$  _|   \$$$$$$\  $$ /  $$ |$$ /      $$ | $$$$$$$ | $$ |    $$ |  $$ |
$$ |      \____$$\ $$ |  $$ |$$ |      $$ |$$  __$$ | $$ |$$\ $$ |  $$ |
$$ |     $$$$$$$  |\$$$$$$  |\$$$$$$$\ $$ |\$$$$$$$ | \$$$$  |\$$$$$$$ |
\__|     \_______/  \______/  \_______|\__| \_______|  \____/  \____$$ |
                                                              $$\   $$ |
                                                              \$$$$$$  |
                                                               \______/ 
""" + RENK_SIFIRLA

def ekrani_temizle():
    """Terminal ekranını temizler, başlığı ve rengi korur."""
    if os.name == 'nt':
        os.system('cls')
        os.system('title MultiToll-by X Man')
        os.system('color 2')
    else:
        sys.stdout.write("\x1b]2;MultiToll-by X Man\x07")
        os.system('clear')

def network_detaylari_al():
    """Hacker tarzı Local IP ve Host Name tespiti yapar."""
    try:
        host_name = socket.gethostname()
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
    except Exception:
        host_name = "UNKNOWN-HOST"
        local_ip = "127.0.0.1"
    return host_name, local_ip

def google_chrome_ac():
    print(f"\n{YESIL}[+] Google Chrome tetikleniyor...{RENK_SIFIRLA}")
    webbrowser.open("https://www.google.com")
    time.sleep(1)

def trfootball_ac():
    url = "https://afootbal.my.canva.site/trfootball"
    print(f"\n{YESIL}[+] TRfootball veri tabanına bağlanılıyor...{RENK_SIFIRLA}")
    webbrowser.open(url)
    time.sleep(1)

def gorev_yoneticisi_ac():
    """İşletim sistemine göre Görev Yöneticisini tetikler."""
    print(f"\n{YESIL}[+] Görev Yöneticisi başlatılıyor...{RENK_SIFIRLA}")
    time.sleep(0.5)
    
    if os.name == 'nt':
        # Windows için Task Manager
        os.system('taskmgr')
    else:
        # Arch Linux ve diğer Linux dağıtımları için sistem izleyici tespiti
        linux_task_managers = ['htop', 'gnome-system-monitor', 'xfce4-taskmanager', 'lxtask', 'top']
        baslatildi = False
        
        for tm in linux_task_managers:
            # Komutun sistemde kurulu olup olmadığını kontrol et
            if subprocess.call(f"type {tm}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0:
                if tm in ['htop', 'top']:
                    # Terminal tabanlı olanları mevcut terminalde çalıştır
                    os.system(tm)
                else:
                    # Grafiksel olanları arka planda çalıştır ki terminal kilitlenmesin
                    subprocess.Popen([tm], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                baslatildi = True
                break
        
        if not baslatildi:
            print(f"{KIRMIZI}[!] Sistemde uygun bir görev yöneticisi (htop, top vb.) bulunamadı!{RENK_SIFIRLA}")
            input("\n[ENTER] Devam et...")

def sistem_bilgisi():
    print(f"\n{YESIL}--- [ SİSTEM ANALİZİ ] ---{RENK_SIFIRLA}")
    print(f"OS/Kernel      : {platform.system()} {platform.release()}")
    print(f"Mimari (Arch)  : {platform.machine()}")
    print(f"Python Core    : {platform.python_version()}")
    input("\n[ENTER] Ana menüye dön...")

def sifre_ureticisi():
    print(f"\n{YESIL}--- [ GÜVENLİ ŞİFRE ÜRETİCİ ] ---{RENK_SIFIRLA}")
    try:
        uzunluk = int(input("Karakter uzunluğu girin (Örn: 16): "))
        if uzunluk < 4:
            uzunluk = 4
    except ValueError:
        uzunluk = 12

    karakterler = string.ascii_letters + string.digits + string.punctuation
    sifre = "".join(random.choice(karakterler) for _ in range(uzunluk))
    
    print(f"\n[+] Şifre oluşturuluyor...")
    time.sleep(0.5)
    print(f"[>] GÜVENLİ VERİ: {YESIL}{sifre}{RENK_SIFIRLA}")
    input("\n[ENTER] Ana menüye dön...")

def hizli_hesap():
    print(f"\n{YESIL}--- [ MATEMATİKSEL ALGORİTMA ] ---{RENK_SIFIRLA}")
    islem = input("İşlemi girin (Örn: 512 * 2): ")
    try:
        sonuc = eval(islem, {"__builtins__": None}, {})
        print(f"[>] ÇIKTI: {YESIL}{sonuc}{RENK_SIFIRLA}")
    except Exception:
        print(f"{KIRMIZI}[!] Geçersiz sözdizimi / Hata!{RENK_SIFIRLA}")
    input("\n[ENTER] Ana menüye dön...")

def ana_menu():
    ekrani_temizle()
    print(LOGO)
    print(f"{YESIL}[*] Sistem mimarisi ve ağ arayüzleri taranıyor...{RENK_SIFIRLA}")
    time.sleep(0.7)
    
    while True:
        host, ip = network_detaylari_al()
        ekrani_temizle()
        print(LOGO)
        
        # Hacker Tarzı Bilgi Paneli
        print("=" * 72)
        print(f" HOSTNAME : {YESIL}{host}{RENK_SIFIRLA}   |   LOCAL IP : {YESIL}{ip}{RENK_SIFIRLA}")
        print(f" STATUS   : {YESIL}ONLINE{RENK_SIFIRLA}         |   TARGET   : {YESIL}MultiToll-by X Man{RENK_SIFIRLA}")
        print("=" * 72)
        
        print(f" [{YESIL}1{RENK_SIFIRLA}] Google Chrome'u Çalıştır")
        print(f" [{YESIL}2{RENK_SIFIRLA}] TRfootball Sistemine Sız / Aç")
        print(f" [{YESIL}3{RENK_SIFIRLA}] Görev Yöneticisini (Task Manager) Tetikle")
        print(f" [{YESIL}4{RENK_SIFIRLA}] Sistem Donanım Analizi")
        print(f" [{YESIL}5{RENK_SIFIRLA}] Kriptografik Şifre Üret")
        print(f" [{YESIL}6{RENK_SIFIRLA}] Hızlı Algoritma / Hesap")
        print(f" [{KIRMIZI}0{RENK_SIFIRLA}] Bağlantıyı Kopar (Çıkış)")
        print("=" * 72)
        
        secim = input(f"{YESIL}X-Man@Terminal:~# {RENK_SIFIRLA}").strip()

        if secim == "1":
            google_chrome_ac()
        elif secim == "2":
            trfootball_ac()
        elif secim == "3":
            gorev_yoneticisi_ac()
        elif secim == "4":
            sistem_bilgisi()
        elif secim == "5":
            sifre_ureticisi()
        elif secim == "6":
            hizli_hesap()
        elif secim == "0":
            print(f"\n{KIRMIZI}[!] Oturum kapatılıyor... Güvenli çıkış yapıldı.{RENK_SIFIRLA}")
            sys.exit()
        else:
            print(f"\n{KIRMIZI}[!] Bilinmeyen komut!{RENK_SIFIRLA}")
            time.sleep(1)

if __name__ == "__main__":
    try:
        ana_menu()
    except KeyboardInterrupt:
        print(f"\n\n{KIRMIZI}[!] Sinyal kesildi. Çıkılıyor...{RENK_SIFIRLA}")
        sys.exit()