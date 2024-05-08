from constants import *
from imports import *
def print_error_message(error_code, message):
    print(f"\n{COLOR_RED}Error {error_code}:{COLOR_RESET} {message}")

"""def get_exercise_description(exercise_name):
    # Obtener la URL del archivo JSON del ejercicio
    if exercise_name.endswith(".java"):
        json_url = f"{JSON_CHECKS_BASE_URL}{exercise_name}.json"
    else:
        json_url = f"{JSON_CHECKS_BASE_URL}{exercise_name}.java.json"


    # Descargar el archivo JSON del ejercicio
    response = requests.get(json_url)
    if response.status_code == 200:
        exercise_data = response.json()
        print(f"{COLOR_YELLOW}Información del ejercicio {exercise_name}:{COLOR_RESET}")
        print(DIVIDER)
        print(f"{COLOR_CYAN}Nombre del problema:{COLOR_RESET} {exercise_data['problem_title']} ({exercise_data['problem_name']})")
        print(f"{COLOR_CYAN}Descripción:{COLOR_RESET}\n{exercise_data['description']}")
        print(f"{COLOR_CYAN}Formato de entrada:{COLOR_RESET}\n{exercise_data['input_format']}")
        print(f"{COLOR_CYAN}Restricciones:{COLOR_RESET} {exercise_data['constraints']}")
        print(f"{COLOR_CYAN}Formato de salida:{COLOR_RESET}\n{exercise_data['output_format']}")
        print(f"{COLOR_CYAN}¿Usar locale?:{COLOR_RESET} {exercise_data['use_locale']}")
    else:
        print_error_message("012", "No se pudo obtener la descripción del ejercicio desde la URL.")"""

def get_exercise_description(exercise_name):
    # Obtener la URL del archivo JSON del ejercicio
    if exercise_name.endswith(".java"):
        json_url = f"{JSON_CHECKS_BASE_URL}{exercise_name}.json"
    else:
        json_url = f"{JSON_CHECKS_BASE_URL}{exercise_name}.java.json"


    # Descargar el archivo JSON del ejercicio
    response = requests.get(json_url)
    if response.status_code == 200:
        exercise_data = response.json()
        print(f"{COLOR_YELLOW}Información del ejercicio {exercise_name}:{COLOR_RESET}")
        print(DIVIDER)
        print(f"{COLOR_CYAN}Nombre del problema:{COLOR_RESET} {exercise_data['problem_title']} ({exercise_data['problem_name']})")
        print(f"{COLOR_CYAN}Descripción:{COLOR_RESET}\n{exercise_data['description']}")
        print(f"{COLOR_CYAN}Formato de entrada:{COLOR_RESET}\n{exercise_data['input_format']}")
        print(f"{COLOR_CYAN}Restricciones:{COLOR_RESET} {exercise_data['constraints']}")
        print(f"{COLOR_CYAN}Formato de salida:{COLOR_RESET}\n{exercise_data['output_format']}")
        print(f"{COLOR_CYAN}¿Usar locale?:{COLOR_RESET} {exercise_data['use_locale']}")

        # Mostrar casos de prueba
        print(f"\n{COLOR_YELLOW}Casos de Prueba:{COLOR_RESET}")
        for i, test_case in enumerate(exercise_data['test_cases'], 1):
            inputs_str = ', '.join(test_case['inputs'])
            expected_outputs_str = ', '.join(test_case['expected_outputs'])
            print(f"\n{COLOR_CYAN}Caso de Prueba{COLOR_RESET} {i}:")
            print(f"{COLOR_CYAN}Inputs:{COLOR_RESET} {inputs_str}")
            print(f"{COLOR_CYAN}Respuesta Esperada:{COLOR_RESET} {expected_outputs_str}")
    else:
        print_error_message("012", "No se pudo obtener la descripción del ejercicio desde la URL.")



def print_exit_message(message):
    print(f"\n{COLOR_SALIR}{message}{COLOR_RESET}")

def get_known_java_files():
    known_java_files_url = "https://raw.githubusercontent.com/devflyz/fideo/main/probs/known.json"
    try:
        response = requests.get(known_java_files_url)
        if response.status_code == 200:
            return response.json()
        else:
            print_error_message("001","No se pudo obtener la lista de archivos.java conocidos desde la URL.")
            exit(1)
    except Exception as e:
        print_error_message(f"002","Error al intentar obtener la lista de archivos.java conocidos: {str(e)}")
        exit(1)

# Función para crear el modo examen
def exam_mode():
    start_time = time.time()
    print("¡Bienvenido al modo examen!")

    while True:
        # Generar un ejercicio aleatorio
        exercise = random.choice(get_known_java_files())
        exercise_folder = os.path.join(os.getcwd(), exercise.split('.')[0])

        # Crear la carpeta del ejercicio
        os.makedirs(exercise_folder, exist_ok=True)

        # Copiar el archivo de ejercicio seleccionado a la carpeta
        shutil.copy(exercise, exercise_folder)

        # Compilar el archivo Java
        if not compile_java_file(os.path.join(exercise_folder, exercise)):
            continue

        # Obtener la URL del archivo JSON de los casos de prueba
        json_url = f"https://devflyz.github.io/check/{exercise}.json"

        # Descargar el archivo JSON de los casos de prueba
        response = requests.get(json_url)
        if response.status_code == 200:
            test_cases_data = response.json()
        else:
            print_error_message("003","No se pudo obtener el archivo JSON de casos de prueba desde la URL.")
            continue

        # Obtener los datos específicos del JSON de respuesta
        params_count = test_cases_data[exercise]['params_count']
        outputs_count = test_cases_data[exercise]['outputs_count']
        total_test_cases = test_cases_data[exercise]['total_test_cases']
        test_cases = test_cases_data[exercise]['test_cases']

        # Ejecutar los casos de prueba
        execute_test_cases(os.path.join(exercise_folder, exercise), test_cases)

        # Eliminar la carpeta del ejercicio
        shutil.rmtree(exercise_folder)

        # Verificar si el tiempo límite del examen ha sido alcanzado
        elapsed_time = time.time() - start_time
        if elapsed_time >= 3600:
            print("¡Tiempo límite del examen alcanzado!")
            break



# Función para descargar los checks localmente
def download_checks():
    # Directorio donde se guardarán los checks
    download_dir = input("Ingrese la ruta donde desea guardar los checks descargados: ")

    # Verificar si el directorio existe, si no, crearlo
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    # Descargar los checks JSON y guardarlos localmente
    known_java_files_url = "https://raw.githubusercontent.com/devflyz/fideo/main/probs/known.json"
    response = requests.get(known_java_files_url)
    if response.status_code == 200:
        with open(os.path.join(download_dir, "known_java_files.json"), 'w') as f:
            f.write(response.text)
    else:
        print("Error: No se pudo descargar la lista de archivos .java conocidos.")

    # Descargar otros checks según sea necesario...

# Leer el estado de los ejercicios desde el archivo JSON
def read_check_status():
    check_status_file = 'https://raw.githubusercontent.com/devflyz/devflyz.github.io/main/check/check_status.json'
    response = requests.get(check_status_file)
    if response.status_code == 200:
        check_status = json.loads(response.text)
        return check_status
    else:
        print(f"{COLOR_RED}Error:{COLOR_RESET} No se pudo leer el estado de los ejercicios desde el servidor.")
        return None

# Función para verificar y crear la carpeta ~/.flyz/check.json
def verify_and_create_check_folder():
    check_folder_path = os.path.expanduser('~/flyz/check.json')
    if not os.path.exists(check_folder_path):
        os.makedirs(os.path.dirname(check_folder_path), exist_ok=True)
        with open(check_folder_path, 'w') as f:
            json.dump({"version": VERSION, "github": "devflyz", "youtube": "@devflyz"}, f)
        print(f"{COLOR_GREEN}Carpeta creada y archivo check.json inicializado.{COLOR_RESET}")

# Verificar si se proporcionó el parámetro para descargar checks localmente
def show_exercise_status(check_status):
    print(f"{COLOR_YELLOW}Estado de los Ejercicios:{COLOR_RESET}")
    for exercise, status in check_status.items():
        print(f"{exercise}: {'✅' if status else '❌'}")

# Función para mostrar la lista de archivos .java conocidos
"""def show_known_java_files(known_java_files):
    print(f"{COLOR_YELLOW}Archivos .java conocidos:{COLOR_RESET}")
    print(DIVIDER)
    known_java_list = f"{COLOR_SALIR}0) Salir{COLOR_RESET}"  # Cambiar el color de la opción "Salir"
    for count, java_file in enumerate(known_java_files, start=1):
        # Verificar si el archivo está presente en el directorio actual
        if os.path.isfile(java_file):
            known_java_list += f"\n{COLOR_GREEN}{count}) {java_file}{COLOR_RESET}"
        else:
            known_java_list += f"\n{count}) {java_file}"
    print(known_java_list)"""

def show_known_java_files(known_java_files):
    print(f"{COLOR_YELLOW}Archivos .java conocidos:{COLOR_RESET}")
    print(DIVIDER)

    if len(known_java_files) == 0:
        print("No hay archivos .java conocidos.")
        return

    max_columns = 5  # Número máximo de columnas
    max_files = 10  # Número máximo de archivos a imprimir por columna
    num_files = len(known_java_files)
    num_columns = min((num_files + max_files - 1) // max_files, max_columns)  # Calcula el número de columnas

    max_length = max(len(file) for file in known_java_files)
    column_width = max_length + 5  # Espacio adicional para separación

    for i in range(max_files):
        for j in range(num_columns):
            idx = i + j * max_files
            if idx < num_files:
                java_file = known_java_files[idx]
                enumeration = idx + 1
                if os.path.isfile(java_file):
                    print(f"{COLOR_GREEN}{str(enumeration).ljust(3)} {java_file.ljust(column_width)}{COLOR_RESET}", end="")
                else:
                    print(f"{str(enumeration).ljust(3)} {java_file.ljust(column_width)}", end="")
        print()

    # Opción para salir
    print(f"{COLOR_SALIR}0) Salir{COLOR_RESET}")

# Función para ejecutar los casos de prueba
def execute_test_cases(selected_java_file, test_cases):
    # Divisor
    print(f"\n{DIVIDER}")

    # Contadores
    total_cases = len(test_cases)
    correct_cases = 0

    # Ejecutar el programa para cada ejemplo de entrada y comparar la salida con la salida esperada
    for i, test_case in enumerate(test_cases, start=1):
        input_data = '\n'.join(test_case['inputs'])
        process = subprocess.Popen(['java', selected_java_file[:-5]], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, output_err = process.communicate(input_data)
        expected_output = '\n'.join(test_case['expected_outputs'])

        # Verificar si hubo un error de salida
        if output_err.strip():
            print(f"{COLOR_RED}Caso {i}: error de salida{COLOR_RESET}")
            print(f"{COLOR_RED}Error generado:{COLOR_RESET} {output_err.strip()}")
            continue

        # Comparar la salida generada con la salida esperada
        if output.strip() == expected_output.strip():
            print(f"{COLOR_GREEN}Caso {i}: correcto{COLOR_RESET}")
            correct_cases += 1
        else:
            print(f"{COLOR_RED}Caso {i}: incorrecto{COLOR_RESET}")
            print(f"{COLOR_GREEN}Salida esperada:{COLOR_RESET} {expected_output}")
            print(f"{COLOR_RED}Salida generada:{COLOR_RESET} {output.strip()}")

    # Divisor
    print(f"{DIVIDER}\n")

    # Mostrar resultado del checker
    print(f"{COLOR_YELLOW}Resultado del checker:{COLOR_RESET} {correct_cases}/{total_cases}")

    # Eliminar el archivo .class
    class_file = selected_java_file[:-5] + ".class"
    if os.path.isfile(class_file):
        os.remove(class_file)
        print(f"{COLOR_YELLOW}Archivo .class eliminado.{COLOR_RESET}")


# Función para compilar el archivo Java
def compile_java_file(java_file):
    class_file = java_file[:-5] + ".class"
    if os.path.isfile(class_file):
        os.remove(class_file)  # Eliminar el archivo .class existente antes de compilar

    compile_command = f"javac {java_file}"
    compile_process = subprocess.Popen(compile_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    compile_output, compile_error = compile_process.communicate()

    if compile_process.returncode != 0:
        print_error_message("004","Error al compilar el archivo {}.".format(java_file))
        print(f"{COLOR_RED}{compile_error.decode()}{COLOR_RESET}")
        return False
    else:
        print(f"{COLOR_GREEN}Compilación exitosa:{COLOR_RESET} {java_file}")
        return True
