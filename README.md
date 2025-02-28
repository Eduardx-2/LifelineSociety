<p align="center">
<img width="70%" height="70%" src="https://github.com/Eduardx-2/Lifeline-society/blob/main/lifeLog.jpeg"/>
</a>
</p>

* Lifeline Society es una herramienta de hacking modular, donde cada módulo contiene su propia funcionalidad específica. 
  Características:
  
*    Modularidad: Cada módulo es una herramienta independiente que puede ejecutarse dentro del programa.
*    Ejemplo de módulo: El módulo de web incluye un analizador de páginas .onion, permitiendo verificar si están activas o inactivas.
*    Interfaz de comandos: Puedes interactuar con la herramienta a través de comandos personalizados.

Para listar los comandos disponibles, utiliza cualquiera de las siguientes opciones:
- help  
- list  
- commands  
- commandos  
- cmds

# Catalyst
*  Funciona como una herramienta diseñada para capturar trafico en red y mostralo en consola.
<p align="center">
<img width="60%" height="40%" src="https://github.com/Eduardx-2/LifelineSociety/blob/main/catalyst.jpeg"/>
</a>
</p>

# Napoleon
* Funciona como una herramienta de web scraping diseñada para buscar información sobre un nombre de usuario, identificando en qué sitios está registrado. Incluye el argumento -f, que permite filtrar la búsqueda en plataformas específicas proporcionadas por el usuario, por ejemplo: -f instagram,youtube
<p align="center">
<img width="60%" height="40%" src="https://github.com/Eduardx-2/LifelineSociety/blob/main/napoleon.jpeg"/>
</a>
</p>

    
## Instalación

```console
# clonar el repo
$ git clone https://github.com/Eduardx-2/Lifeline-society.git

# Moverse al directorio
$  cd Lifeline-society

# instalar requirement linux:
$ python3 -m pip3 install -r requirements.txt

# Windows
$ python -m pip install -r requirements.txt

# Ejecución
$ python main.py or python3 main.py

```
## Sistemas Operativos

## La herramienta se encuentra en proceso de creación y desarrollo en el entorno de Windows 11. Dado que es un programa de interfaz de línea de comandos (CLI), su compilación es compatible con varios sistemas operativos. No obstante, es importante considerar que se trata de un programa modular.

•    Windows 8, 10, 11 AMD
•    Linux AMD
•    ARM (Kali Linux (Android), Raspberry Pi)

El programa fue creado y diseñado utilizando la arquitectura AMD. Hasta el momento, no se han realizado pruebas en la arquitectura ARM.

El entorno de Windows permite la ejecución fluida del 100% de los módulos, mientras que en Linux solo funcionan el módulo web, red y Osintx. Aunque es posible la compilación, el módulo de malware puede infectar, pero no ejecutarse dentro de un sistema Linux. Cabe destacar que el virus está específicamente diseñado para Windows, no para Linux. En este caso, la implementación está restringida a SISTEMAS OPERATIVOS WINDOWS, desde la versión 8 en adelante.

## Modulos

* Modulo Web
* Modulo Red
* Modulo Malware
* Modulo Osint

# Instalacion de ejecución

```console
# JS

* npm i puppeteer
* npm i express

#Python

* bs4
* Requests
* os
* sys

```

## Modulo Web 
```console
# Search_onion

$ Antes de usar el programa Search_onion, en un cmd ejecute "tor &", si esta en linux,
si cuenta con una distribución Windows ejecutelo desde la ruta de donde descargo tor 
```


## Legal

* El usuario que descargue este proyecto asume toda la responsabilidad por su uso. El creador de este proyecto no se hace responsable por ningún mal uso de la herramienta. Es importante utilizar esta herramienta de manera ética y dentro de los límites legales y éticos aplicables.

# Versión 

Este proyecto se encuentra en fase beta y aún no está completamente finalizado. Actualmente, presenta algunos problemas y errores que serán abordados y resueltos en futuras actualizaciones

## License

MIT © Lifeline Society<br/>
Creador y desarrolador principal = Eduardx_2
