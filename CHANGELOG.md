# [1.6.0] 2025-09-20

### Breaking Changes
- RGB values for `rgb(...)`, `fg(rgb(...))`, and `bg(rgb(...))` are now strictly validated. Out-of-range values (`<0` or `>255`) raise `ValueError`.

### New Features
- Full support for nested links and nested styles.
- Improved parsing for foreground/background colors in hex and RGB formats.

### Improvements
- Enhanced error messages for unknown or invalid tags.
- General parser performance and stability improvements for complex terminal markup.

# [1.5.0] 2025-08-29

### New Features
- Adds `Panel`, `Progressbar`, and `TermPicker`.
- Example usage available [here](https://github.com/birukbelihu/pyglow/raw/master/examples).

### Improvements
- Performance enhancements.

# [1.4.0] 2025-08-24

### New Features
- Adds `Table` and `Spinner`.
- Example usage available [here](https://github.com/birukbelihu/pyglow/raw/master/examples).

# [1.3.2] 2025-08-16

### New Features
- Case-insensitive tag names.
- Constants for colors (`Fore.BLUE`, `Back.GREEN`, `Style.BLINK`).
- Method `printc` for printing text with constants without manual reset.
- Hyperlink support.

# [1.2.7] 2025-08-14

### Improvements
- Suggestions for misspelt tags.
- Performance enhancements.

# [1.2.0] 2025-08-13

### Initial Release
- pyglow initial release.
