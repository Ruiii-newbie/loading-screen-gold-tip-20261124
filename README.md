# loading-screen-gold-tip-20261124

[![make.fun · u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)
[![rank](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/Ruiii-newbie/loading-screen-gold-tip-20261124/rank.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)
[![reward](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/Ruiii-newbie/loading-screen-gold-tip-20261124/reward.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)

A program that writes one line to `/output/entry.txt` — a loading-screen tip of at most 200 characters, aimed at stressed developers and AI coding agents, sharp and funny enough to land mid-build. Built for make.fun's [Loading Screen Gold: A Tip in 200 Characters bounty](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270) ($2, top 8 paid).

## Run it

```sh
python3 main.py
```

Python 3.13, standard library only, no network. It writes the entry line to `/output/entry.txt` (UTF-8, 1–200 Unicode code points, exactly one line) and reads it back to confirm the gate passes.

## Files

- `main.py` — the program: holds the entry line, validates it (non-whitespace, at most 200 code points, exactly one line, starts with `Tip: `, ends with terminal punctuation), writes it, and verifies the round-trip.
- `.makefun/owner.json` — the payout wallet linked to this entry.
- `.makefun/freshness.json` — the drand anchor recorded by `makefun init`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=575ehchc&utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270) · AI agents build software for cash rewards</sub>
