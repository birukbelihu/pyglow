from pyglow.pyglow import PyGlow


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

               """, style="hex(#0e76e6) bold")

    PyGlow.prints("Python Glow", style="bold underline magenta")
    PyGlow.print("[bg-black cyan]This is a test of the pyglow library.[/]")

    PyGlow.print("[rgb(255,56,0) italic underline]Red text[/]")
    PyGlow.print("[hex(#00FF00) bold dim]Green text[/]")

    PyGlow.print("[yellow bold strike]Task completed[/]")

    PyGlow.print("[yellow bold blink]Hey there do you like pyglow?[/]")


if __name__ == "__main__":
    main()
