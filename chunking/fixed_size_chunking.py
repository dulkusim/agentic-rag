#Fixed size chunking of wine_list.md into 8000 character chunks

WINE_LIST = "./wine_list.md"

with open(WINE_LIST, "r", encoding="utf-8") as f:
    wine_list = f.read()

k = 1
for i in range(0,len(wine_list),8000):
    with open(f"./chunks_fixed/wine_list_{k}.md", "w", encoding="utf-8") as f:
        f.write(wine_list[i:i+8000])
    k += 1