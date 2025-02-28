from scripts_py.Sniif.colors_data import *
import os
import subprocess
import signal
from platform import system
from scripts_py.r_express import _mod_t_

def ctrl_c_trap(sig, frame):
    print(f"{VERDE}[!] {ROJO}Saliendo...")
    exit(1)

signal.signal(signal.SIGINT, ctrl_c_trap)

LIST0VERSYSTEM = ('-r/rhino', '-n/node')


__module_rc = ["search_onion", "dorks_search", "osintx_demo", "catalyst_red", "acustic_grabb", "napoleon"]

def syst3m_0xf():
    sett_env = []
    if system() == "Windows":
        sett_env.append(os.getenv("USERNAME"))
    elif system() == "Linux":
        sett_env.append(os.getenv("USER"))
    return sett_env

def commands_show():
    data_comands = f""" \r{WHITE}Modulos Web: 
                                {ROJO}\r\t[search_onion]
                        {WHITE}\rModulos Osint:
                                    {ROJO}\r\t[osintx_demo]
                                    {ROJO}\r\t[napoleon]\n
                        {WHITE}\rModulo Red:
                            {ROJO}\r\t[catalyst_red]\n
                        {WHITE}\rModulo Malware:
                                    \r\t{ROJO}[acustic_grabb] 
                    """
    print(data_comands)


def mode_execute(execute, args):
    if not os.path.exists("scripts_py/"): print(f"[!] LA RUTA DE EJECUCIÓN ESTA DAÑADA O NO EXISTE.")
    if execute == "osintx_demo":
        path_jar = _mod_t_[execute]
        os.system(f"java -jar {path_jar}Osintx-mtm.jar")
    else:
        _r_ = _mod_t_[execute]

        try:
            path_ = [_r_ + execute + ".py"] + args[0:] 
            path_s_ = " ".join(path_)
            if system() == "Linux":
                os.system(f"python3 {path_s_}")
            elif system() == "Windows":
                os.system(f"python {path_s_}")
            else:
                print(f"{ROJO}[!] {ROJO}- {VERDE}SISTEMA CORRIENDO NO VALIDO")
        except Exception as e:
            print(str(e))


def main():
    banner = f"""⠀{ROJO}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣤⣤⣤⣤⣤⣤⣤⣤⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣖⣾⣯⣽⣿⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣶⣶⣶⣾⣿⣭⣽⣿⣓⣶⣦⣤⣄⣀⡀⣀⣀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠛⠛⠛⠛⠛⠻⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⣿⡿⠟⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠛⠻⠿⡿⠋⠉⠉⠻⣿⣿⣿⣿⣿⣿⡿⠃
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⡏⠙⠻⠁⠀
⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣾⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢺⣿⣿⡏⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣴⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣾⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⢠⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⠁⠀⠀⠀⠀⠀⠀
⢀⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣤⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⡻⣿⣿⣶⣶⣦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⡿⠛⠻⢿⣿⣿⣿⣿⣿⣿⣷⡜⢿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⣾⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠏⠀⠀⠀⠀⠙⢿⣿⣷⡝⣿⣿⣿⣎⢻⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⢠⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀⠀⠀⠀⣀⡼⢿⣿⣿⣎⢿⣿⣿⣦⠻⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣸⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡏⢁⡀⠀⢀⣀⣀⣀⣀⢻⣿⣿⣎⢿⣿⣿⣧⡹⣿⣿⣿⣿⡄⠀⠀⠀⠀⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣼⣧⠀⠸⣿⣿⣿⣿⡏⣿⣿⣿⣎⢿⣿⣿⣷⡙⣿⣿⣿⣿⡀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⢰⣄⠀⠉⠛⠛⠉⠀⣿⣿⣿⣿⡎⢿⣿⣿⣷⡘⣿⣿⣿⡇⠀⠀⣾⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣦⡘⠻⠗⠀⠐⠢⣄⣀⣾⣿⣿⣿⣿⡌⣿⣿⣿⣷⡘⣿⣿⣷⠀⢀⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⢀⢀⢀⢀⢀⢈⢻⣿⣿⣿⣿⣿⣷⡘⣿⣿⣿⣷⡹⣿⣿⠀⢸⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣖⠔⠩⠎⠲⠉⢁⣿⣿⣿⣿⣿⣿⣧⢹⣿⣿⣿⣧⢻⣿⡄⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠀⢀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣇⢿⣿⣿⣿⣇⣿⣷⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡸⣿⣿⣿⣿⣼⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠼⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⡏⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠻⠿⠿⠇⣿⣿⣿⢹⣿⣿⡿⠟⠋⠉⠁⠀⠀⠀⠀⠀⠀  {YELLOW} By: Eduardx_2\n\t\t\t\t\tCOMMAND -> help⠀{WHITE}"""
    print(banner)
    
    while True:
        try:
            command_prompt = str(input("{}root@{}:-$ {}".format(MG, syst3m_0xf()[0], WHITE)))
        except:
            print(f"{ROJO}[!] - NO INGRESES NÚMEROS")
        
        if command_prompt.lower() in ("help", "list", "commands", "commandos", "cmds"): commands_show()
        elif command_prompt.lower() in ("cls", "clear"): subprocess.run("cls || clear", shell=True)
        elif command_prompt.lower() in ("salir", "exit", "flush"): break
        elif command_prompt.lower().split()[0] in __module_rc: mode_execute(command_prompt.split()[0], command_prompt.split()[1:])
        elif command_prompt.lower().split()[0] in ("run", "inicie"): inicie_service(command_prompt.split()[0], command_prompt.split()[1:])
        else: print(f"{VERDE}[!] - El comando que ingresaste no existe ->{VERDE} {ROJO}(Help o cmds)")

def inicie_service(_t, _args):
    find_list_s = ("rhino", "node")
    xor_list = []
    for __C in LIST0VERSYSTEM:
        xor_list.append(__C.split('/')[0])
    if _args[0].lower() in ('dox_w', 'osint', 'search'):
        if system() == "Windows":
            rute = "dox_w/JS/index_server.js"
            subprocess.Popen(['node', rute], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, creationflags=subprocess.DETACHED_PROCESS)
        elif system() == "Linux" and _args[1].lower() in xor_list:
            arg_c = list(map(lambda x: x.lower(), xor_list)).index(_args[1].lower())
            subprocess.run(f"{find_list_s[arg_c]} dox_w/JS/index_server.js", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        else: pass
    elif _args[0] in ('user_find', 'find_username', 'usernamx', 'user_osint'):
        if system() == "Windows":
            rute_ = "osint_name/server_find/index_find.js"
            subprocess.Popen(['node', rute_], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, creationflags=subprocess.DETACHED_PROCESS)
        elif system() == "Linux" and _args[1].lower() in xor_list:
            arg_c = list(map(lambda x: x.lower(), xor_list)).index(_args[1].lower())
            subprocess.run(f"{find_list_s[arg_c]} osint_name/server_find/index_find.js", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    else:
        print(f"{ROJO}[!] {YELLOW}-{YELLOW} {ROJO}EL COMANDO INGRESADO NO EXISTE")
        


main()