# Computer systems: from input to execution

Explain how hardware, software and operating systems work together, and justify choices for a task.

## Outcomes

Identify input, processing, storage and output; distinguish RAM, ROM and secondary storage; explain operating-system services; trace a simple instruction cycle; compare language translators; and relate hardware developments to practical capability. Higher Level extensions examine CPU components and a more detailed fetch–decode–execute cycle.

## A system is a set of interacting parts

A library self-service station reads a card and a book code, checks a database, records the loan, then displays a due date. The scanner is input hardware, the CPU processes instructions, storage holds the catalogue, and the screen is output hardware. A touchscreen performs both input and output. A sensor converts a physical measurement into an electrical signal; an actuator changes the physical world. Do not identify a component by its shape alone: explain its role in the scenario.

Hardware is the physical equipment. Software is the instructions and associated data that make it perform tasks. System software supports the computer itself; an operating system and device drivers are examples. Application software serves a user task, such as editing a document or analysing measurements. Firmware is software stored in a device to support its operation; it is not a third category of physical material.

## Memory and storage

| Component | Main role | What happens without power? | Suitable example |
|---|---|---|---|
| RAM | Instructions and data actively in use | Ordinary RAM is volatile | An unsaved program and its variables |
| ROM/non-volatile firmware memory | Persistent start-up or device instructions | Retains data | Boot firmware |
| Secondary storage | Longer-term files and programs | Normally retains data | A saved photo on an SSD |
| CPU registers | Very small, fast working locations inside the CPU | Normally volatile | An instruction address or arithmetic operand |
| Cache | Keeps copies of likely-needed instructions/data close to the CPU | Normally volatile | Recently used memory contents |

ROM is traditionally read-only; modern firmware often uses electrically rewritable non-volatile memory. Avoid saying that every modern firmware chip can never change. RAM capacity and storage capacity describe different resources. More storage does not by itself let a running program hold more active data in RAM. A solid-state drive has no moving read head and offers fast access; a magnetic hard drive may offer economical capacity but moving parts affect latency and robustness. Choose using the actual task, cost and environment, not “newer is always better”.

## What an operating system does

The OS schedules processor time, manages memory, controls devices through drivers, organises files and directories, and enforces access permissions. It provides an interface and services for applications. Resource management allocates CPU time and memory between competing programs. File management includes names, folders, read/write operations and permissions. These are different functions; merely repeating “it manages resources” does not explain either.

Suppose a pupil edits a report while music plays. The OS schedules work from both programs; it allocates memory and handles keyboard, display and audio devices. A scheduling decision can make interactive input responsive without giving one application permanent exclusive use of the processor. If a program crashes, protected process memory can help contain the damage, although isolation is not an absolute guarantee against every fault.

An interface can be graphical, command based, menu driven, touch or voice based. A command line can support precise repeatable operations but requires command knowledge. A menu can make common options discoverable but can become slow or restrictive with deeply nested choices. Compare against a user's needs and environment; a loud room and a speech impairment affect a voice interface differently.

## CPU and the stored-program idea — Higher Level extension

A stored-program computer keeps instructions as well as data in memory. The **control unit** coordinates instruction execution. The **arithmetic logic unit (ALU)** performs arithmetic and logical operations. Registers hold working values. The **program counter (PC)** holds the address of the next instruction; an instruction register holds the current instruction. Buses carry information between components: address information identifies a location, data carries values, and control signals coordinate actions.

A simplified fetch–decode–execute cycle is: use the PC to fetch an instruction from memory; update the PC as appropriate; decode the instruction; execute it; repeat. A branch can change the next instruction address. The precise internal sequence varies by processor, so use the model specified in a question.

Consider a simplified machine with `LOAD 6`, `ADD 4`, `STORE answer`, `HALT`. After LOAD the working register contains 6. After ADD it contains 10. STORE writes 10 to the named memory location. HALT stops this program. The ALU performs the addition; the control unit directs the sequence. Do not describe the PC as holding every program instruction: it identifies the next one.

## Languages and translation

Machine code is the CPU's encoded instruction language. Assembly uses symbolic operation names and is translated by an assembler. High-level languages express ideas with more human-oriented constructs, usually improving portability and readability. A compiler translates source into another form before execution of the translated result. An interpreter executes or evaluates program instructions using a runtime. Real implementations combine techniques; Python commonly compiles source to bytecode that a virtual machine executes. Therefore “Python is interpreted” is a useful introductory description, not proof that no compilation ever happens.

A syntax error violates language rules. A runtime error arises during execution, such as dividing by zero. A logic error produces the wrong result even though the program runs. Translation success cannot establish that the program solves the intended problem. Topics 06 and 09 turn this distinction into debugging practice.

## Hardware development and performance

Mechanical devices automated physical operations; electronic switching made very rapid operations possible. Transistors replaced many vacuum-tube roles with smaller, more reliable and lower-power components. Integrated circuits put many components on one chip; microprocessors enabled compact general-purpose computers. Explain a milestone through its effect, rather than listing a date alone.

Moore's law describes a historical observation about growth in transistor counts, often summarised as doubling roughly every two years. It is not a physical law and does not say every program's speed doubles on that schedule. Clock rate, instructions per cycle, memory access, core count, software and energy limits all affect performance. Multiple cores help work that can be divided; they do not make every sequential algorithm proportionally faster.

## Worked selection problem

A school needs a classroom sensor logger that operates quietly for hours. A suitable design prioritises low energy use, sufficient memory for readings, compatible sensor inputs and dependable storage. A high-powered gaming graphics card adds cost and power demand without addressing the task. State one advantage and one limitation of your selected device: for example, low power helps battery life, but limited memory restricts how much data can be buffered. A justified answer ties both points to the actual scenario.

## Misconceptions to repair

Saving a file and storing a variable in RAM are different actions. An OS is software, not the CPU. A faster CPU does not fix a slow network connection automatically. A register is not a file on disk. More cores are not equivalent to the same factor of improvement for every workload. Use a labelled input–process–output–storage diagram to check where each operation happens.

## Virtual memory and the accumulator — worked extension

When active memory demand exceeds available physical RAM, an operating system can use secondary storage as backing for virtual memory, moving pages between storage and RAM. This allows a process to use a virtual address space that is not simply a one-to-one view of installed RAM. It is not equivalent to installing equally fast extra RAM: accessing storage-backed pages can be much slower, and excessive page movement can make the system unresponsive. A useful exam explanation names both the capacity benefit and performance limitation.

An **accumulator** is a register used to hold intermediate arithmetic or logical results in a simplified CPU model. In `LOAD 7; ADD 5; SUBTRACT 2`, the accumulator values become 7, 12, 10. Meanwhile the program counter tracks the address of the next instruction. If these instructions are at addresses 20, 21 and 22 and each advances to the next address, after executing the third instruction the next address is 23. The data result 10 and instruction address 23 have different purposes.

Practice: trace an accumulator through LOAD 4; MULTIPLY 3; ADD 1. The final result is 13. Explain why the accumulator cannot replace secondary storage for a permanent file: it is a small volatile working register, designed for current execution.
