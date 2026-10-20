from lib import *

W13 = dict(n=13, unit=4, title="The future of IT: AI, quantum, and zero trust",
    lede="AI is changing both attacks and defenses, zero trust is replacing the old castle-and-moat model, and quantum computing is forcing a change in encryption. What does that mean for your job in 2030?",
    due=["Portfolio full draft"],
    objectives=[("Describe how AI is used by both attackers and defenders.", 2),
                ("Explain zero trust architecture and its career implications.", 2),
                ("Explain why quantum computing affects encryption and what post-quantum cryptography is.", 2),
                ("Identify skills likely to matter in 5–10 years.", 4)],
    explore=f"""<div class="prose"><h3>AI on both sides</h3>
<p>Defenders use AI to summarize alerts, spot unusual behavior, write detection rules, and speed up investigations. Attackers use it to write convincing phishing in any language, clone voices, and automate reconnaissance. Organizations also need people who can secure AI systems themselves. The skills that rise in value: judging whether AI output is correct, understanding the systems underneath, and communicating clearly.</p>
<h3>Zero trust</h3>
<p>The old model trusted anything inside the network, like a castle with a moat. <span class="term">Zero trust</span> assumes no user or device is trusted by default, inside or outside. Every request is checked: who is asking, from what device, for what, and whether that makes sense right now. CISA’s Zero Trust Maturity Model organizes the work into five pillars: identity, devices, networks, applications and workloads, and data. Careers in IAM, endpoint security, and cloud security all grow from this shift.</p>
<h3>Quantum and encryption</h3>
<p>Today’s public-key encryption relies on math problems that ordinary computers cannot solve in any reasonable time. A large enough quantum computer could solve some of them, which would break much of the encryption the internet relies on. Attackers may already be collecting encrypted data to decrypt later. In August 2024 NIST published its first post-quantum cryptography standards, and organizations are now planning the long migration to them. That migration will need people who understand where encryption is used.</p>
<h3>IoT security</h3>
<p>Cameras, medical devices, building controls, and factory equipment are all on networks now, often with weak security. Operational technology (OT) security is a growing specialty; NIST added an OT Cybersecurity Engineering work role to the NICE Framework in 2025.</p>
<h3>Skills that last</h3>
<p>Tools change every few years. Fundamentals do not: networking, operating systems, how authentication works, scripting, writing clearly, and learning how to learn.</p></div>""",
    do=[act("diagram", "w13-zt", "Follow a zero trust sign-in",
            "Step through how a zero trust system decides whether to let an employee open a payroll file from a coffee shop.",
            {"w": 780, "h": 280, "alt": "Diagram: user and device send a request to a policy engine that checks identity, device health, and context before granting access to one application.",
             "nodes": [{"id": "u", "label": "Employee", "sub": "at a coffee shop", "x": 85, "y": 140},
                       {"id": "dev", "label": "Laptop", "sub": "company device", "x": 85, "y": 245},
                       {"id": "pe", "label": "Policy engine", "sub": "decides every request", "x": 330, "y": 140, "w": 150},
                       {"id": "id", "label": "Identity check", "sub": "password + MFA", "x": 330, "y": 40, "w": 140},
                       {"id": "hl", "label": "Device health", "sub": "patched? encrypted?", "x": 330, "y": 245, "w": 150},
                       {"id": "app", "label": "Payroll app", "sub": "only this app", "x": 600, "y": 140, "w": 130},
                       {"id": "log", "label": "Monitoring", "sub": "logs everything", "x": 600, "y": 245, "w": 130}],
             "links": [["u", "pe"], ["pe", "id"], ["dev", "hl"], ["hl", "pe"], ["pe", "app"], ["app", "log"]],
             "steps": [{"on": ["u"], "title": "A request, not a location", "text": "In the old model, being on the office network was enough. In zero trust, being at a coffee shop or at the office makes no difference. Every request starts untrusted."},
                       {"on": ["u", "pe", "id"], "links": [0, 1], "title": "Verify the identity", "text": "The policy engine checks who is asking: correct password plus a phishing-resistant MFA method."},
                       {"on": ["dev", "hl", "pe"], "links": [2, 3], "title": "Verify the device", "text": "Is this a company laptop? Is it patched, encrypted, and running endpoint protection? An unhealthy device can be denied even with the right password."},
                       {"on": ["pe"], "title": "Check the context", "text": "Is the request normal for this person? Payroll staff open payroll on weekdays; a sign-in from a new country at 3 a.m. would trigger more checks."},
                       {"on": ["pe", "app"], "links": [4], "title": "Least privilege", "text": "Access is granted to the payroll app only, not the whole network, and only for this session."},
                       {"on": ["app", "log"], "links": [5], "title": "Keep watching", "text": "Activity is logged and monitored. If behavior changes, access can be cut mid-session. Each box in this diagram is someone’s job."}]}),
        f"""<section class="act" aria-labelledby="w13-2030-h"><span class="act-tag">Scenario</span><h3 id="w13-2030-h">Your job in 2030</h3>
<p class="act-intro">Imagine it is 2030 and you have the role you are aiming for now.</p>
{field("w13-2030-day", "Describe one workday in 2030. Which tools, including AI, are you using?", rows=5)}
{field("w13-2030-trend", "Which trend from this week (AI, zero trust, quantum, IoT) affects your target role most, and how?", rows=4)}
{field("w13-2030-skill", "One skill you will start building this year so you are ready", kind="text")}</section>""",
        f"""<section class="act" aria-labelledby="w13-peer-h"><span class="act-tag">Peer review</span><h3 id="w13-peer-h">Portfolio draft peer review</h3>
<p class="act-intro">Swap portfolio drafts with a partner. Check what is there, then give one specific suggestion.</p>
{field("w13-peer-name", "Whose draft I reviewed", kind="text")}
{checks("Peer review checklist", [("w13-p1", "§1 Bio is about one page and sounds like a person"), ("w13-p2", "§2 Has two NICE work roles with real job postings"), ("w13-p3", "§3 CyberSeek ratings have notes, not just numbers"), ("w13-p4", "§4 Roadmap has dates and Brookdale options"), ("w13-p5", "§5 Resume or LinkedIn is tailored to one role"), ("w13-p6", "§6 Reflection is started")])}
{field("w13-peer-fb", "One strength and one specific suggestion", rows=4)}</section>"""],
    investigate=dict(tag="In-class research", title="What the reports say", short="research",
        intro="<p>Read the summary of one major workforce or technology report and pull out what it means for your target role.</p>",
        resources=[("World Economic Forum: Future of Jobs Report 2025", "https://www.weforum.org/publications/the-future-of-jobs-report-2025/", "Fastest-growing jobs and skills worldwide."),
                   ("ISC2 research", "https://www.isc2.org/research", "Find the most recent Cybersecurity Workforce Study summary."),
                   ("CISA Zero Trust Maturity Model", "https://www.cisa.gov/zero-trust-maturity-model", "The five pillars and how organizations progress."),
                   ("NIST post-quantum cryptography project", "https://csrc.nist.gov/projects/post-quantum-cryptography", "Background on the new encryption standards."),
                   ("Computerphile on YouTube", "https://www.youtube.com/@Computerphile", "Search the channel for quantum computing and encryption.")],
        steps=["Pick one report or resource.",
               "Find two findings that relate to your target role.",
               "Record them below in your own words."],
        fields=(field("w13-rep", "Report I read, and two findings that matter for my target role", rows=5) +
                field("w13-rep-act", "What I will do differently because of it", rows=3)),
        submit=False),
    portfolio=f"""<p class="prose">Your <b>full portfolio draft</b> is due this week. Open the portfolio page, check that every section has content, and save it as a PDF for Canvas.</p>
<p><a class="btn btn-primary" href="../portfolio.html">Review and save my portfolio draft</a></p>""",
    instructor=[("0–12 min", "Explore: AI, zero trust, quantum, IoT."),
                ("12–20", "Zero trust stepper."),
                ("20–28", "Your job in 2030."),
                ("28–44", "Portfolio peer review in pairs."),
                ("44–50", "Report research starts; finish as homework.")],
)

W14 = dict(n=14, unit=4, title="Portfolio polish and presentation skills",
    lede="Tighten your portfolio, learn to tell your story in 60 seconds, and practice the interview questions entry-level IT candidates hear most.",
    due=["Portfolio final submission"],
    objectives=[("Describe what makes a career portfolio strong.", 6),
                ("Deliver a 60-second elevator pitch.", 6),
                ("Answer common entry-level IT interview questions using the STAR method.", 6),
                ("Name the NETW course you will take next.", 3)],
    explore=f"""<div class="prose"><h3>What makes a portfolio strong</h3>
<p>Specific beats general. Real job postings, real numbers, real dates. Your own voice. Evidence that you did the research rather than repeated it. A clear thread from who you are (§1) to what you want (§2–3) to how you will get there (§4–5).</p>
<h3>The elevator pitch</h3>
<p>Sixty seconds, four parts: <b>who you are</b>, <b>what you are working on</b>, <b>what you are looking for</b>, and <b>a question or ask</b>. Practice until it sounds like conversation, not a script.</p>
<h3>Talking about a non-traditional background</h3>
<p>Retail, food service, the military, caregiving, healthcare, and trades all build skills IT employers want: staying calm with upset customers, following procedures, working shifts, solving problems under pressure. Name the skill, give a one-sentence example, and connect it to the role.</p>
<h3>The STAR method</h3>
<p>For “tell me about a time when…” questions, answer with <b>S</b>ituation, <b>T</b>ask, <b>A</b>ction, <b>R</b>esult. Keep the situation short and spend most of your time on what you did.</p>
<h3>Your next NETW course</h3>
<p>Look at your Week 9 roadmap. Which NETW course comes next for you? Meet with an advisor before registration.</p></div>""",
    do=[f"""<section class="act" aria-labelledby="w14-pitch-h"><span class="act-tag">Activity</span><h3 id="w14-pitch-h">Build your elevator pitch</h3>
<div class="cols cols-2">{field("w14-p-who", "Who I am", rows=2, placeholder="I’m a Brookdale student in the NETW program…")}{field("w14-p-what", "What I’m working on", rows=2, placeholder="…studying for CompTIA A+ and building a home lab…")}{field("w14-p-want", "What I’m looking for", rows=2, placeholder="…a part-time help desk role or internship…")}{field("w14-p-ask", "My question or ask", rows=2, placeholder="…how did you get started at your company?")}</div>
{field("w14-pitch", "My full pitch, put together", rows=5, words="110-170")}</section>""",
        act("timer", "w14-timer", "60-second pitch practice", "Pair up. Start the timer and deliver your pitch. Switch roles and give each other one note.", {"seconds": 60}),
        act("flip", "w14-interview", "Mock interview question pairs",
            "One partner asks; the other answers. Flip for what the interviewer is listening for.",
            {"labels": ["Interview question", "What they’re listening for"], "cards": [
                {"f": "Tell me about yourself.", "b": "Your elevator pitch, aimed at this job. Under two minutes."},
                {"f": "A user says the internet is down. Walk me through what you’d do.", "b": "A calm, step-by-step process: ask questions, check one thing at a time, document, escalate when needed."},
                {"f": "Tell me about a time you dealt with an upset customer.", "b": "A STAR story showing patience and problem-solving."},
                {"f": "What’s the difference between a switch and a router?", "b": "Basics from Week 3, explained simply."},
                {"f": "How do you keep your skills current?", "b": "Specific sources: labs, courses, podcasts, communities."},
                {"f": "What would you do if you didn’t know the answer to a problem?", "b": "Honesty plus a plan: research, ask a teammate, escalate. Never guess on security."},
                {"f": "Why do you want to work in IT?", "b": "A genuine reason connected to what you’ve learned about the work."},
                {"f": "Do you have any questions for us?", "b": "Always yes. Ask about training, the team, or what success looks like in 90 days."}]}),
        f"""<section class="act" aria-labelledby="w14-star-h"><span class="act-tag">Activity</span><h3 id="w14-star-h">Write one STAR story</h3>
<div class="cols cols-2">{field("w14-s", "Situation", rows=2)}{field("w14-t", "Task", rows=2)}{field("w14-a", "Action", rows=3)}{field("w14-r", "Result", rows=2)}</div></section>"""],
    investigate=dict(tag="In-class research", title="Interview prep resources", short="research",
        intro="<p>Find one interview resource to use before a real interview, and book a mock interview if you can.</p>",
        resources=[("Brookdale Career Center", "https://www.brookdalecc.edu/career-center/", "Mock interviews and coaching."),
                   ("Simply Cyber on YouTube", "https://www.youtube.com/@SimplyCyber", "Search the channel for interview tips."),
                   ("LinkedIn Learning", "https://www.linkedin.com/learning/", "Interview preparation courses; free through many public libraries."),
                   ("Brookdale catalog", "https://catalog.brookdalecc.edu/", "Confirm your next NETW course.")],
        steps=["Watch or read one interview resource.",
               "Record two tips you will use.",
               "Name your next NETW course and when you will register."],
        fields=(field("w14-tips", "Two interview tips I will use, and where they came from", rows=4) +
                field("w14-next", "My next NETW course and when I will register", kind="text")),
        submit=False),
    portfolio=f"""<p class="prose">Final portfolio submission is due this week. Polish each section on the portfolio page, then save the full portfolio as a PDF for Canvas.</p>
<p><a class="btn btn-primary" href="../portfolio.html">Polish and save my final portfolio</a></p>
<p class="prose">Next week you present portfolio highlights in 3–5 minutes. Preview the format in Week 15.</p>""",
    instructor=[("0–10 min", "Explore: strong portfolios, pitch, non-traditional backgrounds, STAR."),
                ("10–22", "Pitch builder and timed practice in pairs."),
                ("22–36", "Mock interview pairs with the flip cards."),
                ("36–44", "STAR story."),
                ("44–50", "Preview Week 15 presentation format.")],
)

W15 = dict(n=15, unit=4, title="Final presentations and next steps",
    lede="Present your portfolio highlights, give and get feedback, and leave with a plan for what you will do next.",
    due=["Final presentation (3–5 minutes)", "Peer feedback forms", "Course exit reflection"],
    objectives=[("Present a 3–5 minute summary of your Career Exploration Portfolio.", 6),
                ("Give constructive peer feedback.", 6),
                ("Commit to specific next steps and continued learning resources.", 3)],
    explore=f"""<div class="prose"><h3>Presentation format</h3>
<p>Three to five minutes. Suggested flow: your elevator pitch (30 seconds), the two roles you explored and what you learned (1–2 minutes), your roadmap (1 minute), and one thing you will do next (30 seconds). Slides are optional; your portfolio PDF or this site can be your visual.</p>
<h3>Giving useful feedback</h3>
<p>Be specific and kind. Name one thing that worked, ask one genuine question, and offer one suggestion the presenter could use tomorrow.</p>
<h3>Keep going</h3>
<p>Most learning in IT happens after the class ends. TryHackMe, Cisco Networking Academy, NICE’s list of free learning content, professional organizations, and communities like Simply Cyber’s keep you moving. Your next NETW course, starting with NETW 107, is the next step on your roadmap.</p></div>""",
    do=[f"""<section class="act" aria-labelledby="w15-plan-h"><span class="act-tag">Activity</span><h3 id="w15-plan-h">Presentation planner</h3>
{field("w15-open", "Opening: my elevator pitch (about 30 seconds)", rows=3)}
{field("w15-roles", "The two roles I explored and the most important thing I learned about each", rows=4)}
{field("w15-roadmap", "My roadmap highlights", rows=3)}
{field("w15-close", "My closing: the one thing I will do next", rows=2)}</section>""",
        act("timer", "w15-timer", "Five-minute rehearsal timer", "Rehearse once with a partner. Aim to finish between 3 and 5 minutes.", {"seconds": 300}),
        f"""<section class="act no-export" aria-labelledby="w15-peer-h"><span class="act-tag">Peer feedback</span><h3 id="w15-peer-h">Peer feedback form</h3>
<p class="act-intro">Fill this in for a classmate during presentations. Your instructor may collect these in Canvas instead.</p>
{field("w15-pf-name", "Presenter", kind="text")}
{field("w15-pf-good", "One thing that worked", rows=2)}
{field("w15-pf-q", "One question I have for them", rows=2)}
{field("w15-pf-sug", "One suggestion they could use tomorrow", rows=2)}</section>""",
        f"""<section class="act" aria-labelledby="w15-kwl-h"><span class="act-tag">Activity</span><h3 id="w15-kwl-h">Finish your KWL chart</h3>
<p class="act-intro">These are the same boxes you started in Week 1. Read what you wrote, then fill in the last column.</p>
<div class="kwl">{field("w01-kwl-k", "K: What I knew in Week 1", rows=5)}{field("w01-kwl-w", "W: What I wanted to find out", rows=5)}{field("w01-kwl-l", "L: What I learned", rows=5)}</div></section>"""],
    investigate=dict(tag="Course exit reflection", title="Pathways forward", short="reflection",
        intro="<p>Choose your continued learning resources and write a short exit reflection.</p>",
        resources=[("TryHackMe", "https://tryhackme.com/", "Continue with a learning path such as Pre Security or Cyber Security 101."),
                   ("Cisco Networking Academy", "https://www.netacad.com/", "Free courses that line up with NETW content."),
                   ("NICE: free and low-cost online learning content", "https://www.nist.gov/itl/applied-cybersecurity/nice/resources/online-learning-content", "NIST’s curated list."),
                   ("Simply Cyber", "https://simplycyber.io/", "Community and career resources, including a Discord server."),
                   ("Brookdale catalog", "https://catalog.brookdalecc.edu/", "Your next NETW course.")],
        steps=["Pick one continued learning resource and one first step in it.",
               "Write your exit reflection.",
               "Save as PDF and upload to Canvas."],
        fields=(field("w15-next-res", "The resource I will continue with, and my first step", rows=3) +
                field("w15-exit", "Course exit reflection: one thing I will do next, by when, and how I’ll know I did it", rows=5) +
                field("w15-feedback", "Optional: feedback for the instructor about this course", rows=4)),
        submit=True),
    instructor=[("0–5 min", "Presentation order and feedback form instructions."),
                ("5–40", "Presentations, 3–5 minutes each, with peer feedback forms."),
                ("40–46", "Course debrief: finish the KWL chart."),
                ("46–50", "Share one thing you will do next; exit survey.")],
    instructor_note="With more than about eight students, split presentations into two rooms or record some in advance. The peer feedback form is excluded from the student’s own Week 15 PDF.",
)

WEEKS = [W13, W14, W15]
