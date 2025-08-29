from pyglow.views.termpicker import TermPicker
from pyglow.styles.foreground import Fore

def main():
    languages = ["Java", "Python", "C", "C++", "Rust"]

    term_picker = TermPicker(
                        languages,
                        "Select a language",
                        Fore.BLUE,
                        "*")

    choice = term_picker.pick()

    print(f"\n✅ You selected: {choice}")

if __name__ == "__main__":
    main()