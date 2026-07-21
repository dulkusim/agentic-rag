#Fixed size chunking of wine_list.md into 8000 character chunks with 800 character overlap

WINE_LIST = "./wine_list.md"

with open(WINE_LIST, "r", encoding="utf-8") as f:
    wine_list = f.read()

CHUNK_SIZE = 8000
CHUNK_OVERLAP = 800

chunks = []
start = 0
step = CHUNK_SIZE - CHUNK_OVERLAP

while start < len(wine_list):
    end = start + CHUNK_SIZE
    chunk = wine_list[start:end]
    chunks.append(chunk)
    start += step
    
for i in range(len(chunks)):
    with open(f"chunks_overlap/wine_list_{i+1}.md", "w", encoding="utf-8") as f:
        f.write(chunks[i])