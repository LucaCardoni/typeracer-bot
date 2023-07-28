# Typeracer bot 🏎️

## ⬇️ Setup
First of all, you should install tesseract OCR from [the original github repo](https://github.com/tesseract-ocr/tessdoc/blob/main/Installation.md)

Downoad now the repo, or clone it with git

`git clone https://github.com/LucaCardoni/typeracer-bot`

Open a terminal window wherever you saved the repo and type

`pip install -r requirements.txt`

Go now in `main.py` and edit row 9 with the directory of where you installed tesseract.

## 🏃‍♂️ Usage

Start `main.py`, it will ask you the language of the game, type in the LangCode you prefer.

<details>
<summary>Supported languages</summary>

| LangCode | Language |
| --- | --- |
| `afr` | Afrikaans |
| `amh` | Amharic |
| `ara` | Arabic |
| `asm` | Assamese |
| `aze` | Azerbaijani |
| `aze_cyrl` | Azerbaijani - Cyrilic |
| `bel` | Belarusian |
| `ben` | Bengali |
| `bod` | Tibetan |
| `bos` | Bosnian |
| `bre` | Breton |
| `bul` | Bulgarian |
| `cat` | Catalan; Valencian |
| `ceb` | Cebuano |
| `ces` | Czech |
| `chi_sim` | Chinese - Simplified |
| `chi_tra` | Chinese - Traditional |
| `chr` | Cherokee |
| `cos` | Corsican |
| `cym` | Welsh |
| `dan` | Danish |
| `deu` | German |
| `dzo` | Dzongkha |
| `ell` | Greek, Modern (1453-) |
| `eng` | English |
| `enm` | English, Middle (1100-1500) |
| `epo` | Esperanto |
| `est` | Estonian |
| `eus` | Basque |
| `fao` | Faroese |
| `fas` | Persian |
| `fil` | Filipino (old - Tagalog) |
| `fin` | Finnish |
| `fra` | French |
| `frk` | German - Fraktur |
| `frm` | French, Middle (ca.1400-1600) |
| `fry` | Western Frisian |
| `gla` | Scottish Gaelic |
| `gle` | Irish |
| `glg` | Galician |
| `grc` | Greek, Ancient (to 1453) (contrib) |
| `guj` | Gujarati |
| `hat` | Haitian; Haitian Creole |
| `heb` | Hebrew |
| `hin` | Hindi |
| `hrv` | Croatian |
| `hun` | Hungarian |
| `hye` | Armenian |
| `iku` | Inuktitut |
| `ind` | Indonesian |
| `isl` | Icelandic |
| `ita` | Italian |
| `ita_old` | Italian - Old |
| `jav` | Javanese |
| `jpn` | Japanese |
| `kan` | Kannada |
| `kat` | Georgian |
| `kat_old` | Georgian - Old |
| `kaz` | Kazakh |
| `khm` | Central Khmer |
| `kir` | Kirghiz; Kyrgyz |
| `kmr` | Kurmanji (Kurdish - Latin Script) |
| `kor` | Korean |
| `kor_vert` | Korean (vertical) |
| `lao` | Lao |
| `lat` | Latin |
| `lav` | Latvian |
| `lit` | Lithuanian |
| `ltz` | Luxembourgish |
| `mal` | Malayalam |
| `mar` | Marathi |
| `mkd` | Macedonian |
| `mlt` | Maltese |
| `mon` | Mongolian |
| `mri` | Maori |
| `msa` | Malay |
| `mya` | Burmese |
| `nep` | Nepali |
| `nld` | Dutch; Flemish |
| `nor` | Norwegian |
| `oci` | Occitan (post 1500) |
| `ori` | Oriya |
| `osd` | Orientation and script detection module |
| `pan` | Panjabi; Punjabi |
| `pol` | Polish |
| `por` | Portuguese |
| `pus` | Pushto; Pashto |
| `que` | Quechua |
| `ron` | Romanian; Moldavian; Moldovan |
| `rus` | Russian |
| `san` | Sanskrit |
| `sin` | Sinhala; Sinhalese |
| `slk` | Slovak |
| `slv` | Slovenian |
| `snd` | Sindhi |
| `spa` | Spanish; Castilian |
| `spa_old` | Spanish; Castilian - Old |
| `sqi` | Albanian |
| `srp` | Serbian |
| `srp_latn` | Serbian - Latin |
| `sun` | Sundanese |
| `swa` | Swahili |
| `swe` | Swedish |
| `syr` | Syriac |
| `tam` | Tamil |
| `tat` | Tatar |
| `tel` | Telugu |
| `tgk` | Tajik |
| `tha` | Thai |
| `tir` | Tigrinya |
| `ton` | Tonga |
| `tur` | Turkish |
| `uig` | Uighur; Uyghur |
| `ukr` | Ukrainian |
| `urd` | Urdu |
| `uzb` | Uzbek |
| `uzb_cyrl` | Uzbek - Cyrilic |
| `vie` | Vietnamese |
| `yid` | Yiddish |
| `yor` | Yoruba |
</details>

It will the ask you how many milliseconds there must be between one character and another.

You can then choose whether or not to save the configuration so you don't have to enter it every time.

You will then have to place the cursor in the upper left corner of the text, do Ctrl + left click, then go to the lower right corner and do the same.
this will take a screenshot which will then be passed to OCR which will translate the image into text.

As soon as the game starts, press ENTER and the bot will start typing by itself.

And you are Done!

Enjoy!

## WARNING!
This tool is only for educational purpose. I will not be responsible for any consequences if you use this tool for other purposes except education.

## CONTRIBUTING
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## LICENSE
This project is licensed under the [GPL-2.0 license](https://www.gnu.org/licenses/old-licenses/gpl-2.0.txt).
