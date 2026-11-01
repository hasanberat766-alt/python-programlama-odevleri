
# ASCII karakter tablosu

print("ASCII KODU | KARAKTER")
print("----------------------")

for kod in range(128):
    if kod <= 31 or kod == 127:
        karakter = "Kontrol karakteri"
    elif kod == 32:
        karakter = "[boşluk]"
    else:
        karakter = chr(kod)

    print(f"{kod:<10} | {karakter}")
