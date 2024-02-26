# Constants
control_words: list[str] = [
    "AN",  # anteckning
    "AVTE",  # avledd term?
    "BT",  # ?
    "DF",  # definition
    "EKVI",
    "ETYM",  # etymologi
    "EX",  # exempel?
    "FK",  # förklaring
    "KL",  # ?
    "KT",
    "PH",  # ?
    "RETE",  # relaterad term
    "RF",  # ?
    "SA",  # ?
    "SU",
    "SYPH",
    "SYTE",
    "TE",  # term
    "TI",
    "UPTE",  # ursprungsterm?
]
# control words are almost always prefixed by language
known_languages: list[str] = [
    "ar",
    "da",
    "de",
    "sv",
    "en",
    "fr",
    "hr",
    "fi",
    "ru",
    "no",
    "is",
    "la",
    "sq",
    "rm",
    "ra",
    "rk",
    "se",
    "es",
    "ja",
    "pl",
    "so",
    "tr"
]
unprefixed_control_words: list[str] = [
    "BNGR",
    "ETYM",
    "FRKT",
    "GNGR",
    "GE",
    "GR",
    "HONR",
    "ILLU",
    "INAN",
    "INID",
    "ILLT",
    "ILTY",
    "KL",
    "OKGR",
    "RF",
    "RIAN",  # ?
    "RIFR",  # ?
    "SA",  # ?
    "SPBR",
    "UT",  # uttal
]
has_multiple: list[str] = ["svUPTE", "svSYTE"]
