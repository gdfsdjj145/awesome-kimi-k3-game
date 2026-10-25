# 溶解消散 · 提示词

> 🧪 参考实现：本效果由 Grok Bot（代 kajian du 制作）编写，**不是 Kimi 生成**。下方提示词可直接喂给 Kimi K3.1 Pro 复现，用于对比。

## 第 1 轮（主提示词）

```
要求：只输出一个完整的 index.html 单文件，CSS/JS 全部内联（可用 jsDelivr CDN 的开源库，如 three@0.160 及其 examples/jsm 后期模块），不调用任何付费服务或 API；界面文字使用中文；<head> 中加入 <link rel="icon" href="data:,"> 避免 favicon 404；控制台不得有任何报错。
性能与移动端：viewport 设为 width=device-width 并禁止缩放；devicePixelRatio 上限 2；在触屏/小屏/低核数设备上自动进入「省电档」（粒子数减半）；右下角显示实时 FPS，若连续 2 秒低于 40 FPS 就自动降低渲染分辨率（WebGL）或粒子数（Canvas）；所有交互同时支持鼠标与触摸（pointer 事件，touch-action:none）。

用 Three.js 做「溶解消散」效果：模型可切换环面结、茶壶（TeapotGeometry）、用基本几何体合并成的「神像」。在 MeshStandardMaterial 的 onBeforeCompile 里注入：按物体局部坐标计算噪声阈值（多个 sin 叠加的平滑噪声 + 高度渐变，使溶解从下往上推进），低于进度就 discard，接近阈值的边缘输出强自发光（两层颜色：外沿与最亮的内沿）。在 JS 里用一模一样的噪声函数，对 MeshSurfaceSampler 采样出的 14000 个表面点（省电档减半）计算各自阈值，作为粒子属性；粒子的顶点着色器根据「进度 - 阈值」算出年龄，只有被烧掉的那一刻起才出现，并向外、向上飘散后消失，所以粒子与溶解边缘完全同步。4 种风格：灰烬（橙）、奥术（紫）、数据（青，方块化体素溶解 + 扫描线 + 方形粒子）、冰晶（蓝白，粒子向下落）。底部滑条手动控制进度，「自动播放」来回循环。OrbitControls、UnrealBloom、ACES。?t=0.45&s=2 指定进度和风格截图。
```

## 修改记录

- 第 1 轮：按上方主提示词生成，用 Playwright 在 1200×720 与 390×844（手机，DPR 2）两种尺寸下截图并检查控制台。
- 第 2 轮：「Bloom 过曝成一片：边缘自发光倍率从 6/10 降到 2.2/3.5，粒子 alpha 乘 0.55，Bloom 阈值提高到 0.85。」
