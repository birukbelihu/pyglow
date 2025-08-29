from pyglow.pyglow import Glow
from pyglow.mapping import ANSI_RESET
from pyglow.styles.background import Back
from pyglow.styles.foreground import Fore
from pyglow.styles.style import Style


def main():
 Glow.prints("Python glow", "bold underline magenta")
 Glow.print("[bg-black Cyan]This is a test of the pyglow library.[/]")

 Glow.print("[rgb(255,56,0) italic underline]Red subtitle[/]")
 Glow.print("[hex(#00FF00) bold dim]Green subtitle[/]")

 Glow.print("[yellow bold Strike]Task completed[/]")

 print(f"{Fore.BRIGHT_YELLOW}{Back.CYAN}{Style.ITALIC} pyglow {ANSI_RESET}")

 Glow.print("[yellow bold Blink]Hey there do you like pyglow?[/]")

if __name__ == "__main__":
    main()
