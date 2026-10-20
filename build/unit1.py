from lib import *

BLS = "https://www.bls.gov/ooh/computer-and-information-technology/home.htm"
BLS_ISA = "https://www.bls.gov/ooh/computer-and-information-technology/information-security-analysts.htm"
CYB_HEAT = "https://www.cyberseek.org/heatmap.html"
CYB_PATH = "https://www.cyberseek.org/pathway.html"
NICE = "https://www.nist.gov/itl/applied-cybersecurity/nice/nice-framework-resource-center"
NICE_CUR = "https://www.nist.gov/itl/applied-cybersecurity/nice/nice-framework-resource-center/nice-framework-current-versions"
NICCS_NICE = "https://niccs.cisa.gov/tools/nice-framework"

SURVEY_CATS = [
    {"id": "sup", "label": "Tech support and help desk", "desc": "You like solving people’s problems quickly and explaining tech in plain language. Start with Week 5 and the CompTIA A+ pathway."},
    {"id": "net", "label": "Networking and infrastructure", "desc": "You like figuring out how things connect and keeping systems running. Week 6 covers network admin and engineer roles."},
    {"id": "soc", "label": "Security operations (SOC)", "desc": "You enjoy spotting patterns, investigating, and staying calm when something goes wrong. Week 7 covers SOC analyst tiers."},
    {"id": "off", "label": "Ethical hacking and testing", "desc": "You like taking things apart to see how they break, with permission. Week 7 covers what penetration testing really looks like."},
    {"id": "grc", "label": "Governance, risk, and compliance (GRC)", "desc": "You like rules, writing, and connecting technology to business decisions. GRC is one of the most accessible security pathways (Week 7)."},
    {"id": "cld", "label": "Cloud and automation", "desc": "You like building things, scripting, and working with new platforms. Week 8 covers cloud engineering and DevSecOps."},
]
SURVEY_ITEMS = [
    {"t": "Friends and family ask me for help when their phone or laptop acts up, and I usually figure it out.", "c": ["sup"]},
    {"t": "I’m patient explaining something technical to someone who is frustrated.", "c": ["sup", "grc"]},
    {"t": "I wonder how Wi-Fi, streaming, and the internet actually get data from one place to another.", "c": ["net"]},
    {"t": "I like setting things up so they keep working without me: a home network, a smart home, a game server.", "c": ["net", "cld"]},
    {"t": "I enjoy puzzles where I have to find the one clue that doesn’t fit.", "c": ["soc", "off"]},
    {"t": "I stay calm and methodical when something is going wrong.", "c": ["soc", "sup"]},
    {"t": "I’m curious how hackers break into systems and how you would stop them.", "c": ["off", "soc"]},
    {"t": "I like reading the fine print: policies, rules, terms of service.", "c": ["grc"]},
    {"t": "I’m comfortable writing reports or explaining risks to people who are not technical.", "c": ["grc"]},
    {"t": "I like learning new apps and platforms as soon as they come out.", "c": ["cld"]},
    {"t": "I would enjoy writing small scripts or automations to save myself time.", "c": ["cld", "off"]},
    {"t": "I like a job where every day brings different people and problems.", "c": ["sup", "soc"]},
]

W1 = dict(n=1, unit=1, title="Orientation: the career landscape",
    lede="What do people in IT, networking, and cybersecurity actually do all day, and how many of those jobs are out there? This week you get the big picture and a map for the rest of the course.",
    due=[],
    objectives=[("Describe in your own words what IT, networking, and cybersecurity professionals do.", 1),
                ("Read basic workforce data from CyberSeek and the Bureau of Labor Statistics.", 4),
                ("Explain what the NICE Framework is and why employers and schools use it.", 1)],
    explore=f"""<div class="prose">
<h3>Three overlapping fields</h3>
<p><span class="term">Information technology (IT)</span> keeps people and organizations working: laptops, accounts, printers, software, phones, and the help desk that answers when they break. <span class="term">Networking</span> is the plumbing that connects all of it: the switches, routers, Wi-Fi, and cloud links that move data. <span class="term">Cybersecurity</span> protects all of it: the people, the devices, the data, and the network.</p>
<p>In real jobs these blur together. A help desk technician resets passwords (IT), troubleshoots Wi-Fi (networking), and reports a suspicious email (security) before lunch. That overlap is good news: skills you build in one area carry into the others.</p>
<h3>How big is the job market?</h3>
<p>Two free tools give you real numbers instead of hype.</p>
</div>
{stats([("514,359", "U.S. cybersecurity job listings in one 12-month period, up about 12% (CyberSeek, June 2025 release)"),
        ("29%", "projected growth for information security analysts, 2024–34, much faster than average (BLS)"),
        ("$124,910", "median pay for information security analysts, May 2024 (BLS)"),
        ("$105,990", "median pay across all computer and IT occupations, May 2024 (BLS)")])}
<p class="source">Sources: {ext("https://www.nist.gov/node/1883016", "NIST on the 2025 CyberSeek update")}, {ext(BLS_ISA, "BLS Occupational Outlook Handbook")}. A median means half of workers earn more and half earn less. It is not a starting salary.</p>
<div class="prose">
<p><span class="term">CyberSeek</span> counts real job postings, state by state, and maps career pathways. The <span class="term">BLS Occupational Outlook Handbook</span> reports pay, required education, and 10-year projections for each occupation. You will use both all semester.</p>
<h3>A shared language: the NICE Framework</h3>
<p>Job titles are messy. One company’s “security analyst” is another’s “SOC engineer.” The <span class="term">NICE Workforce Framework for Cybersecurity</span>, published by NIST, solves this by describing <em>work roles</em>: groupings of tasks, knowledge, and skills. One job can include several work roles, and two people with the same title may do very different work.</p>
<p>As of NICE Framework Components v2.2.0 (released April 2026), the framework organizes 42 work roles into five categories:</p>
</div>
{roles([("Oversight and Governance", "<p>Policy, risk, compliance, legal, training, leadership. Where most GRC jobs live.</p>"),
        ("Design and Development", "<p>Architecting and building secure systems and software.</p>"),
        ("Implementation and Operation", "<p>Running systems day to day: technical support, network operations, systems administration.</p>"),
        ("Protection and Defense", "<p>Detecting and responding to attacks: defensive cybersecurity, incident response, vulnerability analysis.</p>"),
        ("Investigation", "<p>Cybercrime investigation and digital evidence analysis.</p>")])}
{callout("Heads-up about older sources", "<p>Videos and articles from before 2024 describe seven NICE categories with names like “Securely Provision,” “Protect and Defend,” and “Analyze.” Those names were retired. If a source uses them, translate to the five current categories above.</p>", note=True)}
<div class="prose">
<h3>Where Brookdale fits</h3>
<p>Brookdale’s Network and Information Technology (NETW) courses lead to the NTIT A.A.S. degree and a Cybersecurity certificate. This course is the front door: by Week 15 you will know which roles interest you, which NETW course to take next, and which certifications to aim for. Week 9 walks through the full sequence.</p>
</div>""",
    do=[f"""<section class="act" aria-labelledby="w01-kwl-h"><span class="act-tag">Activity</span><h3 id="w01-kwl-h">KWL chart: what you know, want to know, and will learn</h3>
<p class="act-intro">Fill in the first two columns now. You will come back in Week 15 to finish the last one, so be honest about where you are starting.</p>
<div class="kwl">{field("w01-kwl-k", "K: What I already know about IT and cyber careers", rows=6)}{field("w01-kwl-w", "W: What I want to find out this semester", rows=6)}{field("w01-kwl-l", "L: What I learned (finish in Week 15)", rows=6)}</div></section>""",
        f"""<section class="act" aria-labelledby="w01-daily-h"><span class="act-tag">Discussion</span><h3 id="w01-daily-h">Tech in your daily life</h3>
<p class="act-intro">Think about everything you did today before class. Somebody in IT, networking, or security made each step work.</p>
{field("w01-daily", "List three things you used today that depend on a network or an IT team, and guess who keeps each one running.", rows=4)}</section>""",
        act("survey", "w01-survey", "Career interest survey",
            "Rate each statement. There are no right answers. Your results point you toward the weeks and roles worth a closer look, and they appear in your portfolio.",
            {"cats": SURVEY_CATS, "items": SURVEY_ITEMS}),
    ],
    investigate=dict(tag="In-class research", title="CyberSeek first look", short="research",
        intro="<p>You will use CyberSeek all semester. Today, learn your way around and collect a few real numbers for New Jersey.</p>",
        resources=[("CyberSeek heat map", CYB_HEAT, "Job postings and supply of workers by state and metro area."),
                   ("CyberSeek career pathway", CYB_PATH, "Feeder, entry, mid, and advanced roles with salaries, certs, and skills."),
                   ("BLS Occupational Outlook Handbook: Computer and IT", BLS, "Pay, education, and outlook for every major IT occupation."),
                   ("NICE Framework Resource Center (NIST)", NICE, "The official home of the framework."),
                   ("Simply Cyber on YouTube", "https://www.youtube.com/@SimplyCyber", "Career guidance from a working practitioner. Search the channel for “what is cybersecurity.”")],
        steps=["Open the CyberSeek heat map and select New Jersey.",
               "Record the number of cybersecurity job postings and the top job titles listed.",
               "Find the supply and demand ratio and write what it means in your own words.",
               "Open the career pathway tool and click one role that looks interesting. Note its average salary and the top skill listed."],
        fields=(field("w01-cs-postings", "New Jersey cybersecurity job postings (number and time period)", kind="text") +
                field("w01-cs-titles", "Top job titles in New Jersey", rows=3) +
                field("w01-cs-ratio", "The supply and demand ratio, and what it tells you", rows=3) +
                field("w01-cs-role", "One role from the pathway tool: its salary and top skill, and why you clicked it", rows=3)),
        submit=False),
    instructor=[("0–8 min", "Welcome, course overview, how this site saves work and makes PDFs."),
                ("8–15", "Tech in your daily life, pair share."),
                ("15–25", "Explore: three fields, labor data, NICE five categories (project the stat cards)."),
                ("25–35", "CyberSeek first look, live demo then students repeat."),
                ("35–45", "Career interest survey and KWL chart."),
                ("45–50", "Exit ticket. Preview Week 2 and the bio draft.")],
)

W2 = dict(n=2, unit=1, title="The IT career family",
    lede="Help desk, network admin, SOC analyst, cloud engineer, GRC analyst: meet the main role families, see how careers grow from entry level to senior, and look at what they pay.",
    due=["Portfolio §1 bio draft started"],
    objectives=[("Name the major IT role families and describe a typical day in four of them.", 1),
                ("Distinguish entry-level, mid-career, and senior roles.", 1),
                ("Compare pay and outlook for IT occupations using BLS data.", 4),
                ("Identify transferable skills you already have.", 6)],
    explore=f"""<div class="prose"><h3>Six role families</h3>
<p>Most IT and cyber jobs fall into one of these families. Many people move between them over a career.</p></div>
{roles([("Support", "<p><b>Help desk, desktop support, IT technician.</b> First responders for people with tech problems. The most common entry point into the whole field.</p>"),
        ("Networking", "<p><b>Network technician, network admin, network engineer.</b> Build and run the connections between devices, buildings, and clouds.</p>"),
        ("Security operations", "<p><b>SOC analyst, incident responder, threat hunter.</b> Watch for attacks and respond when they happen.</p>"),
        ("Cloud and systems", "<p><b>Systems admin, cloud engineer, DevOps engineer.</b> Run servers and cloud platforms, often by writing code to automate them.</p>"),
        ("Governance, risk, and compliance", "<p><b>GRC analyst, IT auditor, compliance specialist.</b> Make sure the organization follows rules and manages risk.</p>"),
        ("Management", "<p><b>IT manager, security manager, CISO.</b> Lead teams, budgets, and strategy. Usually reached after years in another family.</p>")])}
<div class="prose"><h3>A day in the life</h3></div>
<details class="more"><summary>Help desk technician</summary><p>Starts the shift by checking the ticket queue. Resets a locked account, walks someone through connecting to the VPN, replaces a failing laptop battery, and escalates a server problem to the systems team. Spends a lot of the day talking to people, so communication matters as much as technical skill.</p></details>
<details class="more"><summary>Network administrator</summary><p>Reviews overnight alerts on network devices, adds a new switch for an office expansion, adjusts Wi-Fi coverage in a conference room, and plans a firmware update for the weekend maintenance window.</p></details>
<details class="more"><summary>SOC analyst (Tier 1)</summary><p>Works a queue of security alerts. Decides which are false alarms, which need more digging, and which to escalate. Documents everything. Many SOCs run 24/7, so shifts can include nights or weekends early in a career.</p></details>
<details class="more"><summary>Cloud engineer</summary><p>Writes templates that build cloud servers automatically, tunes costs, fixes a broken deployment, and meets with developers about a new application. Usually reached after support or systems experience.</p></details>
<div class="prose"><h3>Entry, mid, senior</h3>
<p>Careers usually grow in stages. <b>Entry-level</b> roles (0–2 years) follow procedures and escalate hard problems. <b>Mid-career</b> roles (3–7 years) own systems and solve the hard problems. <b>Senior</b> roles design, lead, and set direction. CyberSeek calls the roles that lead into cybersecurity <em>feeder roles</em>, and help desk and network jobs are the biggest feeders.</p>
<h3>What does the data say about pay?</h3>
<p>The chart below starts with four occupations from the BLS Occupational Outlook Handbook. In the Investigate section you will add your own.</p></div>""",
    do=[act("sort", "w02-match", "Role matching: which job is this?",
            "Each card is a line from a real-style job description. Sort it into the role family it best describes.",
            {"buckets": [{"id": "sup", "label": "Support"}, {"id": "net", "label": "Networking"}, {"id": "soc", "label": "Security operations"},
                         {"id": "cld", "label": "Cloud and systems"}, {"id": "grc", "label": "GRC"}],
             "items": [{"t": "Respond to employee tickets by phone, chat, and email", "b": "sup"},
                       {"t": "Image and deploy new laptops for incoming staff", "b": "sup"},
                       {"t": "Configure VLANs and routing on switches across three campuses", "b": "net", "why": "VLANs and routing are core network configuration tasks."},
                       {"t": "Troubleshoot Wi-Fi dead zones and access point coverage", "b": "net"},
                       {"t": "Triage alerts from the SIEM and escalate confirmed incidents", "b": "soc", "why": "A SIEM collects security alerts. Triage and escalation is SOC Tier 1 work."},
                       {"t": "Analyze suspicious emails reported by employees", "b": "soc"},
                       {"t": "Automate server builds with infrastructure-as-code templates", "b": "cld", "why": "Infrastructure as code is a cloud and DevOps skill."},
                       {"t": "Monitor cloud spending and right-size virtual machines", "b": "cld"},
                       {"t": "Map company controls to PCI DSS requirements before the audit", "b": "grc", "why": "Mapping controls to a standard is compliance work."},
                       {"t": "Update the acceptable use policy and run annual training", "b": "grc"}],
             "done": "All sorted correctly. Notice how many entry-level tasks involve people, not just machines."}),
        act("compare", "w02-pay", "Pay and outlook compare",
            "Four BLS occupations are preloaded. Read the bars, then add one or two occupations you look up yourself.",
            {"rows": [{"name": "Computer support specialists", "pay": 61550, "growth": -3},
                      {"name": "Network and computer systems administrators", "pay": 96800, "growth": -4},
                      {"name": "Information security analysts", "pay": 124910, "growth": 29},
                      {"name": "Computer network architects", "pay": 130390, "growth": 12}],
             "growthLabel": "Projected employment change, 2024–34",
             "note": "Preloaded data: BLS Occupational Outlook Handbook, May 2024 median pay and 2024–34 projections. A projected decline does not mean no jobs: BLS still expects tens of thousands of openings each year in support roles as people retire or move up."}),
        f"""<section class="act" aria-labelledby="w02-skills-h"><span class="act-tag">Activity</span><h3 id="w02-skills-h">Transferable skills you already have</h3>
<p class="act-intro">Check every skill you have used in a job, class, team, family, or hobby. Employers hiring for entry-level IT ask about these constantly.</p>
{checks("Transferable skills I have", [("w02-sk-cust", "Customer service: calming someone down and solving their problem"), ("w02-sk-doc", "Writing clear instructions or notes someone else could follow"), ("w02-sk-trouble", "Troubleshooting: fixing something by testing one thing at a time"), ("w02-sk-team", "Working on a team with a deadline"), ("w02-sk-detail", "Careful attention to detail: inventory, cash, data entry, lab work"), ("w02-sk-learn", "Teaching myself something from videos or manuals"), ("w02-sk-pressure", "Staying calm under pressure: retail rush, emergency, military, healthcare"), ("w02-sk-bilingual", "Speaking more than one language")])}
{field("w02-sk-story", "Pick one checked skill and describe a moment you used it. This becomes material for your bio and resume.", rows=4)}</section>""",
        f"""<section class="act" aria-labelledby="w02-group-h"><span class="act-tag">Group discussion</span><h3 id="w02-group-h">Which role appeals to you, and why?</h3>
{field("w02-appeal", "The role family that appeals to me most right now, and the reason", rows=4)}</section>"""],
    investigate=dict(tag="In-class research", title="Look up two occupations", short="research",
        intro="<p>Use the BLS handbook to add two occupations to the chart above, then try a live LinkedIn search to see what employers ask for.</p>",
        resources=[("BLS Occupational Outlook Handbook: Computer and IT", BLS, "Pick any occupation and open its Pay and Job Outlook tabs."),
                   ("CyberSeek career pathway: role profiles", CYB_PATH, "Click a role to see salary, certifications, and top skills."),
                   ("LinkedIn Jobs", "https://www.linkedin.com/jobs/", "Search “help desk” or “IT support” with location New Jersey."),
                   ("NetworkChuck on YouTube", "https://www.youtube.com/@NetworkChuck", "Search the channel for his IT career roadmap videos.")],
        steps=["Pick two occupations from the BLS Computer and IT list that are not already in the chart.",
               "For each, add the median pay and the projected growth to the chart above, with “BLS OOH” as the source.",
               "Search LinkedIn Jobs for one entry-level title in New Jersey and count the results.",
               "Answer the questions below."],
        fields=(field("w02-inv-bls", "What surprised you about the BLS numbers? Which occupation has the best combination of pay and outlook for someone starting out?", rows=4) +
                field("w02-inv-li", "Your LinkedIn search: the title, how many results, and two requirements you saw in more than one posting", rows=4)),
        submit=False),
    portfolio=f"""<p class="prose">Start Portfolio §1, your professional bio. It does not need to be polished. Write a first draft of about 150 words now; you will expand it to about one page by Week 13.</p>
{field("pf-bio", "Portfolio §1: Professional bio (draft)", help="Who you are, what you have done (work, school, military, family, hobbies), the skills you bring, and what draws you to IT. First person is fine.", rows=10, words="250-450")}""",
    instructor=[("0–5 min", "Recap Week 1 survey results: quick hands-up by strongest match."),
                ("5–18", "Explore: role families and day-in-the-life panels. Show the pay chart."),
                ("18–28", "Role matching sort in pairs. Review two misses as a class."),
                ("28–38", "Live LinkedIn job search demo, then students add two BLS occupations."),
                ("38–46", "Transferable skills checklist and the bio draft start."),
                ("46–50", "Exit ticket.")],
)

W3 = dict(n=3, unit=1, title="How networks work",
    lede="Every IT role touches the network. Follow a single Google search from your laptop to a data center and back, and meet the devices that make it happen.",
    due=[],
    objectives=[("Explain LANs, WANs, and the internet at a conceptual level.", 2),
                ("Describe what routers, switches, firewalls, and access points do.", 2),
                ("Explain IP addresses and DNS in plain language.", 2),
                ("Connect networking knowledge to your target role.", 1)],
    explore=f"""<div class="prose"><h3>Networks inside networks</h3>
<p>A <span class="term">LAN</span> (local area network) connects devices in one place: your home, a classroom, an office. A <span class="term">WAN</span> (wide area network) connects LANs across distances: a company’s offices in Lincroft and Freehold. The <span class="term">internet</span> is a network of networks, owned by thousands of companies that agree to pass each other’s traffic.</p>
<h3>The devices</h3></div>
{roles([("Switch", "<p>Connects devices inside a LAN and sends each message only to the device it is meant for.</p>"),
        ("Router", "<p>Connects different networks and picks the path traffic takes between them. Your home router connects your LAN to your internet provider.</p>"),
        ("Firewall", "<p>Allows or blocks traffic based on rules. Sits at the edge of a network like a security checkpoint.</p>"),
        ("Wireless access point", "<p>Lets Wi-Fi devices join the LAN. Home routers usually have one built in.</p>")])}
<div class="prose"><h3>Addresses and names</h3>
<p>Every device on a network has an <span class="term">IP address</span>, like a mailing address, such as <code>142.250.80.46</code>. People are bad at remembering numbers, so <span class="term">DNS</span> (the Domain Name System) works like a contact list: you type <code>google.com</code> and DNS looks up the IP address for you.</p>
<p>Most devices also get their address automatically from <span class="term">DHCP</span> when they join a network. That is why your phone just works when you join campus Wi-Fi.</p>
<h3>The shift to the cloud</h3>
<p><span class="term">On-premises</span> means the organization owns the servers in its own building. <span class="term">Cloud</span> means renting computing from a provider like Microsoft Azure, Amazon Web Services, or Google Cloud. Most organizations now run a mix. The network still matters, because everything in the cloud is reached over a network. Network skills are moving toward cloud networking, not disappearing.</p></div>
{callout("Why this matters for every role", "<p>The help desk troubleshoots Wi-Fi. The SOC analyst reads network traffic to spot attacks. The GRC analyst asks whether the firewall rules match policy. The cloud engineer builds virtual networks. Networking is the common language.</p>")}""",
    do=[act("diagram", "w03-trace", "Trace the path of a Google search",
            "Step through what happens in the second after you press Enter. Watch which device is doing the work at each step.",
            {"w": 780, "h": 300, "alt": "Diagram: laptop, Wi-Fi access point, home router, internet provider, DNS server, and Google data center, connected in a path.",
             "nodes": [{"id": "pc", "label": "Your laptop", "sub": "192.168.1.20", "x": 80, "y": 150},
                       {"id": "ap", "label": "Wi-Fi + router", "sub": "home gateway", "x": 240, "y": 150},
                       {"id": "fw", "label": "Firewall / NAT", "sub": "inside the router", "x": 240, "y": 255, "w": 140},
                       {"id": "isp", "label": "Internet provider", "sub": "ISP network", "x": 420, "y": 150, "w": 140},
                       {"id": "dns", "label": "DNS resolver", "sub": "looks up names", "x": 420, "y": 45, "w": 140},
                       {"id": "net", "label": "Internet routers", "sub": "many hops", "x": 580, "y": 150, "w": 130},
                       {"id": "goo", "label": "Google", "sub": "data center", "x": 715, "y": 150, "w": 110}],
             "links": [["pc", "ap"], ["ap", "fw"], ["ap", "isp"], ["isp", "dns"], ["isp", "net"], ["net", "goo"]],
             "steps": [{"on": ["pc"], "title": "You press Enter", "text": "Your browser needs to reach google.com, but computers route by IP address, not by name. First it needs the address."},
                       {"on": ["pc", "ap"], "links": [0], "title": "Over Wi-Fi to your router", "text": "Your laptop sends a request over Wi-Fi to the access point and router. The router is your laptop’s gateway out of your LAN."},
                       {"on": ["ap", "isp", "dns"], "links": [2, 3], "title": "DNS finds the address", "text": "The router forwards a DNS question through your internet provider to a DNS resolver: what is the IP address for google.com? The answer comes back in milliseconds."},
                       {"on": ["ap", "fw"], "links": [1], "title": "The router translates your address", "text": "Your laptop’s address (192.168.1.20) is private and only works at home. Network address translation (NAT) swaps it for your home’s public address. The firewall tracks the conversation so the reply is allowed back in."},
                       {"on": ["isp", "net"], "links": [4], "title": "Across the internet", "text": "Routers owned by different companies pass your request hop by hop, each one choosing the next best path toward Google’s network."},
                       {"on": ["net", "goo"], "links": [5], "title": "Google answers", "text": "A Google server receives the encrypted request (HTTPS) and sends back the search results page."},
                       {"on": ["pc", "ap", "isp", "net", "goo"], "links": [0, 2, 4, 5], "title": "And back again", "text": "The reply retraces the path. The whole round trip usually takes well under a second. Every step is a place where something can break, and a place where an IT professional works."}]}),
        act("sort", "w03-devices", "Network device card sort",
            "Which device is doing the job described on each card?",
            {"buckets": [{"id": "sw", "label": "Switch"}, {"id": "rt", "label": "Router"}, {"id": "fw", "label": "Firewall"}, {"id": "ap", "label": "Access point"}, {"id": "dns", "label": "DNS server"}],
             "items": [{"t": "Connects 48 desktops in the library to the same LAN", "b": "sw"},
                       {"t": "Sends a frame only to the port where the destination device is plugged in", "b": "sw"},
                       {"t": "Picks the path between the campus network and the internet provider", "b": "rt"},
                       {"t": "Connects the Lincroft and Freehold office networks together", "b": "rt", "why": "Connecting separate networks is a router’s job."},
                       {"t": "Blocks incoming traffic that does not match an allowed rule", "b": "fw"},
                       {"t": "Stops a computer from reaching a known malicious website", "b": "fw"},
                       {"t": "Lets students’ phones join the network without a cable", "b": "ap"},
                       {"t": "Turns brookdalecc.edu into an IP address", "b": "dns"}],
             "done": "All correct. You can now name the four devices you will see in nearly every job posting."}),
        f"""<section class="act" aria-labelledby="w03-refl-h"><span class="act-tag">Reflection</span><h3 id="w03-refl-h">How does networking connect to your target role?</h3>
{field("w03-refl", "Pick the role family you are leaning toward. Describe one way someone in that role uses networking knowledge.", rows=4)}</section>"""],
    investigate=dict(tag="In-class research", title="Networking basics, from the source", short="research",
        intro="<p>Pick one free resource below and use it to answer three questions. If you are on a Windows computer, try the optional command at the end.</p>",
        resources=[("Cisco Networking Academy: Networking Basics", "https://www.netacad.com/courses/networking-basics", "Free self-paced course. Module 1 is enough for today."),
                   ("Cloudflare Learning Center: What is DNS?", "https://www.cloudflare.com/learning/dns/what-is-dns/", "A short, clear explainer with diagrams."),
                   ("Professor Messer", "https://www.professormesser.com/", "Free video courses. Search for his OSI model video in the Network+ course."),
                   ("NetworkChuck on YouTube", "https://www.youtube.com/@NetworkChuck", "Search the channel for “what is networking.”")],
        steps=["Choose one resource and spend about 10 minutes with it.",
               "Answer the three questions below in your own words.",
               "Optional: on Windows, open Command Prompt and type <code>nslookup brookdalecc.edu</code>. Record the address you get back."],
        fields=(field("w03-q1", "In your own words, what is the difference between a switch and a router?", rows=3) +
                field("w03-q2", "What would happen if DNS stopped working at your school?", rows=3) +
                field("w03-q3", "Which resource did you use, and one thing from it that was new to you", rows=3) +
                field("w03-nslookup", "Optional: the result of nslookup brookdalecc.edu", kind="text")),
        submit=False),
    instructor=[("0–5 min", "Poll: what happens when you type a web address?"),
                ("5–17", "Explore: LAN, WAN, devices, IP and DNS, cloud."),
                ("17–27", "Trace the Google search stepper, projected, with students predicting each step."),
                ("27–35", "Device card sort, individually."),
                ("35–46", "Investigate: one resource plus optional nslookup."),
                ("46–50", "Reflection and exit ticket.")],
)

QUIZ1 = [
    {"q": "Which tool counts real cybersecurity job postings by state?", "options": [{"t": "CyberSeek", "ok": True}, {"t": "The NICE Framework"}, {"t": "Professor Messer"}, {"t": "TryHackMe"}], "explain": "CyberSeek is built from job posting data and shows postings by state and metro area."},
    {"q": "The NICE Framework describes cybersecurity work using…", "options": [{"t": "Work roles made of tasks, knowledge, and skills", "ok": True}, {"t": "A list of company job titles"}, {"t": "Salary ranges by state"}, {"t": "A ranking of certifications"}], "explain": "Work roles are not job titles. One job can include several work roles."},
    {"q": "How many work role categories are in the current NICE Framework?", "options": [{"t": "Five", "ok": True}, {"t": "Three"}, {"t": "Seven"}, {"t": "Twelve"}], "explain": "Five: Oversight and Governance, Design and Development, Implementation and Operation, Protection and Defense, Investigation. The old version had seven."},
    {"q": "A median salary of $96,800 means…", "options": [{"t": "Half of workers earn more and half earn less", "ok": True}, {"t": "Most new hires start at $96,800"}, {"t": "Nobody earns less than $96,800"}, {"t": "It is the average of the highest and lowest salaries"}], "explain": "The median is the middle value. Entry-level pay is usually lower."},
    {"q": "Which NICE category includes Technical Support and Systems Administration?", "options": [{"t": "Implementation and Operation", "ok": True}, {"t": "Protection and Defense"}, {"t": "Oversight and Governance"}, {"t": "Investigation"}], "explain": "Running systems day to day is Implementation and Operation."},
    {"q": "CyberSeek calls roles that lead into cybersecurity, such as help desk and networking jobs…", "options": [{"t": "Feeder roles", "ok": True}, {"t": "Shadow roles"}, {"t": "Tier 3 roles"}, {"t": "Legacy roles"}], "explain": "Feeder roles build the foundation many security professionals start from."},
    {"q": "Which role family is the most common entry point into IT?", "options": [{"t": "Support and help desk", "ok": True}, {"t": "Management"}, {"t": "Cloud architecture"}, {"t": "Penetration testing"}], "explain": "Help desk and support jobs are the largest group of entry-level IT roles."},
    {"q": "Mapping company controls to PCI DSS requirements is typical work for…", "options": [{"t": "A GRC analyst", "ok": True}, {"t": "A help desk technician"}, {"t": "A network technician"}, {"t": "A cloud cost analyst"}], "explain": "Compliance mapping is governance, risk, and compliance work."},
    {"q": "Which device connects different networks and chooses paths between them?", "options": [{"t": "Router", "ok": True}, {"t": "Switch"}, {"t": "Access point"}, {"t": "Printer"}], "explain": "Routers connect networks. Switches connect devices within one network."},
    {"q": "What does DNS do?", "options": [{"t": "Translates names like google.com into IP addresses", "ok": True}, {"t": "Encrypts your web traffic"}, {"t": "Blocks malicious websites"}, {"t": "Assigns Wi-Fi passwords"}], "explain": "DNS works like a contact list for the internet."},
    {"q": "A LAN is…", "options": [{"t": "A network in one location, like a home or office", "ok": True}, {"t": "The whole internet"}, {"t": "A network that connects cities"}, {"t": "A type of firewall"}], "explain": "LAN stands for local area network."},
    {"q": "Which device allows or blocks traffic based on rules?", "options": [{"t": "Firewall", "ok": True}, {"t": "Switch"}, {"t": "DNS server"}, {"t": "Access point"}], "explain": "Firewalls enforce rules at the edge of a network."},
    {"q": "What usually gives your phone an IP address when it joins campus Wi-Fi?", "options": [{"t": "DHCP", "ok": True}, {"t": "DNS"}, {"t": "HTTPS"}, {"t": "The firewall"}], "explain": "DHCP hands out addresses automatically."},
    {"q": "Why does networking still matter as organizations move to the cloud?", "options": [{"t": "Cloud resources are reached over networks, and cloud platforms have their own virtual networks", "ok": True}, {"t": "It doesn’t. Cloud removes the need for networks"}, {"t": "Only because of old printers"}, {"t": "Because cloud providers ban Wi-Fi"}], "explain": "Network skills are shifting toward cloud networking."},
    {"q": "BLS projects employment of information security analysts to grow about how much from 2024 to 2034?", "options": [{"t": "29%", "ok": True}, {"t": "3%"}, {"t": "−4%"}, {"t": "100%"}], "explain": "29%, much faster than the average for all occupations."},
]

PHISH = [
    {"card": {"kind": "email", "head": [["From:", "Microsoft 365 Security <alerts@micros0ft-support.co>"], ["Subject:", "Action required: password expires in 2 hours"]],
              "body": "Your Brookdale mailbox password will expire today.\nTo keep access, verify your account now:\n[[https://micros0ft-support.co/verify]]\n\nFailure to verify will result in permanent account deletion."},
     "q": "Phishing or legitimate?", "options": [{"t": "Phishing", "ok": True}, {"t": "Legitimate"}],
     "explain": "Red flags: a zero instead of an o in the sender’s domain, a non-Microsoft link, an artificial deadline, and a threat of deletion. Report it, don’t click."},
    {"card": {"kind": "email", "head": [["From:", "Brookdale Bookstore <bookstore@brookdalecc.edu>"], ["Subject:", "Your order is ready for pickup"]],
              "body": "Hi Jordan,\nYour textbook order #48213 is ready at the Lincroft campus bookstore. Bring your student ID.\nHours are posted on the bookstore page of the college website."},
     "q": "Phishing or legitimate?", "options": [{"t": "Phishing"}, {"t": "Legitimate", "ok": True}],
     "explain": "It comes from the real college domain, asks for nothing, contains no link to click, and matches something you would expect. When unsure, go to the website yourself instead of clicking."},
    {"card": {"kind": "email", "head": [["From:", "Dr. Patel (via Gmail) <prof.patel.brookdale@gmail.com>"], ["Subject:", "Quick favor"]],
              "body": "Are you on campus? I need you to pick up four $100 gift cards for a student award. I’m in a meeting and can’t talk. Send me the codes and I’ll pay you back today."},
     "q": "Phishing or legitimate?", "options": [{"t": "Phishing", "ok": True}, {"t": "Legitimate"}],
     "explain": "Gift cards, urgency, “can’t talk,” and a personal Gmail address pretending to be a professor. This is a classic impersonation scam. Verify by calling or emailing the person at their real address."},
    {"card": {"kind": "email", "head": [["From:", "Package Delivery <tracking@ups-delivery-notice.info>"], ["Subject:", "Delivery failed: fee required"]],
              "body": "We attempted to deliver your package. A $1.99 redelivery fee is required.\nPay now: [[https://ups-delivery-notice.info/pay]]"},
     "q": "Phishing or legitimate?", "options": [{"t": "Phishing", "ok": True}, {"t": "Legitimate"}],
     "explain": "A small fee is bait to collect your card number. The domain is not ups.com. Check deliveries by typing the carrier’s site yourself."},
    {"card": {"kind": "email", "head": [["From:", "IT Help Desk <helpdesk@brookdalecc.edu>"], ["Subject:", "Scheduled maintenance Saturday 6–9 a.m."]],
              "body": "Canvas and email may be unavailable Saturday from 6 to 9 a.m. while we apply updates. No action is needed. Questions? Call the Help Desk at the number on the college website."},
     "q": "Phishing or legitimate?", "options": [{"t": "Phishing"}, {"t": "Legitimate", "ok": True}],
     "explain": "Real domain, no link, no request for credentials, and it tells you to use a number you can find yourself. Good IT notices look like this."},
]

W4 = dict(n=4, unit=1, title="Cybersecurity fundamentals and ethics",
    lede="The CIA triad, the threats you will hear about in every job, the defenses that stop them, and the ethical lines security professionals never cross.",
    due=["Reflection Journal 1", "Quiz 1 (open-note, Weeks 1–3)"],
    objectives=[("Explain confidentiality, integrity, and availability with examples.", 2),
                ("Recognize phishing, malware, ransomware, and social engineering.", 2),
                ("Describe common defenses such as MFA, firewalls, VPNs, and backups.", 2),
                ("Apply ethical reasoning to scenarios about authorization and privacy.", 5)],
    explore=f"""<div class="prose"><h3>The CIA triad</h3>
<p>Almost every security decision protects one of three things:</p></div>
{roles([("Confidentiality", "<p>Only the right people can see the data. Broken when grades leak or a password is stolen.</p>"),
        ("Integrity", "<p>Data is accurate and has not been tampered with. Broken when someone changes a bank transfer amount.</p>"),
        ("Availability", "<p>Systems and data are there when needed. Broken when ransomware locks a hospital’s records.</p>")])}
<div class="prose"><h3>Common threats</h3>
<p><span class="term">Phishing</span> tricks people into clicking a link, opening an attachment, or handing over a password, usually by email or text. <span class="term">Malware</span> is any malicious software. <span class="term">Ransomware</span> is malware that encrypts files and demands payment. <span class="term">Social engineering</span> manipulates people rather than technology: a fake phone call from “IT,” a stranger following you through a locked door.</p>
<p>Most successful attacks start with a person, not a clever exploit. That is why security awareness is part of every IT job.</p>
<h3>Common defenses</h3>
<p><span class="term">Multi-factor authentication (MFA)</span> requires something besides a password, such as a code or an app prompt, and blocks most account takeovers. <span class="term">Firewalls</span> filter traffic. A <span class="term">VPN</span> encrypts traffic between a device and a trusted network. <span class="term">Backups</span>, kept offline or separate, let an organization recover from ransomware without paying.</p>
<h3>Ethics: the line that defines the profession</h3>
<p>The tools a security professional uses to defend a network are often the same tools an attacker uses. What separates them is <b>authorization</b>: written permission from someone who owns the system. Testing a system you do not own without permission is illegal under laws such as the federal Computer Fraud and Abuse Act, even if you mean well.</p>
<p>Two more principles come up constantly. <b>Privacy</b>: IT staff can often see other people’s email and files, and professionals look only when the job requires it. <b>Responsible disclosure</b>: if you find a security flaw, you report it privately to the owner and give them time to fix it before telling anyone else.</p></div>""",
    do=[act("choices", "w04-phish", "Phishing inbox analysis",
            "Five messages landed in a student’s inbox. Decide which are phishing, then read the red flags.",
            {"items": PHISH, "label": "Message", "okLabel": "Right call.", "noLabel": "Look again."}),
        act("sort", "w04-cia", "CIA triad scenario mapping",
            "Which part of the CIA triad is most directly harmed in each scenario?",
            {"buckets": [{"id": "c", "label": "Confidentiality"}, {"id": "i", "label": "Integrity"}, {"id": "a", "label": "Availability"}],
             "items": [{"t": "A stolen laptop exposes 2,000 patient records", "b": "c"},
                       {"t": "An attacker changes the amount on a payroll file", "b": "i"},
                       {"t": "Ransomware locks every file at a school district", "b": "a", "why": "Ransomware is mainly an availability attack, though many groups also steal data."},
                       {"t": "A flood of fake traffic knocks the college website offline", "b": "a"},
                       {"t": "A coworker reads a manager’s email without permission", "b": "c"},
                       {"t": "A student edits their grade in the gradebook", "b": "i"},
                       {"t": "A cloud outage stops online class registration", "b": "a"},
                       {"t": "A shared folder of Social Security numbers is set to “anyone with the link”", "b": "c"}]}),
        act("choices", "w04-ethics", "Ethics dilemmas",
            "There is a best answer for each, but read the feedback for every option you consider. These situations really happen to new IT staff.",
            {"scored": False, "label": "Scenario", "okLabel": "Strong choice.", "noLabel": "Risky choice.",
             "items": [{"q": "You work at the help desk. While fixing a professor’s laptop, you notice a folder called “Student complaints.” You are curious.", "options": [{"t": "Leave it alone and finish the repair", "ok": True, "fb": "Access is for the job you were asked to do, nothing more."}, {"t": "Open it quickly. You won’t tell anyone.", "fb": "Looking without a work reason is a privacy violation and can cost you the job."}, {"t": "Copy it so the professor has a backup", "fb": "Copying someone’s data without being asked is still unauthorized access."}]},
                       {"q": "A classmate shows you how to scan the campus Wi-Fi for open devices “just to practice for Security+.”", "options": [{"t": "Decline and practice on TryHackMe or a lab you are allowed to use", "ok": True, "fb": "Practice happens in environments you are authorized to test."}, {"t": "It is fine because you are students", "fb": "Being a student is not authorization. Scanning a network you don’t own can violate policy and law."}, {"t": "Scan, but only for a minute", "fb": "There is no “a little” unauthorized scanning."}]},
                       {"q": "You discover a website for a local business leaks customer emails if you change a number in the address bar.", "options": [{"t": "Stop, write down what you saw, and report it privately to the business", "ok": True, "fb": "That is responsible disclosure. Don’t keep testing, and don’t download data."}, {"t": "Post about it online so they are forced to fix it", "fb": "Public disclosure before the owner can fix it puts customers at risk."}, {"t": "Download the list to prove the problem is real", "fb": "Taking the data turns a discovery into a breach."}]},
                       {"q": "Your manager asks you to quietly look through an employee’s email because “something seems off.”", "options": [{"t": "Ask for the request in writing and follow the company’s investigation policy, usually through HR or legal", "ok": True, "fb": "Legitimate investigations have a documented process and approvals."}, {"t": "Do it. Your manager is your boss.", "fb": "Doing it without the proper process exposes you, your manager, and the company."}, {"t": "Warn the employee", "fb": "Tipping someone off could interfere with a legitimate investigation. Follow policy instead."}]}]}),
        act("choices", "w04-quiz", "Practice Quiz 1: Weeks 1–3",
            "Fifteen open-note practice questions, the same style as the graded Quiz 1 in Canvas. Use your notes and the glossary.",
            {"items": QUIZ1, "shuffle": True}, tag="Practice quiz")],
    investigate=dict(tag="Reflection Journal 1", title="Test yourself, then reflect", short="journal",
        intro="<p>Take Google’s free phishing quiz, read CISA’s phishing guidance, and then write your first reflection journal.</p>",
        resources=[("Google Phishing Quiz (Jigsaw)", "https://phishingquiz.withgoogle.com/", "Eight realistic messages. Takes about 5 minutes."),
                   ("CISA: Recognize and report phishing", "https://www.cisa.gov/secure-our-world/recognize-and-report-phishing", "The U.S. government’s plain-language guide."),
                   ("CISA: Multifactor authentication", "https://www.cisa.gov/topics/cybersecurity-best-practices/multifactor-authentication", "Why MFA matters and how to turn it on."),
                   ("Professor Messer: Security+ course", "https://www.professormesser.com/", "Free videos. Browse the threats section.")],
        steps=["Take the Google Phishing Quiz and record your score.",
               "Read the CISA phishing page and note one tip you did not know.",
               "Write Reflection Journal 1 (250–350 words) using the prompt below.",
               "Save it as a PDF and upload it to Canvas."],
        fields=(field("w04-gq-score", "Google Phishing Quiz score (out of 8) and the red flag you missed most often", kind="text") +
                field("w04-cisa-tip", "One CISA tip that was new to you", rows=2) +
                field("w04-journal", "Reflection Journal 1",
                      help="Prompt: Before this course, what did you picture when you heard “cybersecurity”? What has changed after four weeks? Which ethical situation from this week would be hardest for you, and why? Which role family are you most curious about now?",
                      rows=12, words="250-350")),
        grade="Reflection journals are 15% of the course total across three entries. Write in your own words. AI tools may help you brainstorm or edit, and you must disclose any use.",
        submit=True),
    portfolio=f"""<p class="prose">Next week you begin Portfolio §2, two NICE work role analyses. Get a head start: browse the work roles and shortlist two or three.</p>
<ul class="res-list">{res("CISA NICCS: NICE Framework work roles", NICCS_NICE, "Searchable list of every work role with its tasks, knowledge, and skills.")}{res("NIST: NICE Framework current versions", NICE_CUR, "Download the official components spreadsheet.")}</ul>
{field("w04-pf-shortlist", "Two or three NICE work roles I might analyze, and why", rows=4)}""",
    instructor=[("0–5 min", "Show of hands: who has received a phishing text this month?"),
                ("5–15", "Explore: CIA triad, threats, defenses."),
                ("15–25", "Phishing inbox, then CIA mapping in pairs."),
                ("25–33", "Ethics dilemmas as a whole-class discussion. Ask for minority opinions."),
                ("33–48", "Quiz 1 in Canvas (open note). Students who finish early start Journal 1."),
                ("48–50", "Remind: Journal 1 due; Assignment 1 starts next week.")],
    instructor_note="The graded Quiz 1 lives in Canvas. The practice quiz on this page uses different wording so students can prepare without seeing the graded items.",
)

WEEKS = [W1, W2, W3, W4]
