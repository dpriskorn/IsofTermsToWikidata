# Constants
control_words: list[str] = [
    "AN",  # anteckning
    "AVTE",  # avledd term?
    "BT",  # ?
    "DF",  # definition
    "ETYM",  # etymologi
    "EX",  # exempel?
    "FK",  # förklaring
    "KL",  # ?
    "PH", #?
    "RETE",  # relaterad term
    "RF",  # ?
    "SA",  # ?
    "SYTE",
    "TE",  # term
    "UPTE",  # ursprungsterm?
]
# control words are almost always prefixed by language
known_languages: list[str] = ["sv", "en", "fr", "la"]
unprefixed_control_words: list[str] = [
    "BNGR",
    "ETYM",
    "GNGR",
    "GR",
    "HONR",
    "ILLU",
    "INAN",
    "OKGR",
    "RF",
    "RIAN", #?
    "RIFR", #?
    "SA",  # ?
    "UT", # uttal
]
has_multiple: list[str] = ["svUPTE", "svSYTE"]
