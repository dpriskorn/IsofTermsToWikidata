# ISOF terms to Wikidata
Det här är ett verktyg för att bearbeta och publicera termer från ISOF 
på ett sätt så de kan länkas ihop med koncepter på Wikidata.

## Offentlig verksamhet
Termerna har samlats ihop från många olika officiella rapporter dokument på svenska. 
Det finns termer på både svenska och engelska.

### TODO
* skrapa rikstermbanken.se och länka ihop?
* möjliggör att kolla upp varje term i Wikipedia
* create a webapp that helps editors upload missing terms 
or missing swedish translations of terms to Wikidata

### Statistik
Det finns ~93984 termer ($ grep -r TE .|wc -l)
49365 svenska $ grep -r ^svTE .|wc -l
11110 engelska $ grep -r ^enTE .|wc -l

Det finns ~30545 definitioner ($ grep -r DF .|wc -l)
28773 svenska $ grep -r ^svDF .|wc -l
1356 engelska $ grep -r ^enDF .|wc -l

Det finns ~16038 anteckningar ($ grep -r AN .|wc -l)
11356 svenska anteckningar $ grep -r ^svAN .|wc -l
331 engelska anteckningar $ grep -r ^enAN .|wc -l

Found 2366 sources with a total of 49266 terms and 175027 term lines in total.
19496 (39.57293062152397%) terms lack a definition
13851 (28.114724150529778%) terms lack a definition but has an explanation
5645 (11.458206470994195%) terms lack a definition and an explanation
49260 (99.9878212154427%) swedish terms

### Observationer
* Datan från ISOF innebär en del utmaningar pga bristen 
på enhetlig struktur. Tex är den svår att läsa rad för rad för 
varje rad är inte markerat upp 100% tex när definitioner fortsätter på ny rad.
* Datamängden saknar helt unika identifierare för varje term. Det är en stor brist som sänker värdet avsevärt.
* Bristen på GUPRI och API vittnar om att ISOF ser det här som ett arkiv, det pågår ingen förädling eller 
löpande kvalitetshöjning. Datan är "död" och utelämnas "as is".
* Datamängden verkar ha värde eftersom den 
  * kopplar ihop svenska och förvaltningsbegrepp på andra språk (mestadels engelska)
  * har vettiga definitioner
  * har vettiga anteckningar
  * har synonymer
  * har relationer till andra begrepp
* Datamängden saknar källor och författare. Det går inte att utläsa vem som skrivit vad. 
* Datamängden verkar sakna en "ägare" som går i god för innehållet, 
detta gäller både samlat och för varje term/källdokument.

# Erfarenheter
* På en helg lyckades jag begripa mig på och tvätta datan och 
skriva kod för att kunna läsa in det mesta i Pydantic objekter.
* En API/webbplats där varje term får en unik ID och presenteras via HTTP skulle vara ett stort lyft. 
Då skulle varje term kunna nås via internet och kunna länkas till. 
