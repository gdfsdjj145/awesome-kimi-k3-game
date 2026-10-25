# Blender 场景脚本：低多边形篝火营地 · 提示词

> 🧪 参考实现：本效果由 Grok Bot（代 kajian du 制作）编写，**不是 Kimi 生成**。下方提示词可直接喂给 Kimi K3.1 Pro 复现，用于对比。

> 实测说明：campfire_scene.py 已在 Blender 4.2.3 LTS 中以 `blender --background --python campfire_scene.py -- --render out.png --glb scene.glb` 真实运行（生成 100 个物体，Cycles CPU 渲染 + glTF 导出成功）；需 Blender 4.0+。目录下附 campfire_scene.py、campfire_scene.glb、blender-render.jpg。

## 第 1 轮（主提示词）

```
要求：只输出一个完整的 index.html 单文件，CSS/JS 全部内联（可用 jsDelivr CDN 的开源库），不调用任何付费服务或 API；界面文字使用中文；<head> 中加入 <link rel="icon" href="data:,"> 避免 favicon 404；控制台不得有任何报错。

第一部分：写一个 Blender 4.x 的 Python 脚本 campfire_scene.py，用 bpy 从零生成一个「低多边形篝火营地」场景：清空场景；地面（细分后随机起伏的平面）；中央篝火（石头圈、交叉木柴、发光火焰锥体用 Emission 材质）；帐篷；原木座椅；周围随机分布的低多边形松树和石头（固定随机种子）；暖色点光源模拟火光 + 冷色日光模拟月光；相机用 Track To 约束对准营地。脚本支持命令行参数：blender --background --python campfire_scene.py -- --render out.png --glb scene.glb，分别用 Cycles 渲染图片、导出 glTF。
第二部分：做一个 index.html：用 Three.js（importmap 引 jsDelivr）加载这份 glb，OrbitControls 旋转查看，篝火点光源闪烁、火星粒子上升，有昼夜切换。页面右侧标签页：「Python 脚本」（带语法高亮）、「Blender 渲染」（真实渲染图）、「使用说明」。按钮：下载 .py、复制脚本、下载 .glb。为了单文件可用，可把 glb 与渲染图以 base64 内嵌。
```

## 修改记录

- 第 1 轮：按上方主提示词一次生成，自测截图与控制台无报错。
- 第 2 轮（修改提示词）：「首次渲染画面是空的（手动设置的相机旋转没有对准营地）。改为在营地中心放一个空物体，相机加 Track To 约束对准它。」修改后 Blender 4.2.3 无界面实测渲染与 glTF 导出均成功。
