# Brainteasers

Try each for at least 10 minutes before opening the solution. Say your reasoning out loud; interviewers grade the structure of the argument as much as the answer.

Difficulty: 🟢 warm-up · 🟡 standard · 🔴 hard

---

### 1. Monty Hall 🟢

Three doors hide a car and two goats. You pick door 1. The host, who knows where the car is, opens door 3 to show a goat. Should you switch to door 2?

<details><summary>Solution</summary>

Yes. Switching wins with probability **2/3**.

Your first pick is correct with probability 1/3. In that case, switching loses. In the other 2/3 of cases, the car is behind one of the two doors you didn't pick, and the host's choice reveals the other goat, so switching wins.

The key is that the host's action is not random. It depends on where the car is. If the host opened a door at random and happened to show a goat, the answer would be 1/2.
</details>

---

### 2. Expected rolls to see every face 🟢

How many rolls of a fair six-sided die do you expect until every face has appeared at least once?

<details><summary>Solution</summary>

This is the coupon collector problem. When k faces have been seen, the wait for a new face is geometric with success probability (6 − k)/6, so its expected length is 6/(6 − k).

Summing over k = 0 to 5:

E = 6 (1 + 1/2 + 1/3 + 1/4 + 1/5 + 1/6) = 6 × 2.45 = **14.7**

The general result for n faces is n · H_n, where H_n is the nth harmonic number.
</details>

---

### 3. Burning ropes 🟡

You have two ropes. Each takes exactly one hour to burn end to end, but they burn unevenly. Using only these ropes and a lighter, measure 45 minutes.

<details><summary>Solution</summary>

Light rope A at both ends and rope B at one end at the same moment.

Rope A burns out after 30 minutes, since both ends are burning. At that moment, light the other end of rope B.

Rope B now has 30 minutes of burn left, but it is burning from both ends, so it finishes after 15 more minutes. The total is 30 + 15 = **45 minutes**.

The idea is that a rope burning from both ends halves the remaining time, and an event (the first rope finishing) can start a timer.
</details>

---

### 4. A die that rolls itself 🟡

A fair coin is flipped until a head appears. The number of flips is N. What is the expected value of 2^N?

<details><summary>Solution</summary>

N is geometric with p = 1/2, so P(N = k) = (1/2)^k for k ≥ 1.

E[2^N] = Σ_(k ≥ 1) 2^k (1/2)^k = Σ_(k ≥ 1) 1 = **∞**

The expected payoff is infinite, even though almost every outcome is small. This is the St. Petersburg paradox. The point of the question is what a fair price for an infinite expected value means, and why people refuse to pay it. A trader would ask how much of the value sits in the tail, and whether the tail can be realised in practice.
</details>

---

### 5. Hats in a line 🔴

A hundred prisoners stand in a line, each wearing a red or blue hat chosen at random. Each prisoner can see the hats of everyone in front of them, but not their own, and cannot hear anyone behind. Starting from the back, each prisoner must call out one colour. What is the best strategy?

<details><summary>Solution</summary>

The strategy guarantees that 99 of the 100 prisoners are correct.

The last prisoner announces the parity of the red hats in front of them, say "red" for even and "blue" for odd. Each prisoner after that counts the red hats they see, and compares the parity with what has been announced so far. They can work out their own hat colour from the change in parity, and call it.

The last prisoner has a 50% chance of being correct, since they only learn the parity. Everyone else is always correct.

The answer shows how a single shared signal (the parity) carries information through the line.
</details>

---

### 6. Bertrand's chord 🔴

Pick a chord of a circle at random. What is the probability that its length is longer than the side of the inscribed equilateral triangle?

<details><summary>Solution</summary>

The answer depends on what "random" means, so the first step is to define the procedure.

- **Random endpoints:** choose two random points on the circle. The probability is **1/3**.
- **Random radius:** choose a random radius and a random point on it, and draw the chord perpendicular to the radius at that point. The probability is **1/2**.
- **Random midpoint:** choose a random point inside the circle as the midpoint. The probability is **1/4**.

The lesson is that a probability question on a continuous space is not well defined until the sampling procedure is stated. Interviewers want to hear you ask for it.
</details>

---

### 7. Rolling a six, trials with a bias 🟡

A die is rolled until a six appears, but each roll costs one unit. The die is loaded so that P(6) = 1/4. What is the expected cost, and how would it change if you could stop after any roll and keep the chance to roll again?

<details><summary>Solution</summary>

The number of rolls is geometric with p = 1/4, so the expected cost is 1/p = **4 units**.

Stopping options do not change this, because the game ends the moment a six appears. If the rule were to stop at any point and collect a payoff, the decision would depend on the payoffs. In that case, use the same conditioning method as in the [probability set](probability.md): the value of continuing equals the expected value of the next roll, and you stop when the payoff exceeds that value.
</details>

---

### 8. Sum of two dice given at least one 6 🟢

Two fair dice are rolled. You're told that at least one shows a 6. What's the probability that the sum is 7?

<details><summary>Solution</summary>

The outcomes with at least one 6 are 11 in number: (6,1) through (6,6) and (1,6) through (5,6).

Of these, the sums equal to 7 are (6,1) and (1,6). That gives 2 out of 11, so the probability is **2/11**.

The check is to write the sample space explicitly, which is the habit interviewers look for.
</details>
