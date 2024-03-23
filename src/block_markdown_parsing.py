
def markdown_to_blocks(markdown: str) -> list[str]:
    blocks: list[str] =  markdown.split("\n\n")
    for idx, bl in enumerate(blocks):
        blocks[idx] = bl.replace("\n", " ").strip()
    return blocks
