# Evidence-Gated Agentic Workflow

這個 repository 提供一套供新軟件與網頁項目採用的文件及協作 starter：通用工作入口、來源路由、三類協作標準、九份 Runbook、八種文件模板，以及只處理本地 Markdown 的工具。它提供工作方法和可填骨架；產品規則、技術棧、服務、runner 與驗收由各項目的 owner 決定。

一般採用的固定版本為 `v0.3.0-rc.4`；公開 Release 的核對條件與來源身份見下方[版本與來源身份](#版本與來源身份)。候選 branch 與本地 clone 只供 maintainer 以已核實的 commit 預演，不能代替公開版本驗收。

RC4 包含更新後的 AGENTS.md、工作標準、九份 Runbook 及八種文件模板，並將任務登記、SDD／TDD 與完整開發 Loop 納入同一固定版本；各項改動及採納條件見 [CHANGELOG](CHANGELOG.md)。新項目沿該 tag 的文件採用，初始化後取得三份項目核心 draft；`main` 後續更新不會自動改變已固定的版本。

Evidence-Gated Agentic Workflow 是本 repository 自定義的描述性名稱，不是正式標準、安全認證或 formal assurance case；目前亦沒有以 benchmark 證明其 operational effectiveness。

## 第一次使用

從這裡完成三步：下載固定版本、開啟項目資料夾、把開場提示交給 AI。完整的來源驗證與初始化沿用下方[採用狀態路由](#採用前先辨認工作狀態)及[採用程序](#從固定版本採用)。

**版本說明：** RC4 將本首次使用入口、同版開場提示、更新後的 AGENTS／核心文件入口與九份 Runbook 一併提供；從固定版本取得後沿該 checkout 內的 README／AGENTS 開始。

### 1. 下載固定版本

以下使用 macOS／Linux 的 sh 相容終端機，先確保 Git 可用。把 `PROJECT_DIR` 改成自己的項目絕對路徑；目的地須尚未存在，父目錄須已存在。若已有 checkout，直接前往下一步，讓 AI 按實際狀態處理。

~~~sh
(
  set -eu
  PROJECT_DIR="$HOME/my-new-project"
  if [ -e "$PROJECT_DIR" ] || [ -L "$PROJECT_DIR" ]; then
    printf '目標已存在，請保留原資料並選擇新的 PROJECT_DIR。\n' >&2
    exit 1
  fi
  git clone --branch v0.3.0-rc.4 --single-branch \
    https://github.com/Alex0158/evidence-gated-agentic-workflow.git \
    "$PROJECT_DIR"
  printf '已下載，請在 AI 工具開啟：%s\n' "$PROJECT_DIR"
)
~~~

這一步只下載來源，尚未完成 Release 身份驗證或初始化。保持下載的檔案原樣，讓 AI 按[版本與來源身份](#版本與來源身份)核實後再執行初始化。

### 2. 開啟項目資料夾

在 AI 開發工具中，開啟剛才的 `PROJECT_DIR` 作為工作目錄／workspace：選擇同時包含 `README.md`、`AGENTS.md` 和 `.git` 的那一層。若 clone 顯示 `detached HEAD`，這是選定固定 tag 的正常狀態；後續採用程序會建立項目工作 branch，不需為消除提示而切換到 main。

初始化還需要 Python 3.11+，以及支援 Release 驗證且有相應登入／存取能力的 GitHub CLI。讓 AI 沿[版本與來源身份](#版本與來源身份)及[項目工程入口](項目文件/00-協作與執行/項目工程入口.md)檢查前提；工具或登入不可用時，先處理該缺口。

### 3. 複製開場提示給新 AI

填寫項目名稱與一兩句初步想法，再把整段貼給已開啟項目資料夾的 AI。這段是本次任務的交接文字；協作規則與程序仍由 Repo 中既有的 owner 承接。

~~~text
我要使用這份通用底座開始一個新的軟件開發項目。

項目名稱：［填寫名稱］
初步想法：［描述想做甚麼、給誰使用］

目前工作目錄是剛從已發布固定版本取得、尚未初始化的 checkout；請先實際核對。
請先閱讀根目錄 README.md 和 AGENTS.md，再沿引用按需閱讀。不要依賴先前對話，也不要把本次工作當成維護通用底座。

請依 README 核對工具、Release 與來源身份，使用既有 checkout 的採用路徑，在目前目錄建立工作分支、初始化並完成文件檢查，不要再巢狀 clone。若實際狀態不同，依 README 的狀態路由處理。
完成後核對原有 AGENTS.md、工作標準及九份 Runbook 均保留，簡短說明生成的三份核心草稿及 active binding，再按「啟動項目 Runbook」與我討論產品骨架。先提出會影響下一步的關鍵問題；確認方向前先不要寫產品程式碼。

本次可以進行上述本地檢查、初始化及整理草稿。暫時不要 push、建立遠端 Repo、部署或發布。
若缺少工具、需要登入或核對不一致，指出具體問題並保留現況，不跳過核對。
~~~

## 先從哪裡開始

- 人類或新 session：本 README 是唯一的底座採用入口。
- Agent 工作邊界：[AGENTS.md](AGENTS.md)。
- 產品、業務、技術、決策及工作內容的來源：[項目文件來源目錄](項目文件/README.md)。
- 選擇本次工作的程序：[00 工作路由](項目文件/00-協作與執行/README.md)。
- Repo、工具、命令、環境及 runner：[項目工程入口](項目文件/00-協作與執行/項目工程入口.md)。

九份 Runbook（含任務登記與分流、規格驅動開發及測試驅動開發共用子程序）和八種模板由上述路由及工程入口定位；開發主 Loop 串接規格、實作、驗證與回跳，重要發現可先最小登記再補齊。舊方法文章、案例、探索及 Codex adapter 保留為參考，採用者不需要先讀完整個 repository。

<a id="採用前先辨認工作狀態"></a>

## 採用前先辨認工作狀態

README 是採用流程的唯一 owner；先按目前目錄狀態選入口，再看下方的共用採用程序。`PROJECT_DIR` 一律填絕對路徑。新目錄模式要求其父目錄已存在；既有 checkout 模式會在該 checkout 根目錄完成採用，不會再巢狀 clone。

| 目前狀態 | 下一步 |
| --- | --- |
| 尚未取得項目目錄 | 用 `DESTINATION_MODE='new'`，指定不存在的新 `PROJECT_DIR`，並從該路徑的既有父目錄執行。 |
| 已取得乾淨、未初始化的 Git checkout | 先檢查 ignored files 與項目資料，再用 `DESTINATION_MODE='existing'` 指向該 checkout 根目錄；驗證來源後在同一根目錄建立工作 branch 並初始化，不要再 clone。既有 `origin` 保留；只有能明確辨認為此 workflow 上游來源時才按下方規則調整。 |
| 已初始化的項目 | 以 `.workflow/instance.json` 為唯一 active binding，沿項目文件來源目錄及工作路由繼續工作；不要再次執行初始化器。 |
| 有 partial receipt、非空核心文件、自訂／不確定 binding、未追蹤或 ignored 項目資料，或來源／branch 衝突 | 停止初始化並保留現況。依[項目工程入口](項目文件/00-協作與執行/項目工程入口.md)及[啟動項目 Runbook](項目文件/00-協作與執行/Runbooks/啟動項目.md)的 recovery 分支核對 owner；需要時改在新目的地明確採納。不要用 reset、clean、force 或刪檔重試。 |
| 維護底座模板 | 按底座 maintainer scope 工作。`.workflow/project.json` 的 `TEMPLATE` 狀態本身不會觸發產品初始化，也不代表要把底座 repository 轉成某個產品項目。 |

`v0.3.0-rc.2` 的來源包含本節起點分流及初始化後交接指引；已發布的 `v0.3.0-rc.1` tag 與 Release 保持原樣，其 attestation 不涵蓋 RC2 改動。RC3 將完整首次使用入口、同版開場提示及採用程序放在同一固定版本；RC4 再納入更新後的 AGENTS、工作標準、九份 Runbook 及其模板。新採用者依該 checkout 內的文件即可開始，不必切到 `main` 或依賴另一個私人對話。版本是否已公開仍須按下節核對，README 或 metadata 的版號或 merge 不代表公開 Release 已完成。既有 RC1、RC2 或 RC3 項目毋須重新初始化；若採納新指引，先比較與項目現有 owner 的差異，不覆寫 active binding 或產品內容。

## 版本與來源身份

- 公開上游 repository 的身份網址是 [Alex0158/evidence-gated-agentic-workflow](https://github.com/Alex0158/evidence-gated-agentic-workflow)。變更歷史以 [Commits](https://github.com/Alex0158/evidence-gated-agentic-workflow/commits/main) 核對；tag 與 Release 狀態分別以 [Tags](https://github.com/Alex0158/evidence-gated-agentic-workflow/tags) 及 [Releases](https://github.com/Alex0158/evidence-gated-agentic-workflow/releases) 核實。
- 固定採用版本為 `v0.3.0-rc.4`。一般採用者須先在[精確 Release 頁面](https://github.com/Alex0158/evidence-gated-agentic-workflow/releases/tag/v0.3.0-rc.4)確認 Release 已公開、`draft=false`、`prerelease=true`、`latest=false`、`immutable=true`；不要使用 `/releases/latest`。公開狀態和發布時間以 GitHub Release 的實際狀態、`published_at` 及可回查 receipt 為準。本 README 的準備或合併本身不代表 Release 已公開。
- 透過 GitHub CLI 驗證時，先確認目前安裝版本支援 `gh release verify`，且目前登入／存取狀態能讀取該 Release；不要假設任一 CLI 版本或未登入環境都支援此命令。執行：

~~~sh
gh release verify v0.3.0-rc.4 --repo Alex0158/evidence-gated-agentic-workflow --format json
~~~

在成功驗證的輸出中，找到 `verificationResult.statement.subject` 內 URI 精確符合 `pkg:github/Alex0158/evidence-gated-agentic-workflow@v0.3.0-rc.4` 的記錄。本底座使用 annotated tag；該 subject 的 `digest.sha1` 是 tag object SHA，不是其指向的 commit SHA。將這個完整值填入下方 `ATTESTED_TAG_OBJECT`，查詢該物件的 target：

~~~sh
ATTESTED_TAG_OBJECT='FULL_TAG_OBJECT_SHA_FROM_MATCHING_RELEASE_ATTESTATION_SUBJECT'
gh api "repos/Alex0158/evidence-gated-agentic-workflow/git/tags/$ATTESTED_TAG_OBJECT" --jq '.object | {type, sha}'
~~~

回傳須為 `type=commit`；將其完整 `sha` 填入採用程序的 `EXPECTED_COMMIT`，並沿用同一 `ATTESTED_TAG_OBJECT`。核對鏈路為 **attestation subject → tag object → peeled commit**：fetch 精確 tag ref 後比對 tag object SHA，再比對 `refs/tags/$RELEASE_TAG^{commit}` 與 `EXPECTED_COMMIT`。不要把 subject digest 當 commit SHA，也不要沿用其他版本的值。Release notes 記錄本版完整 commit／tag SHA 供對照，但不能以可編輯 notes 代替 cryptographic identity。Release 不可讀、驗證命令不可用、沒有 matching subject、target 不是 commit 或任一 SHA 不一致時，停止一般採用。RC1 的歷史身份可在其[原 Release](https://github.com/Alex0158/evidence-gated-agentic-workflow/releases/tag/v0.3.0-rc.1)核對。
- Maintainer 預演可從 PR head／GitHub branch readback 取得候選 branch 的完整 commit SHA，並按該 branch/head 核對 [framework-checks workflow run](https://github.com/Alex0158/evidence-gated-agentic-workflow/actions/workflows/framework-checks.yml)。Branch 名稱本身不能證明檢查結果；未完成或 skipped 的 run 不算成功，預演也不代表 Release 已公開。
- 設計基線仍記為 v1.0-rev15。項目 metadata 的 source digest 用來識別設計來源，不是整個底座、下載包或公開 release 的 checksum。
- 公開版本身份以 GitHub 實際 Release、tag peeled commit、attestation 與 CHANGELOG 共同核實。只改版號、有本地 commit 或找到同名 tag，不表示公開版本已驗證。

## 從固定版本採用

<a id="從候選採用"></a>

固定版本是一般採用的主路徑；候選 branch 和 local 只供 maintainer 以已核實的完整 SHA 預演，不能代替公開 Release 驗證。Tag 模式只解析精確的 `refs/tags/$RELEASE_TAG`，核對 attested tag object，再檢查 peeled commit，不會以同名 branch 代替 tag。

採用前先讀[項目工程入口](項目文件/00-協作與執行/項目工程入口.md)的 filesystem 前提，包括 exclusive maintenance、hard link 支援及 symlink／越界保護；環境不符合時停止並保留資料。固定版本模式執行前，先按[版本與來源身份](#版本與來源身份)核實公開 Release、attestation subject、tag object 與 peeled commit，將 tag object SHA 填入 `ATTESTED_TAG_OBJECT`、commit SHA 填入 `EXPECTED_COMMIT`。候選 branch 使用經 readback 的完整 branch SHA；local source 必須是乾淨候選 clone，且 HEAD 和 branch tip 都等於同一預期 SHA。

把每個值替換成自己的內容並保留引號。`DESTINATION_MODE` 使用 `new`（不存在的新目錄）或 `existing`（乾淨、未初始化的 Git checkout）；`SOURCE_MODE` 使用 `release`、`candidate-branch` 或 `local`。候選 branch 模式要核對相應 Actions run；它仍是 maintainer rehearsal。`PROJECT_DIR` 填絕對路徑：new 模式從其已存在的父目錄執行，existing 模式直接在已取得的 checkout root 內採用。執行前確保 `git`、`sh` 和 Python 3.11+ 可用。下方區塊會明確啟動 `sh`，貼入 zsh 等 shell 時仍由 `sh` 執行；`set -eu` 令任何失敗即停止：

~~~sh
sh <<'WORKFLOW_ADOPTION'
set -eu

DESTINATION_MODE='new' # new | existing
SOURCE_MODE='release' # release | candidate-branch | local
WORKFLOW_REPOSITORY='https://github.com/Alex0158/evidence-gated-agentic-workflow.git'
RELEASE_TAG='v0.3.0-rc.4'
CANDIDATE_BRANCH='BRANCH_FROM_PR_HEAD_OR_GITHUB_READBACK'
ATTESTED_TAG_OBJECT='FULL_TAG_OBJECT_SHA_FROM_MATCHING_RELEASE_ATTESTATION_SUBJECT' # release only
EXPECTED_COMMIT='FULL_40_CHARACTER_VERIFIED_PEELED_COMMIT_OR_BRANCH_SHA'
SOURCE_REPO='LOCAL_REPOSITORY_PATH'
PROJECT_DIR='/absolute/path/to/project'
WORK_BRANCH='adopt/workflow-starter'
PROJECT_NAME='My Project'

python3 -c 'import sys; print("Python %s.%s" % sys.version_info[:2]); raise SystemExit(sys.version_info < (3, 11))'
case "$PROJECT_DIR" in
  /*) ;;
  *) printf 'PROJECT_DIR must be an absolute path\n' >&2; exit 1 ;;
esac
git check-ref-format --branch "$WORK_BRANCH"

is_workflow_url() {
  case "$1" in
    "$WORKFLOW_REPOSITORY"|"https://github.com/Alex0158/evidence-gated-agentic-workflow"|"git@github.com:Alex0158/evidence-gated-agentic-workflow.git"|"ssh://git@github.com/Alex0158/evidence-gated-agentic-workflow.git") return 0 ;;
    *) return 1 ;;
  esac
}

case "$SOURCE_MODE" in
  release)
    git check-ref-format "refs/tags/$RELEASE_TAG"
    SOURCE_REMOTE="$WORKFLOW_REPOSITORY"
    SOURCE_REF="refs/tags/$RELEASE_TAG"
    FETCH_REF="$SOURCE_REF:$SOURCE_REF"
    NEW_FETCHED_REF="$SOURCE_REF"
    case "$ATTESTED_TAG_OBJECT" in
      *[!0-9a-f]*|'') printf 'ATTESTED_TAG_OBJECT must be a full lowercase hexadecimal object SHA\n' >&2; exit 1 ;;
    esac
    if [ "${#ATTESTED_TAG_OBJECT}" -ne 40 ]; then
      printf 'ATTESTED_TAG_OBJECT must contain all 40 characters of the tag object SHA\n' >&2
      exit 1
    fi
    ;;
  candidate-branch)
    git check-ref-format --branch "$CANDIDATE_BRANCH"
    SOURCE_REMOTE="$WORKFLOW_REPOSITORY"
    SOURCE_REF="refs/heads/$CANDIDATE_BRANCH"
    FETCH_REF="$SOURCE_REF:refs/remotes/origin/$CANDIDATE_BRANCH"
    NEW_FETCHED_REF="refs/remotes/origin/$CANDIDATE_BRANCH"
    ;;
  local)
    git check-ref-format --branch "$CANDIDATE_BRANCH"
    SOURCE_REMOTE=$(git -C "$SOURCE_REPO" rev-parse --show-toplevel)
    test -z "$(git -C "$SOURCE_REPO" status --porcelain --untracked-files=normal)"
    test "$(git -C "$SOURCE_REPO" rev-parse HEAD)" = "$EXPECTED_COMMIT"
    test "$(git -C "$SOURCE_REPO" rev-parse --verify "refs/heads/$CANDIDATE_BRANCH^{commit}")" = "$EXPECTED_COMMIT"
    SOURCE_REF="refs/heads/$CANDIDATE_BRANCH"
    FETCH_REF="$SOURCE_REF:refs/remotes/origin/$CANDIDATE_BRANCH"
    NEW_FETCHED_REF="refs/remotes/origin/$CANDIDATE_BRANCH"
    ;;
  *) printf 'SOURCE_MODE must be release, candidate-branch, or local\n' >&2; exit 2 ;;
esac

case "$EXPECTED_COMMIT" in
  *[!0-9a-f]*|'') printf 'EXPECTED_COMMIT must be a full lowercase hexadecimal commit SHA\n' >&2; exit 1 ;;
esac
if [ "${#EXPECTED_COMMIT}" -ne 40 ]; then
  printf 'EXPECTED_COMMIT must contain all 40 characters of the commit SHA\n' >&2
  exit 1
fi

case "$DESTINATION_MODE" in
  new)
    if [ -e "$PROJECT_DIR" ] || [ -L "$PROJECT_DIR" ]; then
      printf 'new PROJECT_DIR must not already exist: %s\n' "$PROJECT_DIR" >&2; exit 1
    fi
    PROJECT_PARENT=$(dirname "$PROJECT_DIR")
    if [ ! -d "$PROJECT_PARENT" ]; then
      printf 'PROJECT_DIR parent must already exist: %s\n' "$PROJECT_PARENT" >&2; exit 1
    fi
    PROJECT_PARENT=$(cd -- "$PROJECT_PARENT" && pwd -P)
    PROJECT_DIR="$PROJECT_PARENT/$(basename "$PROJECT_DIR")"
    git init -- "$PROJECT_DIR"
    git -C "$PROJECT_DIR" remote add origin "$SOURCE_REMOTE"
    git -C "$PROJECT_DIR" fetch --no-tags origin "$FETCH_REF"
    FETCHED_REF="$NEW_FETCHED_REF"
    ;;
  existing)
    if [ ! -d "$PROJECT_DIR" ] || [ -L "$PROJECT_DIR" ]; then
      printf 'existing PROJECT_DIR must be a real directory: %s\n' "$PROJECT_DIR" >&2; exit 1
    fi
    PROJECT_DIR=$(cd -- "$PROJECT_DIR" && pwd -P)
    test "$(git -C "$PROJECT_DIR" rev-parse --show-toplevel)" = "$PROJECT_DIR"
    test -z "$(git -C "$PROJECT_DIR" status --porcelain --untracked-files=normal)"
    if [ ! -f "$PROJECT_DIR/.workflow/project.json" ] || [ -L "$PROJECT_DIR/.workflow/project.json" ] || [ -e "$PROJECT_DIR/.workflow/instance.json" ] || [ -L "$PROJECT_DIR/.workflow/instance.json" ]; then
      printf 'existing checkout is not an uninitialized project template\n' >&2; exit 1
    fi
    PROJECT_MODE=$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1], encoding="utf-8"))["project"]["mode"])' "$PROJECT_DIR/.workflow/project.json")
    if [ "$PROJECT_MODE" != 'TEMPLATE' ]; then
      printf 'existing checkout is initialized; preserve it and use its owner route\n' >&2; exit 1
    fi
    for STATE_FILE in "$PROJECT_DIR"/.workflow/init-receipt.json "$PROJECT_DIR"/.workflow/init-config-before.json "$PROJECT_DIR"/.workflow/init-candidate-*.json "$PROJECT_DIR"/.workflow/init-partial-*.json; do
      if [ -e "$STATE_FILE" ] || [ -L "$STATE_FILE" ]; then
        printf 'initialization state must be reviewed and preserved: %s\n' "$STATE_FILE" >&2; exit 1
      fi
    done
    if git -C "$PROJECT_DIR" show-ref --verify --quiet "refs/heads/$WORK_BRANCH"; then
      printf 'WORK_BRANCH already exists; choose a reviewed unused branch name: %s\n' "$WORK_BRANCH" >&2; exit 1
    fi
    if git -C "$PROJECT_DIR" remote | grep -Fxq workflow-upstream; then
      EXISTING_UPSTREAM=$(git -C "$PROJECT_DIR" remote get-url --all workflow-upstream) || { printf 'workflow-upstream has no readable URL; preserve remotes and inspect it before adoption\n' >&2; exit 1; }
      if ! is_workflow_url "$EXISTING_UPSTREAM" || ! is_workflow_url "$(git -C "$PROJECT_DIR" remote get-url --push --all workflow-upstream)"; then
        printf 'workflow-upstream URL is unrecognized; preserve remotes and inspect it before adoption\n' >&2; exit 1
      fi
    fi
    ORIGIN_ACTION='preserve'
    if git -C "$PROJECT_DIR" remote | grep -Fxq origin; then
      ORIGIN_URL=$(git -C "$PROJECT_DIR" remote get-url --all origin) || { printf 'origin has no readable URL; preserve remotes and inspect it before adoption\n' >&2; exit 1; }
    else
      ORIGIN_URL=''
    fi
    if is_workflow_url "$ORIGIN_URL"; then
      ORIGIN_PUSH_URL=$(git -C "$PROJECT_DIR" remote get-url --push --all origin)
      if ! is_workflow_url "$ORIGIN_PUSH_URL"; then
        printf 'origin has a different push URL; preserve remotes and inspect it before adoption\n' >&2; exit 1
      fi
      if git -C "$PROJECT_DIR" remote get-url workflow-upstream >/dev/null 2>&1; then
        printf 'both origin and workflow-upstream identify the base; preserve remotes and reconcile before adoption\n' >&2; exit 1
      fi
      ORIGIN_ACTION='rename-to-workflow-upstream'
    fi
    if [ "$SOURCE_MODE" = 'release' ]; then
      git -C "$PROJECT_DIR" fetch --no-tags "$SOURCE_REMOTE" "$SOURCE_REF:refs/tags/$RELEASE_TAG"
      FETCHED_REF="refs/tags/$RELEASE_TAG"
    else
      git -C "$PROJECT_DIR" fetch --no-tags "$SOURCE_REMOTE" "$SOURCE_REF"
      FETCHED_REF='FETCH_HEAD'
    fi
    ;;
  *) printf 'DESTINATION_MODE must be new or existing\n' >&2; exit 2 ;;
esac

if [ "$SOURCE_MODE" = 'release' ]; then
  FETCHED_TAG_OBJECT=$(git -C "$PROJECT_DIR" rev-parse --verify "$FETCHED_REF")
  if [ "$(git -C "$PROJECT_DIR" cat-file -t "$FETCHED_TAG_OBJECT")" != 'tag' ]; then
    printf 'the selected release ref is not an annotated tag object\n' >&2; exit 1
  fi
  test "$FETCHED_TAG_OBJECT" = "$ATTESTED_TAG_OBJECT"
fi
CANDIDATE_COMMIT=$(git -C "$PROJECT_DIR" rev-parse --verify "$FETCHED_REF^{commit}")
test "$CANDIDATE_COMMIT" = "$EXPECTED_COMMIT"
if [ "$DESTINATION_MODE" = 'existing' ]; then
  test "$(git -C "$PROJECT_DIR" rev-parse HEAD)" = "$EXPECTED_COMMIT"
  test -z "$(git -C "$PROJECT_DIR" status --porcelain --untracked-files=normal)"
fi
for NATIVE_FILE in AGENTS.md .workflow/project.json scripts/init_project.py scripts/check_docs.py scripts/create_document.py '項目文件/00-協作與執行/README.md'; do
  git -C "$PROJECT_DIR" cat-file -e "$CANDIDATE_COMMIT:$NATIVE_FILE"
done
git -C "$PROJECT_DIR" show "$CANDIDATE_COMMIT:.workflow/project.json"

git -C "$PROJECT_DIR" switch --create "$WORK_BRANCH" "$CANDIDATE_COMMIT"
(
  cd -- "$PROJECT_DIR"
  python3 -B scripts/init_project.py --project-name "$PROJECT_NAME"
  python3 -B scripts/check_docs.py
  python3 -B scripts/check_docs.py --project-docs
)
if [ "$DESTINATION_MODE" = 'new' ]; then
  git -C "$PROJECT_DIR" remote rename origin workflow-upstream
  git -C "$PROJECT_DIR" remote set-url workflow-upstream "$WORKFLOW_REPOSITORY"
else
  case "$ORIGIN_ACTION" in
    rename-to-workflow-upstream) git -C "$PROJECT_DIR" remote rename origin workflow-upstream ;;
    preserve)
      if ! git -C "$PROJECT_DIR" remote get-url workflow-upstream >/dev/null 2>&1; then
        git -C "$PROJECT_DIR" remote add workflow-upstream "$WORKFLOW_REPOSITORY"
      fi
      ;;
  esac
fi
git -C "$PROJECT_DIR" config --local push.default nothing
git -C "$PROJECT_DIR" remote -v
git -C "$PROJECT_DIR" rev-parse HEAD
WORKFLOW_ADOPTION
~~~

`existing` 模式要求 Git root、乾淨 working tree、`TEMPLATE` mode、沒有 active instance 或 init receipt／partial receipt；執行前亦須檢查 ignored files 與項目資料。更細的 binding、產品文件與目錄 preflight 由唯一 initializer `scripts/init_project.py` 負責；它拒絕自訂狀態而不覆寫，部分失敗則留下 recovery receipt。若拒絕或部分失敗，保留已建立的 verified work branch、所有原文件及 receipt，依[啟動項目 Runbook](項目文件/00-協作與執行/Runbooks/啟動項目.md) recovery，不 reset／clean／刪檔。Release 來源比對 attested tag object 與 peeled commit；branch/local rehearsal 比對各自完整 commit SHA。已知指向 workflow repository 的 `origin` 會在無名稱衝突時改名為 `workflow-upstream`；項目或身份未確認的 `origin` 原樣保留。現有 `workflow-upstream` URL 不明、兩個 remote 都指向底座或工作 branch 已存在時，不改 remote／branch／文件並停止。

初始化成功後，將 `PROJECT_DIR` 當作實際項目／workspace 根目錄；`.workflow/instance.json` 是 active binding，`.workflow/project.json` 仍是底座 metadata／framework baseline。原有 AGENTS.md、工作標準與九份 Runbook 沿用本次已核實 tag 的內容，初始化器不另行生成或改寫它們。三個生成 draft 固定落在 `項目文件/01-產品需求/產品骨架.md`、`項目文件/02-業務規格/業務模組/規格草稿.md`、`項目文件/03-系統設計/系統設計草稿.md`；產品／業務／技術語義仍由各自 owner 定義。接著按[啟動項目 Runbook](項目文件/00-協作與執行/Runbooks/啟動項目.md)整理問題、角色、主流程、scope 與假設，再判斷近期 slice readiness；初始化或模板文字不代表需求已確認。Runbook 是 brainstorm 與 handoff 的唯一程序 owner，這裡不複製它的問題清單或規則。

初始化 draft 以外的五種 template ID 為 business-flow、decision、task、verification、delivery，按需建立：

~~~sh
(
  set -eu
  PROJECT_DIR='/absolute/path/to/project'
  git -C "$PROJECT_DIR" rev-parse --show-toplevel >/dev/null
  cd -- "$PROJECT_DIR"
  python3 -B scripts/create_document.py --template business-flow --filename example-flow
)
~~~

生成文件不等於產品語義已確認；不要預造完整空文件樹，也不要以文件數或百分比宣稱 readiness。

### 綁定項目與工具

初始化後先讀 `.workflow/instance.json`；它是項目的 active binding。`.workflow/project.json` 保留底座 metadata／framework baseline。按實際 owner 填項目名稱、用途及 repo 邊界；核實 repositories 路徑，並只為本項目真實存在的 runner 設定 entry 和 argv。不存在的產品 runner 保持 null，相關 evidence 記為 NOT_RUN。Secrets 只記錄已授權的 secure retrieval reference，不寫入檔案或命令。

文件檢查的 PASS 只涵蓋 checker 實際檢查的靜態條件。default check 和 `--project-docs` 的擴展範圍由工程入口說明；兩者都不是完整的全 repository Markdown 驗證，更不是產品 build、test、runtime、deployment 或 user acceptance。

## 分開上游與項目 repository

新目錄模式會把採用來源設為 `workflow-upstream`；既有 checkout 的項目 `origin` 原樣保留。先核實 `git remote -v`：沒有項目 `origin` 時，建立並確認項目自己的 repository 後才新增；已有項目 `origin` 時沿用並確認 URL。身份不明或指向 workflow 上游的 `origin` 不可當作項目 remote。只在確認 `origin` 是項目 repository 後，設定預設 push target：

~~~sh
(
set -eu
PROJECT_DIR='/absolute/path/to/project'
PROJECT_ORIGIN_URL='PROJECT_REPOSITORY_URL'
git -C "$PROJECT_DIR" rev-parse --show-toplevel >/dev/null
if ! git -C "$PROJECT_DIR" remote get-url origin >/dev/null 2>&1; then
  git -C "$PROJECT_DIR" remote add origin "$PROJECT_ORIGIN_URL"
fi
test "$(git -C "$PROJECT_DIR" remote get-url origin)" = "$PROJECT_ORIGIN_URL"
git -C "$PROJECT_DIR" config --local remote.pushDefault origin
git -C "$PROJECT_DIR" config --local push.default nothing
git -C "$PROJECT_DIR" remote -v
git -C "$PROJECT_DIR" config --local --get remote.pushDefault
git -C "$PROJECT_DIR" config --local --get push.default
)
~~~

先按項目資料性質選擇 public 或 private visibility。上述設定令沒有明確 refspec 的 `git push` 失敗；這不是服務端權限或完整防護。明確 refspec、其他設定及外部工具仍可指定目的地，所以每次外部寫入都須先核對 target 和授權。設定 remote 本身不會 push。

第一次 push、開啟 Issues 或邀請 PR 協作之前，逐一檢查 clone 帶入的 `.github/`、`SECURITY.md`、`CONTRIBUTING.md`、`GOVERNANCE.md` 和 license 說明。它們是上游底座維護用內容；由項目 owner 設定自己的回報入口和協作規則，並保留適用的來源署名。初始化器不會自動搬走或刪除這些檔案。也要核對 `.gitignore`；以 `git check-ignore -v` 和 `git status --short --ignored` 檢查 private／audit／memory 等路徑是否意外略過項目資料，按項目 owner 精準調整，不要刪除資料或移除秘密保護。

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

## License

編纂與授權者：[Alex0158](https://github.com/Alex0158)。

本 repository 的文字、圖表、文件模板及其他方法論模板沿用 [Creative Commons Attribution 4.0 International](LICENSE)。新工具程式的 scripts/**、tests/** 及 .github/workflows/** 依 [MIT License](LICENSE-CODE) 授權。兩種授權的範圍不同；不要把一種授權推定為另一種的替代。

底座 license 不替採用者決定新產品的原創內容或程式碼授權。各項目 owner 應按自己的權利與產品需要選擇 license，並核實其相依內容和來源。

## 延伸參考與舊文件身份

README、AGENTS.md、項目文件來源目錄及 00 工作路由是採用與工作入口。docs/、templates/、examples/、explorations/ 和 integrations/ 中保留的舊方法論文章、舊模板、案例、探索及 Codex adapter 供按需參考；它們不另行裁決目前工作規則，也不構成平行的採用流程。若參考內容和目前入口衝突，依本 repository 的 GOVERNANCE.md 所列 owner 路由核實。
