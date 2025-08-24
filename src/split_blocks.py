"""
The Module helps to split Markdown syntax into blocks
"""


def markdown_to_blocks(markdown):
    """
    The function split Markdown syntax into blocks
    """
    list_of_blocks = []

    to_process = markdown.split("\n\n")

    for item in to_process:
        stripped = item.strip()
        if stripped == "":
            continue
        list_of_blocks.append(stripped)

    return list_of_blocks
