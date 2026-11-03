# Door logic

Sketch a door rule with logic gates.

Use this after the Higher Level truth-table task. You can draw on paper instead.

**Rule:** a valid card is required, plus either a booking or a staff override.

1. Label inputs **C** (card), **B** (booking), **S** (staff override).
2. Join B and S to an **OR** gate.
3. Join that result and C to an **AND** gate.
4. Label the final output **Open**.

**Check:** C=0, B=1, S=1 must give **0** (closed). C=1, B=0, S=1 must give **1** (open).

Text version: **Open = C AND (B OR S)**. <a href="https://tutors.dev/lab/lc-cs/topic-03-representation-logic/book-01-practice">Return to the lab</a>.
