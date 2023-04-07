# __<font color="Lime">    設定  </font>__
CWTools - Paradox Language Servicesの設定方法  
ユーザー設定	→	設定	→	ユーザー  
拡張機能	→	CWTools configuration  
Cwtools › Cache: Stellaris	にステラリス本体を  
例C:\Program Files (x86)\Steam\steamapps\common\Stellaris  

ユーザー設定	→	設定	→	ワークスペース  
拡張機能	→	CWTools configuration  
Cwtools › Cwtools: Rules_folder	にModフォルダにある.cwtoolsの絶対パスを  
例I:\Prg\Stellaris\Additional Districts\.cwtools  

これしたのちにvscordを再起すると補助機能が使える  

# __<font color="Lime">    ToDo  </font>__
それぞれにテンプレート置いといた
アセンション
common\ascension_perks\NGM_ascension_perks.txt
伝統のカテゴリ
common\tradition_categories\NGM_tradition_categories.txt
伝統
common\traditions\NGM_traditions.txt
名前設定
localisation\NGM_l_english.yml

伝統等でアンロックされる政策
1.労働法(労働者の権利や自由を規定し、企業活動に影響を与える)
  ①企業規制	(労働者幸福度+10%)				(労働者は国民で、国民の権利は保証されるべきだ)
  ②労働者優先	(労働者幸福度+5%)				(労働者の過度な搾取は国家を損ねている)
  〇③一般規制							(過度な規制や緩和は社会の不安定を招く)
  ④企業優先	(労働者生産量+5%)				(労働者利益よりも企業利益こそが国家への利益へ直結する)
  ⑤規制緩和	(労働者生産量+10%、無職の召使Jobをアンロック)	(労働に値しない者は、値する者に仕えることで社会を回転させる)

2.学術政策(国家の研究に関しての方針を規定する)
  ①政府主導  (研究選択肢+5)		(政府が研究の優先度を決定する)
  〇②国家後援  			(国家による研究優遇は常識の範囲に収まる)
  ③民間主導  (研究速度+10%)		(政府よりも民間研究機関が国家の研究を担う)

3.介入政策(他国に対する介入方針を決定する)
  ①公然としの介入(外交発言力+20%)(相手に対する介入は公然と行うことが公正だ)
  〇②介入の手控え(暗号力+5)	(介入を控え、自分の行動を見直すべきだ。内政不干渉である)
  ③秘匿した介入  (解読力+10)	(表にできないような介入を隠れて行っていく)

4.諜報政策(情報こそすべてを制する)
  ①対外注力	(解読力+10)	(相手の情報を得ることこそが自国を守る)
  〇②バランス	(情報基礎値+5)	(攻めるも守るも優劣はつけがたい)
  ③防諜注力	(暗号力+10)	(相手に情報を隠すことこそが自国を守る)

5.ロボット職権(ロボットに与えられる権限や職域の方針を決定する)
  ①自由意志	(ロボット維持費-10%)	(ロボットの職権や職域は、ロボット自身の希望と成果を基準に決められる)
  ②上司指導	(ロボット製造速度+10%)	(ロボットの職権や職域は、上司が決定を行う)
  ③適正優先	(ロボット生産量+10%)	(ロボットの職権や職域は、ロボット自身の適正が重視される)


# __<font color="Lime">    完成  </font>__
## __☆ 起源__
### __〇 「律儀な古代の緩衝国家」__
この国が位置する星系はその豊かな立地ゆえに古代においても戦略重要地として奪い合いの戦争が繰り広げられていました。
古代の国家はこの星系に極々小さな独立緩衝国を築き上げ、統治させることで戦争の危機を脱しました。そうして出来上がった国家は貿易的利益と強力な国際発言力の代償に小さな国土と限られた原料生産を強いられている。
古代の国家群が滅びた後でも、この国はその伝統を数少ない継承要素として維持しているのである。

1. 平和主義のみ取得可能。
2. 非常に豊かなチョークポイントに位置する星系に生成される。
3. 開始時に遺物『古代の盟約』を取得する。
4. 拡張に関して極めて大きな制約を課せられる。
5. 市場手数料-10%、Pop成長率+100%、
6. 特殊な種族特性を取得する。

初期建築物「永久の宮殿」（古代から続くこの地を治める者のための宮殿で、列強の君主や元首が集い交渉を行うことも多かったためか、壮麗な建築でいまだに陰りを見せていない。現在も支配者の宮殿や国際会議場としてだけではなく、政府機関や上流階級の住居として使用されている。）

維持費：エネルギー5。住居+10、快適度+10、貴族Job+1、政治家+1、紋章官+1、高級参謀+1、事務員+10、建築物Slot+10、  

遺物「古代の盟約」（古代の列強間の協定で、緊急時に強力な自衛力を求められたうえで、平時には他国の脅威にならない経済国家であることを求められる条文。所有国は永久にこれを守らなくてはならない。）  

パッシブ効果	：請求権作成コスト+9999%、開拓前哨地建造コスト+9999%、外交発言力+100%。統合力+30%、交易価値+100%、  
アクティブ効果	：船体値+100%、宇宙軍許容量+500%、造船速度+500%(10年間。起動コスト影響力200)  

種族特性「古代からの商人」（はるか太古から頭脳労働者として活躍してきたため、創造やデスクワークに適性がある種族。人口過少の防止として太古に繁殖力の増強が図られている。）  
交易価値+30%、住居使用量-30%、Pop成長率+20%。鉱山労働者の生産量-50%、消費財消費量+10%。途中削除、追加不可。強制取得。  

開始時、20年の間Pop成長速度+200%、Pop製造速度+200%、流入魅力+100%の惑星特性（国家再興の決意）を付与  


### __〇 「過去への逃走」__

この国の種族は苛烈な運命をたどる時代から逃げ去り、未来を変えるために再度過去へと戻った。  
しかし、その運命から抗う手法は追跡者を生み、定期的な襲撃を受けることとなる。  

研究力+10%、艦隊連射レート+5%  
120か月に1度未来からの艦隊が襲撃する。打ち勝つことによって技術のデブリを取得することが可能となる。  

首都惑星に特殊な特性「時空超越機」（時間を超えることができる機械で、惑星と一体化している。原理は失われているため再現は不可能であるが、時折亡命者がこの時代に流れ込んでいる。）  
物理学研究+20%、Pop成長速度+10%  


## __☆ 決議__
| 決議 | Main categories | Sub Categories | Cost | Effect  |
|:------:|:------|:------|------:|------:|
| 銀河規模の拡大 | Environment and Technology | 銀河規模の拡大 | 100 | Pop成長率+1000%、Pop製造速度+1000%。Pop消費財+50% |
| 銀河規模の拡大の廃止 | Environment and Technology | 銀河規模の拡大 | 100 | 銀河規模の拡大の廃止 |

## __☆ イベント__
### __〇 リーダーイベント__

<!-- 1.政治論争
(派閥名)を支持する(10年の間当該派閥の幸福度+10、派閥の影響力+10。当該派閥リーダーに「政府後見」の特性を付与)  
政府は臨機応変に対応する。(影響力100獲得。)   -->

| イベント | option 1 | option 2 | option 3 | Effect |
|:------:|------:|------:|------:|------:|
| 学術論争 | リーダーに一人に「政府後見」の特性を付与。各研究力100を獲得 | 研究力各500獲得 |  |  |
| 軍事論争 | 提督に一人に「政府後見」の特性を付与 | 将軍に一人に「政府後見」の特性を付与 | 影響力+100 |  |
<!-- |  |  |  |  |  | -->

| 政府後見 | Effect 1 | Effect 2 | Effect 3 |
|:------:|------:|------:|------:|
| 総督 | リーダー経験値取得+20% | 職からの統合力+10% | 職からの管理許容量+10% |
| 研究者 | リーダー経験値取得+20% | 調査速度+10% | 研究速度+5% |
| 提督 | リーダー経験値取得+20% | 艦隊維持費-10% | 亜空間移動速度+10% |
| 将軍 | リーダー経験値取得+20% | 地上軍維持費-10% | 地上軍士気+20% |

## __☆ 志向__
### __〇 社会主義__：
労働者幸福度+5%、布告「5か年計画」を宣言可能。（企業選択不可）  狂：労働者幸福度+10%、統治者幸福度-5%、布告「5か年計画」を宣言可能。（企業選択不可）	

社会主義  
狂信社会主義  

#### 布告「5か年計画」  布告できるのはいずれか1つ。布告コスト  影響力：20、エネルギー500  影響力布告期間は5年。クールタイムは10年
* 建築5か年計画  ：建造物コスト-5%、建造物建築速度+10%、区域建造速度+5%	  Pop消費財使用量+5%
* 重工業5か年計画：合金生産量+10%、造船速度5%		居住性-5%、農業生産量-10%
* 農業5か年計画  ：農業生産量+20%、Pop成長速度+5%	研究力-5%
* 研究5か年計画  ：工学+10%、巨大構造物建造速度+5%	物理学-5%、社会学-5%
* 思想5か年計画  ：社会主義魅力+20%、統合力+10%		安定度-5

### __〇 資本主義__：
統治者幸福度+5%、交易価値+10%	狂：統治者幸福度+10%、交易価値+10%、労働者幸福度-10%（君主制選択不可）  

資本主義  
狂信資本  
### __〇 介入主義__：
使節+1、解読力+2			狂：関係-30、使節+2、解読力+5

介入  
狂信介入
### __〇 中立主義__：
関係+20、暗号力+5	狂：連邦結束度月-5、関係+50、暗号力+10（対外）

中立
狂信中立
### __〇 保全主義__：
居住性＋5%、農業生産量+10%  	狂：居住性+10%、農業生産量+20%、鉱物生産量-10%  

保全
狂信保全
### __〇 開発主義__：
鉱物生産+5%、建築スロット＋2    狂：鉱物生産+10%、建築スロット+2、区域建造速度+10%、居住性-5%

開発
狂信開発
### __〇 栄望主義__：
Pop30あたり貴族職業枠＋1、統治者の幸福度＋10%、開戦自由「名誉にかけて」勝利時影響力＋100  狂：Pop20あたり貴族職業枠＋1、統治者の幸福度＋20%、戦争疲弊-20%、開戦自由「名誉にかけて」勝利時影響力＋100（民主制選択不可）

栄誉
狂信栄誉 
### __〇 実利主義__：
奴隷の使用許可、30Popあたりインフルエンサー職業枠+1、奴隷の購入コスト-10%    狂：奴隷の使用許可、20Popあたりインフルエンサー職業枠+1、奴隷購入コスト-20%、戦時中の艦隊製造速度+10%（民主制、君主制選択不可）

実利
狂信実利
## __☆ 建築物__
| 建物 | authority | cost | upkeep | time | effect |
|:------|:------|:------|:------|:------|:------|
| 儀典局 |  | エネルギ200 鉱石400 |  |  | 式部官x2 |
| 永久の宮殿 |  |  | エネルギー10 消費財5 |  | 住居+5 快適度+5 貴族Job+1 政治家+1 紋章官+1 高級参謀+1 事務員+10 建築物Slot+16 |
| 市街地調整地域 |  | 鉱物300 | エネルギー1 |  | 事務員+2 企業建築物スロット+2 アップグレード 惑星規模産業調整地 |
| 惑星規模産業調整地域 |  | 鉱物500 | エネルギー3 |  | 事務員+4、企業建築物スロット+4 |
| 銀河百貨店 |  |  |  |  | 支社の価値+20% 惑星快適度+5 事務員+3 |
| 企業大学校 |  |  |  |  | 企業国家の研究算出各々+10、研究者+1 |

## __☆ 職業__
* 式武官   統合力10 影響力1 → 勲章0.02
* インフルエンサーJob  統治者  影響力+0.1、社会研究+5、統治志向魅力+5%

## __☆ 国是__
### __〇 ノーマル__
* 円滑な交通			亜光移動速度+10%、交易価値+5%
* 船舶保護プロトコル 回避+20%、緊急FTL時損害-30%、艦船連射レート-10%
* 宙間警備本部 海賊抑止力+5、交易保護値+5、交易価値+5%
* 乱脈的出生率 (ゲーム開始後の追加削除不可)Pop成長率+10%、幸福度-5%、住居使用量+5%
* 貿易国家 	交易価値+10%、市場手数料-5%、犯罪度+5
* 仮想的社会 幸福度+10%、居住性+5%、Pop成長速度-10%
* 健康的習慣 (ゲーム開始後の追加削除不可)リーダー寿命+10年、幸福度+5%
* 文化高権 統合力+10%、リーダー取得経験値+10%

### __〇 政治制度規定__(全て相互に排他的、狂信的な浄化主義、内向きの成熟と排他的)
* 銀河連邦 		(民主制、受容主義) 派閥影響力収入+10%、リーダー経験値取得+20%、リーダースキル上限+1、政治家の一人を社会的英雄に置換え。		
* 環境民主制  (民主制、保全主義) 居住性+5%、Pop成長速度+10%、政治家の一人を大自然監督官に置換え。
* 宗教共和制 		 (民主制、精神主義) 統合力+10%、安定度+5、政治家の一人を大祭司に置換え。
* 人民民主制 			 (民主制、社会主義) Pop幸福度+5%、労働者生産量+5%、政治家の一人を書記に置換え。
* サイバー民主制 			 (民主制、物質主義) 研究力+5%、管理許容量+10%、政治家の一人を科学総裁に置換え。
* 貴族共和制 		(寡頭制、栄望主義) 影響力+0.5、安定度+5、政治家の一人を紋章官に置換え。
* 書記長制 		(寡頭制、社会主義) 安定度+10、消費財生産量+5%、合金生産量+5%、政治家の一人を書記に置換え。
* 戦争卿 		  		 (独裁制、軍国主義) 宿敵の最大数+3、地上軍編成速度-50%、艦隊建造コスト-5%、政治家の一人を高級参謀に置換え。
* 共産独裁制 		 (独裁制、社会主義) 防衛軍耐久度+20%、労働者生産量+5%、政治家の一人を書記に置換え。
* 衆愚扇動制 	 		 (独裁制、実利主義) 安定度+10、政治家の一人を宣撫官に置換え。
* 騎士団 			 (君主制、軍国主義) 艦船連射レート+5%、地上軍士気+20%、政治家の一人を高級参謀に置換え。
* 名誉帝制 			 (君主制、栄望主義) 安定度+10、統合力+10%、リーダースキル上限+2、政治家の一人を紋章官に置換え。

書記  				安定度+5、工学+3、社会主義魅力+10%
宣撫官  				労働者幸福度+5%、労働者生産力+1%、実利主義魅力+10%
紋章官  				統合力+5、惑星統合力+1%、影響力+0.01、栄望主義魅力+10%
高級参謀 			防衛軍+5、宇宙軍許容量+5、安定度+5、軍国主義魅力+10%
社会的英雄  			幸福度+5%、快適度+3、安定度+5
大自然監督官 	統合力+3、社会学+3、居住性+5%、保全主義魅力+10%

### __〇 権威__
* 指導者原理 			(狂権威、ゲーム開始後の追加と削除不可) (カースト制、部族制、徒弟制度と相互排他)	影響力+0.5、統治志向魅力+15%、労働者幸福度+5%、専門家幸福度-5%、安定度-5
* 党支配				(権威、社会主義)(部族制、カースト制、徒弟制度と相互排他)統治志向魅力+10%、布告コスト-10%、労働者生産+5%、安定度-5
* 服従の中の自由 	  	(権威、受容)	安定度+5、移民流入+10%
* カースト制度 		  	(権威、精神)(指導者原理、党支配と相互排他)	市民権がカースト制固定、統治者幸福度+10%、労働者と奴隷Popの生産量+5%、奴隷の割合25%、階級の降下時間+300%
* 部族制 				(権威、排他)（党支配と相互排他）	住居使用量-20%、統治志向への魅力+10%、統合力-5%、研究力-10%
* 宮廷政治 			(権威、栄望)	影響力+0.5、統治者幸福度+5%、統合力+10%、リーダー雇用コスト+30%、研究力-5%
* 社会ダーヴィニズム 		(狂権威)	影響力+0.5、統合力+10%、研究力+5%、Pop成長速度-10%
* 徒弟制度   			(権威、物質) (指導者原理、党支配と相互排他)	専門家出力+5%、リーダースキル上限+2、リーダー選択肢-2、労働者幸福度-5%

### __〇 平等主義__
* 直接民主制  			 						(民主制、平等主義)			影響力+0.5、布告コスト+20%
* 自由主義教育 		 						(平等主義)（実利や排他、軍国ではない）	統合力+10%、専門家生産力+5%
* デモ文化 		 				(平等)(実利、栄望ではない)		影響力+0.5、派閥幸福度+5%、統治志向魅力-5%、安定度-5
* 公開討論会  			 	(平等)(実利ではない)			統合力+10%統治志向魅力-5%、派閥幸福度+5%
* 消費社会  			 									(平等、資本主義)(狂信的社会主義ではない)			幸福度+5%、安定度+5、消費財消費+10%
* 社会福祉  			 						(平等)(実利、狂信的資本主義ではない)	労働者幸福度+5%、労働者生産力+5%、犯罪度-5%、消費財消費量+10%
* 宇宙規模の解放  	 						(平等、軍国)(中立ではない)		艦船連射レート+5%、建艦速度+5%、宇宙軍許容量+10%
* 究極の思想的自由 	 							(狂信的平等)(ゲーム開始後の追加削除不可)				管理許容量+30%、安定度-10、統治志向魅力-30%
* 個人武装権  		 							(平等、軍国)				地上軍ダメージ+30%、地上軍コスト-20%、犯罪発生率+10、犯罪発生率+20%

### __〇 受容主義__
* 共通価値観   					(受容)			統合力+10%、移民流入+5%
* 共に征く 	 	 		(受容)			(防衛戦争時)艦船連射レート+10%、(防衛戦争時)建艦速度+5%、危機に対するダメージ+10%
* グローバル主義 					(受容、資本主義)	交易価値+10%、市場手数料-5%
* 多文化主義 						(受容、平等)		統合力+10%、Pop成長速度+5%
* 庇護主義 				(狂信的受容、介入)	属国の友好度+100、属国の受け入れ値+10、艦船連射レート+5%
* 来るものは拒まず 	 		(受容、中立)			移民流入+10%、難民政策を無制限許容で固定
* 飛び立つ民衆 			(狂信的受容)(中立、来るものは拒まずではない)		流出圧力+10%、Pop成長速度+5%

### __〇 排他主義__	
* 排他的コミュニティ  			(排他、権威)	統合力+5%、安定度+10、交易価値-5%
* 呵責なき正義 			(排他、軍国)（実利ではない）	艦隊連射レート+5%、無制限爆撃以外選択不可、犯罪度-10%、安定度-5、他国友好度-30
* 他者蔑視								(排他)（実利ではない）		影響力+0.5、防衛ステーション防衛力+10%、暗号力+5、交易魅力値-100
* 紳士的距離感				(排他、栄望)（実利ではない）	使節+1、統合力+5%、交易価値+5%
* 痕跡の抹消												(狂排他)	統合力+10%、無制限爆撃以外選択不可、他者痕跡の抹消の開戦事由を取得（総力戦）、異種族を浄化しなくてはならない。		
* 選民思想						(排他、精神)	統合力+10%、安定度+5、精神主義魅力+10%
* 異種族解剖					(排他、物質or実利)	研究力+10%、異種族は強制で奴隷化、他国友好度-100

### __〇 軍国主義__
* 帝国主義					(軍国、受容、中立ではない)	請求権作成コスト-20%、前哨地建造コスト-20%
* 大艦巨砲主義				(軍国)			船体値+10%、艦船連射レート+10%、宇宙軍許容量+30、回避-10%、亜光速* 移動速度-10%
* 軍産複合体 					(軍国、資本主義or実利)	交易保護値+5、20Popあたり兵士+1、兵士が交易価値を1生み出す。
* 戦争経済 		 					(狂信軍国)（中立ではない）		戦争疲弊-20%、戦時中の鉱物、合金、交易価値、消費財生産量+10%、建艦速度+10%。非戦争時の鉱物、合金、交易価値、消費財生産量-20%、建艦速度+20%
* 軍事政権									(軍国)			20popにつき兵士+1、兵士により統合力+1、安定度+5、軍国主義への魅力+10%、軍国以外の派閥幸福度-5%
* 闘争のための闘争 			(狂信軍国)(ゲーム開始後の追加削除不可)		戦争疲弊-20%、戦時中の合金生産量+10%、軍艦建造コスト-5%

### __〇 平和主義__
* イージスの護り	(平和)（介入ではない）		ステーション許容量+5、ステーション防衛+10%、船体値+20%、暗号力+5、艦船連射レート-10%
* 繁栄主義者		(平和、実利)	労働者生産量+5%、交易価値+10%、平和の期間が1年続くごとに労働者生産量+0.2%、交易価値+0.5%（最大50年分）
* 武装平和主義		(平和、開発)	宇宙軍許容量+10、国内での連射レート+15%、船体値+10%
* 積極的平和主義者	(平和、介入)	使節+1、外交発言力+10%、宇宙軍許容量+20、他国友好度-10
* 平和の使者		(狂平和)	安定度+5、亜光速移動速度+10%、危機に対する攻撃力+20%
* 誠実な交渉人		(平和、平等)	使節+1、他国友好度+20

### __〇 精神主義__
* 機械信仰		(精神、開発)(ゲーム開始後の追加削除不可)	精神主義派閥がロボットに怒らなくなる。工学研究+10%、ロボット建造速度+10%、ロボット維持費+5%、ロボットを非合法化できない。ロボットの人権を市民権に固定。
* 伝道者団		(精神、介入)	使節+1、隣国の精神主義魅力+20%、他国友好度-50
* 信仰の擁護者		(精神、軍国)	宇宙軍許容量+20、艦船連射レート+5%、交易価値-5%、影響力+0.2、非精神主義国家友好度-30
* 亀卜（きぼく）	(狂精神)	統合力+20%、幸福度+5%、研究力-10%、精神主義魅力+20%、そのほかの志向魅力-5%
* 文化の大量消費	(精神、実利)	統合力-10%、安定度+5、幸福度+5%

### __〇 物質__
* AIによる補助政治 	(物質)					統治志向魅力+10%、幸福度+5%
* 機械は友達 		(物質、ゲーム開始後削除不可)		ロボット製造速度+10%、ロボット維持費+10%、ロボットの権利を市民権以外に変更不可
* 未来への渇望		(物質、内向きの成熟を取得していない)	調査速度+20%、アノマリー発見率+10%、アノマリー調査速度+10%
* 実験的物質の発見	(物質、開発)				首都惑星の各戦略資源特性を1つずつ付与
* 産業資本主義		(物質、資本主義、開発主義)		鉱物、合金、消費財+10%、エネルギー通貨+15%、労働者Pop幸福度-10%、専門家Pop幸福度-5%
* 実験的実践		(狂信的な物質)				研究力+10%、幸福度-10%
* AI主導政治		(狂信的な物質：ゲーム開始後削除不可)	統治志向魅力+10%、研究力+10%、安定度-10、幸福度+5%

### __〇 社会主義__
* 社会的平等		(社会、平等)	安定度+10、Pop降下時間-50%、労働者政治力+50%、市場手数料+10%
* 分配主義		(社会、精神)	労働者生産量+10%、労働者政治力+100%
* 人民軍		(社会、軍国)	防衛軍士気+20%、防衛軍ダメージ+10%、地上軍維持費-50%、地上軍編成速度+30%、攻撃軍士気-20%、攻撃軍ダメージ-10%
* 経済的原始主義	(狂社会)(ゲーム開始後の追加削除不可)	職業によるエネルギーと交易価値-20%、鉱物と農作物+20%、幸福度+20%、消費財消費-50%、市場手数料+30%
* 土地の共有		(社会)		住居使用量-10%、農作物と鉱物生産量+10%、居住性-5%
* 共産主義		(社会、権威)	Pop成長速度+10%、工学研究速度+5%、Pop降下速度-100%、消費財消費量+10%、都市区域維持コスト+20%

### __〇 資本主義__
* 開発独裁		(独裁、資本、開発)	建造速度+10%、建造コスト-10%、安定度+5、専門家幸福度-10%
* 重商主義		(資本)			政治家が交易価値+3を産む、交易価値+10%、市場手数料+5%
* 金融資本主義		(資本)			都市区域が豪商1を産む。交易価値+15%、労働者幸福度-5%、消費財生産量-5%、合金生産量-5%
* 情報資本主義		(資本、物質)		交易価値+10%、研究力+5%、解読力+5、暗号力-5
* 農業資本主義		(資本、保全)		交易価値+10%、農作物生産+10%、居住性+5%、鉱物生産-5%
* 究極の規制緩和	(狂資本)(ゲーム開始後の追加削除不可)		専門家出力+10%、流入圧力+10%、犯罪度+20、犯罪度+15%、労働者幸福度-10%、安定度+10

### __〇 介入主義__
* 攻撃的情報機関	(介入、軍国)	解読力+5、回避+5%、連射レート+5%
* 情報操作		(介入、物質)	解読力+5、暗号力+5、友好度+20
* 高度な暗号技術	(介入)		暗号力+5、研究力+5%
* 外に向けられた眼	(介入、排他)	解読力+5、社会学研究+10%
* 笑顔の仲介者		(介入、平和)	使節+1、取引受諾値+50、交易価値+5%、友好度+20、統治志向魅力-10%
* 国際的黒幕		(狂介入)(ゲーム開始後の追加削除不可)	使節+1、暗号力+5、解読力+5、外交発言力+10%、友好度-30

### __〇 中立主義__
* 栄光ある孤立		(中立)(ゲーム開始後の追加削除不可)		安定度+5、宇宙軍許容量+20
* 防衛的情報機関	(中立、平和)	暗号力+10、研究力+5%
* 内政不干渉		(中立、排他)	安定度+10、統治者幸福度+10%
* 内なる満足感		(狂中立)	幸福度+5%、統合力+20%、研究力-10%
* 武装中立		(中立、軍国)	ステーション許容量+3、ステーション耐久度+10%、ステーション連射レート+10%、
* 利益代表国		(中立、平和)	使節+1、交易価値+10%、市場手数料-5%

### __〇 保全主義__
* 環境維持工学		(保全、物質)	居住性+10%、社会学+10%、鉱物生産-5%
* 害虫駆除		(保全、軍国)	開発主義国家に対して、環境保全の開戦事由を獲得（勝利すると開発主義の志向を保全主義に転向させ、相手を属国化させる。さらに、終戦時に戦争相手へ社会学研究力を自国の3か月分あげる）。
* 自然適応		(狂保全)	社会学+10%、農作物生産+10%、遺伝子改造コスト-25%
* 惑星庭園		(保全)		統合力+10%、農業生産量+5%、消費財生産+5%
* 絶滅防止法		(狂保全)(ゲーム開始後の追加削除不可)	社会学研究+20%、統合力+10%、消費財消費+10%、
* 自然信仰		(保全、精神)	司祭が算出する社会学+1、司祭が居住性+1%を算出、統合力+10%、精神志向魅力+10%

### __〇 開発主義__
* グランド・モニュメント(開発)							建築物Slot+1、建造物速度+10%、建築物コスト+10%、巨大構造物建造速度-10%
* 破壊掘削		(狂開発)(ゲーム開始後の追加削除不可)					居住性-10%、鉱物生産+30%、粉末生産量+20%
* 不可逆的な工業化	(開発)(ゲーム開始後の追加削除不可)							居住性-5%、合金生産量+10%、消費財生産+10%
* インフラ建築		(開発)							区域建造速度+10%、区域建造コスト-10%、区域維持コスト+20%
* 全国総合開発計画	(開発)							植民速度+25%、植民中維持コスト+10%、建築物スロット+1、巨大構造物建造コスト-10%
* 惑星規模灌漑			居住性+10%、農作物生産量+10%
* 惑星改造工学		(開発、物質)						テラフォーミング研究コスト-10%、テラフォーミングコスト-10%、テラフォーミング速度+10%

### __〇 栄望主義__
* 高度な栄典制度	(栄望)		以下略
* 複雑な外交儀礼	(栄望、削除不可)使節+1、影響力+1、消費材消費量+5%、友好度-10
* 栄典交換		(栄望、受容)	統合力+10%、友好度+20、志向転向度+5%
* 英雄志願部隊		(栄望、軍国)	攻撃軍士気+20%、攻撃軍ダメージ+10%、攻撃軍製造コスト+20%
* 独善的な英雄		(栄望、排他)	統合力+20%、艦船連射レート+5%、使節-1
* 称号と敬称の尊重法	(狂栄望)	25Popあたり1の貴族、影響力+1、栄望主義魅力+10%、移民流入-10%、幸福度-5%

### __〇 実利主義__
* 個人利益至上法	(実利、資本)	エネルギー生産+10%、交易価値+10%、犯罪度+10、犯罪度+10%
* 人権への抵当権	(実利、権威)	安定度+10、奴隷生産量+5%、奴隷購入コスト-10%、幸福度-10%
* 刑罰の金銭代替	(狂実利)	惑星の犯罪度*1の交易価値を惑星に付与、交易価値+10%、犯罪度+10、犯罪度+10%
* 適切な利益誘導	(実利)		安定度+5、エネルギー生産+10%、交易価値+20%、市場手数料-5%、労働者幸福度-5%
* 実益の確保		(実利)		外交発言力+10%、艦船連射レート+5%、請求権作成コスト-10%、友好度-10
* 高度生産消費社会	(実利、資本)	労働者生産量+10%、専門家生産量+5%、消費財消費量+20%

* 新自由主義（狂資本主義）
* カキストクラシー（実利主義。社会主義ではない）
* 三権分立（寡頭制、独裁制ではない、実利主義ではない）
* 空想的社会主義（社会主義）
* ノブレス＝オブリージュ（栄望主義。社会主義、資本主義ではない）
* 啓蒙主義（介入主義、受容主義。実利主義ではない）
* 真実と和解委員会（受容主義、中立主義。権威主義、実利主義、狂信的資本主義ではない）
* 戦力の不保持（狂平和、狂中立）


## __☆ 特性__

* 騎士道精神	：2p	統合力+10%、犯罪度-10%	
* 紳士      	：1p	統合力+5%、犯罪度-5%	
* 悪漢      	：-1p	統合力-5%、犯罪度+5%	
* 巨悪      	：-2p	統合力-10%、犯罪度-10%	

* 治癒遺伝子	：2p	Pop成長速度+5%、リーダー寿命+10年、地上軍耐久度+30%	
* 修復不能  	：-2p	Pop成長速度-5%、リーダー寿命-10年、地上軍耐久度-30%	

* 身体的同化	：1p	居住性+10%、Popの移住-10%	
* 適応不足  	：2p	居住性-10%、Popの移住+10%	

* 生体分裂  	：2p	Pop成長速度+10%				
* 多産多死  	：0p	Pop成長速度+5%、リーダー寿命-30年	
* 少子長命  	：0p	Pop成長速度-5%、リーダー寿命+30年	

* 異常発達  	：1p	Pop成長速度+20%、防衛軍強度+20%、統合力-20%、研究力-10%	
* 失われし種	：1p 	Pop成長速度-50%、統合力+20%、研究力+20%			

* 縄張り意識	：-2p	強制移住コスト+25%、Popの流入-10%、防衛軍士気+10%、住居使用量+5%	
* 移動性社会	：2p	強制移住コスト-25%、Popの流入+10%、住居使用量-5%、侵攻軍士気＋10%	

* 共感      	：1p	職業による統合力+5%、統治志向への魅力+10%、犯罪度-5%	
* 反感      	：-1p	職業による統合力-5%、統治志向への魅力-10%、犯罪度+5%	(この種族は、他者に対して常に反感を覚えている。)

* 磁性      	：2p	物理学+20%、合金生産-5%、					(この種族はほのかに磁性を有しており、物理学的技術発展に寄与している。)
* 放射性血液	：2p	物理学+10%、エネルギー+5%					(この種族の血液には放射性物質が含まれている。)
* 鬼火      	：2p	地上軍ダメージ+15%、合金生産+5%、侵攻軍ダメージ＋15%		(この種族は自在に火を操ることが可能である。)
* 光学適応  	：2p	地上軍耐久度+30%、住居使用量-5%、快適度消費-5%、犯罪発生+5%	(この種族は光学的に周囲へ溶け込むことで隠れることができる。)
* 硬質器官  	：2p	地上軍ダメージ+20%、地上軍耐久度+20%、鉱物生産+5%		(この種族は体の一部を硬化させることができる。)
* 神経遮断  	：2p	地上軍士気+40%、リーダー寿命+5年				(この種族は痛覚神経を一時的に遮断させ、痛みを避けることができる。)
* 飛行器官  	：2p	回避+5%、軍用機ダメージ+10%					(この種族は飛行することができる。)
* 俊足      	：3p	地上軍ダメージ+10%、地上軍耐久度+10%、地上軍士気+10%		(この種族は恐ろしい速度で走ることができる。)

* 千里眼    	：3p	食料算出量+5%、地上軍士気+10%、軍用機ダメージ+10%			(この種族は通常の視界以上のものを見ることができる。)
* 第六感    	：5p	地上軍士気+10%、回避+10%、研究力+5%					(この種族は予知能力のような形で一時的に未来を知ることができる。)
* 鈍い感覚  	：-3p	回避-10%、研究力-5%							(この種族は5感が鈍く、周囲を知るために時間がかかる。)
* 退化した眼	：-5p	回避-15%、研究力-5%、地上軍士気-10%					(この種族は眼が退化しており、周囲を探る方法が限られている。)

* 混乱      	：-2p	地上軍士気-5%、研究力-5%						(この種族はちょっとしたことで落ち着きを失い、混乱した状態となる。)
* 錯乱      	：-2p	研究力-10%、Popの快適度使用量+10%					(この種族は混沌に満ちており、冷静さを失っている。)
* 憂鬱      	：-3p	Popの快適度使用量+10%、幸福度-10%					(この種族は常に憂鬱で、落ち込んだ状態で生活している。)
* 惰弱      	：-4p	鉱物生産量-10%、食料生産量-10%、地上軍耐久度-10%			(この種族は身体が弱く、熱心に動くことができない。)
* 心の死    	：-4p	研究力-10%、統合力-10%、Popの快適度使用量-15%				(この種族は心を失っており、熱心さがない。)

* 巨大      	：3p	Popの食料消費量+10%、住居使用量+15%、地上軍ダメージ+20%、地上軍耐久度+20%、家畜からの食料+3、Popの鉱物・エネルギー・食料生産+10％	(この種族の身体は銀河基準からしても巨大である。)
* 大型      	：2p	Popの食料消費量+5%、住居使用量+10%、地上軍ダメージ+10%、地上軍耐久度+10%、家畜からの食料+1、Popの鉱物・エネルギー・食料生産+5％		(この種族の身体は銀河基準からしても大柄である。)
* 小型      	：-2p	Popの食料消費量-5%、住居使用量-10%、地上軍ダメージ-10%、地上軍耐久度-10%、家畜からの食料-1、Popの鉱物・エネルギー・食料生産-5％		(この種族の身体は銀河基準からしても小型である。)
* 極小      	：-3p	Popの食料消費量-10%、住居使用量-15%、地上軍ダメージ-20%、地上軍耐久度-20%、家畜からの食料-3、Popの鉱物・エネルギー・食料生産-10％	(この種族の身体は銀河基準からしても極小である。)

* 狩猟文化  	：-3p	食料生産-20%、居住性-5%	(この種族の社会は狩猟により食料を確保している。)
* 採取文化        ：-3p	食料生産-20%、居住性-5%	(この種族の社会は採取により食料を確保している。)
* 狩猟採取文化    ：-2p	食料生産-10%、居住性-3%	(この種族の社会は狩猟や採取により食料を確保している。)
* 農耕文化        ：2p	食料生産+10%、居住性+3%	(この種族の社会は農業に基盤が置かれている。)

* 複雑な言語      ：-1p	Popの快適度使用量+25%、統合力+5%	(この種族の語彙や文法は極めて難しい。)
* 非言語社会      ：-2p	研究力-10%、統合力-5%、Pop成長速度+3%	(この種族には言語という概念が存在しない。)
* 無文字社会      ：-2p	研究力-10%				(この種族には文字という概念が存在しない。)

* 美味な肉体      ：0p	家畜からの食料+2					(この種族は美味しい！)
* 不味い肉体      ：+1p	家畜からの食料-2、Popの食料消費量-10%			(この種族は不味い！)
* 霜降り          ：-1p	家畜からの食料+1、Popの食料消費量+10%、リーダー寿命-5年	(この種族は全身が霜降りである。)
* 有毒            ：-1p	家畜からの食料-3、職業による快適度-10%			(この種族の肉は有毒である。)

* 複雑な遺伝構造  ：1p	社会学+15%、遺伝子改造コスト+20%	(この種族の遺伝子は極めて複雑である。)
* 単純な遺伝構造  ：-1p	社会学-15%、遺伝子改造コスト-20%	(この種族の遺伝子は極めて単純である。)

* 感光性          ：-1p	快適度使用量+10%	(この種族は極めて光に弱く、光を避ける傾向にある。)
* 好光性          ：-1p	住居使用量+5%		(この種族は光を好み、日光を浴びることを好む。)

* インドア派      ：-1p	住居使用量+10%	(この種族は屋内での活動を好む。)
* アウトドア派    ：+1p	住居使用量-10%	(この種族は屋外での活動を好む。)

* マルチタスク    ：+1p	研究力+5%	(この種族は器用で、同時に仕事を行うことができる。)
* 不器用          ：-1p	研究力-5%	(この種族は不器用で、同時に仕事を行うことが苦手である。)

* 理論的後進      ：-1p	物理学-10%	(この種族は理論構築が苦手であり、うまく物理学を扱えない。)
* 文化的後進      ：-1p	社会学-10%	(この種族の社会学的発展は遅れており、銀河規模の社会を取り扱い切れていない。)
* 技術的後進      ：-1p	工学-10%	(この種族の工学技術は遅れており、機械構築などは苦手である。)

* 優秀な個性      ：3p	リーダー取得経験値+10%、リーダースキル上限+2	(この種族は個々の個性を伸ばすことを重要視している。)
* 無個性          ：-3p	リーダー取得経験値-10%、リーダースキル上限-2	(この種族は個々の個性を均一化することを重要視している。)

* 社交性          ：2p	職業による快適度+10%、職業による統合力+5%	(この種族は社交的だ。)
* 内向性          ：-2p	職業による快適度-10%、職業による統合力-5%	(この種族は内向的だ。)

* 精神的開放  	：-4p	統治志向魅力-30%	(この種族は精神的な束縛を嫌う。)
* 精神的自由  	：-2p	統治志向魅力-15%	(この種族は精神的な自由を重視している。)
* 精神的権威  	：2p	統治志向魅力+15%	(この種族は精神的に誰かに従うことに慣れている。)
* 精神的従属	：4p	統治志向魅力+30%	(この種族は精神的に誰かの管理下に置かれることを好んでいる。)

* 嘘吐き      	：-2p	職業による快適度-10%	(この種族は小さい嘘をつくことを好み、しばし周囲を疲弊させる。)
* 正直者      	：2p	職業による快適度+10%	(この種族は正直者で、周囲に気持ちの良い関係を構築する。)

* 無心        	：-2p	食料算出量-15%		(この種族は心を込めて食物を作ることができない。)
* 放蕩        	：-2p	エネルギー算出量-15%	(この種族はエネルギーを無駄にする傾向がある。)
* 疲労感      	：-2p	鉱物産出量-15%		(この種族は疲労しやすく、鉱物生産が苦手である。)
* 愚鈍      	：-2p	研究力-10%		(この種族は知力が低く、うまく研究を進めることができない。)
* 浪費家      	：-2p	交易価値-25%		(この種族は浪費癖があり、交易をうまく行うことができない。)
<!-- 以下、対応するポートレートのみ選択可能。 -->
* 高度な手指（ヒューマノイド）：2p	合金生産+10%							(この種族の手指は器用で、うまく加工を行うことができる。)
* 同族殺し（ヒューマノイド）  ：-2p	統合力-10%、安定度-5%、軍国主義魅力＋10%、平和主義魅力-10%	(この種族は互いに殺し合いを行う悪習がある。)
* 美しい毛並み（哺乳類）      ：2p	職業による快適度+10%、居住性+5%					(この種族の毛並みは長く、美しい。)
* 暴力的本能（哺乳類）        ：-2p	地上軍士気-10%、統合力-5%、地上軍士気＋5%			(この種族は本能的に粗暴である。)
* 身軽な身体（鳥）            ：2p	回避+5%、住居使用量-10%						(この種族は体重が少ない割に筋肉量が多く、身軽に動くことができる。)
* 鳥頭（鳥）                  ：-2p	研究力-10%、統合力-5%、幸福度＋5%、統治志向魅力＋10%		(この種族の脳は小さく、すぐ忘れてしまう。)
* 効率的代謝（爬虫類）        ：2p	食料消費量-15%							(この種族の代謝効率は極めて高く、少ない食料で生きていける。)
* 外温性（爬虫類）            ：-2p	居住性-5%、リーダーの寿命＋5年					(この種族は外部の温度に体温を左右されるため、居住について課題が多い。)
* 合理的身体機能（虫）        ：2p	居住性+10%							(この種族の身体は極めて合理的で、あらゆる環境に適応できる。)
* 変態（虫）                  ：-2p	Pop成長速度-10%、住居使用量-5%					(この種族は幼体から成体になる間に大きな形態変化を必要とするほか、変態時に突然死することも多い。)
* 柔軟な筋肉（軟体人）        ：2p	鉱物生産量+5%、地上軍ダメージ+10%				(この種族の筋肉は柔軟で、強度も高い。)
* 腐食性粘液（軟体人）        ：-2p	Pop消費財消費量+10%、地上軍攻撃力+5%				(この種族が分泌する粘液は腐食性で、様々なものを壊すことが多い。)
* 高分子分解（菌類）          ：2p	Pop成長速度+10%							(この種族は様々なものを分解し、栄養とすることができる。)
* 変性胞子（菌類）            ：-2p	職業による快適度-10%、居住性-5%、統合力+5%			(この種族の胞子は周囲に予測可能性の低い影響を与える。)
* 光合成（植物）              ：2p	食料消費量-20%、居住性+5%					(この種族は光合成により栄養を手に入れることができる。)
* 遅速性（植物）              ：-2p	地上軍耐久度-30%、住居使用量+10%、リーダー寿命＋15年		(この種族の足は遅く、動作が緩慢である。)

## __☆ 伝統__



## __☆ アセッションパーク__

* 外交シンクタンク					(外交官+2、外交発言力+30%)
* 帝国学士院					(研究選択肢+2、研究力+5%)
* 行政機構の再編			(管理許容量+20%、国是slot+1)
* 津波									(コルベット建造速度+100%、全艦隊建造速度-50%、艦隊許容量+30)
* 静謐										(統合力+20%、研究力+10%)3つ以上アセンションパークを取得しなければならない。平和、中立のみ
* 宮廷外交						(影響力+2、外交発言力+20%)権威もしくは栄望のみ
* 未来インフラ			(建造物slot+3、建造物建造速度+20%、区域建造枠+3、区域建造速度+20%、巨大構造物建造枠+2、巨大建造速度+10%)
* 高度防衛計画						(ステーション許容量+10、防衛プラットフォームの上限+150、星系基地船体値+50%)
* 絶対的階級制						(労働者生産力+15%、労働者政治力-100%、統治者幸福度+10%)権威のみ
* 象徴的構造物						(巨大構造物建造枠+2、巨大構造物速度+10%、巨大構造物コスト-10%)開発もしくは物質のみ
* 資源戦略調整省			(職業が消費する資源-5%、建造物のエキゾチックガス・揮発性粉末・レアクリスタル消費量-20%)
* 贅沢は敵だ						(Pop維持費-50%)軍国もしくは権威のみ
* 帝国の大動脈			(交易価値+30%、交易保護値+20、20Popにつき事務員Job+1、40Popにつき豪商+1)
* 人的資源省					(Pop成長速度+20%、幸福度+5%)
* 幸福省								(幸福度+5%、安定度+40)
* 徹底抗戦						(自国内連射レート+20%、船体値+10%、回避+10%、離脱可能性の減少-50%、厭戦値-30%)
* 帝国統合参謀本部		(亜高速移動速度+20%、FTL速度+10%、星系基地許容量+5、防衛ステーションの上限+50、宇宙軍許容量+30、指揮上限+30)
* 植民省					(入植速度+30%、移民流入+20%、Pop成長速度+5%、居住性+25%)
* 社会秩序維持局					(他国からの干渉的影響を受けない)
* 英雄の血統				(特殊なリーダー特性を追加)(英雄:このリーダーは全国民の憧れであり、素晴らしい成果を残した:リーダー経験値入手+100%、寿命+10年)
* 大規模建築計画局		(巨大構造物建造枠+2、巨大構造物速度+10%、研究選択肢を追加・メガエンジニアリング)（戦艦、シタデル、ゼロポイント発電の研究を完了している）
* 奢侈品の天国						(幸福度+50%、消費財消費量+100%)
* 重層的国家					(属国化要求受容度+50%、属国との友好度+50)
* 司教による請求権の捏造	(請求権コスト-50%、統合力+20%）精神のみ
* 帝国芸術協会				(統合力+20%、Jobによる統合力算出+20%、20Popにつき文化人Job+1)
* 諜報網に基づく請求権の捏造	(請求権コスト-50%、暗号力+10、解読力+10)精神以外
* スピードこそ命								(亜高速移動速度+20%、区域建造速度+10%、建造物速度+10%)
* 寵児							(没落帝国、覚醒帝国からの関係+200)
* 工部省					(建造物建造コスト-20%、区域建造コスト-20%、住居+30%)
* ハニカムハウス			(コロニー船建造コスト-50%、区域建造コスト-20%、住居使用量-30%)
* インサイダー取引		(貿易機構との裏取引は、交易による利益を最大化させる)		(市場手数料-10%、交易価値+20%)
* マンデルブロー集合における平面展開定理を利用した大規模農業	(農業区域の農民数+10、農業区域の住居+3、惑星における農業区域最大数+5)


## __☆ イベント__

### 1.作戦会議(ランダム発生)
我が国の戦争に対して、各所から所見が届いている。統合参謀本部からは必要な補給物資を将兵に与えることで士気を高めることができると指摘している。しかし、前線指揮官達は補給物資を別の用途で使用することで戦力を向上させることができると主張している。  
これらとは別に陸軍将校からは臨時の補強計画が提案されている。  
本日の会議は限られた資源をどのように投入するかという内容である。  


統合参謀本部に任せる。(消費財1000消費。1年間亜空間移動速度+10%)  
前線指揮官の見解を聞こう。(エネルギー1000消費。1年間艦隊連射レート+5%)  
陸軍のやり方に一理あるようだ。(合金500消費。3年間陸軍耐久+20%)  
ふむ。私の意見ではな......(軍国のみの選択)(エネルギー、合金500消費。2年間艦隊船体値+5%)  
会議は躍る(効果なし)  

### 2.軍事パレード(戦争期間2年以上でランダム発生)

長引く戦争の影響で国民の中には厭戦感情を訴えるものも存在する。その者たちの不安を解消し、我が国の威力を誇示するために戦時の軍事パレードを行うよう国防省から提案があった。

よろしい。直ちに軍事パレードだ。(影響力100消費。厭戦値-10)  
そのような余裕はない。(消費なし)  
軍事パレードではなく、追悼集会をしよう(平和のみ。影響力50消費。厭戦-10)  
盛大にやろうじゃないか(軍国or栄望or権威のみ。影響力100、エネルギー500消費。厭戦値-10%、1年間の厭戦増加-10%)  
英雄を讃え、勲章を配ろう。(実利以外。勲章を-10 厭戦値-10%、1年間の厭戦増加-10%)(編集済)  

### 3.厭戦活動(厭戦50以上かつ2年以上の戦争、攻撃側のみランダムで発生)

長きにわたる戦争のためか遂に(惑星名)の市民の一部が反戦デモを開始した。これは我が国の方針に反しており、徐々に規模が拡張している。

すぐに鎮圧しろ！(3年間惑星安定度-10。厭戦+10)  
代表者と交渉しろ。(影響力-100)  
いつも通り行えば良い。(権威のみ。影響力-30)  
群衆に呼びかけ、軍の支持集会を開け。(軍国のみ。影響力-50。厭戦-10)  
とある施設なら中で叫んでくれて構わない。(権威かつ社会主義。影響力-80。当該惑星に3年間強制労働者3枠のJobを獲得)  

開催地コンペ
  ●●大会の開催が決定された！我々もぜひ参加し、国威を高めるべきであるという意見が多数である。その大規模な大会を開催するに至り、開催地の選定が開始されることとなっている。
  銀河中の各惑星が名乗りを上げており、賑わいを見せている。我が国の経済と国威のためにも選定に参加するべきだ。国内の一惑星を選択してディシジョンにより推薦することができる。
  「よろしい。早速確認しよう」
  (銀河市場と同じような形のコンペ)

↓1年後
開催地決定
  1.大会の開催地が決定した。●●つまり、我が国の惑星は選ばれませんでしたが、素晴らしい大会にしようと我が国の選手も練習に励んでいる。選ばれた惑星には徐々に参加者や見物客が集まっている。「残念だが、大会こそ努力するべきである」
  2.大会の開催地が決定した。●●つまり、我が国の惑星が選ばれました。素晴らしい大会にしようと芸術家や建築家、官僚などが大会の演出について話し合い、急いで準備を始めている。●●には多くの参加者や見物客が集まっており、惑星の経済は大きく発展を見せている。「すばらしい。大会もすばらしいものにしなければ」
  (当該惑星5年間統合力+20%、交易価値+20%、幸福度+5%、Pop成長速度+10%、Pop製造速度+10%、流入魅力+30%。犯罪度+20%)

↓半年後
開催規模決定(選択期間半年)
  近くに開催される大会において、我が国の演出と選手団の規模について議論が上がっている。壮麗なものとすればもちろん国威を示すことができるが、選手団にその費用は用意できないという相談があった。我が国としてはどのように支援するべきであろうか。(主催国、参加国双方発生。時間切れの選択肢として最低限が選択される。)
  (大規模、質実充実、最低限の3種類。それぞれエネルギー3k、1k、0の消費で、大規模であれば、開会式で影響力を獲得する。)

↓8か月後
開会式
  ●●において△△の大会が開催された。開会にあたり式典が行われ、最新鋭の技術を利用したホログラムや機械的なアピールが行われ、市民たちは熱狂の渦に置かれた。各国の選手たちの入場もつつがなく行われ、居住性に合わせたドームの中で行進が行われた。
  入場の後には□□の国家元首である××により開会の宣言が起こなわれ、今から大会が開催される。「すばらしい」
  (開催規模決定の準備に応じて影響力を200、50、10を獲得)

↓2か月後
イベント
  イベント表準拠

↓1か月後
競技イベント
  競技イベント表準拠

↓2か月後
イベント
  イベント表準拠

↓1か月後
閉会式
  ●●における△△の大会が終了した。終了にあたる式典では今まで盛り上がった市民も冷めやらぬ中、優秀な成績を残した国家の表彰が行われた。最も優秀な成績を残した〇〇にはブリリアント合金によるトロフィーが贈られ、それに準じる◆◆と■■にもクリアナイト合金のメダルが贈られた。彼らの名前は会場付近のオベリスクに記名されて永遠に称えられる。
  □□の国家元首である××により閉会の宣言が行えわれ、大会は無事終了した。
  (優勝国1国、表彰国2名、その他に分かれる。それぞれのボーナスは別記

イベント表

1.地元の好況(大会開催以来開催地の景気は向上している。観光客を中心とした消費の上昇と土地価格等の向上は惑星規模の経済を大きく発展させている。地元企業や住民はこの好景気により多大な利益を得ている。)
エネルギー2k
1年間当該惑星交易価値+10%

2.テロ行為の事前発覚(惑星の治安当局は大会において大規模なテロ行為を行おうとした犯罪組織を未然に摘発することに成功したした。その組織は大会会場において原始的な中性子爆弾を炸裂させようとしたが、その材料入手の経路から組織摘発につながった。)
影響力+50
2年間当該惑星安定度+10

3.外交官の関心(この大会は世界的な注目を集めており、各国の外交官においても例外ではない。外交官の多くも選手の督励や観戦のために会場に集まっており、主催国の印象向上や外交的アピールの場としても利用されている。)
影響力+50
1年間外交発言力+10%

4.大会への熱狂(市民達は現在世界規模の大規模大会への関心を強めており、その開催と大会の内容に熱狂を続けている。至る所で大会の話題に花が咲き、市民は大会を心から楽しんでいる。)
2年間当該惑星幸福度+10%

5.国家規模の好景気(大会開催以来〇〇の景気は向上している。観光客を中心とした消費の上昇と土地価格等の向上は国家規模の経済を大きく発展させている。企業や市民はこの好景気により多大な利益を得ている。)
エネルギー5k
1年間帝国交易価値+10%

6.テロ組織の粉砕(〇〇の治安当局は大会において大規模なテロ行為を行おうとした犯罪組織を未然に摘発することに成功したした。その組織は大会会場において多数の中性子爆弾を炸裂させようとしたが、その材料入手の経路から組織摘発につながった。)
影響力+100
2年間帝国安定度+10

7.大会記念品のヒット(大会が開催されるにあたり、大会マスコットやさまざまな記念品が飛ぶように売れている。これらの経済効果は一時的であろうが、絶大な利益を産んでいる)
1年間当該惑星交易価値+10%

8.移民の流入(大会に合わせて観光客が惑星に詰めかけている。その中には〇〇への移住希望者が含まれており、入境当局は移民を許可した。そのことから観光客の中にも移住希望者が出ており、惑星人口は上昇傾向にある。)
当該惑星に全銀河のPopのうちランダムに2Pop発生
1年間当該惑星Pop成長速度+10%

9.国威発揚(大会は〇〇の経済的、文化的威信を示しており、国威発揚の側面を見せている。住民は大会誘致に成功した政府を支持し、各国の外交官や観光客に自国の宣伝を行うことに成功した。)
影響力+100
5年間帝国安定度+10

10.歴史的記録(この大会の実施と経過は全銀河史に残る偉業であると〇〇の文化人は主張している。この声を受けて現地当局は大会の歴史を記すプロジェクトを開始し、永遠に大会を記録しようと努力している。)
5年間当該惑星統合力+10%

11.世界的配信(この銀河的大会は全銀河で報道されており、その合間に行われる企業の宣伝活動やパブリックビューイングにおける経済活動は全銀河的な好景気を生んでいる。)
1年間参加国交易価値+5%

12.観光地評価(〇〇における大会は銀河中でも評価されており、観光地としての名声が高まっている。そのため、多くの観光客が〇〇に集まっており、経済的な利益を生んでいる。)
2年間当該惑星交易価値+5%
2年間当該惑星移民流入+20%

13.効率的運営(大会の運営は滞りなく行われており、その経験と知識は国家運営においても転用され、効率的な行政に繋げることが可能である)
影響力+50
5年間帝国管理許容量+10%

14.犯罪流入(大会が開催されるにあたり、開催地には多くの人的流入が発生した。無論多くは観光客や大会関係者ではあるが、その中には犯罪者もまぎれており、開催地での治安悪化が報告されている。)
2年間当該惑星犯罪度+10

15.大会事故発生(大会が開催され、協議が進んでいる中で会場の照明が落下する事故が発生した。幸いにも死傷者は出なかったが、会場の設備等の再点検が行われ、開催地の住民は不安視している。)
1年間惑星幸福度-5%

16.運営の腐敗(大会の運営に対して「偶然」行われた金融調査の結果、大会役員の数名が大規模な汚職をしていたことが発覚した。国家の最高クラスの政治家がかかわっているとも考えられたが証拠は見つからなかった。しかし、今回の大会の誘致や会場建設等に大きな汚職事件が見つかったことは国家的威信を失うこととなった。)
エネルギー-1k
影響力-50

17.テロ発生(大会に多くの観光客が集まる中、突然発生した爆発は多くの命を奪った。反政府勢力を自称するテロ組織は会場近辺で中性子爆弾を破裂させ、数十万人の命を一瞬で奪い去った。幸いなことに選手や外交官、政府高官に犠牲者は出ておらず、会場自体も無事であった。大会運営は苦渋の決断として大会を継続させることを決めたが、遺族は不満を示しており、現地から逃げる者もいる。)
惑星上のPopをランダムに1Pop殺害
2年間帝国Pop幸福度-10%
1年間当該惑星Pop成長速度-10%

18.予想外の不況(大会の誘致は経済に大きな影響を与えるとされてきた。しかし、膨大な資金を投下したにもかかわらず経済的効果は殆ど現れなかった。あらゆる投資が効果をなしておらず、以外にも不況が訪れている。)
2年間当該惑星交易価値-10%

別枠
1.観艦式(栄望もしくは軍国のみ主催可能。エネルギー1000、影響50を消費。銀河コミュニティ加盟国に呼びかけ、3ヵ国以上の参加で開催。消費後に1年以内に首都惑星で軍艦1隻以上を当てるプロジェクトを遂行すれば達成。主催国は影響力200と5年間軍国主義、栄望主義魅力+20%、5年間外交発言力+20％)参加国は影響100と2年間外交発言力+10%を獲得。

行進開始
市民の関心
盛大な式次第
成功裏の終了
将校への叱責
私は帰ってきた！

競技イベント

1.息をのむ競技(しんと静まった会場の中で繰り広げられる競技は全銀河に放送されている。意図的に静かにしているわけではなく、皆無意識に息をのんでいるのだ。それほどまでに皆を引き込む試合はまだ続いている。)
1年間全参加国幸福度+10%

2.感動的選手(△△の選手団の団長は大会の有力選手である。何度も繰り返し傷病や成績不良による挫折を味わいながら這い上がった経歴を持つ団長は母国では英雄詩されており、彼の活躍は多くの人に感動を与えている。)
1年間参加国のうちランダムで1か国幸福度+20%

3.熾烈な競技(大会の有力国である●●と〇〇による競技は絶対に譲れない熱気がある。人々も熾烈なこの競技の結果を予測できておらず、予想外の追い抜きが繰り返されるたびに歓声をあげている。)
1年間参加国のうちランダムで2か国幸福度+20%

4.歴史的一戦(歴史的に熾烈な競争を続けている●●と〇〇による競技は絶対に譲れない熱気がある。人々も熾烈なこの競技の結果を予測できておらず、予想外の追い抜きが繰り返されるたびに歓声をあげている。)
1年間参加国のうちランダムで2か国幸福度+20%
1年間全参加国統合力+20%

5.全銀河記録の樹立(競技のとある試合において記録された成績は銀河で記録されたもののなかで、最も高い成績となった。全銀河記録の樹立に選手だけではなく人々も熱狂している。)
1年間参加国のうちランダムで1か国統合力+20%、影響力+100

6.観客の熱狂(大会の観客は選手たちの白熱する競技に熱狂しており、歓声は惑星中に広がっている。特に主催国である●●での熱狂ぶりは甚だしく、市民は競技に夢中である。)
1年間主催国の幸福度+10%

7.革新的チーム(△△の選手団は大会の有力候補である。天才的選手の直感に任せた勝利は派手さもあって人々からも人気であり、勝利に向かって進んでいる。)
参加国のうちランダムで1カ国優勝確率+20%

8.堅実なチーム(△△の選手団は大会の有力候補である。堅実に努力を重ねた優秀な選手が行う堅実な勝利は人々からも大いに認められており、優勝へと邁進している。)
参加国のうちランダムで1カ国優勝確率+20%

9.競技外での表彰(△△の選手団は日ごろの行いが素晴らしく、会場付近では自発的にごみ拾いを、選手団の中でも謙虚で礼儀正しい。その選手団の行為に対して現地当局は感謝状を発行し、選手団も恭しく受け取った。)
参加国のうちランダムで1カ国に影響力+30

10.スリル感のある競技(△△選手団は当初有力候補ではなかった。しかし、試合が開始すると頭角を現した。各試合の最終局面で一気に勝利へと追い込むさまはスリル感もあって全銀河を虜にしている。)
参加国のうちランダムで1カ国優勝確率+20%

11.ドーピングの発覚(厳正な審判団はあることに気が付いた。△△の選手団の様子がおかしいのである。審判団の追求と調査により△△選手団が違法薬物による瞬時の能力向上を行っていたことが発覚した。△△選手団の一部は失格となった。)
1年間参加国のうちランダムで1か国幸福度-10%
1年間主催国社会学研究+10%

12.競技における不正(厳正な審判団はあることに気が付いた。△△の選手団の様子がおかしいのである。審判団の追求と調査により不正なデータを結果に反映させるようクラッキングが行われていたのだ。△△選手団の一部は失格となった。)
1年間参加国のうちランダムで1か国幸福度-10%
主催国影響力+50

13.有力選手の故障(△△の選手団のうち最も有力視されている選手が発熱し、最高のパフォーマンスができない状態にある。そのため△△の選手団の成績は確実に落ちており、優勝の確立は下がっている。)
参加国のうちランダムで1カ国優勝確率+20%

14.選手によるヘイトクライム(△△の選手団の数名が開催惑星の市民に対して信じられないほどの差別的発言を行っていたことが発覚された。融和と平和の祭典で差別的発言を行ったことは許されない行為であり、△△の政府は弁明に追われている。)
参加国のうちランダムで1カ国影響力-50、1年間統合力-10%



決議「観艦式の実施」
観艦式（主催国は影響力200と5年間軍国主義、栄望主義魅力+20%、5年間外交発言力+20％)

開催地コンペ後、参加するか否かの選択肢が各国に与えられる。AIについては軍国と栄望は確定で参加。狂信的平和や狂信排他は参加しない。
各国は開催地で軍艦が最低1隻以上必要なスペシャルプロジェクトを実施。実施するとスペシャルプロジェクト実施国に効果があり、世界中に通知される観艦式のイベントが発生する。

威風堂々(影響力+100、影響力算出+10%)		(堂々とした艦隊。そして威厳溢れる将兵の威容が全世界に示され、〇〇軍の規律の高さは各国の称賛の的となっている。威厳ある軍は国際的な影響力の源泉となるだろう。)
百発百中(影響力+50、命中力+10%)			(〇〇の艦隊による観艦式とそれに伴う公開砲撃訓練は見事なものであった。用意された的を〇〇艦隊は高い精度で打ち抜いた。その成績は各国軍の中でも群を抜いており、その実力を〇〇軍は誇っている。)
疾風怒濤(影響力+50、亜高速移動速度+10%)		(〇〇の艦隊による観艦式とそれに伴う公開展開訓練は見事なものであった。〇〇艦隊は恐るべき速さと正確さで美しさを感じさせる陣形を展開させた。その成績は各国軍の中でも群を抜いており、その実力を〇〇軍は誇っている。)
堅甲利兵(影響力+50、船体値+10%)			(〇〇の艦隊による観艦式とそれに伴う模擬戦闘訓練は見事なものであった。〇〇艦隊は他国軍よりも粘り強く戦いを続け、最も精悍に戦い抜いた。その成績は各国軍の中でも群を抜いており、その実力を〇〇軍は誇っている。)
市民交流(影響力+50、外交発言力+10%)		(〇〇艦隊は観艦式に伴って市民との交流活動を開始した。市民との友好関係をアピールし、厳格な軍のイメージを軟化することに成功したことは〇〇のイメージを国際的に改善することに大いに役立った。)
情報漏洩(影響力-50、2年間暗号力-10)		(〇〇艦隊は観艦式に伴って市民との交流活動を開始した。しかし、この活動は大失敗であったと言わざるを得ない。市民に扮した工作員が艦内に侵入し、バックドアを残していったのだ。重要な軍事機密は各国に筒抜けとなってしまった。)
意外な冷遇(影響力-50)				(○○艦隊が開会地に向かうと、その場では〇〇軍に対する反対運動が発生していた。市民の反発と、それに伴う現地当局による冷遇は〇〇政府の体面を大きく損なった。)
大失態(影響力-100)				(〇〇艦隊は観艦式に伴う行進を開始すると、恐ろしいことに接触事故を起こしてしまった。損害は出なかったが大衆の前で発生した事故であり、その収拾にあたった将校も泥酔状態という信じられない大失態を起こしてしまった。)
私は帰ってきた！(参加した艦艇を失う。影響力-150)(「●●よ！  私は帰ってきた！」そう通信網に響き渡ったかと思うと、艦隊集結地に眩い光が満ちたかと思うとすさまじい衝撃波が襲った。艦隊集結地に純粋水爆ミサイルが撃ち込まれたのだ。●●に古くから残るテロ団体が乾坤一擲の一撃を食らわせたが、治安機関の力ですぐさまテロ団体は撃滅された。破壊された艦隊に生存者はおらず、損害は莫大である。最後に残された通信回線にはとある艦長の一言が残されていた。「何の光!?」)レアイベント

●●(開催地星系名)
〇〇(スペシャルプロジェクト実施国)