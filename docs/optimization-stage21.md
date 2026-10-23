# 最適化・旧処理撤去 実装報告（dev.21）

対象: インストール済みStellaris Cygnus 4.5.2 (9776)。版: 1.39.0-dev.21。2026-10-23。

ユーザー指示により古いsaveの移行を終了した。新規ゲーム向けの更新であり、旧版saveの掃除・互換移行は提供しない。実機未検証。

## 実装内容

|対象|変更|維持する仕様|
|---|---|---|
|旧対外デバフ|旧63補正と旧支援5補正を定義・表示名ごと撤去。旧flag・カウンタ掃除、移行flag、移行通知イベント.30を撤去|現行v2の7系統と支援効果|
|対外圧力|集計値と適用済み値を分離。値の変化・補正欠落時だけ付け直す。0なら残留補正だけ削除|複数国からの同一効果は加算、独自上限なし。免疫・正式/仮想宿敵の条件|
|支援省|宿敵数を0～5に集計し、変化時だけ影響力補正更新|正式宿敵数による元の最大5の支援|
|仮想宿敵メニュー|追加/解除16選択肢から、選んだ受け手だけを直接再計算|選択時の接触・資格・関係flag再確認|
|罰金制度|犯罪値を切り上げて0～50に制限。段階不変ならdepositを操作しない。変化時だけ更新|50段階の既存効果、犯罪0では効果なし、国是無効・所有者変更時の解除|
|逆境|防衛戦争への現在の参加状況で補正を同期。開始、終了、取得、月次に接続|防衛戦争中だけ亜高速移動補正。複数戦争の片方だけ終わっても維持|
|月次惑星巡回|経済・倫理職・国是職・民兵・戦争経済・繁栄の6巡回を共通化。戦争/繁栄の国家状態を先に更新|植民・所有者変更・戦争等の即時経路と独立effect API|
|リーダー巡回|若年/長老の特性と年齢、徒弟、狂気を共通入口から一回の所有者/候補巡回で処理|原版の所有/候補への適用範囲、年齢の初回設定、永続的な贈与特性|
|根本的狂気|既存maniacal初段を2段へ一度だけ昇格。未所持なら初段、既存2/3段は維持|原版のelse-ifによる分岐。月次ごとの無限昇格なし|
|国是職業|50組合せを共通データからdepositと減算script valueへ生成。上限のmin/max逆転を修正|複数国是の独自職業は加算、政治家減少はVanilla容量まで|
|前衛メニュー|55イベントをデータと生成スクリプトへ分離。既存ID・条件・選択結果を構文木で照合|今回伝統本体は有効化せず、復旧範囲を拡大しない|
|職業適性|儀典局・庭師は行政官、潮力技師は技術者、水産技師は農民、独自提督は兵士の現行weightを基準に調整|出力・維持費・就業可能条件はdev.20と同一。専門職の基本weightは専門職を維持|

罰金の高速経路は保持した段階と実depositが一致する通常状態を前提とする。他MODやコンソールでdepositだけを書き換えた場合の自動修復は今回の対象外。犯罪値や国是の状態が変われば通常の更新で再同期する。

## Vanillaの上書き整理

`common/policies/00_policies.txt` は4.5.2実定義を基準に再構成し、NGM条件が必要な7政策だけを上書きする。独自の研究政策・roboticist_outputは維持する。

上書きを残す定義: `war_philosophy`、`orbital_bombardment`、`first_contact_protocol`、`artificial_intelligence_policy`、`robot_pop_policy`、`refugees`、`slavery`。

それ以外の21政策はゲーム本体の現行定義を使う。例として、交易外交姿勢は現行Vanillaの国家交易+10%・外部リーダー候補+1に戻る。dev.20の職業交易+10%・国家交易+5%とは値と対象が異なる。これは旧定義を温存せず現行政策へ追従する変更である。NGM機械信仰等のAI権利例外、寛容国是の難民条件、追加倫理の奴隷制条件は保持する。終末爆撃はNGM国是だけでなく、現行Vanillaが認める浄化帝国等でも選べる条件を保持する。

`common/pop_faction_types/00_traditionalist.txt` は4.5.2の全定義を使い、機械信仰による二つの要求免除だけを追加。個別機械帝国等の現行条件を失わない。

`common/economic_categories/NGM_categories.txt` から `country_ruler` と `megastructures` の旧上書きを撤去し、Vanillaに任せる。同内容の独自カテゴリ重複も統合する。現在のmegastructuresが生成するupkeep補正を旧定義で失わない。

競合: 上記7政策とtraditionalistは依然として同名Vanilla定義の上書きなので、同じ定義を編集するMODと競合しうる。既存の倫理作成GUIや他の上書きは今回そのまま。新規Vanilla定義の上書きは増やしていない。

## 実装の根拠と判断

- 犯罪値の数値参照はVanilla `common/script_values/07_script_values_shroud.txt` の `trigger:planet_crime`。切り上げと制限は `00_script_values.txt` にある `ceiling`、`max`、`min`。
- `max` は上限、`min` は下限。従来の政治家減算に用いた `min = 200` 等は下限だったため、`max` に修正した。容量200/300/400/200/600は現行首都の職業付与と対応する。
- 戦争終了hookのRootは敗者、Fromは主勝者。その一国だけでは同盟参加国を網羅できないため、終了時はplayable countryを一度走査して逆境の状態だけを同期する。惑星巡回はしない。月次修復も残す。
- 伝統/AP取得hookの文書上のscopeはcountryのみ。取得IDを推測してフィルターしないため、ここは全体圧力再計算を維持する。確実に相手が分かる仮想宿敵変更だけ対象を限定した。
- 外部雇用者やパラゴンを年齢変更から除外する変更は、原版の適用対象を狭めるため採用していない。年齢の初回flag・贈与特性の永続性を保ったまま経路を統合した。
- 国是併用は加算のままとし、新たな排他条件を追加しない。
- 倫理や評議員の条件は異なるscope・AI倍率を含むため、一律の共通triggerへ置換しない。今回の具体的な反復削減は惑星/リーダー入口と職業/メニューの生成元に限定する。

## 変更ファイル

中心となる実装:

- `common/scripted_effects/NGM_pressure_v2_effects.txt`、`NGM_pressure_v2_support.txt`、`NGM_pressure_v2_migration.txt`（現在は移行なしの全体dispatcherのみ）。
- `NGM_civic_economy_effects.txt`、`NGM_adversity_effects.txt`、`NGM_monthly_sync_effects.txt`、`NGM_leader_sync_effects.txt`、戦争経済・繁栄・残り国是effect。
- `common/script_values/NGM_optimization_values.txt`、`NGM_civic_ruler_values.txt`、`common/deposits/NGM_civic_ruler_jobs.txt`。
- `events/NGM_monthly_sync_events.txt`、`NGM_civic_event.txt`、`NGM_tradition_event.txt`、`NGM_pressure_v2_selection.txt`、`NGM_avantgarde_menu_generated.txt`。
- 関連on_actions、旧modifierと多言語表示名、政策・派閥・経済カテゴリ・職業、descriptor/Launcher/README。
- `tools/generate_catalogs.py`、`tools/data/ruler-jobs.json`、`tools/data/avantgarde-menu.json`。

生成方法: `python tools/generate_catalogs.py --root .`。原版やVanillaがなくても、このリポジトリだけから3配布ファイルを再生成できる。

## 検証

- 配布構造: 127 script/UIファイル、136 event ID、parser・直接event参照・localization BOMの検査合格。
- 現行圧力コア20シナリオ合格。40発信国、繰り返し同期、免疫、国の消滅、正式/仮想宿敵等。
- UI・支援55チェック合格。追加/解除時に選択した相手だけが再計算される経路も確認。
- 第21段階209チェック合格。犯罪境界、国是無効化・譲渡、複数戦争、特性一度限り昇格、補正の変更時更新/欠落修復、旧68定義の参照撤去、生成の再現、55メニューの意味保持、政策選択肢、派閥現行定義、職業の出力/資格、種族特性の不変を確認。
- engine modifier照合で未知補正候補0。直接呼出の未定義イベント0。友人版の922参照ファイルは変更なし。
- 第19段階の「当時の政策・static定義から変更しない」履歴検査は、今回の意図した旧定義撤去で不成立になる。これを今回の合格件数に含めない。代わりに現行政策/派閥の照合と、dev.20 ZIPとの種族特性・職業出力比較を行った。

いずれも静的検査または限定的な構文評価器による検証であり、Stellaris実機検証ではない。実際のhook発火順、旧save読込、長期AI、職業配置、月次時間短縮率は未確認。

## Save compatibilityと次の確認

旧NGM版からの移行・掃除はユーザー指示により提供しない。新規ゲームで検証する。イベントIDの大半は維持するが、旧補正・通知イベントの削除があるため、既存saveに安全と案内しない。

次に行うべき確認は実機での新規ゲーム起動、error.logの最初のエラー、罰金の犯罪境界、複数戦争、国是改革、職業配置と生産、外交による圧力変化。その後に同じ銀河・日付・国数・惑星数で処理時間を比較する。

前衛/記憶など未復旧の伝統や他の未移植機能は、この最適化で復旧済みにはならない。前衛メニューには原版由来の未復旧国是参照が残り、伝統本体が無いため通常取得経路から有効化していない。別MOD化した技術取引・艦隊贈与は対象外。
