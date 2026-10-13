> Denne side er genereret fra README.md og wiki/. Ændringer her bliver overskrevet, næste gang wikien udgives.

> Den engelske side er den gældende; denne oversættelse følger den.

[English](Home) | Dansk | [Bahasa Melayu](Home.ms)

# Snake-spillet (dag 24)

Det klassiske Snake-spil, bygget med Pythons `turtle`-modul. Det er opgaven fra dag 24 i Udemys *100 Days of Code: The Complete Python Pro Bootcamp*, som handler om det lokale filsystem og om at læse og skrive filer. En slange bevæger sig af sig selv hen over en sort skærm på 600 gange 600 og styres med piletasterne; den spiser mad og vokser, og tavlen øverst viser scoren og highscoren. Spillet slutter ikke: når hovedet passerer væggen eller rører sin egen hale, starter slangen og scoren forfra, og den bedste score gemmes i filen `data.txt`, så den stadig er der, næste gang du spiller.

## Styring

| Tast | Virkning |
| --- | --- |
| Op, Ned, Venstre, Højre | Drejer slangen |

Slangen vender aldrig direkte om på sig selv. Når hovedet kommer tættere end 15 pixels på den blå mad, spiser slangen den, vokser med ét led, og scoren stiger med 1.

## Highscore-filen

Highscoren gemmes som tekst i `data.txt` i den mappe, du starter spillet fra. Filen oprettes med `0` første gang. Vil du starte fra nul igen, så luk spillet og slet filen.

## Kør spillet

Der skal bruges Python 3.13 eller nyere med `tkinter`; spillet har ingen andre afhængigheder ved kørsel.

```bash
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/024-snake.git
cd 024-snake
python -m pip install -e .
python -m snake_game
```

Repositoriets README har den fulde opsætning til Windows, Linux og macOS.
