# Token Sweep

把即将重置的 AI 编程额度，换成可复核、可沉淀的仓库价值。

Token Sweep 不是“为了烧 token 而烧 token”的死循环。它会根据你剩余的时间，把额度投入深度代码审查、测试缺口、文档漂移、依赖健康、架构债务或性能风险分析，并默认只产出报告，不擅自修改代码。

> Skill 无法可靠读取你的精确剩余额度，也不能保证刚好消耗某个 token 数。请提供时间预算和关注方向；工作会在价值耗尽或时间到达时停止。

## 包含的 Skills

| Skill | 用途 |
| --- | --- |
| `spend-tokens-wisely` | 按时间、方向和风险偏好组合任务 |
| `review-repository-deeply` | 深度检查正确性、可靠性、安全边界和维护风险 |
| `find-test-gaps` | 找出最值得补的行为测试 |
| `audit-docs-drift` | 对照实现检查文档、示例和配置是否过期 |
| `map-architecture-debt` | 梳理耦合、边界、所有权与渐进式改造方案 |
| `audit-dependency-health` | 审查漏洞、过期、无用、重复和高风险依赖 |
| `profile-performance-risks` | 在优化前定位性能风险并设计测量方案 |

## 安装

仓库发布后可安装全部 skills：

```bash
npx skills add KillerQueen-Z/token-sweep
```

也可以只安装总控：

```bash
npx skills add KillerQueen-Z/token-sweep --skill spend-tokens-wisely
```

## 使用

```text
使用 $spend-tokens-wisely。我还有 45 分钟额度就会重置。
只做报告，重点检查这个仓库的正确性和测试缺口，不要修改代码。
```

也可以直接调用专项 skill：

```text
使用 $find-test-gaps 检查支付和结算路径。
返回价值最高的 5 个测试，写清 setup、action 和 assertions，不要修改代码。
```

本地预算选择器：

```bash
python3 skills/spend-tokens-wisely/scripts/plan_sweep.py \
  --minutes 60 --focus correctness,testing --repo-size medium
```

## 设计原则

- 追求有用产出，而不是 token 数字；
- 默认只读，修改必须单独授权；
- 每个结论都要有证据和置信度；
- 明确范围和停止条件；
- 不通过重复审查、降低测试质量或制造无意义文字来填满时间；
- 涉及专业安全审计时，交给专门的安全工作流，不用浅层清单冒充。

英文说明、研究来源和安全边界见 [README.md](README.md)、[research/SOURCES.md](research/SOURCES.md) 与 [SECURITY.md](SECURITY.md)。
