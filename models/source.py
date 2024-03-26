import logging

from pydantic import BaseModel

from models.term_entry import TermEntry

logger = logging.getLogger(__name__)


class Source(BaseModel):
    """All sources have headers like this:

    global metapost
    högsta.Id 0

    metapost
    Status publicerad
    Källid 3222
    Titel Långsiktig strålskyddsforskning. Betänkande av Utredningen om strålskyddsforskning
    Titel.kortform Långsiktig strålskyddsforskning
    Titel.dokumentnr SOU 1994:40
    Titel.överordnad Excerpter ur Statens offentliga utredningar (SOU)
    Utgivningsår 1994
    Utgåvenr
    Ställe Bilaga 7 Ordlista och förkortningar, s. 217--227
    ISBN-kod 91-38-13608-2
    ISSN-kod 0375-250X
    Internkommentar
    Leverantörskommentar
    Sekretariatskommentar
    SAB-kod Oe
    URL http://weburn.kb.se/sou/472/urn-nbn-se-kb-digark-4717498.pdf
    URL-datum 2017-01-23
    Utgivare.1.urspr.organisation Miljö- och naturresursdepartementet
    Utgivare.1.urspr.författare
    Utgivare.1.urspr.kontaktperson
    Utgivare.1.urspr.e-post
    Utgivare.2.nu.organisation
    Utgivare.2.nu.författare
    Utgivare.2.nu.kontaktperson
    Utgivare.2.nu.e-post
    Klassifikationssystem.1.namn
    Klassifikationssystem.1.kortnamn
    Klassifikationssystem.1.url
    Klassifikationssystem.1.beskrivning
    Tolka.OKGR-märkning baraOmInteOrdklassSjälvklar
    Tolka.skillnadTermSynonym.förvalt troligenIngenSkillnad
    Tolka.skillnadTermSynonym.sv troligenIngenSkillnad
    """

    name: str
    path: str
    terms: list[TermEntry] = list()
    # source_id: Field("", alias="Källid")
    raw_metadata: dict[str, str] = dict()

    def parse_metadata(self):
        # parse all lines after metapost until next empty line into a dictionary
        # the lines are space separated key-value pairs
        logger.debug("parse_metadata: running")
        # exit()
        count = 0
        with open(file=self.path, mode="r", encoding="UTF8") as file:
            for line in file.readlines():
                count += 1
                logger.debug(f"working on count {count}, {line}")
                # discard line 1-4
                if count <= 4:
                    logger.debug("skipping line")
                    # exit()
                    continue
                elif line == "\n":
                    logger.debug("got empty line, breaking")
                    # exit()
                    break
                else:
                    logger.debug("found metadata")
                    content = line.split(" ")
                    self.raw_metadata[content[0]] = (
                        " ".join(content[1:]) if len(content) > 1 else ""
                    )
                    # exit()
        # pprint(self.raw_metadata)
        # exit()

    def parse_terms(self):
        # parse lines like this into a Term
        # terms are separated by an empty line
        # ignore first 3 lines, then ignore all lines until the first empty line
        logger.debug("parse_metadata: running")
        # exit()
        count = 0
        term = TermEntry()
        with open(file=self.path, mode="r") as file:
            for line in file.readlines():
                count += 1
                # Remove NBSP-characters
                line.replace("\xa0", " ")
                logger.debug(f"working on count {count}, {line}")
                # discard line 1- end of metadata + separating line
                skip_count = 4 + len(self.raw_metadata) + 1
                logger.debug(f"skip_count: {skip_count}")
                if count <= skip_count:
                    logger.debug(f"skipping line")
                    # exit()
                    continue
                # Strip the line here to avoid space related errors
                elif line.strip() == "":
                    logger.debug(
                        "got empty line, marking end of term and adding term to list"
                    )
                    self.terms.append(term)
                    # resetting term
                    term = TermEntry()
                    # exit()
                    # debug exit
                    # break
                else:
                    logger.debug("found term line")
                    if not len(term.raw_lines):
                        logger.debug(f"start line of this term: {count}")
                        term.line_start = count
                    term.raw_lines.append(line)
                    # overwrite the end line count
                    term.line_end = count
                    logger.debug(f"added line to term: {line}")
        # logger.info(f"number of terms found: {len(self.terms)}")
        # pprint(self.terms)
        # exit()

    def check_terms(self):
        for term in self.terms:
            logger.debug(f"working on path {self.path}")
            term.check_languages_and_control_words()

    def iterate_terms(self):
        """Debug method to show the terms one by one"""
        logger.debug("iterate_terms: running")
        for term in self.terms:
            print(
                f"terms: {term.term_lines}\n"
                f"definitions: {term.definition_lines}\n"
                f"annotations: {term.annotation_lines}"
            )
            input("press enter to show next")

    def start(self):
        self.parse_metadata()
        self.parse_terms()
        self.check_terms()
        # self.iterate_terms()
