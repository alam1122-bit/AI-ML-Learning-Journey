# AI-ML-Learning-Journey
This repository tracks my end-to-end learning progress, concepts, and source codes as I transition from an Electrical and Electronic Engineering (EEE) background into AI/ML research.

## 🗺️ Roadmap Overview
- [ ] **Course 1: Elements of AI** (University of Helsinki) - *In Progress 🔄*
- [ ] **Course 2: Intro to Deep Learning** (Kaggle Learn) - *Planned ⏳*
- [ ] **Course 3: PyTorch for Deep Learning Bootcamp** (freeCodeCamp) - *Planned ⏳*
- [ ] **Course 4: Deep Reinforcement Learning Course** (Hugging Face) - *Planned ⏳*

---

## 📚 Course 1: Elements of AI (University of Helsinki)

### 🗓️ Day 1: July 14, 2026 (Started on the night of July 13)
- **Topic Covered:** Chapter 1, Section 1 - What is, and what isn't AI?
- **Key Takeaways:** 
  - **No Fixed Definition:** AI doesn't have a permanently fixed definition; it evolves constantly as old problems (like pathfinding) become standard computer science.
  - **The Paradox:** Tasks that feel effortless to humans (like grabbing an object) are extremely hard for robots/AI, while tasks that feel hard to humans (like chess or complex math) are very easy for computers.
  - **Core Criteria:** Real AI must possess **Autonomy** (ability to handle unpredictable situations without human rules) and **Adaptivity** (ability to improve from experience).
  - **Professional Terminology:** Learned that "AI" is a discipline, not a countable noun. Moving forward, I will use terms like "an AI method" or "an AI model" instead of "an AI" to maintain professional/academic standards.
- **Exercise 1 Result:** Scored **6/7 correct** on the first try! Understood that traditional software like spreadsheets do not qualify as AI because they lack autonomy and adaptivity.
- **Time Spent:** ~45 mins

### 🗓️ Day 2: July 14, 2026 (Night)
- - **Topic Covered:** Chapter 1, Section 2 - Related Fields
- **Exercise 2 Result (Taxonomy of AI):** Scored **5/5 correct**! Mastered the Euler diagram relations: CS > AI > ML > DL, and how Data Science acts as an overlapping umbrella bridging CS, AI, and Statistics.
- **Exercise 3 Result (AI Applications Case Study):** Scored **3/5 correct**. Analyzed real-world use cases to distinguish when to apply AI/ML vs. classical methods:
  - *Autonomous Cars, Chatbots, and Ad Optimization* heavily rely on **Machine Learning and Statistics**.
  - *Rocket Steering* is strictly a **Robotics** domain governed by deterministic physics laws rather than ML trial-and-error.
  - *Gallup Results Summarization* falls under pure **Classical Statistics** rather than adaptive AI solutions.
- **Time Spent:** ~40 mins

### 🗓️ Day 3: July 15, 2026 (Night)
- **Topic Covered:** Chapter 1, Section 3 - Philosophy of AI
- **Key Takeaways:** 
  - **Philosophy of AI:** Explored the fundamental question of whether intelligent behavior requires a conscious "mind" or if consciousness can be replicated purely through computation.
  - **The Turing Test:** Proposed by Alan Turing ("father of computer science"). It states that if a computer behaves indistinguishably from a human in natural language chat, it exhibits human-level intelligence ("intelligent is as intelligent says").
  - **Limitation of Turing Test:** It often measures human-like behavior (jokes, evasion, typos) rather than actual intelligence (e.g., the Eugene Goostman chatbot simulation).
  - **The Chinese Room Argument (John Searle):** A powerful counter-argument to the Turing Test. It suggests that executing mechanical, automated rules (like translating symbols using a manual) does not equal actual "understanding" or "consciousness." A self-driving car's safe-driving actions are automated, but it does not "understand" its environment in a human-like way.
  - **Key Terminology:**
    - **General vs. Narrow AI:** *Narrow AI* handles specific, single tasks (what we have today in leaps and bounds). *General AI (AGI)* refers to a machine capable of any intellectual task (still science fiction).
    - **Strong vs. Weak AI:** *Strong AI* is a genuinely intelligent, self-conscious mind. *Weak AI* consists of systems that merely exhibit intelligent behaviors despite being "mere" computers (what exists today).
- **Time Spent:** ~35 mins

### 🗓️ Day 4: July 16, 2026 (Night)
**Topic Covered:** Chapter 2, Section 1 - Search and problem solving

- **Key Takeaways:**

 - **Problem Formulation:** Learned how real-world navigation and decision-making scenarios are mathematically structured as search problems by defining alternative choices and their consequences.

- **Core Elements of Search:** Mastered the three foundational components of graph-based problem solving:

- **State Space:** The full set of all valid and allowed situations within a problem's constraints.

- **Transitions:** Direct valid movements from one state to another (a sequence of which forms a path).

- **Costs:** The algorithmic weight (time, distance, or resource expenditure) assigned to transitions to determine the most optimal path.

- **Constraint Handling:** Explored how AI systems eliminate forbidden states (such as resource conflicts or logical contradictions) to systematically compute the shortest path from an initial state to a goal state.

- **Time Spent:** ~35 mins

### 🗓️ Day 5: July 17, 2026
- **Topic Covered:** Chapter 2, Section 2 - Solving problems with AI
- **Key Takeaways:** 
  - **Foundations of Automation (Alan Turing):** Explored how AI's roots are intertwined with the birth of computer science. Learned that Alan Turing's fundamental insight—anything that can be computed using numbers or symbols can be automated—laid the groundwork for the field. His theoretical model, the *Turing machine*, directly led to the invention of programmable, multi-task computers, which were famously utilized to crack German secret codes during World War II.
  - **Coining of "Artificial Intelligence" (John McCarthy):** Studied how John McCarthy (the Father of AI) officially coined and established the term "Artificial Intelligence" during the historic Dartmouth conference in 1956. 
  - **The Core AI Conjecture:** Evaluated McCarthy’s foundational hypothesis: *"every aspect of learning or any other feature of intelligence can in principle be so precisely described that a machine can be made to simulate it."* This means complex intelligence can be broken down into small, mechanical, programmable steps—a concept that bypasses philosophical objections like Searle's Chinese Room by asserting that mechanical execution of a program still constitutes intelligence.
  - **Rise of Search and Games in AI:** Understood why board games (like checkers, chess, and Go) became the primary testing grounds for early AI algorithms in the 1950s—they provided restricted, easily formalized domains. This focus drove massive advancements in *search and planning techniques* during the 1960s, giving birth to foundational algorithms like **Minimax** and **Alpha-Beta Pruning**, which remain core architectures for game-playing AI today.
- **Time Spent:** ~30 mins

### 🗓️ Day 6: July 21, 2026 (Night of July 20, 2026)
- **Topic Covered:** Chapter 2, Section 3 - Search and games
- **Key Takeaways:** 
  - **Game Trees & Minimax:** Alternating layers of `MAX` (aims for $+1$) and `MIN` (aims for $-1$). Optimal moves are determined by backpropagating values up from terminal states.
  - **Combinatorial Explosion:** Games like Chess ($\text{branching factor} \approx 35$) and Go ($\approx 250$) generate massive trees, making exhaustive search impossible.
  - **Depth-Limited Heuristics:** Evaluates intermediate board states when terminal nodes can't be reached (e.g., Chess piece scores: Queen = 9, Rook = 5, Pawn = 1).
  - **Real-World Non-Determinism:** Classical search assumes deterministic rules; real-world AI requires handling uncertainty and randomness (Chapter 3 preview).
- **Exercise 7 Result (Why so pessimistic, Max?):** Scored **Correct** (Answer: **-1**). Evaluated the defensive sub-game tree and proved that Min forces a guaranteed victory regardless of Max's optimal play.
- **Time Spent:** ~50 mins

### 🗓️ Day 7: July 22, 2026 (Night of July 21, 2026)
- **Topic Covered:** Chapter 3, Section 1 - Odds and Probability
- **Key Takeaways:** 
  - **Handling Real-World Uncertainty:** Classical AI relies on perfect information (like Chess), whereas modern real-world AI (e.g., self-driving cars, medical diagnostics) must deal with incomplete data and sensor "noise" using probability.
  - **Quantifying Uncertainty:** Instead of complex calculus, the core paradigm shift is treating uncertainty as a measurable number. Probability allows us to objectively quantify and compare real-world risks (e.g., vaccine benefits vs. side effects).
  - **Odds vs. Probability:**
    - **Odds ($x:y$):** Expresses the ratio of success events to failure events (e.g., $3:1$ means 3 wins for every 1 loss).
    - **Natural Frequencies:** Expressed as a fraction $\frac{x}{x+y}$ (e.g., $\frac{3}{4}$).
    - **Critical Pitfall:** $1:5$ Odds ($\text{Ratio} = 0.2$, Total outcomes = $6$) is NOT equal to $20\%$ Probability ($\frac{1}{5}$, Total outcomes = $5$).
  - **Odds-to-Probability Conversion Formula:** 
    $$\text{Probability} = \frac{x}{x + y}$$
- **Exercise 8 Result (Probabilistic Forecasts):** Scored **3/4 correct**. Learned that a single outcome cannot prove or disprove a probabilistic forecast (e.g., a $10\%$ event happening doesn't mean a $90\%$ forecast was wrong). Only long-run statistical observations can evaluate forecast accuracy.
- **Exercise 9 Result (Odds):** Scored **6/6 correct (100%)**! Mastered converting odds into fractions and percentages:
- **Time Spent:** ~50 mins

### 🗓️ Day 8: July 22, 2026

- **Topic Covered:** Chapter 3, Section 2 – The Bayes Rule
- **Key Takeaways:** 
  - **Updating Beliefs:** The Bayes rule provides an elegant mathematical way to update initial beliefs (Prior Odds) when new evidence (Likelihood Ratio) becomes available to arrive at a final belief (Posterior Odds).
  - **The Core Formula:** 
    $$\text{Posterior Odds} = \text{Likelihood Ratio} \times \text{Prior Odds}$$
  - **Likelihood Ratio (LR):** Measures the strength of new evidence by comparing how much more likely an observation is if the event occurs versus if it does not ($\text{LR} = \frac{P(\text{Observation} \mid \text{Event})}{P(\text{Observation} \mid \text{No Event})}$).
  - **Base-Rate Fallacy:** Human intuition naturally ignores low background probabilities (base rates) when presented with positive test results. Knowing Bayes rule cures this cognitive bias.
  - **Medical Screening Counter-Intuition:** Even with $80\%$ test sensitivity and $90\%$ specificity, a positive test for a disease with a $5\%$ base rate results in only a $\approx 29.6\%$ actual chance of having the disease ($40:95$ odds).
- **Exercise 10 Result (Bayes Rule - Rain in Helsinki):** Scored **100% Correct**.
  - $\text{Prior Odds} = 206:159$, $\text{LR} = 9 \implies \text{Posterior Odds} = \mathbf{1854:159}$ ($\approx 92\%$ probability).
- **Exercise 11 Result (Bayes Rule - Breast Cancer Screening):** Scored **100% Correct**.
  - $\text{Prior Odds} = 5:95$, $\text{LR} = \frac{0.80}{0.10} = 8 \implies \text{Posterior Odds} = \mathbf{40:95}$ ($\approx 29.6\%$ probability).
- **Time Spent:** ~45 mins

---



