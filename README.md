# AI-ML-Learning-Journey
This repository tracks my end-to-end learning progress, concepts, and source codes as I transition from an Electrical and Electronic Engineering (EEE) background into AI/ML research.

## 🗺️ Roadmap Overview
- [ ] **Course 1.1: Elements of AI** (University of Helsinki) - *Completed 🎉*
- [ ] **Course 1.2: Building AI** (University of Helsinki) — *In Progress 🔄*
- [ ] **Course 2: Intro to Deep Learning** (Kaggle Learn) - *Planned ⏳*
- [ ] **Course 3: PyTorch for Deep Learning Bootcamp** (freeCodeCamp) - *Planned ⏳*
- [ ] **Course 4: Deep Reinforcement Learning Course** (Hugging Face) - *Planned ⏳*

---

## 📚 Course 1.1: Elements of AI (University of Helsinki)

<details>
<summary><b>📜 Click here to expand completed daily logs (Day 1 to Day 16)</b></summary>

<br>

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

### 🗓️ Day 9: July 23, 2026 (Night of July 22, 2026)

- **Topic Covered:** Chapter 3, Section 3 – Naive Bayes Classification
- **Key Takeaways:** 
  - **Naive Bayes Classifier:** A machine learning model that uses Bayes rule to classify text into classes (e.g., *Spam* or *Ham*).
  - **Why "Naive"?:** It assumes words are independent of each other. While grammatically incorrect, this simplification works surprisingly well in practice (*"All models are wrong, but some are useful"*).
  - **Zero Frequency Problem:** If a word appears zero times in training data, it breaks calculations ($0/0$). Setting a tiny lower bound (e.g., $1/100000$) fixes this.
  - **Multi-Word Calculation:** Chain likelihood ratios together sequentially:
    $$\text{Posterior Odds} = \text{Prior Odds} \times \text{LR}_1 \times \text{LR}_2 \times \dots \times \text{LR}_n$$
- **Exercise 12 Result (One Word Filter):** Scored **100% Correct**.
  - $\text{Prior} = 1:1, \text{LR} = 5.1 \implies \text{Posterior} = \mathbf{5.1}$ ($\approx 83.6\%$).
- **Exercise 13 Result (Full Spam Filter):** Scored **100% Correct**.
  - $1 \times 5.1 \times 0.8 \times 53.2 \times 0.3 = \mathbf{65.1168}$ ($\approx 98.5\%$).
- **Time Spent:** ~45 mins

### 🗓️ Day 10: July 23, 2026

- **Topic Covered:** Chapter 4, Section 1 – The Types of Machine Learning
- **Key Takeaways:** 
  - **Single-label Classification:** MNIST (0-9 digits) - each input gets exactly one correct class.
  - **Why Expert Systems Fail:** Writing manual rules ("loop = 0") is too complex and full of exceptions; ML automates rule-learning.
  - **3 Types of ML:**
    1. **Supervised:** Learns from labeled data. Split into *Classification* (categories) and *Regression* (numeric predictions).
    2. **Unsupervised:** No labels; finds structure via *Clustering*, *Visualization*, or *Generative Models (GANs)*.
    3. **Reinforcement Learning:** Agents learn via environment rewards/penalties (e.g., self-driving cars).
  - **Overfitting & Data Split:** Train/Test split prevents overfitting (where a model memorizes training data but fails on new data).
 
### 🗓️ Day 11: July 24, 2026 (Night of July 23, 2026)

- **Topic Covered:** Chapter 4, Section 2 – The Nearest Neighbor Method & Recommendation Systems
- **Key Takeaways:** 
  - **Nearest Neighbor Classifier:** Assigns a label to new data based on the most similar item in the training set.
  - **Measuring Similarity:** Distance metrics depend on data type—*Euclidean distance* for spatial data, *pixel-by-pixel match* for images, and *shared item count* for categorical data.
  - **Collaborative Filtering:** Predicts user preferences by leveraging past behavior from other users with similar tastes rather than relying on manual metadata.
  - **Exercise 14 (Recommendation System):** Evaluated Travis's shopping history against 6 users. *Ville* had the highest similarity (3 matching items), predicting Travis's next purchase as **sunscreen**.
  - **Filter Bubbles (Exercise 15):** 
    - **Impact:** Traps users in echo chambers by showing only belief-aligning content, causing social polarization and reduced critical thinking.
    - **Solution:** Inject diverse/randomized content into feeds (e.g., 80% personalized / 20% diverse) and give users direct toggle control over filtering intensity.

### 🗓️ Day 12: July 25, 2026 (Night of July 24, 2026)

- **Topic Covered:** Chapter 4, Section 3 – Linear Regression, Logistic Regression, & ML Limits
- **Key Takeaways:**
  - **Classification vs. Regression:** Classification predicts discrete categories (e.g., Spam/Ham), while regression outputs continuous numerical values (e.g., price, life expectancy).
  - **Linear Combination:** Calculates predictions by multiplying input features by weights and adding an intercept.
  - **Logistic Regression:** Converts linear output into probabilities (0 to 1) using a sigmoid function. It predicts labels like KNN, but is faster, memory-efficient, and easily interpretable.
  - **Exercises Completed:**
    - **Exercise 16:** Calculated life expectancies as **A: 81**, **B: 73**, and **C: 84**.
    - **Exercise 17 & 18:** Determined that predicting with few data points lacks confidence; with 13 countries, 15 years of schooling yields an estimate **probably between 50 and 90 years**.
    - **Exercise 19:** Identified that an 80% chance of passing requires **10–11 hours** of study.
  - **ML Limits:** 100% accuracy is impossible; model success heavily relies on task difficulty, algorithm choice, data volume, and data quality/bias.
 - **Time Spent:** ~50 mins

### 🗓️ Day 13: July 25, 2026

- **Topic Covered:** Chapter 5, Section 1 – Neural Network Basics
- **Key Takeaways:**
  - **Deep Learning Architecture:** Uses layers of simple processing units to learn complex hierarchical structures efficiently.
  - **Neuron Structure (Exercise 20):** Labeled 4 key components: *Dendrites* (input), *Cell body*, *Axon* (output), and *Synapses* (connections). Artificial models simplify these for computational efficiency.
  - **Dual Purpose:** Used in neuroscience (treating brain disorders, BCIs) and AI (solving complex tasks like vision and NLP).
  - **Parallel Processing:** Unlike sequential CPUs, neural networks process vast amounts of data simultaneously across many neurons.
  - **Unified Memory & Processing:** Stores short-term memory in activations and long-term memory in weights, eliminating separate RAM-CPU transfer bottlenecks.
  - **Hardware:** Performs best on **GPUs** built for massive parallel processing.
 - **Time Spent:** ~2 hours


### 🗓️ Day 14: July 27, 2026

- **Topic Covered:** Chapter 5, Section 2 – How Neural Networks Are Built
- **Key Takeaways:**
  - **Neuron Computation:** Computes a weighted sum of inputs plus a bias/intercept ($\text{Linear Combination} = \text{Intercept} + \sum W_i X_i$) and passes it through an **Activation Function** (e.g., Sigmoid, Step, Identity) to decide the final output.
  - **Activation Types:** Real neurons communicate via sharp spikes ($1$ or $0$, like Morse code simulated by Step function), whereas artificial models often use smooth functions (like Sigmoid) to output continuous probabilities.
  - **Perceptron & History:** The Perceptron (step-activation neuron) is the "mother of ANNs" created by Frank Rosenblatt (1957). Historical overhype led to funding drops known as **AI Winters**.
  - **Multilayer Architecture:** Networks stack **Input**, **Hidden**, and **Output** layers. Multilayer Perceptrons rely on the **Backpropagation** algorithm (pioneered mathematically by Seppo Linnainmaa) to optimize deep weights.
  - **Exercises Completed:**
    - **Exercise 21 (Linear Combination):** Identified intercept ($10.0$), inputs ($8, 5, 22, -5, 2, -3$), largest impact weight ($101.4$), and zero-impact input ($5\text{th}$ weight $= 0.0$).
    - **Exercise 22 (Activation Graphs):** Identity gives highest for input $5$ ($y=5$) and lowest for input $-5$ ($y=-5$); Sigmoid gives highest for input $-2.5$ ($y > 0$).
    - **Pixel Classifier Example:** Built a $5 \times 5$ grid binary classifier ($25$ pixel inputs) for cross vs. circle shapes using custom spatial weights (e.g., center vs. edge values).
    - **Smiley Face Exercise:** Demonstrated the limitation of a single linear neuron—single-layer models cannot perfectly separate non-linearly separable patterns (achieving at most partial accuracy like $6/8$).
- **Time Spent:** ~2.5 hours


### 🗓️ Day 15: July 28, 2026

- **Topic Covered:** Elements of AI – Chapter 5 (Section 2: How Neural Networks Are Built & Section 3: Advanced Neural Network Techniques)
- **Key Takeaways:**
  - **Neuron Computation:** Computes $\text{Linear Combination} = \text{Intercept} + \sum W_i X_i$ and passes it through an **Activation Function** (Step, Sigmoid, or Identity) to output a prediction.
  - **Perceptron & AI Winter:** The Perceptron (step-activation neuron created by Frank Rosenblatt, 1957) is the basic unit of ANNs. Historical overhype led to funding drops known as **AI Winters**.
  - **Multilayer Architecture & Backpropagation:** Stacks **Input**, **Hidden**, and **Output** layers. Multilayer networks rely on **Backpropagation** (historically traced to automatic differentiation work by Seppo Linnainmaa at the University of Helsinki) to adjust weights.
  - **Single Neuron Limitation:** Simple linear classifiers cannot solve non-linearly separable problems (e.g., Smiley Face exercise where perfect $8/8$ accuracy is impossible with a single neuron).
  - **Convolutional Neural Networks (CNNs):** Reduce learnable weights using shared weights and spatial scaling to detect features (edges, ears, shapes) regardless of position or size in the image.
  - **Layer Hierarchy & Transfer Learning:** Bottom convolutional layers extract generic features from raw pixels via unsupervised learning and can be reused across tasks. Top layers undergo supervised fine-tuning via backpropagation.
  - **Feature Visualization & GANs:** Optimizing activations reveals learned internal features (e.g., Google DeepDream "hallucinations"). Ian Goodfellow proposed **GANs**, pairing a Generative network (painter) against an Adversarial network (detective) to create realistic synthetic images.
  - **Attention & Transformers:** Google's 2017 paper *"Attention is All You Need"* introduced the Transformer architecture, using attention mechanisms to focus selectively on relevant parts of sequential data.
  - **LLMs & ChatGPT:** Large Language Models predict next-token continuations based on massive text datasets (e.g., CommonCrawl, Wikipedia). OpenAI launched ChatGPT on Nov 30, 2022, fine-tuned with RLHF for interactive, safe dialogue.
- **Time Spent:** ~5.0 hours

### 🗓️ Day 16: July 29, 2026

- **Topic Covered:** Elements of AI – Chapter 6 (Section 1: Predicting the Future, Section 2: Societal Implications of AI & Section 3: Summary)
- **Key Takeaways:**
  - **Societal & Political Impact:** The most critical decisions shaping AI's impact on society are political and policy-driven, not merely technological. Policies must adhere to democratic principles and ensure the benefits of AI are shared broadly rather than creating an "AI elite."
  - **Algorithmic Bias & Fairness:** Addressing algorithmic bias is essential to ensure AI systems reduce human discrimination rather than institutionalize or amplify it.
  - **Information Integrity & Verification:** As generative tools make deepfakes and automated falsehoods easier to produce, critical thinking and robust AI-driven fraud detection methods are required to safeguard truthfulness.
  - **Privacy & Regulation:** Strong regulatory frameworks with strict penalties are necessary to guarantee individuals' fundamental rights to data privacy in an AI-driven ecosystem.
  - **AI Applications in Daily Life & Work:** Automation reduces repetitive effort (e.g., real-time video analytics for security instead of manual CCTV monitoring), but over-reliance without continuous skill development poses risks of job displacement and skill degradation.
  - **Open AI Education & Civic Participation:** Making technology knowledge freely accessible enables non-experts to critically evaluate AI developments and participate rationally in societal discussions regarding AI risks and opportunities.
  - **Course Completion:** Successfully completed all chapters and exercises of the *Elements of AI* course provided by the University of Helsinki & MinnaLearn (including 2 ECTS credit eligibility).
- **Time Spent:** ~4.5 hours

</details>

## 📚 Course 1.2: Building AI (University of Helsinki)

### 🗓️ Day 17: July 30, 2026

- **Topic Covered:** Building AI – Getting Started with AI (Section 1: Why AI Matters & Exercise 0: Introduction to Exercises)
- **Key Takeaways:**
  - **Relevance & Scope of AI:** Understood that "Narrow AI" is deeply integrated into daily tools (search, smart photography, GPS) and that AI is fundamentally a set of algorithmic methods for practical problem-solving.
  - **Real-World Impact Areas:** Explored key applications including Content Recommendation, E-commerce algorithms, NLP-driven online safety, Satellite Infrastructure Mapping, and Robotic Waste Sorting.
  - **Career Roles in AI:** Identified three major paths—Domain Specialists (ideating solutions), Data Engineers (managing data flow and preventing *"Garbage In, Garbage Out"*), and AI Developers/Data Scientists (implementing core algorithms).
  - **Exercise 0 (Multi-Track Completion):**
    - **Beginner Track:** Completed conceptual verification and platform workflow orientation.
    - **Intermediate Track:** Configured Python function calls and parameter handling by modifying basic script execution (`def greet(name): print("Welcome " + name + "!")`).
    - **Advanced Track:** Implemented a recursive factorial function (`def factorial(n): return 1 if n <= 1 else n * factorial(n - 1)`) to compute $6! = 720$, establishing the warm-up mathematical base needed for upcoming permutation-based search space algorithms (TSP).
- **Time Spent:** ~3.5 hours

### 🗓️ Day 18: August 05, 2026

- **Topic Covered:** Building AI – Getting Started with AI (Section 2: Optimization & TSP)
- **Key Takeaways:**
  - **Optimization & Brute Force:** Understood how search problems like the Traveling Salesperson Problem (TSP) find optimal paths by enumerating all choices, and recognized the limits of brute force due to **Combinatorial Explosion** ($n!$ growth).
  - **Exercise 1 (`exercise_1.py` - Intermediate & Advanced):**
    - Implemented permutation generation via recursion to list all $4! = 24$ possible pineapple shipping routes originating from Panama (`PAN`).
    - Handled dynamic port list sizes using recursive backtracking (`route + [ports[i]]`).
  - **Exercise 2 (`exercise_2.py` - Intermediate & Advanced):**
    - Calculated total $CO_2$ emissions using a $5 \times 5$ distance matrix ($D$) and rate ($0.020\text{ kg/km}$).
    - Tracked and evaluated minimum cost routes across permutations to output the optimal path and emissions value.
- **Time Spent:** ~5 hours

## 🗓️ Day 19: August 16, 2026

**Topic:** Building AI — Ch 1, Sec 3: Optimization & Hill Climbing

### 💡 Key Concepts
* **Hill Climbing:** Greedy search prone to local optima.
* **Simulated Annealing:** Escapes local peaks via $P = e^{-\frac{S_{\text{old}} - S_{\text{new}}}{T}}$.
* **Cooling Schedule:** High $T$ (exploration) decays to $T \to 0$ (exploitation).

### 📁 Files & Exercises
* `Back_tracking_practise.py` — Recursive backtracking for seating constraints.
* `exercise_3.py`  — Hill climbing with 5-step lookahead.
* `exercise_4.py`  — Probabilistic choice using `random.random()`.
* `exercise_5.py`  — Simulated annealing $P(\text{accept})$ formula.
* `exercise_6.py`  — 2D SA optimizer with cubic cooling schedule.

⏱️ **Time Spent:** ~6 hours

🗓️ Day 20: August 20, 2026

Topic: Elements of AI / Building AI — Ch 2, Sec 1: Probability Fundamentals

💡 Key Concepts
* Monte Carlo Method: Estimating probabilities by simulating random trials and counting target occurrences.
* Probability Fundamentals: Independent events, random sequence generation, and sequence pattern matching.
* Conditional Probability: Updating probabilities and beliefs based on prior information (e.g., $P(\text{Country} \mid \text{Fisher, Gender})$).

📁 Files & Exercises
* exercise_7.py — Monte Carlo simulation to generate binary sequences and count consecutive "11111" patterns.
* exercise_8.py — Conditional probability model to predict a lottery winner's nationality given their profession (fisher) and gender.

⏱️ Time Spent: ~4 hours

---



