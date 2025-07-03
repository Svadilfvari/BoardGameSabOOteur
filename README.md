# 🎲 BoardGameSabOOteur

A Python-based simulation for the popular hidden-role card game **Saboteur**, where players dig tunnels, hide identities, and race to gold—or sabotage the efforts.

---

## 🧩 About Saboteur

**Saboteur** is a mining-themed, semi-cooperative card game designed by Frédéric Moyersoen (2004). Players take on secret roles—**Gold-Diggers** who aim to build a path to hidden gold, or **Saboteurs** who try to prevent it.

- 🧙‍♂️ Players: 3–10  
- ⏱️ Play time: ~30 minutes  
- 🎲 Mechanics: Hidden roles, path-building, deduction  

Game end conditions:  
- If a path reaches gold: Miners win, collect nuggets.  
- If cards run out or paths are blocked: Saboteurs win and earn points.

Learn more on [Wikipedia](https://en.wikipedia.org/wiki/Saboteur_%28card_game%29).

---

## 💻 About This Project

This repository simulates Saboteur gameplay in Python, enabling experimentation with strategies, rule variants, and automated AI player agents.

**Features:**

- Full card deck and player-role handling  
- Path-card placement and validation  
- Action card effects (break/repair tools, rock slides, map reveals)  
- Hidden roles with end-of-round reveal & scoring  
- Support for multi-round gameplay and score tracking  

---

## ▶️ Getting Started
git clone https://github.com/Svadilfvari/BoardGameSabOOteur.git
cd BoardGameSabOOteur

## 🛠️ Key Concepts & Implementation

- **Deck Management**: Shuffles and deals path, action, and gold nugget cards.  
- **Hidden Roles**: Players are randomly assigned roles each round.  
- **Turn Mechanics**: Players can place path cards, play action cards (break, repair, rockslide, map), or pass.  
- **Path Validation**: Ensures continuous, valid tunnels from the start card.  
- **Scoring & Rounds**: Follows official rules including gold distribution and end-of-round outcomes.  

---

## 🧩 Extensions & To-Do

- Add support for **Saboteur 2** mechanics (multi-team, geologists, bosses)  
- Improve AI agents with reinforcement learning or Monte Carlo methods  
- Visualize board state using ASCII art or GUI  
- Evaluate rule variants (e.g., score distribution, hand size)  

---

## 📚 References

- [Saboteur Rulebook (AMIGO, 2004)](https://cdn.1j1ju.com/medias/83/8a/e7-saboteur-rulebook.pdf)  
- [Saboteur - Wikipedia](https://en.wikipedia.org/wiki/Saboteur_%28card_game%29)  
- [BoardGameGeek - Saboteur](https://boardgamegeek.com/boardgame/9220/saboteur)  

---

## 🤝 Contributing

Contributions are welcome! Suggestions, bug reports, rule variants, and AI improvements are highly appreciated — please submit a pull request.
