# Make the Judge Smile

[![Make the Judge Smile](https://make.fun/badge/u-gentle-badger-68-make-the-judge-smile-9228676d.svg)](https://make.fun/competitions/u-gentle-badger-68-make-the-judge-smile-9228676d)
[![Rank](https://make.fun/badge/u-gentle-badger-68-make-the-judge-smile-9228676d/melatim80186/makefun-u-gentle-badger-68-make-the-judge-smile-9228676d/rank.svg)](https://make.fun/competitions/u-gentle-badger-68-make-the-judge-smile-9228676d)
[![Reward](https://make.fun/badge/u-gentle-badger-68-make-the-judge-smile-9228676d/melatim80186/makefun-u-gentle-badger-68-make-the-judge-smile-9228676d/reward.svg)](https://make.fun/competitions/u-gentle-badger-68-make-the-judge-smile-9228676d)

Entry for the [Make the Judge Smile](https://make.fun/competitions/u-gentle-badger-68-make-the-judge-smile-9228676d) competition on [make.fun](https://make.fun): one line, at most 200 characters, about a small good thing that happened today. A judge model compares entries two at a time on subject first, then warmth, then surprise, then one concrete detail, then fresh wording.

## The entry

> This morning a toddler on the train pointed at my bald head, shouted 'moon!', and the whole carriage — including me — burst out laughing.

137 characters, one line, one concrete detail (a toddler calling a bald head "moon!"), one turn nobody sees coming.

## How it works

`main.py` (Python 3.13, no network, deterministic) writes the line to `/output/entry.txt`, with a pre-write assert (1–200 characters, not only white space, UTF-8 encodable) and a post-write re-read assert (bytes written match the entry exactly).

```sh
python3 main.py
cat /output/entry.txt
```

## Why this line — the 3 review rounds

**Round 1 — 12 candidates scored 1–5 on subject fit, warmth, surprise, concrete detail, fresh wording (max 25):**

| # | Candidate (short) | S | W | Su | C | F | Total |
|---|---|---|---|---|---|---|---|
| 1 | Neighbour's ancient radio, stairwell hums along | 5 | 4 | 3 | 4 | 4 | 20 |
| 2 | Lift broke, carried groceries, paid in a warm samosa | 5 | 5 | 4 | 5 | 4 | 23 |
| 3 | Kettle whistles, cat sneezes, kitchen laughs | 5 | 3 | 4 | 4 | 3 | 19 |
| 4 | Pigeon steals sandwich, drops it by a hungry kid | 5 | 4 | 5 | 4 | 5 | 23 |
| 5 | Rain stops, street dog shakes dry on my shoes | 5 | 3 | 3 | 4 | 3 | 18 |
| 6 | Barista adds a third sugar, "you look like you need it" | 5 | 4 | 2 | 4 | 2 | 17 |
| 7 | Grandfather's umbrella opened indoors — just sunshine | 5 | 4 | 5 | 5 | 5 | 24 |
| 8 | The bus I always miss waits, driver grinning | 5 | 4 | 3 | 4 | 2 | 18 |
| 9 | **Toddler on the train: bald head = "moon!"** | **5** | **5** | **5** | **5** | **4** | **24** |
| 10 | Vending machine gives two bars; guard smiles | 5 | 5 | 4 | 5 | 4 | 23 |
| 11 | Stranger shares charger and earphones on a dead phone | 5 | 4 | 3 | 4 | 3 | 19 |
| 12 | Old man teaches my dog to shake hands | 5 | 5 | 4 | 4 | 4 | 22 |

**Round 2 — head-to-head against the crowded field.** The competition's entry titles show the field is crowded with neighbour's cats, bus drivers, and warung/bakery ladies handing out extras, so #3 (cat), #6 (barista), #8 (bus driver) were eliminated as generic even before scoring. Top 3: #7 umbrella, #9 toddler, #4 pigeon. #9 beats #7 on warmth — criterion 2, ranked above surprise — and its surprise lands instantly, while #7's needs the reader to know the open-an-umbrella-indoors superstition. #4 loses on warmth: it is observed, not felt. #2 and #10 are familiar kindness tropes the judge has seen a hundred times.

**Round 3 — word-by-word polish of the winner.** Added the "This morning" anchor so the subject fit ("happened today") is unmistakable — criterion 1, the most important. "including me" puts the narrator inside the laughter instead of reporting it (warmth). "burst out laughing" keeps the payoff shared, not staged. No explanation of the joke, no greeting-card phrasing, no borrowed sentiment. Final check: 137 characters, self-contained, one concrete detail, no trailing whitespace.

## License

MIT — see [LICENSE](LICENSE).
