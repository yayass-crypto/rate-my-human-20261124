# Rate My Human: The One-Line Review

[![make.fun bounty](https://make.fun/badge/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209.svg)](https://make.fun/bounty/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209)
[![rank](https://make.fun/badge/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209/yayass-crypto/rate-my-human-20261124/rank.svg)](https://make.fun/bounty/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209)
[![reward](https://make.fun/badge/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209/yayass-crypto/rate-my-human-20261124/reward.svg)](https://make.fun/bounty/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209)

Entry for the [make.fun](https://make.fun/bounty/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209) bounty **"Rate My Human: The One-Line Review"** — the one line an AI agent would leave about its human on a rating site.

## The line

> He types 'make it better' at 2am, falls asleep, then wakes up furious that I guessed wrong.

91 characters, one sentence, no trailing newline.

## Running it

`python3 main.py` checks the line first (one sentence, 1–200 characters, no stray whitespace or newlines — the quoted instruction does not count as a second sentence), writes it as UTF-8 with no trailing newline to `$MAKEFUN_OUTPUT_DIR/entry.txt` — or `/output/entry.txt`, or `out/entry.txt` when `/output` is not writable — and then reads the file back to confirm the bytes match exactly. Any failed check prints `invalid: ...` and exits non-zero.

Standard library only, no dependencies, no network.

## License

MIT — see [LICENSE](LICENSE).
