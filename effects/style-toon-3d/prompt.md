# 三渲二卡通 3D 风格 · 提示词

> 🧪 参考实现：本效果由 Grok Bot（代 kajian du 制作）编写，**不是 Kimi 生成**。下方提示词可直接喂给 Kimi K3.1 Pro 复现，用于对比。

## 第 1 轮（主提示词）

```
要求：只输出一个完整的 index.html 单文件，CSS/JS 全部内联（可用 jsDelivr CDN 的开源库），不调用任何付费服务或 API；界面文字使用中文；<head> 中加入 <link rel="icon" href="data:,"> 避免 favicon 404；控制台不得有任何报错。

用 Three.js（importmap 从 jsDelivr 引 three@0.160）做一个「三渲二（Toon Shading）」风格的 3D 小场景：漂浮的圆形草地小岛，上面有房子、几棵圆球树、池塘、花，天上有飘动的云，一只小鸡在岛上跑（方向键/WASD 控制，无输入时自动绕圈），带跳跃步态和扇翅膀动画。材质用 MeshToonMaterial，配合 NearestFilter 的 DataTexture 色阶贴图形成硬边明暗；所有物体用「反向外壳法」（BackSide 黑色材质放大一点的副本）做描边。UI：色阶 2/3/5 阶切换、描边开关、「卡通 / 写实对比」切换（换成 MeshStandardMaterial）。OrbitControls 可旋转缩放，带阴影。
```

## 修改记录

- 第 1 轮：按上方主提示词一次生成，自测截图与控制台无报错。
