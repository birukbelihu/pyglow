import re
import pytest
from pyglow.parser import Parser
from pyglow.mapping import get_style

def strip_ansi(text):
    return re.sub(r"\x1b\[[0-9;]*m|\033]8;;.*?\033\\", "", text)

def test_basic_rgb_foreground():
    s = "[rgb(255,0,0)]Red[/]"
    result = Parser.parse(s)
    assert "\u001b[38;2;255;0;0m" in result
    assert "Red" in strip_ansi(result)

def test_hex_foreground():
    s = "[hex(#00FF00)]Green[/]"
    result = Parser.parse(s)
    assert "\u001b[38;2;0;255;0m" in result
    assert "Green" in strip_ansi(result)

def test_fg_bg_hex():
    s = "[fg(#0000FF)][bg(#FFFF00)]Blue on Yellow[/]"
    result = Parser.parse(s)
    assert "\u001b[38;2;0;0;255m" in result
    assert "\u001b[48;2;255;255;0m" in result
    assert "Blue on Yellow" in strip_ansi(result)

def test_fg_bg_rgb():
    s = "[fg(rgb(128,128,128))][bg(rgb(255,128,0))]Gray on Orange[/]"
    result = Parser.parse(s)
    assert "\u001b[38;2;128;128;128m" in result
    assert "\u001b[48;2;255;128;0m" in result
    assert "Gray on Orange" in strip_ansi(result)

def test_style_from_mapping():
    s = "[bold]Bold Text[/]"
    result = Parser.parse(s)
    ansi_code = get_style("bold")
    assert ansi_code in result
    assert "Bold Text" in strip_ansi(result)

def test_simple_link():
    s = "[link=https://example.com]Click[/link]"
    result = Parser.parse(s)
    assert "\033]8;;https://example.com\033\\" in result
    assert "Click" in strip_ansi(result)

def test_nested_link_and_style():
    s = "[link=https://example.com][fg(rgb(255,0,255))][bold]Nested[/][/link]"
    result = Parser.parse(s)
    assert "\033]8;;https://example.com\033\\" in result
    assert "\u001b[38;2;255;0;255m" in result
    assert get_style("bold") in result
    assert "Nested" in strip_ansi(result)

def test_multiple_styles():
    s = "[fg(#FF0000)][bg(#00FF00)][bold]Multiple[/]"
    result = Parser.parse(s)
    assert "\u001b[38;2;255;0;0m" in result
    assert "\u001b[48;2;0;255;0m" in result
    assert get_style("bold") in result
    assert "Multiple" in strip_ansi(result)

@pytest.mark.parametrize("input_str", [
    "[rgb(300,0,0)]Invalid RGB[/]",    # Out of range
    "[fg(rgb(0,0,256))]Invalid FG[/]", # Out of range
    "[bg(rgb(0,-1,0))]Invalid BG[/]"   # Negative value
])
def test_invalid_rgb(input_str):
    with pytest.raises(ValueError):
        Parser.parse(input_str)
