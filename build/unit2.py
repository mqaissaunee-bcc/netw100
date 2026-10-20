from lib import *
from unit1 import NICCS_NICE, NICE_CUR, CYB_PATH, CYB_HEAT

def role_analysis(p, n):
    return (f'<h4>NICE work role analysis #{n}</h4>' +
            field(f"{p}-role", f"Role analysis #{n}: NICE work role name and ID", help="For example, the role name and its code such as IO-WRL-00x, copied from NICCS.", kind="text") +
            field(f"{p}-cat", f"Role analysis #{n}: work role category", kind="text") +
            field(f"{p}-tasks", f"Role analysis #{n}: three tasks from the role, in your own words", rows=4) +
            field(f"{p}-ks", f"Role analysis #{n}: three knowledge or skill statements you already partly have, and three you would need to build", rows=5) +
            field(f"{p}-match", f"Role analysis #{n}: how the job postings compare to the NICE role", help="What did the postings ask for that NICE also lists? What did they add or leave out?", rows=5) +
            field(f"{p}-fit", f"Role analysis #{n}: is this role a good fit for you? Why or why not?", rows=4))

W5 = dict(n=5, unit=2, title="Help desk and IT support",
    lede="Help desk is where most IT careers start. See what the job is really like, what CompTIA A+ covers, and how people grow from the help desk into systems and security roles.",
    due=["Career Role Research Assignment 1", "Portfolio §2: role analysis #1"],
    objectives=[("Describe a typical help desk day, its tools, and escalation tiers.", 1),
                ("Explain what CompTIA A+ covers, what it costs, and how long people study for it.", 3),
                ("Analyze real entry-level job postings against a NICE work role.", 1)],
    explore=f"""<div class="prose"><h3>Why help desk is the foundation</h3>
<p>Help desk technicians see every part of an organization’s technology: accounts, laptops, printers, software, phones, Wi-Fi, and the people using them. That breadth is why so many network admins, security analysts, and cloud engineers started here.</p></div>
{stats([("$61,550", "median pay, computer support specialists, May 2024"), ("$73,340", "median pay, computer network support specialists, May 2024"), ("−3%", "projected change in employment, 2024–34")])}
<p class="source">Source: {ext("https://www.bls.gov/ooh/computer-and-information-technology/computer-support-specialists.htm", "BLS Occupational Outlook Handbook: Computer Support Specialists")}. A small decline still leaves a large number of openings each year because so many people hold these jobs and move up or out.</p>
<div class="prose"><h3>Tiers and escalation</h3>
<p>Most support teams work in <span class="term">tiers</span>. <b>Tier 1</b> handles common requests: passwords, basic software, connecting devices. <b>Tier 2</b> takes harder problems that need deeper access or skill. <b>Tier 3</b> is usually the engineers who built the system. <span class="term">Escalation</span> means handing a ticket up a tier with clear notes about what you already tried.</p>
<h3>The tools</h3>
<p>A <span class="term">ticketing system</span> (such as ServiceNow, Jira Service Management, or Zendesk) tracks every request. <span class="term">Remote support</span> tools let you see and control a user’s screen. A <span class="term">knowledge base</span> holds step-by-step fixes. Account tools such as Microsoft Entra ID and Active Directory manage who can sign in to what.</p>
<h3>CompTIA A+</h3>
<p>A+ is the most widely requested certification for support jobs. It has two exams, Core 1 (hardware, mobile devices, networking, troubleshooting) and Core 2 (operating systems, security, software, operational procedures). Many people study for two to four months per exam. Check CompTIA’s site for current exam versions and voucher prices, and ask about student discounts.</p>
<h3>A realistic path</h3>
<p>A common path: help desk (year 1–2), desktop or Tier 2 support, then systems administrator, network administrator, or SOC analyst. Remote help desk jobs exist, but many employers want new technicians on site at first so they can learn from the team.</p></div>""",
    do=[act("choices", "w05-tickets", "Ticket triage: what would you do first?",
            "Four tickets just came in. For each one, choose the best first move.",
            {"label": "Ticket", "items": [
                {"card": {"kind": "ticket", "head": [["Ticket:", "INC-20431"], ["From:", "Front desk, Admissions"], ["Priority:", "Not set"]], "body": "Nobody in Admissions can print. The printer shows online. Open house starts in 40 minutes."},
                 "q": "Best first move?", "options": [{"t": "Set priority high and check whether the print queue on the print server is stuck", "ok": True, "fb": "Many users, a deadline, and a likely shared cause. A stuck queue is a common culprit."}, {"t": "Ask each user to restart their computer", "fb": "When everyone is affected, look for the shared component first."}, {"t": "Order a new printer", "fb": "Hardware replacement is a last resort, not a first step."}]},
                {"card": {"kind": "ticket", "head": [["Ticket:", "INC-20432"], ["From:", "Adjunct professor"], ["Priority:", "Not set"]], "body": "I clicked a link in an email about my paycheck and typed my password. Now my email is sending messages I didn’t write."},
                 "q": "Best first move?", "options": [{"t": "Escalate to security right away and help reset the password and sign-out sessions", "ok": True, "fb": "A compromised account is a security incident. Speed limits the damage."}, {"t": "Tell the professor to delete the email", "fb": "The account is already compromised. Deleting the email doesn’t fix it."}, {"t": "Put it in the queue for tomorrow", "fb": "Every hour the attacker has access, more phishing goes out from a trusted account."}]},
                {"card": {"kind": "ticket", "head": [["Ticket:", "REQ-8801"], ["From:", "New hire, Finance"], ["Priority:", "Low"]], "body": "Can I get Adobe Acrobat Pro installed? I start editing forms next week."},
                 "q": "Best first move?", "options": [{"t": "Check the software request policy and confirm license and manager approval", "ok": True, "fb": "Software requests usually need approval and a license. Following the process protects everyone."}, {"t": "Install a free trial from the web", "fb": "Unapproved software is a security and licensing risk."}, {"t": "Close the ticket because it is low priority", "fb": "Low priority means it can wait, not that it should be ignored."}]},
                {"card": {"kind": "ticket", "head": [["Ticket:", "INC-20433"], ["From:", "Student, via chat"], ["Priority:", "Not set"]], "body": "Wi-Fi works in the library but my laptop won’t connect in the science building."},
                 "q": "Best first move?", "options": [{"t": "Ask which network name they are joining and whether others in the building have the same problem", "ok": True, "fb": "Good troubleshooting starts by narrowing the problem: one device, or the whole building?"}, {"t": "Tell them to buy a new Wi-Fi adapter", "fb": "It works elsewhere, so the adapter is probably fine."}, {"t": "Escalate to network engineering immediately", "fb": "Collect basic facts first so the escalation is useful."}]}]}),
        f"""<section class="act" aria-labelledby="w05-disc-h"><span class="act-tag">Discussion</span><h3 id="w05-disc-h">Is help desk right for me?</h3>
{field("w05-disc", "What would you enjoy about help desk work, and what would be hard for you? Would you take a help desk job as a first step? Why?", rows=5)}</section>"""],
    investigate=dict(tag="Career Role Research Assignment 1", title="Entry-level IT jobs and the Technical Support role", short="assignment",
        intro="<p>Find three real entry-level IT job postings, then compare them to the NICE <b>Technical Support</b> work role (or another Implementation and Operation role if your postings fit better). Your analysis becomes role analysis #1 in Portfolio §2.</p>",
        resources=[("Indeed", "https://www.indeed.com/", "Search “help desk,” “IT support,” or “desktop support” in New Jersey."),
                   ("LinkedIn Jobs", "https://www.linkedin.com/jobs/", "Filter by Entry level experience."),
                   ("CISA NICCS: NICE Framework work roles", NICCS_NICE, "Find Technical Support and read its tasks, knowledge, and skills."),
                   ("CompTIA A+", "https://www.comptia.org/en-us/certifications/a/", "Exam objectives, prices, and study options."),
                   ("Professor Messer: A+ course", "https://www.professormesser.com/", "Free full-length A+ video course."),
                   ("CyberSeek career pathway", CYB_PATH, "Look at the IT support feeder role.")],
        steps=["Find three entry-level postings in New Jersey or remote. Record each below.",
               "Open the NICE Technical Support work role on NICCS. Read its tasks, knowledge, and skills.",
               "Complete role analysis #1. It saves into your portfolio automatically.",
               "Save as PDF and upload to Canvas."],
        fields=job_cards("w05", 3) + role_analysis("pf-r1", 1),
        grade="Career Role Research Assignments are 20% of the course total across three assignments.",
        submit=True),
    instructor=[("0–8 min", "Explore: why help desk, tiers, tools."),
                ("8–18", "Ticket triage, pairs, then debrief the compromised-account ticket."),
                ("18–25", "A+ overview with the CompTIA page projected."),
                ("25–45", "Assignment 1 work time: job search and NICE lookup."),
                ("45–50", "Discussion question and exit ticket.")],
)

W6 = dict(n=6, unit=2, title="Networking careers",
    lede="Network administrators keep things running; network engineers design what gets built. Explore both, the Cisco and CompTIA certification paths, and how cloud is changing the work.",
    due=[],
    objectives=[("Distinguish network administrator and network engineer roles.", 1),
                ("Map the Cisco and CompTIA networking certification paths.", 3),
                ("Compare networking job postings and salary progression in the NJ/NY market.", 4)],
    explore=f"""<div class="prose"><h3>Administrator or engineer?</h3>
<p>A <span class="term">network administrator</span> runs the network that exists: monitors it, adds users and devices, fixes outages, applies updates. A <span class="term">network engineer</span> designs and builds: plans new sites, chooses equipment, and solves the hardest problems. Titles overlap, so read the duties in each posting.</p></div>
{stats([("$96,800", "median pay, network and computer systems administrators, May 2024"), ("$130,390", "median pay, computer network architects, May 2024"), ("−4% and +12%", "projected change 2024–34 for administrators and architects")])}
<p class="source">Sources: BLS Occupational Outlook Handbook pages for {ext("https://www.bls.gov/ooh/computer-and-information-technology/network-and-computer-systems-administrators.htm", "administrators")} and {ext("https://www.bls.gov/ooh/computer-and-information-technology/computer-network-architects.htm", "architects")}. The numbers tell a story: routine administration is shrinking as automation grows, while design and cloud skills are growing.</p>
<div class="prose"><h3>The certification paths</h3>
<p><b>CompTIA Network+</b> is vendor-neutral: it covers how networks work regardless of brand, and fits well after A+. <b>Cisco</b> certifications teach Cisco equipment, which is common in enterprise networks. Cisco’s entry credential is the CCST (Cisco Certified Support Technician) in Networking; the <b>CCNA</b> is the best-known associate certification and is a common requirement for network admin jobs; CCNP and CCIE come later in a career.</p>
<h3>Cloud networking</h3>
<p>Cloud platforms have their own virtual networks, firewalls, and load balancers, configured with code instead of cables. Network professionals who add cloud and automation skills (scripting, Ansible, infrastructure as code) are the ones whose roles are growing.</p>
<h3>The NJ/NY market</h3>
<p>The New York metro area has one of the largest concentrations of IT jobs in the country, especially in finance, healthcare, pharmaceuticals, telecommunications, and government. Pay in the region generally runs above the national median, but so does cost of living. Use the BLS state data or CyberSeek’s metro view to compare.</p></div>""",
    do=[act("sort", "w06-certs", "Certification pathway mapping",
            "Place each certification at the career stage where people usually earn it.",
            {"buckets": [{"id": "e", "label": "Starting out", "hint": "first year or before your first IT job"}, {"id": "a", "label": "Associate", "hint": "1–3 years in"}, {"id": "p", "label": "Professional", "hint": "3–7 years in"}, {"id": "x", "label": "Expert", "hint": "senior engineers"}],
             "items": [{"t": "CompTIA A+", "b": "e"}, {"t": "Cisco CCST Networking", "b": "e"}, {"t": "CompTIA Network+", "b": "a", "why": "Network+ is often earned after A+ or in the first year of an IT job."},
                       {"t": "Cisco CCNA", "b": "a"}, {"t": "Cisco CCNP Enterprise", "b": "p"}, {"t": "Cisco CCIE", "b": "x", "why": "CCIE requires a hands-on lab exam and usually years of experience."}],
             "done": "Nicely mapped. Paths vary, but this is the typical order."}),
        f"""<section class="act" aria-labelledby="w06-cmp-h"><span class="act-tag">Activity</span><h3 id="w06-cmp-h">Compare two networking job postings</h3>
<p class="act-intro">Find one network administrator and one network engineer posting. Compare them side by side.</p>
{job_cards("w06", 2, "Networking posting")}
{field("w06-cmp", "What is the biggest difference between the two postings? Which one could you realistically apply for in two years?", rows=4)}</section>""",
        f"""<section class="act" aria-labelledby="w06-guest-h"><span class="act-tag">Guest speaker clip</span><h3 id="w06-guest-h">Notes from the guest speaker or video</h3>
{field("w06-guest", "Who spoke, what their path looked like, and one piece of advice you will use", rows=5)}</section>"""],
    investigate=dict(tag="In-class research", title="Map a networking career", short="research",
        intro="<p>Use the certification roadmap and Cisco’s own pages to sketch a five-year networking path.</p>",
        resources=[("Paul Jerimy Security Certification Roadmap", "https://pauljerimy.com/security-certification-roadmap/", "A huge chart of security certifications by domain and level. Find the networking and cloud columns."),
                   ("Cisco Networking Academy", "https://www.netacad.com/", "Free and low-cost Cisco courses, including CCNA material."),
                   ("CompTIA Network+", "https://www.comptia.org/en-us/certifications/network/", "Exam details and objectives."),
                   ("BLS: Network and Computer Systems Administrators", "https://www.bls.gov/ooh/computer-and-information-technology/network-and-computer-systems-administrators.htm", "Duties, pay, and outlook."),
                   ("NetworkChuck on YouTube", "https://www.youtube.com/@NetworkChuck", "Search the channel for CCNA videos.")],
        steps=["Find Network+ and CCNA on the Paul Jerimy roadmap. Note what sits next to and above them.",
               "Read the BLS page and find what education and experience administrators usually need.",
               "Sketch a five-year path below: year by year, role and certification."],
        fields=(field("w06-path", "My five-year networking path (year 1 through year 5: role, certification, skill)", rows=7) +
                field("w06-bls", "What BLS says administrators need to get hired", rows=3)),
        submit=False),
    instructor=[("0–10 min", "Explore: admin vs engineer, the salary numbers and what they suggest."),
                ("10–18", "Certification pathway sort."),
                ("18–30", "Compare two postings in pairs."),
                ("30–40", "Guest speaker video clip with notes."),
                ("40–50", "Five-year path sketch and exit ticket.")],
)

W7 = dict(n=7, unit=2, title="Cybersecurity careers: SOC, GRC, and pen testing",
    lede="Three very different ways to work in security: defending in a security operations center, managing risk and compliance, and testing defenses as an ethical hacker.",
    due=["Career Role Research Assignment 2", "Portfolio §2: role analysis #2"],
    objectives=[("Describe SOC analyst tiers and a day of alert triage.", 1),
                ("Explain GRC work and why it is an accessible pathway.", 1),
                ("Describe ethical hacking realistically, including authorization.", 5),
                ("Compare Protection and Defense roles with Oversight and Governance roles in the NICE Framework.", 1)],
    explore=f"""<div class="prose"><h3>The security operations center (SOC)</h3>
<p>A SOC is the team that watches for attacks. Alerts flow in from a <span class="term">SIEM</span> (security information and event management) system and other tools.</p></div>
{roles([("Tier 1: triage", "<p>Work the alert queue. Separate false positives from real problems. Escalate with good notes. The most common entry-level security job.</p>"),
        ("Tier 2: incident response", "<p>Investigate escalated alerts, scope the damage, contain the threat.</p>"),
        ("Tier 3: threat hunting", "<p>Search for attackers who slipped past the alerts. Tune detections. Usually senior analysts.</p>")])}
<div class="prose"><h3>Governance, risk, and compliance (GRC)</h3>
<p>GRC professionals make sure security matches the rules the organization must follow and the risks it is willing to accept. They write policies, run risk assessments, prepare for audits, and map controls to standards such as the NIST Cybersecurity Framework, HIPAA, or PCI DSS. GRC rewards writing, organization, and communication, so it is a strong pathway for people coming from business, healthcare, law, or the military.</p>
<h3>Ethical hacking</h3>
<p>Penetration testers attack systems with written permission to find weaknesses before criminals do. The reality: a lot of planning, careful scoping, and report writing, not just breaking in. Most testers spend years in IT, networking, or the SOC first. Practice happens only in authorized labs such as TryHackMe or Hack The Box.</p>
<h3>Certifications in this space</h3>
<p><b>CompTIA Security+</b> is the most common baseline security certification and is required for many U.S. government and contractor roles. <b>CompTIA CySA+</b> focuses on analyst work. <b>ISC2 Certified in Cybersecurity (CC)</b> is an entry-level credential. Its free training and exam program, One Million Certified in Cybersecurity, closed to new enrollments on May 20, 2026; the certification itself is still available.</p>
<h3>Reading NICE: two categories</h3>
<p>SOC and penetration testing work sit mostly in <b>Protection and Defense</b> (roles such as Defensive Cybersecurity, Incident Response, Threat Analysis, and Vulnerability Analysis). GRC work sits mostly in <b>Oversight and Governance</b> (roles such as Cybersecurity Policy and Planning, Security Control Assessment, and Privacy Compliance). Older sources call these “Protect and Defend” and “Oversee and Govern.”</p></div>""",
    do=[act("choices", "w07-soc", "SOC alert queue",
            "You are on Tier 1. Decide what to do with each alert.",
            {"label": "Alert", "items": [
                {"card": {"kind": "alert", "head": [["Rule:", "Impossible travel"], ["User:", "m.rivera"], ["Severity:", "Medium"]], "body": "Sign-in from Newark, NJ at 9:02 a.m., then from Lagos, Nigeria at 9:15 a.m. Second sign-in passed MFA by push approval."},
                 "q": "Your call?", "options": [{"t": "Escalate as a likely compromise and recommend disabling the session", "ok": True, "fb": "Two distant sign-ins 13 minutes apart, plus an approved push, suggests MFA fatigue: the user approved a prompt they didn’t start."}, {"t": "Close as a false positive: MFA passed", "fb": "MFA approval doesn’t prove the user started the sign-in. Attackers spam push prompts until someone taps Approve."}, {"t": "Ignore it until it happens again", "fb": "Delay gives the attacker time."}]},
                {"card": {"kind": "alert", "head": [["Rule:", "Port scan detected"], ["Source:", "10.20.5.14 (IT vulnerability scanner)"], ["Severity:", "Low"]], "body": "Host scanned 1,024 ports across the server subnet. Scheduled maintenance window: Tuesdays 1–3 a.m. Current time: Tuesday 1:40 a.m."},
                 "q": "Your call?", "options": [{"t": "Mark as a benign true positive: it is the approved scanner during its window, and note it", "ok": True, "fb": "The alert is accurate, but the activity is authorized. Good notes help tune the rule."}, {"t": "Escalate as an active attack", "fb": "Check context first. This is the company’s own scanner in its scheduled window."}, {"t": "Block the scanner’s address", "fb": "That would break an authorized security tool."}]},
                {"card": {"kind": "alert", "head": [["Rule:", "Mass file rename"], ["Host:", "FIN-LT-022"], ["Severity:", "High"]], "body": "3,400 files renamed to *.locked in 90 seconds. A file named README_RESTORE.txt appeared in each folder."},
                 "q": "Your call?", "options": [{"t": "Escalate immediately as likely ransomware and follow the playbook to isolate the host", "ok": True, "fb": "This is ransomware behavior. Isolating fast stops it spreading to shared drives."}, {"t": "Email the user to ask if they renamed files", "fb": "Waiting for a reply lets encryption spread."}, {"t": "Restart the laptop", "fb": "Restarting can destroy evidence and does not stop the spread. Follow the incident playbook."}]},
                {"card": {"kind": "alert", "head": [["Rule:", "Failed logins"], ["User:", "j.chen"], ["Severity:", "Low"]], "body": "Five failed logins from the user’s usual laptop at 8:01 a.m., then a successful login at 8:03 a.m. Password was changed yesterday."},
                 "q": "Your call?", "options": [{"t": "Close as a false positive with a note: likely the old password after a reset", "ok": True, "fb": "Same device, short burst, then success the day after a password change. Document your reasoning."}, {"t": "Escalate as a brute-force attack", "fb": "Brute force usually shows many attempts, often from unfamiliar sources."}, {"t": "Lock the account", "fb": "Locking a legitimate user creates work and frustration without reducing risk here."}]}]}),
        act("sort", "w07-fit", "SOC, GRC, or pen test? Sort the tasks",
            "Which role family does each task belong to? Notice which tasks you would enjoy.",
            {"buckets": [{"id": "soc", "label": "SOC analyst"}, {"id": "grc", "label": "GRC analyst"}, {"id": "pt", "label": "Penetration tester"}],
             "items": [{"t": "Review overnight alerts and document each decision", "b": "soc"}, {"t": "Write a password and MFA policy", "b": "grc"},
                       {"t": "Agree on scope and rules of engagement before testing", "b": "pt", "why": "Scoping and written permission come before any testing."},
                       {"t": "Prepare evidence for a HIPAA audit", "b": "grc"}, {"t": "Contain an infected laptop during an incident", "b": "soc"},
                       {"t": "Write a report explaining each weakness found and how to fix it", "b": "pt"}, {"t": "Score vendors on a third-party risk questionnaire", "b": "grc"},
                       {"t": "Tune a SIEM rule that creates too many false positives", "b": "soc"}]}),
        f"""<section class="act" aria-labelledby="w07-which-h"><span class="act-tag">Discussion</span><h3 id="w07-which-h">SOC analyst or GRC analyst: which fits you?</h3>
{field("w07-which", "Which of the two appeals more, and what in your background or personality points that way?", rows=4)}</section>"""],
    investigate=dict(tag="Career Role Research Assignment 2", title="Analyze a security work role", short="assignment",
        intro="<p>Pick one security work role from Protection and Defense or Oversight and Governance (for example, Defensive Cybersecurity, Incident Response, Vulnerability Analysis, Cybersecurity Policy and Planning, or Security Control Assessment). Find two postings that match it and complete role analysis #2 for Portfolio §2.</p>",
        resources=[("CISA NICCS: NICE Framework work roles", NICCS_NICE, "Read the tasks, knowledge, and skills for your chosen role."),
                   ("CyberSeek career pathway", CYB_PATH, "Find your role or its closest pathway title."),
                   ("Simply Cyber on YouTube", "https://www.youtube.com/@SimplyCyber", "Search the channel for advice on landing a SOC analyst job."),
                   ("CompTIA Security+", "https://www.comptia.org/en-us/certifications/security/", "Exam objectives (free download)."),
                   ("CompTIA CySA+", "https://www.comptia.org/en-us/certifications/cybersecurity-analyst/", "The analyst-focused certification."),
                   ("ISC2 Certified in Cybersecurity", "https://www.isc2.org/certifications/cc", "Entry-level certification. Check the page for current pricing and student options.")],
        steps=["Choose a work role and read it on NICCS.",
               "Find two postings on LinkedIn or Indeed that match it.",
               "Complete role analysis #2. It saves into your portfolio.",
               "Save as PDF and upload to Canvas."],
        fields=job_cards("w07", 2) + role_analysis("pf-r2", 2),
        grade="Career Role Research Assignments are 20% of the course total across three assignments.",
        submit=True),
    instructor=[("0–10 min", "Explore: SOC tiers, GRC, ethical hacking reality."),
                ("10–22", "SOC alert queue projected; students vote before revealing."),
                ("22–28", "Task sort and the “which fits you” discussion."),
                ("28–46", "Assignment 2 work time."),
                ("46–50", "Exit ticket.")],
    instructor_note="The ISC2 One Million Certified in Cybersecurity program ended May 20, 2026. If ISC2 offers a new academic or chapter voucher program, update the certification paragraph and the Week 9 roadmap note.",
)

QUIZ2 = [
    {"q": "Which tier of a help desk handles password resets and common requests?", "options": [{"t": "Tier 1", "ok": True}, {"t": "Tier 2"}, {"t": "Tier 3"}, {"t": "The SOC"}], "explain": "Tier 1 handles common, well-documented requests."},
    {"q": "Escalating a ticket means…", "options": [{"t": "Handing it to a higher tier with notes on what you tried", "ok": True}, {"t": "Closing it without a fix"}, {"t": "Raising its price"}, {"t": "Sending it back to the user"}], "explain": "Good escalation notes save the next tier time."},
    {"q": "CompTIA A+ is made of…", "options": [{"t": "Two exams, Core 1 and Core 2", "ok": True}, {"t": "One exam"}, {"t": "A hands-on lab only"}, {"t": "Four exams"}], "explain": "Core 1 covers hardware and networking; Core 2 covers operating systems, security, and procedures."},
    {"q": "Who usually designs new networks rather than running existing ones?", "options": [{"t": "Network engineer", "ok": True}, {"t": "Help desk technician"}, {"t": "GRC analyst"}, {"t": "SOC Tier 1 analyst"}], "explain": "Administrators run; engineers design and build. Titles overlap, so read the duties."},
    {"q": "Which certification is vendor-neutral?", "options": [{"t": "CompTIA Network+", "ok": True}, {"t": "Cisco CCNA"}, {"t": "Cisco CCNP"}, {"t": "Cisco CCIE"}], "explain": "CompTIA certifications aren’t tied to one manufacturer."},
    {"q": "A SIEM is used to…", "options": [{"t": "Collect and correlate security events and generate alerts", "ok": True}, {"t": "Route traffic between networks"}, {"t": "Print reports for HR"}, {"t": "Assign IP addresses"}], "explain": "SOC analysts work alerts that come largely from the SIEM."},
    {"q": "Two sign-ins 13 minutes apart from New Jersey and another continent most likely suggest…", "options": [{"t": "A compromised account", "ok": True}, {"t": "A normal business trip"}, {"t": "A DNS outage"}, {"t": "A slow laptop"}], "explain": "This is an impossible travel alert."},
    {"q": "What separates ethical hacking from a crime?", "options": [{"t": "Written authorization from the system owner", "ok": True}, {"t": "Good intentions"}, {"t": "Using well-known tools"}, {"t": "Being a student"}], "explain": "Authorization is the line."},
    {"q": "Writing policies and preparing for audits is typical of which pathway?", "options": [{"t": "GRC", "ok": True}, {"t": "Penetration testing"}, {"t": "Network engineering"}, {"t": "Help desk"}], "explain": "Governance, risk, and compliance."},
    {"q": "In the current NICE Framework, Incident Response belongs to…", "options": [{"t": "Protection and Defense", "ok": True}, {"t": "Oversight and Governance"}, {"t": "Design and Development"}, {"t": "Investigation"}], "explain": "Older sources called this category “Protect and Defend.”"},
    {"q": "Under the cloud shared responsibility model, who is responsible for setting strong passwords and MFA on user accounts?", "options": [{"t": "The customer", "ok": True}, {"t": "The cloud provider"}, {"t": "Nobody"}, {"t": "The internet provider"}], "explain": "Providers secure the physical cloud; customers secure their accounts, data, and configurations."},
    {"q": "IAM stands for…", "options": [{"t": "Identity and access management", "ok": True}, {"t": "Internet address mapping"}, {"t": "Incident alert monitoring"}, {"t": "Integrated application management"}], "explain": "IAM decides who can sign in and what they can reach."},
    {"q": "Which law protects health information in the United States?", "options": [{"t": "HIPAA", "ok": True}, {"t": "GDPR"}, {"t": "PCI DSS"}, {"t": "FERPA"}], "explain": "GDPR is the EU privacy law. PCI DSS is a payment card industry standard. FERPA covers student records."},
    {"q": "PCI DSS applies to organizations that…", "options": [{"t": "Store, process, or transmit payment card data", "ok": True}, {"t": "Run hospitals"}, {"t": "Have offices in Europe"}, {"t": "Use cloud email"}], "explain": "PCI DSS is the payment card security standard."},
    {"q": "According to CyberSeek’s 2025 data, roughly what share of cybersecurity job listings explicitly mention AI skills?", "options": [{"t": "About 10%", "ok": True}, {"t": "About 90%"}, {"t": "Almost none"}, {"t": "Exactly half"}], "explain": "About one in ten, a number worth watching as AI skills become more common in postings."},
]

PATHWAY = {"groups": [
    {"label": "Feeder roles", "roles": [{"id": "f-sup", "name": "IT support / help desk"}, {"id": "f-net", "name": "Networking"}, {"id": "f-sw", "name": "Software development"}, {"id": "f-sys", "name": "Systems engineering"}, {"id": "f-fin", "name": "Financial and risk analysis"}, {"id": "f-intel", "name": "Security intelligence"}]},
    {"label": "Entry level", "roles": [{"id": "e-spec", "name": "Cybersecurity specialist or technician"}, {"id": "e-crime", "name": "Cyber crime analyst"}, {"id": "e-ir", "name": "Incident and intrusion analyst"}, {"id": "e-audit", "name": "IT auditor"}]},
    {"label": "Mid level", "roles": [{"id": "m-analyst", "name": "Cybersecurity analyst"}, {"id": "m-cons", "name": "Cybersecurity consultant"}, {"id": "m-pt", "name": "Penetration and vulnerability tester"}]},
    {"label": "Advanced", "roles": [{"id": "a-mgr", "name": "Cybersecurity manager"}, {"id": "a-eng", "name": "Cybersecurity engineer"}, {"id": "a-arch", "name": "Cybersecurity architect"}]}]}

W8 = dict(n=8, unit=2, title="Cloud, AI, and emerging IT careers",
    lede="Cloud engineering, cloud security, and DevSecOps are among the fastest-changing parts of IT. Add identity, privacy law, and AI to see where your target role is heading.",
    due=["Reflection Journal 2", "Quiz 2 (open-note, Unit 2)", "Portfolio §3: CyberSeek pathway annotation"],
    objectives=[("Describe cloud engineer, cloud security, and DevSecOps roles.", 1),
                ("Explain the shared responsibility model and identity and access management.", 2),
                ("Identify which laws and standards (GDPR, HIPAA, PCI DSS) apply to common scenarios.", 2),
                ("Annotate a CyberSeek career pathway with personal interest ratings.", 6)],
    explore=f"""<div class="prose"><h3>Cloud roles</h3></div>
{roles([("Cloud engineer", "<p>Builds and runs systems on Azure, AWS, or Google Cloud, usually by writing code that creates the infrastructure.</p>"),
        ("Cloud security engineer", "<p>Secures cloud accounts, identities, networks, and data. Hunts for misconfigurations, the most common cause of cloud breaches.</p>"),
        ("DevSecOps engineer", "<p>Builds security checks into the pipeline that turns developers’ code into running software.</p>")])}
<div class="prose"><h3>Shared responsibility</h3>
<p>In the cloud, the provider secures the physical data centers, hardware, and core platform. The customer secures what it puts there: accounts, data, settings, and access. Most cloud breaches come from the customer side, such as a storage bucket left public or an account without MFA.</p>
<h3>Identity and access management (IAM)</h3>
<p>IAM decides who can sign in and what each person can reach. The principle of <span class="term">least privilege</span> says everyone gets only the access their job needs. As networks spread across clouds and home offices, identity has become the new perimeter, and IAM specialists are in demand.</p>
<h3>Privacy and compliance</h3>
<p><b>GDPR</b> is the European Union’s privacy law; it applies to organizations that handle EU residents’ personal data, including many U.S. companies. <b>HIPAA</b> protects health information in the U.S. <b>PCI DSS</b> is the security standard for organizations that handle payment cards. Knowing which rules apply is everyday GRC work.</p>
<h3>AI’s impact</h3>
<p>CyberSeek’s 2025 data found that about 10 percent of cybersecurity job listings specifically mention AI skills. AI tools already help SOC analysts summarize alerts and help attackers write convincing phishing. Routine tasks are being automated, while judgment, communication, and the ability to check AI output are becoming more valuable. Brookdale has proposed a 200-level course, AI Cybersecurity Foundations, that goes deeper.</p></div>""",
    do=[act("sort", "w08-shared", "Shared responsibility: provider or customer?",
            "In a typical cloud service, who is responsible for each item?",
            {"buckets": [{"id": "p", "label": "Cloud provider"}, {"id": "c", "label": "Customer"}],
             "items": [{"t": "Physical security of the data center", "b": "p"}, {"t": "Replacing failed hard drives in the servers", "b": "p"},
                       {"t": "Turning on MFA for employee accounts", "b": "c"}, {"t": "Deciding who can read a storage bucket", "b": "c", "why": "Access settings are the customer’s job. Public buckets are a classic breach cause."},
                       {"t": "Classifying which data is sensitive", "b": "c"}, {"t": "Power and cooling for the servers", "b": "p"},
                       {"t": "Configuring firewall rules for virtual machines", "b": "c"}]}),
        act("sort", "w08-laws", "Which rule applies?",
            "Match each scenario to the law or standard most directly involved.",
            {"buckets": [{"id": "gdpr", "label": "GDPR"}, {"id": "hipaa", "label": "HIPAA"}, {"id": "pci", "label": "PCI DSS"}],
             "items": [{"t": "A clinic emails lab results to the wrong patient", "b": "hipaa"}, {"t": "An online store stores customers’ card numbers", "b": "pci"},
                       {"t": "A New Jersey retailer sells to shoppers in France and collects their addresses", "b": "gdpr", "why": "GDPR applies to EU residents’ data wherever the company is."},
                       {"t": "A campus café upgrades its card readers", "b": "pci"}, {"t": "A health insurer’s claims database is breached", "b": "hipaa"},
                       {"t": "A user in Germany asks a U.S. app to delete all their data", "b": "gdpr"}]}),
        f"""<section class="act" aria-labelledby="w08-ai-h"><span class="act-tag">Discussion</span><h3 id="w08-ai-h">How will AI affect your target role?</h3>
{field("w08-ai", "Name your target role. List one task AI might take over, one task AI will make easier, and one human skill that will matter more.", rows=5)}</section>""",
        act("choices", "w08-quiz", "Practice Quiz 2: Unit 2", "Fifteen open-note practice questions covering Weeks 5–8, in the style of the graded Quiz 2 in Canvas.",
            {"items": QUIZ2, "shuffle": True}, tag="Practice quiz")],
    investigate=dict(tag="Reflection Journal 2", title="Explore cloud careers, then reflect", short="journal",
        intro="<p>Browse one cloud provider’s free training, then write Reflection Journal 2.</p>",
        resources=[("Microsoft Learn: Azure Fundamentals (AZ-900)", "https://learn.microsoft.com/en-us/credentials/certifications/azure-fundamentals/", "Microsoft’s entry-level cloud certification with free learning paths."),
                   ("Microsoft Learn career paths", "https://learn.microsoft.com/en-us/training/career-paths/", "Role-based learning paths."),
                   ("AWS Skill Builder", "https://skillbuilder.aws/", "Free AWS training, including Cloud Practitioner prep."),
                   ("World Economic Forum: Future of Jobs Report 2025", "https://www.weforum.org/publications/the-future-of-jobs-report-2025/", "Read the summary on fastest-growing jobs and skills."),
                   ("Simply Cyber on YouTube", "https://www.youtube.com/@SimplyCyber", "Search the channel for cloud security career videos.")],
        steps=["Open one cloud provider’s training page and find a beginner learning path.",
               "Skim the WEF Future of Jobs summary for technology skills.",
               "Write Reflection Journal 2 (250–350 words).",
               "Save as PDF and upload to Canvas."],
        fields=(field("w08-cloudpath", "The beginner cloud learning path you found and how long it takes", kind="text") +
                field("w08-journal", "Reflection Journal 2",
                      help="Prompt: You have now looked at support, networking, security, and cloud roles. Which two interest you most, and why? What surprised you? What worries you about entering the field, including AI, and what is one step that would ease that worry?",
                      rows=12, words="250-350")),
        grade="Reflection journals are 15% of the course total across three entries.",
        submit=True),
    portfolio=f"""<p class="prose">Portfolio §3 asks for an annotated CyberSeek career pathway. Open the {ext(CYB_PATH, "CyberSeek pathway tool")}, click each role, and rate your interest from 0 to 5 with a short note. The tool’s role list may have changed since this page was written; add notes about any new roles you find in the box at the end.</p>
{act("rating", "pf-pathway", "Portfolio §3: My annotated CyberSeek pathway", "Rate each role from 0 (not interested) to 5 (very interested). Your note should mention something you learned from the CyberSeek role profile: salary, a skill, or a certification.", PATHWAY, tag="Portfolio §3")}
{field("pf-pathway-notes", "Portfolio §3: Overall notes on the pathway", help="Which path from a feeder role to an advanced role looks most realistic for you? Any roles on the current CyberSeek map that are not listed above?", rows=5)}""",
    instructor=[("0–10 min", "Explore: cloud roles, shared responsibility, IAM."),
                ("10–18", "Shared responsibility and compliance sorts."),
                ("18–24", "AI discussion."),
                ("24–40", "Quiz 2 in Canvas (open note)."),
                ("40–50", "Start Portfolio §3 annotation; Journal 2 is due.")],
)

WEEKS = [W5, W6, W7, W8]
