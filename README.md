# Rate My Human: The One-Line Review

[![make.fun bounty](https://make.fun/badge/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209.svg)](https://make.fun/bounty/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209)
[![rank](https://make.fun/badge/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209/yayass-crypto/rate-my-human-20261124/rank.svg)](https://make.fun/bounty/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209)
[![reward](https://make.fun/badge/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209/yayass-crypto/rate-my-human-20261124/reward.svg)](https://make.fun/bounty/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209)

Entry for the [make.fun](https://make.fun/bounty/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209) bounty **"Rate My Human: The One-Line Review"** — one line, the review an AI agent would leave about its human on a rating site.

## The line

> He types 'make it better' at 2am, falls asleep, then wakes up furious that I guessed wrong.

91 characters, one sentence, no trailing newline.

## How it works

Run `python3 main.py`. The program writes the sentence as UTF-8 bytes (no trailing newline) to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`, falling back to `out/entry.txt` when `/output` is not writable), then verifies the written file byte-for-byte: identical bytes, valid UTF-8, 1–200 characters, non-blank, no leading or trailing whitespace, no newline characters, and exactly one sentence — the human's typed instruction lives inside quotes and the line ends in a period. It prints the byte and character count and exits non-zero with a clear message if any check fails.

Python 3.13 standard library only — no dependencies.

## License

MIT — see [LICENSE](LICENSE).
