import os
import platform
import random
import socket
import string
import sys
import time
import webbrowser
import subprocess

# Arch Linux ve diğer Linux terminalleri için kusursuz ANSI Yeşili
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
    """Terminali temizler ve pencere başlığını günceller."""
    sys.stdout.write("\x1b]2;MultiToll-by X Man\x07")
    os.system('clear')

def network_detaylari_al():
    """Hedef bilgisayarın ağ bilgilerini çeker."""
    try:
        host_name = socket.gethostname()
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
    except Exception:
        host_name = "ARCH-TARGET"
        local_ip = "127.0.0.1"
    return host_name, local_ip

def google_chrome_ac():
    print(f"\n{YESIL}[+] Sistemdeki varsayılan tarayıcı tetikleniyor...{RENK_SIFIRLA}")
    webbrowser.open("https://www.google.com")
    time.sleep(1)

def trfootball_ac():
    url = "https://afootbal.my.canva.site/trfootball"
    print(f"\n{YESIL}[+] TRfootball platformuna yönlendiriliyorsunuz...{RENK_SIFIRLA}")
    webbrowser.open(url)
    time.sleep(1)

def gorev_yoneticisi_ac():
    """Arch Linux ortamına uygun görev yöneticisini bulur ve çalıştırır."""
    print(f"\n{YESIL}[+] Görev Yöneticisi / Sistem İzleyici aranıyor...{RENK_SIFIRLA}")
    time.sleep(0.5)
    
    # Arch Linux'ta en yaygın kullanılan izleyiciler (Terminal ve GUI karışık)
    izleyiciler = ['htop', 'bottom', 'top', 'xfce4-taskmanager', 'gnome-system-monitor', 'lxtask']
    baslatildi = False
    
    for arac in izleyiciler:
        # Aracın kurulu olup olmadığını kontrol et
        if subprocess.call(f"type {arac}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0:
            if arac in ['htop', 'bottom', 'top']:
                # Terminal tabanlı olanları mevcut pencerede aç
                os.system(arac)
            else:
                # Grafiksel olanları arka planda aç ki multitool kilitlenmesin
                subprocess.Popen([arac], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            baslatildi = True
            break
            
    if not baslatildi:
        print(f"{KIRMIZI}[!] Sistemde htop veya top bulunamadı!{RENK_SIFIRLA}")
        input("\n[ENTER] Devam et...")

def sistem_bilgisi():
    print(f"\n{YESIL}--- [ DETAYLI HEDEF ANALİZİ ] ---{RENK_SIFIRLA}")
    print(f"Dağıtım (OS)   : Arch Linux / {platform.system()}")
    print(f"Kernel Sürümü  : {platform.release()}")
    print(f"Mimari (Arch)  : {platform.machine()}")
    print(f"Python Core    : {platform.python_version()}")
    input("\n[ENTER] Ana menüye dön...")

def sifre_ureticisi():
    print(f"\n{YESIL}--- [ KRİPTOGRAFİK ŞİFRE ÜRETİCİ ] ---{RENK_SIFIRLA}")
    try:
        uzunluk = int(input("Karakter uzunluğu girin (Örn: 16): "))
        if uzunluk < 4: uzunluk = 4
    except ValueError:
        uzunluk = 12

    karakterler = string.ascii_letters + string.digits + string.punctuation
    sifre = "".join(random.choice(karakterler) for _ in range(uzunluk))
    print(f"\n[>] GÜVENLİ ANAHTAR: {YESIL}{sifre}{RENK_SIFIRLA}")
    input("\n[ENTER] Ana menüye dön...")

def hizli_hesap():
    print(f"\n{YESIL}--- [ MATEMATİKSEL ALGORİTMA ] ---{RENK_SIFIRLA}")
    islem = input("İşlemi girin (Örn: 2 ** 10): ")
    try:
        sonuc = eval(islem, {"__builtins__": None}, {})
        print(f"[>] ÇIKTI: {YESIL}{sonuc}{RENK_SIFIRLA}")
    except Exception:
        print(f"{KIRMIZI}[!] Geçersiz işlem!{RENK_SIFIRLA}")
    input("\n[ENTER] Ana menüye dön...")

def ana_menu():
    ekrani_temizle()
    print(LOGO)
    print(f"{YESIL}[*] Arch Linux çevre birimleri taranıyor...{RENK_SIFIRLA}")
    time.sleep(0.6)
    
    while True:
        host, ip = network_detaylari_al()
        ekrani_temizle()
        print(LOGO)
        
        print("=" * 72)
        print(f" ARCH_HOST : {YESIL}{host}{RENK_SIFIRLA}   |   LOCAL IP : {YESIL}{ip}{RENK_SIFIRLA}")
        print(f" STATUS    : {YESIL}READY{RENK_SIFIRLA}          |   OPERATOR : {YESIL}X Man (Arch Mode){RENK_SIFIRLA}")
        print("=" * 72)
        
        print(f" [{YESIL}1{RENK_SIFIRLA}] Tarayıcıyı Başlat (Google)")
        print(f" [{YESIL}2{RENK_SIFIRLA}] TRfootball Sistemini Aç")
        print(f" [{YESIL}3{RENK_SIFIRLA}] Görev Yöneticisini (Sistem İzleyici) Çalıştır")
        print(f" [{YESIL}4{RENK_SIFIRLA}] İşletim Sistemi / Kernel Analizi")
        print(f" [{YESIL}5{RENK_SIFIRLA}] Kriptografik Güvenli Şifre Üret")
        print(f" [{YESIL}6{RENK_SIFIRLA}] Matematiksel Algoritma / Hesap")
        print(f" [{KIRMIZI}0{RENK_SIFIRLA}] Oturumu Kapat (Exit)")
        print("=" * 72)
        
        secim = input(f"{YESIL}X-Man@Arch:~# {RENK_SIFIRLA}").strip()

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
            print(f"\n{KIRMIZI}[!] Oturum sonlandırıldı. Güvenli çıkış yapıldı.{RENK_SIFIRLA}")
            sys.exit()
        else:
            print(f"\n{KIRMIZI}[!] Bilinmeyen Komut!{RENK_SIFIRLA}")
            time.sleep(0.8)

if __name__ == "__main__":
    try:
        ana_menu()
    except KeyboardInterrupt:
        print(f"\n\n{KIRMIZI}[!] Sinyal kesildi. Çıkılıyor...{RENK_SIFIRLA}")
        sys.exit()