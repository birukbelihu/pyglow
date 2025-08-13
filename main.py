from pyglowx.pyglowx import PyGlowx

def main():
 PyGlowx.print("[green]Success: [bold]42 tests passed!!![/]")

 PyGlowx.print("[bg-yellow black italic]Warning:[/] Low disk space.")

 PyGlowx.print("[red bold]Error:[/] Something went wrong!")

 PyGlowx.prints(r"""
 _ __    _   _    __ _  | |   ___   __      __ __  __
| '_ \  | | | |  / _` | | |  / _ \  \ \ /\ / / \ \/ /
| |_) | | |_| | | (_| | | | | (_) |  \ V  V /   >  <
| .__/   \__, |  \__, | |_|  \___/    \_/\_/   /_/\_\
|_|      |___/   |___/
               """, "hex(#0e76e6) bold")

 PyGlowx.prints("Python Glow", "bold underline magenta")
 PyGlowx.print("[bg-black cyan]This is a test of the pyglowx library.[/]")

 PyGlowx.print("[rgb(255,56,0) italic underline]Red text[/]")
 PyGlowx.print("[hex(#00FF00) bold dim]Green text[/]")

 PyGlowx.print("[yellow bold strike]Task completed[/]")

 PyGlowx.print("[yellow bold blink]Hey there do you like pyglowx?[/]")

if __name__ == "__main__":
    main()