# 1. Learn: Society

Explain how computing affects people.

Practise explaining how technology affects people. Start with the worked answer, then learn the terms for your own judgement. Allow two 40-minute study sessions. The Turing-machine section is a **Higher Level extension**.

## Build an answer in four steps

A **stakeholder** is anyone affected: a user, worker, owner or someone excluded from a system. A **mitigation** is an action that reduces a risk.

Suppose a library app recommends books using borrowing history:

| Step | Worked answer |
|---|---|
| Feature | The app finds patterns in books previously borrowed. |
| Benefit and person | A reader may discover a suitable book more quickly. |
| Risk and reason | A new reader has little history, so suggestions may be poor. |
| Mitigation and judgement | Let readers choose interests and ignore suggestions. Trial the app before relying on it. |

“AI is good” gives no reason. “The app may save searching time because it narrows a large catalogue” explains a benefit. Separate details supplied in the question from your assumptions.

**Try:** an automated stock alert orders replacements when a shelf sensor reports low stock. Give one benefit for a worker and one risk from a faulty sensor. <a href="https://tutors.dev/note/lc-cs/topic-14-society-ethics/note-02-feedback">Check the short-task answers</a>.

## History: learn a change and its effect

| Development | What changed? |
|---|---|
| Turing's 1936 model | Gave a precise mathematical description of computation. |
| Electronic computers, 1940s | Automated large calculations. |
| Manchester stored-program computer, 1948 | Held instructions in memory, so a stored program could direct the machine. |
| Transistors and integrated circuits | Made electronics smaller and more reliable. |
| Microprocessors | Put CPU functions on a chip, supporting personal and embedded computers. |
| Packet networks and common protocols | Allowed different networks to exchange data. |
| Web, proposed at CERN in 1989 | Made linked documents accessible through browsers. The Web uses the Internet. |
| Mobile devices, cloud services and data-driven AI | Widened access and increased scale, with new dependencies on devices, networks and data. |

**Named pioneer:** Grace Hopper developed the early A-0 programming tool and promoted higher-level languages, including work around COBOL. This helped programming move towards symbolic and English-like instructions. Explain her contribution without crediting one person with every part of a shared development.

Sources: [1948 timeline](https://www.computerhistory.org/timeline/1948/), [CERN on the Web](https://home.cern/science/computing/the-birth-of-the-web/where-web-was-born/), [Grace Hopper](https://www.computerhistory.org/revolution/story/117).

**Checkpoint:** cover the table. Name one development and finish “This mattered because …”.

Optional: the early-computing video is in the <a href="https://tutors.dev/course/lc-cs#side-reference">reference area</a>. The history table above is the written alternative.

## AI vocabulary with examples

**Artificial intelligence (AI)** covers systems doing tasks associated with intelligence, such as pattern recognition or planning. **Machine learning (ML)** learns patterns from examples. A fixed rule such as “warn below 30” automates work without ML.

| Term | Meaning | Example |
|---|---|---|
| Training | Adjust a model using examples | Learn from labelled bottle images |
| Inference | Use the trained model | Predict the category of a new image |
| Supervised learning | Learn from examples with target labels | Images labelled glass or plastic |
| Unsupervised learning | Find structure without target labels | Group similar borrowing patterns |
| Reinforcement learning | Learn actions through rewards from interaction | A game agent earns rewards for useful moves |
| Classification | Predict a category | Glass or plastic |
| Regression | Predict a numerical quantity | Predict tomorrow's demand |

**Narrow AI** handles a bounded task or range of tasks. **AGI**, artificial general intelligence, describes a proposed ability to learn and perform broadly across domains. Fluent conversation alone does not demonstrate AGI. **Generative AI** creates content such as text, images, audio, video or code from learned patterns. A plausible answer may still be wrong: check important claims against reliable sources. [ML background](https://www.ibm.com/think/topics/machine-learning).

## Test an AI claim

A classifier predicts “normal” for all 100 cases. There are 95 normal cases and 5 unusual cases. It gets **95/100 = 95% accuracy**, yet misses every unusual case.

Ask: What was tested? Were examples representative? How did it perform on rare cases? What happens when it is wrong?

- A **false positive** flags a case that should not be flagged: an ordinary bottle is rejected.
- A **false negative** misses a case that should be flagged: a damaged bottle is accepted.
- **Overfitting** means learning the training examples too closely and performing poorly on unfamiliar examples. Keep evaluation data separate from training data.
- **Confidence** is a score for one prediction. **Accuracy** is the fraction correct across a test set. A confidence of 0.9 does not prove correctness. To check **calibration**, see whether roughly 90% of many comparable 0.9 predictions are correct.

**Try:** explain why “95% accurate” alone is not enough to approve a diagnosis tool. Who is affected by missed cases and false alarms?

## Bias, privacy and responsibility

**Bias** is a systematic skew in data or decisions. It can arise from the sample, labels, features chosen as stand-ins for other facts, design choices or use conditions. Daytime-only training images may produce poor night-time recognition. More of the same data may leave the problem unchanged.

Test relevant groups and conditions. Let people challenge mistakes. Human review helps only if the reviewer can understand and override the result.

**Personal data** can identify someone directly or indirectly. Replacing a name with an ID is not necessarily anonymity: an ID-to-name table can reconnect it. For the library app, collect only what is needed, restrict access, allow corrections and decide when to delete old records. Use fictional data in these activities.

The [Irish Data Protection Commission](https://www.dataprotection.ie/en/individuals/data-protection-basics/principles-data-protection) explains principles including lawful, fair and transparent use; clear purposes; minimum necessary data; accuracy; storage limits; security; and accountability. Follow school policy for classroom work.

A service may earn money by using behaviour data to target advertisements; this is one form of **data monetisation**. Personalised political messages may reach interested voters, but hidden targeting can limit the views people see or make manipulation harder to notice. Explain the data used, who benefits and how transparency or user controls could reduce the risk.

## Access, ownership and environmental cost

The **digital divide** is unequal access because of connectivity, devices, skills, language or accessibility barriers. Screen readers, captions and alternative input devices can help. Universal design aims to make the main service usable by more people. An essential service may also need an offline alternative.

**Intellectual property** concerns rights in creations. A **licence** says how a resource may be reused. Credit code, images and data; explain your contribution. Downloading a file does not make you its author.

Computing uses materials and energy during manufacture, use and disposal. Consider device life, repair, data centres and electronic waste. Video meetings can reduce travel while still consuming electricity. Explain both effects before judging the overall benefit.

## Emerging technologies

| Technology | What it does | Benefit and limit |
|---|---|---|
| Quantum computing | Uses quantum states and suitable algorithms | May help particular problems; not faster at every task |
| Edge computing | Processes data near its source | Can reduce delay and traffic; local devices still need maintenance and security |
| Internet of Things (IoT) | Connects devices that sense or act | Supports remote monitoring; adds devices needing protection |
| Biometrics | Recognises physical or behavioural characteristics | Convenient identification; false matches and hard-to-replace compromised traits are risks |
| Blockchain | Links records using cryptography and distributed agreement | Can make changes evident; cannot prove an original claim was true |

Blockchain designs have different energy and governance costs. Sources: [quantum computing](https://www.ibm.com/think/topics/quantum-computing), [edge computing](https://www.ibm.com/think/topics/edge-computing).

**Checkpoint:** a sensor processes readings locally and sends only a summary to the cloud. Which technology is this? What work still needs doing on the sensor device?

## Higher Level extension: trace a Turing machine

A **Turing machine** is a mathematical model with a tape, a head that reads/writes one cell, states and rules. The tape is conceptually unbounded. Each rule says what to write, where to move and which state comes next.

Our machine adds one to a **unary** number: `111` means three and `_` is blank. Number cells from 0. Start in `scan` at the first symbol.

| Current state | Read | Write | Move | Next state |
|---|---|---|---|---|
| scan | 1 | 1 | Right | scan |
| scan | _ | 1 | Left | halt |

Look up one rule each step for `11_`:

| Step | Head before | Read | Action | Head after | Tape after |
|---|---:|---|---|---:|---|
| 1 | 0 | 1 | Keep 1; move right; stay in scan | 1 | `11_` |
| 2 | 1 | 1 | Keep 1; move right; stay in scan | 2 | `11_` |
| 3 | 2 | _ | Write 1; move left; halt | 1 | `111` |

The blank ends the finite run of ones, so the machine halts. There is no rule for other input symbols; do not invent one. **Try:** trace `111_` and `_`. Expected final nonblank tapes: `1111` and `1`.

A **Turing test** concerns whether an evaluator can distinguish conversational behaviour. It is different from the tape machine. Conversational imitation does not establish correctness, consciousness or reliability. Sources: [1936 computation paper](https://theory.stanford.edu/~trevisan/cs172-07/turing36.pdf), [1950 imitation-game paper](https://doi.org/10.1093/mind/LIX.236.433).

## Careers checkpoint

A developer writes software; a data analyst investigates data; a security specialist protects systems; a hardware engineer works with physical components. Testers, accessibility specialists and user researchers check whether systems work for people. Choose one role and explain how it could improve the library app. Communication and knowledge of users matter alongside coding.


**Next:** <a href="https://tutors.dev/lab/lc-cs/topic-14-society-ethics/book-01-practice">2. Practise</a>.
