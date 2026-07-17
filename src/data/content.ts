import * as PrinciplesDoc from '../../docs/01-core-principles.md';
import * as LoopDoc from '../../docs/02-operating-loop.md';
import * as StackDoc from '../../docs/03-ai-collaboration-stack.md';
import * as MethodDoc from '../../docs/04-methodology-positioning.md';
import * as RiskDoc from '../../docs/05-risk-authority-and-decision-rights.md';
import * as VerifyDoc from '../../docs/06-verification-delivery-and-closure.md';
import * as EvolutionDoc from '../../docs/07-system-evolution.md';
import * as AdoptionDoc from '../../docs/08-adoption-guide.md';

import * as TaskBrief from '../../templates/task-brief.md';
import * as Investigation from '../../templates/investigation.md';
import * as Implementation from '../../templates/implementation.md';
import * as HighRisk from '../../templates/high-risk-change.md';
import * as ConnectorGate from '../../templates/connector-capability-gate.md';
import * as Authorization from '../../templates/authorization-ledger.md';
import * as Receipt from '../../templates/operation-receipt.md';
import * as Verification from '../../templates/verification-report.md';
import * as Handoff from '../../templates/handoff.md';
import * as Extraction from '../../templates/workflow-extraction.md';
import * as PublicRelease from '../../templates/public-release.md';

import * as FastCase from '../../examples/fast-read-only-investigation/README.md';
import * as StandardCase from '../../examples/standard-bugfix/README.md';
import * as AssuredCase from '../../examples/assured-remote-write/README.md';
import * as CodexDoc from '../../integrations/codex/README.md';
import * as AgentsExample from '../../integrations/codex/AGENTS.example.md';

export const lessons = [
  {
    order: '01',
    slug: 'core-principles',
    title: '可信工作的十條原則',
    shortTitle: '核心原則',
    description: '從 current truth、boundary、evidence，一路到真正 closure。',
    signal: 'TRUTH / BOUNDARY',
    readTime: '9 min',
    sourcePath: 'docs/01-core-principles.md',
    module: PrinciplesDoc,
  },
  {
    order: '02',
    slug: 'operating-loop',
    title: '端到端 Operating Loop',
    shortTitle: 'Operating Loop',
    description: '把模糊要求收斂成有邊界、有證據、可交付的狀態。',
    signal: '13 STAGES',
    readTime: '12 min',
    sourcePath: 'docs/02-operating-loop.md',
    module: LoopDoc,
  },
  {
    order: '03',
    slug: 'ai-collaboration-stack',
    title: 'AI / Codex 協作堆疊',
    shortTitle: 'AI 協作堆疊',
    description: 'Instructions、Memory、Skills、Plugins、Connectors 與 tools 各自負責什麼。',
    signal: 'CAPABILITY STACK',
    readTime: '10 min',
    sourcePath: 'docs/03-ai-collaboration-stack.md',
    module: StackDoc,
  },
  {
    order: '04',
    slug: 'methodology-positioning',
    title: '方法論定位',
    shortTitle: '方法論定位',
    description: 'Prompt、Context、Harness、Loop，以及 TDD、SDD、Source of Truth 的關係。',
    signal: 'CONCEPT MAP',
    readTime: '11 min',
    sourcePath: 'docs/04-methodology-positioning.md',
    module: MethodDoc,
  },
  {
    order: '05',
    slug: 'risk-and-authority',
    title: '風險、授權與決策權',
    shortTitle: '風險與授權',
    description: '按 blast radius 調整 autonomy，將 authority 拆成可執行 contract。',
    signal: 'DECISION RIGHTS',
    readTime: '10 min',
    sourcePath: 'docs/05-risk-authority-and-decision-rights.md',
    module: RiskDoc,
  },
  {
    order: '06',
    slug: 'verification-and-closure',
    title: '驗證、交付與 Closure',
    shortTitle: '驗證與 Closure',
    description: '讓 claim 不超過 evidence，並把交付推進到真正閉環。',
    signal: '7 LEVELS',
    readTime: '12 min',
    sourcePath: 'docs/06-verification-delivery-and-closure.md',
    module: VerifyDoc,
  },
  {
    order: '07',
    slug: 'system-evolution',
    title: '把重複成功演化成系統',
    shortTitle: '系統演化',
    description: '以 double-loop learning 沉澱 workflow，同時持續 pruning。',
    signal: 'EVOLVE / PRUNE',
    readTime: '10 min',
    sourcePath: 'docs/07-system-evolution.md',
    module: EvolutionDoc,
  },
  {
    order: '08',
    slug: 'adoption-guide',
    title: '四週採用指南',
    shortTitle: '採用指南',
    description: '從三個最小習慣開始，逐週建立風險分流與可觀測閉環。',
    signal: '4-WEEK PATH',
    readTime: '8 min',
    sourcePath: 'docs/08-adoption-guide.md',
    module: AdoptionDoc,
  },
];

export const templates = [
  { slug: 'task-brief', title: 'Task Brief', purpose: '把 objective、boundary、authority 與 closure target 鎖進同一個 envelope。', mode: 'ALL', sourcePath: 'templates/task-brief.md', module: TaskBrief },
  { slug: 'investigation', title: 'Investigation', purpose: '用 hypotheses、evidence plan 與 falsifier 做 read-only 排查。', mode: 'FAST', sourcePath: 'templates/investigation.md', module: Investigation },
  { slug: 'implementation', title: 'Implementation', purpose: '連接 current evidence、smallest action、verification 與 record。', mode: 'STANDARD', sourcePath: 'templates/implementation.md', module: Implementation },
  { slug: 'high-risk-change', title: 'High-Risk Change Gate', purpose: '在高風險 crossing 前完成 challenge、premortem 與 recovery 設計。', mode: 'ASSURED', sourcePath: 'templates/high-risk-change.md', module: HighRisk },
  { slug: 'connector-capability-gate', title: 'Connector Capability Gate', purpose: '驗證 configured、authenticated、target access 與 write authority。', mode: 'ASSURED', sourcePath: 'templates/connector-capability-gate.md', module: ConnectorGate },
  { slug: 'authorization-ledger', title: 'Authorization Ledger', purpose: '保存 target、operator、mutation class、lifetime 與 revalidation trigger。', mode: 'ASSURED', sourcePath: 'templates/authorization-ledger.md', module: Authorization },
  { slug: 'operation-receipt', title: 'Operation Receipt', purpose: '處理 remote write、timeout 與 outcome reconciliation。', mode: 'ASSURED', sourcePath: 'templates/operation-receipt.md', module: Receipt },
  { slug: 'verification-report', title: 'Verification Report', purpose: '明確寫出跑了什麼、沒跑什麼、證據最多支持什麼。', mode: 'ALL', sourcePath: 'templates/verification-report.md', module: Verification },
  { slug: 'handoff', title: 'Handoff', purpose: '讓接手者不必重讀整條 conversation 也能安全執行。', mode: 'STANDARD', sourcePath: 'templates/handoff.md', module: Handoff },
  { slug: 'workflow-extraction', title: 'Workflow Extraction', purpose: '只把重複、穩定、可驗證的 pattern 提升成 durable asset。', mode: 'EVOLVE', sourcePath: 'templates/workflow-extraction.md', module: Extraction },
  { slug: 'public-release', title: 'Public Release Gate', purpose: '為公開 repository 或文件執行 privacy、content、Git 與 public closure。', mode: 'ASSURED', sourcePath: 'templates/public-release.md', module: PublicRelease },
  { slug: 'codex-agents-example', title: 'Codex AGENTS Example', purpose: '為 project-level instructions 提供可裁剪、預設不生效的安全起點。', mode: 'CODEX', sourcePath: 'integrations/codex/AGENTS.example.md', module: AgentsExample },
];

export const cases = [
  {
    slug: 'configured-not-connected',
    eyebrow: 'FAST / READ-ONLY',
    title: 'Configured 不等於 Connected',
    description: '一個 connector 顯示 enabled，但真正的問題是：當前 task 是否 exposed、身份是否正確、target 是否可讀。',
    lesson: '不要由 config 推導 live capability。',
    sourcePath: 'examples/fast-read-only-investigation/README.md',
    module: FastCase,
  },
  {
    slug: 'standard-bugfix',
    eyebrow: 'STANDARD / CHANGE',
    title: 'Targeted pass 不等於 Full suite',
    description: '用 TDD-shaped repair 修復指定 contract，同時保留尚未覆蓋的 regression 邊界。',
    lesson: '讓完成聲明與 evidence 同粒度。',
    sourcePath: 'examples/standard-bugfix/README.md',
    module: StandardCase,
  },
  {
    slug: 'remote-timeout',
    eyebrow: 'ASSURED / REMOTE WRITE',
    title: 'Timeout 後，結果仍可能 Unknown',
    description: 'remote mutation 失去回應時，先 reconcile authoritative state，不盲目重送。',
    lesson: 'Unknown 是合法狀態；duplicate write 不是。',
    sourcePath: 'examples/assured-remote-write/README.md',
    module: AssuredCase,
  },
];

export const codexContent = {
  sourcePath: 'integrations/codex/README.md',
  module: CodexDoc,
  agentsModule: AgentsExample,
};

export const modes = [
  {
    slug: 'fast',
    name: 'Fast',
    index: '01',
    description: '可逆、局部、read-only 或低風險工作。',
    promise: '最小 boundary，快速 evidence，立即 readback。',
    minimum: ['確認 target 與 source', '執行 smallest useful action', '回讀結果並限制 claim'],
    color: 'signal',
  },
  {
    slug: 'standard',
    name: 'Standard',
    index: '02',
    description: '一般實作、正式文件或可控資料操作。',
    promise: 'brief、challenge、targeted verification、record。',
    minimum: ['鎖定 objective / non-goals', '建立 evidence map 與最小方案', '驗證 owning contract 並同步 current truth'],
    color: 'amber',
  },
  {
    slug: 'assured',
    name: 'Assured',
    index: '03',
    description: 'Production、customer、auth、permissions、destructive 或 external publication。',
    promise: '明確 authority、recovery、多層 evidence 與外部 closure。',
    minimum: ['Challenge / spec gate', 'identity、scope、authority、recovery', 'runtime / external readback 與 residual-risk owner'],
    color: 'coral',
  },
];

export const loopStages = [
  { id: '00', name: 'Objective', question: '真正要改變的 outcome 是什麼？', output: 'Objective、success、non-goals', stop: '症狀與目標仍混在一起', verb: 'Frame' },
  { id: '01', name: 'Boundary', question: '誰擁有 target？可做哪種 mutation？', output: 'Scope、authority、stop condition', stop: '身份、target 或權限不清', verb: 'Bound' },
  { id: '02', name: 'Classify', question: '這是什麼任務？風險 profile 是哪一級？', output: 'Fast / Standard / Assured', stop: '高風險被偽裝成 quick task', verb: 'Route' },
  { id: '03', name: 'Evidence', question: '哪些 current evidence 會改變 decision？', output: 'Verified / Inferred / Unknown map', stop: '只有 history 或 memory，沒有 current proof', verb: 'Observe' },
  { id: '04', name: 'Challenge', question: '什麼會證明目前假設錯？', output: 'Falsifier、failure modes、minimum test', stop: '方案仍修錯層或擴大 blast radius', verb: 'Stress' },
  { id: '05', name: 'Decision', question: '直接做、先記錄，還是只分析？', output: 'Decision / issue / spec / non-goal', stop: '高風險 intent 沒有留下 record', verb: 'Commit' },
  { id: '06', name: 'Smallest Path', question: '最小、可逆、可驗證的下一步是什麼？', output: 'Precondition → action → verify → rollback', stop: '方案包含無關 cleanup 或 shared-layer change', verb: 'Design' },
  { id: '07', name: 'Execute', question: '如何精準 mutation 並保存 receipt？', output: 'Exact change、operation receipt', stop: 'remote 結果未知卻準備盲目重試', verb: 'Act' },
  { id: '08', name: 'Verify', question: '哪一層 evidence 才支持 intended claim？', output: 'Static → targeted → runtime → external', stop: 'claim 超過已跑的驗證層級', verb: 'Prove' },
  { id: '09', name: 'Record', question: '結果應回到哪個 owning truth layer？', output: 'Current docs / issue / test / release record', stop: '探索歷史冒充正式 current truth', verb: 'Land' },
  { id: '10', name: 'Deliver', question: '接手者能否不重讀對話就執行？', output: 'Self-contained handoff', stop: 'artifact ready 被誤當 adopted', verb: 'Transfer' },
  { id: '11', name: 'Evolve', question: '這個 pattern 值得沉澱還是應該 pruning？', output: 'Rule / Skill / helper / test / no promotion', stop: '只因一次成功就過度制度化', verb: 'Learn' },
  { id: '12', name: 'Close', question: 'Objective、evidence、truth 與 risk 是否都收口？', output: 'Precise closure state', stop: '仍有 adoption 或 residual risk 沒有 owner', verb: 'Close' },
];

export const evidenceLevels = [
  { value: 1, name: 'Static / Readback', proof: 'Diff、schema、route、file 或 record 回讀', claim: '變更存在，結構符合預期', not: 'Runtime 或業務成功' },
  { value: 2, name: 'Targeted', proof: '指定 unit / integration / boundary checks', claim: '指定 contract 在測試範圍通過', not: 'Full regression coverage' },
  { value: 3, name: 'Full Suite', proof: '實際完成完整 suite', claim: 'Suite 覆蓋範圍內未見 regression', not: 'Live environment 或 external state' },
  { value: 4, name: 'Runtime Smoke', proof: '真 process、service、config、browser/API path', claim: '指定 live path 當下可運作', not: '完整跨角色業務閉環' },
  { value: 5, name: 'True-chain', proof: '真 UI、core API/data、角色或 state transition', claim: '指定 end-to-end chain 閉環', not: 'Artifact freshness 或使用者 adoption' },
  { value: 6, name: 'Artifact Freshness', proof: 'Source、build、artifact、runtime binding', claim: 'Runtime 使用正確、fresh artifact/config', not: 'Downstream adoption 已完成' },
  { value: 7, name: 'External Closure', proof: 'Delivered、adopted、evidence returned、verified', claim: '指定外部結果 verified and closed', not: '框架保證所有 future outcomes' },
];

export const capabilityLayers = [
  { name: 'Configured', note: '設定存在；只證明控制面有記錄。' },
  { name: 'Exposed', note: '能力出現在 current task 的 tool surface。' },
  { name: 'Authenticated', note: 'Session 有效；仍未證明身份與 workspace 正確。' },
  { name: 'Identity', note: '精確 account / workspace 已 read back。' },
  { name: 'Target access', note: '指定 target 真正可讀或可寫。' },
  { name: 'Authorized', note: '本次 mutation class 有清楚 authority。' },
];

export const searchEntries = [
  { title: '開始一個任務', type: 'Action', path: '/start/', keywords: 'classifier fast standard assured risk' },
  { title: 'Operating Loop', type: 'System', path: '/system/', keywords: 'objective boundary evidence verify closure' },
  { title: 'Evidence Matcher', type: 'Tool', path: '/system/evidence/', keywords: 'claim verified inferred unknown proof' },
  { title: 'Task Workbench', type: 'Tool', path: '/workbench/', keywords: 'brief export markdown objective authority' },
  { title: 'Playbooks', type: 'Reference', path: '/playbooks/', keywords: 'fast standard assured' },
  { title: 'Codex Stack', type: 'Guide', path: '/codex/', keywords: 'agents memory skill plugin connector mcp browser' },
  { title: 'Cases', type: 'Examples', path: '/cases/', keywords: 'configured bugfix timeout remote write' },
  { title: '四週採用', type: 'Guide', path: '/adopt/', keywords: 'personal team adoption week' },
  ...lessons.map((item) => ({ title: item.title, type: 'Chapter', path: `/learn/${item.slug}/`, keywords: `${item.signal} ${item.description}` })),
  ...templates.map((item) => ({ title: item.title, type: 'Template', path: `/toolkit/${item.slug}/`, keywords: `${item.mode} ${item.purpose}` })),
  ...cases.map((item) => ({ title: item.title, type: 'Case', path: `/cases/${item.slug}/`, keywords: `${item.eyebrow} ${item.lesson}` })),
];
