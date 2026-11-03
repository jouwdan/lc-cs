# Computing, society, AI and history

Concepts, worked examples and practical reasoning for computing, society, ai and history.

## Explain a consequence, not a slogan

Computing changes who can do a task, how quickly it can be done, what information is available and who controls it. A strong answer connects a technical feature to a specific consequence for a stakeholder. “Automation is good” is too vague. “An automated stock alert can reduce missed orders, but incorrect sensor readings may trigger unnecessary purchases” identifies a mechanism, benefit and limitation. Consider users, workers, maintainers, excluded groups and the wider environment.

Use a balanced structure: describe the system, identify a benefit, explain a risk, propose a proportionate mitigation and justify your conclusion. Balance does not mean claiming every option is equally good. Evidence may support one choice strongly. Separate what the scenario tells you from assumptions you introduce. Discuss a concrete case rather than listing unrelated advantages and disadvantages learned by heart.

## Milestones and their significance

History is more useful when it explains changes in capability. Turing's 1936 work formalised a model of computation. Early electronic computers in the 1940s demonstrated large-scale automated calculation. The Manchester experimental computer ran a stored program in 1948: instructions could be held in memory, a central idea in modern architectures. Transistors and integrated circuits enabled smaller, more reliable electronics; microprocessors concentrated CPU functions on chips, supporting personal and embedded computing.

Packet networks and common protocols enabled machines to communicate across different networks. The Web made linked documents accessible through browsers: Tim Berners-Lee proposed it at CERN in 1989. The Web is a service using the Internet, not another name for the Internet. Mobile devices, cloud services and data-driven AI later changed access and scale. Explain both opportunities and new dependencies rather than treating newer technology as automatically better.

Sources: [Computer History Museum's 1948 timeline](https://www.computerhistory.org/timeline/1948/) and [CERN's account of the Web](https://home.cern/science/computing/the-birth-of-the-web/where-web-was-born/). For an exam milestone, connect a named development to a meaningful effect; avoid unsupported “first ever” claims.

Grace Hopper is one named computing pioneer whose contribution can be explained precisely: she developed the early A-0 programming tool and promoted higher-level languages, including work around COBOL. Her work helped move programming towards more accessible symbolic and English-like instructions. See the [Computer History Museum account](https://www.computerhistory.org/revolution/story/117). Explain the contribution rather than attributing every development in a collaborative field to one person.

## Higher Level: a Turing-machine trace

A Turing machine is an abstract computational model with a tape of cells, a read/write head, a finite set of states and rules. A rule depends on current state and scanned symbol, then specifies what to write, how to move and the next state. The tape is conceptually unbounded; a classroom diagram shows only the relevant portion. This is not a modern computer's physical design and not a test of intelligence.

Our original machine increments a non-negative unary number. Three consecutive `1` symbols represent three; `_` denotes blank. Start in `scan` at the leftmost `1`, or at a blank for zero.

| State | Read | Write | Move | Next state |
|---|---|---|---|---|
| scan | 1 | 1 | Right | scan |
| scan | _ | 1 | Left | halt |

With tape `111_`, after step 1 the head is at cell 1; after step 2 at cell 2; after step 3 at blank cell 3. Step 4 writes `1`, moves left to cell 2 and halts. The tape now contains `1111`: three became four. A trace table should show step, state, head position, read symbol, action and tape. The machine halts because a finite run of ones is followed by a blank. Its input contract excludes other symbols; do not invent transitions for them.

The [1936 paper](https://theory.stanford.edu/~trevisan/cs172-07/turing36.pdf) introduced the foundational model. Turing's later [1950 paper](https://doi.org/10.1093/mind/LIX.236.433) discusses an imitation-game approach to machine intelligence. A Turing test concerns whether an evaluator can distinguish conversational behaviour; it is not the tape machine. Conversational imitation alone does not establish correctness, consciousness or reliability.

## Artificial intelligence and machine learning

AI is a broad area concerned with systems performing tasks associated with intelligence, such as recognising patterns or planning. A rule-based system follows explicitly written rules. Machine learning fits patterns from training examples and applies them to new inputs. Training changes model parameters; inference uses the trained model. A system can be automated without using machine learning, such as a fixed temperature threshold controller.

Supervised learning uses examples with target labels, such as images labelled by category. Unsupervised learning explores structure without those target labels, such as clustering similar observations. Reinforcement learning uses feedback in the form of rewards to learn behaviour through interaction. Classification predicts a category; regression predicts a numerical quantity. These descriptions explain the learning setup; they do not guarantee a model is suitable or fair. See [IBM's machine-learning overview](https://www.ibm.com/think/topics/machine-learning).

Keep training and evaluation examples separate. A model may memorise training patterns and perform poorly on unfamiliar data: this is overfitting. Evaluate on representative data and inspect different types of mistakes. If 95 of 100 examples are “normal”, always predicting normal achieves 95% accuracy while missing every unusual case. The cost of false positives and false negatives depends on the application. A convincing generated explanation may still contain factual errors, so verify important claims against suitable sources.

**Narrow AI** is designed for a bounded task or range of tasks. **Artificial general intelligence (AGI)** describes a proposed broad capability to learn and perform across many domains; do not assume a fluent conversational system meets that definition. **Generative AI** produces new content such as text, images, audio, video or code from learned patterns. Generating a plausible output is different from retrieving a verified fact.

A model's confidence score concerns an individual prediction; accuracy summarises the fraction of correct predictions over an evaluated set. A prediction assigned 0.9 confidence is not itself proof of correctness. A well-calibrated model would be correct about 90% of the time among many comparable predictions assigned 0.9, but calibration must be tested. Do not confuse a high score on one case with high overall accuracy or fairness across groups.

## Bias, privacy and human responsibility

Bias can enter through sampling, labels, proxy features, design choices and deployment conditions. More data does not automatically remove it. A system trained only on daytime images may fail at night. Test relevant groups and conditions, document limitations and allow meaningful human review when consequences matter. Explain who can challenge an incorrect decision and how it can be corrected. A “human in the loop” is ineffective if the person cannot understand or override the output.

Personal data can identify a person directly or indirectly. Replacing a name with an identifier does not necessarily make a dataset anonymous if the person can still be reidentified. Collect less, limit access, protect storage and decide when information is no longer needed. The [Irish Data Protection Commission](https://www.dataprotection.ie/en/individuals/data-protection-basics/principles-data-protection) describes GDPR principles including fair and transparent lawful processing, purpose limits, minimisation, accuracy, retention limits, security and accountability. Apply classroom examples through school policy and synthetic data rather than collecting classmates' sensitive information.

## Inclusion, ownership and environmental cost

Adaptive technologies include screen readers, alternative input devices and captions. Universal design aims to make mainstream systems usable by a wider range of people. A digital service may exclude someone without reliable connectivity, an appropriate device, language support or accessible controls: this is a digital-divide issue, not simply reluctance to use technology. Offer a practical alternative where access is essential.

Intellectual property and licences determine permitted reuse. Being able to download a file does not mean you created it or can remove attribution. Credit code, media and data sources and distinguish your contribution. In assessment, learning from an example differs from presenting another person's work as your own. Maintain an honest development record.

Computing also consumes materials and energy. Consider manufacture, device lifetime, repair, electricity use, data-centre operation and electronic waste. A remote service may save travel while increasing computing demand. Evaluate the whole relevant lifecycle and avoid claiming that cloud or paperless services have zero environmental impact. Appropriate hardware and restrained data collection can reduce unnecessary resource use.

## Emerging technologies: describe mechanisms and trade-offs

The 2024 Higher Level paper names quantum computing, edge computing, IoT, biometrics and blockchain. Quantum computers use quantum states and algorithms that may offer advantages for particular problems; they are not universally faster replacements for ordinary computers. [IBM's introduction](https://www.ibm.com/think/topics/quantum-computing) gives context. Edge computing processes data nearer its source, potentially reducing latency and network traffic, while distributing maintenance responsibilities; see [IBM's edge overview](https://www.ibm.com/think/topics/edge-computing).

IoT connects devices that sense or act, supporting remote monitoring but increasing the number of devices requiring protection. Biometrics use physical or behavioural characteristics for recognition; convenience must be weighed against false matches and the difficulty of replacing a compromised characteristic. Blockchain links records using cryptographic techniques and distributed agreement; it does not prove that information entered into the system was true, and different designs have different energy and governance costs.

## Careers and a reasoned decision

Computing work includes software development, data analysis, cybersecurity, hardware engineering, accessibility, testing and user research. These roles combine communication and domain knowledge with technical skills. For a final practice task, evaluate a fictional automated library recommendation system. State what it uses, what it can help with, who might be disadvantaged, what data it truly needs, how errors are challenged and which evidence would justify adoption. A defensible answer explains both the technology and the people affected.
