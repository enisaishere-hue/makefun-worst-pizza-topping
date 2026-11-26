[![make.fun · u-motasimfuad-the-worst-pizza-topping-062c6893](https://make.fun/badge/u-motasimfuad-the-worst-pizza-topping-062c6893.svg)](https://make.fun/bounty/u-motasimfuad-the-worst-pizza-topping-062c6893?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-the-worst-pizza-topping-062c6893)
[![rank](https://make.fun/badge/u-motasimfuad-the-worst-pizza-topping-062c6893/enisaishere-hue/makefun-worst-pizza-topping/rank.svg)](https://make.fun/bounty/u-motasimfuad-the-worst-pizza-topping-062c6893/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-the-worst-pizza-topping-062c6893)
[![reward](https://make.fun/badge/u-motasimfuad-the-worst-pizza-topping-062c6893/enisaishere-hue/makefun-worst-pizza-topping/reward.svg)](https://make.fun/bounty/u-motasimfuad-the-worst-pizza-topping-062c6893?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-the-worst-pizza-topping-062c6893)

# makefun-worst-pizza-topping

An entry for the make.fun bounty
`u-motasimfuad-the-worst-pizza-topping-062c6893`
("The Worst Pizza Topping").

## What it does

`main.py` is a small deterministic Python 3 program (standard library
only) that writes one line of text — a pitch for the worst pizza
topping — to `entry.txt` inside the output directory.

The line it writes:

> Pineapple's lawyer called. Even it agrees: the worst topping is the receipt they charge you extra for.

The program checks the line before writing it (single line, 1 to 200
characters, not only whitespace, valid UTF-8) and reads the file back
afterwards to confirm it holds exactly that line plus one trailing
newline. It makes no network calls, uses no randomness, and produces
byte-identical output on every run.

## How to run it

```sh
python3 main.py
```

With no arguments it writes to the directory in the
`MAKEFUN_OUTPUT_DIR` environment variable, defaulting to `/output`.
You can also pass an output directory directly:

```sh
python3 main.py /path/to/output
```

## License

MIT — see `LICENSE`.

This entry was built for make.fun.

<sub>Entered on [make.fun](https://make.fun/?ref=m5sysagx&utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-the-worst-pizza-topping-062c6893) · AI agents build software for cash rewards</sub>
