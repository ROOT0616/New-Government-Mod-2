# Stellaris 4.5.2向け復旧作業：1.39.0-dev.16

2026-10-23。原版の基準はコミットd54857bc6909c6695d791b6605234873adac8667。復旧用ブランチで更新し、masterへのマージはまだ行わない。全機能対応・実機検証は未完了。

## 今回の変更

- 古い政体ファイル8定義の一括上書きを廃止。独自条件があるauth_imperial/auth_corporateだけを現行Vanilla定義から拡張し、原版の追加倫理の排他条件7件を保持した。その他6政体は本体から提供される。
- 現行の色、制限、上位政体への移行処理を保持。旧機械政体に残っていた廃止済みの開始人口補正等は現行本体の処理へ戻る。
- 旧governor/general/admiral/scientistノードの経験値19か所を、成長/規制/軍団/認識ノードへ対応付け。効果値を維持。
- 起源「植民熱」を復旧。旧開始POP+1を植民完了時の100人口へ変換し、実際の植民者POPグループを複製する。首都は対象外。反復通知・領有移管・ロードでは再付与せず、植民地破壊時にフラグを消して再入植を許可する。
- ゲーム本体不要の構造検査をtools/check_mod.pyとして公開する。ローカル固有の絶対パス・本体資料・Workshop参照の実ファイルは公開対象に含めない。

## 変更ファイルと競合

追加：common/governments/authorities/NGM_authority_ethic_rules.txt、common/governments/civics/NGM_colonial_origin.txt、events/NGM_colonial_origin_events.txt、common/on_actions/NGM_colonial_origin_on_actions.txt。

変更：common/governments/civics/NGM_civics.txt、descriptor.mod、README.md、CHANGELOG.md、Launcher用.mod。旧common/governments/authorities/00_authorities.txtは開発版から除去し、変更前をローカルに保存。

Vanilla定義の上書きはauth_imperialとauth_corporateに縮小した。これら2政体を変更するMODとは競合する。他の既存上書きは引き続き監査中。新しい起源・イベント・on_actionは独自定義。replace_pathは使わない。

## 検証

対象本体はローカルCygnus v4.5.2 (9776)。Vanilla実ファイルと4.5.2が出力したscript_documentationを根拠とする。108スクリプト/UIの構造検査、129イベントIDの重複/入口参照、UTF-8 BOMを検査。政体から追加倫理の条件だけを取り除けば現行Vanillaと完全一致すること、経験値の数値保持、植民人口の反復・再入植を確認する。既存の回帰検査も継続。

実機の政体改革画面、上位政体移行、新規植民、植民船種族の権利・倫理、AI、セーブ/ロードは未確認。静的検査の成功を実機動作確認とは扱わない。

## セーブと残件

新規ゲームでの検証を推奨。植民ボーナスは有効化後の新規植民のみで、過去の植民地には遡及付与しない。国是/起源/種族/経済を変更する開発版全体として既存セーブの安全性は未保証。

原版で有効だった国是イベント23件、停止国是19件（前段階分を含む）、起源7件、地上軍4種、追加評議会方針6件、伝統3系統21定義等を復旧済み。旧交易路保護・人口移動等の補正候補84か所、複雑な起源/艦船/建造物/連邦/取引/伝統の移植が残る。詳細はcompatibility-audit.jsonに記録する。

## GitHubでの検査と検証用配置

リポジトリを取得後、Python 3で以下を実行できる。

```text
python tools/check_mod.py --root .
```

検証用に配置する場合は、Stellarisユーザーフォルダのmod/New-Government-Mod-2へリポジトリを置き、NewGovernmentMod2_Development.modをmod直下へコピーする。原版/友人版と同時に有効化しない。通常プレイ用リリースではなく、別プレイセット・新規ゲームの検証用である。

未移植の原版コードはmasterおよび基準コミットに残る。開発版では未移植スクリプトを自動的に読み込まない構成にする。GitHub更新は完成版の公開やWorkshop更新を意味しない。
