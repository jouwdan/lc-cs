# 1. Learn: Systems

See how CPU, memory and the OS work.

Follow a library loan from scanning a book to saving the record. Use that example to learn each computer part.

**Split this lesson:** first study sections 1–4, then do the diagram in the lab. Return for sections 5–8 before the quiz. Read the Higher Level sections when ready.

## 1. Input, process, output and storage

A library machine scans your card and a book, records the loan and shows a due date.

| Job | Library example |
|---|---|
| **Input:** receives data | Scanner reads the book code. |
| **Process:** follows instructions | CPU checks whether the book can be borrowed. |
| **Output:** presents a result | Screen shows the due date. |
| **Storage:** keeps data | A saved loan record stays on storage. |

**Hardware** is physical equipment, such as a scanner. **Software** is the instructions and associated data, such as the loan program.

A touchscreen is both input and output: it detects a touch and displays a result. A **sensor** measures something, such as temperature. An **actuator** changes something, such as a motor turning a fan.

**Try:** is a printer input or output? What about a microphone?

**Check:** a printer is output; a microphone is input.

## 2. RAM is not the same as saved storage

**Volatile** means the contents are lost when power is removed.

| Part | What it holds | Keeps its contents without power? |
|---|---|---|
| **RAM** | Programs and data currently being used | No, ordinary RAM is volatile. |
| **ROM / firmware memory** | Start-up or device instructions | Yes. |
| **SSD or hard drive** | Saved files and programs | Yes, normally. |
| **CPU register** | A tiny amount of data the CPU is working on | No, normally. |
| **Cache** | Copies of data/instructions likely to be needed soon | No, normally. |

**Example:** you type a paragraph but do not save it. It is working data in RAM. Saving writes a copy to storage, so the saved version can remain after shutdown.

Registers are very small, fast working locations **inside the CPU**. RAM is larger main memory and is slower to access than registers.

ROM traditionally means read-only memory. Modern firmware often uses rewritable non-volatile memory, so firmware can sometimes be updated.

An **SSD** has no moving read head. It is usually faster to access and better suited to being moved. A **hard drive (HDD)** has moving parts and may offer more capacity for the price. Choose for the task and budget.

**Try:** will a larger SSD alone give a running program more RAM?

**Check:** no. Storage capacity and RAM capacity are different.

## 3. What does an operating system do?

An **operating system (OS)** manages the computer and provides services for applications. It is software, not a CPU.

| OS job | Example |
|---|---|
| Schedule CPU time | Share processing time between a report editor and music player. |
| Manage memory | Allocate RAM to running programs. |
| Manage files | Save, name and organise files in folders. |
| Control devices | Use a **driver** to communicate with a printer. |
| Manage access | Decide which accounts can open or change a file. |

The OS and drivers are **system software**. A document editor or game is **application software**: it does a user's task. **Firmware** is software stored in a device to help operate it.

**Try:** name two OS services used when saving and printing a report.

**Check:** file management saves it; a printer driver controls printing. Memory and CPU scheduling also support the work.

## 4. Choose an interface for its user

An **interface** is how a person interacts with a system.

- **Graphical:** windows, icons and buttons make options visible.
- **Command line:** typed commands can repeat precise tasks, but must be learned.
- **Menu:** users choose from listed options; many nested menus can be slow.
- **Touch or voice:** useful in some settings, but affected by access needs and surroundings.

**Worked choice:** a touchscreen with large labelled buttons suits a public loan station. A command line would require visitors to know commands. Voice controls could be difficult in a noisy room or for a person with a speech impairment.

**Pause here:** <a href="https://tutors.dev/lab/lc-cs/topic-02-computer-systems/book-01-practice">start the library diagram in the lab</a>. Return for the next sections afterwards.

## 5. The CPU follows instructions

The **central processing unit (CPU)** executes instructions.

| CPU part | Job |
|---|---|
| **Control unit** | Coordinates instruction execution. |
| **Arithmetic logic unit (ALU)** | Performs arithmetic and logic. |
| **Register** | Holds a working value or address. |
| **Program counter (PC)** | Holds the address of the next instruction. |
| **Instruction register** | Holds the current instruction. |

A **stored-program computer** keeps instructions and data in memory.

The simplified cycle is **fetch → decode → execute → repeat**:

1. Fetch the instruction at the address held in the PC.
2. Decode it: determine what operation it requests.
3. Execute it, such as adding two numbers.
4. Continue with the next instruction. A branch can change its address.

The PC is updated during this process; follow the precise CPU model supplied in an exam question.

### Worked trace

These are instructions for an invented machine, not Python. Here, `STORE` copies a value to a named **main-memory location**. It does not save a file to disk; this memory value can be lost when power is removed.

| Instruction | Working register afterwards | Memory value `answer` |
|---|---:|---|
| LOAD 6 | 6 | Not set |
| ADD 4 | 10 | Not set |
| STORE answer | 10 | 10 |
| HALT | 10 | 10 |

The ALU does the addition. The control unit directs the steps. The PC holds an **instruction address**, not the answer 10.

**Try:** change `ADD 4` to `ADD 7`. What value is written to memory?

**Check:** 13.

### Higher Level: buses and the accumulator

A **bus** carries information between components. The address bus identifies a location; the data bus carries values; control signals coordinate operations.

An **accumulator** is a register used for intermediate results in a simple CPU model. `LOAD 7; ADD 5; SUBTRACT 2` gives 7, 12, then 10. If those instructions occupy addresses 20, 21 and 22, the next address is 23 in this simple sequential model. The result **10** and the address **23** have different jobs.

### Higher Level: virtual memory

An OS can move memory pages between RAM and secondary storage. This supports a virtual address space and helps when physical RAM is under pressure.

**Benefit:** more data can be managed than fits in physical RAM at once. **Limit:** accessing storage-backed pages is much slower than RAM; frequent transfers can slow the computer badly. It is not the same as installing equally fast extra RAM.

## 6. Languages and translators

| Term | Meaning |
|---|---|
| Machine code | Encoded instructions a CPU executes. |
| Assembly language | Symbolic names for machine operations. |
| Assembler | Translates assembly into machine code. |
| High-level language | Uses constructs closer to human problem solving, such as Python loops. |
| Compiler | Translates source into another form before that result is run. |
| Interpreter | Executes or evaluates instructions using a runtime. |

Real systems can combine these approaches. Python commonly compiles to bytecode which a virtual machine executes.

Successful translation does **not** prove correct results:

- A **syntax error** breaks language rules, such as missing punctuation.
- A **runtime error** occurs while running, such as division by zero.
- A **logic error** gives a wrong answer even though the program runs.

## 7. Hardware milestones and speed

| Development | Why it mattered |
|---|---|
| Mechanical devices | Automated physical operations. |
| Electronic switching | Allowed much faster operations. |
| Transistors | Replaced many vacuum tubes with smaller, lower-power, more reliable components. |
| Integrated circuits | Put many components on one chip. |
| Microprocessors | Helped make compact general-purpose computers possible. |

**Moore's law** is a historical observation about growing transistor counts, often described as roughly doubling every two years. It is not a physical law or a promise that every program gets twice as fast.

Performance also depends on clock rate, work per clock cycle, RAM access, cores, software and energy limits. More cores help tasks that can be split up. A faster CPU will not automatically fix a slow internet connection.

## 8. Give a reason for a hardware choice

For a quiet battery-powered sensor logger, choose low energy use, enough memory, compatible sensor inputs and dependable storage. A gaming graphics card adds power use and cost without helping this job.

Use this answer pattern: **choice → benefit for this task → limitation**.

Example: “Choose a low-power processor so the logger runs longer on its battery. Check that it is fast enough to process each reading on time.”

**Next:** <a href="https://tutors.dev/lab/lc-cs/topic-02-computer-systems/book-01-practice">2. Practise: Design a library computer →</a>
