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
╱╱╱╱╱╱╱╱v1.2.1╱╱╱╱╱╱╱╱╭━╯┃[localho3t]
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯{colored('(nginx)','green')}
""", 'red'), colored(f"""
[*] last update :  4 Jul 2023
[*] ideas : Coding with security ;)
""", 'green')
    )
