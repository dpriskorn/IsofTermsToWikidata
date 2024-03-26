from models.term import Term


class TestTerm:
    def test_definition_lines(self):
        t = Term(
            raw_lines=[
                "svTE brandfarlig vara",
                "svDF Dels gasformig vara som vid en temperatur av +21 °C eller därunder kan antändas och brinna i luft (brandfarlig gas), dels flytande eller halvfast vara med en flampunkt av högst +60°C samt (oavsett flampunkten) dieselolja och eldningsolja (brandfarlig vätska).",
                "   Se vidare SFS 1961:568 och 1973:584.",
            ]
        )
        assert len(t.sv_termlines) == 1
        assert t.sv_termlines[0] == "brandfarlig vara"
        assert len(t.definition_lines) == 2
        assert t.definition_lines[0] == ("Dels gasformig vara som vid en temperatur av +21 °C "
                                         "eller därunder kan antändas och brinna i luft (brandfarlig gas), "
                                         "dels flytande eller halvfast vara med en flampunkt av högst +60°C "
                                         "samt (oavsett flampunkten) dieselolja och eldningsolja (brandfarlig vätska).")
        assert t.definition_lines[1] == "Se vidare SFS 1961:568 och 1973:584."

    def test_multiple_explanation_lines(self):
        t = Term(
            raw_lines="""svTE kvalificerad majoritet
svFK Från utvidgningen den 1 maj 2004 kommer tillfälliga regler tillämpas för definition av kvalificerad majoritet fram till första november 2004. Sedan gäller att kvalificerad majoritet kräver dels 232 röster av 321 (72,3 %) dels en majoritet, eller i vissa fall två tredjedelar, av antalet medlemsländer samt, om ett medlemsland begär det, att länder som representerar 62 % av EU:s befolkning skall stå bakom förslaget. Röstfördelningen kommer att vara följande:
   Tyskland, Frankrike, Italien och Storbritannien 29
   Spanien och Polen 27
   Nederländerna 13
   Belgien, Tjeckien, Grekland, Ungern och Portugal 12
   Österrike och Sverige 10
   Danmark, Irland, Litauen, Slovakien och Finland 7
   Cypern, Estland, Lettland, Luxemburg and Slovenien 4
   Malta 3
RIFR Stämmer detta eller bör det uppdateras?""".split("\n")
        )
        assert len(t.sv_termlines) == 1
        assert len(t.explanation_lines) == 9
        assert t.explanation_lines[8] == "Malta 3"
