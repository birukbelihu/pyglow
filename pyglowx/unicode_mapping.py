ANSI_RESET = "\u001B[0m"

FOREGROUND_COLORS = {
    "black": "\u001B[30m",
    "red": "\u001B[31m",
    "green": "\u001B[32m",
    "yellow": "\u001B[33m",
    "blue": "\u001B[34m",
    "purple": "\u001B[35m",
    "magenta": "\u001B[35m",
    "cyan": "\u001B[36m",
    "white": "\u001B[37m"
}

BACKGROUND_COLORS = {
    "bg-black": "\u001B[40m",
    "bg-red": "\u001B[41m",
    "bg-green": "\u001B[42m",
    "bg-yellow": "\u001B[43m",
    "bg-blue": "\u001B[44m",
    "bg-purple": "\u001B[45m",
    "bg-magenta": "\u001B[45m",
    "bg-cyan": "\u001B[46m",
    "bg-white": "\u001B[47m"
}

STYLES = {
    "bold": "\u001B[1m",
    "dim": "\u001B[2m",
    "italic": "\u001B[3m",
    "underline": "\u001B[4m"
}

def preprocess(text: str) -> str:
    return text.strip().lower()

def contains_foreground_color(background_tag: str) -> bool:
    return background_tag in FOREGROUND_COLORS


def contains_background_color(tag: str) -> bool:
    return tag in BACKGROUND_COLORS


def contains_style(tag: str) -> bool:
    return tag in STYLES


def get_foreground_color(foreground_tag: str) -> str:
    return FOREGROUND_COLORS.get(preprocess(foreground_tag), "")


def get_background_color(background_tag: str) -> str:
    return BACKGROUND_COLORS.get(preprocess(background_tag), "")


def get_style(style_tag: str) -> str:
    return STYLES.get(preprocess(style_tag), "")
