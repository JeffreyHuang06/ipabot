import re
from typing import List, Match, Tuple

# regex is terrifying i hope i never have to modfiy this string again
slash_regex = r"/.+?/"
bracket_regex = r"\[.+?\]"

MatchList = list[Match[str]]

def detectslash(text: str) -> MatchList:
    ret: List[Tuple[Match[str], MatchList]] = []

    matches = re.finditer(slash_regex, text)

    for m in matches:
        matched_string = text[m.start(0) : m.end(0)]
        all_brackets = list(re.finditer(bracket_regex, matched_string))

        if all_brackets is not []: 
            ret.append((m, all_brackets))
    
    return ret

detectslash("/a[fgr]bgg/ /[gg]j[hi]/ ")
