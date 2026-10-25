# Awesome Kimi K3 Game [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

**English summary:** A curated list of games, demos, skills, tutorials and benchmarks made with Moonshot **Kimi K3 / K3.1 / K3.1 Pro**. Every game entry is "one game" with model, engine, one-shot or not, time, cost, source post, and playable link / source code when available. Each item is tagged ✅ verified (we opened it and it runs) or 📣 promotional (official showcase, no reproducible code, or likely part of Kimi's creator campaign). Includes a uniform benchmark prompt set ([benchmarks/](benchmarks/)) and a placeholder for running the open weights locally (expected by 2026-11-04). The main body is in Chinese. List content is CC0.

> 用 Kimi K3 / K3.1 / K3.1 Pro 做游戏的合集，**一个条目 = 一个游戏**。K3.1 Pro 于 2026-10-23 发布（北京时间 10-24 凌晨）：2.8T 总参 / 104B 激活 MoE，1M 上下文；API $2 输入 / $10 输出（每百万 tokens）；**开放权重预计 11 月 4 日前发布**。
>
> 赞 / 浏览 / Star 数据采集于 2026-10-24 22:00（北京时间），仅供参考。欢迎 PR，见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 标记说明

| 标记 | 含义 |
| --- | --- |
| ✅ 已验证 | 我们打开过可玩链接或源码，能跑 |
| 🧪 参考实现 | 非 Kimi 生成，由 Grok Bot 编写的对照实现，附可复现提示词 |
| 📣 推广 | 官方展示、无可复现源码的营销式帖子，或作者推自家产品。Kimi 有[创作者推广活动](https://x.com/elshayib_/status/2113903850641842589)，请自行甄别 |

「未说明」= 原帖没给，我们不猜。

## 目录

- [官方资源](#官方资源) · [游戏作品与 Demo](#游戏作品与-demo) · [效果库](#效果库) · [GitHub 项目](#github-项目) · [Skill 与工作流](#skill-与工作流) · [教程与提示词](#教程与提示词) · [评测](#评测) · [社区讨论](#社区讨论) · [相关合集](#相关合集) · [待补充：本地运行做游戏](#待补充本地运行做游戏) · [统一测试题](benchmarks/README.md)

## 官方资源

- [Kimi K3.1 Pro 发布推文](https://x.com/Kimi_Moonshot/status/2113680701770068067) - 官方发布主帖，Unreal/Unity/Godot 全项目游戏 + Blender 3D（2.6 万赞、约 276 万浏览）。
- [Meet Kimi K3.1 Pro 视频](https://x.com/Kimi_Moonshot/status/2113681863109939271) - 官方宣传片（2.2 万赞、145 万浏览）。
- [Blender / Unreal / Godot / CAD 能力帖](https://x.com/Kimi_Moonshot/status/2113680710150357279) - 3D 与游戏工具链说明，BenchCAD 92.7%（1,768 赞、12.5 万浏览）。
- [Kimi K3.1 Pro Tech Blog](https://www.kimi.ai/blog/kimi-k3-1-pro) - 官方技术博客，含端到端生成的游戏、Three.js 场景与 3D 资产示例。
- [API 与 Highspeed 版上线](https://x.com/Kimi_Moonshot/status/2113680718249500786) - `kimi-k3.1-pro` / `kimi-k3.1-pro-highspeed`（2–3× 速度）。
- [Kimi Code What's New](https://www.kimi.com/code/docs/en/kimi-code/whats-new.html) - Kimi Code 中启用 K3.1 Pro 的会员档位与使用建议（必须开启 thinking、新开会话）。

## 游戏作品与 Demo

| 游戏 | 模型 | 引擎 | 一次生成 | 耗时 | 成本 | 原帖 | 可玩 / 源码 | 标记 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Unreal 开放世界游戏 | K3.1 Pro | Unreal | 未说明 | 未说明 | 未说明 | [@nattcornelis](https://x.com/nattcornelis/status/2113710554225504495)（125 赞 / 3.5 万浏览） | 无 | 📣 推广 |
| 官方博客示例游戏与 3D 场景 | K3.1 Pro | Unreal / Godot / Three.js | 未说明 | 未说明 | 未说明 | [官方博客](https://www.kimi.ai/blog/kimi-k3-1-pro) | 无 | 📣 推广（官方） |
| Diorama Day（模拟人生风微缩场景） | K3.1 Pro | three.js 单 HTML | 是 | 未说明 | 未说明 | [GitHub](https://github.com/agent-marsha/csc35-diorama-day) | [在线试玩（作者页面）](https://agent-marsha.github.io/csc35-diorama-day/) · [源码](https://github.com/agent-marsha/csc35-diorama-day)（无许可证） | ✅ 已验证 |
| 牧野逐风（水牛竞速）/ 界刃（刀战）等 | K3.1 Pro（对比 Opus 5.5） | three.js + Vite | 未说明 | 未说明 | 未说明 | [GitHub](https://github.com/Zp-Peter/kimi-k31pro-opus55-benchmark-showcase) | [在线试玩（作者页面）](https://zp-peter.github.io/kimi-k31pro-opus55-benchmark-showcase/) · 源码（无许可证） | ✅ 已验证 |
| 3D 钓鱼小世界 | K3.1 | 单 HTML | 是（单提示词） | 未说明 | 未说明 | [@vipinxtwt](https://x.com/vipinxtwt/status/2113936333899214870) | 无 | 📣 推广（仅视频，无法复现） |
| 互动 3D 展馆 | K3.1 Pro | 网页 3D（Clusy） | 是 | 未说明 | 未说明 | [@urjr1](https://x.com/urjr1/status/2113791313346961430) | [Clusy](https://app.clusy.io)（需账号） | 📣 推广（产品宣传） |
| 摩纳哥赛车（失败案例） | K3.1 Pro（网页「创建应用」） | 网页 | 未说明 | 未说明 | 未说明 | [@poolmoon6](https://x.com/poolmoon6/status/2113805948016009610)（20 赞） | 无 | 📣 推广（仅视频；作者指出赛道、比例、操控反向问题） |
| 开发者多引擎实测 | K3.1 Pro | Unity / Unreal / Godot / Three.js / Blender | 未说明 | 未说明 | 未说明 | [@Layton_Gott](https://x.com/Layton_Gott/status/2113809753541410864)（45 赞） | 无 | 📣 推广（体验帖，无源码） |

> 两个 ✅ 项目仓库都**没有许可证**，所以没有复制进 [games/](games/)，只链接作者自己的在线页面。

## 效果库

单 HTML、打开即玩的游戏效果，每个附完整提示词（可直接喂给 Kimi K3.1 Pro 复现）。画廊页：[https://gdfsdjj145.github.io/awesome-kimi-k3-game/](https://gdfsdjj145.github.io/awesome-kimi-k3-game/)

> 🧪 参考实现 = 由 Grok Bot 代 kajian du 制作，**不是 Kimi 生成**，用来给 Kimi 复现做对照。欢迎用同一提示词跑 Kimi 后提交结果。

| 类别 | 效果 | 可玩链接 | 提示词 | 标记 |
| --- | --- | --- | --- | --- |
| 玩法 | 平台跳跃 | [在线试玩](https://gdfsdjj145.github.io/awesome-kimi-k3-game/effects/platformer/) | [prompt.md](effects/platformer/prompt.md) | 🧪 参考实现 |
| 玩法 | 弹球 | [在线试玩](https://gdfsdjj145.github.io/awesome-kimi-k3-game/effects/pinball/) | [prompt.md](effects/pinball/prompt.md) | 🧪 参考实现 |
| 玩法 | 塔防 | [在线试玩](https://gdfsdjj145.github.io/awesome-kimi-k3-game/effects/tower-defense/) | [prompt.md](effects/tower-defense/prompt.md) | 🧪 参考实现 |
| 玩法 | 三消 | [在线试玩](https://gdfsdjj145.github.io/awesome-kimi-k3-game/effects/match-three/) | [prompt.md](effects/match-three/prompt.md) | 🧪 参考实现 |
| 玩法 | 跑酷 | [在线试玩](https://gdfsdjj145.github.io/awesome-kimi-k3-game/effects/endless-runner/) | [prompt.md](effects/endless-runner/prompt.md) | 🧪 参考实现 |
| 卡牌与抽卡 | 卡牌十连抽动画 | [在线试玩](https://gdfsdjj145.github.io/awesome-kimi-k3-game/effects/gacha-ten-pull/) | [prompt.md](effects/gacha-ten-pull/prompt.md) | 🧪 参考实现 |
| 卡牌与抽卡 | 卡牌翻转与稀有度展示 | [在线试玩](https://gdfsdjj145.github.io/awesome-kimi-k3-game/effects/card-flip-rarity/) | [prompt.md](effects/card-flip-rarity/prompt.md) | 🧪 参考实现 |
| 战斗特效 | 技能释放特效 | [在线试玩](https://gdfsdjj145.github.io/awesome-kimi-k3-game/effects/skill-vfx/) | [prompt.md](effects/skill-vfx/prompt.md) | 🧪 参考实现 |
| 战斗特效 | 爆炸与受击特效 | [在线试玩](https://gdfsdjj145.github.io/awesome-kimi-k3-game/effects/explosion-hit-vfx/) | [prompt.md](effects/explosion-hit-vfx/prompt.md) | 🧪 参考实现 |
| 3D 场景 | 体素小岛 | [在线试玩](https://gdfsdjj145.github.io/awesome-kimi-k3-game/effects/voxel-island/) | [prompt.md](effects/voxel-island/prompt.md) | 🧪 参考实现 |
| 3D 场景 | 低多边形小镇 | [在线试玩](https://gdfsdjj145.github.io/awesome-kimi-k3-game/effects/lowpoly-town/) | [prompt.md](effects/lowpoly-town/prompt.md) | 🧪 参考实现 |
| UI | 游戏 UI 套件（血条、背包、对话框、主菜单） | [在线试玩](https://gdfsdjj145.github.io/awesome-kimi-k3-game/effects/game-ui-kit/) | [prompt.md](effects/game-ui-kit/prompt.md) | 🧪 参考实现 |
| 美术风格 | 同一小游戏的三种美术风格（像素 / 卡通渲染 / 赛博） | [在线试玩](https://gdfsdjj145.github.io/awesome-kimi-k3-game/effects/art-style-switch/) | [prompt.md](effects/art-style-switch/prompt.md) | 🧪 参考实现 |
| 卡牌与抽卡 | 抽卡结算界面 | [在线试玩](https://gdfsdjj145.github.io/awesome-kimi-k3-game/effects/gacha-result-screen/) | [prompt.md](effects/gacha-result-screen/prompt.md) | 🧪 参考实现 |
| 粒子与光效 | 粒子拖尾 | [在线试玩](https://gdfsdjj145.github.io/awesome-kimi-k3-game/effects/particle-trail/) | [prompt.md](effects/particle-trail/prompt.md) | 🧪 参考实现 |
| 粒子与光效 | 烟花 | [在线试玩](https://gdfsdjj145.github.io/awesome-kimi-k3-game/effects/fireworks/) | [prompt.md](effects/fireworks/prompt.md) | 🧪 参考实现 |
| 粒子与光效 | 魔法阵 | [在线试玩](https://gdfsdjj145.github.io/awesome-kimi-k3-game/effects/magic-circle/) | [prompt.md](effects/magic-circle/prompt.md) | 🧪 参考实现 |
| UI | 转场动画合集 | [在线试玩](https://gdfsdjj145.github.io/awesome-kimi-k3-game/effects/screen-transitions/) | [prompt.md](effects/screen-transitions/prompt.md) | 🧪 参考实现 |
| 3D 场景 | 天气系统 | [在线试玩](https://gdfsdjj145.github.io/awesome-kimi-k3-game/effects/weather-system/) | [prompt.md](effects/weather-system/prompt.md) | 🧪 参考实现 |
| Blender | Blender 场景脚本：低多边形篝火营地 | [在线试玩](https://gdfsdjj145.github.io/awesome-kimi-k3-game/effects/blender-scene-script/) | [prompt.md](effects/blender-scene-script/prompt.md) | 🧪 参考实现 |
| 美术风格 | 水墨山水风格 | [在线试玩](https://gdfsdjj145.github.io/awesome-kimi-k3-game/effects/style-ink-wash/) | [prompt.md](effects/style-ink-wash/prompt.md) | 🧪 参考实现 |
| 美术风格 | GameBoy 四色掌机风格 | [在线试玩](https://gdfsdjj145.github.io/awesome-kimi-k3-game/effects/style-gameboy/) | [prompt.md](effects/style-gameboy/prompt.md) | 🧪 参考实现 |
| 美术风格 | 三渲二卡通 3D 风格 | [在线试玩](https://gdfsdjj145.github.io/awesome-kimi-k3-game/effects/style-toon-3d/) | [prompt.md](effects/style-toon-3d/prompt.md) | 🧪 参考实现 |
| 美术风格 | 剪纸风格 | [在线试玩](https://gdfsdjj145.github.io/awesome-kimi-k3-game/effects/style-papercut/) | [prompt.md](effects/style-papercut/prompt.md) | 🧪 参考实现 |

## GitHub 项目

- [kimi-game-rank](https://github.com/silverbullet-liang/kimi-game-rank) - ✅ Kimi 社区游戏/作品六维评分排行榜（PHP + MySQL，AGPL-3.0）。
- 两个可玩的 Kimi 游戏源码仓库见上表（Diorama Day、Zp-Peter 对比集）。
- 还没找到用 K3.1 做的 Unity / Godot / Unreal 开源整项目，欢迎提交。

## Skill 与工作流

- [Claude Code 接入 Kimi（官方）](https://www.kimi.com/code/docs/en/third-party-tools/claude-code) - 用 Claude Code + 游戏 skill 跑 Kimi 的基础配置。
- [How to Use Kimi K3.1 Pro in Claude Code](https://llmapiguide.com/en/posts/kimi-k3-1-pro-claude-code) - 第三方/OpenRouter 方案的环境变量与 `/status` 检查。
- [ForgeSkills](https://github.com/sekaikx/ForgeSkills) - 20 个 SKILL.md 的游戏开发 skill 合集（通用 agent skill，可配合 Kimi Code / Claude Code 使用，未专门针对 Kimi 测试）。
- [Kimi K3.1 Pro in Hermes Agent](https://x.com/IBuzovskyi/status/2113906652390838572) - Hermes Agent 已支持 K3.1 Pro。

## 教程与提示词

- 统一测试题的完整提示词见 [benchmarks/README.md](benchmarks/README.md)。

- [Kimi K3.1 Pro built a game: how editable?](https://x.com/ExtrudeGStudio/status/2113893987476230251) - 视频讲解游戏 Demo 的可编辑性与局限。

## 评测

- [Design Arena 上线 K3.1 Pro](https://x.com/DesignArena/status/2113684321479557197) - 网页/游戏类盲测竞技场（109 赞）。
- [Terminal-Bench 4.0 官方成绩](https://x.com/Kimi_Moonshot/status/2113680705855373791) - 65.7%，Opus 5.5 为 66.4%（1,885 赞）。
- [3D Helicopter 对比](https://x.com/LuminaBench/status/2113960038423572794) - Gemini 4 Carbon vs Kimi K3.1 Pro vs Qwen 4 的 3D 工程理解（99 赞、9,501 浏览）。
- [One-shot 同题：Kimi 13 分钟 $1.26 vs Opus 20 分钟 $2.95](https://x.com/nathangu76/status/2113725061748400501) - 耗时与成本对比（11 赞）。
- [3D storm lighthouse 单 HTML 对比](https://x.com/arncof/status/2113804662298091864) - Kimi $0.93 / 12.7 分钟 vs Opus $2.99。
- [3 道困难 one-shot：Voxel Island / Hexagon Pinball](https://x.com/wikiwayne/status/2113811211783487920) - 0/3 通过的负面样本，适合做难度基准。
- [3D galaxy in Three.js 四模型对比](https://x.com/AIC_Hugo/status/2113844470747910527) - DeepSeek 4.1 / Kimi / Opus / Argon 同题。
- [Eiffel Tower K3 vs K3.1 Pro](https://x.com/domsilvestre/status/2113722311341690981) - 同提示词对比 K3 与 K3.1 Pro 的 3D 进步。

## 社区讨论

- [Open weights 12 天后可下载](https://x.com/gippp69/status/2113742171488895178) - SWE Marathon 51.7 vs Opus 46.3 的讨论（78 赞）。
- [2.8T 本地运行的期待](https://x.com/TeksEdge/status/2113715608030417201) - 开源权重本地部署讨论（80 赞、6,749 浏览）。
- [创作者推广活动争议](https://x.com/elshayib_/status/2113903850641842589) - 指 Kimi 创作者活动要求对比贬低竞品（623 赞、4.85 万浏览）；收录作品时请注意甄别推广内容。
- [Game dev rarely ends at the first playable](https://x.com/SoduWork/status/2113836737994907911) - 对「多轮修改不崩」的质疑，值得做长程迭代评测。

## 相关合集

- [awesome-kimi-k3-1-videos](https://github.com/yihui-dev/awesome-kimi-k3-1-videos) - 187 个 K3.1 作品视频，其中「Games & interactive experiences」30 个（8★）。
- [awesome-kimi-k3.1-guide-and-use-cases](https://github.com/cheercheung/awesome-kimi-k3.1-guide-and-use-cases) - 83 个带来源的用例，11 种语言（5★）。
- [awesome-Kimi-K3.1-pro-videos](https://github.com/mileson/awesome-Kimi-K3.1-pro-videos) - 视频、提示词与帧画廊。

## 待补充：本地运行做游戏

开放权重预计 **2026-11-04 前**发布，放出后补充：

- [ ] 权重下载地址与许可证
- [ ] 硬件需求与量化版本
- [ ] 本地推理方案（vLLM / SGLang / llama.cpp 等，以实际支持为准）
- [ ] 接入 Claude Code / Kimi Code / Hermes 跑游戏 skill 的配置
- [ ] 本地版在[统一测试题](benchmarks/README.md)上的结果

## 贡献

见 [CONTRIBUTING.md](CONTRIBUTING.md)。一个 PR 加一个游戏。

## License

列表内容 [CC0 1.0](LICENSE)。`games/` 下的游戏沿用各自原始许可证。
