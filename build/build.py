import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from lib import *
import unit1, unit2, unit3, unit4
from unit2 import role_analysis, PATHWAY
from unit3 import ROADMAP

OUT = os.path.join(os.path.dirname(__file__), "..")
WEEKS = unit1.WEEKS + unit2.WEEKS + unit3.WEEKS + unit4.WEEKS
TITLES = [w["title"] for w in WEEKS]
SHORT = ["Orientation", "IT career family", "How networks work", "Security, ethics", "Help desk",
         "Networking careers", "SOC, GRC, pen test", "Cloud and AI", "Pathways and certs", "Resume and LinkedIn",
         "Networking and jobs", "DEI in IT", "Future of IT", "Portfolio polish", "Presentations"]

def write(rel, text):
    p = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(text)

# ---------- Week pages ----------
for w in WEEKS:
    write(f"weeks/week-{w['n']:02d}.html", week_page(w, TITLES))

# ---------- Home: route map ----------
def routemap():
    xs = [80, 235, 390, 545]
    rows = [70, 185, 300, 415]
    pos = {}
    for i in range(4): pos[i + 1] = (xs[i], rows[0])
    for i in range(4): pos[i + 5] = (xs[3 - i], rows[1])
    for i in range(4): pos[i + 9] = (xs[i], rows[2])
    for i in range(3): pos[i + 13] = (xs[3 - i], rows[3])
    paths = [
        ("u1", f"M80,{rows[0]} H545"),
        ("u2", f"M545,{rows[0]} C640,{rows[0]} 640,{rows[1]} 545,{rows[1]} H80"),
        ("u3", f"M80,{rows[1]} C8,{rows[1]} 8,{rows[2]} 80,{rows[2]} H545"),
        ("u4", f"M545,{rows[2]} C640,{rows[2]} 640,{rows[3]} 545,{rows[3]} H150"),
    ]
    out = ['<svg viewBox="0 0 660 470" role="group" aria-label="Course route map: 15 weeks in four units. Each station links to its week.">']
    for cls, d in paths:
        out.append(f'<path class="rm-line {cls}" d="{d}"/>')
    out.append('<text class="rm-unit u1" x="66" y="32">Unit 1: Career landscape</text>')
    out.append('<text class="rm-unit u2" x="590" y="150" text-anchor="end">Unit 2: Roles deep dive</text>')
    out.append('<text class="rm-unit u3" x="66" y="265">Unit 3: Career readiness</text>')
    out.append('<text class="rm-unit u4" x="590" y="380" text-anchor="end">Unit 4: Future and portfolio</text>')
    for n in range(1, 16):
        x, y = pos[n]
        label = esc(SHORT[n - 1])
        out.append(f'<g class="rm-st" data-week="w{n:02d}"><a href="weeks/week-{n:02d}.html" aria-label="Week {n}: {esc(TITLES[n-1])}">'
                   f'<circle cx="{x}" cy="{y}" r="15"/><text class="num" x="{x}" y="{y+4}" text-anchor="middle">{n}</text>'
                   f'<text class="lbl" x="{x}" y="{y+36}" text-anchor="middle">{label}</text></a></g>')
    out.append(f'<g class="rm-term"><a href="portfolio.html" aria-label="Destination: your Career Exploration Portfolio">'
               f'<rect x="14" y="{rows[3]-20}" width="122" height="40" rx="8"/>'
               f'<text x="75" y="{rows[3]+5}" text-anchor="middle">Your portfolio</text></a></g>')
    out.append("</svg>")
    return "".join(out)

CLOS = ["Describe the landscape of IT, networking, and cybersecurity careers using the NIST NICE Framework, including typical roles, responsibilities, and entry requirements.",
        "Explain fundamental concepts in computer networking and cybersecurity at a conceptual, non-technical level suitable for informed career decision-making.",
        "Identify and compare educational pathways, including certificates, associate degrees, and industry certifications (CompTIA, Cisco, ISC2), aligned to personal career goals.",
        "Evaluate regional and national labor market data, including salary ranges, job demand, and growth projections for IT and cybersecurity roles.",
        "Apply ethical reasoning to real-world scenarios involving privacy, authorization, professional responsibility, and the acceptable use of technology.",
        "Produce a Career Exploration Portfolio documenting personal learning, career interests, and a personalized professional development roadmap."]

units_html = "".join(
    f'<li class="u{u}"><h3>{UNITS[u][0]}: {UNITS[u][1]}</h3><ol start="{[1,5,9,13][u-1]}">' +
    "".join(f'<li><a href="weeks/week-{w["n"]:02d}.html">{w["title"]}</a></li>' for w in WEEKS if w["unit"] == u) +
    "</ol></li>" for u in range(1, 5))

home = f"""<section class="home-hero" aria-labelledby="home-h">
  <div>
    <p class="course-code">NETW 100, 1 credit, no experience needed</p>
    <h1 id="home-h">Find your route into IT and cybersecurity</h1>
    <p class="lede">Fifteen weekly stops, from what IT people actually do to a career plan you build yourself. Every week has a short reading, hands-on activities, and research with real job data. By the end you will have a Career Exploration Portfolio and a next step.</p>
    <div class="btn-row">
      <a class="btn btn-primary" id="continue" href="weeks/week-01.html">Start Week 1</a>
      <a class="btn" href="portfolio.html">Open my portfolio</a>
    </div>
  </div>
  <figure class="routemap" style="margin:0">
    {routemap()}
    <figcaption class="legend"><span><i aria-hidden="true"></i>Not started</span><span><i class="p" aria-hidden="true"></i>In progress</span><span><i class="d" aria-hidden="true"></i>Every part marked done</span></figcaption>
  </figure>
</section>

<h2>How each week works</h2>
<div class="cols cols-3">
  <div class="panel"><h3 style="margin-top:0">Explore, Do, Investigate</h3><p>Read a short primer, work through interactive activities in class, then use real resources such as CyberSeek and the BLS to research and answer questions.</p></div>
  <div class="panel"><h3 style="margin-top:0">Your work saves as you go</h3><p>Answers are saved in this browser only, on this device. Nothing is sent anywhere. Download a backup from <a href="my-work.html">My work</a> to move between computers.</p></div>
  <div class="panel"><h3 style="margin-top:0">Submit as PDF</h3><p>Assignments, journals, and the portfolio each have a “Save as PDF” button. Pick “Save as PDF” in the print window, then upload the file to Canvas.</p></div>
</div>

<h2>Your portfolio so far</h2>
<p class="prose">The Career Exploration Portfolio builds across the semester. Draft due Week 13, final due Week 14, presentation Week 15.</p>
<ul class="pf-progress" id="pf-progress"></ul>
<p><a href="portfolio.html">Work on my portfolio</a></p>

<h2>Four units</h2>
<ul class="unit-list">{units_html}</ul>

<h2>Course learning outcomes</h2>
<p class="prose">When you finish NETW 100 you will be able to:</p>
<ol class="prose">{''.join(f'<li>{c}</li>' for c in CLOS)}</ol>"""
write("index.html", shell("Weeks", "NETW 100 Explore IT & Cyber Careers: a free, interactive, week-by-week course site for exploring IT, networking, and cybersecurity careers at Brookdale Community College.", "home", "", home, "home"))

# ---------- Schedule ----------
TOPICS = ["Course overview; what IT, network, and security pros do; workforce data; NICE Framework; Brookdale NETW overview",
          "Role families; day in the life; entry vs mid vs senior; pay and outlook; transferable skills",
          "LANs, WANs, the internet; routers, switches, firewalls; IP and DNS; cloud vs on-premises",
          "CIA triad; phishing, malware, ransomware, social engineering; MFA, firewalls, VPNs, backups; ethics",
          "Help desk work, tools, escalation; CompTIA A+; help desk to sysadmin; job posting analysis",
          "Network admin vs engineer; Cisco and CompTIA paths; cloud networking; NJ/NY market",
          "SOC tiers; GRC; ethical hacking; Security+ and CySA+; NICE Protection and Defense vs Oversight and Governance",
          "Cloud roles; shared responsibility; IAM; GDPR, HIPAA, PCI DSS; AI’s impact",
          "Brookdale NETW sequence; NJ Transfer, NJ STARS; cert map; self-study vs bootcamp vs college; stacking",
          "Entry-level resume; LinkedIn; GitHub and labs; common mistakes; online conduct",
          "Professional networking; informational interviews; ISACA, ISSA, ISC2, OWASP; competitions; internships",
          "Representation in tech; professional communities; first-gen resources; imposter syndrome",
          "AI in cybersecurity; zero trust; quantum and post-quantum cryptography; IoT and OT; lasting skills",
          "Strong portfolios; elevator pitch; non-traditional backgrounds; interview questions; next NETW course",
          "Portfolio presentations; peer feedback; course debrief; continued learning"]
rows = "".join(
    f'<tr><td>{w["n"]}</td><td>{UNITS[w["unit"]][0]}</td><td><a href="weeks/week-{w["n"]:02d}.html">{w["title"]}</a></td><td>{TOPICS[w["n"]-1]}</td><td>{"<br>".join(w.get("due", [])) or "None"}</td></tr>'
    for w in WEEKS)
sched = f"""<h1>Schedule</h1>
<p class="lede">One 50-minute session per week for 15 weeks. Topics are a guide; your instructor may adjust depth based on class questions.</p>
<div class="table-wrap"><table>
<caption class="visually-hidden">Week-by-week schedule</caption>
<thead><tr><th scope="col">Week</th><th scope="col">Unit</th><th scope="col">Session</th><th scope="col">Key topics</th><th scope="col">Due</th></tr></thead>
<tbody>{rows}</tbody></table></div>
<h2>How your work is weighted</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Component</th><th scope="col">Weight</th><th scope="col">When</th></tr></thead>
<tbody>
<tr><td>Weekly participation and in-class activities</td><td>20%</td><td>Every week</td></tr>
<tr><td>Career Role Research Assignments (3)</td><td>20%</td><td>Weeks 5, 7, 9</td></tr>
<tr><td>Reflection Journals (3)</td><td>15%</td><td>Weeks 4, 8, 12</td></tr>
<tr><td>Quizzes (2, open-note)</td><td>15%</td><td>Weeks 4 and 8</td></tr>
<tr><td>Career Exploration Portfolio</td><td>20%</td><td>Draft Week 13, final Week 14</td></tr>
<tr><td>Final presentation (3–5 minutes)</td><td>10%</td><td>Week 15</td></tr>
</tbody></table></div>
<p class="prose">NETW 100 is graded Credit / No Credit. A final score of 70% or higher earns Credit (P). Check Canvas and the syllabus for the official policies, due dates, and rubrics.</p>"""
write("schedule.html", shell("Schedule", "Week-by-week schedule and grading for NETW 100.", "schedule", "", sched, "schedule"))

# ---------- Portfolio ----------
def pf_sec(n, title, src, inner):
    return (f'<section class="pf-sec" data-export-h="§{n} {title}" aria-labelledby="pf{n}-h">'
            f'<h2 id="pf{n}-h">§{n} {title}</h2><p class="pf-from">{src} <span class="pf-status" data-pf-status="{n}"></span></p>{inner}</section>')

portfolio = f"""<h1>Career Exploration Portfolio</h1>
<p class="lede">Your capstone, built week by week. Anything you write here also updates the matching box on its week page, and the other way around.</p>
<div class="panel"><p>Draft due <b>Week 13</b>. Final due <b>Week 14</b>. Present highlights in <b>Week 15</b>. When you are ready, save the whole portfolio as one PDF at the bottom of this page.</p></div>
{pf_sec(1, "Professional introduction and bio", 'Started in <a href="weeks/week-02.html">Week 2</a>. About one page.',
        field("pf-bio", "§1 Professional bio", help="Who you are, what you have done, the skills you bring, and what draws you to IT. Look at your Week 1 interest survey and Week 2 transferable skills for material.", rows=14, words="250-450"))}
{pf_sec(2, "Two NICE work role analyses", 'From Career Role Research Assignments 1 and 2 (<a href="weeks/week-05.html">Week 5</a>, <a href="weeks/week-07.html">Week 7</a>).',
        role_analysis("pf-r1", 1) + '<details class="more"><summary>Job postings for role analysis #1 (from Week 5)</summary>' + job_cards("w05", 3) + '</details>' +
        role_analysis("pf-r2", 2) + '<details class="more"><summary>Job postings for role analysis #2 (from Week 7)</summary>' + job_cards("w07", 2) + '</details>')}
{pf_sec(3, "Annotated CyberSeek career pathway", 'From <a href="weeks/week-08.html">Week 8</a>.',
        act("rating", "pf-pathway", "§3 My annotated CyberSeek pathway", "Rate each role 0–5 and add a note from its CyberSeek profile.", PATHWAY, tag="Portfolio §3") +
        field("pf-pathway-notes", "§3 Overall notes on the pathway", rows=5))}
{pf_sec(4, "Certification and education roadmap", 'From <a href="weeks/week-09.html">Week 9</a>. A 6–18 month plan.',
        act("roadmap", "pf-roadmap", "§4 My roadmap", "Check off courses, certifications, and experiences, and choose when.", ROADMAP, tag="Portfolio §4") +
        field("pf-roadmap-why", "§4 Why this order? How does it lead to your target role, and what could slow you down?", rows=6))}
{pf_sec(5, "Resume or LinkedIn draft", 'From <a href="weeks/week-10.html">Week 10</a>. Tailored to one entry-level role.',
        field("pf-target-posting", "§5 The entry-level role this is tailored to", kind="text") +
        field("pf-headline", "§5 LinkedIn headline or resume summary line", kind="text") +
        field("pf-about", "§5 About section or resume summary", rows=6, words="80-200") +
        field("pf-skills", "§5 Skills list", rows=3) +
        field("pf-bullets", "§5 Resume bullets (one per line)", rows=8))}
{pf_sec(6, "Final reflection", 'Started in <a href="weeks/week-12.html">Week 12</a>. 400–600 words.',
        field("pf-reflection", "§6 Final reflection on the course and your career intentions", help="What did you learn about the field and yourself? Which roles are you aiming for and why? What is your plan for the next 6–18 months?", rows=16, words="400-600"))}
<section class="pf-sec" data-export-h="AI use disclosure" aria-labelledby="pf-ai-h"><h2 id="pf-ai-h">AI use disclosure</h2>
{field("pf-ai-note", "How I used AI tools, if at all", help="AI tools may help you brainstorm or edit, not write the portfolio for you. Name the tool and how you used it, or write “None.”", rows=3)}
</section>
<section class="panel" aria-labelledby="pf-save-h"><h2 id="pf-save-h" style="margin-top:0">Save your portfolio as PDF</h2>
{name_field()}
{export_btn(".pf-sec", "NETW 100 Career Exploration Portfolio", "Save my portfolio as PDF")}
</section>"""
write("portfolio.html", shell("Portfolio", "Build and save your NETW 100 Career Exploration Portfolio.", "portfolio", "", portfolio, "portfolio"))

# ---------- Resources ----------
R = [("Career and labor market data", [
        ("CyberSeek heat map", "https://www.cyberseek.org/heatmap.html", "Cybersecurity job postings and workers by state and metro."),
        ("CyberSeek career pathway", "https://www.cyberseek.org/pathway.html", "Feeder through advanced roles with salaries, certifications, and skills."),
        ("BLS Occupational Outlook Handbook: Computer and IT", "https://www.bls.gov/ooh/computer-and-information-technology/home.htm", "Pay, education, and 10-year outlook."),
        ("BLS state wage data: New Jersey", "https://www.bls.gov/oes/current/oes_nj.htm", "Occupational employment and wages for New Jersey."),
        ("CISA NICCS Cyber Career Pathways Tool", "https://niccs.cisa.gov/tools/cyber-career-pathways-tool", "Interactive map of NICE work roles and how they connect."),
        ("World Economic Forum: Future of Jobs Report 2025", "https://www.weforum.org/publications/the-future-of-jobs-report-2025/", "Global trends in jobs and skills."),
        ("ISC2 research", "https://www.isc2.org/research", "Cybersecurity Workforce Study and other reports.")]),
     ("NICE Framework", [
        ("NIST NICE Framework Resource Center", "https://www.nist.gov/itl/applied-cybersecurity/nice/nice-framework-resource-center", "Official home of the framework."),
        ("NICE Framework current versions", "https://www.nist.gov/itl/applied-cybersecurity/nice/nice-framework-resource-center/nice-framework-current-versions", "Download the current components."),
        ("CISA NICCS: NICE Framework work roles", "https://niccs.cisa.gov/tools/nice-framework", "Searchable work roles with tasks, knowledge, and skills."),
        ("NICE free and low-cost online learning content", "https://www.nist.gov/itl/applied-cybersecurity/nice/resources/online-learning-content", "NIST’s curated training list.")]),
     ("Certifications", [
        ("CompTIA A+", "https://www.comptia.org/en-us/certifications/a/", "Entry-level IT support."),
        ("CompTIA Network+", "https://www.comptia.org/en-us/certifications/network/", "Vendor-neutral networking."),
        ("CompTIA Security+", "https://www.comptia.org/en-us/certifications/security/", "Baseline security certification."),
        ("CompTIA CySA+", "https://www.comptia.org/en-us/certifications/cybersecurity-analyst/", "Security analyst certification."),
        ("ISC2 Certified in Cybersecurity (CC)", "https://www.isc2.org/certifications/cc", "Entry-level security certification."),
        ("Microsoft Azure Fundamentals (AZ-900)", "https://learn.microsoft.com/en-us/credentials/certifications/azure-fundamentals/", "Entry-level cloud certification."),
        ("Paul Jerimy Security Certification Roadmap", "https://pauljerimy.com/security-certification-roadmap/", "Hundreds of certifications by domain and level.")]),
     ("Free learning", [
        ("Professor Messer", "https://www.professormesser.com/", "Free A+, Network+, and Security+ video courses."),
        ("Cisco Networking Academy", "https://www.netacad.com/", "Free and low-cost Cisco courses."),
        ("Cisco NetAcad: Introduction to Cybersecurity", "https://www.netacad.com/courses/introduction-to-cybersecurity", "Free beginner course with a badge."),
        ("Cisco NetAcad: Networking Basics", "https://www.netacad.com/courses/networking-basics", "Free beginner networking course."),
        ("TryHackMe", "https://tryhackme.com/", "Browser-based security labs. Free account required for this course."),
        ("Fortinet Training Institute", "https://training.fortinet.com/", "Free self-paced security courses."),
        ("AWS Skill Builder", "https://skillbuilder.aws/", "Free AWS training."),
        ("Microsoft Learn career paths", "https://learn.microsoft.com/en-us/training/career-paths/", "Role-based learning paths."),
        ("Cloudflare Learning Center: DNS", "https://www.cloudflare.com/learning/dns/what-is-dns/", "Clear explainers on how the internet works.")]),
     ("Security awareness and policy", [
        ("Google Phishing Quiz", "https://phishingquiz.withgoogle.com/", "Practice spotting phishing."),
        ("CISA: Recognize and report phishing", "https://www.cisa.gov/secure-our-world/recognize-and-report-phishing", "Plain-language guidance."),
        ("CISA cybersecurity best practices", "https://www.cisa.gov/topics/cybersecurity-best-practices", "MFA, updates, passwords, and more."),
        ("CISA Zero Trust Maturity Model", "https://www.cisa.gov/zero-trust-maturity-model", "The five pillars of zero trust."),
        ("NIST post-quantum cryptography", "https://csrc.nist.gov/projects/post-quantum-cryptography", "The new encryption standards."),
        ("PCI Security Standards Council", "https://www.pcisecuritystandards.org/", "Payment card security standards."),
        ("European Commission: data protection (GDPR)", "https://commission.europa.eu/law/law-topic/data-protection_en", "Official EU privacy law information.")]),
     ("Videos", [
        ("Simply Cyber", "https://www.youtube.com/@SimplyCyber", "Career guidance and SOC operations."),
        ("NetworkChuck", "https://www.youtube.com/@NetworkChuck", "Networking and Linux fundamentals."),
        ("Computerphile", "https://www.youtube.com/@Computerphile", "Computer science explained, including encryption.")]),
     ("Professional organizations and competitions", [
        ("ISACA New Jersey Chapter", "https://engage.isaca.org/newjerseychapter/home", "Audit, governance, and risk."),
        ("ISSA", "https://issa.org/", "Information Systems Security Association."),
        ("ISC2 chapters", "https://isc2chapters.isc2.org/", "Local ISC2 chapters."),
        ("OWASP", "https://owasp.org/", "Application security community."),
        ("WiCyS", "https://www.wicys.org/", "Women in CyberSecurity."),
        ("Blacks in Technology", "https://www.blacksintechnology.net/", "Community and mentoring."),
        ("NSBE", "https://www.nsbe.org/", "National Society of Black Engineers."),
        ("BDPA", "https://bdpa.org/", "Technology organization and student programs."),
        ("National Cyber League", "https://nationalcyberleague.org/", "College CTF competition."),
        ("Collegiate Cyber Defense Competition", "https://www.nationalccdc.org/", "Team network defense."),
        ("CyberPatriot", "https://www.uscyberpatriot.org/", "Youth competition; mentor opportunities."),
        ("Simply Cyber community", "https://simplycyber.io/", "Career community and Discord.")]),
     ("Brookdale and New Jersey", [
        ("Brookdale catalog", "https://catalog.brookdalecc.edu/", "Programs and courses."),
        ("Brookdale Career Center", "https://www.brookdalecc.edu/career-center/", "Resumes, interviews, job search."),
        ("Handshake for Brookdale students", "https://www.brookdalecc.edu/career-center/career-center-resources/handshake-for-students/", "Jobs and internships."),
        ("Brookdale student support", "https://www.brookdalecc.edu/support/", "Advising, counseling, accessibility, and more."),
        ("Brookdale tutoring", "https://www.brookdalecc.edu/academic-tutoring/", "Free tutoring."),
        ("NJ Transfer", "https://www.njtransfer.org/", "How credits transfer in New Jersey.")]),
     ("Job search", [
        ("LinkedIn Jobs", "https://www.linkedin.com/jobs/", "Search and filter by experience level."),
        ("Indeed", "https://www.indeed.com/", "Large job board."),
        ("LinkedIn Learning", "https://www.linkedin.com/learning/", "Often free with a public library card."),
        ("GitHub", "https://github.com/", "Host lab write-ups and scripts.")])]
res_html = "".join(f"<h2>{h}</h2>{res_list(items)}" for h, items in R)
resources = f"""<h1>Resources</h1>
<p class="lede">Every outside resource used in the course, in one place. All are free to use; some certifications cost money to take the exam.</p>
<p class="small muted">Links were last checked {VERIFIED}. Websites change; if a link breaks, search the organization’s name and tell your instructor.</p>
{res_html}"""
write("resources.html", shell("Resources", "Free resources for exploring IT, networking, and cybersecurity careers.", "resources", "", resources, "resources"))

# ---------- Glossary ----------
G = [("Access point", "Device that lets Wi-Fi devices join a wired network.", 3),
     ("Articulation agreement", "Agreement between colleges that guarantees how credits transfer.", 9),
     ("Authorization", "Permission from the owner to access or test a system. The line between ethical hacking and crime.", 4),
     ("Availability", "Systems and data are there when needed. Part of the CIA triad.", 4),
     ("Backup", "A copy of data kept separately so it can be restored after loss or ransomware.", 4),
     ("CIA triad", "Confidentiality, integrity, and availability: the three goals of security.", 4),
     ("Cloud", "Renting computing resources from a provider instead of owning servers.", 3),
     ("Confidentiality", "Only authorized people can see data. Part of the CIA triad.", 4),
     ("CTF (capture the flag)", "A security competition made of puzzles that hide a “flag” to find.", 11),
     ("CyberSeek", "Free tool showing cybersecurity job postings by location and career pathways.", 1),
     ("DevSecOps", "Building security into the process of developing and deploying software.", 8),
     ("DHCP", "Automatically assigns IP addresses to devices that join a network.", 3),
     ("DNS", "Domain Name System. Translates names like google.com into IP addresses.", 3),
     ("Escalation", "Handing a problem to a higher support tier with notes on what you tried.", 5),
     ("Feeder role", "A job, such as help desk or networking, that commonly leads into cybersecurity.", 2),
     ("Firewall", "Device or software that allows or blocks traffic based on rules.", 3),
     ("GDPR", "European Union privacy law covering EU residents’ personal data.", 8),
     ("GRC", "Governance, risk, and compliance: policies, risk management, and audits.", 7),
     ("HIPAA", "U.S. law protecting health information.", 8),
     ("IAM", "Identity and access management: who can sign in and what they can reach.", 8),
     ("Imposter syndrome", "Feeling like a fraud despite evidence of your ability.", 12),
     ("Informational interview", "A short conversation to learn about someone’s job, not to ask for one.", 11),
     ("Integrity", "Data is accurate and has not been tampered with. Part of the CIA triad.", 4),
     ("IP address", "A number that identifies a device on a network.", 3),
     ("LAN", "Local area network: devices connected in one location.", 3),
     ("Least privilege", "Giving each person only the access their job needs.", 8),
     ("Malware", "Any malicious software.", 4),
     ("Median", "The middle value: half are above and half below.", 1),
     ("MFA", "Multi-factor authentication: a second proof of identity beyond a password.", 4),
     ("NAT", "Network address translation: swaps private addresses for a public one at the router.", 3),
     ("NICE Framework", "NIST’s Workforce Framework for Cybersecurity, describing work roles by tasks, knowledge, and skills.", 1),
     ("NJ Transfer", "Website showing how New Jersey community college credits transfer.", 9),
     ("On-premises", "Servers and systems owned and run in an organization’s own building.", 3),
     ("PCI DSS", "Security standard for organizations that handle payment card data.", 8),
     ("Penetration testing", "Authorized simulated attacks to find weaknesses.", 7),
     ("Phishing", "Messages that trick people into clicking, opening, or revealing information.", 4),
     ("Post-quantum cryptography", "Encryption designed to resist attacks by future quantum computers.", 13),
     ("Ransomware", "Malware that encrypts files and demands payment.", 4),
     ("Responsible disclosure", "Reporting a security flaw privately to its owner and allowing time to fix it.", 4),
     ("Router", "Device that connects networks and chooses paths between them.", 3),
     ("Shared responsibility model", "In the cloud, the provider secures the platform and the customer secures what they put on it.", 8),
     ("SIEM", "Security information and event management: collects security events and creates alerts.", 7),
     ("SOC", "Security operations center: the team that monitors for and responds to attacks.", 7),
     ("Social engineering", "Manipulating people rather than technology to gain access.", 4),
     ("STAR method", "Situation, Task, Action, Result: a structure for interview stories.", 14),
     ("Switch", "Device that connects devices within a LAN.", 3),
     ("Ticketing system", "Software that tracks support requests from start to finish.", 5),
     ("VPN", "Virtual private network: an encrypted connection to a trusted network.", 4),
     ("WAN", "Wide area network: connects LANs across distances.", 3),
     ("Work role", "In the NICE Framework, a grouping of work defined by tasks, knowledge, and skills. Not the same as a job title.", 1),
     ("Zero trust", "Security model in which no user or device is trusted by default; every request is verified.", 13)]
gl = "".join(f'<dt>{t}</dt><dd>{d} <span class="wk">(<a href="weeks/week-{w:02d}.html">Week {w}</a>)</span></dd>' for t, d, w in G)
glossary = f"""<h1>Glossary</h1>
<p class="lede">Key terms from every week. Quizzes are open-note, so this page is fair game.</p>
<div class="field gloss-search"><label for="gloss-filter">Filter terms</label><input type="text" id="gloss-filter" autocomplete="off"></div>
<p class="small muted" id="gloss-count" aria-live="polite">{len(G)} terms</p>
<dl class="gloss">{gl}</dl>"""
write("glossary.html", shell("Glossary", "Glossary of IT, networking, and cybersecurity career terms.", "glossary", "", glossary, "glossary"))

# ---------- My work ----------
mywork = """<h1>My work</h1>
<div class="prose">
<p class="lede">Your answers, activity results, and portfolio are saved only in this browser, on this device. Nothing is sent anywhere.</p>
<p>That keeps your work private, but it stays behind if you switch computers, clear your browser data, or open the course inside Canvas instead of directly. A backup file solves all three: download one each week, keep it somewhere safe such as OneDrive, and restore it wherever you need it.</p>
</div>
<h2>What is saved in this browser</h2>
<div class="table-wrap"><table><thead><tr><th scope="col">Week</th><th scope="col">Parts marked done</th><th scope="col">Written answers</th><th scope="col">Activities started</th></tr></thead><tbody id="mw-rows"></tbody></table></div>
<div class="cols cols-3" style="margin-top:1.5rem">
<section class="panel" aria-labelledby="mw-b"><h2 id="mw-b" style="margin-top:0">Back up</h2><p>Download one file with everything.</p><button type="button" class="btn btn-primary" id="mw-backup">Download my backup</button></section>
<section class="panel" aria-labelledby="mw-r"><h2 id="mw-r" style="margin-top:0">Restore</h2>
<div class="field"><label for="mw-file">Backup file</label><input type="file" id="mw-file" accept=".json,application/json"></div>
<fieldset style="border:0;padding:0;margin:0 0 .6rem"><legend class="small">How to restore</legend>
<label class="small" style="display:block"><input type="radio" name="mw-mode" value="merge" checked> Merge with what is here (the backup wins where both have the same item)</label>
<label class="small" style="display:block"><input type="radio" name="mw-mode" value="replace"> Replace everything here with the backup</label></fieldset>
<button type="button" class="btn" id="mw-restore">Restore from backup</button></section>
<section class="panel" aria-labelledby="mw-d"><h2 id="mw-d" style="margin-top:0">Delete</h2><p>Remove all course data from this browser, for example on a library computer.</p>
<button type="button" class="btn" id="mw-delete">Delete all my course data</button>
<button type="button" class="btn" id="mw-delete-confirm" hidden>Yes, delete everything</button></section>
</div>
<p class="act-status" id="mw-msg" aria-live="polite"></p>"""
write("my-work.html", shell("My work", "Back up, restore, or delete your NETW 100 work saved in this browser.", "mywork", "", mywork, "mywork"))

print("Built", len(WEEKS), "weeks")
