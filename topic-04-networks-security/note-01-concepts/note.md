# 1. Learn: Networks

Follow web requests and protect data.

Follow a web request, then choose protections for a small school booking system.

**Two sessions:** study sections 1–5 and draw a network; next study sections 6–9 and choose security controls. Higher Level sections explain protocols in more detail.

## 1. A network connects devices

A **network** lets devices exchange data and share resources.

| Term | Meaning | Example |
|---|---|---|
| LAN | Local area network in a limited place | A school's computers |
| WAN | Wide area network across larger distances | Connected school campuses |
| Internet | A network of interconnected networks | Global network infrastructure |
| World Wide Web | A service using the internet | Pages opened in a browser |

The internet and web are different. Email and internet voice calls need not be web pages.

A **client** requests a service. A **server** provides it. These describe roles, not the size or price of a computer.

In **client–server** computing, a server can centralise accounts, files and backups. If it fails, clients may lose that service. In **peer-to-peer** computing, devices can both request and provide resources; management can be harder to keep consistent.

## 2. Know what each device does

| Device | Main job |
|---|---|
| Switch | Connect devices within a LAN; forward frames to the appropriate local link. |
| Router | Forward packets between networks. |
| Wireless access point | Connect Wi-Fi devices to a network. |
| Modem / optical termination device | Provide the relevant connection to the service provider. |

A **packet** is a unit of data sent across a network. A **frame** is a link-layer unit used for delivery over a local connection. A home router box often combines several of the jobs above.

**Try:** which device forwards packets from one network to another?

**Check:** a router.

## 3. Names, addresses and protocols

| Term | What it does |
|---|---|
| IP address | Identifies a network interface for communication over IP. |
| MAC address | Identifies an interface on link technologies such as Ethernet. |
| Domain name | Gives people a readable name for a service. |
| DNS | Looks up records for a name, including IP addresses. |
| URL | Specifies a resource, with a scheme, host and often a path. |

Example URL: `https://example.org/lessons`. The scheme is `https`, the host is `example.org` and the path is `/lessons`.

A **protocol** is a set of communication rules.

| Protocol | Job |
|---|---|
| IP | Address and route packets. |
| TCP | Provide a reliable, ordered stream; retransmit data when needed. |
| HTTP | Define web requests and responses. |
| HTTPS | Protect HTTP traffic using TLS. |

**TLS** encrypts traffic in transit and authenticates the server endpoint using certificates. HTTPS does not guarantee that a site's claims are true.

## 4. Follow one web request

1. You enter a URL.
2. The browser finds the host's IP address, using DNS or cached information.
3. Traffic goes through the local network and router towards the server.
4. For HTTPS, a secure connection is established.
5. The browser requests the resource. The server responds.
6. The browser displays the page, often requesting images and other files too.

**DNS finds address information; it does not send the page.**

**Try:** a computer has no network connection. Would changing a page's HTML repair that?

**Check:** no. Check the cable or Wi-Fi connection first. A missing page path, a DNS problem and a disconnected cable need different checks.

### Higher Level: four TCP/IP layers

| Layer | Job | Example |
|---|---|---|
| Application | Define service messages | HTTP, DNS |
| Transport | Communicate between application endpoints | TCP, UDP |
| Internet | Address and route packets | IP |
| Network access / link | Carry data across each local link | Ethernet, Wi-Fi |

Some models split the bottom layer further. Use the model a question requests.

Each sending layer adds information for its job; the receiver interprets the corresponding information. A router can forward packets without understanding the article being requested.

Packets may be delayed, lost or take different paths. TCP reconstructs a reliable ordered stream. UDP does not itself provide TCP's delivery and ordering guarantees; applications may choose it when timely arrival matters more than waiting for a retransmission.

**Try:** place a web request, a TCP port, an IP destination and an Ethernet frame in the table.

**Check:** application, transport, internet, network access.

## 5. Wired, wireless and network shape

| Choice | Benefit | Limitation |
|---|---|---|
| Wired Ethernet | Stable connection with less radio interference | Needs cabling; restricts movement |
| Wi-Fi | Lets users move around | Distance, walls, interference and shared radio capacity affect performance |

Both need security controls. A cable alone does not prevent every attack.

A **topology** is the arrangement of network connections:

- **Star:** each device connects to a central component. One endpoint cable failure affects that device; central-switch failure can affect many.
- **Bus:** devices share a backbone.
- **Ring:** connections form a loop.

Real networks may combine shapes and backup paths. Explain the failure in the diagram you are given.

### Higher Level: voice over IP

**VoIP** carries voice over IP networks. Sound is digitised, encoded into packets and reconstructed for playback. It can reduce costs and combine calling with other applications, but depends on power, service and network conditions.

| Measure | Meaning | Effect on a call |
|---|---|---|
| Bandwidth | Capacity per unit time | Too little limits how much data can be carried. |
| Latency | Delay | People wait for each other's speech. |
| Jitter | Variation in delay | Audio arrives unevenly. |

A buffer can smooth uneven arrivals but adds delay. Late audio may no longer be useful, even if retransmission eventually delivers it.

## 6. Three security goals

| Goal | Meaning | Booking-system example |
|---|---|---|
| **Confidentiality** | Only permitted people can read data | Keep private contact details private. |
| **Integrity** | Protect against unauthorised changes | Stop students editing other bookings. |
| **Availability** | Keep the service usable when needed | Restore the system after a failure. |

Name the data or service at risk before choosing a control.

## 7. Match each threat to a control

| Threat | Useful control | What it does |
|---|---|---|
| Phishing: a deceptive request for information or action | Verify through a known separate channel | Check the request before responding. |
| Malware: malicious software | Updates and anti-malware tools | Repair known flaws and detect some threats. |
| Ransomware: malware that can lock data | Tested separate backups | Restore usable data after an incident. |
| Unauthorised changes | Separate accounts and permissions | Limit who can edit which records. |
| Unwanted network traffic | Firewall rules | Filter traffic according to rules. |

No control is perfect. Backups help recover from deletion; they do not prevent the original deletion. Ransomware can also steal data, so restoration is not the only concern.

## 8. Accounts, encryption and hashing

**Authentication** asks “Who are you?” **Authorisation** asks “What are you allowed to do?”

Use long unique passwords, an approved password manager where available and **multi-factor authentication (MFA)**. MFA combines different kinds of factor, such as a password (knowledge) and a possession-based token. Two passwords are still the same factor type.

**Least privilege** means giving only the access a role needs. Remove access when it is no longer needed.

| Method | Purpose |
|---|---|
| Encryption | Use a key to protect readable data; decrypt with the appropriate key. |
| Hashing | Produce a fixed-size digest; it is not intended to be reversed. |

Real password storage needs suitable password-hashing methods and salts. Our tasks use fictional data and do not ask you to build a real login system or collect anyone's password.

## 9. Explain a choice, including its limit

Use **control → how it helps → limitation**.

**Worked answer:** “Only the organiser can edit all bookings. This stops ordinary members changing other people's records. The organiser can still make a mistake, so the system also needs recoverable backups.”

### Cloud or local storage?

**Cloud computing** supplies computing services over a network. Cloud storage can support access from different devices, collaboration and off-site copies. It depends on connectivity, provider availability and account security.

**Sync is not automatically backup:** a deletion may spread to all synced devices. Check version history and recovery separately.

Compare access needs, permissions, costs and recovery. Remote servers still use electricity, cooling and materials. Cloud infrastructure may improve resource use, but it is not automatically cheaper, greener or safer for every task.

**Try:** name one benefit and one limit of cloud storage for a group project.

**Check:** members can access shared files from different places; an internet outage can interrupt access. Other justified pairs are valid.

**Next:** <a href="https://tutors.dev/lab/lc-cs/topic-04-networks-security/book-01-practice">2. Practise: Design a booking network →</a>
