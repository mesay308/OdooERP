# -*- coding: utf-8 -*-
# Visual-Oriented Addis Tech Odoo ERP Guide — Part 2 (Sections 6-11, Dock, JS & Assembler)

from build_visual_part1 import HEAD_VISUAL, STICKY_VISUAL, COVER_VISUAL, SEC1_V, SEC2_V, SEC3_V, SEC4_V, SEC5_V

# ── Section 6: Detailed Odoo ERP Module Profiles (Odoo Brand Zone) ──
modules_data = [
  ('6.1', 'fin', False, 'Odoo Accounting &amp; Invoicing',
   'Your Complete Financial Hub Built for Ethiopian Compliance.',
   'Replaces Peachtree and unlinked spreadsheets by connecting bank accounts, daily sales, vendor bills, and warehouse stock into one live MOR-compliant ledger.',
   [
     ('Ethiopian Tax Ready', 'Pre-configured VAT (15%), Withholding Tax (2% goods / 30% services) &amp; monthly deduction reports.'),
     ('E-Invoicing &amp; Fiscal Devices', 'Ready for upcoming electronic invoicing rules and certified fiscal cash registers.'),
     ('Amharic &amp; Local Calendars', 'Full Amharic language support and Ethiopian fiscal years (Hamle to Sene).'),
     ('Auto Bank Reconciliation', 'Match bank and Telebirr statements with internal sales and payment records.'),
     ('Instant Financial Reports', 'Generate Profit &amp; Loss, Balance Sheets, and Trial Balances in one click.'),
     ('Credit &amp; Bill Control', 'Customer credit limits, payment reminders, and vendor bill-to-receipt matching.')
   ]),
  ('6.2', 'ops', True, 'Odoo Inventory &amp; Warehouse Management',
   'Complete, Real-Time Control Over Your Stock and Stores.',
   'Direct visibility over all goods from supplier delivery to final sale across multiple locations, preventing shortages and showing exact stock value.',
   [
     ('Multi-Store Management', 'Track inventory across shops, central warehouses, and regional branches on one screen.'),
     ('Low-Stock Warnings', 'Instant alerts or automated purchase drafts before essential items run out.'),
     ('Barcode &amp; Mobile Scanning', 'Receive goods, pack orders, and count stock using phones or barcode scanners.'),
     ('Landed Cost for Importers', 'Add customs duty, transit fees, and shipping directly to true unit price.'),
     ('Batch, Lot &amp; Serials', 'Track expiry dates for food/pharma or serial numbers for machinery.'),
     ('Simple Stock Audits', 'Perform cyclic inventory counts quickly without pausing daily operations.')
   ]),
  ('6.3', 'ops', False, 'Odoo Purchasing &amp; Vendor Management',
   'Take Full Control Over Company Spending and Supplier Orders.',
   'Digital requisitions, supplier price comparisons, and purchase orders linked with warehouse and accounting so you pay only for arrived goods.',
   [
     ('Clear Purchase Requests', 'Digital item requisitions with mandatory manager approvals before ordering.'),
     ('Supplier Price Comparisons', 'Send RFQs to multiple vendors to compare prices, terms, and delivery schedules.'),
     ('Automated Purchase Orders', 'Turn approved quotes into official printable purchase orders with one click.'),
     ('3-Way Matching', 'Check purchase order, warehouse receipt, and vendor bill to stop overbilling.'),
     ('Vendor Performance', 'Track which local or overseas suppliers deliver on time with best quality.'),
     ('Import &amp; Forex Tracking', 'Manage international orders, shipments in transit, and foreign currency costs.')
   ]),
  ('6.4', 'sales', True, 'Odoo Sales &amp; Point of Sale (POS)',
   'Close Deals Faster and Run Fast, Modern Checkout Counters.',
   'Equips wholesale agents, showrooms, and retail cashiers to check live stock, calculate prices, and keep selling even during internet cuts.',
   [
     ('Instant Quotes &amp; Price Lists', 'Clean branded quotes in seconds with retail, wholesale, or corporate pricing.'),
     ('Fast Touchscreen POS', 'Modern checkout counters for shops, supermarkets, and restaurants on any device.'),
     ('Local Payment Support', 'Accept cash, Telebirr, CBE Birr, and bank transfers with instant receipts.'),
     ('Offline Selling Mode', 'Keep scanning and selling during internet cuts; auto-syncs when reconnected.'),
     ('Auto Stock Reservations', 'Orders reserve warehouse items immediately so out-of-stock goods are never promised.'),
     ('Sales Team Tracking', 'Monitor sales rep performance, commissions, and live revenue dashboards.')
   ]),
  ('6.5', 'sales', False, 'Odoo Customer Relationship Management (CRM)',
   'Turn Leads into Loyal Clients and Never Lose a Business Deal.',
   'Organizes client communications and sales pipelines in one visible place from first inquiry to signed contract.',
   [
     ('Visual Sales Pipeline', 'Drag-and-drop board categorized by stage (New, Qualified, Proposal Sent, Won).'),
     ('Automated Lead Capture', 'Collect inquiries automatically from website, email, or social campaigns.'),
     ('Follow-up Reminders', 'Schedule calls, meetings, demos, and quote follow-ups so no lead is forgotten.'),
     ('Complete Customer History', 'Unified log of phone notes, past quotes, purchases, and client preferences.'),
     ('Revenue Forecasting', 'Predict monthly cash flow and expected revenue from open deal probabilities.'),
     ('Lost Deal Analysis', 'Record why deals were lost (price, delivery time) to refine sales strategy.')
   ]),
  ('6.6', 'fin', True, 'Odoo Human Resources &amp; Payroll',
   'Organize Your Workforce and Automate Ethiopian Payroll.',
   'Unifies employee profiles, attendance, and monthly compensation in full compliance with Ethiopian labor, tax, and pension rules.',
   [
     ('Central Employee Directory', 'Secure digital profiles for contracts, IDs, emergency contacts, and departments.'),
     ('Ethiopian Payroll Rules', 'Auto-computes progressive income tax, 7% employee pension &amp; 11% employer pension.'),
     ('Attendance &amp; Shifts', 'Track daily check-ins via biometric devices, RFID cards, or mobile check-in.'),
     ('Leave &amp; Holiday Approvals', 'Online annual, sick, or maternity leave requests with live balance tracking.'),
     ('Direct Bank Disbursals', 'Generate summary payment files for bank salary transfers or Telebirr wallets.'),
     ('Expense Reimbursements', 'Staff submit fuel and expense claims by phone for quick verification and payout.')
   ]),
  ('6.7', 'ops', False, 'Odoo Manufacturing &amp; Production (MRP)',
   'Streamline Production Lines, Control Raw Materials, and Track Costs.',
   'Built for assembly plants, food processors, metal fabricators, and workshops—connecting the shop floor with raw material stores and finance.',
   [
     ('Bills of Materials (BOM)', 'Exact product recipe cards and ingredient lists including multi-stage assemblies.'),
     ('Raw Material Reservations', 'Auto-allocates raw goods from inventory as soon as a work order is scheduled.'),
     ('Shop Floor Work Orders', 'Assign tasks to machines or stations, tracking start times, pauses, and output.'),
     ('True Unit Cost Tracking', 'Combines raw materials, direct labor hours, and machine overhead automatically.'),
     ('Scrap &amp; Waste Management', 'Log material loss or defective output during runs to pinpoint bottlenecks.'),
     ('Quality Checkpoints', 'Mandatory quality control steps before finished goods enter inventory.')
   ]),
  ('6.8', 'fin', True, 'Odoo Budget Management',
   'Maintain Financial Discipline and Monitor Real Expenses in Real Time.',
   'Links budgets directly to the general ledger to compare planned targets against actual transactions across departments, projects, or cost centers.',
   [
     ('Department &amp; Project Budgets', 'Set monthly, quarterly, or annual limits for business units or branches.'),
     ('Live Planned vs. Actual', 'Side-by-side income and expense comparisons with zero manual collation.'),
     ('Early Overspending Warnings', 'Receive alerts when expenditures approach or exceed allocated budget lines.'),
     ('Analytical Cost Centers', 'Tag daily purchase invoices and expenses to specific branch or project codes.'),
     ('Multi-Period Planning', 'Parallel budgets for optimistic, conservative, or baseline projections.'),
     ('Management Dashboards', 'Color-coded visual reports showing current budget usage percentages at a glance.')
   ]),
  ('6.9', 'ops', False, 'Odoo Project Management',
   'Deliver Customer Work on Schedule and Keep Project Costs Under Control.',
   'Helps contractors, service firms, and technical teams plan and execute deliverables linked to timesheets, billing, and material procurement.',
   [
     ('Visual Kanban Task Boards', 'Organize deliverables by stage (Planning, In Progress, Review, Completed).'),
     ('Gantt Charts &amp; Milestones', 'Map complex schedules, critical deadlines, and task dependencies visually.'),
     ('Employee Timesheets', 'Field and technical staff record hours worked per task on mobile or desktop.'),
     ('Automated Project Invoicing', 'Bill clients by milestones, fixed contracts, or billable hourly rates in one click.'),
     ('Project Material Consumption', 'Link warehouse items and site expenses to a project code for true net profit.'),
     ('Document &amp; Client Portals', 'Share updates, drawings, and approvals with clients and site supervisors.')
   ]),
  ('6.10', 'sales', True, 'Odoo Website &amp; E-Commerce',
   'Build Your Online Store and Sell Directly into Your ERP.',
   'Connects your digital storefront directly with warehouse stock and accounting so online purchases automatically reserve stock and draft invoices.',
   [
     ('Drag-and-Drop Web Builder', 'Create mobile-friendly web pages and product catalogs without coding.'),
     ('Direct Inventory Sync', 'Quantities update live online; out-of-stock warehouse items hide automatically.'),
     ('Local &amp; Global Payments', 'Accept Telebirr, CBE Birr, bank transfers, and Visa/Mastercard for foreign buyers.'),
     ('Customer Self-Service Portal', 'Clients log in to view order status, download tax invoices, and track deliveries.'),
     ('Auto Order Fulfillment', 'Online purchases instantly generate sales orders, packing slips, and draft invoices.'),
     ('B2B &amp; B2C Pricing Rules', 'Show retail prices to visitors and negotiated wholesale discounts to corporate logins.')
   ]),
]

mod_cards_html = ''
for idx, (num, cat, is_teal, title, sub, intro, feats) in enumerate(modules_data):
    open_cls = ' open' if idx == 0 else ''
    teal_cls = ' teal-left' if is_teal else ''
    chips_html = ''.join(
        '<div class="mod-feat-chip"><div class="mod-feat-t"><span>&#10004;</span>%s</div><div class="mod-feat-d">%s</div></div>' % (ft, fd)
        for ft, fd in feats
    )
    mod_cards_html += '''
    <div class="mod-acc%s%s" data-cat="%s" id="mod-%d">
      <button class="mod-trig" onclick="toggleMod('mod-%d')">
        <span class="mod-num">%s</span>
        <div class="mod-head-wrap">
          <div class="mod-title">%s</div>
          <span class="mod-tag">%s</span>
        </div>
        <svg class="mod-chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg>
      </button>
      <div class="mod-body">
        <p style="font-size:.74rem;color:#3A3A5A;line-height:1.42;margin-top:8px;">%s</p>
        <div class="mod-feat-grid">%s</div>
      </div>
    </div>''' % (open_cls, teal_cls, cat, idx, idx, num, title, sub, intro, chips_html)

SEC6_V = '''
  <div id="sec6" class="odoo-sec">
    <div class="sec-head">
      <span class="sec-pill odoo-pill">6</span>
      <h2 class="sec-title odoo-title">Detailed Odoo ERP Module Profiles</h2>
    </div>
    <p class="sec-sub odoo-sub">Tap any module or filter by category &bull; 6 key features per module</p>

    <!-- Filter Bar + Expand All -->
    <div class="filter-bar">
      <button class="filter-pill active" onclick="filterMods('all', this)">All 10 Modules</button>
      <button class="filter-pill" onclick="filterMods('fin', this)">Finance &amp; Control (3)</button>
      <button class="filter-pill" onclick="filterMods('ops', this)">Operations &amp; Supply (4)</button>
      <button class="filter-pill" onclick="filterMods('sales', this)">Sales &amp; Growth (3)</button>
      <button class="filter-pill" style="border-color:#017E84;color:#017E84;" onclick="expandAllMods(this)" data-expanded="0">Expand All</button>
    </div>

    <div id="mod-list">%s</div>
  </div>
</div><!-- /odoo-zone-wrap -->
<div class="v-divider"></div>
''' % mod_cards_html

# ── Section 7: Additional Modules & Custom Solutions (Addis Tech Theme) ──
SEC7_V = '''
<div id="sec7" class="v-sec">
  <div class="sec-head">
    <span class="sec-pill">7</span>
    <h2 class="sec-title">Additional Modules &amp; Custom Solutions</h2>
  </div>
  <p class="sec-sub">Growing Beyond the Basics with AI and Custom Workflows</p>

  <!-- AI OCR Visual Flow Infographic -->
  <div style="background:linear-gradient(135deg,#1B1464 0%,#003B95 100%);border-radius:10px;padding:11px 10px;color:#fff;margin-bottom:12px;">
    <div style="font-size:.66rem;font-weight:800;color:#FFA600;text-transform:uppercase;letter-spacing:.05em;margin-bottom:6px;">&#9889; Native AI &amp; Custom Workflow Integration</div>
    <div style="display:grid;grid-template-columns:1fr auto 1fr auto 1fr;gap:4px;align-items:center;text-align:center;font-size:.69rem;font-weight:700;">
      <div style="background:rgba(255,255,255,.12);padding:6px 4px;border-radius:7px;">Printed Supplier Invoice / Receipt</div>
      <span style="color:#FFA600;font-weight:800;">&#10140;</span>
      <div style="background:rgba(255,166,0,.22);border:1px solid rgba(255,166,0,.45);padding:6px 4px;border-radius:7px;color:#FFA600;">AI OCR Extracts Vendor, Date &amp; Totals</div>
      <span style="color:#FFA600;font-weight:800;">&#10140;</span>
      <div style="background:rgba(6,162,37,.28);padding:6px 4px;border-radius:7px;color:#86EFAC;">Auto-Drafts Accounting Entry</div>
    </div>
  </div>

  <!-- 4 Ecosystem Cards (7.1 - 7.4) -->
  <div class="grid-2">
    <div class="v-card">
      <div style="display:flex;align-items:center;gap:6px;margin-bottom:2px;">
        <span style="background:#1B1464;color:#FFA600;font-size:.66rem;font-weight:800;padding:2px 6px;border-radius:5px;">7.1</span>
        <span class="v-card-title">Free Built-In Team Chat</span>
      </div>
      <div class="v-card-desc" style="display:flex;flex-direction:column;gap:4px;">
        <div><strong>&bull; Odoo Discuss:</strong> Private team channels &amp; direct messages replacing chaotic WhatsApp/Telegram groups.</div>
        <div><strong>&bull; Document Chatter:</strong> Chat, tag staff &amp; attach receipts directly under any invoice or PO.</div>
        <div><strong>&bull; Live Website Chat:</strong> Turn online visitors into sales leads in real time.</div>
      </div>
    </div>

    <div class="v-card">
      <div style="display:flex;align-items:center;gap:6px;margin-bottom:2px;">
        <span style="background:#003B95;color:#fff;font-size:.66rem;font-weight:800;padding:2px 6px;border-radius:5px;">7.2</span>
        <span class="v-card-title">Built-In AI Integration</span>
      </div>
      <div class="v-card-desc" style="display:flex;flex-direction:column;gap:4px;">
        <div><strong>&bull; Smart Receipt Scanning:</strong> AI reads supplier bills and drafts accounting entries.</div>
        <div><strong>&bull; Email &amp; Proposal Drafts:</strong> AI text assistance for client quotes and follow-ups.</div>
        <div><strong>&bull; AI Chatbots &amp; Helpdesk:</strong> Connect ChatGPT/AI assistants to answer client questions &amp; route tickets.</div>
      </div>
    </div>

    <div class="v-card">
      <div style="display:flex;align-items:center;gap:6px;margin-bottom:2px;">
        <span style="background:#06A225;color:#fff;font-size:.66rem;font-weight:800;padding:2px 6px;border-radius:5px;">7.3</span>
        <span class="v-card-title">100+ Ready Modules</span>
      </div>
      <div class="v-card-desc" style="display:flex;flex-direction:column;gap:4px;">
        <div><strong>&bull; Fleet &amp; Vehicles:</strong> Fuel, maintenance &amp; driver logs.</div>
        <div><strong>&bull; Quality Control:</strong> Mandatory checks for imports &amp; production.</div>
        <div><strong>&bull; Maintenance &amp; Repair:</strong> Prevent factory or truck breakdowns.</div>
        <div><strong>&bull; Barcode &amp; Documents:</strong> Digitize trade licenses &amp; contracts.</div>
      </div>
    </div>

    <div class="v-card" style="background:#F0F4FF;border-color:#B8C7F0;">
      <div style="display:flex;align-items:center;gap:6px;margin-bottom:2px;">
        <span style="background:#FFA600;color:#000C1D;font-size:.66rem;font-weight:800;padding:2px 6px;border-radius:5px;">7.4</span>
        <span class="v-card-title">Custom Dev by Addis Tech</span>
      </div>
      <div class="v-card-desc" style="display:flex;flex-direction:column;gap:4px;">
        <div><strong>&bull; Exact Workflow:</strong> Import container clearance, wholesale loyalty, or agricultural collection sheets.</div>
        <div><strong>&bull; Local Integrations:</strong> Connect local bank APIs &amp; Telebirr gateways.</div>
        <div><strong>&bull; Upgrade-Safe:</strong> Built on standard Odoo frameworks for smooth yearly updates.</div>
      </div>
    </div>
  </div>
</div>
<div class="v-divider"></div>
'''

# ── Section 8: Industries Covered by Odoo ERP ──
ind_data = [
  ('8.1', 'Wholesale &amp; Import', 'Wholesale, Distribution &amp; Import/Export',
   'For general importers, FMCG distributors, building material suppliers, and regional traders.',
   '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="3" width="15" height="13"/><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg>',
   [('Landed Cost Calculations', 'Distribute maritime shipping, transit fees, customs duties, and local transport directly onto true unit cost.'),
    ('Multi-Warehouse Logistics', 'Manage central storage hubs in Addis Ababa alongside regional distribution stores on one screen.'),
    ('Credit &amp; Wholesale Pricing', 'Set custom credit limits for distributors and tiered price lists for high-volume buyers.')]),
  ('8.2', 'Manufacturing', 'Manufacturing &amp; Agro-Processing',
   'For factories, metal and wood workshops, food and beverage producers, and edible oil/flour mills.',
   '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9"/></svg>',
   [('Formula &amp; Recipe Control (BOM)', 'Define multi-level Bills of Materials to track exact raw ingredients or parts per batch.'),
    ('Production Floor Tracking', 'Monitor station work orders, machine runtimes, and labor hours for accurate unit costs.'),
    ('Scrap &amp; Waste Auditing', 'Log raw material waste and scrap during runs to stop inventory leakage.')]),
  ('8.3', 'Construction', 'Construction, Engineering &amp; Contracting',
   'For general contractors, electro-mechanical firms, and specialized project service providers.',
   '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 20h20"/><path d="M5 20V8l7-5 7 5v12"/><path d="M9 20v-6h6v6"/></svg>',
   [('Project Milestone Tracking', 'Track project phases visually using Kanban boards and Gantt charts to keep site deliverables on schedule.'),
    ('Site Material Usage', 'Assign warehouse withdrawals and equipment usage directly to construction sites or project codes.'),
    ('Progress Invoicing', 'Bill clients automatically based on completed milestones, verified timesheets, or percentage-of-completion.')]),
  ('8.4', 'Retail &amp; POS', 'Retail Chains, Supermarkets &amp; Showrooms',
   'For electronics stores, fashion boutiques, supermarkets, and construction supply outlets.',
   '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>',
   [('Fast Point of Sale (POS)', 'Ring up sales quickly using barcode scanners, receipt printers, and touchscreen interfaces.'),
    ('Local Payment Support', 'Accept cash, Telebirr, CBE Birr, and card payments directly at the cash register.'),
    ('Uninterrupted Offline Selling', 'Keep selling and printing receipts during network cuts; auto-syncs once reconnected.')]),
  ('8.5', 'Services &amp; NGOs', 'Professional Services, Consulting &amp; NGOs',
   'For audit firms, legal practices, consulting agencies, and non-profit organizations.',
   '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>',
   [('Budget &amp; Fund Accounting', 'Track grants, donor funds, and expenditures against approved budget lines in real time.'),
    ('Timesheet &amp; Billing', 'Track billable consultant hours and generate client invoices with one click.'),
    ('Document &amp; Approval Control', 'Manage purchase approvals, vendor agreements, and payment vouchers digitally without paper trails.')]),
  ('8.6', 'Healthcare', 'Healthcare, Clinics &amp; Pharmaceuticals',
   'For private hospitals, specialty clinics, pharmacies, and pharmaceutical importers.',
   '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>',
   [('Expiry &amp; Batch/Lot Control', 'Track medications and supplies by batch numbers and expiration dates with automatic pre-expiry alerts.'),
    ('Direct POS for Pharmacies', 'Issue compliant receipts and track shelf inventory instantly at retail medicine counters.'),
    ('Strict Stock Traceability', 'Maintain an unbroken audit trail for regulated supplies from customs arrival to patient dispensing.')]),
]

tiles_html = ''
views_html = ''
for i, (num, short_t, full_t, aud, svg_ic, pts) in enumerate(ind_data):
    act = ' active' if i == 0 else ''
    tiles_html += '''
    <button class="ind-tile%s" onclick="selInd(%d)">
      <span class="ind-tile-num">%s</span>
      %s
      <span class="ind-tile-name">%s</span>
    </button>''' % (act, i, num, svg_ic, short_t)
    pts_html = ''.join(
        '<div style="background:#fff;border:1px solid #E2E5F3;border-left:3px solid #FFA600;border-radius:7px;padding:7px 9px;margin-top:6px;">'
        '<div style="font-family:\'Outfit\',sans-serif;font-size:.77rem;font-weight:700;color:#1B1464;">%s</div>'
        '<div style="font-size:.72rem;color:#444462;line-height:1.38;">%s</div></div>' % (pt, pd)
        for pt, pd in pts
    )
    views_html += '''
    <div class="ind-view%s" id="ind-v-%d">
      <div style="font-family:'Outfit',sans-serif;font-size:.88rem;font-weight:800;color:#1B1464;">%s. %s</div>
      <div style="font-size:.73rem;color:#003B95;font-style:italic;margin-bottom:4px;">%s</div>
      %s
    </div>''' % (act, i, num, full_t, aud, pts_html)

SEC8_V = '''
<div id="sec8" class="v-sec">
  <div class="sec-head">
    <span class="sec-pill">8</span>
    <h2 class="sec-title">Industries Covered by Odoo ERP</h2>
  </div>
  <p class="sec-sub">Built for the Realities of the Ethiopian Economy &bull; Tap any sector</p>

  <div class="ind-grid">%s</div>
  %s
</div>
<div class="v-divider"></div>
''' % (tiles_html, views_html)

# ── Section 9: Implementation Approach & Methodology ──
SEC9_V = '''
<div id="sec9" class="v-sec">
  <div class="sec-head">
    <span class="sec-pill">9</span>
    <h2 class="sec-title">Implementation Approach &amp; Methodology</h2>
  </div>
  <p class="sec-sub">A Practical, Step-by-Step Path to Business Transformation</p>

  <div style="background:#E5F0FC;border-left:3.5px solid #003B95;padding:9px 11px;border-radius:0 8px 8px 0;margin-bottom:12px;font-size:.76rem;color:#1A1A2E;line-height:1.42;">
    <strong>Software alone will not transform a company; execution does.</strong> Addis Tech breaks every rollout into <strong>4 straightforward phases</strong> tailored to Ethiopian realities (manual store records, internet fluctuations, paper approval habits) to guarantee smooth adoption from day one.
  </div>

  <!-- 4-Phase Visual Timeline Infographic -->
  <div style="display:flex;flex-direction:column;gap:8px;margin-bottom:14px;">
    <!-- Phase 1 -->
    <div style="background:#F8F9FE;border:1px solid #DCE1F5;border-left:4px solid #1B1464;border-radius:10px;padding:10px 11px;">
      <div style="display:flex;align-items:center;gap:8px;margin-bottom:4px;">
        <span style="width:24px;height:24px;border-radius:50%;background:#1B1464;color:#FFA600;font-family:'Outfit',sans-serif;font-size:.74rem;font-weight:800;display:inline-flex;align-items:center;justify-content:center;">1</span>
        <div>
          <div style="font-family:'Outfit',sans-serif;font-size:.84rem;font-weight:800;color:#1B1464;">Phase 1: Discovery &amp; Business Blueprint</div>
          <div style="font-size:.69rem;color:#003B95;font-style:italic;">Understanding how your business runs before configuring software</div>
        </div>
      </div>
      <div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:5px;margin-top:6px;">
        <div style="background:#fff;border:1px solid #E2E5F3;border-radius:6px;padding:6px;font-size:.69rem;"><strong style="color:#1B1464;display:block;">On-Site Walkthrough</strong>Inspect head office, shops &amp; regional hubs.</div>
        <div style="background:#fff;border:1px solid #E2E5F3;border-radius:6px;padding:6px;font-size:.69rem;"><strong style="color:#1B1464;display:block;">Process Mapping</strong>Document PO-to-shelf, sales &amp; MOR VAT filing.</div>
        <div style="background:#fff;border:1px solid #E2E5F3;border-radius:6px;padding:6px;font-size:.69rem;"><strong style="color:#1B1464;display:block;">Clear Blueprint</strong>Roles, approvals &amp; milestones approved first.</div>
      </div>
    </div>

    <!-- Phase 2 -->
    <div style="background:#F8F9FE;border:1px solid #DCE1F5;border-left:4px solid #003B95;border-radius:10px;padding:10px 11px;">
      <div style="display:flex;align-items:center;gap:8px;margin-bottom:4px;">
        <span style="width:24px;height:24px;border-radius:50%;background:#003B95;color:#fff;font-family:'Outfit',sans-serif;font-size:.74rem;font-weight:800;display:inline-flex;align-items:center;justify-content:center;">2</span>
        <div>
          <div style="font-family:'Outfit',sans-serif;font-size:.84rem;font-weight:800;color:#1B1464;">Phase 2: System Configuration &amp; Localization</div>
          <div style="font-size:.69rem;color:#003B95;font-style:italic;">Tailoring the system to match your daily workflow and local tax rules</div>
        </div>
      </div>
      <div class="grid-2" style="margin-top:6px;gap:5px;">
        <div style="background:#fff;border:1px solid #E2E5F3;border-radius:6px;padding:6px;font-size:.69rem;"><strong style="color:#1B1464;">&bull; Core Module Setup:</strong> Accounting, Inventory, Sales, Purchase, HR, or Production.</div>
        <div style="background:#fff;border:1px solid #E2E5F3;border-radius:6px;padding:6px;font-size:.69rem;"><strong style="color:#1B1464;">&bull; Ethiopian Tax Setup:</strong> VAT 15%, Withholding, fiscal calendars &amp; fiscal machines.</div>
        <div style="background:#fff;border:1px solid #E2E5F3;border-radius:6px;padding:6px;font-size:.69rem;"><strong style="color:#1B1464;">&bull; Local Integrations:</strong> Connect Telebirr, CBE Birr &amp; company databases.</div>
        <div style="background:#fff;border:1px solid #E2E5F3;border-radius:6px;padding:6px;font-size:.69rem;"><strong style="color:#1B1464;">&bull; Simulation &amp; Testing:</strong> Test containers, tax invoices &amp; payroll before launch.</div>
      </div>
    </div>

    <!-- Phase 3 -->
    <div style="background:#F8F9FE;border:1px solid #DCE1F5;border-left:4px solid #FFA600;border-radius:10px;padding:10px 11px;">
      <div style="display:flex;align-items:center;gap:8px;margin-bottom:4px;">
        <span style="width:24px;height:24px;border-radius:50%;background:#FFA600;color:#000C1D;font-family:'Outfit',sans-serif;font-size:.74rem;font-weight:800;display:inline-flex;align-items:center;justify-content:center;">3</span>
        <div>
          <div style="font-family:'Outfit',sans-serif;font-size:.84rem;font-weight:800;color:#1B1464;">Phase 3: Data Transfer &amp; Hands-On Staff Training</div>
          <div style="font-size:.69rem;color:#003B95;font-style:italic;">Cleaning your business records and empowering your employees</div>
        </div>
      </div>
      <div class="grid-2" style="margin:6px 0;gap:5px;">
        <div style="background:#fff;border:1px solid #E2E5F3;border-radius:6px;padding:6px;font-size:.69rem;"><strong style="color:#1B1464;">&bull; Data Cleansing:</strong> Verify opening balances, contacts &amp; stock from Peachtree/Excel.</div>
        <div style="background:#fff;border:1px solid #E2E5F3;border-radius:6px;padding:6px;font-size:.69rem;"><strong style="color:#1B1464;">&bull; Accurate Data Import:</strong> Reconcile against financial statements for zero data loss.</div>
      </div>
      <!-- Role-Based In-Person Training 2x2 Visual Grid -->
      <div style="background:#1B1464;color:#fff;border-radius:8px;padding:8px 9px;">
        <div style="font-size:.68rem;font-weight:800;color:#FFA600;text-transform:uppercase;margin-bottom:5px;">Role-Based, In-Person Training (Amharic &amp; English):</div>
        <div class="grid-2" style="gap:5px;font-size:.68rem;">
          <div style="background:rgba(255,255,255,.1);padding:5px 7px;border-radius:6px;"><strong style="color:#FFA600;display:block;">Sales &amp; Cashiers</strong>Touchscreen POS, receipts, Telebirr &amp; cash.</div>
          <div style="background:rgba(255,255,255,.1);padding:5px 7px;border-radius:6px;"><strong style="color:#FFA600;display:block;">Warehouse Staff</strong>Barcodes, supplier shipments, slips &amp; stock counts.</div>
          <div style="background:rgba(255,255,255,.1);padding:5px 7px;border-radius:6px;"><strong style="color:#FFA600;display:block;">Accountants</strong>VAT reports, vendor bill matching &amp; bank reconciliation.</div>
          <div style="background:rgba(255,255,255,.1);padding:5px 7px;border-radius:6px;"><strong style="color:#FFA600;display:block;">Executive Management</strong>Live dashboards, financial reports &amp; mobile PO approvals.</div>
        </div>
      </div>
    </div>

    <!-- Phase 4 -->
    <div style="background:#F8F9FE;border:1px solid #DCE1F5;border-left:4px solid #06A225;border-radius:10px;padding:10px 11px;">
      <div style="display:flex;align-items:center;gap:8px;margin-bottom:4px;">
        <span style="width:24px;height:24px;border-radius:50%;background:#06A225;color:#fff;font-family:'Outfit',sans-serif;font-size:.74rem;font-weight:800;display:inline-flex;align-items:center;justify-content:center;">4</span>
        <div>
          <div style="font-family:'Outfit',sans-serif;font-size:.84rem;font-weight:800;color:#1B1464;">Phase 4: Go-Live &amp; On-Site Support</div>
          <div style="font-size:.69rem;color:#06A225;font-style:italic;">Smooth switchover with zero disruption to daily sales</div>
        </div>
      </div>
      <div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:5px;margin-top:6px;">
        <div style="background:#fff;border:1px solid #E2E5F3;border-radius:6px;padding:6px;font-size:.69rem;"><strong style="color:#1B1464;display:block;">Controlled Cutover</strong>Scheduled on weekends or month-end closings.</div>
        <div style="background:#fff;border:1px solid #E2E5F3;border-radius:6px;padding:6px;font-size:.69rem;"><strong style="color:#1B1464;display:block;">2-Week Floor Support</strong>Engineers physically on-site at your offices.</div>
        <div style="background:#fff;border:1px solid #E2E5F3;border-radius:6px;padding:6px;font-size:.69rem;"><strong style="color:#1B1464;display:block;">Ongoing Maintenance</strong>Regular backups, updates &amp; local technical support.</div>
      </div>
    </div>
  </div>

  <!-- 3 Implementation Guarantees Shield Cards -->
  <p style="font-family:'Outfit',sans-serif;font-size:.86rem;font-weight:800;color:#1B1464;margin-bottom:7px;">Our Implementation Guarantees</p>
  <div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:6px;">
    <div style="background:#F0FDF4;border:1px solid #BBF7D0;border-radius:9px;padding:8px 7px;text-align:center;">
      <div style="font-family:'Outfit',sans-serif;font-size:.75rem;font-weight:800;color:#14532D;margin-bottom:3px;">&#128737; Phased Deployment</div>
      <p style="font-size:.68rem;color:#166534;line-height:1.35;">Start with Accounting, Inventory &amp; Sales first; add Manufacturing or CRM once staff are comfortable.</p>
    </div>
    <div style="background:#F0FDF4;border:1px solid #BBF7D0;border-radius:9px;padding:8px 7px;text-align:center;">
      <div style="font-family:'Outfit',sans-serif;font-size:.75rem;font-weight:800;color:#14532D;margin-bottom:3px;">&#128274; Zero Data Loss</div>
      <p style="font-size:.68rem;color:#166534;line-height:1.35;">Opening cash, customer debts, supplier payables &amp; stock counts audited line-by-line before retiring old tools.</p>
    </div>
    <div style="background:#F0FDF4;border:1px solid #BBF7D0;border-radius:9px;padding:8px 7px;text-align:center;">
      <div style="font-family:'Outfit',sans-serif;font-size:.75rem;font-weight:800;color:#14532D;margin-bottom:3px;">&#129309; Local Accountability</div>
      <p style="font-size:.68rem;color:#166534;line-height:1.35;">Work directly with software engineers and consultants based in Addis Ababa for immediate in-person support.</p>
    </div>
  </div>
</div>
<div class="v-divider"></div>
'''

# ── Section 10: Project Team & Governance Structure ──
SEC10_V = '''
<div id="sec10" class="v-sec">
  <div class="sec-head">
    <span class="sec-pill">10</span>
    <h2 class="sec-title">Project Team &amp; Governance Structure</h2>
  </div>
  <p class="sec-sub">Cross-functional domain specialists &amp; Odoo engineers in Finance, Sales &amp; Supply Chain</p>

  <!-- Governance Structure Visual Diagram -->
  <div style="background:linear-gradient(135deg,#1B1464,#0B0642);color:#fff;border-radius:10px;padding:10px;margin-bottom:10px;text-align:center;">
    <div style="font-size:.68rem;font-weight:800;color:#FFA600;text-transform:uppercase;letter-spacing:.05em;">2-Tier Project Delivery Governance</div>
    <div style="font-size:.74rem;margin:4px 0;"><strong>5 Senior Project Leads &amp; Subject-Matter Experts</strong> (Governance, Strategy &amp; Core Delivery)</div>
    <div style="color:#FFA600;font-size:.8rem;line-height:1;">&#8595; Supported Dynamically By &#8595;</div>
    <div style="font-size:.73rem;margin-top:3px;color:rgba(240,240,255,.9);"><strong>4 Extended Implementation &amp; Support Squad Units</strong> across all project phases</div>
  </div>

  <!-- 5 Senior Leads Compact Visual Cards -->
  <div style="display:flex;flex-direction:column;gap:7px;margin-bottom:12px;">
    <div class="v-card-row" style="background:#fff;">
      <div class="v-icon" style="width:36px;height:36px;font-family:'Outfit',sans-serif;font-weight:800;font-size:.82rem;">EA</div>
      <div style="flex:1;min-width:0;">
        <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:4px;">
          <span style="font-family:'Outfit',sans-serif;font-size:.84rem;font-weight:800;color:#1B1464;">1. Eyob Atnafu &mdash; <span style="color:#003B95;">Project Manager</span></span>
          <span style="font-size:.65rem;font-weight:800;background:#E6F7EA;color:#06A225;padding:1px 7px;border-radius:99px;">10+ Years</span>
        </div>
        <div style="font-size:.68rem;color:#003B95;font-weight:600;margin:2px 0;">Software Project Management | ERP Implementation | Software Development Lifecycle</div>
        <p style="font-size:.72rem;color:#444462;line-height:1.38;">Leads overall execution, timeline, resource allocation, and risk mitigation—coordinating stakeholders and technical teams on budget and quality.</p>
      </div>
    </div>

    <div class="v-card-row" style="background:#fff;">
      <div class="v-icon" style="width:36px;height:36px;font-family:'Outfit',sans-serif;font-weight:800;font-size:.82rem;">MA</div>
      <div style="flex:1;min-width:0;">
        <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:4px;">
          <span style="font-family:'Outfit',sans-serif;font-size:.84rem;font-weight:800;color:#1B1464;">2. Mesay Alemayehu &mdash; <span style="color:#003B95;">Lead Business (Functional) Consultant</span></span>
          <span style="font-size:.65rem;font-weight:800;background:#E6F7EA;color:#06A225;padding:1px 7px;border-radius:99px;">12+ Years</span>
        </div>
        <div style="font-size:.68rem;color:#003B95;font-weight:600;margin:2px 0;">Business Process Reengineering (BPR) | Process Design | Change Management | Sales &amp; Supply Chain</div>
        <p style="font-size:.72rem;color:#444462;line-height:1.38;">Audits workflows to design target processes. Leads functional blueprinting, change management, and user adoption aligned with international ERP best practices.</p>
      </div>
    </div>

    <div class="v-card-row" style="background:#fff;">
      <div class="v-icon" style="width:36px;height:36px;font-family:'Outfit',sans-serif;font-weight:800;font-size:.82rem;">YT</div>
      <div style="flex:1;min-width:0;">
        <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:4px;">
          <span style="font-family:'Outfit',sans-serif;font-size:.84rem;font-weight:800;color:#1B1464;">3. Yohanis Taye &mdash; <span style="color:#003B95;">Lead Odoo Developer</span></span>
          <span style="font-size:.65rem;font-weight:800;background:#E6F7EA;color:#06A225;padding:1px 7px;border-radius:99px;">8+ Years</span>
        </div>
        <div style="font-size:.68rem;color:#003B95;font-weight:600;margin:2px 0;">Odoo Core Architecture | Custom Module Development | System Integration | Backend Engineering</div>
        <p style="font-size:.72rem;color:#444462;line-height:1.38;">Spearheads technical customization, module configuration, and API integrations with clean architecture and tailored workflow logic.</p>
      </div>
    </div>

    <div class="v-card-row" style="background:#fff;">
      <div class="v-icon" style="width:36px;height:36px;font-family:'Outfit',sans-serif;font-weight:800;font-size:.82rem;">GM</div>
      <div style="flex:1;min-width:0;">
        <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:4px;">
          <span style="font-family:'Outfit',sans-serif;font-size:.84rem;font-weight:800;color:#1B1464;">4. Gashaw Mekonen &mdash; <span style="color:#003B95;">Accounting &amp; Finance Expert</span></span>
          <span style="font-size:.65rem;font-weight:800;background:#E6F7EA;color:#06A225;padding:1px 7px;border-radius:99px;">13+ Yrs &bull; Certified Accountant &amp; Auditor</span>
        </div>
        <div style="font-size:.68rem;color:#003B95;font-weight:600;margin:2px 0;">Financial Advisory | Tax Compliance &amp; Reporting | Statutory Auditing | Cost Accounting</div>
        <p style="font-size:.72rem;color:#444462;line-height:1.38;">Oversees financial localization, Chart of Accounts, and MOR tax setup (VAT, Withholding) for automated reconciliation and complete audit readiness.</p>
      </div>
    </div>

    <div class="v-card-row" style="background:#fff;">
      <div class="v-icon" style="width:36px;height:36px;font-family:'Outfit',sans-serif;font-weight:800;font-size:.82rem;">BT</div>
      <div style="flex:1;min-width:0;">
        <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:4px;">
          <span style="font-family:'Outfit',sans-serif;font-size:.84rem;font-weight:800;color:#1B1464;">5. Belay Tadios &mdash; <span style="color:#003B95;">Senior DevOps Engineer</span></span>
          <span style="font-size:.65rem;font-weight:800;background:#E6F7EA;color:#06A225;padding:1px 7px;border-radius:99px;">6+ Years</span>
        </div>
        <div style="font-size:.68rem;color:#003B95;font-weight:600;margin:2px 0;">ERP Infrastructure &amp; Deployment | System Environment Setup | Database Security &amp; Optimization</div>
        <p style="font-size:.72rem;color:#444462;line-height:1.38;">Architect of cloud and on-premise servers—responsible for security, automated backups, high availability, and offline-online sync.</p>
      </div>
    </div>
  </div>

  <!-- Extended Implementation & Support Squad (2x2 Grid) -->
  <p style="font-family:'Outfit',sans-serif;font-size:.84rem;font-weight:800;color:#1B1464;margin-bottom:6px;">Extended Implementation &amp; Support Squad</p>
  <div class="grid-2">
    <div class="v-card">
      <span class="v-card-title">Functional Consultants</span>
      <p class="v-card-desc">Module-specific user training (Amharic &amp; English), daily workflow setup &amp; initial go-live assistance.</p>
    </div>
    <div class="v-card">
      <span class="v-card-title">Software &amp; Integration Devs</span>
      <p class="v-card-desc">Custom reports, data extraction scripts, interface tuning &amp; local payment/hardware integrations.</p>
    </div>
    <div class="v-card">
      <span class="v-card-title">Data Migration Analysts</span>
      <p class="v-card-desc">Cleansing, auditing, and loading historical balances, contacts &amp; stock counts for zero data loss.</p>
    </div>
    <div class="v-card">
      <span class="v-card-title">On-Site Floor Technicians</span>
      <p class="v-card-desc">Stationed at headquarters, retail stores, or warehouses during launch to guide users instantly.</p>
    </div>
  </div>
</div>
<div class="v-divider"></div>
'''

# ── Section 11: Next Steps & Project Initiation ──
SEC11_V = '''
<div id="sec11" class="v-sec">
  <div class="sec-head">
    <span class="sec-pill">11</span>
    <h2 class="sec-title">Next Steps &amp; Project Initiation</h2>
  </div>
  <p class="sec-sub">Recommended 4-Step Roadmap to Engagement with Addis Tech PLC</p>

  <div class="grid-2" style="margin-bottom:16px;">
    <div class="v-card" style="background:#fff;border-top:3px solid #FFA600;">
      <div style="display:flex;align-items:center;gap:6px;">
        <span style="width:22px;height:22px;border-radius:50%;background:#FFA600;color:#000C1D;font-family:'Outfit',sans-serif;font-size:.72rem;font-weight:800;display:inline-flex;align-items:center;justify-content:center;">1</span>
        <span class="v-card-title">Executive Alignment &amp; Live Demo</span>
      </div>
      <p class="v-card-desc"><strong style="color:#003B95;">Action:</strong> Schedule a tailored Odoo demo on your industry workflows (Finance, Supply Chain, POS, or MRP).</p>
      <p class="v-card-desc"><strong style="color:#06A225;">Outcome:</strong> Experience how Odoo handles your daily scenarios &amp; local tax rules live.</p>
    </div>

    <div class="v-card" style="background:#fff;border-top:3px solid #003B95;">
      <div style="display:flex;align-items:center;gap:6px;">
        <span style="width:22px;height:22px;border-radius:50%;background:#003B95;color:#fff;font-family:'Outfit',sans-serif;font-size:.72rem;font-weight:800;display:inline-flex;align-items:center;justify-content:center;">2</span>
        <span class="v-card-title">On-Site Assessment (Blueprint)</span>
      </div>
      <p class="v-card-desc"><strong style="color:#003B95;">Action:</strong> 1-to-2 day walkthrough of your office, store, or warehouse locations.</p>
      <p class="v-card-desc"><strong style="color:#06A225;">Outcome:</strong> Formal <strong>Business Requirements &amp; Scope Alignment Document</strong>.</p>
    </div>

    <div class="v-card" style="background:#fff;border-top:3px solid #1B1464;">
      <div style="display:flex;align-items:center;gap:6px;">
        <span style="width:22px;height:22px;border-radius:50%;background:#1B1464;color:#FFA600;font-family:'Outfit',sans-serif;font-size:.72rem;font-weight:800;display:inline-flex;align-items:center;justify-content:center;">3</span>
        <span class="v-card-title">Scope Approval &amp; Sign-Off</span>
      </div>
      <p class="v-card-desc"><strong style="color:#003B95;">Action:</strong> Review and sign the Implementation Statement of Work (SOW), milestones &amp; warranty agreement.</p>
      <p class="v-card-desc"><strong style="color:#06A225;">Outcome:</strong> Formal authorization &amp; reservation of dedicated senior resources.</p>
    </div>

    <div class="v-card" style="background:#fff;border-top:3px solid #06A225;">
      <div style="display:flex;align-items:center;gap:6px;">
        <span style="width:22px;height:22px;border-radius:50%;background:#06A225;color:#fff;font-family:'Outfit',sans-serif;font-size:.72rem;font-weight:800;display:inline-flex;align-items:center;justify-content:center;">4</span>
        <span class="v-card-title">Mobilization &amp; Phase 1 Kickoff</span>
      </div>
      <p class="v-card-desc"><strong style="color:#003B95;">Action:</strong> Official launch meeting between your executive sponsors and the Addis Tech squad.</p>
      <p class="v-card-desc"><strong style="color:#06A225;">Outcome:</strong> Immediate start of system setup, data preparation &amp; workflow configuration.</p>
    </div>
  </div>

  <!-- Contact Hub -->
  <div id="contact" style="background:linear-gradient(155deg,#1B1464 0%,#0B0642 100%);border-radius:12px;padding:16px 12px;color:#fff;">
    <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px;margin-bottom:8px;">
      <p style="font-family:'Outfit',sans-serif;font-size:1.02rem;font-weight:800;">&#128222; Contact Us to Get Started Today</p>
      <a href="addis_tech_odoo_guide.html" style="font-family:'Outfit',sans-serif;font-size:.7rem;font-weight:800;background:#fff;color:#1B1464;padding:4px 10px;border-radius:99px;text-decoration:none;">Read Full Document &rarr;</a>
    </div>
    <p style="font-size:.76rem;color:rgba(240,240,255,.85);margin-bottom:12px;">Take the first step toward operational excellence and real-time financial control:</p>

    <div class="grid-2" style="gap:7px;">
      <a href="https://wa.me/251911202265" target="_blank" rel="noopener" style="background:rgba(255,166,0,.18);border:1px solid rgba(255,166,0,.45);border-radius:8px;padding:9px 10px;text-decoration:none;color:#fff;display:flex;flex-direction:column;">
        <span style="font-size:.63rem;font-weight:800;color:#FFA600;text-transform:uppercase;">WhatsApp (Primary)</span>
        <span style="font-size:.82rem;font-weight:800;">+251 91120 2265</span>
      </a>
      <a href="tel:+251911505992" style="background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.15);border-radius:8px;padding:9px 10px;text-decoration:none;color:#fff;display:flex;flex-direction:column;">
        <span style="font-size:.63rem;font-weight:800;color:#FFA600;text-transform:uppercase;">Phone</span>
        <span style="font-size:.82rem;font-weight:700;">+251 911 505992</span>
      </a>
      <a href="mailto:info@addistechplc.com" style="background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.15);border-radius:8px;padding:9px 10px;text-decoration:none;color:#fff;display:flex;flex-direction:column;">
        <span style="font-size:.63rem;font-weight:800;color:#FFA600;text-transform:uppercase;">Email</span>
        <span style="font-size:.74rem;font-weight:600;">info@addistechplc.com / sales@addistechplc.com</span>
      </a>
      <a href="https://www.addistechplc.com" target="_blank" rel="noopener" style="background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.15);border-radius:8px;padding:9px 10px;text-decoration:none;color:#fff;display:flex;flex-direction:column;">
        <span style="font-size:.63rem;font-weight:800;color:#FFA600;text-transform:uppercase;">Office &amp; Web</span>
        <span style="font-size:.74rem;font-weight:600;">Addis Ababa &bull; www.addistechplc.com</span>
      </a>
    </div>
  </div>
</div>
'''

DOCK_VISUAL = '''
<div id="bottom-dock">
  <div class="dock-inner">
    <a class="dock-btn dock-cta" href="https://wa.me/251911202265" target="_blank" rel="noopener">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.4 8.4 0 0 1-12.4 7.4L3 20.5l1.7-5.4A8.4 8.4 0 1 1 21 11.5z"/></svg>
      WhatsApp +251 91120 2265
    </a>
    <a class="dock-btn" href="https://wa.me/251911202265?text=Hello%20Addis%20Tech%2C%20I%20would%20like%20to%20book%20an%20Odoo%20ERP%20demo." target="_blank" rel="noopener">Book Demo</a>
    <a class="dock-btn dock-doc" href="addis_tech_odoo_guide.html">Main Doc</a>
    <a class="dock-btn" style="width:36px;padding:0;border-radius:50%;" href="#top" aria-label="Back to top">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M18 15l-6-6-6 6"/></svg>
    </a>
  </div>
</div>
<button id="back-top" aria-label="Back to top" onclick="window.scrollTo({top:0,behavior:'smooth'})">
  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M18 15l-6-6-6 6"/></svg>
</button>
'''

SCRIPT_VISUAL = '''
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
    if(y>60 && y>lastY+4){ header.classList.add('hidden-up'); dock.classList.add('hidden-down'); }
    else if(y<lastY-8 || y<=60){ header.classList.remove('hidden-up'); dock.classList.remove('hidden-down'); }
    backTop.classList.toggle('show', y>600);
    var idx=-1;
    for(var i=0;i<sections.length;i++){ if(sections[i] && sections[i].getBoundingClientRect().top<=135) idx=i; }
    chips.forEach(function(c,i){ c.classList.toggle('active', i===idx); });
    // Switch sticky header into Odoo Plum mode when inside Sections 4, 5, or 6 (indices 3, 4, 5)
    header.classList.toggle('odoo-mode', idx>=3 && idx<=5);
    if(idx>=0){ var a=chips[idx], nav=document.getElementById('toc-nav');
      nav.scrollLeft=a.offsetLeft-nav.clientWidth/2+a.clientWidth/2; }
    lastY=y; ticking=false;
  }
  window.addEventListener('scroll',function(){ if(!ticking){ticking=true;requestAnimationFrame(update);} },{passive:true});
  update();

  chips.forEach(function(c){
    c.addEventListener('click',function(e){
      e.preventDefault();
      var t=document.querySelector(c.getAttribute('href'));
      if(t) window.scrollTo({top:t.getBoundingClientRect().top+window.pageYOffset-10,behavior:'smooth'});
    });
  });
})();

function toggleMod(id){
  var el=document.getElementById(id);
  el.classList.toggle('open');
}

function filterMods(cat, btn){
  document.querySelectorAll('.filter-pill').forEach(function(b){
    if(!b.hasAttribute('data-expanded')) b.classList.remove('active');
  });
  btn.classList.add('active');
  document.querySelectorAll('.mod-acc').forEach(function(m){
    m.style.display=(cat==='all' || m.getAttribute('data-cat')===cat)?'block':'none';
  });
}

function expandAllMods(btn){
  var exp=btn.getAttribute('data-expanded')==='1';
  document.querySelectorAll('.mod-acc').forEach(function(m){
    m.classList.toggle('open', !exp);
  });
  btn.setAttribute('data-expanded', exp?'0':'1');
  btn.textContent=exp?'Expand All':'Collapse All';
}

function selInd(n){
  document.querySelectorAll('.ind-tile').forEach(function(t,i){t.classList.toggle('active',i===n);});
  document.querySelectorAll('.ind-view').forEach(function(v,i){v.classList.toggle('active',i===n);});
}
</script>
'''

html_out = (
    HEAD_VISUAL + '\n<body>\n' + STICKY_VISUAL + COVER_VISUAL +
    SEC1_V + SEC2_V + SEC3_V + SEC4_V + SEC5_V + SEC6_V +
    SEC7_V + SEC8_V + SEC9_V + SEC10_V + SEC11_V +
    DOCK_VISUAL + SCRIPT_VISUAL + '\n</body>\n</html>\n'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_out)

print('index.html written:', len(html_out), 'chars')
