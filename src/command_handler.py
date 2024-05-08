# command_handler.py
from imports import *
from constants import *
from defs import *

"""
def handle_help_command():
  print(f"{COLOR_YELLOW}Uso:{COLOR_RESET} python3 autocheck.py [{COLOR_YELLOW}--help | --version | --download-checks | --exercise-status | --yt | --exam-mode | --descs <nombre_ejercicio> | --list{COLOR_RESET}]")
  print(f"{COLOR_YELLOW}--help:{COLOR_RESET} Muestra esta información de ayuda.")
  print(f"{COLOR_YELLOW}--version:{COLOR_RESET} Muestra la versión del programa.")
  print(f"{COLOR_YELLOW}--download-checks:{COLOR_RESET} Descarga los checks necesarios localmente para su uso offline.")
  print(f"{COLOR_YELLOW}--exercise-status:{COLOR_RESET} Muestra el estado de los ejercicios.")
  print(f"{COLOR_YELLOW}--yt:{COLOR_RESET} Abre el canal de YouTube de Flyz.")
  print(f"{COLOR_YELLOW}--exam-mode:{COLOR_RESET} Activa el modo examen.")
  print(f"{COLOR_YELLOW}--descs <nombre_ejercicio>:{COLOR_RESET} Muestra la descripción de un ejercicio específico.")
  print(f"{COLOR_YELLOW}--list:{COLOR_RESET} Muestra una lista de archivos .java conocidos.")
  exit(0)
"""

def handle_help_command():
    help_info = [
        {"command": "--help | -h", "description": "Muestra esta información de ayuda."},
        {"command": "--version | -v", "description": "Muestra la versión del programa."},
        {"command": "--download-checks | -c", "description": "Descarga los checks necesarios localmente para su uso offline."},
        {"command": "--exercise-status | -s", "description": "Muestra el estado de los ejercicios."},
        {"command": "--yt | -y", "description": "Abre el canal de YouTube de Flyz."},
        {"command": "--exam-mode | -t", "description": "Activa el modo examen."},
        {"command": "--descs <nombre_ejercicio> | -d <nombre_ejercicio>", "description": "Muestra la descripción de un ejercicio específico."},
        {"command": "--list | -l", "description": "Muestra una lista de archivos .java conocidos."}
    ]

    print(f"{COLOR_YELLOW}Uso:{COLOR_RESET} python3 autocheck.py [<comando>]")
    for info in help_info:
        print(f"{COLOR_YELLOW}{info['command']}:{COLOR_RESET} {info['description']}")
    exit(0)

def handle_version_command():
  print(f"Autocheck {COLOR_YELLOW}{VERSION}{COLOR_RESET}")

def handle_description_command():
  if len(sys.argv) > 2:
    exercise_name = sys.argv[2]
    get_exercise_description(exercise_name)
  else:
    print_error_message("010", "Se requiere el nombre del ejercicio después de --descs.")

def handle_exercise_status_command():
  check_status = read_check_status()
  if check_status:
    show_exercise_status(check_status)

def open_youtube_channel():
  youtube_channel = "@devflyz"
  youtube_url = f"https://www.youtube.com/{youtube_channel}"
  subprocess.run(['xdg-open', youtube_url])
