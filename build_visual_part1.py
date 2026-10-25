# -*- coding: utf-8 -*-
# Visual-Oriented Addis Tech Odoo ERP Guide — Part 1 (Head, Cover, Nav, Sections 1-5)

HEAD_VISUAL = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>Odoo ERP Visual Overview &amp; Implementation Guide | Addis Tech PLC</title>
<meta name="description" content="Visual-oriented overview of Odoo ERP and Addis Tech PLC implementation methodology for Ethiopian businesses.">
<meta name="theme-color" content="#1B1464">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@500;600;700;800&family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
<script src="https://cdn.tailwindcss.com"></script>
<style>
*{box-sizing:border-box;margin:0;padding:0;}
html{scroll-behavior:smooth;background:#F4F5FA;}
body{font-family:'Plus Jakarta Sans',sans-serif;color:#1A1A2E;background:#F4F5FA;overflow-x:hidden;padding-top:98px;padding-bottom:66px;}

/* ── Reading Progress Bar ── */
#progress-bar{position:fixed;top:0;left:0;height:3px;width:0%;background:linear-gradient(90deg,#FFA600,#714B67,#017E84,#06A225);z-index:9999;transition:width .1s linear;pointer-events:none;}

/* ── Sticky Header ── */
#sticky-header{position:fixed;top:3px;left:0;right:0;z-index:1000;background:#1B1464;border-bottom:1px solid rgba(255,255,255,.12);transition:transform .3s ease,opacity .25s ease,background-color .3s ease;transform:translateY(0);}
#sticky-header.odoo-mode{background:#53354B;}
#sticky-header.hidden-up{transform:translateY(-110%);opacity:0;pointer-events:none;}

/* ── Section Chip Nav ── */
#toc-nav{background:#120D45;border-bottom:1px solid rgba(255,255,255,.1);overflow-x:auto;white-space:nowrap;scrollbar-width:none;-webkit-overflow-scrolling:touch;transition:background-color .3s ease;}
#sticky-header.odoo-mode #toc-nav{background:#3E2638;}
#toc-nav::-webkit-scrollbar{display:none;}
.toc-chip{display:inline-flex;align-items:center;padding:5px 11px;margin:5px 3px;border-radius:9999px;font-size:.69rem;font-weight:600;color:rgba(240,240,255,.85);background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.12);text-decoration:none;transition:all .2s;cursor:pointer;white-space:nowrap;flex-shrink:0;}
.toc-chip.odoo-chip{border-color:rgba(1,126,132,.55);background:rgba(113,75,103,.32);}
.toc-chip.active,.toc-chip:hover{background:#FFA600;color:#000C1D;border-color:#FFA600;font-weight:700;}
.toc-chip.odoo-chip.active{background:#00A09D;color:#fff;border-color:#00A09D;}

/* ── Section Container & Headers ── */
.v-sec{max-width:680px;margin:0 auto;padding:22px 12px;background:#fff;}
.v-divider{height:8px;background:#ECEEF8;max-width:680px;margin:0 auto;}
.sec-head{display:flex;align-items:center;gap:9px;margin-bottom:6px;}
.sec-pill{display:inline-flex;align-items:center;justify-content:center;min-width:26px;height:26px;padding:0 8px;border-radius:8px;background:#1B1464;color:#FFA600;font-size:.72rem;font-weight:800;font-family:'Outfit',sans-serif;flex-shrink:0;}
.sec-title{font-family:'Outfit',sans-serif;font-size:1.15rem;font-weight:800;color:#1B1464;line-height:1.25;}
.sec-sub{font-size:.78rem;color:#003B95;font-weight:600;margin-bottom:12px;}
.sec-rule{border:none;border-top:1.5px solid #E6E8F4;margin:8px 0 14px 0;}

/* ── Odoo Brand Zone (Sections 4, 5, 6) ── */
.odoo-zone-wrap{background:linear-gradient(180deg,#F9F5F8 0%,#F3F9F9 100%);border-top:3px solid #714B67;border-bottom:3px solid #017E84;}
.odoo-sec{max-width:680px;margin:0 auto;padding:22px 12px;background:transparent;}
.odoo-divider{height:8px;background:linear-gradient(90deg,rgba(113,75,103,.12),rgba(1,126,132,.12));max-width:680px;margin:0 auto;}
.odoo-pill{background:#714B67;color:#fff;}
.odoo-title{color:#53354B;}
.odoo-sub{color:#017E84;}
.odoo-rule{border-top-color:#E5D8E2;}
.odoo-badge{display:inline-flex;align-items:center;gap:6px;background:linear-gradient(90deg,#714B67,#017E84);color:#fff;font-family:'Outfit',sans-serif;font-size:.66rem;font-weight:700;text-transform:uppercase;letter-spacing:.07em;padding:4px 10px;border-radius:999px;margin-bottom:8px;}

/* ── Visual Cards & Grids ── */
.grid-2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px;}
.grid-3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:6px;}
.v-card{background:#F8F9FE;border:1px solid #E2E5F3;border-radius:10px;padding:10px;display:flex;flex-direction:column;gap:5px;}
.v-card-row{background:#F8F9FE;border:1px solid #E2E5F3;border-radius:10px;padding:10px 12px;display:flex;align-items:flex-start;gap:10px;}
.v-icon{width:32px;height:32px;border-radius:8px;background:#1B1464;color:#FFA600;display:flex;align-items:center;justify-content:center;flex-shrink:0;}
.v-icon-blue{background:#E5F0FC;color:#003B95;}
.v-icon-green{background:#E6F7EA;color:#06A225;}
.v-icon-plum{background:#714B67;color:#fff;}
.v-icon-teal{background:#017E84;color:#fff;}
.v-card-title{font-family:'Outfit',sans-serif;font-size:.82rem;font-weight:700;color:#1B1464;line-height:1.25;}
.v-card-desc{font-size:.74rem;color:#444462;line-height:1.4;}

/* ── Stat / Counter Strip ── */
.stat-strip{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:6px;margin:12px 0;}
.stat-box{background:linear-gradient(145deg,#1B1464,#0B0642);color:#fff;border-radius:10px;padding:10px 6px;text-align:center;border:1px solid rgba(255,255,255,.1);}
.stat-num{font-family:'Outfit',sans-serif;font-size:1.05rem;font-weight:800;color:#FFA600;line-height:1.1;}
.stat-lbl{font-size:.63rem;color:rgba(240,240,255,.85);margin-top:3px;line-height:1.2;}
.odoo-stat-box{background:linear-gradient(145deg,#714B67,#4E3247);}
.odoo-stat-teal{background:linear-gradient(145deg,#017E84,#015B60);}

/* ── Accordion (Section 6 Odoo Modules) ── */
.mod-acc{background:#fff;border:1px solid #DFCEDA;border-left:4px solid #714B67;border-radius:10px;margin-bottom:8px;overflow:hidden;transition:box-shadow .2s;}
.mod-acc.teal-left{border-left-color:#017E84;}
.mod-acc.open{box-shadow:0 4px 14px rgba(113,75,103,.12);}
.mod-trig{width:100%;display:flex;align-items:center;gap:9px;padding:11px 12px;background:none;border:none;text-align:left;cursor:pointer;}
.mod-num{font-family:'Outfit',sans-serif;font-size:.7rem;font-weight:800;padding:3px 7px;border-radius:6px;background:#714B67;color:#fff;flex-shrink:0;}
.mod-acc.teal-left .mod-num{background:#017E84;}
.mod-head-wrap{flex:1;min-width:0;}
.mod-title{font-family:'Outfit',sans-serif;font-size:.86rem;font-weight:700;color:#4E3247;line-height:1.2;}
.mod-tag{font-size:.69rem;color:#017E84;font-weight:600;display:block;margin-top:1px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}
.mod-chev{width:18px;height:18px;color:#714B67;transition:transform .25s;flex-shrink:0;}
.mod-acc.open .mod-chev{transform:rotate(180deg);}
.mod-body{display:none;padding:0 12px 12px 12px;border-top:1px dashed #EADCE6;}
.mod-acc.open .mod-body{display:block;}
.mod-feat-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:6px;margin-top:8px;}
.mod-feat-chip{background:#FAF6F9;border:1px solid #E9DAE5;border-radius:8px;padding:7px 8px;}
.mod-acc.teal-left .mod-feat-chip{background:#F3FAFA;border-color:#D2ECEC;}
.mod-feat-t{font-family:'Outfit',sans-serif;font-size:.74rem;font-weight:700;color:#53354B;display:flex;align-items:center;gap:4px;margin-bottom:2px;}
.mod-acc.teal-left .mod-feat-t{color:#015B60;}
.mod-feat-d{font-size:.69rem;color:#4A4A68;line-height:1.35;}

/* ── Filter Pills (Section 6 & Section 8) ── */
.filter-bar{display:flex;gap:5px;overflow-x:auto;padding-bottom:6px;margin-bottom:10px;scrollbar-width:none;}
.filter-bar::-webkit-scrollbar{display:none;}
.filter-pill{padding:5px 11px;border-radius:999px;font-size:.7rem;font-weight:700;font-family:'Outfit',sans-serif;border:1px solid #D9C3D3;background:#fff;color:#53354B;cursor:pointer;white-space:nowrap;flex-shrink:0;}
.filter-pill.active{background:#714B67;color:#fff;border-color:#714B67;}

/* ── Industry Selector Tiles (Section 8) ── */
.ind-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:6px;margin-bottom:10px;}
.ind-tile{background:#F5F7FF;border:1.5px solid #DCE1F5;border-radius:10px;padding:8px 6px;text-align:center;cursor:pointer;transition:all .2s;display:flex;flex-direction:column;align-items:center;gap:4px;}
.ind-tile.active{background:#1B1464;border-color:#1B1464;color:#fff;box-shadow:0 3px 10px rgba(27,20,100,.22);}
.ind-tile-num{font-size:.62rem;font-weight:800;color:#003B95;background:#E5F0FC;padding:1px 6px;border-radius:99px;}
.ind-tile.active .ind-tile-num{background:#FFA600;color:#000C1D;}
.ind-tile-name{font-family:'Outfit',sans-serif;font-size:.71rem;font-weight:700;line-height:1.2;color:#1B1464;}
.ind-tile.active .ind-tile-name{color:#fff;}
.ind-view{display:none;background:#F8F9FE;border:1.5px solid #1B1464;border-radius:10px;padding:12px;}
.ind-view.active{display:block;}

/* ── Bottom Dock & Back Top ── */
#bottom-dock{position:fixed;bottom:0;left:0;right:0;z-index:1000;background:rgba(27,20,100,.96);backdrop-filter:blur(12px);border-top:1px solid rgba(255,255,255,.12);padding:7px 10px;padding-bottom:max(7px,env(safe-area-inset-bottom));transition:transform .3s ease;}
#bottom-dock.hidden-down{transform:translateY(110%);}
.dock-inner{max-width:680px;margin:0 auto;display:grid;grid-template-columns:1.5fr 1fr 1fr auto;gap:6px;align-items:center;}
.dock-btn{display:flex;align-items:center;justify-content:center;gap:4px;background:rgba(255,255,255,.11);border:1px solid rgba(255,255,255,.18);color:#fff;border-radius:8px;padding:6px 6px;text-decoration:none;font-size:.68rem;font-weight:700;min-height:38px;white-space:nowrap;}
.dock-cta{background:#FFA600;color:#000C1D;border:none;font-weight:800;font-size:.72rem;}
.dock-doc{background:#fff;color:#1B1464;border:none;font-weight:800;}
#back-top{position:fixed;bottom:68px;right:12px;z-index:900;display:none;width:36px;height:36px;border-radius:50%;background:#1B1464;color:#FFA600;border:1px solid rgba(255,255,255,.2);cursor:pointer;align-items:center;justify-content:center;box-shadow:0 4px 12px rgba(27,20,100,.35);}
#back-top.show{display:flex;}

@media (max-width:360px){
  .stat-strip{grid-template-columns:repeat(2,1fr);}
  .mod-feat-grid{grid-template-columns:1fr;}
}
@media print{
  #sticky-header,#bottom-dock,#back-top,#progress-bar{display:none!important;}
  body{padding:0!important;}
  .mod-body,.ind-view{display:block!important;}
}
</style>
</head>
'''

STICKY_VISUAL = '''
<div id="progress-bar"></div>
<div id="sticky-header">
  <div style="max-width:680px;margin:0 auto;padding:6px 12px;display:flex;align-items:center;justify-content:space-between;gap:6px;">
    <div style="display:flex;align-items:center;gap:7px;">
      <div style="background:rgba(255,255,255,.12);border-radius:6px;padding:4px;display:flex;">
        <svg width="14" height="14" viewBox="0 0 20 20" fill="none"><path d="M3.334 14.166L8.334 9.166L3.334 4.166" stroke="#FFA600" stroke-linecap="round" stroke-width="1.8"/><path d="M10 15.834H16.6667" stroke="#FFA600" stroke-linecap="round" stroke-width="1.8"/></svg>
      </div>
      <span style="font-family:'Outfit',sans-serif;font-size:.88rem;font-weight:800;color:#fff;">Addis<span style="color:#FFA600;">Tech</span></span>
      <span style="font-size:.6rem;background:rgba(255,166,0,.18);color:#FFA600;padding:2px 6px;border-radius:99px;font-weight:700;">Visual Guide</span>
    </div>
    <div style="display:flex;align-items:center;gap:5px;">
      <a href="addis_tech_odoo_guide.html" style="display:inline-flex;align-items:center;gap:4px;background:#fff;color:#1B1464;font-family:'Outfit',sans-serif;font-weight:800;font-size:.68rem;padding:5px 9px;border-radius:9999px;text-decoration:none;">
        <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
        Main Document
      </a>
      <a href="https://wa.me/251911202265" target="_blank" rel="noopener" style="display:inline-flex;align-items:center;gap:4px;background:#FFA600;color:#000C1D;font-family:'Outfit',sans-serif;font-weight:800;font-size:.68rem;padding:5px 10px;border-radius:9999px;text-decoration:none;">
        <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.4 8.4 0 0 1-12.4 7.4L3 20.5l1.7-5.4A8.4 8.4 0 1 1 21 11.5z"/></svg>
        WhatsApp
      </a>
    </div>
  </div>
  <div id="toc-nav">
    <div style="max-width:680px;margin:0 auto;padding:0 6px;">
      <a href="#sec1" class="toc-chip">1. Context</a>
      <a href="#sec2" class="toc-chip">2. ERP Benefits</a>
      <a href="#sec3" class="toc-chip">3. Why Addis Tech</a>
      <a href="#sec4" class="toc-chip odoo-chip">4. Why Odoo ERP</a>
      <a href="#sec5" class="toc-chip odoo-chip">5. Core Apps</a>
      <a href="#sec6" class="toc-chip odoo-chip">6. 10 Modules</a>
      <a href="#sec7" class="toc-chip">7. AI &amp; Custom</a>
      <a href="#sec8" class="toc-chip">8. Industries</a>
      <a href="#sec9" class="toc-chip">9. Methodology</a>
      <a href="#sec10" class="toc-chip">10. Project Team</a>
      <a href="#sec11" class="toc-chip">11. Next Steps</a>
    </div>
  </div>
</div>
'''

COVER_VISUAL = '''
<div id="top"></div>
<div style="background:linear-gradient(155deg,#1B1464 0%,#0B0642 65%,#2D1846 100%);padding:22px 12px 20px 12px;">
  <div style="max-width:680px;margin:0 auto;">
    <!-- Top Brand & Mode Badge -->
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:14px;flex-wrap:wrap;gap:8px;">
      <div style="display:flex;align-items:center;gap:8px;">
        <div style="background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.2);border-radius:7px;padding:5px;display:flex;">
          <svg width="16" height="16" viewBox="0 0 20 20" fill="none"><path d="M3.334 14.166L8.334 9.166L3.334 4.166" stroke="#FFA600" stroke-linecap="round" stroke-width="1.8"/><path d="M10 15.834H16.6667" stroke="#FFA600" stroke-linecap="round" stroke-width="1.8"/></svg>
        </div>
        <span style="font-family:'Outfit',sans-serif;font-size:1.05rem;font-weight:800;color:#fff;">Addis<span style="color:#FFA600;">Tech</span> <span style="font-weight:500;font-size:.78rem;opacity:.75;">PLC</span></span>
      </div>
      <span style="font-size:.66rem;font-weight:700;color:#FFA600;background:rgba(255,166,0,.15);border:1px solid rgba(255,166,0,.35);padding:3px 9px;border-radius:99px;letter-spacing:.05em;text-transform:uppercase;">Visual Presentation &bull; 9/1/2026</span>
    </div>

    <h1 style="font-family:'Outfit',sans-serif;font-size:1.38rem;font-weight:800;color:#fff;line-height:1.22;margin-bottom:6px;">Odoo Enterprise Resource Planning (ERP) System Overview &amp; Implementation Guide</h1>
    <p style="font-size:.78rem;color:rgba(240,240,255,.8);margin-bottom:14px;font-style:italic;">Business with World-Class Digital Solutions</p>

    <!-- 3 Visual Value Pillars Infographic -->
    <div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:6px;margin-bottom:16px;">
      <div style="background:rgba(255,255,255,.09);border:1px solid rgba(255,255,255,.15);border-radius:10px;padding:9px 7px;text-align:center;">
        <div style="width:28px;height:28px;margin:0 auto 5px;border-radius:7px;background:rgba(255,166,0,.2);color:#FFA600;display:flex;align-items:center;justify-content:center;">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/></svg>
        </div>
        <p style="font-family:'Outfit',sans-serif;font-size:.7rem;font-weight:700;color:#fff;line-height:1.25;">Manage Multiple Business Operations with One System</p>
      </div>
      <div style="background:rgba(255,255,255,.09);border:1px solid rgba(255,255,255,.15);border-radius:10px;padding:9px 7px;text-align:center;">
        <div style="width:28px;height:28px;margin:0 auto 5px;border-radius:7px;background:rgba(6,162,37,.25);color:#4ADE80;display:flex;align-items:center;justify-content:center;">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
        </div>
        <p style="font-family:'Outfit',sans-serif;font-size:.7rem;font-weight:700;color:#fff;line-height:1.25;">Automate your Business Operations with One System</p>
      </div>
      <div style="background:rgba(255,255,255,.09);border:1px solid rgba(255,255,255,.15);border-radius:10px;padding:9px 7px;text-align:center;">
        <div style="width:28px;height:28px;margin:0 auto 5px;border-radius:7px;background:rgba(1,126,132,.35);color:#5EEAD4;display:flex;align-items:center;justify-content:center;">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>
        </div>
        <p style="font-family:'Outfit',sans-serif;font-size:.7rem;font-weight:700;color:#fff;line-height:1.25;">Get Auto Generated Reports with Live Dashboards</p>
      </div>
    </div>

    <!-- Hero Action Strip (Rule 6: Main Document Link Button + Primary WhatsApp) -->
    <div style="display:flex;gap:8px;flex-wrap:wrap;">
      <a href="https://wa.me/251911202265" target="_blank" rel="noopener" style="flex:1;min-width:170px;display:inline-flex;align-items:center;justify-content:center;gap:6px;background:#FFA600;color:#000C1D;font-family:'Outfit',sans-serif;font-weight:800;font-size:.8rem;padding:9px 14px;border-radius:9999px;text-decoration:none;">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.4 8.4 0 0 1-12.4 7.4L3 20.5l1.7-5.4A8.4 8.4 0 1 1 21 11.5z"/></svg>
        WhatsApp +251 91120 2265
      </a>
      <a href="addis_tech_odoo_guide.html" style="flex:1;min-width:165px;display:inline-flex;align-items:center;justify-content:center;gap:6px;background:#fff;color:#1B1464;font-family:'Outfit',sans-serif;font-weight:800;font-size:.8rem;padding:9px 14px;border-radius:9999px;text-decoration:none;box-shadow:0 3px 10px rgba(0,0,0,.22);">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#1B1464" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
        Main Document (Full Guide)
      </a>
    </div>
  </div>
</div>
'''

# ── Section 1: Introduction & Executive Context ──
SEC1_V = '''
<div id="sec1" class="v-sec">
  <div class="sec-head">
    <span class="sec-pill">1</span>
    <h2 class="sec-title">Introduction &amp; Executive Context</h2>
  </div>
  <hr class="sec-rule">

  <div style="background:#E5F0FC;border-left:3.5px solid #003B95;padding:10px 12px;border-radius:0 8px 8px 0;margin-bottom:12px;font-size:.78rem;color:#1A1A2E;line-height:1.45;font-weight:500;">
    Navigating digital transformation requires localized ERP solutions that align directly with Ethiopian statutory tax laws, fiscal calendars, and commercial operating realities.
  </div>

  <!-- Visual Infographic: Fragmented Silos vs Unified ERP Solution -->
  <div style="display:grid;grid-template-columns:1fr;gap:8px;margin-bottom:10px;">
    <!-- Before: Fragmented Departmental Silos -->
    <div style="background:#FFF5F5;border:1px solid #FECACA;border-left:4px solid #DC2626;border-radius:10px;padding:10px 12px;">
      <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:6px;">
        <span style="font-family:'Outfit',sans-serif;font-size:.8rem;font-weight:800;color:#991B1B;text-transform:uppercase;letter-spacing:.04em;">&#9888; Isolated Departmental Silos &amp; Off-the-Shelf Limits</span>
      </div>
      <div style="display:flex;flex-wrap:wrap;gap:4px;margin-bottom:7px;">
        <span style="font-size:.66rem;background:#FEE2E2;color:#991B1B;padding:2px 7px;border-radius:4px;font-weight:700;">Sales</span>
        <span style="font-size:.66rem;background:#FEE2E2;color:#991B1B;padding:2px 7px;border-radius:4px;font-weight:700;">Procurement</span>
        <span style="font-size:.66rem;background:#FEE2E2;color:#991B1B;padding:2px 7px;border-radius:4px;font-weight:700;">Inventory</span>
        <span style="font-size:.66rem;background:#FEE2E2;color:#991B1B;padding:2px 7px;border-radius:4px;font-weight:700;">Manufacturing</span>
        <span style="font-size:.66rem;background:#FEE2E2;color:#991B1B;padding:2px 7px;border-radius:4px;font-weight:700;">HR</span>
        <span style="font-size:.66rem;background:#FEE2E2;color:#991B1B;padding:2px 7px;border-radius:4px;font-weight:700;">Financial Management</span>
      </div>
      <p style="font-size:.74rem;color:#7F1D1D;line-height:1.4;">Fragmented workflows and manual administration cause <strong>administrative bottlenecks, redundant data entry, routine errors, and inflated operating costs</strong>. Off-the-shelf global software fails without local Ethiopian tax and commercial customization.</p>
    </div>

    <!-- Down Arrow Infographic Connector -->
    <div style="text-align:center;line-height:1;margin:-2px 0;">
      <span style="display:inline-flex;align-items:center;gap:5px;background:#1B1464;color:#FFA600;font-family:'Outfit',sans-serif;font-size:.68rem;font-weight:800;padding:3px 10px;border-radius:99px;">&#8595; THE ERP SOLUTION BY ADDIS TECH PLC &#8595;</span>
    </div>

    <!-- After: Unified ERP Platform -->
    <div style="background:#F0FDF4;border:1px solid #BBF7D0;border-left:4px solid #06A225;border-radius:10px;padding:10px 12px;">
      <p style="font-family:'Outfit',sans-serif;font-size:.82rem;font-weight:800;color:#14532D;margin-bottom:4px;">&#10004; Unified Platform + End-to-End Ethiopian Transformation</p>
      <p style="font-size:.74rem;color:#166534;line-height:1.42;margin-bottom:6px;">Consolidates company data into a single unified platform, automating routine tasks and enabling seamless cross-departmental information flow without manual intervention.</p>
      <div style="background:#fff;border:1px solid #DCFCE7;border-radius:7px;padding:7px 9px;font-size:.73rem;color:#1A1A2E;line-height:1.38;">
        <strong style="color:#1B1464;">Addis Tech PLC:</strong> Combines deep business consulting with dedicated software engineering to re-engineer core processes for the Ethiopian enterprise landscape.
      </div>
    </div>
  </div>
</div>
<div class="v-divider"></div>
'''

# ── Section 2: Benefits of an ERP System (11 Visual Cards) ──
SEC2_V = '''
<div id="sec2" class="v-sec">
  <div class="sec-head">
    <span class="sec-pill">2</span>
    <h2 class="sec-title">Benefits of an ERP System</h2>
  </div>
  <p class="sec-sub">Core objectives achieved through unified ERP integration</p>

  <div class="grid-2">
    <div class="v-card">
      <div style="display:flex;align-items:center;gap:7px;">
        <div class="v-icon"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg></div>
        <span class="v-card-title">Real-time Information &amp; Data</span>
      </div>
      <p class="v-card-desc">Systematically unifies business data and information flow across all departments.</p>
    </div>

    <div class="v-card">
      <div style="display:flex;align-items:center;gap:7px;">
        <div class="v-icon v-icon-blue"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/></svg></div>
        <span class="v-card-title">Improved Collaboration</span>
      </div>
      <p class="v-card-desc">Cross-departmental data access eliminates communication silos so staff see the big picture.</p>
    </div>

    <div class="v-card">
      <div style="display:flex;align-items:center;gap:7px;">
        <div class="v-icon v-icon-green"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg></div>
        <span class="v-card-title">Increased Productivity</span>
      </div>
      <p class="v-card-desc">Eliminates repetitive manual tasks so staff focus on core business growth.</p>
    </div>

    <div class="v-card">
      <div style="display:flex;align-items:center;gap:7px;">
        <div class="v-icon"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg></div>
        <span class="v-card-title">Total Visibility</span>
      </div>
      <p class="v-card-desc">Complete visibility into key processes for staff and leadership via customized permissions.</p>
    </div>

    <div class="v-card">
      <div style="display:flex;align-items:center;gap:7px;">
        <div class="v-icon v-icon-blue"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg></div>
        <span class="v-card-title">Improved Reporting &amp; Planning</span>
      </div>
      <p class="v-card-desc">Unifies reporting across functions for seamless analysis without messy spreadsheets.</p>
    </div>

    <div class="v-card">
      <div style="display:flex;align-items:center;gap:7px;">
        <div class="v-icon v-icon-green"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg></div>
        <span class="v-card-title">Customer Service</span>
      </div>
      <p class="v-card-desc">Centralizes client information so sales teams focus on relationships instead of data entry.</p>
    </div>

    <div class="v-card">
      <div style="display:flex;align-items:center;gap:7px;">
        <div class="v-icon"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div>
        <span class="v-card-title">Data Security &amp; Quality</span>
      </div>
      <p class="v-card-desc">Centralized data with granular role-based permissions and intrinsic security controls.</p>
    </div>

    <div class="v-card">
      <div style="display:flex;align-items:center;gap:7px;">
        <div class="v-icon v-icon-blue"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><line x1="8.59" y1="13.51" x2="15.42" y2="17.49"/><line x1="15.41" y1="6.51" x2="8.59" y2="10.49"/></svg></div>
        <span class="v-card-title">Collaboration &amp; Workflows</span>
      </div>
      <p class="v-card-desc">Funnels interdepartmental data into one central location for instant team access.</p>
    </div>

    <div class="v-card">
      <div style="display:flex;align-items:center;gap:7px;">
        <div class="v-icon v-icon-green"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 11 12 14 22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg></div>
        <span class="v-card-title">Standardized Processes</span>
      </div>
      <p class="v-card-desc">Adopts proven industry best practices to standardize operations and boost efficiency.</p>
    </div>

    <div class="v-card">
      <div style="display:flex;align-items:center;gap:7px;">
        <div class="v-icon"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg></div>
        <span class="v-card-title">Regulatory Compliance</span>
      </div>
      <p class="v-card-desc">Validated data and automated reporting tools simplify compliance and lower audit costs.</p>
    </div>

    <div class="v-card" style="grid-column:span 2;">
      <div style="display:flex;align-items:center;gap:7px;">
        <div class="v-icon v-icon-blue"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/></svg></div>
        <span class="v-card-title">Superior Scalability</span>
        <span style="font-size:.73rem;color:#444462;margin-left:4px;">— Elegantly and efficiently accommodates company growth as operations expand.</span>
      </div>
    </div>
  </div>
</div>
<div class="v-divider"></div>
'''

# ── Section 3: Why Choose Addis Tech? ──
SEC3_V = '''
<div id="sec3" class="v-sec">
  <div class="sec-head">
    <span class="sec-pill">3</span>
    <h2 class="sec-title">Why Choose Addis Tech?</h2>
  </div>
  <p class="sec-sub">Hands-on world-class functional consultants &amp; software engineering adapted for Ethiopia</p>

  <!-- Stat Counter Infographic -->
  <div class="stat-strip">
    <div class="stat-box">
      <div class="stat-num">7M+</div>
      <div class="stat-lbl">Active Platform Users</div>
    </div>
    <div class="stat-box">
      <div class="stat-num">100+</div>
      <div class="stat-lbl">Integrated Modules</div>
    </div>
    <div class="stat-box">
      <div class="stat-num">17+ Yrs</div>
      <div class="stat-lbl">Global Refinement</div>
    </div>
    <div class="stat-box" style="background:linear-gradient(145deg,#06A225,#047A1B);">
      <div class="stat-num" style="color:#fff;">1-Year</div>
      <div class="stat-lbl" style="color:#E6F7EA;">Free Error Warranty</div>
    </div>
  </div>

  <div class="grid-2">
    <div class="v-card">
      <span class="v-card-title">&#9679; Integrates All Key Functions</span>
      <p class="v-card-desc">Connects all departments into one centralized database, eliminating bottlenecks and manual work.</p>
    </div>
    <div class="v-card">
      <span class="v-card-title">&#9679; Automated Real-Time Flow</span>
      <p class="v-card-desc">Modules share data automatically without human intervention for real-time visibility.</p>
    </div>
    <div class="v-card">
      <span class="v-card-title">&#9679; Tailored to Ethiopia</span>
      <p class="v-card-desc">Customized and reconfigured to align with Ethiopian operating rules and tax frameworks.</p>
    </div>
    <div class="v-card">
      <span class="v-card-title">&#9679; Modular Phased Rollout</span>
      <p class="v-card-desc">Deploys highest-priority modules first to maximize immediate business value.</p>
    </div>
    <div class="v-card">
      <span class="v-card-title">&#9679; Future-Proof Scalability</span>
      <p class="v-card-desc">Seamlessly integrate new modules or connect third-party apps as operations expand.</p>
    </div>
    <div class="v-card">
      <span class="v-card-title">&#9679; Affordable &amp; High-ROI</span>
      <p class="v-card-desc">Feature-rich, world-class ERP software at cost-effective rates for accessible transformation.</p>
    </div>
    <div class="v-card">
      <span class="v-card-title">&#9679; Cloud &amp; Mobile Mobility</span>
      <p class="v-card-desc">Local network or cloud-hosted environments accessible securely from any device anywhere.</p>
    </div>
    <div class="v-card">
      <span class="v-card-title">&#9679; Full or Partial Deployment</span>
      <p class="v-card-desc">Step-by-step module rollouts for growing firms or full core suites for established enterprises.</p>
    </div>
    <div class="v-card">
      <span class="v-card-title">&#9679; Internationally Proven</span>
      <p class="v-card-desc">Tested over 17+ years with 7M+ users, 100+ modules, supporting up to 10,000 simultaneous users.</p>
    </div>
    <div class="v-card" style="background:#F0FDF4;border-color:#BBF7D0;">
      <span class="v-card-title" style="color:#06A225;">&#10004; 1-Year Service Guarantee</span>
      <p class="v-card-desc" style="color:#166534;">100% confidence in reliability with a complimentary 1-year warranty to fix system errors free of charge.</p>
    </div>
  </div>
</div>
'''

# ── ODOO BRAND ZONE: SECTIONS 4, 5, 6 (Rule 5) ──
SEC4_V = '''
<div class="odoo-zone-wrap">
  <div id="sec4" class="odoo-sec">
    <div class="odoo-badge">
      <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="9"/></svg>
      Odoo ERP Official Ecosystem &bull; Sections 4 – 6
    </div>
    <div class="sec-head">
      <span class="sec-pill odoo-pill">4</span>
      <h2 class="sec-title odoo-title">Why Odoo ERP?</h2>
    </div>
    <p class="sec-sub odoo-sub">The Smart, Reliable, and Future-Proof Choice for Ethiopian Businesses</p>

    <!-- 3-Way Comparison Visual Infographic -->
    <div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px;margin-bottom:8px;">
      <div style="background:#FFF5F5;border:1px solid #FECACA;border-top:3px solid #DC2626;border-radius:10px;padding:10px;">
        <div style="font-size:.65rem;font-weight:800;color:#DC2626;text-transform:uppercase;margin-bottom:2px;">&#10006; Bad Option 1</div>
        <p style="font-family:'Outfit',sans-serif;font-size:.82rem;font-weight:800;color:#7F1D1D;margin-bottom:4px;">Basic, Disconnected Systems <span style="font-weight:500;font-size:.7rem;">(Peachtree, Excel)</span></p>
        <p style="font-size:.72rem;color:#991B1B;line-height:1.38;">Cannot talk to warehouse, store, or purchasing. Staff enter numbers twice—causing missing stock, tax mistakes, and lost money.</p>
      </div>

      <div style="background:#FFF5F5;border:1px solid #FECACA;border-top:3px solid #DC2626;border-radius:10px;padding:10px;">
        <div style="font-size:.65rem;font-weight:800;color:#DC2626;text-transform:uppercase;margin-bottom:2px;">&#10006; Bad Option 2</div>
        <p style="font-family:'Outfit',sans-serif;font-size:.82rem;font-weight:800;color:#7F1D1D;margin-bottom:4px;">Big Legacy Software <span style="font-weight:500;font-size:.7rem;">(SAP, Oracle)</span></p>
        <p style="font-size:.72rem;color:#991B1B;line-height:1.38;">Built for massive global conglomerates, demand huge scarce foreign currency upfront, take 1+ year to set up, and are too complicated.</p>
      </div>
    </div>

    <!-- Winner Banner: Odoo ERP -->
    <div style="background:linear-gradient(135deg,#714B67 0%,#4E3247 55%,#017E84 100%);color:#fff;border-radius:10px;padding:12px;margin-bottom:12px;box-shadow:0 4px 12px rgba(113,75,103,.2);">
      <div style="display:flex;align-items:center;gap:6px;margin-bottom:4px;">
        <span style="background:#FFA600;color:#000C1D;font-family:'Outfit',sans-serif;font-size:.65rem;font-weight:800;padding:2px 8px;border-radius:99px;text-transform:uppercase;">&#10004; The Best of Both Worlds</span>
      </div>
      <p style="font-size:.78rem;line-height:1.45;color:rgba(255,255,255,.95);"><strong>Odoo ERP</strong> brings your entire company—<strong>sales, warehouse, accounting, purchasing, and staff records</strong>—into one unified, easy-to-use system accessible from your computer or mobile phone.</p>
    </div>

    <!-- Odoo Global Scale Infographic Counter Strip -->
    <div class="stat-strip">
      <div class="stat-box odoo-stat-box">
        <div class="stat-num">28M+</div>
        <div class="stat-lbl">Global Active Users</div>
      </div>
      <div class="stat-box odoo-stat-teal">
        <div class="stat-num">200K+</div>
        <div class="stat-lbl">Organizations</div>
      </div>
      <div class="stat-box odoo-stat-box">
        <div class="stat-num">100K</div>
        <div class="stat-lbl">Simultaneous Users</div>
      </div>
      <div class="stat-box odoo-stat-teal">
        <div class="stat-num">50K+</div>
        <div class="stat-lbl">Training Videos</div>
      </div>
    </div>

    <p style="font-family:'Outfit',sans-serif;font-size:.86rem;font-weight:800;color:#53354B;margin:10px 0 8px;">7 Key Advantages of Odoo ERP</p>
    <div class="grid-2">
      <div class="v-card" style="background:#fff;border-color:#DFCEDA;">
        <div style="display:flex;align-items:center;gap:7px;">
          <div class="v-icon v-icon-plum"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M9 14l2 2 4-4"/><rect x="3" y="3" width="18" height="18" rx="2"/></svg></div>
          <span class="v-card-title" style="color:#53354B;">Ethiopian Taxes &amp; E-Invoicing</span>
        </div>
        <p class="v-card-desc">Replaces Peachtree with MOR tax rules (VAT, Withholding), fiscal printers, and upcoming e-invoicing standards.</p>
      </div>

      <div class="v-card" style="background:#fff;border-color:#D2ECEC;">
        <div style="display:flex;align-items:center;gap:7px;">
          <div class="v-icon v-icon-teal"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg></div>
          <span class="v-card-title" style="color:#015B60;">Native Amharic &amp; Fiscal Calendar</span>
        </div>
        <p class="v-card-desc">Supports Amharic natively and configures directly to Ethiopian business tax years and reporting periods.</p>
      </div>

      <div class="v-card" style="background:#fff;border-color:#DFCEDA;">
        <div style="display:flex;align-items:center;gap:7px;">
          <div class="v-icon v-icon-plum"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg></div>
          <span class="v-card-title" style="color:#53354B;">World-Class Trust &amp; Scale</span>
        </div>
        <p class="v-card-desc">Trusted by 28M+ users across 200,000+ organizations; supports 100,000 concurrent users with 50,000+ training videos.</p>
      </div>

      <div class="v-card" style="background:#fff;border-color:#D2ECEC;">
        <div style="display:flex;align-items:center;gap:7px;">
          <div class="v-icon v-icon-teal"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="5" y="2" width="14" height="20" rx="2"/><line x1="12" y1="18" x2="12.01" y2="18"/></svg></div>
          <span class="v-card-title" style="color:#015B60;">Easy on Any Device &amp; Phone</span>
        </div>
        <p class="v-card-desc">Designed like a modern smartphone app so managers track approvals, sales, and inventory anytime.</p>
      </div>

      <div class="v-card" style="background:#fff;border-color:#DFCEDA;">
        <div style="display:flex;align-items:center;gap:7px;">
          <div class="v-icon v-icon-plum"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg></div>
          <span class="v-card-title" style="color:#53354B;">2FA Security &amp; Auto Backup</span>
        </div>
        <p class="v-card-desc">Protects financial and customer data using two-factor authentication (2FA), granular access controls, and auto backups.</p>
      </div>

      <div class="v-card" style="background:#fff;border-color:#D2ECEC;">
        <div style="display:flex;align-items:center;gap:7px;">
          <div class="v-icon v-icon-teal"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg></div>
          <span class="v-card-title" style="color:#015B60;">Customization &amp; Telebirr APIs</span>
        </div>
        <p class="v-card-desc">Tailored to your exact business rules and connects smoothly with external software and Telebirr via APIs.</p>
      </div>

      <div class="v-card" style="grid-column:span 2;background:#fff;border-color:#DFCEDA;">
        <div style="display:flex;align-items:center;gap:7px;">
          <div class="v-icon v-icon-plum"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="23 4 23 10 17 10"/><path d="M20.49 15a9 9 0 1 1-2.12-9.36L23 10"/></svg></div>
          <span class="v-card-title" style="color:#53354B;">Continuous Yearly Upgrades</span>
          <span style="font-size:.73rem;color:#444462;">— Major yearly updates introduce new features, faster speeds, and enhanced security.</span>
        </div>
      </div>
    </div>
  </div>
  <div class="odoo-divider"></div>
'''

# ── Section 5: Core Odoo ERP Applications (Odoo Brand Theme) ──
SEC5_V = '''
  <div id="sec5" class="odoo-sec">
    <div class="sec-head">
      <span class="sec-pill odoo-pill" style="background:#017E84;">5</span>
      <h2 class="sec-title odoo-title">Core Odoo ERP Applications</h2>
    </div>
    <p class="sec-sub odoo-sub">All Your Business Tools Working as One Connected Platform</p>

    <!-- Silos Eliminated Strip -->
    <div style="background:#fff;border:1px solid #E5D8E2;border-radius:10px;padding:9px 10px;margin-bottom:12px;">
      <div style="font-size:.68rem;font-weight:800;color:#991B1B;text-transform:uppercase;margin-bottom:5px;">Replaces Disconnected Departmental Silos:</div>
      <div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:5px;font-size:.71rem;color:#7F1D1D;">
        <div style="background:#FEF2F2;padding:4px 7px;border-radius:6px;">&#10006; Sales paper slips</div>
        <div style="background:#FEF2F2;padding:4px 7px;border-radius:6px;">&#10006; Warehouse private notebooks</div>
        <div style="background:#FEF2F2;padding:4px 7px;border-radius:6px;">&#10006; Retyping into Peachtree</div>
        <div style="background:#FEF2F2;padding:4px 7px;border-radius:6px;">&#10006; Scattered project spreadsheets</div>
      </div>
    </div>

    <!-- SVG Hub-and-Spoke Architecture Infographic -->
    <div style="background:#fff;border:1.5px solid #714B67;border-radius:12px;padding:12px 10px;margin-bottom:12px;">
      <p style="text-align:center;font-family:'Outfit',sans-serif;font-size:.76rem;font-weight:800;color:#714B67;text-transform:uppercase;letter-spacing:.05em;margin-bottom:8px;">3 Operational Categories &bull; 10 Core Modules</p>
      <svg viewBox="0 0 600 175" style="width:100%;height:auto;display:block;" aria-label="Odoo 3 Operational Categories Diagram">
        <!-- Connector lines -->
        <line x1="300" y1="36" x2="105" y2="92" stroke="#714B67" stroke-width="2.5" stroke-dasharray="4 3"/>
        <line x1="300" y1="36" x2="300" y2="92" stroke="#017E84" stroke-width="2.5" stroke-dasharray="4 3"/>
        <line x1="300" y1="36" x2="495" y2="92" stroke="#714B67" stroke-width="2.5" stroke-dasharray="4 3"/>
        <!-- Top Hub -->
        <rect x="195" y="4" width="210" height="34" rx="17" fill="#714B67"/>
        <text x="300" y="25" text-anchor="middle" fill="#fff" font-family="Outfit,sans-serif" font-size="13" font-weight="800">ODOO ERP LIVE LEDGER</text>
        <!-- Pillar 1 -->
        <rect x="8" y="88" width="188" height="82" rx="10" fill="#FAF5F9" stroke="#714B67" stroke-width="2"/>
        <rect x="8" y="88" width="188" height="24" rx="8" fill="#714B67"/>
        <text x="102" y="104" text-anchor="middle" fill="#fff" font-family="Outfit,sans-serif" font-size="11" font-weight="800">1. FINANCE &amp; CONTROL</text>
        <text x="102" y="126" text-anchor="middle" fill="#4E3247" font-family="Plus Jakarta Sans,sans-serif" font-size="10" font-weight="600">&bull; Accounting &amp; Invoicing</text>
        <text x="102" y="142" text-anchor="middle" fill="#4E3247" font-family="Plus Jakarta Sans,sans-serif" font-size="10" font-weight="600">&bull; Budget Management</text>
        <text x="102" y="158" text-anchor="middle" fill="#4E3247" font-family="Plus Jakarta Sans,sans-serif" font-size="10" font-weight="600">&bull; HR &amp; Payroll</text>
        <!-- Pillar 2 -->
        <rect x="206" y="88" width="188" height="82" rx="10" fill="#F2FAFA" stroke="#017E84" stroke-width="2"/>
        <rect x="206" y="88" width="188" height="24" rx="8" fill="#017E84"/>
        <text x="300" y="104" text-anchor="middle" fill="#fff" font-family="Outfit,sans-serif" font-size="11" font-weight="800">2. OPERATIONS &amp; SUPPLY</text>
        <text x="300" y="123" text-anchor="middle" fill="#015B60" font-family="Plus Jakarta Sans,sans-serif" font-size="9.5" font-weight="600">&bull; Inventory &amp; Warehouses</text>
        <text x="300" y="136" text-anchor="middle" fill="#015B60" font-family="Plus Jakarta Sans,sans-serif" font-size="9.5" font-weight="600">&bull; Purchasing &amp; Vendors</text>
        <text x="300" y="149" text-anchor="middle" fill="#015B60" font-family="Plus Jakarta Sans,sans-serif" font-size="9.5" font-weight="600">&bull; Manufacturing (MRP)</text>
        <text x="300" y="162" text-anchor="middle" fill="#015B60" font-family="Plus Jakarta Sans,sans-serif" font-size="9.5" font-weight="600">&bull; Project Management</text>
        <!-- Pillar 3 -->
        <rect x="404" y="88" width="188" height="82" rx="10" fill="#FAF5F9" stroke="#53354B" stroke-width="2"/>
        <rect x="404" y="88" width="188" height="24" rx="8" fill="#53354B"/>
        <text x="498" y="104" text-anchor="middle" fill="#FFA600" font-family="Outfit,sans-serif" font-size="11" font-weight="800">3. SALES &amp; GROWTH</text>
        <text x="498" y="126" text-anchor="middle" fill="#4E3247" font-family="Plus Jakarta Sans,sans-serif" font-size="10" font-weight="600">&bull; Sales &amp; Point of Sale (POS)</text>
        <text x="498" y="142" text-anchor="middle" fill="#4E3247" font-family="Plus Jakarta Sans,sans-serif" font-size="10" font-weight="600">&bull; Customer Management (CRM)</text>
        <text x="498" y="158" text-anchor="middle" fill="#4E3247" font-family="Plus Jakarta Sans,sans-serif" font-size="10" font-weight="600">&bull; Website &amp; E-Commerce</text>
      </svg>
    </div>

    <!-- 3 Category Cards with Condensed Module Descriptions -->
    <div style="display:flex;flex-direction:column;gap:8px;">
      <!-- Cat 1 -->
      <div style="background:#fff;border:1px solid #DFCEDA;border-left:4px solid #714B67;border-radius:10px;padding:10px 12px;">
        <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:3px;">
          <span style="font-family:'Outfit',sans-serif;font-size:.86rem;font-weight:800;color:#714B67;">&#128202; 1. Finance &amp; Control</span>
          <span style="font-size:.65rem;background:#F7F1F5;color:#714B67;padding:2px 7px;border-radius:99px;font-weight:700;">3 Core Modules</span>
        </div>
        <p style="font-size:.72rem;color:#666;font-style:italic;margin-bottom:7px;">Stay compliant, safeguard cash flow, and maintain total financial clarity.</p>
        <div style="display:flex;flex-direction:column;gap:5px;font-size:.74rem;color:#2C2C3E;">
          <div><strong style="color:#714B67;">&bull; Accounting &amp; Invoicing:</strong> Live ledger for Ethiopian taxes (VAT, Withholding), e-invoicing, fiscal printers, Amharic menus &amp; local fiscal years.</div>
          <div><strong style="color:#714B67;">&bull; Budget Management:</strong> Tracks planned vs. actual spending in real time across branches and departments.</div>
          <div><strong style="color:#714B67;">&bull; HR &amp; Payroll:</strong> Centralizes staff files, attendance &amp; monthly payroll with Ethiopian income tax brackets and pension laws (7% / 11%).</div>
        </div>
      </div>

      <!-- Cat 2 -->
      <div style="background:#fff;border:1px solid #D2ECEC;border-left:4px solid #017E84;border-radius:10px;padding:10px 12px;">
        <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:3px;">
          <span style="font-family:'Outfit',sans-serif;font-size:.86rem;font-weight:800;color:#017E84;">&#128230; 2. Operations &amp; Supply Chain</span>
          <span style="font-size:.65rem;background:#E8F6F6;color:#017E84;padding:2px 7px;border-radius:99px;font-weight:700;">4 Core Modules</span>
        </div>
        <p style="font-size:.72rem;color:#666;font-style:italic;margin-bottom:7px;">Eliminate stock losses, streamline purchasing, and track true production costs.</p>
        <div style="display:flex;flex-direction:column;gap:5px;font-size:.74rem;color:#2C2C3E;">
          <div><strong style="color:#017E84;">&bull; Inventory &amp; Warehouses:</strong> Live multi-shop stock tracking, auto reordering, mobile barcode scanning &amp; import landed costs.</div>
          <div><strong style="color:#017E84;">&bull; Purchasing &amp; Vendors:</strong> Standardizes requisitions and 3-way matching (order, receipt, vendor bill) to stop duplicate payments.</div>
          <div><strong style="color:#017E84;">&bull; Manufacturing (MRP):</strong> Multi-level Bills of Materials (BOM), shop-floor task tracking &amp; true finished-product unit costs.</div>
          <div><strong style="color:#017E84;">&bull; Project Management:</strong> Visual task boards linking deliverables to field timesheets, materials used &amp; client invoicing.</div>
        </div>
      </div>

      <!-- Cat 3 -->
      <div style="background:#fff;border:1px solid #DFCEDA;border-left:4px solid #53354B;border-radius:10px;padding:10px 12px;">
        <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:3px;">
          <span style="font-family:'Outfit',sans-serif;font-size:.86rem;font-weight:800;color:#53354B;">&#128200; 3. Sales &amp; Customer Growth</span>
          <span style="font-size:.65rem;background:#F7F1F5;color:#53354B;padding:2px 7px;border-radius:99px;font-weight:700;">3 Core Modules</span>
        </div>
        <p style="font-size:.72rem;color:#666;font-style:italic;margin-bottom:7px;">Sell across retail counters, enterprise sales teams, and digital channels.</p>
        <div style="display:flex;flex-direction:column;gap:5px;font-size:.74rem;color:#2C2C3E;">
          <div><strong style="color:#53354B;">&bull; Sales &amp; Point of Sale (POS):</strong> Fast retail/wholesale checkouts with cash, Telebirr, CBE Birr &amp; offline selling during internet cuts.</div>
          <div><strong style="color:#53354B;">&bull; Customer Management (CRM):</strong> Visual sales pipeline, follow-up tracking &amp; revenue forecasting so deals are never lost.</div>
          <div><strong style="color:#53354B;">&bull; Website &amp; E-Commerce:</strong> Online storefront synced live with warehouse stock, auto-generating orders and invoices.</div>
        </div>
      </div>
    </div>
  </div>
  <div class="odoo-divider"></div>
'''
