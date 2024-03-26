from pydantic import BaseModel

from constants import known_languages, control_words, unprefixed_control_words
from models.exceptions import UnknownCombination


class TermEntry(BaseModel):
    """Klass för en term.
    En term kan ha flera linjer med samma kontrolord.
    Formatet är svårt att tolka.
    Specifikation av formatet har inte ISOF så det är take it or leave it"""

    """
    svTE MR
    svSYTE MRI
    svSYTE MRT
    svSYTE magnetisk resonanstomografi
    svFK Avbildningsmetod som utnyttjar väteatomkärnors egenskap att då de befinner sig i ett starkt homogent magnetfält återsända pulser av radiovågor. Pulserna som detekteras utanför patienten innehåller sådan information om väteförekomst (vattenhalt) och kemisk bindning att detaljerade snittbilder av kroppen kan byggas upp
    svRETE CT
    data/Offentlig_verksamhet/Departement/Miljö- och naturresursdepartementet/SOU_1994_40.txt

    svTE internationell militär insats
    svDF verksamhet som Försvarsmakten bedriver i ett insatsområde utomlands i syfte att
       a) avvärja risk för en väpnad konflikt,
       b) hejda en pågående väpnad konflikt,
       c) övervaka överenskommelser om fred och vapenstillestånd, eller
       d) skapa förutsättningar för varaktig fred och säkerhet genom humanitärt arbete i samband med en väpnad konflikt
    data/Offentlig_verksamhet/Departement/Försvarsdepartementet/SFS/SFS_2012_332.txt

    svTE fartygsregister
    svUPTE skepp
    svUPTE båt
    svFK Svenskt fartyg som används yrkesmässigt för befordran av gods eller passagerare skall införas i skepps- eller båtregister. Fartyg med största längd av minst tolv meter och bredd av minst fyra meter betecknas skepp. Annat fartyg kallas båt.
    data/Offentlig_verksamhet/Departement/Utbildningsdepartementet/SOU/SOU_1989_07.txt

    svTE MCM
    svDF elektronisk krets som integreras och kapslas som en enhet
    enTE multi-chip-module
    enSYTE MCM
    data/Offentlig_verksamhet/Departement/Utbildningsdepartementet/SOU/SOU_1997_37.txt

    svTE folkhälsoarbete
    svUPTE promotion
    svUPTE prevention
    svDF arbete på alla nivåer i samhället och inom flertalet sektorer i samverkan för att främja människors hälsa
    svAN Kommuner är huvudaktörer eftersom de har det primära samhällsansvaret för medborgarnas välfärd. I kommunerna finns dessutom flera verksamheter som är viktiga områden för folkhälsoarbete; skola, fritid, barnomsorg, socialtjänst, miljö- och hälsoskydd, kultur och idrotts- och annan föreningsverksamhet. Folkhälsoarbetet består av flera komponenter:
     ·  att främja hälsa (promotion), att skapa förutsättningar för människor att leva ett gott liv och främja sin hälsa utifrån sina egna kunskaper.
     ·  att förebygga ohälsa (prevention), handlar om eliminering av riskfaktorer för sjukdom, skador och ohälsa, oftast insatser innan sjukdom uppstått (primärprevention). (SOU 1997:119, En tydligare roll för hälso- och sjukvården i folkhälsoarbetet, s. 31).
    data/Offentlig_verksamhet/Departement/Utbildningsdepartementet/SOU/SOU_2000_19.txt
    
    svTE kvalificerad majoritet
    svFK Från utvidgningen den 1 maj 2004 kommer tillfälliga regler tillämpas för definition av kvalificerad majoritet fram till första november 2004. Sedan gäller att kvalificerad majoritet kräver dels 232 röster av 321 (72,3 %) dels en majoritet, eller i vissa fall två tredjedelar, av antalet medlemsländer samt, om ett medlemsland begär det, att länder som representerar 62 % av EU:s befolkning skall stå bakom förslaget. Röstfördelningen kommer att vara följande:
       Tyskland, Frankrike, Italien och Storbritannien 29
       Spanien och Polen 27
       Nederländerna 13
       Belgien, Tjeckien, Grekland, Ungern och Portugal 12
       Österrike och Sverige 10
       Danmark, Irland, Litauen, Slovakien och Finland 7
       Cypern, Estland, Lettland, Luxemburg and Slovenien 4
       Malta 3
    RIFR Stämmer detta eller bör det uppdateras?
    data/Offentlig_verksamhet/Regeringen/Regeringskansliet/Regeringskansliet/EUordlista_Regeringskansliet_imkand.txt
    """

    # todo hantera flera synonymer och upte
    # hantera annotation och definition som html
    # synonym: list[str] = list()
    # upte: list[str] = list()
    # term: Field("", alias="svTE")
    # description: Field("", alias="svDF")
    # annotation: Field("", alias="svAN")
    # rete: Field("", alias="svRETE")
    # pronounciacion: Field("", alias="UT")
    # sa: Field("", alias="svSA")
    # etymology: Field("", alias="ETYM")
    # fk: Field("", alias="svFK")
    # rifr: Field("", alias="RIFR")
    # kl: Field("", alias="KL")
    raw_lines: list[str] = list()
    line_start: int = 0
    line_end: int = 0

    @property
    def sv_related_termlines(self):
        return self.get_specific_line_content(control_word="svRETE")

    @property
    def en_related_termlines(self):
        return self.get_specific_line_content(control_word="enRETE")

    @property
    def fr_related_termlines(self):
        return self.get_specific_line_content(control_word="frRETE")

    @property
    def fr_termlines(self) -> list[str]:
        return self.get_specific_line_content(control_word="frTE")

    @property
    def en_termlines(self) -> list[str]:
        return self.get_specific_line_content(control_word="enTE")

    @property
    def sv_termlines(self) -> list[str]:
        return self.get_specific_line_content(control_word="svTE")

    def get_specific_line_content(
        self, control_word: str = "", control_words=None
    ) -> list[str]:
        """This returns the content without the control word and first space after
        NOTE: it does not yet support multi-line entries"""
        if control_words is None:
            control_words = list()
        lines = []
        # TODO make this support multi-line entries
        for line in self.raw_lines:
            space_split_list = line.split(" ")
            if space_split_list:
                # logger.debug(f"split line: {space_split_list}")
                first_word = space_split_list[0]
                if first_word == control_word or first_word in control_words:
                    # Join the value with spaces before adding it to the list.
                    lines.append(" ".join(space_split_list[1:]).strip())
        return lines

    @property
    def term_lines(self) -> list[str]:
        return self.get_specific_line_content(
            control_words=self.term_language_control_word_combinations
        )

    @property
    def definition_lines(self) -> list[str]:
        return self.get_specific_line_content(
            control_words=self.definition_language_control_word_combinations
        )

    @property
    def annotation_lines(self) -> list[str]:
        return self.get_specific_line_content(
            control_words=self.annotation_language_control_word_combinations
        )

    @property
    def explanation_lines(self) -> list[str]:
        return self.get_specific_line_content(
            control_words=self.explanation_language_control_word_combinations
        )

    @property
    def term_language_control_word_combinations(self) -> list[str]:
        return self.control_word_combinations_for_all_languages(control_word="TE")

    @property
    def definition_language_control_word_combinations(self) -> list[str]:
        return self.control_word_combinations_for_all_languages(control_word="DF")

    @property
    def annotation_language_control_word_combinations(self) -> list[str]:
        return self.control_word_combinations_for_all_languages(control_word="AN")

    @property
    def explanation_language_control_word_combinations(self) -> list[str]:
        return self.control_word_combinations_for_all_languages(control_word="FK")

    @staticmethod
    def control_word_combinations_for_all_languages(control_word: str) -> list[str]:
        combinations = list()
        for language in known_languages:
            combinations.append(f"{language}{control_word}")
        # logger.debug(f"generated combinations: {combinations}")
        return combinations

    @property
    def all_language_control_word_combinations(self) -> list[str]:
        """This is used for checking that we recognize
        all control words and all languages that appear"""
        combinations = list()
        for language in known_languages:
            for word in control_words:
                combinations.append(f"{language}{word}")
        for unprefixed_control_word in unprefixed_control_words:
            combinations.append(unprefixed_control_word)
        # logger.debug(f"generated combinations: {combinations}")
        return combinations

    def parse_multiple_fields(self):
        pass

    def check_languages_and_control_words(self):
        # throw an exeption if all lines do not start with
        # 1) a space (continuation of former line)
        # 2) a language
        # 3) known unprefixed control
        for line in self.raw_lines:
            if line == "\n":
                line = ""
            first_word = line.split(" ")[0]
            if len(first_word):
                if first_word in self.all_language_control_word_combinations:
                    # logger.debug(f"recognized control word: {first_word}")
                    pass
                else:
                    # if not first_word == "\n":
                    raise UnknownCombination(f"'{first_word}' in {line}")
            else:
                # first word was empty == continuation line
                # logger.debug("found continuation line")
                pass

    def has_control_word(self, line: str) -> bool:
        first_word = line.split(" ")[0]
        if len(first_word):
            if first_word in self.all_language_control_word_combinations:
                return True
        return False

    @property
    def raw_line_count(self) -> int:
        return len(self.raw_lines)
