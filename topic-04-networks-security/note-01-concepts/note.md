# Networks, the internet and cybersecurity

Follow a request across a network and explain protections in terms of the threats they address.

## Outcomes

Distinguish a local network from the internet and the web; identify switches, routers and servers; explain addressing and protocols; compare wired and wireless connections; and recommend proportionate security measures. Higher Level extensions examine TCP/IP and VoIP more closely. Use only your own isolated examples: none of the activities requires probing a real school network.

## Devices and connections

A network connects devices so they can exchange data and share resources. A local area network (LAN) serves a limited place such as a school. A wide area network connects across larger distances. The internet is a network of interconnected networks. The World Wide Web is one service that uses the internet: browsers request resources using web protocols. Email and voice calls can use the internet without being web pages.

A switch forwards frames between devices in a local network, using link-layer addresses. A router forwards packets between networks, using network addresses and routing information. A wireless access point connects wireless devices to a network. A modem or optical termination device provides the relevant access link; a domestic box often combines several roles. Do not assume a single physical box has only one logical function.

A client requests a service. A server supplies a service such as files, web pages or database queries. These are roles, not permanent labels for expensive and cheap computers. In a peer-to-peer arrangement, peers can provide and consume resources. A central server can simplify administration and backups but creates a dependency on its availability and capacity; peer systems distribute responsibilities but can be harder to manage consistently.

## Addressing and protocols

An IP address identifies an interface for communication on an IP network. A MAC address is a link-layer identifier used on technologies such as Ethernet. A domain name is a human-friendly name; DNS resolves names to records, including IP addresses. DNS does not itself fetch the web page. A URL also includes a scheme and can include a path to a resource.

A protocol is an agreed set of rules for communication: message structure, ordering and interpretation. IP handles addressing and routing packets. TCP provides a reliable, ordered byte stream over IP by tracking delivery and retransmitting when needed. HTTP defines web requests and responses. HTTPS uses TLS to protect HTTP traffic in transit and authenticate the server endpoint through certificates. Encryption does not prove that the site's claims are honest or that the endpoint itself is safe.

**Higher Level:** TCP and IP serve different layers; do not treat TCP/IP as a single device. Packets can take different paths and encounter delays or loss. A reliable transport restores the intended stream for the application. Some real-time applications use UDP and other protocols because waiting for retransmissions can harm timeliness. A protocol choice trades requirements rather than simply choosing “the fastest”.

## A web request, step by step

A learner enters a school resource URL. The browser may use cached information or ask DNS for the host address. The device sends traffic through the local network and router toward the server. For HTTPS, a secure connection is established. The browser sends an HTTP request and the server returns a response, often containing HTML and references to additional resources. The browser may make more requests for images, scripts and styles before rendering the page.

If the page fails, separate possible causes: no local link, DNS failure, unreachable server, failed authentication or an unavailable resource. Repeatedly changing the page HTML cannot repair a disconnected network cable. A useful troubleshooting question narrows which part of the path has evidence of working.

## VoIP — Higher Level extension

Voice over IP describes carrying voice communications over IP networks. Audio is digitised, encoded and sent as packets, then reconstructed for playback. IP provides the network addressing/routing role; VoIP is a use of networking for voice communication and involves additional signalling and media protocols. It can reduce costs and integrate calling with applications, but quality depends on network conditions, electricity and the service.

Bandwidth is capacity per unit time; latency is delay; jitter is variation in delay. A call can sound poor despite adequate average bandwidth if packets arrive too late or irregularly. A buffer can smooth variation but adds delay. Explain the effect on the person speaking, rather than saying only “the internet is slow”.

## Wired, wireless and topology

Wired Ethernet can offer stable performance and less radio interference but requires cabling and restricts movement. Wi-Fi supports mobility and easier installation in some buildings, but shared radio conditions, distance, obstructions and interference affect performance. Both require security controls. Wireless does not mean insecure by definition, and a physical cable does not prevent every attack.

In a star topology, devices connect to a central component. A single endpoint cable failure need not disconnect everyone, but failure of the central switch can disrupt many clients. In a bus model, devices share a backbone; in a ring, connections form a loop. Treat textbook topology diagrams as models: real networks can combine structures and redundant paths. Draw devices and links clearly and explain the actual failure consequence shown.

## Security goals and controls

Confidentiality limits access to information; integrity protects against unauthorised alteration; availability means services are usable when needed. A public timetable may prioritise accuracy and availability; a private health record also has strong confidentiality needs. Identify the asset and threat before choosing a control.

Phishing tricks a person into revealing information or taking an unsafe action. Verify unexpected requests using a known independent channel. Malware is malicious software; ransomware can deny access by encrypting data. Updates repair known software weaknesses; anti-malware tools can detect some threats but are not complete protection. A firewall filters traffic according to rules. Backups and tested restoration reduce the consequences of data loss; they do not prevent every infection.

Use long unique passwords and an approved password manager where available. Multi-factor authentication combines factors of different kinds, such as knowledge and possession; two passwords are not two independent factor types. Authentication checks identity; authorisation controls permitted actions. Least privilege gives users only the access their role needs. Removing a former account's access is as important as initially creating it.

Encryption converts readable data into a protected form using keys; decryption recovers it with the appropriate key. Hashing produces a fixed-size digest and is not intended to be reversed. Password systems should use suitable password-hashing methods with salts; do not design a real credential system from a classroom toy hash. Never practise by collecting classmates' real passwords. Use invented examples only.

## Worked threat-control explanation

A school club stores fictional membership data in our lab. If all members share an administrator account, accidental edits and unauthorised access are difficult to attribute. Separate accounts and role-based permissions reduce exposure. A backup allows recovery after a mistaken deletion; it does not determine who was authorised to delete. Encryption in transit reduces interception risk; it does not stop an authorised user from copying a visible record. Each control addresses a different failure mode.

For an exam response, name the measure, explain its mechanism and connect it to the scenario. “Use security” is too vague. “Restrict editing to the organiser's role, so ordinary members cannot alter everyone else's registrations” is an assessable explanation. Include a limitation when asked to evaluate, and avoid promises of perfect protection.

## The four-layer TCP/IP model — Higher Level extension

A common teaching model groups the internet protocol suite into four layers. Some resources split the bottom layer further; use the model requested in a question and keep each function clear.

| Layer | Role | Example |
|---|---|---|
| Application | Rules for an application service and its messages | HTTP for web requests; DNS for names |
| Transport | Communication between application endpoints, including reliability where provided | TCP; UDP |
| Internet | Logical addressing and routing packets between networks | IP |
| Network access/link | Delivery across the local link and access to the physical medium | Ethernet or Wi-Fi |

On sending, each layer adds information needed for its role; the receiver interprets and removes the corresponding information. In a page download, HTTP describes what resource is requested, TCP maintains the ordered byte stream, IP addresses/routes packets, and the link technology carries them over each local hop. A router need not understand the meaning of the requested article to forward its packets.

Practice: place a web request, a TCP port, an IP destination and an Ethernet frame in the model. Answers: application, transport, internet, network access. Explain why “DNS is the transport layer” is incorrect: DNS provides a naming service and uses transport protocols to carry its messages.

## Cloud services and local storage

Cloud computing supplies computing resources or services over a network, often from infrastructure managed by a provider. Cloud storage can support access from different devices, collaboration and off-site copies. It creates dependencies on connectivity, the provider's availability, account security and the applicable data arrangements. Synchronisation is not automatically a backup: an accidental deletion can propagate to every synchronised device unless version history or independent recovery is available.

A school deciding between local and cloud storage should compare access needs, permissions, recurring costs, recovery, retention and environmental impact. Remote servers still consume electricity, cooling and materials; moving a file to the cloud does not remove its physical footprint. Central infrastructure may improve utilisation, but the outcome depends on actual use and energy sources. A justified answer presents a concrete benefit and a related limitation instead of saying “the cloud is always cheaper” or “local is always safer”.
