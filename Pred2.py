import random
import time
import colorama
from colorama import Fore, Style


print(Fore.RED + """
   _____      _         __  __ _                  __      ____ 
  / ____|    (_)       |  \/  (_)                 \ \    / /_ |
 | |     ___  _ _ __   | \  / |_ _ __   ___ _ __   \ \  / / | |
 | |    / _ \| | '_ \  | |\/| | | '_ \ / _ \ '__|   \ \/ /  | |
 | |___| (_) | | | | | | |  | | | | | |  __/ |       \  /   | |
  \_____\___/|_|_| |_| |_|  |_|_|_| |_|\___|_|        \(_)  |_|
                                                               
                                                               
""")

def print_colored(text, color):
    print(color + text + Style.RESET_ALL)
    
def choose_risk_level():
    print_colored("*================= " + Fore.YELLOW + "Choose your option " + Fore.RESET + "================*", colorama.Fore.RESET)
    print_colored("| " + Fore.BLUE + "            [1]" + Fore.GREEN + "Low risk - Small Profit" + Fore.RESET + "             |", colorama.Fore.RESET)
    print_colored("| " + Fore.BLUE + "            [2]" + Fore.RED + "High Risk - High Profit" + Fore.RESET + "               |", colorama.Fore.RESET)
    print_colored("*======================================================*", colorama.Fore.RESET)
    option = int(input("Option: "))
    if option == 1:
        return "low"
    elif option == 2:
        return "high"
    else:
        print_colored("Invalid option. Defaulting to low risk.", Fore.YELLOW)
        return "low"

def generate_prediction(risk_level):
    if risk_level == "low":
        bot_options = [
            "[❌❌✅❌❌]",
            "[✅❌❌❌❌]",
            "[❌❌❌❌✅]",
            "[✅❌❌❌❌]",
            "[❌❌✅❌❌]",
        ]
    else:
        bot_options = [
            "[✅❌✅✅❌]",
            "[❌❌❌✅❌]",
            "[❌✅❌✅❌]",
            "[✅❌✅❌❌]",
            "[✅❌❌✅❌]",
        ]
    random.shuffle(bot_options)
    return bot_options

def display_prediction(prediction):
    print_colored(Fore.GREEN + "BOT IS READY", colorama.Fore.RESET)
    time.sleep(1)
    print_colored(Fore.GREEN + "Showing prediction...", colorama.Fore.RESET)
    time.sleep(1)
    for line in prediction:
        print_colored(line, colorama.Fore.RESET)
        time.sleep(0.5)
    probably_chance = random.randint(10, 90)
    print_colored(Fore.YELLOW + f"Probably chance: {probably_chance}%", colorama.Fore.RESET)

print_colored(Fore.GREEN + "WELCOME TO PREDICTOR BOT", Fore.RESET)
time.sleep(1)
print_colored(Fore.GREEN + "Log in successfully", Fore.RESET)
print()
time.sleep(1)

while True:
    risk_level = choose_risk_level()
    prediction = generate_prediction(risk_level)
    display_prediction(prediction)
