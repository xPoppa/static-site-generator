
def markdown_to_blocks(markdown: str) -> list[str]:
    new_lines =  markdown.split("\n")
    blocks: list[str] = []
    block = ""
    for idx, line in enumerate(new_lines):
        if line != "":
            block += " " + line
            if idx == len(new_lines) - 1:
                blocks.append(block)
        if line == "":
            blocks.append(block)
            block = ""
    for idx, bl in enumerate(blocks):
        blocks[idx] = bl.strip()
    return blocks
