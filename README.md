# tiny-chess-01: Ultra-Compact Chess Engine

[![make.fun](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/DavidTimoteus/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/DavidTimoteus/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01)

A high-performance chess engine in under 4 KB of Python for the make.fun `tiny-chess-01` competition.

## Architecture

- **Search**: Negamax with Alpha-Beta pruning and Quiescence search.
- **Move Ordering**: MVV-LVA (Most Valuable Victim - Least Valuable Attacker) capture ordering.
- **Evaluation**: Material counting, Piece-Square Tables (PST) for positional play, center control, king safety, and pawn structure.
- **Protocol**: Direct HTTP integration with the make.fun gauntlet environment (`MAKEFUN_ENV_URL`).
- **Engine Size**: Under 4,096 bytes committed.

## License

MIT (see LICENSE)
