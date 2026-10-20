from lib import *
from unit1 import NICCS_NICE, CYB_PATH

ROADMAP = {"horizon": 18,
    "typeLabels": {"course": "Brookdale courses (check the catalog and your advisor for the current sequence)", "cert": "Industry certifications", "exp": "Experience and community"},
    "options": [
        {"id": "c-107", "label": "NETW 107", "type": "course", "note": "the first course in the NETW sequence"},
        {"id": "c-110", "label": "NETW 110 Red Hat Linux Administration", "type": "course"},
        {"id": "c-111", "label": "NETW 111 Red Hat Ansible Automation", "type": "course"},
        {"id": "c-112", "label": "NETW 112 Containers and Orchestration", "type": "course"},
        {"id": "c-190", "label": "NETW 190 Windows Endpoint Administration", "type": "course"},
        {"id": "c-191", "label": "NETW 191 Hybrid Server Administration", "type": "course"},
        {"id": "c-237", "label": "NETW 237 Perimeter Security", "type": "course"},
        {"id": "x-aplus", "label": "CompTIA A+", "type": "cert", "note": "support"},
        {"id": "x-netplus", "label": "CompTIA Network+", "type": "cert", "note": "networking"},
        {"id": "x-ccst", "label": "Cisco CCST Networking", "type": "cert", "note": "networking, entry"},
        {"id": "x-ccna", "label": "Cisco CCNA", "type": "cert", "note": "networking"},
        {"id": "x-secplus", "label": "CompTIA Security+", "type": "cert", "note": "security baseline"},
        {"id": "x-cc", "label": "ISC2 Certified in Cybersecurity (CC)", "type": "cert", "note": "security, entry"},
        {"id": "x-cysa", "label": "CompTIA CySA+", "type": "cert", "note": "SOC analyst"},
        {"id": "x-az900", "label": "Microsoft Azure Fundamentals (AZ-900)", "type": "cert", "note": "cloud"},
        {"id": "x-awscp", "label": "AWS Certified Cloud Practitioner", "type": "cert", "note": "cloud"},
        {"id": "x-rhcsa", "label": "Red Hat Certified System Administrator (RHCSA)", "type": "cert", "note": "Linux"},
        {"id": "e-thm", "label": "Complete a TryHackMe learning path", "type": "exp"},
        {"id": "e-ncl", "label": "Compete in the National Cyber League", "type": "exp"},
        {"id": "e-org", "label": "Join a professional organization chapter meeting", "type": "exp"},
        {"id": "e-intern", "label": "Apply for an IT internship or help desk job", "type": "exp"},
        {"id": "e-transfer", "label": "Meet with an advisor about transfer (NJ Transfer)", "type": "exp"}]}

W9 = dict(n=9, unit=3, title="Education pathways and certifications",
    lede="Degrees, certificates, transfer, certifications, bootcamps: there are many ways in. Build a realistic 6–18 month plan that stacks credentials toward your target role.",
    due=["Career Role Research Assignment 3", "Portfolio §4: education and certification roadmap"],
    objectives=[("Describe Brookdale’s NETW sequence, certificate, and A.A.S. options.", 3),
                ("Explain NJ Transfer, NJ STARS, and articulation agreements.", 3),
                ("Compare self-study, bootcamps, and community college.", 3),
                ("Build a stacked 6–18 month credential roadmap.", 6)],
    explore=f"""<div class="prose"><h3>Brookdale’s NETW options</h3>
<p>Brookdale offers the <b>Network and Information Technology (NTIT) A.A.S.</b> degree and a <b>Cybersecurity</b> certificate. NETW courses include Linux administration, automation, containers, Windows endpoint and hybrid server administration, and perimeter security, and many are built around industry certifications. The college catalog is the official source for the current sequence; your advisor can confirm what applies to you.</p>
<h3>Transfer</h3>
<p><span class="term">NJ Transfer</span> shows how Brookdale courses transfer to New Jersey four-year schools. <span class="term">NJ STARS</span> is a state scholarship program for high-achieving New Jersey students that can continue at a four-year school. <span class="term">Articulation agreements</span> are deals between colleges that guarantee how credits transfer. Remember from Week 1: BLS lists a bachelor’s degree as the typical entry education for information security analysts, so many students plan an A.A.S. now and a bachelor’s later, often while working.</p>
<h3>The certification map</h3>
<p>Four organizations show up in most entry-level postings: <b>CompTIA</b> (A+, Network+, Security+, CySA+), <b>Cisco</b> (CCST, CCNA), <b>ISC2</b> (CC, then CISSP for experienced professionals), and <b>EC-Council</b> (CEH, an ethical hacking certification). Cloud providers (Microsoft, AWS, Google) and Red Hat have their own tracks.</p></div>
<div class="table-wrap"><table>
<caption class="visually-hidden">Comparing three ways to learn</caption>
<thead><tr><th scope="col">Path</th><th scope="col">Cost</th><th scope="col">Structure and support</th><th scope="col">Credential</th></tr></thead>
<tbody>
<tr><th scope="row">Self-study</th><td>Lowest: free videos plus exam vouchers</td><td>All on you. Works well for disciplined learners.</td><td>Certifications only</td></tr>
<tr><th scope="row">Bootcamp</th><td>Often several thousand dollars or more</td><td>Fast and intense; quality varies widely. Ask for verified job placement data.</td><td>Certificate of completion, sometimes cert prep</td></tr>
<tr><th scope="row">Community college</th><td>Moderate; financial aid eligible</td><td>Instructors, labs, advising, tutoring, transfer paths</td><td>College credit, certificates, A.A.S., plus cert prep</td></tr>
</tbody></table></div>
<div class="prose"><h3>Stacking credentials</h3>
<p>Stacking means each credential builds on the last and each one is useful by itself. A common support-to-security stack: A+ in the first semester, Network+ in the second, Security+ by the end of the first year, while earning college credit and getting a help desk job. Pick a 6–18 month horizon: long enough to make progress, short enough to stay real.</p></div>
{callout("A note on the free ISC2 CC program", "<p>ISC2’s One Million Certified in Cybersecurity program ended for new enrollments on May 20, 2026. If you already have a voucher, you have until December 31, 2026 to test. Check the ISC2 CC page for current pricing.</p>", note=True)}""",
    do=[act("roadmap", "pf-roadmap", "Portfolio §4: Build your certification and education roadmap",
            "Check off what you plan to do and choose when. Add your own steps at the bottom. The timeline updates as you go and appears in your portfolio.",
            ROADMAP, tag="Portfolio §4"),
        f"""<section class="act" aria-labelledby="w09-why-h"><span class="act-tag">Portfolio §4</span><h3 id="w09-why-h">Explain your roadmap</h3>
{field("pf-roadmap-why", "Portfolio §4: Why this order? How does it lead to your target role, and what could slow you down?", rows=6)}</section>""",
        f"""<section class="act" aria-labelledby="w09-cat-h"><span class="act-tag">Activity</span><h3 id="w09-cat-h">Catalog walkthrough</h3>
<p class="act-intro">Open the {ext("https://catalog.brookdalecc.edu/", "Brookdale catalog")} and search for NETW and the NTIT program.</p>
{field("w09-cat", "Which program fits you (certificate, A.A.S., or both)? List the first three NETW courses you would take.", rows=4)}</section>"""],
    investigate=dict(tag="Career Role Research Assignment 3", title="Pathway analysis for your target role", short="assignment",
        intro="<p>Pick your current target role (from Assignment 1, Assignment 2, or a new one). Find out exactly what education and credentials it takes to get there from where you are today.</p>",
        resources=[("Brookdale catalog", "https://catalog.brookdalecc.edu/", "Official program and course listings."),
                   ("NJ Transfer", "https://www.njtransfer.org/", "See how Brookdale courses transfer to four-year schools."),
                   ("Paul Jerimy Security Certification Roadmap", "https://pauljerimy.com/security-certification-roadmap/", "Find certifications for your role’s domain."),
                   ("CyberSeek career pathway", CYB_PATH, "Top certifications listed for your role."),
                   ("CISA NICCS: NICE Framework work roles", NICCS_NICE, "Look up your role’s knowledge and skills."),
                   ("ISC2 Certified in Cybersecurity", "https://www.isc2.org/certifications/cc", "Current details on the entry-level certification.")],
        steps=["Name your target role and its NICE work role.",
               "Find two current postings for it and list the education and certifications each requires or prefers.",
               "Check CyberSeek and the Paul Jerimy roadmap for the certifications most associated with it.",
               "Use NJ Transfer to find one four-year option that accepts Brookdale credits in a related field.",
               "Complete the fields below, save as PDF, and upload to Canvas."],
        fields=(field("w09-a3-role", "Target role and its NICE work role", kind="text") +
                job_cards("w09", 2) +
                field("w09-a3-certs", "Certifications most associated with this role (CyberSeek, roadmap, postings), and which one to earn first", rows=4) +
                field("w09-a3-edu", "Education needed: what Brookdale provides and what might come after (transfer option you found)", rows=4) +
                field("w09-a3-gap", "The biggest gap between where you are now and this role, and your plan to close it", rows=4)),
        grade="Career Role Research Assignments are 20% of the course total across three assignments.",
        submit=True),
    portfolio=f"""<p class="prose">Your roadmap and explanation above are Portfolio §4. Reflection Journal 3 is due in Week 12; preview the prompt now.</p>
{callout("Journal 3 preview", "<p>How has your idea of “someone who works in tech” changed? What barriers do you see for yourself, and what resources could help? You will write it in Week 12.</p>")}""",
    instructor=[("0–12 min", "Explore: Brookdale options, transfer, cert map, learning paths table."),
                ("12–20", "Catalog walkthrough live."),
                ("20–32", "Roadmap builder."),
                ("32–46", "Assignment 3 work time."),
                ("46–50", "Exit ticket; preview Journal 3.")],
    instructor_note="Course titles in the roadmap reflect pending Coursedog proposals. Update the ROADMAP list in build/unit3.py once the catalog changes are approved, and add NETW 107’s full title.",
)

W10 = dict(n=10, unit=3, title="Resume, LinkedIn, and online presence",
    lede="You may not have IT experience yet, but you have evidence. Learn what an entry-level IT resume looks like, set up LinkedIn, and turn labs and side projects into proof of skill.",
    due=["Portfolio §5: resume or LinkedIn draft"],
    objectives=[("Describe the structure of an entry-level IT resume.", 6),
                ("Write a LinkedIn headline, About section, and skills list.", 6),
                ("Rewrite weak resume bullets as specific, results-focused ones.", 6),
                ("Use labs, GitHub, and TryHackMe as portfolio evidence.", 6)],
    explore=f"""<div class="prose"><h3>Anatomy of an entry-level IT resume</h3>
<p>One page. Contact info and a LinkedIn link at the top. A two-line summary aimed at the role. A <b>skills</b> section with tools you have actually used. <b>Certifications</b> (including “in progress” with a target date). <b>Projects and labs</b> if you lack IT jobs. <b>Experience</b>, including non-IT jobs written to highlight transferable skills. <b>Education</b>.</p>
<h3>Bullets that work</h3>
<p>A strong bullet starts with an action verb, says what you did, and shows a result or scale: “Resolved 40+ customer issues per shift at a busy retail service desk, keeping satisfaction above 95%.” Weak bullets list duties: “Responsible for customer service.”</p>
<h3>LinkedIn</h3>
<p>Your <b>headline</b> is the line under your name. Make it about where you are heading: “Network & IT student at Brookdale | CompTIA A+ in progress | Help desk ready.” Your <b>About</b> section is a short, friendly version of your bio. Add skills recruiters search for, and keep a clear, professional photo.</p>
<h3>Proof of skill</h3>
<p>No experience? Build evidence. A home lab, a <span class="term">GitHub</span> repository with scripts or lab write-ups, and a public <span class="term">TryHackMe</span> profile showing completed rooms all count. A short write-up of what you did and learned matters more than the badge.</p>
<h3>Common mistakes</h3>
<p>Two pages of unrelated detail. Listing every tool you have heard of. Typos. An email like gamerkid2007@. A generic resume sent to every job. Social media posts you would not want an employer to see.</p></div>""",
    do=[act("choices", "w10-bullets", "Resume bullet makeover",
            "Which version of each bullet would catch a hiring manager’s eye?",
            {"label": "Bullet", "items": [
                {"q": "From a retail job:", "options": [{"t": "Responsible for helping customers", "fb": "Duty, not accomplishment."}, {"t": "Resolved 40+ customer issues per shift and trained 3 new hires on the point-of-sale system", "ok": True, "fb": "Specific, quantified, and shows troubleshooting and teaching."}, {"t": "Good with people", "fb": "A claim with no evidence."}]},
                {"q": "From a home lab:", "options": [{"t": "Built a home network lab with a router, switch, and two VLANs, and documented the setup on GitHub", "ok": True, "fb": "Names real skills and points to proof."}, {"t": "Know networking", "fb": "Too vague to believe."}, {"t": "Watched NetworkChuck videos", "fb": "Watching is a start; doing is what goes on a resume."}]},
                {"q": "From TryHackMe:", "options": [{"t": "Completed TryHackMe’s Pre Security path (networking, Linux, web basics); profile linked", "ok": True, "fb": "Clear, verifiable, relevant."}, {"t": "Hacker", "fb": "Unclear and may worry an employer."}, {"t": "Did some cyber stuff online", "fb": "Say what you did."}]},
                {"q": "From volunteering:", "options": [{"t": "Helped at church", "fb": "Say what you did and what changed."}, {"t": "Set up Wi-Fi and a shared printer for a 30-member community center and wrote a one-page guide for staff", "ok": True, "fb": "Real IT work, real users, documentation."}, {"t": "Volunteer, 2023", "fb": "No content."}]}]}),
        f"""<section class="act" aria-labelledby="w10-crit-h"><span class="act-tag">Peer critique</span><h3 id="w10-crit-h">Resume checklist</h3>
<p class="act-intro">Use this on your own draft or swap with a partner.</p>
{checks("Resume checklist", [("w10-c1", "Fits on one page"), ("w10-c2", "Professional email and a LinkedIn link"), ("w10-c3", "Summary names the target role"), ("w10-c4", "Every bullet starts with an action verb"), ("w10-c5", "At least two bullets include a number"), ("w10-c6", "Skills list only includes tools I have used"), ("w10-c7", "Certifications in progress list a target date"), ("w10-c8", "No typos (read aloud or use a screen reader)")])}
{field("w10-crit", "Feedback received or given: one strength, one change", rows=3)}</section>"""],
    investigate=dict(tag="In-class research", title="Career Center and LinkedIn setup", short="research",
        intro="<p>Set up or update your LinkedIn profile in class, and find what Brookdale’s Career Center offers.</p>",
        resources=[("Brookdale Career Center", "https://www.brookdalecc.edu/career-center/", "Resume reviews, mock interviews, and job search help."),
                   ("Handshake for Brookdale students", "https://www.brookdalecc.edu/career-center/career-center-resources/handshake-for-students/", "Job and internship postings for students."),
                   ("LinkedIn Learning", "https://www.linkedin.com/learning/", "Many public libraries give free access with a library card. Check your county library."),
                   ("Simply Cyber on YouTube", "https://www.youtube.com/@SimplyCyber", "Search the channel for cybersecurity resume videos."),
                   ("TryHackMe", "https://tryhackme.com/", "A free account and public profile you can link from your resume."),
                   ("GitHub", "https://github.com/", "Free repositories for lab write-ups and scripts.")],
        steps=["Create or update your LinkedIn profile: photo, headline, About, skills.",
               "Find one Career Center service you will use this semester.",
               "Draft Portfolio §5 below."],
        fields=(field("w10-cc", "Career Center service I will use, and when", kind="text") +
                field("w10-li-url", "My LinkedIn profile link (optional)", kind="url", placeholder="https://www.linkedin.com/in/")),
        submit=False),
    portfolio=f"""<p class="prose">Portfolio §5 is a resume or LinkedIn draft tailored to one entry-level role. Draft the core pieces here.</p>
{field("pf-target-posting", "Portfolio §5: The entry-level role this is tailored to", kind="text")}
{field("pf-headline", "Portfolio §5: LinkedIn headline or resume summary line", kind="text", placeholder="e.g. IT student at Brookdale | CompTIA A+ in progress | Help desk ready")}
{field("pf-about", "Portfolio §5: About section or resume summary", rows=6, words="80-200")}
{field("pf-skills", "Portfolio §5: Skills list (tools and skills you have actually used)", rows=3)}
{field("pf-bullets", "Portfolio §5: Four to six resume bullets (one per line)", help="Use the action + what + result pattern. Include labs and non-IT jobs.", rows=8)}""",
    instructor=[("0–10 min", "Explore: resume anatomy, bullets, LinkedIn, proof of skill."),
                ("10–18", "Bullet makeover."),
                ("18–35", "Live LinkedIn setup."),
                ("35–46", "Draft §5 and peer critique checklist."),
                ("46–50", "Exit ticket.")],
)

W11 = dict(n=11, unit=3, title="Networking, mentorship, and the job search",
    lede="Many IT jobs are filled through people who know people. Learn how to build professional relationships, ask for informational interviews, and find events and competitions near you.",
    due=[],
    objectives=[("Distinguish professional networking from social networking.", 6),
                ("Write a professional LinkedIn connection message.", 6),
                ("Identify professional organizations, competitions, and events in NJ/NY.", 3),
                ("Plan an informational interview.", 6)],
    explore=f"""<div class="prose"><h3>Professional networking</h3>
<p>Professional networking is building relationships with people in your field before you need anything from them. It is not collecting connections. A good relationship starts with curiosity: ask people about their work, listen, and follow up.</p>
<h3>Informational interviews</h3>
<p>An <span class="term">informational interview</span> is a 15–20 minute conversation where you ask someone about their job. You are not asking for a job. People say yes more often than you would think, especially to students. Prepare questions, respect their time, and send a thank-you within a day.</p>
<h3>Professional organizations</h3></div>
{roles([("ISACA New Jersey", "<p>Audit, governance, risk, and compliance. Strong for GRC interests.</p>"),
        ("ISSA", "<p>Information Systems Security Association: chapters for security practitioners.</p>"),
        ("ISC2 chapters", "<p>Local chapters of the organization behind CC and CISSP.</p>"),
        ("OWASP", "<p>Open Worldwide Application Security Project: free meetups on web and application security.</p>")])}
<div class="prose"><h3>Competitions</h3>
<p><span class="term">Capture the flag (CTF)</span> events are security puzzles solved in teams. The <b>National Cyber League</b> runs seasons open to college students. The <b>Collegiate Cyber Defense Competition (CCDC)</b> has student teams defend networks against live attackers. <b>CyberPatriot</b> is for middle and high school students; college students can get involved as mentors, which is great experience to talk about in interviews.</p>
<h3>Mentors and internships</h3>
<p>A mentor is someone a few steps ahead who checks in with you over time. Mentors often come from informational interviews, professional organization meetings, or instructors. Internships and co-ops are the fastest way to get “experience” on a resume; Handshake and the Career Center list them.</p></div>""",
    do=[act("choices", "w11-msg", "Which connection message would you answer?",
            "You want to connect with a SOC analyst at a New Jersey hospital. Pick the best message.",
            {"label": "Option set", "items": [
                {"q": "Choose the message most likely to get a reply:", "options": [
                    {"t": "Hi, can you get me a job at your hospital?", "fb": "Asking for a job from a stranger puts them on the spot."},
                    {"t": "Hi Ms. Lopez, I’m a Brookdale student exploring SOC careers. I saw your post about the ISSA meeting. Would you be open to a 15-minute chat about how you got started? Thanks either way.", "ok": True, "fb": "Personal, specific, small ask, and easy to say yes or no."},
                    {"t": "(No message, just a connection request)", "fb": "Blank requests from strangers are often ignored."},
                    {"t": "Hello sir/madam, please accept my request and refer me for openings.", "fb": "Generic and transactional."}]}]}),
        f"""<section class="act" aria-labelledby="w11-draft-h"><span class="act-tag">Activity</span><h3 id="w11-draft-h">Draft your own connection message</h3>
<p class="act-intro">LinkedIn limits personal notes on connection requests, so aim for about 300 characters.</p>
{field("w11-msg", "Who you would contact (role and organization), and your message", rows=5)}</section>""",
        act("flip", "w11-ii", "Informational interview questions",
            "Flip each card for a tip on why the question works. Pick three to use.",
            {"labels": ["Question", "Why it works"], "cards": [
                {"f": "What does a typical week look like in your job?", "b": "Gets past job titles to the real work."},
                {"f": "How did you get your first job in this field?", "b": "Shows you realistic entry paths, not just ideal ones."},
                {"f": "Which skills do you use most that you didn’t learn in school?", "b": "Points you to what to practice on your own."},
                {"f": "Which certifications actually mattered when you were hired?", "b": "Separates required from nice-to-have."},
                {"f": "What do you wish you had known when you were starting out?", "b": "People love answering this, and it builds rapport."},
                {"f": "Is there anyone else you think I should talk to?", "b": "This is how one conversation turns into a network."}]}),
        f'{field("w11-ii-pick", "Three questions I would ask, and who I would ask", rows=4)}'],
    investigate=dict(tag="In-class research", title="One organization, one event", short="research",
        intro="<p>Research one professional organization and find one upcoming IT or cybersecurity event in New Jersey or New York you could attend.</p>",
        resources=[("ISACA New Jersey Chapter", "https://engage.isaca.org/newjerseychapter/home", "Events and student membership."),
                   ("ISSA International", "https://issa.org/", "Find a chapter near you."),
                   ("ISC2 chapters", "https://isc2chapters.isc2.org/", "Local ISC2 chapter directory."),
                   ("OWASP", "https://owasp.org/", "Search for New Jersey or New York chapters."),
                   ("National Cyber League", "https://nationalcyberleague.org/", "College-level CTF seasons."),
                   ("Collegiate Cyber Defense Competition", "https://www.nationalccdc.org/", "Team network defense competition."),
                   ("CyberPatriot", "https://www.uscyberpatriot.org/", "Youth competition; look for mentor opportunities.")],
        steps=["Pick one organization and find its student membership cost and next meeting.",
               "Find one event (meetup, conference, CTF, career fair) within the next two months.",
               "Record what you found."],
        fields=(field("w11-org", "Organization: name, what it focuses on, student membership cost, next meeting", rows=4) +
                field("w11-event", "Event: name, date, location or online, cost, and why you want to go", rows=4)),
        submit=False),
    instructor=[("0–12 min", "Explore: networking, informational interviews, organizations, competitions."),
                ("12–24", "Message choice, then students draft their own."),
                ("24–32", "Informational interview cards."),
                ("32–46", "One organization, one event research."),
                ("46–50", "Exit ticket.")],
)

W12 = dict(n=12, unit=3, title="Diversity, equity, and inclusion in IT",
    lede="People from every background work in IT and cybersecurity, but some groups are still underrepresented. Explore the communities that support new professionals and practical ways to handle imposter syndrome.",
    due=["Reflection Journal 3", "Portfolio §6: final reflection begins"],
    objectives=[("Explain why representation in tech teams is discussed as a workforce issue.", 5),
                ("Identify professional communities and student support resources.", 3),
                ("Recognize imposter syndrome and practical ways to respond to it.", 6)],
    explore=f"""<div class="prose"><h3>Who works in tech</h3>
<p>Workforce studies consistently find that women and several racial and ethnic groups are underrepresented in cybersecurity compared with the overall workforce. People also enter the field later in life, from the military, from other careers, and as first-generation college students. Organizations discuss representation for several reasons: widening the talent pool during a worker shortage, fairness and access, and the argument that teams with different experiences anticipate a wider range of threats and users. People debate how much weight each reason deserves and which programs work best, and you will hear a range of views in the industry.</p>
<h3>Communities that help</h3></div>
{roles([("WiCyS", "<p>Women in CyberSecurity: student chapters, conference scholarships, mentoring.</p>"),
        ("NSBE", "<p>National Society of Black Engineers: chapters and career fairs, including tech.</p>"),
        ("BDPA", "<p>A technology organization focused on Black professionals and students in IT.</p>"),
        ("Blacks in Technology", "<p>Community, mentoring, and events for Black technologists.</p>")])}
<div class="prose"><p>Many other groups exist for veterans, Latino and Hispanic technologists, LGBTQ+ professionals, people with disabilities, and career changers. Most welcome allies and anyone interested.</p>
<h3>First-generation and returning students</h3>
<p>If you are the first in your family to go to college, or returning after years away, Brookdale has support for you: advising, tutoring, counseling, accessibility services, and more. Using support is what successful students do, not a sign that you don’t belong.</p>
<h3>Imposter syndrome</h3>
<p><span class="term">Imposter syndrome</span> is the feeling that you are a fraud and will be “found out,” even when you are doing fine. It is extremely common in IT because the field is huge and changes fast; even senior engineers look things up all day. Practical responses: keep a list of things you have learned, compare yourself with where you were last month rather than with experts, and say “I don’t know yet, but I’ll find out,” which is exactly what employers want to hear.</p></div>""",
    do=[act("choices", "w12-imposter", "Reframe the thought",
            "Each card is a common imposter-syndrome thought. Pick the most helpful reframe.",
            {"scored": False, "label": "Thought", "okLabel": "Helpful reframe.", "noLabel": "Less helpful.",
             "items": [{"q": "“Everyone in this class already knows more than me.”", "options": [{"t": "“Some do, some don’t. I know more than I did in Week 1, and that’s the comparison that counts.”", "ok": True}, {"t": "“I should drop the course.”", "fb": "One feeling isn’t evidence. Talk to the instructor or a classmate first."}, {"t": "“I’ll just stay quiet so nobody notices.”", "fb": "Asking questions is how you catch up, and others usually have the same question."}]},
                       {"q": "“I got the interview, but they’ll realize I’m not qualified.”", "options": [{"t": "“They picked me based on what I showed them. My job is to show how I learn and solve problems.”", "ok": True}, {"t": "“I’ll cancel the interview.”", "fb": "Every interview is practice, even if you don’t get the job."}, {"t": "“I’ll pretend I know everything.”", "fb": "Interviewers respect “I don’t know, but here’s how I’d find out” far more than bluffing."}]},
                       {"q": "“I had to look up how to do that. A real IT person would just know.”", "options": [{"t": "“Looking things up is the job. Knowing where to look is a skill.”", "ok": True}, {"t": "“I need to memorize everything before I apply anywhere.”", "fb": "Nobody can. The field changes too fast."}]}]}),
        f"""<section class="act" aria-labelledby="w12-barriers-h"><span class="act-tag">Discussion</span><h3 id="w12-barriers-h">Barriers in pursuing tech careers</h3>
<p class="act-intro">Write only what you are comfortable sharing. This stays in your browser unless you choose to save it as a PDF.</p>
{field("w12-barriers", "What barriers could make an IT career harder to reach for someone like you (time, cost, family, confidence, transportation, anything)? What is one resource that could help?", rows=5)}</section>"""],
    investigate=dict(tag="Reflection Journal 3", title="Find a community, then reflect", short="journal",
        intro="<p>Research one professional community connected to your background or interests, then write Reflection Journal 3.</p>",
        resources=[("WiCyS", "https://www.wicys.org/", "Women in CyberSecurity."),
                   ("Blacks in Technology", "https://www.blacksintechnology.net/", "Community and mentoring."),
                   ("NSBE", "https://www.nsbe.org/", "National Society of Black Engineers."),
                   ("BDPA", "https://bdpa.org/", "Technology organization and student programs."),
                   ("Brookdale student support", "https://www.brookdalecc.edu/support/", "Advising, counseling, accessibility, and more."),
                   ("Brookdale tutoring", "https://www.brookdalecc.edu/academic-tutoring/", "Free tutoring for all students.")],
        steps=["Pick one community above or another you find, and look at its student offerings.",
               "Find one Brookdale support service you might use.",
               "Write Reflection Journal 3 (250–350 words).",
               "Save as PDF and upload to Canvas."],
        fields=(field("w12-community", "The community I researched: what it offers students and how to join", rows=3) +
                field("w12-support", "One Brookdale support service I might use, and for what", kind="text") +
                field("w12-journal", "Reflection Journal 3",
                      help="Prompt: How has your picture of “someone who works in tech” changed this semester? What barriers do you see for yourself, and which resources or communities could help? What is one thing you will do in the next month?",
                      rows=12, words="250-350")),
        grade="Reflection journals are 15% of the course total across three entries.",
        submit=True),
    portfolio=f"""<p class="prose">Start Portfolio §6, your final reflection (400–600 words). Draft freely now; you will finish it in Weeks 14–15. Look back at your Week 1 KWL chart and your journals for material.</p>
{field("pf-reflection", "Portfolio §6: Final reflection on the course and your career intentions", help="What did you learn about the field and yourself? Which roles are you aiming for and why? What is your plan for the next 6–18 months? What will you do if your plans change?", rows=16, words="400-600")}""",
    instructor=[("0–12 min", "Explore: representation, communities, first-gen resources."),
                ("12–22", "Imposter syndrome reframes."),
                ("22–30", "Barriers discussion: offer pass options; keep it voluntary."),
                ("30–46", "Community research and Journal 3."),
                ("46–50", "Introduce Portfolio §6.")],
    instructor_note="Keep the barriers discussion opt-in. Students can share in small groups or not at all.",
)

WEEKS = [W9, W10, W11, W12]
