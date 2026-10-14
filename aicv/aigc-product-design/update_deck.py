import re

with open('deck.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract slides content
slides_match = re.search(r'<!-- Slide 01: Cover -->(.*)</div>\s*</body>', content, re.DOTALL)
if not slides_match:
    print("Could not find slides")
    exit(1)

slides_html = "  <!-- Slide 01: Cover -->" + slides_match.group(1).strip()
# ensure the first slide has .active
slides_html = slides_html.replace('<div class="slide cover">', '<div class="slide cover active">', 1)

new_html = """<!doctype html>
<html lang="zh-CN"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>决策汇报 Deck · AIGC 视觉交付管线</title>
<style>
:root {
  --bg: #fbfbfa; --fg: #1c1c1a; --muted: #6b6b66; --line: #e3e3df; --card: #fff;
  --accent: #b4531f; --ok: #2f6b45; --bad: #a12a2a;
}
@media(prefers-color-scheme:dark){
  :root:not([data-theme=light]){
    --bg: #131312; --fg: #e8e8e4; --muted: #96968f; --line: #2b2b28; --card: #191918;
    --accent: #e08a52; --ok: #7ab88f; --bad: #e08585;
  }
}
* { box-sizing: border-box; }
body { margin: 0; background: #000; color: var(--fg); font: 16px/1.6 -apple-system, sans-serif; overflow: hidden; height: 100vh; display: flex; flex-direction: column; }

/* 悬浮导航栏 */
.nav-bar {
  background: var(--card); border-bottom: 1px solid var(--line);
  padding: 12px 24px; display: flex; justify-content: space-between; align-items: center; z-index: 100;
}
.nav-bar a { color: var(--muted); text-decoration: none; font-size: 14px; font-weight: 600; }
.nav-bar a:hover { color: var(--accent); }
.nav-controls { display: flex; gap: 12px; align-items: center; }
.btn { background: transparent; border: 1px solid var(--line); color: var(--fg); padding: 4px 12px; border-radius: 6px; cursor: pointer; font-size: 13px; font-weight: 600; }
.btn:hover { border-color: var(--accent); color: var(--accent); }

/* 幻灯片容器（视口居中） */
.deck-viewport {
  flex: 1; display: flex; align-items: center; justify-content: center; position: relative; background: var(--bg);
}

.deck-container {
  width: 960px; height: 540px; position: relative; perspective: 1000px;
}

/* 单张 Slide */
.slide {
  background: var(--card); border: 1px solid var(--line); border-radius: 12px;
  width: 100%; height: 100%; position: absolute; top: 0; left: 0;
  display: flex; flex-direction: column;
  box-shadow: 0 10px 40px rgba(0,0,0,0.15);
  opacity: 0; pointer-events: none; transform: translateX(80px) scale(0.95);
  transition: all 0.5s cubic-bezier(0.2, 0.8, 0.2, 1);
}
.slide.active { opacity: 1; pointer-events: auto; transform: translateX(0) scale(1); z-index: 10; }
.slide.prev { transform: translateX(-80px) scale(0.95); opacity: 0; }

.slide-header {
  padding: 24px 32px 16px; border-bottom: 1px solid var(--line); display: flex; align-items: baseline; gap: 16px;
}
.slide-num { font-size: 14px; color: var(--accent); font-weight: 700; }
.slide-title { font-size: 22px; font-weight: 600; margin: 0; letter-spacing: -0.01em; }

.slide-body { padding: 32px; flex: 1; display: flex; flex-direction: column; }

.slide-footer {
  padding: 12px 32px; border-top: 1px solid var(--line); font-size: 12px; color: var(--muted);
  display: flex; justify-content: space-between; background: rgba(0,0,0,0.01);
}

/* 版式辅助工具 */
.grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; height: 100%; }
.box { background: var(--bg); border: 1px solid var(--line); border-radius: 8px; padding: 20px; }
.box h4 { margin: 0 0 10px 0; color: var(--accent); font-size: 15px; }
.box p { margin: 0; font-size: 14px; color: var(--muted); line-height: 1.6; }
.highlight { color: var(--accent); font-weight: 600; }

/* 封面页特殊样式 */
.slide.cover { justify-content: center; align-items: center; text-align: center; background: linear-gradient(135deg, var(--card), var(--bg)); }
.slide.cover h1 { font-size: 36px; margin: 0 0 16px 0; letter-spacing: -0.02em; }
.slide.cover p { font-size: 18px; color: var(--muted); max-width: 600px; margin: 0 0 32px 0; }
.role-badge { display: inline-block; background: rgba(180,83,31,0.08); color: var(--accent); border: 1px solid rgba(180,83,31,0.25); padding: 6px 16px; border-radius: 20px; font-size: 13px; font-weight: 600; }

ul { margin: 0; padding-left: 20px; }
li { margin-bottom: 12px; font-size: 15px; }
</style>
</head>
<body>

<div class="nav-bar">
  <a href="index.html">&larr; 返回项目主看板</a>
  <div class="nav-controls">
    <span id="pageCount" style="font-size:12px; color:var(--muted); margin-right:8px">1 / 7</span>
    <button class="btn" id="btnPrev">&lt; 上一页</button>
    <button class="btn" id="btnNext">下一页 &gt;</button>
    <button class="btn" id="btnFullscreen" title="快捷键：F">全屏演示</button>
  </div>
</div>

<div class="deck-viewport">
<div class="deck-container">

{SLIDES_HTML}

</div>
</div>

<!-- 底部进度条 -->
<div id="progressBar" style="position:fixed; bottom:0; left:0; height:5px; background:var(--accent); width:0%; transition:width 0.3s ease; z-index:1000; box-shadow: 0 0 10px var(--accent);"></div>

<script>
  const slides = document.querySelectorAll('.slide');
  const btnPrev = document.getElementById('btnPrev');
  const btnNext = document.getElementById('btnNext');
  const pageCount = document.getElementById('pageCount');
  const progressBar = document.getElementById('progressBar');
  let currentSlide = 0;

  function updateSlides() {
    slides.forEach((slide, index) => {
      slide.classList.remove('active', 'prev');
      if (index === currentSlide) {
        slide.classList.add('active');
      } else if (index < currentSlide) {
        slide.classList.add('prev');
      }
    });
    
    pageCount.textContent = (currentSlide + 1) + ' / ' + slides.length;
    
    // 更新进度条
    const progress = ((currentSlide + 1) / slides.length) * 100;
    progressBar.style.width = progress + '%';
    
    btnPrev.disabled = currentSlide === 0;
    btnPrev.style.opacity = currentSlide === 0 ? '0.3' : '1';
    btnNext.disabled = currentSlide === slides.length - 1;
    btnNext.style.opacity = currentSlide === slides.length - 1 ? '0.3' : '1';
  }

  function nextSlide() {
    if (currentSlide < slides.length - 1) {
      currentSlide++;
      updateSlides();
    }
  }

  function prevSlide() {
    if (currentSlide > 0) {
      currentSlide--;
      updateSlides();
    }
  }

  btnNext.addEventListener('click', nextSlide);
  btnPrev.addEventListener('click', prevSlide);

  // 全屏功能
  const btnFullscreen = document.getElementById('btnFullscreen');
  function toggleFullScreen() {
    if (!document.fullscreenElement && !document.webkitFullscreenElement) {
      const elem = document.documentElement;
      if (elem.requestFullscreen) {
        elem.requestFullscreen();
      } else if (elem.webkitRequestFullscreen) { /* Safari */
        elem.webkitRequestFullscreen();
      }
      btnFullscreen.textContent = "退出全屏";
    } else {
      if (document.exitFullscreen) {
        document.exitFullscreen();
      } else if (document.webkitExitFullscreen) { /* Safari */
        document.webkitExitFullscreen();
      }
      btnFullscreen.textContent = "全屏演示";
    }
  }

  btnFullscreen.addEventListener('click', toggleFullScreen);

  // 监听全屏状态变化，避免按 Esc 退出时按钮文字不更新
  document.addEventListener('fullscreenchange', () => {
    btnFullscreen.textContent = document.fullscreenElement ? "退出全屏" : "全屏演示";
  });
  document.addEventListener('webkitfullscreenchange', () => {
    btnFullscreen.textContent = document.webkitFullscreenElement ? "退出全屏" : "全屏演示";
  });

  // 键盘支持 (增加 F 键全屏)
  window.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {
      nextSlide();
    } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
      prevSlide();
    } else if (e.key === 'f' || e.key === 'F') {
      toggleFullScreen();
    }
  });

  // 窗口自适应缩放 (Responsive Scaling)
  function resizeDeck() {
    const viewport = document.querySelector('.deck-viewport');
    const container = document.querySelector('.deck-container');
    const vw = viewport.clientWidth;
    const vh = viewport.clientHeight;
    // 基础尺寸 960x540，留出 4% 的边距
    const scale = Math.min(vw / 960, vh / 540) * 0.96; 
    container.style.transform = `scale(${scale})`;
  }
  window.addEventListener('resize', resizeDeck);
  // 重新计算一次，防止首次加载缩放不对
  setTimeout(resizeDeck, 0);

  // 初始化
  updateSlides();
</script>
</body>
</html>
"""

new_html = new_html.replace('{SLIDES_HTML}', slides_html)

with open('deck.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Restored full screen slider!")
