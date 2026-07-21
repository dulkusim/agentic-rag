#Recursive size chunking using langchain's RecursiveCharacterTextSplitter

from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", ".", " ", ""],
    chunk_size=8000,
    chunk_overlap=800,
    length_function=len
)

with open("chinese_menu.md", "r", encoding="utf-8") as f:
    chinese_menu = f.read()

texts = text_splitter.create_documents([chinese_menu])

for i in range(len(texts)):
    with open(f"./chunks_recursive/chunk_{i + 1}.md", "w", encoding="utf-8") as f:
        f.write(texts[i].page_content)