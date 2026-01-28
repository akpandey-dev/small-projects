import keyboard, time, sys, random, colorama, string
colorama.init()

code_dict = {
  "a": "😎",
  "b": "😁",
  "c": "😂",
  "d": "🤣",
  "e": "😃",
  "f": "😄",
  "g": "😅",
  "h": "😆",
  "i": "😉",
  "j": "😊",
  "k": "😋",
  "l": "😀",
  "m": "😍",
  "n": "😘",
  "o": "😗",
  "p": "😙",
  "q": "😚",
  "r": "☺️",
  "s": "🙂",
  "t": "🤗",
  "u": "🤩",
  "v": "🤔",
  "w": "🤨",
  "x": "😐",
  "y": "😑",
  "z": "😶",
  " ": "👽",
  ".": "🔸",
  ",": "🔹",
  "?": "❓",
  "!": "❗",
  "(": "🅾️",
  ")": "🅿️",
  "[": "🪧",
  "]": "🔲",
  "{": "🧃",
  "}": "🥤",
  "'": "👈",
  "\"": "👉",
  "+": "➕",
  "-": "➖",
  "*": "✳️",
  "/": "➗",
  "=": "🟰",
  "<": "⬅️",
  ">": "➡️",
  ":": "🔽",
  ";": "🔼",
  "@": "📧",
  "#": "🔢",
  "&": "🤝",
  "%": "📊",
  "|": "🚪",
  "^": "⏫",
  "~": "🌊",
  "_": "⬛",
  "₹": "💰",
  "$": "💵",
  "€": "💶",
  "£": "💷",
  "¥": "💴",
  "\n": "🔁"
}
def conv_func(encTxt):
    encoded = []
    for n in encTxt:
        emoji = code_dict.get(n, n)  
        encoded.append(emoji)
    return "".join(encoded)

inputTxt = input("Type the text here...")
print(conv_func(inputTxt))