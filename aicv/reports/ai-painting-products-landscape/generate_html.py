#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成带统一侧边栏抽屉导航（Unified Sidebar Drawer Navigation）的高保真 HTML 研报与备忘录。
"""
import re
import pathlib
import markdown

BASE = pathlib.Path(__file__).parent

STYLE_AND_NAV = """
<style>
/* 统一风格深浅自适应样式规范 */
*,*::before,*::after { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; scroll-behavior: smooth; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "PingFang SC",
               "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
  line-height: 1.78; color: #1e293b; background: #f8fafc; margin: 0; padding: 0;
}
@media (prefers-color-scheme: dark) {
  body { background: #0b0f19; color: #e2e8f0; }
}
.container {
  max-width: 1120px; margin: 0 auto; padding: 44px 36px 88px;
  background: #ffffff; min-height: 100vh;
  box-shadow: 0 4px 28px rgba(15,23,42,0.06);
}
@media (prefers-color-scheme: dark) {
  .container { background: #111827; box-shadow: 0 4px 28px rgba(0,0,0,0.5); }
}

h1 {
  font-size: 28px; margin: 0 0 14px; color: #0f172a;
  border-bottom: 3px solid #2563eb; padding-bottom: 14px;
  line-height: 1.35;
}
@media (prefers-color-scheme: dark) {
  h1 { color: #f8fafc; border-bottom-color: #38bdf8; }
}
h2 {
  font-size: 22px; margin: 44px 0 18px; color: #1d4ed8;
  border-bottom: 1px solid #e2e8f0; padding-bottom: 10px;
}
@media (prefers-color-scheme: dark) {
  h2 { color: #38bdf8; border-bottom-color: #1e293b; }
}
h3 { font-size: 18px; margin: 28px 0 14px; color: #0f172a; }
@media (prefers-color-scheme: dark) { h3 { color: #f1f5f9; } }
h4 { font-size: 16px; margin: 18px 0 10px; color: #334155; }
@media (prefers-color-scheme: dark) { h4 { color: #94a3b8; } }

p, li { font-size: 15px; }
code {
  background: #f1f5f9; padding: 2px 6px; border-radius: 4px;
  font-family: "JetBrains Mono", "SF Mono", Menlo, Consolas, monospace;
  font-size: 13.5px; color: #b91c1c;
}
@media (prefers-color-scheme: dark) {
  code { background: #1e293b; color: #f87171; }
}
pre {
  background: #0f172a; color: #e2e8f0; padding: 18px 20px;
  border-radius: 8px; overflow-x: auto; margin: 18px 0;
  box-shadow: inset 0 2px 6px rgba(0,0,0,0.3);
}
pre code {
  background: transparent; padding: 0; color: #e2e8f0;
  font-size: 13px; line-height: 1.6;
}
blockquote {
  border-left: 4px solid #2563eb; padding: 12px 18px;
  background: #eff6ff; color: #1e40af; margin: 20px 0;
  border-radius: 0 8px 8px 0;
}
@media (prefers-color-scheme: dark) {
  blockquote { background: #1e293b; color: #93c5fd; border-left-color: #38bdf8; }
}
blockquote p { margin: 6px 0; }

table {
  width: 100%; border-collapse: collapse; margin: 22px 0;
  font-size: 13.5px; line-height: 1.55;
}
th, td {
  border: 1px solid #e2e8f0; padding: 11px 13px;
  text-align: left; vertical-align: top;
}
@media (prefers-color-scheme: dark) {
  th, td { border-color: #1e293b; }
}
th {
  background: #f8fafc; font-weight: 600; color: #0f172a;
}
@media (prefers-color-scheme: dark) {
  th { background: #1e293b; color: #f8fafc; }
}
tr:nth-child(even) { background: #fcfdfe; }
@media (prefers-color-scheme: dark) {
  tr:nth-child(even) { background: #162032; }
}

a { color: #2563eb; text-decoration: none; word-break: break-all; }
a:hover { text-decoration: underline; }
@media (prefers-color-scheme: dark) {
  a { color: #38bdf8; }
}
hr {
  border: 0; border-top: 1px solid #e2e8f0; margin: 38px 0;
}
@media (prefers-color-scheme: dark) {
  hr { border-top-color: #1e293b; }
}

.meta { 
  background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; 
  padding: 16px 20px; margin: 0 0 28px; 
}
@media (prefers-color-scheme: dark) {
  .meta { background: #162032; border-color: #1e293b; }
}
.meta p { margin: 4px 0; font-size: 14px; color: #475569; }
@media (prefers-color-scheme: dark) { .meta p { color: #94a3b8; } }
.footer { 
  margin-top: 56px; padding-top: 20px; border-top: 1px solid #e2e8f0;
  font-size: 13px; color: #64748b; text-align: center; 
}

/* ==================== Unified Sidebar Drawer Navigation ==================== */
:root { --unified-nav-width: 320px; }
.unified-nav-btn {
  position: fixed; top: 18px; left: 18px; z-index: 9999;
  width: 44px; height: 44px; border-radius: 10px;
  border: 1px solid rgba(0, 0, 0, 0.12); background: #ffffff;
  color: #1e293b; cursor: pointer; display: flex;
  align-items: center; justify-content: center; font-size: 20px;
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.08);
  transition: all .2s cubic-bezier(0.4, 0, 0.2, 1);
}
.unified-nav-btn:hover {
  background: #f8fafc; color: #2563eb; border-color: #2563eb;
  transform: scale(1.05); box-shadow: 0 6px 20px rgba(37, 99, 235, 0.15);
}
@media (prefers-color-scheme: dark) {
  .unified-nav-btn {
    background: #1e293b; color: #f8fafc; border-color: #334155;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.3);
  }
  .unified-nav-btn:hover {
    background: #0f172a; color: #38bdf8; border-color: #38bdf8;
  }
}
body.unified-nav-open .unified-nav-btn { opacity: 0; pointer-events: none; }
/* 无蒙版模式：打开导航时保持正文完全清晰、无遮罩与高斯模糊 */
.unified-nav-overlay {
  display: none !important;
}
body.unified-nav-open .unified-nav-overlay {
  display: none !important;
}
aside.unified-nav-drawer {
  position: fixed; left: 0; top: 0; bottom: 0;
  width: var(--unified-nav-width); max-width: 86vw;
  background: #ffffff; border-right: 1px solid #e2e8f0;
  padding: 22px 16px 24px; overflow-y: auto; display: flex;
  flex-direction: column; z-index: 10001;
  box-shadow: 8px 0 28px rgba(0, 0, 0, 0.12);
  transform: translateX(-100%);
  transition: transform .28s cubic-bezier(0.4, 0, 0.2, 1);
}
@media (prefers-color-scheme: dark) {
  aside.unified-nav-drawer {
    background: #0f172a; border-right-color: #1e293b;
    box-shadow: 8px 0 28px rgba(0, 0, 0, 0.45);
  }
}
body.unified-nav-open aside.unified-nav-drawer { transform: translateX(0); }
.unified-nav-drawer .drawer-header {
  display: flex; align-items: center; justify-content: space-between;
  padding-bottom: 14px; border-bottom: 1px solid #e2e8f0; margin-bottom: 14px;
}
@media (prefers-color-scheme: dark) {
  .unified-nav-drawer .drawer-header { border-bottom-color: #1e293b; }
}
.unified-nav-drawer .drawer-brand {
  font-size: 14.5px; font-weight: 700; color: #0f172a;
}
@media (prefers-color-scheme: dark) { .unified-nav-drawer .drawer-brand { color: #f8fafc; } }
.unified-nav-drawer .drawer-brand span { color: #2563eb; }
@media (prefers-color-scheme: dark) { .unified-nav-drawer .drawer-brand span { color: #38bdf8; } }
.unified-nav-drawer .drawer-close-btn {
  background: transparent; border: 1px solid transparent;
  font-size: 18px; color: #64748b; cursor: pointer; padding: 4px 8px;
  border-radius: 6px; transition: all .15s;
}
.unified-nav-drawer .drawer-shortcuts {
  display: flex; flex-direction: column; gap: 6px; margin-bottom: 14px;
  padding-bottom: 14px; border-bottom: 1px dashed #e2e8f0;
}
@media (prefers-color-scheme: dark) {
  .unified-nav-drawer .drawer-shortcuts { border-bottom-color: #1e293b; }
}
.unified-nav-drawer .shortcut-btn {
  display: flex; align-items: center; gap: 8px; padding: 8px 12px;
  border-radius: 6px; font-size: 13px; font-weight: 500;
  color: #334155; text-decoration: none; background: #f8fafc;
  border: 1px solid #e2e8f0; transition: all .15s ease;
}
@media (prefers-color-scheme: dark) {
  .unified-nav-drawer .shortcut-btn {
    background: #1e293b; border-color: #334155; color: #cbd5e1;
  }
}
.unified-nav-drawer .shortcut-btn:hover {
  background: #eff6ff; border-color: #93c5fd; color: #1d4ed8;
}
.unified-nav-drawer .toc-section-title {
  font-size: 11px; font-weight: 700; text-transform: uppercase;
  color: #94a3b8; letter-spacing: 0.6px; margin: 6px 0 10px 4px;
}
.unified-nav-drawer .drawer-toc {
  display: flex; flex-direction: column; gap: 3px; flex: 1;
}
.unified-nav-drawer .drawer-toc a {
  font-size: 13px; color: #475569; text-decoration: none;
  padding: 6px 10px; border-radius: 6px; line-height: 1.4;
  overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
  border-left: 3px solid transparent; transition: all .15s ease;
}
@media (prefers-color-scheme: dark) { .unified-nav-drawer .drawer-toc a { color: #94a3b8; } }
.unified-nav-drawer .drawer-toc a:hover {
  color: #0f172a; background: #f1f5f9;
}
@media (prefers-color-scheme: dark) {
  .unified-nav-drawer .drawer-toc a:hover { color: #f8fafc; background: #1e293b; }
}
.unified-nav-drawer .drawer-toc a.active {
  color: #2563eb; background: #eff6ff; border-left-color: #2563eb; font-weight: 600;
}
@media (prefers-color-scheme: dark) {
  .unified-nav-drawer .drawer-toc a.active {
    color: #38bdf8; background: #0369a126; border-left-color: #38bdf8;
  }
}
.back-to-top {
  position: fixed; bottom: 24px; right: 24px; z-index: 999;
  width: 40px; height: 40px; border-radius: 50%;
  background: #2563eb; color: #fff; border: none; cursor: pointer;
  display: flex; align-items: center; justify-content: center;
  font-size: 18px; box-shadow: 0 4px 12px rgba(37,99,235,0.3);
  opacity: 0; pointer-events: none; transition: all .2s ease;
}
.back-to-top.visible { opacity: 1; pointer-events: auto; }
.back-to-top:hover { background: #1d4ed8; transform: translateY(-2px); }
</style>
"""

DRAWER_HTML = """
<!-- Sidebar Navigation Elements -->
<button class="unified-nav-btn" id="unifiedNavBtn" title="展开目录导航">☰</button>
<div class="unified-nav-overlay" id="unifiedNavOverlay"></div>
<aside class="unified-nav-drawer" id="unifiedNavDrawer">
  <div class="drawer-header">
    <div class="drawer-brand">作品集深度研报 · <span>AI 绘画产品全景</span></div>
    <button class="drawer-close-btn" id="unifiedNavClose" title="收起导航">✕</button>
  </div>
  <div class="drawer-shortcuts">
    <a href="../../index.html" class="shortcut-btn">🏠 返回作品集总览</a>
    <a href="deck.html" class="shortcut-btn">📊 演示幻灯片 Deck</a>
    <a href="decision-memo.html" class="shortcut-btn">📝 决策备忘录 Memo</a>
    <a href="../../prd/01_出版级AI绘画产品全链路规划(PRD与架构).html" class="shortcut-btn">📄 PRD 01 · 产品全链路规划</a>
    <a href="../../prd/02_出版级AI绘画工作流与ComfyUI方案设计.html" class="shortcut-btn">📄 PRD 02 · ComfyUI工作流</a>
  </div>
  <div class="toc-section-title">报告核心章节</div>
  <nav class="drawer-toc" id="unifiedNavToc">
    <a href="#sec-exec" title="1. 核心结论（Executive Summary）">1. 核心结论摘要</a>
    <a href="#sec-matrix-overview" title="2.1 全球与国内主流产品矩阵">2.1 产品矩阵四象限</a>
    <a href="#sec-ux-paradigm" title="2.2 核心产品功能与五代交互演进">2.2 五代交互范式演进</a>
    <a href="#sec-user-pyramid" title="2.3 目标用户画像与商业金字塔">2.3 客群画像五层金字塔</a>
    <a href="#sec-business-model" title="2.4 商业模式与收费体系拆解">2.4 商业模式与定价矩阵</a>
    <a href="#sec-unit-economics" title="2.5 单位经济学与单图推理成本测算">2.5 单位经济学与算力模型</a>
    <a href="#sec-reusable-design" title="3. 可借鉴设计点与复用经验">3. 可复用设计经验</a>
    <a href="#sec-devils-advocate" title="4. 局限性与魔鬼代言人分析">4. 魔鬼代言人与风险</a>
    <a href="#sec-comparison-table" title="5. 主流产品多维度横评矩阵">5. 7大标杆多维横评大表</a>
    <a href="#sec-citations" title="附录 A：参考来源清单">附录 A：参考来源清单</a>
    <a href="#sec-coverage" title="附录 B：举一反三维度执行情况">附录 B：举一反三维度</a>
  </nav>
</aside>
<button class="back-to-top" id="backToTop" title="回到顶部">↑</button>
"""

DRAWER_JS = """
<script>
(function() {
  const btn = document.getElementById('unifiedNavBtn');
  const overlay = document.getElementById('unifiedNavOverlay');
  const drawer = document.getElementById('unifiedNavDrawer');
  const closeBtn = document.getElementById('unifiedNavClose');
  const tocLinks = document.querySelectorAll('#unifiedNavToc a');

  function openNav() {
    document.body.classList.add('unified-nav-open');
  }
  function closeNav() {
    document.body.classList.remove('unified-nav-open');
  }

  if (btn) btn.addEventListener('click', openNav);
  if (overlay) overlay.addEventListener('click', closeNav);
  if (closeBtn) closeBtn.addEventListener('click', closeNav);

  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' && document.body.classList.contains('unified-nav-open')) {
      closeNav();
    }
  });

  tocLinks.forEach(link => {
    link.addEventListener('click', function() {
      closeNav();
    });
  });

  const sections = Array.from(tocLinks).map(link => {
    const id = link.getAttribute('href').replace('#', '');
    return document.getElementById(id);
  }).filter(Boolean);

  window.addEventListener('scroll', function() {
    let currentId = '';
    const scrollPos = window.scrollY + 130;
    sections.forEach(sec => {
      if (sec.offsetTop <= scrollPos) {
        currentId = sec.id;
      }
    });
    tocLinks.forEach(link => {
      if (link.getAttribute('href') === '#' + currentId) {
        link.classList.add('active');
      } else {
        link.classList.remove('active');
      }
    });
    const btt = document.getElementById('backToTop');
    if (btt) {
      if (window.scrollY > 400) { btt.classList.add('visible'); }
      else { btt.classList.remove('visible'); }
    }
  }, { passive: true });

  const bttBtn = document.getElementById('backToTop');
  if (bttBtn) {
    bttBtn.addEventListener('click', function() {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }
})();
</script>
"""

def add_section_anchors(text: str) -> str:
    """给报告关键标题注入 HTML 锚点 ID"""
    replacements = [
        (r"## 1\. 核心结论（Executive Summary）", r'<h2 id="sec-exec">1. 核心结论（Executive Summary）</h2>'),
        (r"### 2\.1 全球与国内 AI 绘画主流产品梯队矩阵", r'<h3 id="sec-matrix-overview">2.1 全球与国内 AI 绘画主流产品梯队矩阵</h3>'),
        (r"### 2\.2 核心产品功能与交互范式演进", r'<h3 id="sec-ux-paradigm">2.2 核心产品功能与交互范式演进</h3>'),
        (r"### 2\.3 目标用户画像细分与核心场景渗透", r'<h3 id="sec-user-pyramid">2.3 目标用户画像细分与核心场景渗透</h3>'),
        (r"### 2\.4 商业模式与收费体系拆解", r'<h3 id="sec-business-model">2.4 商业模式与收费体系拆解</h3>'),
        (r"### 2\.5 单位经济学（Unit Economics）与算力成本深度测算模型", r'<h3 id="sec-unit-economics">2.5 单位经济学（Unit Economics）与算力成本深度测算模型</h3>'),
        (r"## 3\. 可借鉴设计点与可复用经验", r'<h2 id="sec-reusable-design">3. 可借鉴设计点与可复用经验</h2>'),
        (r"## 4\. 局限性、失败模式与魔鬼代言人分析", r'<h2 id="sec-devils-advocate">4. 局限性、失败模式与魔鬼代言人分析</h2>'),
        (r"## 5\. 主流产品多维度横评矩阵", r'<h2 id="sec-comparison-table">5. 主流产品多维度横评矩阵</h2>'),
        (r"## 附录 A：参考来源清单", r'<h2 id="sec-citations">附录 A：参考来源清单</h2>'),
        (r"## 附录 B：举一反三维度执行情况", r'<h2 id="sec-coverage">附录 B：举一反三维度执行情况</h2>'),
    ]
    for pattern, repl in replacements:
        text = re.sub(pattern, repl, text)
    return text

def render_report():
    md_path = BASE / "report.md"
    out_path = BASE / "report.html"
    text = md_path.read_text(encoding="utf-8")
    
    # 提取顶部的 blockquote 元数据块
    m = re.search(r"\n((?:>.*\n?)+)", text)
    meta_html = ""
    if m:
        meta_html = '<div class="meta">' + markdown.markdown(m.group(1)) + "</div>"
        text = text[: m.start()] + text[m.end():]
        
    text = add_section_anchors(text)
    
    body = markdown.markdown(
        text,
        extensions=["tables", "fenced_code", "sane_lists", "nl2br"],
    )
    
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI 绘画产品全景深度调研：产品矩阵、交互工作流、客群画像与商业模式经济学</title>
{STYLE_AND_NAV}
</head>
<body>
{DRAWER_HTML}
<div class="container">
{meta_html}
{body}
<div class="footer">deep-research Compiler v1.0.3 · 作品集前沿研报 · 生成时间：2026-10-12</div>
</div>
{DRAWER_JS}
</body>
</html>
"""
    out_path.write_text(html, encoding="utf-8")
    print(f"→ {out_path.name}  ({len(html)} chars, navigation injected)")

def render_memo():
    md_path = BASE / "decision-memo.md"
    out_path = BASE / "decision-memo.html"
    text = md_path.read_text(encoding="utf-8")
    m = re.search(r"\n((?:>.*\n?)+)", text)
    meta_html = ""
    if m:
        meta_html = '<div class="meta">' + markdown.markdown(m.group(1)) + "</div>"
        text = text[: m.start()] + text[m.end():]
    body = markdown.markdown(
        text,
        extensions=["tables", "fenced_code", "sane_lists", "nl2br"],
    )
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Decision Memo — AI 绘画赛道产品与商业化战略选择判断系统</title>
{STYLE_AND_NAV}
</head>
<body>
<div class="container">
{meta_html}
{body}
<div class="footer">deep-research Compiler v1.0.3 · 战略决策备忘录 · 2026-10-12</div>
</div>
</body>
</html>
"""
    out_path.write_text(html, encoding="utf-8")
    print(f"→ {out_path.name}  ({len(html)} chars)")

if __name__ == "__main__":
    render_report()
    render_memo()
