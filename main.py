from pyglow.pyglow import Glow
from pyglow.styles.foreground import Fore
from pyglow.styles.background import Back
from pyglow.styles.style import Style
from pyglow.mapping import ANSI_RESET


def main():
    Glow.print("[green]Success: [bold]42 tests passed!!![/]")

    Glow.print("[bg-yellow black italic]Warning:[/] Low disk space.")

    Glow.print("[red bold]Error:[/] Something went wrong!")

    Glow.prints(r"""
                         _
 _ __    _   _    __ _  | |   ___   __      __
| '_ \  | | | |  / _` | | |  / _ \  \ \ /\ / /
| |_) | | |_| | | (_| | | | | (_) |  \ V  V /
| .__/   \__, |  \__, | |_|  \___/    \_/\_/
|_|      |___/   |___/

               """, style="hex(#0e76e6) BOLD")

    Glow.print(f"[link=https://github.com/birukbelihu/pyglow]pyglow GitHub[]")

    Glow.prints("Python glow", style="bold underline magenta")
    Glow.print("[bg-black Cyan]This is a test of the pyglow library.[/]")

    Glow.print("[rgb(255,56,0) italic underline]Red text[/]")
    Glow.print("[hex(#00FF00) bold dim]Green text[/]")

    Glow.print("[yellow bold Strike]Task completed[/]")

    print(f"{Fore.BRIGHT_YELLOW}{Back.CYAN}{Style.ITALIC} pyglow {ANSI_RESET}")

    Glow.print("[yellow bold Blink]Hey there do you like pyglow?[/]")

if __name__ == "__main__":
    main()
