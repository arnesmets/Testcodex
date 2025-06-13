"""Script om een wandelherinnering te sturen."""

from __future__ import annotations

import argparse
import datetime as _dt
import logging
import sys

from plyer import notification
import tkinter as tk
from tkinter import simpledialog


def _beep() -> None:
    """Speel een eenvoudige beep af indien mogelijk."""
    try:
        import winsound

        winsound.MessageBeep()
    except Exception:  # pragma: no cover - afhankelijk van OS
        # Fallback voor andere systemen
        sys.stdout.write("\a")
        sys.stdout.flush()


def stuur_melding(icon: str | None) -> None:
    """Stuur de bureaubladmelding en log dit."""
    kwargs = {
        "title": "Tijd voor een korte wandeling",
        "message": "Sta even op en wandel 1 minuut voor een betere doorbloeding.",
        "timeout": 10,
    }
    if icon:
        kwargs["app_icon"] = icon

    notification.notify(**kwargs)
    _beep()
    logging.info("Melding verstuurd")


def _parse_time(value: str) -> _dt.time:
    """Zet een HH:MM string om naar ``datetime.time``."""
    return _dt.datetime.strptime(value, "%H:%M").time()


def main() -> None:
    parser = argparse.ArgumentParser(description="Wandelherinnering")
    parser.add_argument(
        "--interval",
        type=int,
        default=60,
        help="Tijd tussen meldingen in minuten (standaard 60).",
    )
    parser.add_argument("--start", type=_parse_time, help="Starttijd in HH:MM")
    parser.add_argument("--end", type=_parse_time, help="Eindtijd in HH:MM")
    parser.add_argument("--icon", help="Pad naar een icoon voor de melding")
    args = parser.parse_args()

    logging.basicConfig(
        filename="wandel_reminder.log",
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
    )

    interval_ms = args.interval * 60 * 1000

    def stop() -> None:
        root.destroy()

    def open_settings() -> None:
        nonlocal interval_ms
        result = simpledialog.askinteger(
            "Instellingen",
            "Aantal minuten tussen meldingen:",
            parent=root,
            initialvalue=interval_ms // 60000,
            minvalue=1,
        )
        if result is not None:
            interval_ms = result * 60 * 1000

    def loop() -> None:
        now = _dt.datetime.now().time()
        allowed = True
        if args.start and now < args.start:
            allowed = False
        if args.end and now > args.end:
            allowed = False
        if allowed:
            stuur_melding(args.icon)
        root.after(interval_ms, loop)

    root = tk.Tk()
    root.title("Wandel Reminder")

    settings_btn = tk.Button(root, text="Settings", command=open_settings)
    settings_btn.pack(fill="x")

    trigger_btn = tk.Button(
        root, text="Trigger", command=lambda: stuur_melding(args.icon)
    )
    trigger_btn.pack(fill="x")

    exit_btn = tk.Button(root, text="Exit", command=stop)
    exit_btn.pack(fill="x")

    root.after(interval_ms, loop)
    root.mainloop()


if __name__ == "__main__":
    main()

