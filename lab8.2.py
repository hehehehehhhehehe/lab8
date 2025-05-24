o = {
    1: "АВЕИНОРСТ",
    2: "ДКЛМПУ",
    3: "БГЁЬЯ",
    4: "ЙЫ",
    5: "ЖЗХЦЧ",
    8: "ШЭЮ",
    10: "ФЩЪ"
}
buk_o = {}
for kol, bk in o.items():
    for buk in bk:
        buk_o[buk] = kol

s = input("введите слово: ").upper()
score = sum(buk_o.get(char, 0) for char in s)
print(f"стоимость слова '{s}': {score} очков.")
