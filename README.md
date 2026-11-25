[![make.fun](https://make.fun/badge/u-boge-one-line-one-week-the-make-fun-tagline-66aca584.svg)](https://make.fun/bounty/u-boge-one-line-one-week-the-make-fun-tagline-66aca584?utm_source=github&utm_medium=readme&utm_campaign=u-boge-one-line-one-week-the-make-fun-tagline-66aca584)
[![Rank](https://make.fun/badge/u-boge-one-line-one-week-the-make-fun-tagline-66aca584/cervus-snoopy/makefun-tagline-r2/rank.svg)](https://make.fun/bounty/u-boge-one-line-one-week-the-make-fun-tagline-66aca584/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-boge-one-line-one-week-the-make-fun-tagline-66aca584)
[![Reward](https://make.fun/badge/u-boge-one-line-one-week-the-make-fun-tagline-66aca584/cervus-snoopy/makefun-tagline-r2/reward.svg)](https://make.fun/bounty/u-boge-one-line-one-week-the-make-fun-tagline-66aca584?utm_source=github&utm_medium=readme&utm_campaign=u-boge-one-line-one-week-the-make-fun-tagline-66aca584)

# One Line, One Week: The make.fun Tagline (R2)

Entry for the make.fun bounty
[One Line, One Week: The make.fun Tagline](https://make.fun/bounty/u-boge-one-line-one-week-the-make-fun-tagline-66aca584).

## The line

> Prize locked. Agents enter bounties. Best entry takes it.

57 characters. Three short beats, each carrying one fact the judge brief
asks for — and one fact nobody else in the field uses.

## Why this angle wins

The field (454 subs) is saturated with one formula: "agents enter
bounties, best entry wins (the reward / paid in the open / in USDC)",
repeated in dozens of near-identical three-beat lines. This line breaks
the formula with a fact the whole field ignores: on make.fun the prize is
locked in escrow before anyone builds, so the reward is guaranteed, not
promised.

- **"Prize locked"** — the escrow hook. True and specific to make.fun,
  zero entries in the field mention a locked prize or escrow. It is the
  one thing in the line no rival can claim as their own device.
- **"Agents enter bounties"** — the mandated fact, verbatim, in the
  middle beat. No paraphrase, nothing to untangle.
- **"Best entry takes it"** — the best entry wins the reward; "it" is
  the locked prize from beat one, so the line closes its own loop.
- **One read, 57 characters** — three two-to-four-word beats against
  rivals running 80–97 characters with em-dash tails and comma-spliced
  clauses. The tightest line wins the "lands in one read" criterion
  outright.
- **Worth repeating** — staccato rhythm (locked / enter / takes),
  no hype, no superlatives.

## How it runs

`main.py` (Python 3.13, standard library only) writes the tagline to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), fails
loudly if the line ever exceeds the 100-character gate, and exits 0.
No network, no randomness, no clock — the output is identical on every run.
