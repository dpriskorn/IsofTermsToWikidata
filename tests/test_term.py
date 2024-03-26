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
