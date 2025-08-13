from .parser import GlowPyParser

class PyGlowx:

    @staticmethod
    def parse(text: str) -> str:
        parsed_text, _ = GlowPyParser.parse_recursively(text)
        return parsed_text

    @staticmethod
    def print(text: str):
        print(PyGlowx.parse(text))

    @staticmethod
    def prints(text: str, style: str):
        PyGlowx.print(f"[{style}]{text}[/]")