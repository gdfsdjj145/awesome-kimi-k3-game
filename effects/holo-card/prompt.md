# 全息闪卡 · 提示词

> 🧪 参考实现：本效果由 Grok Bot（代 kajian du 制作）编写，**不是 Kimi 生成**。下方提示词可直接喂给 Kimi K3.1 Pro 复现，用于对比。

## 第 1 轮（主提示词）

```
要求：只输出一个完整的 index.html 单文件，CSS/JS 全部内联（可用 jsDelivr CDN 的开源库，如 three@0.160 及其 examples/jsm 后期模块），不调用任何付费服务或 API；界面文字使用中文；<head> 中加入 <link rel="icon" href="data:,"> 避免 favicon 404；控制台不得有任何报错。
性能与移动端：viewport 设为 width=device-width 并禁止缩放；devicePixelRatio 上限 2；在触屏/小屏/低核数设备上自动进入「省电档」（粒子数减半）；右下角显示实时 FPS，若连续 2 秒低于 40 FPS 就自动降低渲染分辨率（WebGL）或粒子数（Canvas）；所有交互同时支持鼠标与触摸（pointer 事件，touch-action:none）。

只用 HTML/CSS（加少量 JS）做「全息闪卡」：4 张卡（彩虹镭射 SSR、星光闪 SSR、金属拉丝 SR、宇宙全息 UR），卡面插画用 Canvas 程序绘制（渐变 + 同心圆 + 星点 + 大号 emoji），金色渐变边框（mask 实现）、稀有度角标、名称栏。每张卡由多层叠加：插画、镭射层（mix-blend-mode: color-dodge 的重复彩虹渐变，background-position 随指针位置移动）、闪点层（多层 radial-gradient 小白点）、高光层（overlay 混合的指针处径向白光）。用 CSS 变量 --mx/--my/--rx/--ry/--o 驱动：指针在卡上移动时卡片 rotateX/rotateY 倾斜、镭射与高光跟随。四种卡各自的镭射图案不同（线性彩虹、径向同心彩虹、金属拉丝条纹 + 扫光、锥形渐变星云）。点击放大到屏幕中央（再点或点遮罩还原）。无交互时「待机摆动」自动画 8 字。手机上提供「开启陀螺仪」按钮（iOS 需请求权限），用设备倾角驱动。
```

## 修改记录

- 第 1 轮：按上方主提示词生成，用 Playwright 在 1200×720 与 390×844（手机，DPR 2）两种尺寸下截图并检查控制台。
- 第 2 轮：「镭射层太强把插画盖住了：镭射层透明度从 0.25+0.75×强度 降到 0.08+0.45×强度，亮度、饱和度也略降。」
