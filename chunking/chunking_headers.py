#Chunking on headers using langchain's MarkdownHeaderTextSplitter

from langchain_text_splitters import MarkdownHeaderTextSplitter

headers_to_split_on = [
    ("#", "Header 1")
]

text_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on = headers_to_split_on,
    strip_headers=False
)

with open("../data_folder/indian_menu.md", "r", encoding="utf-8") as f:
    chinese_menu = f.read()

texts = text_splitter.split_text(chinese_menu)

for i in range(len(texts)):
    with open(f"./chunks_headers/chunks_{i+1}.md", "w", encoding="utf-8") as f:
        f.write(texts[i].page_content)

for i in range(len(texts)):
    texts[i].metadata.update(
        {
            "source": "chinese_menu.md",
            "chunk_index": i,
         }
    )

for i in range(len(texts)):
    with open(f"./chunks_headers/metadata_{i+1}.md", "w", encoding="utf-8") as f:
        f.write(str(texts[i].metadata))