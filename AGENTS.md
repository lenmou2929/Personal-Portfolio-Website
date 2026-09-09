## 项目铁律（先于下方模板内容，任何智能体必读）

- **任何修改或更新（代码/内容/文档/素材）都必须写日志**：会话内重要节点即时补记，会话结束前在 `../docs/日志/` 新建 `日期-会话编号-主题.md`（编号 = 该目录现有最大编号 + 1；内容含：做了什么、决定了什么、遗留什么）。**没有日志的修改视为未完成**
- git 提交：中文信息、一句一事；不主动 push 除非用户要求（push 即触发 Cloudflare 自动构建上线）
- 方向性决策只增不改地记入 `../README.md` 关键决策表；完整协作规范见 `../docs/公共/00-AI协作规范.md`

## Development

When starting the dev server, use background mode:

```
astro dev --background
```

Manage the background server with `astro dev stop`, `astro dev status`, and `astro dev logs`.

## Documentation

Full documentation: https://docs.astro.build

Consult these guides before working on related tasks:

- [Adding pages, dynamic routes, or middleware](https://docs.astro.build/en/guides/routing/)
- [Working with Astro components](https://docs.astro.build/en/basics/astro-components/)
- [Using React, Vue, Svelte, or other framework components](https://docs.astro.build/en/guides/framework-components/)
- [Adding or managing content](https://docs.astro.build/en/guides/content-collections/)
- [Adding styles or using Tailwind](https://docs.astro.build/en/guides/styling/)
- [Supporting multiple languages](https://docs.astro.build/en/guides/internationalization/)
