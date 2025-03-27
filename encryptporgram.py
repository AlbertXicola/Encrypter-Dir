import os
import time
import platform
import time
import psutil
from cryptography.fernet import Fernet
import sys
import time

def print_banner():
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la terminal
   
    print("\033[1;31m" + "="*56)  
    print("\033[1;32m" + "      ██████████████████████████████████████") 
    print("\033[1;32m" + "      ███\033[1;33m     Kichola Encrypter v1.0     \033[1;32m███") 
    print("\033[1;32m" + "      ██████████████████████████████████████")
    print("\033[1;34m" + "  [~] Welcome to Kichola's terminal. Ready to explore.") 
    print("\033[1;34m" + "  [~] Choose an option from the menu below.")  
    print("\033[1;31m" + "="*56) 

def print_menu():

    print("\033[1;34m" + "="*56) 
    print("\033[1;32m" + "  Please select an option from the menu below.") 
    print("\033[1;34m" + "="*56) 
    print()
    print("\033[1;33m  🔹 [1] Show system info")    
    print("\033[1;31m  🔹 [2] Encrypt files")    
    print("\033[1;35m  🔹 [3] Decrypt files")  
    print("\033[1;32m  🔹 [4] Exit program")        
    print("\033[1;37m  ✨ Please choose an option: ", end="")  


def show_system_info():
    print("\033[1;33mYou selected Show system info.\033[0m")
    
    system_info = {
        "Operating System": platform.system(),
        "OS Version": platform.version(),
        "Node Name": platform.node(),
        "Architecture": platform.architecture()[0],
        "Processor": platform.processor(),
        "Physical Cores": psutil.cpu_count(logical=False),
        "Logical Cores": psutil.cpu_count(logical=True),
        "Total RAM": f"{round(psutil.virtual_memory().total / (1024**3), 2)} GB"
    }

    
    print("\n\033[1;34m--- System Information ---\033[0m")
    for key, value in system_info.items():
        print(f"\033[1;33m{key}:\033[0m {value}") 
  
    input("\n\033[1;32m" + "  Please continue with enter")

    print_banner() 

def list_files(start_path):

    total_archivos = 0 
    for root, dirs, files in os.walk(start_path):
        for file in files:
            file_path = os.path.join(root, file)
            total_archivos += 1 
    print()
                
    print("\033[1;34m" + "="*40)
            
    print(f"\033[1;32m  Total files found: {total_archivos}\033[0m")
    print("\033[1;34m" + "="*40) 
         
    if total_archivos == 0:
        print("No files detected, nothing to encrypt")
        pass
    else:
        while True:

                print()
                
                print(f"    \033[1;31mFiles Found:\033[0m")
                for root, dirs, files in os.walk(start_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        print(f"      {file_path}")
                break

        encrypt(start_path)


    input("\n\033[1;32m" + "  Please continue with enter") 
    print_banner()  # Volver a mostrar el menú después de realizar la opción 2

def generate_key():
    key = Fernet.generate_key()
    key_path = "secret.key"  # Ahora es una ruta válida
    with open(key_path, "wb") as key_file:
        key_file.write(key)
    print(f"  New Key in: {key_path}")

def load_key():
    key_path = "secret.key"
    if not os.path.exists(key_path):
        print("Error: No se encontró la clave de cifrado.")
        return None
    return open(key_path, "rb").read()

def encrypt(start_path):
    print()
    print("    \033[1;31mDo you want to encrypt this files? (y/n): \033[0m", end="")
    respuesta2 = input().strip().lower()

    if respuesta2 in ["y", "yes"]:

        key = load_key()  
        cipher = Fernet(key)
        print()
        print(f"    \033[1;31mEncrypting Files...\033[0m")
        for root, _, files in os.walk(start_path):
            for file in files:
                file_path = os.path.join(root, file)

               
                with open(file_path, "rb") as f:
                    file_data = f.read()
                
                
                encrypted_data = cipher.encrypt(file_data)

              
                with open(file_path, "wb") as f:
                    f.write(encrypted_data)

                print(f"      \033[1;33m{file_path}\033[0m") 
        print(f"    \033[1;31mAll files have been Encrypted\033[0m")
        key_path = "secret.key"
        if os.path.exists(key_path):
            print("\n\033[1;32mEncryption Key:\033[0m")
            with open(key_path, "rb") as key_file:
                key_content = key_file.read()
                print(key_content.decode())

            print("\n    \033[1;31mDeleting key file...\033[0m")
            os.remove(key_path)
            print("    \033[1;32mKey file deleted successfully.\033[0m")


def typing_effect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Salto de línea   

def decrypt(start_path):


    print()
    key = input("     \033[1;32mInput the key to decrypt:\033[0m")
    try:

        cipher = Fernet(key)
        print("     \033[1;32mDecrypting files...\033[0m")
        print()
        print("     \033[1;35mDecryption result: \033[0m") 

        for root, _, files in os.walk(start_path):
            for file in files:
                file_path = os.path.join(root, file)

                try:
                    with open(file_path, "rb") as f:
                        encrypted_data = f.read()

                    # Intentar desencriptar el archivo
                    decrypted_data = cipher.decrypt(encrypted_data)

                    # Si la desencriptación es exitosa, escribir el archivo
                    with open(file_path, "wb") as f:
                        f.write(decrypted_data)
                    print(f"       \033[1;32mCorrect\033[0m           {file_path} ")

                except Exception as e:
                    print(f"       \033[1;31mError Decrypt {e}\033[0m    {file_path} ")
                    continue  # Continuar con los otros archivos, ignorando los que no se pueden desencriptar

        print("     \033[1;35mAll files have been decrypted\033[0m") 
    except ValueError:
        print()
        print("  \033[1;31m   Error: Incorrect Key . Make sure the key is correctly formatted (32 bytes in base64).\033[0m")

    input("\n\033[1;32m" + "  Please continue with enter")
    print_banner()



rutaencrypt = ""


def handle_menu_choice(choice):
    global rutaencrypt 

    if choice == "1":
        print_banner() 
        show_system_info()
        
    elif choice == "2":
        print_banner() 
        
        typing_effect("\033[1;31m  You selected Encrypt files\033[0m") 

        if os.path.exists("secret.key"):
            pass
        else: 
            generate_key()
        print()

        rutaencrypt = input("\033[1;32m" + "  Please enter the path that triggered the encryption:\033[0m ")
        if rutaencrypt:
            list_files(rutaencrypt)
        else:
            print_banner() 
            print("  No empty path please")

    elif choice == "3":
        print_banner()
        print("\033[1;35m  You selected Decrypt files\033[0m") 
        print()

        rutaencrypt = input("\033[1;32m" + "     Please enter the path that triggered the decryption:\033[0m ")
        if rutaencrypt:
            decrypt(rutaencrypt)
        else:
            print_banner() 
            print("  No empty path please")


        
    elif choice == "4":
        print("\033[1;32m  Exiting program... Goodbye!\033[0m")  
        exit()

    else:
        print_banner()
        print("\033[1;33m  Invalid choice. Try again.\033[0m")




def main():
    print_banner() 
    while True:
        print_menu() 
        choice = input("\033[1;37mEnter your choice: ")
        handle_menu_choice(choice) 

main()