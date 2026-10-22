# Evidence-Gated Agentic Workflow

這個 repository 提供一套供新軟件與網頁項目採用的文件及協作 starter：通用工作入口、來源路由、三類協作標準、六份 Runbook、八種文件模板，以及只處理本地 Markdown 的工具。它提供工作方法和可填骨架；產品規則、技術棧、服務、runner 與驗收由各項目的 owner 決定。

一般採用的固定版本為 `v0.3.0-rc.1`；公開 Release 的核對條件與來源身份見下方[版本與來源身份](#版本與來源身份)。候選 branch 與本地 clone 只供 maintainer 以已核實的 commit 預演，不能代替公開版本驗收。

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
- 固定採用版本為 `v0.3.0-rc.1`。一般採用者須先在[精確 Release 頁面](https://github.com/Alex0158/evidence-gated-agentic-workflow/releases/tag/v0.3.0-rc.1)確認 Release 已公開、`draft=false`、`prerelease=true`、`latest=false`；不要使用 `/releases/latest`。公開狀態和發布時間以 GitHub Release 的實際狀態、`published_at` 及可回查 receipt 為準。本 README 的準備或合併本身不代表 Release 已公開。
- 透過 GitHub CLI 驗證時，先確認目前安裝版本支援 `gh release verify`，且目前登入／存取狀態能讀取該 Release；不要假設任一 CLI 版本或未登入環境都支援此命令。執行：

~~~sh
gh release verify v0.3.0-rc.1 --repo Alex0158/evidence-gated-agentic-workflow --format json
~~~

只有驗證成功且 attestation 的完整 commit SHA 可確認時才繼續。取得來源後，核對 tag peeled commit (`refs/tags/$RELEASE_TAG^{commit}`) 與該 SHA 完全相同。Annotated tag object SHA 與其指向的 commit SHA 可以不同；不能把兩者混用。Release 不可讀、驗證命令不可用或 SHA 不一致時，停止一般採用。
- Maintainer 預演可從 PR head／GitHub branch readback 取得候選 branch 的完整 commit SHA，並按該 branch/head 核對 [framework-checks workflow run](https://github.com/Alex0158/evidence-gated-agentic-workflow/actions/workflows/framework-checks.yml)。Branch 名稱本身不能證明檢查結果；未完成或 skipped 的 run 不算成功，預演也不代表 Release 已公開。
- 設計基線仍記為 v1.0-rev15。項目 metadata 的 source digest 用來識別設計來源，不是整個底座、下載包或公開 release 的 checksum。
- 公開版本身份以 GitHub 實際 Release、tag peeled commit、attestation 與 CHANGELOG 共同核實。只改版號、有本地 commit 或找到同名 tag，不表示公開版本已驗證。

## 從固定版本採用

<a id="從候選採用"></a>

固定版本是一般採用的主路徑；下方保留候選 branch 和 local 兩種 maintainer 預演來源。每種來源都先核對完整 commit SHA，再 detached checkout，最後才建立項目自己的工作 branch。Tag 模式只解析精確的 `refs/tags/$RELEASE_TAG^{commit}`，不會以同名 branch 代替 tag。

採用前先讀[項目工程入口](項目文件/00-協作與執行/項目工程入口.md)的 filesystem 前提，包括 exclusive maintenance、hard link 支援及 symlink／越界保護；環境不符合時停止並保留資料。固定版本模式執行前，先按[版本與來源身份](#版本與來源身份)核實公開 Release、attestation 與完整 commit SHA，並將已確認的 SHA 填入 `EXPECTED_COMMIT`。本地來源須是乾淨的候選 clone；其 HEAD 與 branch tip 都必須等於同一預期 SHA。

先把每個值替換成自己的內容；保留引號。`SOURCE_MODE` 使用 `release`（一般採用）、`candidate-branch` 或 `local`。候選 branch 模式須使用 PR head／GitHub branch readback 的實際名稱和完整 SHA，並核對相應 Actions run；本地模式另填乾淨 clone 的 branch 名稱與路徑。`PROJECT_DIR` 必須是尚未存在的新目錄，亦不得是 symlink；命令在可建立該目錄的父目錄執行。執行前須確保 `git`、`sh` 和 Python 3.11+ 可用。整段命令使用 `set -eu` subshell，任何失敗即停止：

~~~sh
(
set -eu

SOURCE_MODE='release' # release | candidate-branch | local
WORKFLOW_REPOSITORY='https://github.com/Alex0158/evidence-gated-agentic-workflow.git'
RELEASE_TAG='v0.3.0-rc.1'
CANDIDATE_BRANCH='BRANCH_FROM_PR_HEAD_OR_GITHUB_READBACK'
EXPECTED_COMMIT='FULL_40_CHARACTER_SHA_FROM_RELEASE_ATTESTATION_OR_BRANCH_READBACK'
SOURCE_REPO='LOCAL_REPOSITORY_PATH'
PROJECT_DIR='new-project'
WORK_BRANCH='adopt/workflow-starter'
PROJECT_NAME='My Project'

python3 -c 'import sys; print("Python %s.%s" % sys.version_info[:2]); raise SystemExit(sys.version_info < (3, 11))'
if [ -e "$PROJECT_DIR" ] || [ -L "$PROJECT_DIR" ]; then
  printf 'PROJECT_DIR must be a new directory: %s\n' "$PROJECT_DIR" >&2
  exit 1
fi

case "$EXPECTED_COMMIT" in
  *[!0-9a-f]*|'')
    printf 'EXPECTED_COMMIT must be a full lowercase hexadecimal commit SHA\n' >&2
    exit 1
    ;;
esac
if [ "${#EXPECTED_COMMIT}" -ne 40 ]; then
  printf 'EXPECTED_COMMIT must contain all 40 characters of the commit SHA\n' >&2
  exit 1
fi

case "$SOURCE_MODE" in
  release)
    SOURCE_REMOTE="$WORKFLOW_REPOSITORY"
    SOURCE_REF="refs/tags/$RELEASE_TAG"
    FETCH_REF="$SOURCE_REF:$SOURCE_REF"
    ;;
  candidate-branch)
    SOURCE_REMOTE="$WORKFLOW_REPOSITORY"
    SOURCE_REF="refs/remotes/origin/$CANDIDATE_BRANCH"
    FETCH_REF="refs/heads/$CANDIDATE_BRANCH:$SOURCE_REF"
    ;;
  local)
    SOURCE_REMOTE=$(git -C "$SOURCE_REPO" rev-parse --show-toplevel)
    test -z "$(git -C "$SOURCE_REPO" status --porcelain)"
    test "$(git -C "$SOURCE_REPO" rev-parse HEAD)" = "$EXPECTED_COMMIT"
    test "$(git -C "$SOURCE_REPO" rev-parse --verify "refs/heads/$CANDIDATE_BRANCH^{commit}")" = "$EXPECTED_COMMIT"
    SOURCE_REF="refs/remotes/origin/$CANDIDATE_BRANCH"
    FETCH_REF="refs/heads/$CANDIDATE_BRANCH:$SOURCE_REF"
    ;;
  *)
    printf 'SOURCE_MODE must be release, candidate-branch, or local\n' >&2
    exit 2
    ;;
esac

git init -- "$PROJECT_DIR"
git -C "$PROJECT_DIR" remote add origin "$SOURCE_REMOTE"
git -C "$PROJECT_DIR" fetch --no-tags origin "$FETCH_REF"

CANDIDATE_COMMIT=$(git -C "$PROJECT_DIR" rev-parse --verify "$SOURCE_REF^{commit}")
test "$CANDIDATE_COMMIT" = "$EXPECTED_COMMIT"
for NATIVE_FILE in AGENTS.md .workflow/project.json scripts/init_project.py scripts/check_docs.py scripts/create_document.py '項目文件/00-協作與執行/README.md'; do
  git -C "$PROJECT_DIR" cat-file -e "$CANDIDATE_COMMIT:$NATIVE_FILE"
done
git -C "$PROJECT_DIR" show "$CANDIDATE_COMMIT:.workflow/project.json"

git -C "$PROJECT_DIR" checkout --detach "$CANDIDATE_COMMIT"
test "$(git -C "$PROJECT_DIR" rev-parse HEAD)" = "$EXPECTED_COMMIT"
git -C "$PROJECT_DIR" switch -c "$WORK_BRANCH"
git -C "$PROJECT_DIR" remote rename origin workflow-upstream
git -C "$PROJECT_DIR" remote set-url workflow-upstream "$WORKFLOW_REPOSITORY"
git -C "$PROJECT_DIR" config --local push.default nothing
git -C "$PROJECT_DIR" remote -v
git -C "$PROJECT_DIR" rev-parse HEAD

(
  cd -- "$PROJECT_DIR"
  python3 -B scripts/init_project.py --project-name "$PROJECT_NAME"
  python3 -B scripts/check_docs.py
  python3 -B scripts/check_docs.py --project-docs
)
)
~~~

Release 模式只 fetch 精確 tag ref，並核 peeled commit；若同名 branch 存在也不會被解析為 tag。候選 branch 模式只 fetch 指定 branch ref，本地模式先核來源乾淨、HEAD 及 branch tip 均等於預期 SHA。三種來源接著共用 native file 核對、detached checkout、新工作 branch、`workflow-upstream` 設定及初始化／文件檢查。每一步都以前一步成功為前提；失敗時停止並查明原因。初始化只在新 clone 建立缺少的項目入口，不覆寫現有內容。遇到拒絕或 partial result，保留原內容並依工程入口的 recovery 指引處理；不要用 force、reset 或 clean 繞過。

初始化建立三份 draft：產品骨架、近期模組／功能規格、技術設計與契約。它不確認產品需求，也不代表項目已準備完成。先與開發者確認全局目標、價值、scope、使用者群組、主要流程、品質限制與重要架構方向，再深化近期工作的 owner 文件。

八種模板中有三份作為初始化 draft；另外五種依工作需要建立。五種 template ID 為 business-flow、decision、task、verification、delivery。上段命令在 subshell 內完成，離開後會回到原目錄；執行下例前，將 PROJECT_DIR 填成剛建立的 clone 目錄：

~~~sh
(
  set -eu
  PROJECT_DIR='PATH_TO_NEW_PROJECT'
  git -C "$PROJECT_DIR" rev-parse --show-toplevel >/dev/null
  cd -- "$PROJECT_DIR"
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

## License

編纂與授權者：[Alex0158](https://github.com/Alex0158)。

本 repository 的文字、圖表、文件模板及其他方法論模板沿用 [Creative Commons Attribution 4.0 International](LICENSE)。新工具程式的 scripts/**、tests/** 及 .github/workflows/** 依 [MIT License](LICENSE-CODE) 授權。兩種授權的範圍不同；不要把一種授權推定為另一種的替代。

底座 license 不替採用者決定新產品的原創內容或程式碼授權。各項目 owner 應按自己的權利與產品需要選擇 license，並核實其相依內容和來源。

## 延伸參考與舊文件身份

README、AGENTS.md、項目文件來源目錄及 00 工作路由是採用與工作入口。docs/、templates/、examples/、explorations/ 和 integrations/ 中保留的舊方法論文章、舊模板、案例、探索及 Codex adapter 供按需參考；它們不另行裁決目前工作規則，也不構成平行的採用流程。若參考內容和目前入口衝突，依本 repository 的 GOVERNANCE.md 所列 owner 路由核實。
