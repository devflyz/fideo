from imports import *
from constants import *

def check_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        
        # Check if all required keys are present
        required_keys = ['problem_name', 'problem_title', 'description', 'input_format',
                         'constraints', 'output_format', 'params_count', 'outputs_count',
                         'total_test_cases', 'use_locale', 'test_cases']
        for key in required_keys:
            if key not in data:
                print(f"{COLOR_RED}Error: Key '{key}' is missing in {file_path}{COLOR_RESET}")
                return False
        
        # Check if the number of inputs and outputs match the params_count and outputs_count respectively
        if data['params_count'] != len(data['test_cases'][0]['inputs']):
            print(f"{COLOR_RED}Error: Number of inputs in test cases does not match params_count in {file_path}{COLOR_RESET}")
            return False
        if data['outputs_count'] != len(data['test_cases'][0]['expected_outputs']):
            print(f"{COLOR_RED}Error: Number of expected outputs in test cases does not match outputs_count in {file_path}{COLOR_RESET}")
            return False
        
        return True

def main(folder_path):
    json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]
    
    for file in json_files:
        file_path = os.path.join(folder_path, file)
        print(f"{COLOR_CYAN}Checking {file}...{COLOR_RESET}")
        if not check_json_file(file_path):
            print(f"{COLOR_RED}File {file} does not meet the required format.{COLOR_RESET}")
        else:
            print(f"{COLOR_GREEN}File {file} is valid.{COLOR_RESET}")
        print()

if __name__ == "__main__":
    folder_path = '../probs/checks'  # Change this to the path of your JSON files folder
    main(folder_path)
