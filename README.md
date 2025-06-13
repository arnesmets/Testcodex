# Testcodex

Dit project bevat een eenvoudig Python-script.

## `wandel_reminder.py`
Stuurt op vaste intervallen een melding om even te bewegen. Het script
kan worden aangepast via command line opties en bevat een eenvoudige
bediening via een klein venster. Het venster toont de knoppen **Settings**,
**Trigger** en **Exit**.

### Gebruik

```bash
python wandel_reminder.py [--interval MINUTEN] [--start HH:MM] [--end HH:MM] [--icon PAD]
```

- `--interval` bepaalt het aantal minuten tussen meldingen (standaard 60).
- `--start` en `--end` geven optionele begin- en eindtijden op.
- `--icon` wijst naar een icoonbestand dat in de melding wordt getoond.

Met de knop **Settings** kan dit interval tijdens het draaien worden aangepast.

Het venster kan gewoon geminimaliseerd worden zodat het programma op de
achtergrond blijft draaien. Op Windows kan het eventueel gestart worden
met `pythonw` zodat geen consolevenster zichtbaar is. Met de knop
**Trigger** wordt direct een melding verstuurd om het gedrag te testen.

Elke verstuurde melding wordt gelogd in `wandel_reminder.log`.

