# Evidence-Gated Agentic Workflow

這個 repository 提供一套供新軟件與網頁項目採用的文件及協作 starter：通用工作入口、來源路由、三類協作標準、六份 Runbook、八種文件模板，以及只處理本地 Markdown 的工具。它提供工作方法和可填骨架；產品規則、技術棧、服務、runner 與驗收由各項目的 owner 決定。

目前整合版本是候選 0.3.0-rc.1；候選分支 `integration/starter-r15` 已可從 GitHub 取得。PR、tag 與 Release 的現況見下方[「版本與來源身份」](#版本與來源身份)。採用前請在 [framework-checks workflow runs](https://github.com/Alex0158/evidence-gated-agentic-workflow/actions/workflows/framework-checks.yml) 開啟對應 run，確認分支及 head commit 與採用時核對的 SHA 相同；branch 名稱本身不能證明檢查結果。下文提供遠端候選和本地 clone 兩種來源選項。

Evidence-Gated Agentic Workflow 是本 repository 自定義的描述性名稱，不是正式標準、安全認證或 formal assurance case；目前亦沒有以 benchmark 證明其 operational effectiveness。

## 先從哪裡開始

- 人類或新 session：本 README 是唯一的底座採用入口。
- Agent 工作邊界：[AGENTS.md](AGENTS.md)。
- 產品、業務、技術、決策及工作內容的來源：[項目文件來源目錄](項目文件/README.md)。
- 選擇本次工作的程序：[00 工作路由](項目文件/00-協作與執行/README.md)。
- Repo、工具、命令、環境及 runner：[項目工程入口](項目文件/00-協作與執行/項目工程入口.md)。

六份 Runbook 和八種模板由上述路由及工程入口定位。舊方法文章、案例、探索及 Codex adapter 保留為參考，採用者不需要先讀完整個 repository。

## 版本與來源身份

- 公開上游 repository 的身份網址是 [Alex0158/evidence-gated-agentic-workflow](https://github.com/Alex0158/evidence-gated-agentic-workflow)。合併狀態以 [PR #1](https://github.com/Alex0158/evidence-gated-agentic-workflow/pull/1) 核對；tag 與 Release 狀態分別以 [Tags](https://github.com/Alex0158/evidence-gated-agentic-workflow/tags) 及 [Releases](https://github.com/Alex0158/evidence-gated-agentic-workflow/releases) 核實。
- 候選版號為 0.3.0-rc.1；branch 可能移動，採用者必須從 PR head 或 GitHub branch readback 取得完整 commit SHA，並核對 clone 後的 SHA。GitHub Actions 狀態須按該 branch/head 的 run 核實，未完成或 skipped 的 run 不算成功。
- 設計基線仍記為 v1.0-rev15。項目 metadata 的 source digest 用來識別設計來源，不是整個底座、下載包或公開 release 的 checksum。
- 發布後，公開版本身份由實際 tag、該 tag 指向的 Git commit 及 CHANGELOG 共同確定。只改版號或有一個本地 commit，不表示已發布。

## 從候選採用

Git 只能 clone 已提交的 commit。可從 GitHub 候選分支或本地 clone 取得來源；遠端 branch 可能移動，因此要先從 PR head 或 GitHub branch readback 取得完整 SHA，再確認 clone 出來的 branch tip 正好相同。若來源仍有未提交變更，停止並先提交候選，不可把舊 HEAD 當成候選。

初始化前先讀[項目工程入口](項目文件/00-協作與執行/項目工程入口.md)的 filesystem 前提，包括 exclusive maintenance、hard link 支援及 symlink／越界保護；環境不符合時停止並保留資料。

先把每個值替換成自己的內容；保留引號。遠端來源使用目前的 `integration/starter-r15`，若 PR 或 branch readback 顯示其他 branch，請改用該名稱及其完整 head SHA。本地來源則填入乾淨的候選 clone 路徑，其 HEAD 必須等於同一個預期 SHA。`PROJECT_DIR` 必須是尚未存在的新目錄；命令在可建立該目錄的父目錄執行。Python 必須是 3.11 或更新版本。整段命令使用 subshell，並在錯誤目錄或 Python 版本不合時停止：

~~~sh
(
set -eu

CANDIDATE_SOURCE='remote' # set to 'local' to use a local clone
WORKFLOW_REPOSITORY='https://github.com/Alex0158/evidence-gated-agentic-workflow.git'
CANDIDATE_BRANCH='integration/starter-r15'
EXPECTED_CANDIDATE_COMMIT='FULL_SHA_FROM_PR_HEAD_OR_GITHUB_BRANCH_READBACK'
SOURCE_REPO='LOCAL_REPOSITORY_PATH'
PROJECT_DIR='new-project'
WORK_BRANCH='adopt/workflow-starter'
PROJECT_NAME='My Project'

python3 -c 'import sys; print("Python %s.%s" % sys.version_info[:2]); raise SystemExit(sys.version_info < (3, 11))'
if [ -e "$PROJECT_DIR" ] || [ -L "$PROJECT_DIR" ]; then
  printf 'PROJECT_DIR must be a new directory: %s\n' "$PROJECT_DIR" >&2
  exit 1
fi

case "$CANDIDATE_SOURCE" in
  remote)
    git clone --origin origin --no-checkout --single-branch --branch "$CANDIDATE_BRANCH" "$WORKFLOW_REPOSITORY" "$PROJECT_DIR"
    CANDIDATE_REF="refs/remotes/origin/$CANDIDATE_BRANCH"
    ;;
  local)
    git -C "$SOURCE_REPO" rev-parse --show-toplevel >/dev/null
    test -z "$(git -C "$SOURCE_REPO" status --porcelain)"
    test "$(git -C "$SOURCE_REPO" rev-parse HEAD)" = "$EXPECTED_CANDIDATE_COMMIT"
    test "$(git -C "$SOURCE_REPO" rev-parse --verify "refs/heads/$CANDIDATE_BRANCH^{commit}")" = "$EXPECTED_CANDIDATE_COMMIT"
    git clone --origin origin --no-checkout --single-branch --branch "$CANDIDATE_BRANCH" "$SOURCE_REPO" "$PROJECT_DIR"
    CANDIDATE_REF="refs/remotes/origin/$CANDIDATE_BRANCH"
    ;;
  *)
    printf 'CANDIDATE_SOURCE must be remote or local\n' >&2
    exit 2
    ;;
esac

CANDIDATE_COMMIT=$(git -C "$PROJECT_DIR" rev-parse --verify "$CANDIDATE_REF^{commit}")
test "$CANDIDATE_COMMIT" = "$EXPECTED_CANDIDATE_COMMIT"
git -C "$PROJECT_DIR" cat-file -e "$CANDIDATE_COMMIT:AGENTS.md"
git -C "$PROJECT_DIR" cat-file -e "$CANDIDATE_COMMIT:scripts/init_project.py"
git -C "$PROJECT_DIR" cat-file -e "$CANDIDATE_COMMIT:項目文件/00-協作與執行/README.md"
git -C "$PROJECT_DIR" show "$CANDIDATE_COMMIT:.workflow/project.json"

git -C "$PROJECT_DIR" checkout --detach "$CANDIDATE_COMMIT"
test "$(git -C "$PROJECT_DIR" rev-parse HEAD)" = "$EXPECTED_CANDIDATE_COMMIT"
git -C "$PROJECT_DIR" switch -c "$WORK_BRANCH"
git -C "$PROJECT_DIR" remote rename origin workflow-upstream
git -C "$PROJECT_DIR" remote set-url workflow-upstream "$WORKFLOW_REPOSITORY"
git -C "$PROJECT_DIR" config --local push.default nothing
git -C "$PROJECT_DIR" remote -v
git -C "$PROJECT_DIR" rev-parse HEAD

(
  cd "$PROJECT_DIR"
  python3 -B scripts/init_project.py --project-name "$PROJECT_NAME"
  python3 -B scripts/check_docs.py
  python3 -B scripts/check_docs.py --project-docs
)
)
~~~

遠端模式會核對 GitHub branch tip 與輸入的完整 SHA；本地模式會核對來源工作樹乾淨且 HEAD 相同。兩者都將來源 remote 命名為 `workflow-upstream`，並在新 branch 上執行同一組初始化與文件檢查。每一步都以前一步成功為前提；失敗時停止並查明原因。初始化只在新 clone 建立缺少的項目入口，不覆寫現有內容。遇到拒絕或 partial result，保留原內容並依工程入口的 recovery 指引處理；不要用 force、reset 或 clean 繞過。

初始化建立三份 draft：產品骨架、近期模組／功能規格、技術設計與契約。它不確認產品需求，也不代表項目已準備完成。先與開發者確認全局目標、價值、scope、使用者群組、主要流程、品質限制與重要架構方向，再深化近期工作的 owner 文件。

八種模板中有三份作為初始化 draft；另外五種依工作需要建立。五種 template ID 為 business-flow、decision、task、verification、delivery。上段命令在 subshell 內完成，離開後會回到原目錄；執行下例前，將 PROJECT_DIR 填成剛建立的 clone 目錄：

~~~sh
(
  set -eu
  PROJECT_DIR='PATH_TO_NEW_PROJECT'
  git -C "$PROJECT_DIR" rev-parse --show-toplevel >/dev/null
  cd "$PROJECT_DIR"
  python3 -B scripts/create_document.py --template business-flow --filename example-flow
)
~~~

filename 是新 Markdown 檔名，不含路徑。template ID 和目的地以項目工程入口所連到的 active binding 為準。生成文件不等於產品語義已確認。不要預造完整空文件樹，也不要以文件數或百分比宣稱 readiness。

### 綁定項目與工具

初始化後，先讀 .workflow/instance.json；它是本項目的 active binding。.workflow/project.json 保留底座 metadata／framework baseline。按實際 owner 填項目名稱、用途及 repo 邊界；核實 repositories 路徑，並只為本項目真實存在的 runner 設定 entry 和 argv。不存在的產品 runner 保持 null，相關 evidence 記為 NOT_RUN。Secrets 只記錄已授權的 secure retrieval reference，不寫入檔案或命令。

文件檢查的 PASS 只涵蓋該 checker 實際檢查的靜態條件。default check 和 --project-docs 的擴展範圍由工程入口說明；兩者都不是完整的全 repository Markdown 驗證，更不是產品 build、test、runtime、deployment 或 user acceptance。

## 分開上游與項目 repository

項目開發應在自己的 repository 和 branch 中進行。上面的 clone 先把採用來源設為 workflow-upstream；它是用來識別及比較通用底座的來源。建立並核實自己的新 repository 後，才把它設為項目 origin：

~~~sh
(
set -eu
PROJECT_DIR='PATH_TO_NEW_PROJECT'
PROJECT_ORIGIN_URL='PROJECT_REPOSITORY_URL'
git -C "$PROJECT_DIR" rev-parse --show-toplevel >/dev/null
git -C "$PROJECT_DIR" remote add origin "$PROJECT_ORIGIN_URL"
git -C "$PROJECT_DIR" config --local remote.pushDefault origin
git -C "$PROJECT_DIR" config --local push.default nothing
git -C "$PROJECT_DIR" remote -v
git -C "$PROJECT_DIR" config --local --get remote.pushDefault
git -C "$PROJECT_DIR" config --local --get push.default
)
~~~

先確認 origin 指向項目自己的 repository，並按項目資料性質選擇 public 或 private visibility。不要把項目內容推到 workflow-upstream。上述本地設定令沒有明確 refspec 的 git push 失敗；這不是服務端權限或完整防護。明確 refspec、其他設定及外部工具仍可指定目的地，所以每次外部寫入都須先核對 target 和授權。設定 remote 本身不會 push。

在第一次 push、開啟 Issues 或邀請 PR 協作之前，逐一檢查 clone 帶入的 .github/、SECURITY.md、CONTRIBUTING.md、GOVERNANCE.md 和 license 說明。它們是上游底座維護用內容；由項目 owner 設定自己的回報入口和協作規則，並保留適用的來源署名。初始化器不會自動搬走或刪除這些檔案。

也要核對 clone 根目錄的 .gitignore。private/、audit/、memory/ 等規則可能影響項目子目錄；以 git check-ignore -v 和 git status --short --ignored 核實真實結果，避免程式碼或需追蹤的項目來源被忽略。按項目 owner 決定精準調整，不要因此刪除資料或移除秘密保護。

## 本地驗證、GitHub CI 與限制

整合候選已完成本機工具契約、文件檢查、隔離 clone／初始化、三核心草稿與五類按需文件生成，以及重複建立／錯配核心路徑的拒絕驗證；README 採用與 remote 分工亦以隔離的本地 repositories 演練。實測 Python 組合與 filesystem 限制見[工程入口](項目文件/00-協作與執行/項目工程入口.md#生成與工程前提)。這些只證明本地框架與採用路徑，不代表產品已實作。

GitHub Actions 的 branch/head 結果須在 [framework-checks workflow runs](https://github.com/Alex0158/evidence-gated-agentic-workflow/actions/workflows/framework-checks.yml) 按實際候選 SHA 核對，不由 branch 名稱推定 PASS。GitHub workflow 是底座維護用檢查；若在下游 repository 被條件略過，skipped 不是已執行，也不證明下游文件或產品通過。候選 CI 不代替發布時對 default branch、tag 與 Release 的查證。

若要聲稱整個 repository 的 Markdown links／anchors 已核對，發布前仍須做一次涵蓋全庫 tracked Markdown 的完整 QA。scripts/check_docs.py 及其 --project-docs 模式都不是這項全庫檢查，不可用它們取代。

候選工具要求 Python 3.11+。實際環境支援聲明只涵蓋已完成並記錄的檢查組合；未跑的組合標為 NOT_RUN。文件檢查與 framework tests 也不代替項目自身的 build、tests、runtime、deployment、安全審查或產品 acceptance。

## 後續採用底座升級

1. 先讀項目目前記錄的採用版本，再選定要比較的上游版本或 commit。
2. 對照候選改動，按產品、業務、技術和工作標準的 owner 決定哪些適用。
3. 逐項採納並核相容性及受影響檢查；不要 pull／merge 整個上游，也不要自動覆寫產品文件、active instance 或項目本地調整。
4. 只在確實採納並驗證 framework 變更後，更新項目記錄的版本。該次選擇與結果留在既有 Task、DEC、VR 或 PR，不另建長期 upgrade ledger。

執行以下 tag clone 命令前，須核實該版本已有公開 Release，且對應 tag 指向預期的 commit；採用者再由該 tag clone，並將 checkout 的 commit 與該版本的 release receipt 核對：

~~~sh
(
set -eu
PROJECT_DIR='new-project'
if [ -e "$PROJECT_DIR" ] || [ -L "$PROJECT_DIR" ]; then
  printf 'PROJECT_DIR must be a new directory: %s\n' "$PROJECT_DIR" >&2
  exit 1
fi
git clone --origin origin --branch 'v0.3.0-rc.1' --single-branch \
  'https://github.com/Alex0158/evidence-gated-agentic-workflow.git' \
  "$PROJECT_DIR"
git -C "$PROJECT_DIR" rev-parse HEAD
)
~~~

## License

編纂與授權者：[Alex0158](https://github.com/Alex0158)。

本 repository 的文字、圖表、文件模板及其他方法論模板沿用 [Creative Commons Attribution 4.0 International](LICENSE)。新工具程式的 scripts/**、tests/** 及 .github/workflows/** 依 [MIT License](LICENSE-CODE) 授權。兩種授權的範圍不同；不要把一種授權推定為另一種的替代。

底座 license 不替採用者決定新產品的原創內容或程式碼授權。各項目 owner 應按自己的權利與產品需要選擇 license，並核實其相依內容和來源。

## 延伸參考與舊文件身份

README、AGENTS.md、項目文件來源目錄及 00 工作路由是採用與工作入口。docs/、templates/、examples/、explorations/ 和 integrations/ 中保留的舊方法論文章、舊模板、案例、探索及 Codex adapter 供按需參考；它們不另行裁決目前工作規則，也不構成平行的採用流程。若參考內容和目前入口衝突，依本 repository 的 GOVERNANCE.md 所列 owner 路由核實。
