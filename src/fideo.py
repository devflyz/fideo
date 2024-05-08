from imports import *
from constants import *
from command_handler import *
from defs import *

# Verificar si se proporcionaron parámetros adicionales
if len(sys.argv) > 1:
    if sys.argv[1] == "--help" or sys.argv[1] == "-h":
        handle_help_command()
        exit(0)
    elif sys.argv[1] == "--version" or sys.argv[1] == "-v":
        handle_version_command()
        exit(0)
    elif sys.argv[1] == "--download-checks" or sys.argv[1] == "-c":
        download_checks()
        exit(0)
    elif sys.argv[1] == "--descs" or sys.argv[1] == "-d":
        handle_description_command()
        exit(0)
    elif sys.argv[1] == "--exercise-status" or sys.argv[1] == "-s":
        handle_exercise_status_command()
        exit(0)
    elif sys.argv[1] == "--yt" or sys.argv[1] == "-y":
        open_youtube_channel()
        exit(0)
    elif sys.argv[1] == "--test" or sys.argv[1] == "-t":
        exam_mode()
        exit(0)
    elif sys.argv[1] == "--update" or sys.argv[1] == "-u":
        update_fideo()
        exit(0):
    elif sys.argv[1] in get_known_java_files():
        selected_java_file = sys.argv[1]
    elif sys.argv[1] == "--list" or sys.argv[1] == "-l":
        show_known_java_files(get_known_java_files());
        exit(0);

    # Compilar el archivo Java
        if not compile_java_file(selected_java_file):
            exit(1)  # Si falla la compilación, salir del programa :c

        # Obtener la URL del archivo JSON de los casos de prueba
        json_url = f"{JSON_CHECKS_BASE_URL}{selected_java_file}.json"

        # Descargar el archivo JSON de los casos de prueba
        response = requests.get(json_url)
        if response.status_code == 200:
            test_cases_data = response.json()
        else:
            print_error_message("005","No se pudo obtener el archivo JSON de casos de prueba desde la URL.")
            exit(1)

        # Obtener los datos específicos del JSON de respuesta
        params_count = test_cases_data[selected_java_file]['params_count']
        outputs_count = test_cases_data[selected_java_file]['outputs_count']
        total_test_cases = test_cases_data[selected_java_file]['total_test_cases']
        test_cases = test_cases_data[selected_java_file]['test_cases']

        # Ejecutar los casos de prueba
        execute_test_cases(selected_java_file, test_cases)
        exit(0)

# Si no se proporcionaron parámetros adicionales, ejecutar normalmente
try:
    while True:
        # Mostrar lista de archivos .java conocidos
        show_known_java_files(get_known_java_files())

        # Solicitar al usuario que seleccione un archivo .java para evaluar
        selection = input(f"{COLOR_YELLOW}Seleccione el archivo .java que desea evaluar (0-{len(get_known_java_files())}): {COLOR_RESET}")

        # Verificar si se seleccionó un archivo .java válido
        try:
            selection = int(selection)
            if selection < 0 or selection > len(get_known_java_files()):
                raise ValueError
        except ValueError:
            print_error_message("006", "Selección inválida.")
            continue

        if selection == 0:
            print_exit_message("Saliendo.")
            exit(0)

        selected_java_file = get_known_java_files()[selection - 1]

        # Verificar si el archivo Java seleccionado existe en la carpeta actual
        if not os.path.isfile(selected_java_file):
            print_error_message("007", "El archivo {} no existe en la carpeta actual.".format(selected_java_file))
            continue

        # Color verde si el archivo existe en el directorio actual
        print(f"{COLOR_GREEN}El archivo {selected_java_file} está presente en el directorio actual.{COLOR_RESET}")

        # Compilar el archivo Java
        if not compile_java_file(selected_java_file):
            print_error_message("008", "Falla la compilación. Volviendo al menú de selección.")
            continue  # Si falla la compilación, volver al menú de selección

        # Obtener la URL del archivo JSON de los casos de prueba
        json_url = f"{JSON_CHECKS_BASE_URL}{selected_java_file}.json"

        # Descargar el archivo JSON de los casos de prueba
        response = requests.get(json_url)
        if response.status_code == 200:
            test_cases_data = response.json()
        else:
            print_error_message("009", "No se pudo obtener el archivo JSON de casos de prueba desde la URL.")
            continue

        # Obtener los datos específicos del JSON de respuesta
        params_count = test_cases_data['params_count']
        outputs_count = test_cases_data['outputs_count']
        total_test_cases = test_cases_data['total_test_cases']
        test_cases = test_cases_data['test_cases']

        # Ejecutar los casos de prueba
        execute_test_cases(selected_java_file, test_cases)
except KeyboardInterrupt:
    print_exit_message("Se ha interrumpido la ejecución del programa. Saliendo...")
    exit(0)
