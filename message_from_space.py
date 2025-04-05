import re

def spaceMessage(msg: str) -> str:
    pattern = re.compile(r'\[(\d+)([A-Z]+)\]')

    while '[' in msg:
        msg = re.sub(pattern, lambda m: int(m.group(1)) * m.group(2), msg)

    return msg


print(spaceMessage("ABCD"))

print(spaceMessage("AB[3CD]"))

print(spaceMessage("IF[2E]LG[5O]D"))