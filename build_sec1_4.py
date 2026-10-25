# -*- coding: utf-8 -*-
# Sections: Cover, Nav, 1-4

COVER = '''
<div id="top"></div>

<!-- ══ COVER ═════════════════════════════════════════════════ -->
<div style="background:linear-gradient(160deg,#1B1464 0%,#0B0642 100%);padding:28px 16px 24px 16px;">
  <div style="max-width:680px;margin:0 auto;">
    <!-- Brand -->
    <div style="display:flex;align-items:center;gap:8px;margin-bottom:20px;">
      <div style="background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.18);border-radius:7px;padding:5px;display:flex;align-items:center;justify-content:center;">
        <svg width="16" height="16" viewBox="0 0 20 20" fill="none"><path d="M3.334 14.166L8.334 9.166L3.334 4.166" stroke="#FFA600" stroke-linecap="round" stroke-width="1.8"/><path d="M10 15.834H16.6667" stroke="#FFA600" stroke-linecap="round" stroke-width="1.8"/></svg>
      </div>
      <span style="font-family:'Outfit',sans-serif;font-size:1.05rem;font-weight:700;color:#fff;">Addis<span style="color:#FFA600;">Tech</span> <span style="font-weight:400;font-size:.8rem;opacity:.7;">PLC</span></span>
    </div>
    <!-- Doc title -->
    <p style="font-family:'Plus Jakarta Sans',sans-serif;font-size:.68rem;font-weight:700;color:#FFA600;text-transform:uppercase;letter-spacing:.08em;margin-bottom:8px;">Official Document — 9/1/2026</p>
    <h1 style="font-family:'Outfit',sans-serif;font-size:1.5rem;font-weight:800;color:#fff;line-height:1.25;margin-bottom:8px;">Odoo Enterprise Resource Planning (ERP) System Overview &amp; Implementation Guide</h1>
    <p style="font-size:.78rem;color:rgba(240,240,255,.75);margin-bottom:18px;font-style:italic;">Business with World-Class Digital Solutions</p>
    <!-- Tag bullets -->
    <div style="display:flex;flex-direction:column;gap:6px;margin-bottom:20px;">
      <div style="display:flex;align-items:flex-start;gap:8px;font-size:.8rem;color:rgba(240,240,255,.9);">
        <span style="color:#FFA600;font-weight:800;flex-shrink:0;">○</span>
        Manage your Multiple Business Operations with One System
      </div>
      <div style="display:flex;align-items:flex-start;gap:8px;font-size:.8rem;color:rgba(240,240,255,.9);">
        <span style="color:#FFA600;font-weight:800;flex-shrink:0;">○</span>
        Automate your Business Operations with One System
      </div>
      <div style="display:flex;align-items:flex-start;gap:8px;font-size:.8rem;color:rgba(240,240,255,.9);">
        <span style="color:#FFA600;font-weight:800;flex-shrink:0;">○</span>
        Get Auto Generated Reports with Live Dashboards
      </div>
    </div>
    <!-- CTA strip -->
    <div style="display:flex;gap:8px;flex-wrap:wrap;">
      <a href="https://wa.me/251911202265" target="_blank" rel="noopener" style="display:inline-flex;align-items:center;gap:6px;background:#FFA600;color:#000C1D;font-family:'Outfit',sans-serif;font-weight:800;font-size:.8rem;padding:8px 16px;border-radius:9999px;text-decoration:none;">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.4 8.4 0 0 1-12.4 7.4L3 20.5l1.7-5.4A8.4 8.4 0 1 1 21 11.5z"/></svg>
        WhatsApp +251 91120 2265
      </a>
      <a href="index.html" style="display:inline-flex;align-items:center;gap:6px;background:#fff;color:#1B1464;font-family:'Outfit',sans-serif;font-weight:800;font-size:.8rem;padding:8px 16px;border-radius:9999px;text-decoration:none;box-shadow:0 2px 8px rgba(0,0,0,.2);">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/></svg>
        Visual Presentation
      </a>
      <a href="mailto:info@addistechplc.com" style="display:inline-flex;align-items:center;gap:6px;background:rgba(255,255,255,.12);color:#fff;font-family:'Outfit',sans-serif;font-weight:600;font-size:.8rem;padding:8px 16px;border-radius:9999px;text-decoration:none;border:1px solid rgba(255,255,255,.2);">
        info@addistechplc.com
      </a>
    </div>
  </div>
</div>
'''

# ── Sticky Header ──
STICKY_HEADER = '''
<div id="sticky-header">
  <div style="max-width:680px;margin:0 auto;padding:7px 14px;display:flex;align-items:center;justify-content:space-between;gap:8px;">
    <div style="display:flex;align-items:center;gap:8px;">
      <div style="background:rgba(255,255,255,.12);border-radius:6px;padding:4px;display:flex;">
        <svg width="14" height="14" viewBox="0 0 20 20" fill="none"><path d="M3.334 14.166L8.334 9.166L3.334 4.166" stroke="#FFA600" stroke-linecap="round" stroke-width="1.8"/><path d="M10 15.834H16.6667" stroke="#FFA600" stroke-linecap="round" stroke-width="1.8"/></svg>
      </div>
      <span style="font-family:'Outfit',sans-serif;font-size:.9rem;font-weight:700;color:#fff;">Addis<span style="color:#FFA600;">Tech</span></span>
      <span style="font-size:.65rem;color:rgba(240,240,255,.55);display:none;" id="doc-label">Odoo ERP Guide</span>
    </div>
    <div style="display:flex;align-items:center;gap:6px;">
      <a href="index.html" style="display:inline-flex;align-items:center;gap:4px;background:rgba(255,255,255,.14);color:#fff;border:1px solid rgba(255,255,255,.25);font-family:'Outfit',sans-serif;font-weight:700;font-size:.7rem;padding:5px 10px;border-radius:9999px;text-decoration:none;">
        <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="#FFA600" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/></svg>
        Visual View
      </a>
      <a href="https://wa.me/251911202265" target="_blank" rel="noopener" style="display:inline-flex;align-items:center;gap:5px;background:#FFA600;color:#000C1D;font-family:'Outfit',sans-serif;font-weight:700;font-size:.72rem;padding:5px 12px;border-radius:9999px;text-decoration:none;">
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.4 8.4 0 0 1-12.4 7.4L3 20.5l1.7-5.4A8.4 8.4 0 1 1 21 11.5z"/></svg>
        WhatsApp
      </a>
    </div>
  </div>
  <!-- TOC Nav -->
  <div id="toc-nav">
    <div style="max-width:680px;margin:0 auto;padding:0 8px;">
      <a href="#sec1" class="toc-chip">1. Introduction</a>
      <a href="#sec2" class="toc-chip">2. ERP Benefits</a>
      <a href="#sec3" class="toc-chip">3. Why Addis Tech</a>
      <a href="#sec4" class="toc-chip">4. Why Odoo ERP</a>
      <a href="#sec5" class="toc-chip">5. Core Applications</a>
      <a href="#sec6" class="toc-chip">6. Module Profiles</a>
      <a href="#sec7" class="toc-chip">7. Add-ons &amp; AI</a>
      <a href="#sec8" class="toc-chip">8. Industries</a>
      <a href="#sec9" class="toc-chip">9. Implementation</a>
      <a href="#sec10" class="toc-chip">10. Project Team</a>
      <a href="#sec11" class="toc-chip">11. Next Steps</a>
    </div>
  </div>
</div>
'''

# ── Section 1 ──
SEC1 = '''
<div id="sec1" class="doc-section" style="padding:24px 16px;max-width:680px;margin:0 auto;">
  <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;">
    <span class="sec-pill">1</span>
    <h2 class="sec-title">Introduction &amp; Executive Context</h2>
  </div>
  <hr class="sec-rule">

  <div class="callout">
    Navigating digital transformation requires localized ERP solutions that align directly with Ethiopian statutory tax laws, fiscal calendars, and commercial operating realities.
  </div>

  <p style="font-size:.84rem;color:#2C2C3E;line-height:1.65;margin-bottom:12px;">
    In today&rsquo;s fast-evolving commercial landscape, Ethiopian organizations often face operational friction caused by fragmented workflows and manual administration. Key business functions&mdash;such as sales, procurement, inventory, manufacturing, human resources, and financial management&mdash;are inherently interdependent. However, when operated in isolated departmental silos, organizations encounter administrative bottlenecks, redundant data entry, routine errors, and inflated operating costs.
  </p>

  <p style="font-size:.84rem;color:#2C2C3E;line-height:1.65;margin-bottom:16px;">
    Navigating digital transformation can also present significant challenges for local enterprises. Off-the-shelf global software frequently fails to deliver expected outcomes because it lacks local customization and does not align with the operational practices, statutory tax requirements, and commercial realities of the Ethiopian market.
  </p>

  <p style="font-family:'Outfit',sans-serif;font-size:.92rem;font-weight:700;color:#1B1464;margin-bottom:8px;">The Enterprise Resource Planning (ERP) Solution</p>

  <p style="font-size:.84rem;color:#2C2C3E;line-height:1.65;margin-bottom:12px;">
    An <strong>Enterprise Resource Planning (ERP)</strong> system resolves operational challenges by consolidating company data into a single, unified platform. Rather than maintaining separate applications for each department, an ERP automates routine operational tasks and facilitates seamless cross-departmental information flow without manual intervention.
  </p>

  <p style="font-size:.84rem;color:#2C2C3E;line-height:1.65;">
    <strong>Addis Tech PLC</strong> bridges business operations with modern technology by delivering end-to-end digital transformation tailored specifically for the Ethiopian enterprise landscape. By combining deep business consulting with dedicated software engineering, Addis Tech extends beyond simple software implementation to re-engineer core processes for sustainable competitive advantage.
  </p>
</div>
<div style="border-top:6px solid #F0F0FA;"></div>
'''

# ── Section 2 ──
SEC2 = '''
<div id="sec2" class="doc-section" style="padding:24px 16px;max-width:680px;margin:0 auto;">
  <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;">
    <span class="sec-pill">2</span>
    <h2 class="sec-title">Benefits of an ERP System</h2>
  </div>
  <hr class="sec-rule">

  <p style="font-size:.84rem;color:#2C2C3E;line-height:1.65;margin-bottom:16px;">
    Implementing an Enterprise Resource Planning (ERP) system provides organizations with a robust foundation for modernizing operational workflows and driving sustainable business growth. Below are the core benefits and objectives achieved through ERP integration:
  </p>

  <div style="display:flex;flex-direction:column;">
    <div class="feat-item">
      <span class="feat-dot">●</span>
      <div><span class="feat-title">Provides Real-time Information and Data: </span><span class="feat-desc">An ERP systematically unifies business data and information flow across all departments.</span></div>
    </div>
    <div class="feat-item">
      <span class="feat-dot">●</span>
      <div><span class="feat-title">Improved Collaboration: </span><span class="feat-desc">Provides cross-departmental data access to eliminate communication silos and help employees see the big picture.</span></div>
    </div>
    <div class="feat-item">
      <span class="feat-dot">●</span>
      <div><span class="feat-title">Allows for Increased Productivity: </span><span class="feat-desc">Eliminates repetitive manual tasks, saving valuable time so staff can focus on core business growth.</span></div>
    </div>
    <div class="feat-item">
      <span class="feat-dot">●</span>
      <div><span class="feat-title">Total Visibility: </span><span class="feat-desc">Delivers complete visibility into key processes for staff and leadership based on customized access permissions.</span></div>
    </div>
    <div class="feat-item">
      <span class="feat-dot">●</span>
      <div><span class="feat-title">Improved Reporting and Planning: </span><span class="feat-desc">Unifies reporting across all functions, enabling seamless cross-departmental analysis without messy spreadsheets.</span></div>
    </div>
    <div class="feat-item">
      <span class="feat-dot">●</span>
      <div><span class="feat-title">Customer Service: </span><span class="feat-desc">Centralizes client information so sales teams can focus on customer relationships rather than manual data entry.</span></div>
    </div>
    <div class="feat-item">
      <span class="feat-dot">●</span>
      <div><span class="feat-title">Data Security and Quality: </span><span class="feat-desc">Enhances collaboration through centralized data while enforcing granular role-based permissions and robust intrinsic security controls.</span></div>
    </div>
    <div class="feat-item">
      <span class="feat-dot">●</span>
      <div><span class="feat-title">Improved Collaboration and Workflows: </span><span class="feat-desc">Funnels interdepartmental data into one central location, giving teams instant access to the information they need to collaborate seamlessly.</span></div>
    </div>
    <div class="feat-item">
      <span class="feat-dot">●</span>
      <div><span class="feat-title">Standardized Business Processes: </span><span class="feat-desc">Adopts proven industry best practices to help businesses standardize operations and boost overall efficiency.</span></div>
    </div>
    <div class="feat-item">
      <span class="feat-dot">●</span>
      <div><span class="feat-title">Facilitated Regulatory Compliance: </span><span class="feat-desc">Simplifies compliance using validated data and automated reporting tools that drastically lower audit costs.</span></div>
    </div>
    <div class="feat-item">
      <span class="feat-dot">●</span>
      <div><span class="feat-title">Superior Scalability: </span><span class="feat-desc">Having a system in place that can elegantly and efficiently accommodate a company&rsquo;s growth is of the utmost importance, and the right ERP system makes it easy.</span></div>
    </div>
  </div>
</div>
<div style="border-top:6px solid #F0F0FA;"></div>
'''

# ── Section 3 ──
SEC3 = '''
<div id="sec3" class="doc-section" style="padding:24px 16px;max-width:680px;margin:0 auto;">
  <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;">
    <span class="sec-pill">3</span>
    <h2 class="sec-title">Why Choose Addis Tech?</h2>
  </div>
  <hr class="sec-rule">

  <p style="font-size:.84rem;color:#2C2C3E;line-height:1.65;margin-bottom:16px;">
    Backed by its hands-on World-class systems and functional consultants, Addis Tech PLC combines advanced system development with specialized software engineering to re-engineer business processes for long-term competitive advantage. Rather than simply deploying software, Addis Tech assesses unique business requirements to implement internationally proven ERP systems adapted specifically to the Ethiopian commercial and regulatory context.
  </p>

  <div style="display:flex;flex-direction:column;">
    <div class="feat-item">
      <span class="feat-dot">●</span>
      <div><span class="feat-title">Integrates All Key Business Functions: </span><span class="feat-desc">Connects interlinked operations across all departments into a single centralized database, eliminating administrative bottlenecks and manual processes.</span></div>
    </div>
    <div class="feat-item">
      <span class="feat-dot">●</span>
      <div><span class="feat-title">Automated Real-Time Information Flow: </span><span class="feat-desc">Modules share data automatically without human intervention, delivering real-time operational visibility and fostering seamless interdepartmental communication.</span></div>
    </div>
    <div class="feat-item">
      <span class="feat-dot">●</span>
      <div><span class="feat-title">Tailored to the Ethiopian Business Context: </span><span class="feat-desc">Global ERP solutions are customized and reconfigured to align with local Ethiopian operating requirements, tax frameworks, and business perspectives.</span></div>
    </div>
    <div class="feat-item">
      <span class="feat-dot">●</span>
      <div><span class="feat-title">Modular &amp; Tailored Implementation: </span><span class="feat-desc">Deployments follow a phased approach, identifying and implementing the highest-priority modules first to maximize immediate business value.</span></div>
    </div>
    <div class="feat-item">
      <span class="feat-dot">●</span>
      <div><span class="feat-title">Future-Proof Scalability: </span><span class="feat-desc">Flexible system architecture enables organizations to seamlessly integrate new modules or connect third-party applications as business operations expand.</span></div>
    </div>
    <div class="feat-item">
      <span class="feat-dot">●</span>
      <div><span class="feat-title">Affordable &amp; High-ROI Pricing: </span><span class="feat-desc">Delivers feature-rich, world-class ERP software at cost-effective rates designed to make digital transformation accessible.</span></div>
    </div>
    <div class="feat-item">
      <span class="feat-dot">●</span>
      <div><span class="feat-title">Cloud &amp; Mobile Mobility: </span><span class="feat-desc">Supports both local network installations and cloud-hosted environments, allowing secure system access from any device, anywhere with an internet connection.</span></div>
    </div>
    <div class="feat-item">
      <span class="feat-dot">●</span>
      <div><span class="feat-title">Flexible Deployment Options (Full or Partial): </span><span class="feat-desc">Accommodates step-by-step module rollouts for growing enterprises as well as full core suite implementations for established businesses.</span></div>
    </div>
    <div class="feat-item">
      <span class="feat-dot">●</span>
      <div><span class="feat-title">Internationally Proven Platforms: </span><span class="feat-desc">Exclusively implements globally recognized ERP systems tested over decades&mdash;such as Odoo, which features over 7 million active users, 100+ modules, 17+ years of refinement, and support for up to 10,000 active users simultaneously.</span></div>
    </div>
    <div class="feat-item">
      <span class="feat-dot">●</span>
      <div><span class="feat-title">Service Guarantee: </span><span class="feat-desc">Backed by 100% confidence in system reliability, providing a complimentary 1-year warranty to fix any system errors free of charge.</span></div>
    </div>
  </div>
</div>
<div style="border-top:6px solid #F0F0FA;"></div>
'''

# ── Section 4 ──
SEC4 = '''
<div id="sec4" class="doc-section" style="padding:24px 16px;max-width:680px;margin:0 auto;">
  <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;">
    <span class="sec-pill">4</span>
    <h2 class="sec-title">Why Odoo ERP?</h2>
  </div>
  <hr class="sec-rule">

  <p style="font-family:'Outfit',sans-serif;font-size:.9rem;font-weight:600;color:#003B95;font-style:italic;margin-bottom:12px;">The Smart, Reliable, and Future-Proof Choice for Ethiopian Businesses.</p>

  <p style="font-size:.84rem;color:#2C2C3E;line-height:1.65;margin-bottom:14px;">
    Running a business in Ethiopia comes with unique practical challenges. Most business owners find themselves stuck between two bad options:
  </p>

  <div class="tbl-wrap">
    <table>
      <thead>
        <tr>
          <th style="width:35%;">Legacy / Traditional Option</th>
          <th>Operational Disadvantages &amp; Bottlenecks</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Basic, Disconnected Systems</strong><br><em style="font-size:.75rem;color:#888;">(e.g., Peachtree, Excel)</em></td>
          <td>Cannot talk to warehouse, store, or purchasing teams. Staff spend hours entering the same numbers twice, leading to missing stock, tax filing mistakes, and lost money.</td>
        </tr>
        <tr>
          <td><strong>Big Legacy Software</strong><br><em style="font-size:.75rem;color:#888;">(e.g., SAP, Oracle)</em></td>
          <td>Built for massive global conglomerates, demand huge sums of scarce foreign currency upfront, take over a year to set up, and are far too complicated for local staff.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <p style="font-size:.84rem;color:#2C2C3E;line-height:1.65;margin:14px 0;">
    <strong>Odoo ERP gives you the best of both worlds.</strong> It brings your entire company&mdash;sales, warehouse, accounting, purchasing, and staff records&mdash;into one unified, easy-to-use system accessible from your computer or mobile phone.
  </p>

  <p style="font-family:'Outfit',sans-serif;font-size:.9rem;font-weight:700;color:#1B1464;margin-bottom:10px;">Key Advantages of Odoo ERP</p>

  <div style="display:flex;flex-direction:column;">
    <div class="feat-item">
      <span class="feat-dot">●</span>
      <div><span class="feat-title">Fully Ready for Ethiopian Taxes &amp; E-Invoicing: </span><span class="feat-desc">Odoo accounting replaces tools like Peachtree with higher accuracy, less manual work, and direct warehouse/sales integration. It easily handles Ministry of Revenues (MOR) tax rules&mdash;including VAT, Withholding Tax, and fiscal printers&mdash;and fully supports upcoming e-receipt and e-invoicing standards.</span></div>
    </div>
    <div class="feat-item">
      <span class="feat-dot">●</span>
      <div><span class="feat-title">Native Amharic Support &amp; Local Fiscal Calendars: </span><span class="feat-desc">Odoo supports Amharic natively, making it comfortable for all team members, with plans to add more local languages. It can also be configured to match your specific business tax year and reporting periods.</span></div>
    </div>
    <div class="feat-item">
      <span class="feat-dot">●</span>
      <div><span class="feat-title">World-Class Global Trust &amp; Scale: </span><span class="feat-desc">Odoo is trusted globally by over 28 million active users across 200,000+ organizations. Its robust architecture smoothly supports up to 100,000 active users simultaneously without performance loss. Odoo provides over 50,000 training videos and detailed user guides to help your staff master every tool at their own pace. Your business never gets left in the dark.</span></div>
    </div>
    <div class="feat-item">
      <span class="feat-dot">●</span>
      <div><span class="feat-title">Easy to Use on Any Device (Even Mobile Phones): </span><span class="feat-desc">Designed like a modern smartphone app, Odoo ensures high user adoption. Managers can track approvals, sales, and inventory directly from their mobile devices anytime.</span></div>
    </div>
    <div class="feat-item">
      <span class="feat-dot">●</span>
      <div><span class="feat-title">Enterprise-Grade Security &amp; Auto Backup: </span><span class="feat-desc">Protect financial and customer data using two-factor authentication (2FA), granular access controls, and automated data backups.</span></div>
    </div>
    <div class="feat-item">
      <span class="feat-dot">●</span>
      <div><span class="feat-title">Endless Customization &amp; Seamless Integrations: </span><span class="feat-desc">Odoo can be tailored to match your exact business rules and connects smoothly with external software or local payment platforms like Telebirr via API integrations.</span></div>
    </div>
    <div class="feat-item">
      <span class="feat-dot">●</span>
      <div><span class="feat-title">Continuous Yearly Upgrades: </span><span class="feat-desc">Major yearly updates introduce new features, boost processing speeds, and enhance security to keep your business running on modern technology.</span></div>
    </div>
  </div>
</div>
<div style="border-top:6px solid #F0F0FA;"></div>
'''

with open("sec1_4.py","w",encoding="utf-8") as f:
    f.write('COVER = ' + repr(COVER) + '\n')
    f.write('STICKY_HEADER = ' + repr(STICKY_HEADER) + '\n')
    f.write('SEC1 = ' + repr(SEC1) + '\n')
    f.write('SEC2 = ' + repr(SEC2) + '\n')
    f.write('SEC3 = ' + repr(SEC3) + '\n')
    f.write('SEC4 = ' + repr(SEC4) + '\n')

print("sec1_4.py written")
