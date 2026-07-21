from langchain_text_splitters import MarkdownHeaderTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter

with open("../data_folder/indian_menu.md", "r", encoding="utf-8") as f:
    indian_menu = f.read()

with open("../data_folder/chinese_menu.md", "r", encoding="utf-8") as f:
    chinese_menu = f.read()
    
with open("../data_folder/wine_list.md", "r", encoding="utf-8") as f:
    wine_list = f.read()

with open("../data_folder/drinks.md", "r", encoding="utf-8") as f:
    drinks = f.read()

with open("../data_folder/desserts.md", "r", encoding="utf-8") as f:
    desserts = f.read()

with open("../data_folder/restaurant_info.md", "r", encoding="utf-8") as f:
    restaurant_info = f.read()

            
headers_to_split_on = [
    ("#", "Header 1")
]

md_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on = headers_to_split_on,
    strip_headers = False
)

text_splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", ".", " ", ""],
    chunk_size=8000,
    chunk_overlap=800,
    length_function=len
)

indian_menu_chunks = md_splitter.split_text(indian_menu)
indian_menu_chunks = text_splitter.split_documents(indian_menu_chunks)

chinese_menu_chunks = md_splitter.split_text(chinese_menu)
chinese_menu_chunks = text_splitter.split_documents(chinese_menu_chunks)

wine_list_chunks = md_splitter.split_text(wine_list)
wine_list_chunks = text_splitter.split_documents(wine_list_chunks)

drinks_chunks = text_splitter.create_documents([drinks])
desserts_chunks = text_splitter.create_documents([desserts])
restaurant_info_chunks = text_splitter.create_documents([restaurant_info])

from datetime import datetime

for i, chunk in enumerate(indian_menu_chunks):
    current_id = f"indian_menu_{i}"
    
    chunk.metadata.update({
        "chunk_id": current_id,
        "source_file": "indian_menu.md",
        "domain": "menu",
        "type": "food",
        "category": "indian",
        "char_count": len(chunk.page_content),
        "last_updated": datetime.now().strftime("%Y-%m-%d"),
        "prev_chunk_id": f"indian_menu_{i-1}" if i > 0 else None,
        "next_chunk_id": f"indian_menu_{i+1}" if i < len(indian_menu_chunks) - 1 else None
    })

for i, chunk in enumerate(chinese_menu_chunks):
    current_id = f"chinese_menu_{i}"
    
    chunk.metadata.update({
        "chunk_id": current_id,
        "source_file": "chinese_menu.md",
        "domain": "menu",
        "type": "food",
        "category": "chinese",
        "char_count": len(chunk.page_content),
        "last_updated": datetime.now().strftime("%Y-%m-%d"),
        "prev_chunk_id": f"chinese_menu_{i-1}" if i > 0 else None,
        "next_chunk_id": f"chinese_menu_{i+1}" if i < len(chinese_menu_chunks) - 1 else None
    })

for i, chunk in enumerate(wine_list_chunks):
    current_id = f"wine_list_{i}"
    
    chunk.metadata.update({
        "chunk_id": current_id,
        "source_file": "wine_list.md",
        "domain": "menu",
        "type": "beverage",
        "category": "wine",
        "char_count": len(chunk.page_content),
        "last_updated": datetime.now().strftime("%Y-%m-%d"),
        "prev_chunk_id": f"wine_list_{i-1}" if i > 0 else None,
        "next_chunk_id": f"wine_list_{i+1}" if i < len(wine_list_chunks) - 1 else None
    })

for i, chunk in enumerate(drinks_chunks):
    current_id = f"drinks_{i}"
    
    chunk.metadata.update({
        "chunk_id": current_id,
        "source_file": "drinks.md",
        "domain": "menu",
        "type": "beverage",
        "category": "drinks",
        "char_count": len(chunk.page_content),
        "last_updated": datetime.now().strftime("%Y-%m-%d"),
        "prev_chunk_id": f"drinks_{i-1}" if i > 0 else None,
        "next_chunk_id": f"drinks_{i+1}" if i < len(drinks_chunks) - 1 else None
    })

for i, chunk in enumerate(desserts_chunks):
    current_id = f"desserts_{i}"
    
    chunk.metadata.update({
        "chunk_id": current_id,
        "source_file": "desserts.md",
        "domain": "menu",
        "type": "food",
        "category": "desserts",
        "char_count": len(chunk.page_content),
        "last_updated": datetime.now().strftime("%Y-%m-%d"),
        "prev_chunk_id": f"desserts_{i-1}" if i > 0 else None,
        "next_chunk_id": f"desserts_{i+1}" if i < len(desserts_chunks) - 1 else None
    })

for i, chunk in enumerate(restaurant_info_chunks):
    current_id = f"restaurant_info_{i}"
    
    chunk.metadata.update({
        "chunk_id": current_id,
        "source_file": "restaurant_info.md",
        "domain": "operations",
        "type": "information",
        "category": "restaurant",
        "char_count": len(chunk.page_content),
        "last_updated": datetime.now().strftime("%Y-%m-%d"),
        "prev_chunk_id": f"restaurant_info_{i-1}" if i > 0 else None,
        "next_chunk_id": f"restaurant_info_{i+1}" if i < len(restaurant_info_chunks) - 1 else None
    })

print(f"Indian Menu Chunks: {len(indian_menu_chunks)}")
print(f"Chinese Menu Chunks: {len(chinese_menu_chunks)}")
print(f"Wine List Chunks: {len(wine_list_chunks)}")
print(f"Drinks Chunks: {len(drinks_chunks)}")
print(f"Desserts Chunks: {len(desserts_chunks)}")
print(f"Restaurant Info Chunks: {len(restaurant_info_chunks)}")