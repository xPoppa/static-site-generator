
block_type_paragraph    = "paragrapgh"
block_type_heading      = "heading"
block_type_code         = "code"
block_type_quote        = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown: str) -> list[str]:
    raw_blocks: list[str] =  markdown.split("\n\n")
    blocks: list[str] = []
    for block in raw_blocks:
        if block != "":
            blocks.append(block.strip().strip("\n"))
    return blocks


def block_to_block_type(block: str) -> str:
## Heading
    if block[0:2] == "# ":
        return block_type_heading
    if block[0:3] == "## ":
        return block_type_heading
    if block[0:4] == "### ":
        return block_type_heading
    if block[0:5] == "#### ":
        return block_type_heading
    if block[0:6] == "##### ":
        return block_type_heading
    if block[0:7] == "###### ":
        return block_type_heading
## quote
    if block[0] == ">":
        result = []
        sub_blocks = block.replace("\n", " ")
        for sub_block in sub_blocks:
            result.append(sub_block[:1] == ">")
        if result.count(True) == len(result) and result:
            return block_type_quote
## code_block
    if block[0:3] == "```" and block[-3:] == "```": #and block[-4:-1] == "```":
        return block_type_code
## unordered list
    if block[0] == "*" or block[0] == "-":
        result = []
        sub_blocks = block.split("\n")
        for sub_block in sub_blocks:
            result.append(sub_block[:1] == "*" or sub_block[:1] == "-")
        if result.count(True) == len(result) and result:
            return block_type_unordered_list
## ordered list
    if block[0:2] == "1.":
        result = []
        sub_blocks = block.split("\n")
        for idx, sub_block in enumerate(sub_blocks):
            num = f"{idx + 1}."
            result.append(sub_block[0:2] == num)
        if result.count(True) == len(result) and result:
            return block_type_ordered_list
    return block_type_paragraph
