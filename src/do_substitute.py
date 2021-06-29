from src.detection import MatchList
from typing import Dict, Match

subs: Dict[str, str] = {
    'epsilon': 'ɛ',
    'hit': 'ɪ',
    'ash': 'æ',
    '3': 'ɜ',
    'schwa': 'ə',
    'theta': 'θ',
    'eth': 'ð',
    'omega': 'ʊ',
    'sh': 'ʃ',
    'integral': 'ʃ',
    'rhotic': 'ɹ',
    'lambda': 'ʌ',
    'carot': 'ʌ',
    '?': 'ʔ',
    'ng': 'ŋ',
    'zh': 'ʒ',
    'gamma': 'ɤ',
    'baby gamma': 'ɤ',
    'alpha': 'ɑ',
    'backwards alpha': 'ɒ',
    'close central unrounded': 'ɨ',
    'close central rounded': 'ʉ',
    'close back unrounded': 'ɯ',
    'near-close near-front rounded': 'ʏ',
    'close-mid front rounded': 'ø',
    'close-mid central rounded': 'ɵ',
    'open-mid back rounded': 'ɔ',
    'open back rounded': 'ɒ'
}

def substitute_slash(text: str, brackets: MatchList) -> str:
    for match in brackets:
        matched_str = match.string[match.start(0): match.end(0)]

        if matched_str[1:-1] in subs:
            text = text.replace(matched_str, subs[matched_str[1:-1]])
    
    return text

def do_substitute(text: str, matches: list[tuple[Match[str], MatchList]]):
    replacements: list[tuple[str, str]] = []

    for match, brackets in matches:
        matched_text = text[match.start(0): match.end(0)]

        subed_str = substitute_slash(matched_text, brackets)
        
        replacements.append((matched_text, subed_str))
    
    for old, new in replacements:
        text = text.replace(old, new)
    
    return text

# st = "$ipa i think /[epsilon][hit]/ is better than /[epsilon]j/"
# d = detectslash(st)
# print(do_substitute(st, d))
