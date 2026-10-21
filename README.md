# Evidence-Gated Agentic Workflow

這個 repository 提供一套供新軟件與網頁項目採用的文件及協作 starter：通用工作入口、來源路由、三類協作標準、六份 Runbook、八種文件模板，以及只處理本地 Markdown 的工具。它提供工作方法和可填骨架；產品規則、技術棧、服務、runner 與驗收由各項目的 owner 決定。

目前整合版本是本地候選 0.3.0-rc.1，尚未發布，沒有對應的公開 GitHub tag 或 Release。不要從公開 repository URL 假設可取得這個候選版。下文先提供從採用者填入的本地 repository 與候選 commit 開始的路徑；公開 tag 的取得方式只在發布後適用。

Evidence-Gated Agentic Workflow 是本 repository 自定義的描述性名稱，不是正式標準、安全認證或 formal assurance case；目前亦沒有以 benchmark 證明其 operational effectiveness。

## 先從哪裡開始

- 人類或新 session：本 README 是唯一的底座採用入口。
- Agent 工作邊界：[AGENTS.md](AGENTS.md)。
- 產品、業務、技術、決策及工作內容的來源：[項目文件來源目錄](項目文件/README.md)。
- 選擇本次工作的程序：[00 工作路由](項目文件/00-協作與執行/README.md)。
- Repo、工具、命令、環境及 runner：[項目工程入口](項目文件/00-協作與執行/項目工程入口.md)。

六份 Runbook 和八種模板由上述路由及工程入口定位。舊方法文章、案例、探索及 Codex adapter 保留為參考，採用者不需要先讀完整個 repository。

## 版本與來源身份

- 公開上游 repository 的身份網址是 [Alex0158/evidence-gated-agentic-workflow](https://github.com/Alex0158/evidence-gated-agentic-workflow)。這個網址標識上游，不代表目前未發布的本地候選已在 GitHub 上。
- 本地候選版號為 0.3.0-rc.1；其 Git commit 必須由採用者從本地來源讀取並核對。候選尚無公開 tag、Release receipt 或 GitHub Actions matrix 結果。
- 設計基線仍記為 v1.0-rev15。項目 metadata 的 source digest 用來識別設計來源，不是整個底座、下載包或公開 release 的 checksum。
- 發布後，公開版本身份由實際 tag、該 tag 指向的 Git commit 及 CHANGELOG 共同確定。只改版號或有一個本地 commit，不表示已發布。

## 從本地候選採用

Git 只能 clone 已存在於來源 repository 的 commit。採用前，請確認本地來源包含候選檔案、工作樹乾淨，並提供要採用的實際 commit SHA。若候選內容仍是未提交的工作樹變更，以下核對會停止；不可將來源的舊 HEAD 當作候選。

初始化前先讀[項目工程入口](項目文件/00-協作與執行/項目工程入口.md)的 filesystem 前提，包括 exclusive maintenance、hard link 支援及 symlink／越界保護；環境不符合時停止並保留資料。

先把每個值替換成自己的內容；保留引號。SOURCE_REPO 是採用者填入的本地 repository 路徑，不需要使用作者的個人絕對路徑。PROJECT_DIR 必須是尚未存在的新目錄。整段命令在可建立該目錄的父目錄執行，命令置於 subshell，離開後不會更改呼叫者 shell 的目錄或選項：

~~~sh
(
set -eu

SOURCE_REPO='LOCAL_REPOSITORY_PATH'
SOURCE_COMMIT='CANDIDATE_COMMIT_SHA'
PROJECT_DIR='new-project'
WORK_BRANCH='adopt/workflow-starter'
PROJECT_NAME='My Project'
WORKFLOW_UPSTREAM_URL='https://github.com/Alex0158/evidence-gated-agentic-workflow.git'

test -z "$(git -C "$SOURCE_REPO" status --porcelain)"
SOURCE_COMMIT=$(git -C "$SOURCE_REPO" rev-parse "$SOURCE_COMMIT^{commit}")
test "$(git -C "$SOURCE_REPO" rev-parse HEAD)" = "$SOURCE_COMMIT"
git -C "$SOURCE_REPO" cat-file -e "$SOURCE_COMMIT^{commit}"
git -C "$SOURCE_REPO" cat-file -e "$SOURCE_COMMIT:AGENTS.md"
git -C "$SOURCE_REPO" cat-file -e "$SOURCE_COMMIT:scripts/init_project.py"
git -C "$SOURCE_REPO" cat-file -e "$SOURCE_COMMIT:項目文件/00-協作與執行/README.md"
git -C "$SOURCE_REPO" show "$SOURCE_COMMIT:.workflow/project.json"

git clone --origin origin --no-checkout "$SOURCE_REPO" "$PROJECT_DIR"
git -C "$PROJECT_DIR" checkout --detach "$SOURCE_COMMIT"
CLONE_COMMIT=$(git -C "$PROJECT_DIR" rev-parse HEAD)
test "$CLONE_COMMIT" = "$SOURCE_COMMIT"
git -C "$PROJECT_DIR" switch -c "$WORK_BRANCH"

git -C "$PROJECT_DIR" remote rename origin workflow-upstream
git -C "$PROJECT_DIR" remote set-url workflow-upstream "$WORKFLOW_UPSTREAM_URL"
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

每一步都以前一步成功為前提；失敗時停止並查明原因。初始化只在新 clone 建立缺少的項目入口，不覆寫現有內容。遇到拒絕或 partial result，保留原內容並依工程入口的 recovery 指引處理；不要用 force、reset 或 clean 繞過。

初始化建立三份 draft：產品骨架、近期模組／功能規格、技術設計與契約。它不確認產品需求，也不代表項目已準備完成。先與開發者確認全局目標、價值、scope、使用者群組、主要流程、品質限制與重要架構方向，再深化近期工作的 owner 文件。

八種模板中有三份作為初始化 draft；另外五種依工作需要建立。五種 template ID 為 business-flow、decision、task、verification、delivery。第一段命令在 subshell 內完成，離開後會回到原目錄；執行下例前，將 PROJECT_DIR 填成剛建立的 clone 目錄：

~~~sh
PROJECT_DIR='PATH_TO_NEW_PROJECT'
(
  set -eu
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

修訂 15 的本機基線曾在 macOS／Python 3.14.2 驗證。這不等於整合後候選已通過同一檢查。0.3.0-rc.1 的 GitHub Actions 矩陣尚未執行；目前不宣稱 Linux、Python 3.11 或其他環境已通過。GitHub workflow 是底座維護用檢查；若在下游 repository 被條件略過，skipped 不是測試成功，也不證明下游文件或產品通過。

若要聲稱整個 repository 的 Markdown links／anchors 已核對，發布前仍須做一次涵蓋全庫 tracked Markdown 的完整 QA。scripts/check_docs.py 及其 --project-docs 模式都不是這項全庫檢查，不可用它們取代。

候選工具要求 Python 3.11+。實際環境支援聲明只涵蓋已完成並記錄的檢查組合；未跑的組合標為 NOT_RUN。文件檢查與 framework tests 也不代替項目自身的 build、tests、runtime、deployment、安全審查或產品 acceptance。

## 後續採用底座升級

1. 先讀項目目前記錄的採用版本，再選定要比較的上游版本或 commit。
2. 對照候選改動，按產品、業務、技術和工作標準的 owner 決定哪些適用。
3. 逐項採納並核相容性及受影響檢查；不要 pull／merge 整個上游，也不要自動覆寫產品文件、active instance 或項目本地調整。
4. 只在確實採納並驗證 framework 變更後，更新項目記錄的版本。該次選擇與結果留在既有 Task、DEC、VR 或 PR，不另建長期 upgrade ledger。

GitHub tag 路徑只在版本已實際發布後適用。發布前不要使用尚不存在的 v0.3.0-rc.1 tag；公開 release 完成後，採用者才可由對應公開 tag clone，並將 checkout 的 commit 與該版本的 release receipt 核對：

~~~sh
git clone --origin origin --branch 'v0.3.0-rc.1' --single-branch \
  'https://github.com/Alex0158/evidence-gated-agentic-workflow.git' \
  'new-project'
git -C 'new-project' rev-parse HEAD
~~~

## License

編纂與授權者：[Alex0158](https://github.com/Alex0158)。

本 repository 的文字、圖表、文件模板及其他方法論模板沿用 [Creative Commons Attribution 4.0 International](LICENSE)。新工具程式的 scripts/**、tests/** 及 .github/workflows/** 依 [MIT License](LICENSE-CODE) 授權。兩種授權的範圍不同；不要把一種授權推定為另一種的替代。

底座 license 不替採用者決定新產品的原創內容或程式碼授權。各項目 owner 應按自己的權利與產品需要選擇 license，並核實其相依內容和來源。

## 延伸參考與舊文件身份

README、AGENTS.md、項目文件來源目錄及 00 工作路由是採用與工作入口。docs/、templates/、examples/、explorations/ 和 integrations/ 中保留的舊方法論文章、舊模板、案例、探索及 Codex adapter 供按需參考；它們不另行裁決目前工作規則，也不構成平行的採用流程。若參考內容和目前入口衝突，依本 repository 的 GOVERNANCE.md 所列 owner 路由核實。
