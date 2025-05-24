st = {
    "Канада": "Оттава",
    "Бразилия": "Бразилиа",
    "Германия": "Берлин",
    "Швеция": "Стокгольм",
    "Россия": "Москва"
}
st_lower = {str.lower(): stol for str, stol in st.items()}
# a
print("страны и столицы:")
for str, stol in st.items():
    print(f"{str} — {stol}")
# b
str_name = input("\nвведите название страны: ").strip().lower()
if str_name in st_lower:
    print(f"страна {str_name.title()} — столица {st_lower[str_name]}")
else:
    print("такой страны нет в списке.")
# c
print("\nотсортированный список стран:")
for str in sorted(st):
    print(f"{str} — {st[str]}")