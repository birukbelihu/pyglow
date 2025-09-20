from pyglow.pyglow import Glow
from pyglow.mapping import ANSI_RESET
from pyglow.styles.background import Back
from pyglow.styles.foreground import Fore
from pyglow.styles.style import Style


def main():
    Glow.prints("Python Glow Library Demo", "bold underline magenta")
    Glow.print("[bg-black Cyan]This is a test of the pyglow library.[/]")

    Glow.print("[rgb(255,56,0) italic underline]Red subtitle[/]")
    Glow.print("[hex(#00FF00) bold dim]Green subtitle[/]")

    Glow.print("[yellow bold strike]Task completed[/]")

    print(f"{Fore.BRIGHT_YELLOW}{Back.CYAN}{Style.ITALIC}pyglow{ANSI_RESET}")

    Glow.print("[yellow bold blink]Hey there! Do you like pyglow?[/]")

    Glow.print("[bg-blue][fg(rgb(255,255,0)) bold underline]Nested styles with colors[/][/]")

    Glow.print("[link=https://github.com/birukbelihu/pyglow][fg(rgb(0,255,255)) bold]Click me![/][/link]")

    Glow.print(
        "[fg(rgb(255,0,0))]Red[/] "
        "[fg(rgb(0,255,0))]Green[/] "
        "[fg(rgb(0,0,255))]Blue[/]"
    )

if __name__ == "__main__":
    main()
