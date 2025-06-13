# Testcodex

Dit project bevat een eenvoudig Python-script.

## `wandel_reminder.py`
Stuurt op vaste intervallen een melding om even te bewegen. Het script
kan worden aangepast via command line opties en bevat een eenvoudige
bediening via een klein venster.

### Gebruik

```bash
python wandel_reminder.py [--interval MINUTEN] [--start HH:MM] [--end HH:MM] [--icon PAD]
```

- `--interval` bepaalt het aantal minuten tussen meldingen (standaard 60).
- `--start` en `--end` geven optionele begin- en eindtijden op.
- `--icon` wijst naar een icoonbestand dat in de melding wordt getoond.
- Indien de `plyer` bibliotheek ontbreekt wordt een eenvoudige
  Tkinter-melding getoond.

Elke verstuurde melding wordt gelogd in `wandel_reminder.log`.

