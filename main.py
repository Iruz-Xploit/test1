import requests, threading, datetime, sys, os, time
import colorama 
from colorama import Fore, Back, Style


def main():
    global auth, maxerr, api, pos, dely
    os.system('cls' if os.name == 'nt' else 'clear')
    print( 'SCRIPP BY IRUZ')
    print(Fore.BLUE)
    print(f"Kalau stuck tunggu aja")
    api = "kitkabackend.eastus.cloudapp.azure.com:5010"
    auth = str(input("Auth Key: "))
    pos = int(
        input("""
0 = Round 1 (Eliminated)
1 = Round 2 (Eliminated)
2 = Round 3 (Eliminated)
3 = Round 3 (Winner)
Input: """))
    dely = float(input("\nJumlah ( Pakai Delay 0.5): "))
    thr = int(
        input(
            "\nThreads ( Default '1' | Masukkan Angka 1 = "))
    print("STARTING" * 1)
    for _ in range(thr):
        threading.Thread(target=s).start()


def s():
    global maxerr
    while True:
        dt = datetime.datetime.now()
        try:
            headers = {
                'authorization': auth,
                'use_response_compression': 'true',
                'Accept-Encoding': 'gzip',
                'Host': api,
                'Connection': None,
                'User-Agent': None,
            }
            response = requests.get(f'http://{api}/round/finishv2/{pos}',
                                    headers=headers)
            if response.status_code == 200:
                negara = response.text.split('"Country":')[1].split(',')[0]
                nama = response.text.split('"Username":')[1].split(',')[0]
                trophy = response.text.split('"SkillRating":')[1].split(',')[0]
                crown = response.text.split('"Crowns":')[1].split(',')[0]
                sys.stdout.write(
                    f"\r[{dt.hour}:{dt.minute}:{dt.second}] {negara} |{nama} | {trophy} | {crown}"
                    
                )
                sys.stdout.flush()
            elif response.status_code == 403 and response.text == "BANNED":
                print(
                    f"[{dt.hour}:{dt.minute}:{dt.second}] Akun Telah Menerima Hadiah dari Kitkat!"
                )
                break
                sys.exit(0)
            elif response.text == "SERVER_ERROR":
                continue
            else:
                print(
                    f"[{response.status_code}] Ditunggu aja Kok Ini bukan ban")
            if dely > 0: time.sleep(dely)
        except Exception as e:
            pass


if __name__ == "__main__":
    main()
