import colorama 
#back for background, fore for text color
from colorama.ansi import Back, Fore 

#reset colore pallet after program executes
colorama.init(autoreset=True) 

text = input("Enter a phrase or a sentence: ") 

# Colorama has limited color options 

print(Fore.BLACK + Back.WHITE + text)
print(Fore.RED + Back.CYAN + text) 
print(Fore.GREEN + Back.YELLOW + text)
print(Fore.BLUE + Back.MAGENTA + text)
print(Fore.YELLOW + Back.BLUE + text) 
print(Fore.CYAN + Back.RED + text)
print(Fore.WHITE + Back.BLACK + text) 