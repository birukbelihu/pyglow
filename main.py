from pyglow.pyglow import PyGlow
from pyglow.ansi.foreground import Fore
from pyglow.ansi.background import Back
from pyglow.ansi.style import Style


def main():
    PyGlow.print("[green]Success: [bold]42 tests passed!!![/]")

    PyGlow.print("[bg-yellow black italic]Warning:[/] Low disk space.")

    PyGlow.print("[red bold]Error:[/] Something went wrong!")

    PyGlow.prints(r"""
                         _
 _ __    _   _    __ _  | |   ___   __      __
| '_ \  | | | |  / _` | | |  / _ \  \ \ /\ / /
| |_) | | |_| | | (_| | | | | (_) |  \ V  V /
| .__/   \__, |  \__, | |_|  \___/    \_/\_/
|_|      |___/   |___/

               """, style="hex(#0e76e6) BOLD")

    PyGlow.print(f"[link=https://github.com/birukbelihu/pyglow]pyglow GitHub[]")

    PyGlow.prints("Python Glow", style="bold underline magenta")
    PyGlow.print("[bg-black Cyan]This is a test of the pyglow library.[/]")

    PyGlow.print("[rgb(255,56,0) italic underline]Red text[/]")
    PyGlow.print("[hex(#00FF00) bold dim]Green text[/]")

    PyGlow.print("[yellow bold Strike]Task completed[/]")

    PyGlow.print("[yellow bold Blink]Hey there do you like pyglow?[/]")

    PyGlow.printc(f"{Fore.WHITE}{Back.BRIGHT_GREEN}{Style.STRIKE} pynum2words")
    PyGlow.printc(
        f"{Fore.BRIGHT_MAGENTA}{Style.ITALIC} pynum2words is a Python library for converting numbers to their word representation and vice versa, using a built-in or custom dictionary.")


if __name__ == "__main__":
    main()
