from termcolor import colored
import os


def banner():
    os.system('clear')
    print(
        colored(
            f"""
╭━━┳━━━━╮╱╭━━━╮╱╱╱╱╱╭╮
┃╭╮┃╭╮╭╮┃╱┃╭━╮┃╱╱╱╱╱┃┃
┃╰╯╰┫┃┃╰╯╱┃┃╱┃┣━╮╭━━┫┃╭╮╱╭┳━━━┳━━┳━╮
┃╭━╮┃┃┃╭━━┫╰━╯┃╭╮┫╭╮┃┃┃┃╱┃┣━━┃┃┃━┫╭╯
┃╰━╯┃┃┃╰━━┫╭━╮┃┃┃┃╭╮┃╰┫╰━╯┃┃━━┫┃━┫┃
╰━━━╯╰╯╱╱╱╰╯╱╰┻╯╰┻╯╰┻━┻━╮╭┻━━━┻━━┻╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯
""", 'red'), colored(f"""
[*] last update :  1 Jul 2023
[*] version : 1.0.0
[*] author : localho3t
[*] ideas : Coding with security ;)
""", 'green')
    )
