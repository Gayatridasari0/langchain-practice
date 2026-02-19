from langchain_text_splitters import MarkdownHeaderTextSplitter

markdown_text = """
# Cricket

Cricket is a popular sport played worldwide.

## Formats

There are three main formats:
- Test
- ODI
- T20

## Famous Players

Sachin Tendulkar is one of the greatest players.

# Football

Football is the most popular sport globally.
"""

headers_to_split_on = [
    ('#', 'Header 1'),
    ('##', 'Header 2')
]

splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on
)

docs = splitter.split_text(markdown_text)

for doc in docs:
    print("CONTENT:\n", doc.page_content)
    print("METADATA:\n", doc.metadata)
    print("-----")