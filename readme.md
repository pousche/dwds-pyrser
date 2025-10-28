# DWDS Parser

A simple app for parse the content of a DWDS article into the following categories:
- **Vokabular**: The word in question.
- **Grammatik**: A short overview of the grammar of the expression.
- **Bedeutung**: The meaning(s) of the word.
- **Beispiele**: Examples corresponding to each meaning.
- **Bedeutungsverwandte**: Related words with a similar meaning.

The formatting is specifically designed for usage with [A German Learner's Deck](https://ankiweb.net/shared/info/1481153793).
# Install

Just download the latest release [here](https://github.com/pousche/dwds-pyrser/releases) and run it.
# How to use

Type your word into the "Vokabular" and press {Enter} or click away. The content will be parsed automatically. You can change the number of examples shown by moving the slider next to the examples fields. Each text field has a copy button next to it for easier transfer of the content. To avoid the tedious copy pasting you can adapt the provided [AutoHotKey script](https://github.com/pousche/dwds-pyrser/blob/main/keyboard_shortcuts.ahk) to your screen and window location. I would recommend using [PowerToys](https://github.com/microsoft/PowerToys) to get a consistent positioning using FancyZones and the relative location of the buttons using the ScreenRuler.
