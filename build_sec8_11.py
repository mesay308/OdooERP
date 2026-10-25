# -*- coding: utf-8 -*-
# Sections 8, 9, 10, 11 + Dock + Script

def fi(title, desc):
    return ('<div class="feat-item"><span class="feat-dot">●</span><div>'
            '<span class="feat-title">%s: </span><span class="feat-desc">%s</span></div></div>' % (title, desc))

def sec_head(n, title):
    return ('<div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;">'
            '<span class="sec-pill">%s</span><h2 class="sec-title">%s</h2></div><hr class="sec-rule">' % (n, title))

P = 'font-size:.84rem;color:#2C2C3E;line-height:1.65;'
H3 = "font-family:'Outfit',sans-serif;font-size:.92rem;font-weight:700;color:#1B1464;"
WRAP = 'padding:24px 16px;max-width:680px;margin:0 auto;'
DIV = '<div style="border-top:6px solid #F0F0FA;"></div>'

# ───────────── SECTION 8 ─────────────
industries = [
 ('8.1', 'Wholesale, Distribution &amp; Import/Export',
  'For general importers, FMCG distributors, building material suppliers, and regional traders.',
  [('Landed Cost Calculations', 'Accurately distribute import costs&mdash;such as maritime shipping, transit fees, customs duties, and local warehouse transport&mdash;directly onto the true unit cost of your goods.'),
   ('Multi-Warehouse Logistics', 'Manage central storage hubs in Addis Ababa alongside regional distribution stores across Ethiopia on one screen.'),
   ('Credit &amp; Wholesale Pricing', 'Set custom credit limits for wholesale distributors and manage tiered price lists for high-volume buyers.')]),
 ('8.2', 'Manufacturing &amp; Agro-Processing',
  'For factories, metal and wood workshops, food and beverage producers, and edible oil/flour mills.',
  [('Formula &amp; Recipe Control (BOM)', 'Define multi-level Bills of Materials to track the exact quantity of raw ingredients or parts needed for each batch.'),
   ('Production Floor Tracking', 'Monitor work orders at each station, measure machine runtimes, and track labor hours to determine accurate unit production costs.'),
   ('Scrap &amp; Waste Auditing', 'Log raw material waste and scrap during manufacturing runs to identify production bottlenecks and stop inventory leakage.')]),
 ('8.3', 'Construction, Engineering &amp; Contracting',
  'For general contractors, electro-mechanical firms, and specialized project service providers.',
  [('Project Milestone Tracking', 'Track project phases visually using Kanban boards and Gantt charts, ensuring site deliverables stay on schedule.'),
   ('Site Material Usage', 'Assign warehouse withdrawals and equipment usage directly to specific construction sites or project codes.'),
   ('Progress Invoicing', 'Bill clients automatically based on completed contract milestones, verified engineer timesheets, or percentage-of-completion agreements.')]),
 ('8.4', 'Retail Chains, Supermarkets &amp; Showrooms',
  'For electronics stores, fashion boutiques, supermarkets, and construction supply outlets.',
  [('Fast Point of Sale (POS)', 'Ring up sales quickly using barcode scanners, receipt printers, and touchscreen interfaces.'),
   ('Local Payment Support', 'Accept cash, Telebirr, CBE Birr, and card payments directly at the cash register.'),
   ('Uninterrupted Offline Selling', 'Continue making sales and printing receipts during network interruptions; the system syncs all records automatically once connectivity returns.')]),
 ('8.5', 'Professional Services, Consulting &amp; NGOs',
  'For audit firms, legal practices, consulting agencies, and non-profit organizations.',
  [('Budget &amp; Fund Accounting', 'Track grants, donor funds, and organizational expenditures against approved budget lines in real time.'),
   ('Timesheet &amp; Billing Management', 'Track billable consultant hours and generate professional client invoices with one click.'),
   ('Document &amp; Approval Control', 'Manage purchase approvals, vendor agreements, and internal payment vouchers digitally without paper trails.')]),
 ('8.6', 'Healthcare, Clinics &amp; Pharmaceuticals',
  'For private hospitals, specialty clinics, pharmacies, and pharmaceutical importers.',
  [('Expiry &amp; Batch/Lot Control', 'Track medications and medical supplies by batch numbers and expiration dates with automatic alerts before items expire.'),
   ('Direct POS Integration for Pharmacies', 'Issue compliant receipts and track shelf inventory instantly at retail medicine counters.'),
   ('Strict Stock Traceability', 'Maintain an unbroken audit trail for regulated supplies from customs arrival to patient dispensing.')]),
]
tabs = ''
panels = ''
for i, (num, name, intro, items) in enumerate(industries):
    act = ' active' if i == 0 else ''
    tabs += '<button class="ind-tab%s" data-tab="%d" onclick="showInd(%d)">%s&nbsp;%s</button>' % (act, i, i, num, name)
    panels += ('<div class="ind-panel%s" id="ind-%d"><p class="ind-panel-title">%s. %s</p>'
               '<p class="ind-panel-intro">%s</p>%s</div>' %
               (act, i, num, name, intro, ''.join(fi(t, d) for t, d in items)))

SEC8 = '<div id="sec8" class="doc-section" style="%s">%s' % (WRAP, sec_head(8, 'Industries Covered by Odoo ERP')) + \
 '<p style="' + H3 + 'margin-bottom:10px;">Built for the Realities of the Ethiopian Economy.</p>' + \
 '<p style="' + P + 'margin-bottom:14px;">One of Odoo&rsquo;s greatest strengths is its versatility. Whether you are moving imported goods through customs, running retail checkout counters, managing a production plant, or handling contracting projects, Odoo provides pre-configured workflows tailored to your sector:</p>' + \
 '<div class="ind-tabs">' + tabs + '</div>' + \
 '<div style="background:#fff;border:1px solid #E0E0EE;border-radius:8px;padding:12px 14px;">' + panels + '</div></div>' + DIV

# ───────────── SECTION 9 ─────────────
def phase(n, title, sub, body):
    return ('<div class="phase-step"><div class="phase-num">%s</div><div style="flex:1;min-width:0;">'
            '<p class="phase-title">Phase %s: %s</p><p class="phase-subtitle">%s</p>%s</div></div>' % (n, n, title, sub, body))

train = ('<div style="margin:6px 0 0 0;padding:8px 10px;background:#fff;border-radius:6px;border:1px solid #E0E0EE;">'
 '<div style="font-size:.78rem;color:#3A3A5A;line-height:1.5;margin-bottom:6px;">We do not deliver abstract lectures. We train your staff directly on their everyday tasks in Amharic and English:</div>'
 '<div style="font-size:.78rem;color:#3A3A5A;line-height:1.5;margin-bottom:4px;"><strong style="color:#1B1464;">&bull; Sales &amp; Cashiers:</strong> Ringing up sales, issuing receipts on touchscreen POS, and accepting Telebirr or cash.</div>'
 '<div style="font-size:.78rem;color:#3A3A5A;line-height:1.5;margin-bottom:4px;"><strong style="color:#1B1464;">&bull; Warehouse Staff:</strong> Scanning barcodes, receiving supplier shipments, issuing delivery slips, and taking stock counts.</div>'
 '<div style="font-size:.78rem;color:#3A3A5A;line-height:1.5;margin-bottom:4px;"><strong style="color:#1B1464;">&bull; Accountants:</strong> Generating VAT reports, matching vendor bills, reconciling bank statements, and checking profit sheets.</div>'
 '<div style="font-size:.78rem;color:#3A3A5A;line-height:1.5;"><strong style="color:#1B1464;">&bull; Executive Management:</strong> Tracking live operational dashboards, viewing financial reports, and approving purchase orders from mobile phones.</div></div>')

ph1 = ''.join([
 fi('On-Site Operational Walkthrough', 'Our business analysts visit your head office, shops, or warehouses in Addis Ababa and regional hubs to inspect daily routines.'),
 fi('Process Mapping', 'We document how items move from purchase orders to your shelves, how sales counters collect money, and how accountants file monthly VAT with the Ministry of Revenues (MOR).'),
 fi('Clear Project Blueprint', 'We establish user roles, approval levels, and project milestones in plain language. Work begins only after leadership reviews and approves the blueprint.')])
ph2 = ''.join([
 fi('Core Module Setup', 'We activate and tune your core applications (Accounting, Inventory, Sales, Purchase, HR, or Production) to mirror your exact operations.'),
 fi('Ethiopian Tax &amp; Compliance Setup', 'We configure VAT (15%), Withholding Tax rules, Ethiopian fiscal calendars, and connections to certified sales register machines or electronic invoicing tools.'),
 fi('Local Integrations', 'Our engineering team connects Odoo directly with local payment services like Telebirr, CBE Birr, or custom company databases.'),
 fi('Simulation &amp; Testing', 'We test everyday transactions&mdash;such as receiving an imported container, issuing a tax invoice, or running monthly payroll&mdash;inside a secure test system to ensure total accuracy before launch.')])
ph3 = ''.join([
 fi('Data Cleansing', 'We assist your team in organizing and verifying opening balances, customer contacts, supplier records, and inventory lists from Peachtree, Excel sheets, or paper records.'),
 fi('Accurate Data Import', 'We load your clean records into Odoo and reconcile them against your current financial statements to guarantee zero data loss.'),
 fi('Role-Based, In-Person Training', 'See details below.').replace('See details below.', '')]) 
# Role-based training: title with training box below
ph3 = ''.join([
 fi('Data Cleansing', 'We assist your team in organizing and verifying opening balances, customer contacts, supplier records, and inventory lists from Peachtree, Excel sheets, or paper records.'),
 fi('Accurate Data Import', 'We load your clean records into Odoo and reconcile them against your current financial statements to guarantee zero data loss.'),
 '<div class="feat-item"><span class="feat-dot">●</span><div style="min-width:0;"><span class="feat-title">Role-Based, In-Person Training:</span>' + train + '</div></div>'])
ph4 = ''.join([
 fi('Controlled Cutover', 'We schedule the final system switchover during low-activity windows (such as weekends or month-end closings) to protect customer service.'),
 fi('On-Site Floor Support', 'During the critical first two weeks of launch, Addis Tech engineers remain physically on-site at your offices to guide staff, resolve questions, and eliminate bottlenecks immediately.'),
 fi('Ongoing Support &amp; Maintenance', 'Once daily operations run smoothly, we transition your business into our local support service for regular system backups, performance updates, and ongoing technical assistance.')])

chips = ''
for t in ['Phase 1:<br>Discovery &amp; Blueprint', 'Phase 2:<br>Configuration &amp; Testing', 'Phase 3:<br>Data Transfer &amp; Training', 'Phase 4:<br>Go-Live &amp; On-Site Support']:
    chips += '<div style="background:#1B1464;color:#fff;border-radius:8px;padding:8px 6px;font-size:.7rem;font-weight:600;line-height:1.35;text-align:center;">%s</div>' % t

SEC9 = '<div id="sec9" class="doc-section" style="%s">%s' % (WRAP, sec_head(9, 'Implementation Approach &amp; Methodology')) + \
 '<p style="' + H3 + 'margin-bottom:10px;">A Practical, Step-by-Step Path to Business Transformation.</p>' + \
 '<div class="callout">Software alone will not transform a company; execution does.</div>' + \
 '<p style="' + P + 'margin-bottom:12px;">In Ethiopia, many software projects fail because external consultants apply rigid corporate templates that ignore local realities&mdash;such as manual store records, fluctuating internet connectivity, paper-based approval habits, and employee resistance to unfamiliar technology.</p>' + \
 '<p style="' + P + 'margin-bottom:18px;">Addis Tech uses a structured, phased implementation methodology built specifically for the Ethiopian business environment. We break every rollout into four straightforward phases to minimize business disruption, ensure full tax compliance, and guarantee your team adopts the system with confidence from day one.</p>' + \
 '<p style="' + H3 + 'margin-bottom:8px;">Our 4-Phase Implementation Framework</p>' + \
 '<div style="display:grid;grid-template-columns:1fr 1fr;gap:6px;margin-bottom:18px;">' + chips + '</div>' + \
 phase(1, 'Discovery &amp; Business Blueprint', 'Understanding how your business runs before configuring software.', ph1) + \
 phase(2, 'System Configuration &amp; Localization', 'Tailoring the system to match your daily workflow and local tax rules.', ph2) + \
 phase(3, 'Data Transfer &amp; Hands-On Staff Training', 'Cleaning your business records and empowering your employees.', ph3) + \
 phase(4, 'Go-Live &amp; On-Site Support', 'Ensuring a smooth, worry-free switchover with zero disruption to daily sales.', ph4) + \
 '<p style="' + H3 + 'margin:20px 0 4px;">Our Implementation Guarantees</p>' + \
 '<div class="tbl-wrap"><table><thead><tr><th style="width:34%;">Key Factor</th><th>What It Means for Your Business</th></tr></thead><tbody>' + \
 '<tr><td><strong>Phased Deployment</strong></td><td>Start with foundational modules (Accounting, Inventory, Sales) first. Once your staff is comfortable, we activate advanced tools like Manufacturing or CRM without disrupting operations.</td></tr>' + \
 '<tr><td><strong>Zero Data Loss</strong></td><td>Opening cash balances, customer debts, supplier payables, and physical stock counts are audited line-by-line before your old tools are retired.</td></tr>' + \
 '<tr><td><strong>Local Accountability</strong></td><td>You work directly with software engineers and consultants based in Addis Ababa who provide immediate, in-person assistance.</td></tr>' + \
 '</tbody></table></div></div>' + DIV

# ───────────── SECTION 10 ─────────────
team = [
 ('EA', 'Eyob Atnafu', 'Project Manager', '10+ Years',
  'Software Project Management | ERP Implementation | Software Development Lifecycle',
  'Leads overall project execution, timeline management, resource allocation, and risk mitigation. Ensures seamless coordination between client stakeholders and technical teams, maintaining strict adherence to deliverables, budget, and quality standards.'),
 ('MA', 'Mesay Alemayehu', 'Lead Business (Functional) Consultant', '12+ Years',
  'Business Process Reengineering (BPR) | Process Design | Change Management | Sales &amp; Supply Chain Optimization',
  'Audits existing client workflows to design optimized target processes. Leads functional blueprinting, change management, and end-user adoption, aligning supply chain, sales, and administrative operations with international ERP best practices.'),
 ('YT', 'Yohanis Taye', 'Lead Odoo Developer', '8+ Years',
  'Odoo Core Architecture | Custom Module Development | System Integration | Backend Engineering',
  'Spearheads technical customization, module configuration, and API integrations. Ensures system performance, clean code architecture, and tailored workflow logic designed specifically for complex operational demands.'),
 ('GM', 'Gashaw Mekonen', 'Accounting &amp; Finance Expert', '13+ Years, Certified Accountant &amp; Auditor',
  'Financial Advisory | Tax Compliance &amp; Reporting | Statutory Auditing | Cost Accounting',
  'Oversees financial localization, Chart of Accounts configuration, and tax rule setup (VAT, Withholding, MOR compliance). Ensures automated reconciliation, ledger accuracy, and complete audit readiness across financial workflows.'),
 ('BT', 'Belay Tadios', 'Senior DevOps Engineer', '6+ Years',
  'ERP Infrastructure &amp; Deployment | System Environment Setup | Database Security &amp; Optimization',
  'Architect of cloud and on-premise server environments. Responsible for system security, automated backups, high-availability architecture, network stability, and offline-online database synchronization.'),
]
cards = ''
for i, (ini, name, role, exp, expertise, impact) in enumerate(team, 1):
    cards += ('<div class="team-card" style="margin-bottom:10px;"><div class="team-avatar">%s</div><div style="flex:1;min-width:0;">'
      '<p class="team-name">%d. %s</p><p class="team-role">%s</p><span class="team-exp">Experience: %s</span>'
      '<p class="team-expertise-label">Core Expertise:</p><p class="team-expertise">%s</p>'
      '<p class="team-impact-label">Role &amp; Impact:</p><p class="team-impact">%s</p></div></div>' % (ini, i, name, role, exp, expertise, impact))

SEC10 = '<div id="sec10" class="doc-section" style="%s">%s' % (WRAP, sec_head(10, 'Project Team &amp; Governance Structure')) + \
 '<p style="' + P + 'margin-bottom:12px;">Depending on the project scale, complexity, and specific business requirements, Addis Tech deploys a dedicated, cross-functional team of seasoned domain specialists and software engineers. Our implementation approach bridges high-level business strategy with deep technical execution, combining direct functional expertise in Finance, Sales, and Supply Chain with hands-on technical mastery in Odoo ERP architecture and infrastructure setup.</p>' + \
 '<div class="callout"><strong style="font-style:normal;">Note on Team Allocation:</strong> The team members highlighted below represent our senior project leads and dedicated subject-matter experts assigned to oversee governance, strategy, and core delivery. Based on project scope and operational needs, each engagement is supported by an extended team comprising additional senior and junior functional consultants, software developers, QA engineers, data migration specialists, and on-site support staff to ensure comprehensive coverage across all project phases.</div>' + \
 '<p style="' + H3 + 'margin:16px 0 10px;">Key Senior Leadership &amp; Project Leads</p>' + cards + \
 '<p style="' + H3 + 'margin:20px 0 6px;">Extended Implementation &amp; Support Squad</p>' + \
 '<p style="' + P + 'margin-bottom:8px;">To ensure complete hands-on execution and seamless on-site support, each implementation team is scaled dynamically:</p>' + \
 fi('Senior &amp; Junior Functional Consultants', 'Conduct module-specific user training (in Amharic and English), handle day-to-day workflow configurations, and assist departments during initial go-live operations.') + \
 fi('Software &amp; Integration Developers', 'Assist with custom report building, data extraction scripts, interface tuning, and local payment gateway/hardware integrations.') + \
 fi('Data Migration &amp; Quality Analysts', 'Focus on cleansing, auditing, and loading historical records (opening balances, contacts, inventory counts) to guarantee zero data loss.') + \
 fi('On-Site Floor Support Technicians', 'Stationed directly at client headquarters, retail stores, or warehouse depots during launch windows to guide end-users and resolve issues instantly.') + \
 '</div>' + DIV

# ───────────── SECTION 11 ─────────────
def step(n, title, action, outcome):
    return ('<div class="next-step"><div class="next-step-header"><div class="next-step-num">%d</div>'
            '<p class="next-step-title">Step %d: %s</p></div>'
            '<p class="action-label">Action:</p><p class="action-text">%s</p>'
            '<p class="outcome-label">Outcome:</p><p class="outcome-text" style="margin-bottom:0;">%s</p></div>' % (n, n, title, action, outcome))

ICON_ADDR = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>'
ICON_MAIL = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></svg>'
ICON_TEL = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.11 12 19.79 19.79 0 0 1 1 4.11a2 2 0 0 1 2-2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>'
ICON_WA = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.4 8.4 0 0 1-12.4 7.4L3 20.5l1.7-5.4A8.4 8.4 0 1 1 21 11.5z"/></svg>'
ICON_WEB = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20"/></svg>'

def contact(icon, label, inner, href=None):
    tag = 'a' if href else 'div'
    h = ' href="%s"' % href if href else ''
    return ('<%s class="contact-item"%s><span class="contact-icon">%s</span><span><span style="display:block;font-size:.66rem;font-weight:700;color:#FFA600;text-transform:uppercase;letter-spacing:.05em;">%s</span>%s</span></%s>'
            % (tag, h, icon, label, inner, tag))

SEC11 = '<div id="sec11" class="doc-section" style="%s">%s' % (WRAP, sec_head(11, 'Next Steps &amp; Project Initiation')) + \
 '<p style="' + P + 'margin-bottom:12px;">Partnering with <strong>Addis Tech PLC</strong> ensures your organization transitions smoothly from fragmented, manual workflows to a unified, automated, and fully compliant Odoo ERP ecosystem. We are prepared to bring our deep industry expertise, hands-on functional engineering, and local tax compliance solutions to empower your business growth.</p>' + \
 '<p style="' + P + 'margin-bottom:14px;">To move forward and initiate your ERP transformation journey, we recommend the following four simple steps:</p>' + \
 '<p style="' + H3 + 'margin-bottom:10px;">Recommended Roadmap to Engagement</p>' + \
 step(1, 'Schedule an Executive Alignment &amp; Live Demo', 'Contact our consulting team to schedule an interactive, tailored Odoo ERP demonstration focused on your specific industry workflows (Finance, Supply Chain, Retail POS, or Manufacturing).', 'Experience how Odoo handles your everyday operational scenarios and local tax requirements in real time.') + \
 step(2, 'Comprehensive On-Site Business Assessment (Blueprint)', 'Our lead functional consultants and business analysts conduct a 1-to-2 day walkthrough of your office, store, or warehouse locations.', 'We map your existing processes, define custom module requirements, and produce a formal <strong>Business Requirements &amp; Scope Alignment Document</strong>.') + \
 step(3, 'Final Scope Approval &amp; Agreement Sign-Off', 'Review and sign the finalized Implementation Statement of Work (SOW), project milestones, timeline schedule, and warranty/support agreement.', 'Formal project authorization and reservation of dedicated senior technical resources.') + \
 step(4, 'Project Mobilization &amp; Phase 1 Discovery Kickoff', 'Official project launch meeting between your executive sponsors, project leads, and the Addis Tech implementation squad.', 'Immediate commencement of system setup, data preparation, and workflow configuration.') + \
 '<div id="contact" style="background:linear-gradient(160deg,#1B1464 0%,#0B0642 100%);border-radius:12px;padding:18px 14px;margin-top:20px;">' + \
 "<p style=\"font-family:'Outfit',sans-serif;font-size:1.05rem;font-weight:800;color:#fff;margin-bottom:6px;\">&#128222; Contact Us to Get Started Today</p>" + \
 '<p style="font-size:.8rem;color:rgba(240,240,255,.85);line-height:1.55;margin-bottom:14px;">Take the first step toward operational excellence and real-time financial control. Reach out to our team to arrange your initial consultation:</p>' + \
 contact(ICON_ADDR, 'Office Address', 'Addis Tech PLC, Addis Ababa, Ethiopia') + \
 contact(ICON_MAIL, 'Email', '<a href="mailto:info@addistechplc.com" style="color:#fff;">info@addistechplc.com</a> / <a href="mailto:sales@addistechplc.com" style="color:#fff;">sales@addistechplc.com</a>') + \
 contact(ICON_WA, 'WhatsApp (Primary Contact)', '<a href="https://wa.me/251911202265" target="_blank" rel="noopener" style="color:#fff;font-weight:700;">+251 91120 2265</a>') + contact(ICON_TEL, 'Phone', '<a href="tel:+251911505992" style="color:#fff;font-weight:700;">+251 911 505992</a>') + \
 contact(ICON_WEB, 'Website', '<a href="https://www.addistechplc.com" target="_blank" rel="noopener" style="color:#fff;">www.addistechplc.com</a>') + \
 '</div></div>'

# ───────────── DOCK / BACK-TOP ─────────────
BOTTOM_DOCK = '''
<div id="progress-bar"></div>
<div id="bottom-dock">
  <div class="dock-inner">
    <a class="dock-btn dock-cta" href="https://wa.me/251911202265" target="_blank" rel="noopener"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.4 8.4 0 0 1-12.4 7.4L3 20.5l1.7-5.4A8.4 8.4 0 1 1 21 11.5z"/></svg>WhatsApp +251 91120 2265</a>
    <a class="dock-btn" href="https://wa.me/251911202265?text=Hello%20Addis%20Tech%2C%20I%20would%20like%20to%20book%20an%20Odoo%20ERP%20demo." target="_blank" rel="noopener">Book Demo</a>
    <a class="dock-btn dock-top" href="#top" aria-label="Back to top"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M18 15l-6-6-6 6"/></svg></a>
  </div>
</div>
<button id="back-top" aria-label="Back to top" onclick="window.scrollTo({top:0,behavior:'smooth'})"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M18 15l-6-6-6 6"/></svg></button>
'''

SCRIPT = '''
<script>
(function(){
  var header=document.getElementById('sticky-header');
  var dock=document.getElementById('bottom-dock');
  var bar=document.getElementById('progress-bar');
  var backTop=document.getElementById('back-top');
  var chips=[].slice.call(document.querySelectorAll('.toc-chip'));
  var sections=chips.map(function(c){return document.querySelector(c.getAttribute('href'));});
  var lastY=window.pageYOffset, ticking=false;

  function update(){
    var y=window.pageYOffset;
    var h=document.documentElement.scrollHeight-window.innerHeight;
    bar.style.width=(h>0?(y/h*100):0)+'%';
    // Hide header + dock after scrolling starts; reveal on scroll-up or at top
    if(y>60 && y>lastY+4){ header.classList.add('hidden-up'); dock.classList.add('hidden-down'); }
    else if(y<lastY-8 || y<=60){ header.classList.remove('hidden-up'); dock.classList.remove('hidden-down'); }
    backTop.classList.toggle('show', y>600);
    // Active TOC chip
    var idx=-1;
    for(var i=0;i<sections.length;i++){ if(sections[i] && sections[i].getBoundingClientRect().top<=140) idx=i; }
    chips.forEach(function(c,i){ c.classList.toggle('active', i===idx); });
    if(idx>=0){ var a=chips[idx], nav=document.getElementById('toc-nav');
      nav.scrollLeft=a.offsetLeft-nav.clientWidth/2+a.clientWidth/2; }
    lastY=y; ticking=false;
  }
  window.addEventListener('scroll',function(){ if(!ticking){ticking=true;requestAnimationFrame(update);} },{passive:true});
  update();

  // Smooth anchor offset for fixed header
  chips.forEach(function(c){
    c.addEventListener('click',function(e){
      e.preventDefault();
      var t=document.querySelector(c.getAttribute('href'));
      if(t) window.scrollTo({top:t.getBoundingClientRect().top+window.pageYOffset-48,behavior:'smooth'});
    });
  });
})();

// Accordion (one open at a time)
function toggleAcc(id){
  var item=document.getElementById(id), wasOpen=item.classList.contains('open');
  document.querySelectorAll('.acc-item.open').forEach(function(i){i.classList.remove('open');});
  if(!wasOpen){ item.classList.add('open');
    setTimeout(function(){ var r=item.getBoundingClientRect(); if(r.top<80) window.scrollTo({top:r.top+window.pageYOffset-80,behavior:'smooth'}); },60); }
}

// Industry tabs
function showInd(n){
  document.querySelectorAll('.ind-tab').forEach(function(t,i){t.classList.toggle('active',i===n);});
  document.querySelectorAll('.ind-panel').forEach(function(p,i){p.classList.toggle('active',i===n);});
}
</script>
'''
SCRIPT = SCRIPT

with open("sec8_11.py", "w", encoding="utf-8") as f:
    for name in ['SEC8', 'SEC9', 'SEC10', 'SEC11', 'BOTTOM_DOCK', 'SCRIPT']:
        f.write('%s = %r\n' % (name, globals()[name]))
print("sec8_11.py written")
