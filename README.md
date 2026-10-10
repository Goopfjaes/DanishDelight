# Dansk Delight

Traditionel dansk mad som tilføjelse til **Farmer's Delight**.

- Minecraft **1.20.1**
- Forge **47.4.20**
- Kræver **Farmer's Delight** (testet mod 1.2.10 – `FarmersDelight-1.20.1-1.2.10.jar`)

## Nye ting

| Ting | Type | Opskrift (Farmer's Delight Cooking Pot) |
|---|---|---|
| **Kulør** | Ingrediens | 3 sukker + glasflaske |
| **Brun sovs** | Ingrediens | Kulør + knogle + hvede + brun champignon + skål |
| **Bernaise** | Ingrediens | 2 æg + løg + bregne (estragon) + skål |
| **Flæskesteg** | Mad | 2 rå koteletter + løg + tørret tang → giver 2 |
| **Flæskefråder** | Mad | Flæskesteg + brun sovs + bagt kartoffel + kålblad |
| **Kylling bernaise** | Mad | Kylling (rå eller stegt) + 2 ris + bernaise + skål |

Alle opskrifter laves i Farmer's Delight's gryde (Cooking Pot) over en varmekilde.
Kulør, brun sovs og bernaise giver glasflasken/skålen tilbage, når de bruges i en opskrift.
Flæskefråder og Kylling bernaise giver Farmer's Delight's *Comfort*-effekt.
Ris er Farmer's Delight's eget `farmersdelight:rice`.

## Byg modden

1. Installer **JDK 17**.
2. Hent Gradle-wrapperen: kopér `gradlew`, `gradlew.bat` og mappen `gradle/` fra Forge MDK 1.20.1-47.4.20
   (https://files.minecraftforge.net) ind i denne mappe – eller kør `gradle wrapper --gradle-version 8.1.1`
   hvis du har Gradle installeret. Alternativt kan IntelliJ IDEA åbne projektet direkte (`build.gradle`).
3. Test i spillet: `./gradlew runClient`
4. Byg jar-filen: `./gradlew build` → `build/libs/danskdelight-1.0.0.jar`
5. Læg jar-filen i `mods/` sammen med Farmer's Delight.

## Sprites

Alle 6 sprites (16×16) er tegnet som originale pixel-art-billeder i `tools/make_textures.py`.
Redigér farverne i scriptet og kør `python3 tools/make_textures.py` for at genskabe dem
(kræver `pip install pillow`). Billederne havner i `src/main/resources/assets/danskdelight/textures/item/`.

## Struktur

```
src/main/java/dk/danskdelight/          Mod-kode (items + creative tab)
src/main/resources/assets/danskdelight/ Sprog (da_dk, en_us), modeller, teksturer
src/main/resources/data/danskdelight/   Opskrifter (farmersdelight:cooking)
tools/make_textures.py                  Sprite-generator
```
