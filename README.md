# PR-Razlogi-za-brezposelnost-v-sloveniji

Brezposelnost v Sloveniji 

Rudarili bomo podatke o brezposelnosti v Sloveniji. Za temo smo se odločili, ker bi radi spoznali dejavnike, ki vplivajo na brezposelnosti in dobili boljsi vpogled v problematiko zaposlitev.

VPRASANJE 1
Kako dosezena stopnja izobrazbe vpliva na brezposelnost? 
CILJ 1
Ugotoviti, kako smiselna je visoka izobrazba pri resevanju problema brezposelnosti

VPRASANJE 2
Kako regija prebivalisca vpliva na brezposelnost?
CILJ 2
Ugotoviti, ali regija prebivalisca vpliva na brezposelnost prebivalcev in preveriti, ce se je z uvedbo “remote” dela  ta vpliv zmanjsal.

VPRAŠANJE 3
Ali regija vpliva na zaposljivost neke izobrazbe?
CILJ 3
Ugotoviti katera stopnja izobrazbe ima najboljso moznost zaposlitve v doloceni regiji




PODATKI
Podatke smo vecinoma crpali iz odprtih podatkov o republiki Slovenije (podatki.gov.si).
Vecina virov je ima malo atributov, zato potrebujemo virov vec.
Podatki so zapisani v PCAXIS formatu. PCAXIS je format datoteke za statistične podatke, ki se uporablja predvsem v Evropi. Ta format datoteke se uporablja za izmenjavo in arhiviranje statističnih podatkov med različnimi uporabniki in programi. Datoteke PCAXIS vsebujejo opisne metapodatke, ki opisujejo vsebino podatkov, ter številske vrednosti, ki predstavljajo statistične podatke. Vsebujejo lahko eno ali več tabel s podatki. Za uporabo datotek PCAXIS v procesu rudarjenja podatkov je treba najprej uvoziti podatke iz datoteke v orodje za analizo podatkov, ali pa jih pretvoriti v zeljeno obliko.

Imamo pa tudi podatke, ki so zapisani tabelaricno.

Za tocno obliko podatkov, s katerimi bomo delali se se nismo odlocili, saj bot a odvisna oz analiticnih metod, ki jih bomo izbrali.
<https://podatki.gov.si/dataset/surs0762112s>

<https://podatki.gov.si/dataset/surs05g3050s>

[https://www.ess.gov.si/partnerji/trg-dela/trg-dela-v-stevilkah/registrirana-brezposelnost/](https://www.ess.gov.si/partnerji/trg-dela/trg-dela-v-stevilkah/registrirana-brezposelnost/%20)** 

# Vpliv korone da delovno aktivnost
*Notebook povzema število brezposelnih in delavno aktivnih prebivalcev po kohezijskih regijah pred, med in po koroni*

**Delitev na obdobja:**
<ul>
    <li>pred: (∞, marec 2020)</li>
    <li>med: [marec 2020, december 2021]</li>
    <li>po: [januar 2022, ∞)</li>
</ul>

Iz grafov je možno razbrati štiri stvari stvari
1. Število brezposelnih pri ljudeh ki niso zaposleni leto ali več se spreminja počasi v primerjavi z ljudmi, ki so brez dela krajši čas, kjer se število brezposelnih spreminja bolj drastično. **Torej imajo ljudje ki so brezposelni dlje časa manjšo verjetnost, da dobijo službo**
2. Vidimo da je vsaka skupina daljše časovne brezposelnosti posledica skupine krajše časovne brezposelnosti ki ohranja trend naraščanja in padanja, a s časovnim zamikom dveh mesecev, ko nekateri ljudje nižje časovno brezposelne skupine prestopijo v višjo časovno skupino. To se na grafu izkaže kot zakasnjen trend z manjšim številom nezaposlenih, kar nam omogora izračun deleža ljudi, ki je v razponu dveh mesecov našlo službo  
3. Trend brezposelnosti z leti pada *zanimivo bi bilo ugotoviti ali se izobrazba giba v drugo smer*, se pravi da se z večanjem izobraženosti družbe niža brezposelnost
4. Brezposelnost je na časovno lokalno gledano periodičen pojav. Z vrhunci ob začetkih let in minimumi poleti(sredi leta).

Ob začetku korone se je število brezposelnih močno povečalo in ostalo visoko do okoli **tretjega vala**. Torej sta prva dva vala veliki prelomnici, ki narekujeta rast brezposelnosti med korono.

**Zanimiv pojav je dvig števila brezposelnih z začetkom novega leta**
