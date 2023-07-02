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
╱╱╱╱╱╱╱╱v1.0.0╱╱╱╱╱╱╱╱╭━╯┃[localho3t]
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯{colored('(nginx)','green')}
""", 'red'), colored(f"""
[*] last update :  1 Jul 2023
[*] ideas : Coding with security ;)
""", 'green')
    )
