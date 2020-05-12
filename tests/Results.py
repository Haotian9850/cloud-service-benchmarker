from enum import Enum

class Results(Enum):
    RESULT_1KB_SPLIT = [0.765718936920166, 0.9154560565948486, 0.6637322902679443, 0.6680769920349121, 0.7591516971588135, 1.0383830070495605, 0.7470967769622803, 0.7216780185699463, 0.7339491844177246, 0.7127771377563477, 0.8606491088867188, 0.6736769676208496, 0.6986627578735352, 0.7168099880218506, 0.6679811477661133, 0.6595220565795898, 0.919748067855835, 1.1856410503387451, 0.6790149211883545, 0.7036218643188477, 0.7574870586395264, 0.6749236583709717, 0.6804962158203125, 0.8470571041107178, 0.7612018585205078, 0.7344119548797607, 0.6679720878601074, 0.6960349082946777, 0.7005171775817871, 0.6957688331604004, 0.836388111114502, 0.6983511447906494, 1.005112886428833, 0.6549108028411865, 0.7874679565429688, 0.8635320663452148, 0.6883373260498047, 1.0215873718261719, 0.7105143070220947, 0.6890809535980225, 0.9603369235992432, 0.7546110153198242, 0.7333779335021973, 0.6732218265533447, 0.7843070030212402, 0.7123799324035645, 0.7265200614929199, 0.7917532920837402, 0.7016360759735107, 0.6767361164093018, 0.7363660335540771, 1.1231248378753662, 0.888282060623169, 0.8048708438873291, 0.7227809429168701, 0.6854188442230225, 0.8378520011901855, 0.8695240020751953, 1.0924968719482422, 1.0971589088439941, 0.772799015045166, 0.8063108921051025, 0.69209885597229, 0.6783788204193115, 0.7198872566223145, 0.643502950668335, 0.6779780387878418, 0.7069098949432373, 0.7414119243621826, 0.8360037803649902, 0.7214820384979248, 0.8149189949035645, 0.750532865524292, 0.6820900440216064, 0.8616750240325928, 0.7586231231689453, 0.7073619365692139, 0.850377082824707, 0.8172092437744141, 0.918795108795166, 0.8662998676300049, 0.8068962097167969, 0.8872747421264648, 0.8471951484680176, 0.9454400539398193, 0.7348752021789551, 0.7808949947357178, 1.7529139518737793, 0.6746459007263184, 0.70784592628479, 1.0175950527191162, 0.6852962970733643, 0.7294199466705322, 0.7778899669647217, 0.8604528903961182, 0.9558889865875244, 0.685643196105957, 0.7688250541687012, 1.001244306564331, 0.7449250221252441]

    RESULT_10KB_SPLIT = [1.0116150379180908, 0.7203099727630615, 0.8242738246917725, 0.7481138706207275, 0.7268857955932617, 0.7137191295623779, 0.7538461685180664, 0.8179912567138672, 1.0764048099517822, 0.7521910667419434, 0.8982329368591309, 0.7316110134124756, 0.7864971160888672, 0.6927690505981445, 0.744844913482666, 0.7303552627563477, 0.8609440326690674, 0.7570981979370117, 0.7241742610931396, 0.8750247955322266, 0.8508510589599609, 1.0772509574890137, 0.7892038822174072, 0.8555741310119629, 0.7898869514465332, 0.6754860877990723, 0.9371597766876221, 1.0120420455932617, 0.9888708591461182, 0.7392849922180176, 0.769460916519165, 0.7098090648651123, 0.7084589004516602, 0.9782509803771973, 0.7013421058654785, 0.7528791427612305, 0.7323048114776611, 0.9137260913848877, 1.2711081504821777, 0.8515110015869141, 0.7360472679138184, 1.2515900135040283, 0.7632629871368408, 1.2816400527954102, 0.9332208633422852, 0.7332139015197754, 0.9788920879364014, 1.3572120666503906, 0.6906602382659912, 0.8568649291992188, 0.7870421409606934, 0.9860861301422119, 0.750769853591919, 0.6888139247894287, 0.7731819152832031, 0.7932541370391846, 0.7217562198638916, 1.0519239902496338, 1.1411771774291992, 1.0922608375549316, 1.273442029953003, 1.069162130355835, 0.7559502124786377, 1.1159439086914062, 0.7900350093841553, 0.7750768661499023, 0.7481589317321777, 0.7988207340240479, 0.8103291988372803, 1.0359370708465576, 0.7456252574920654, 0.8754918575286865, 0.857684850692749, 1.0406639575958252, 0.6766409873962402, 0.7373030185699463, 0.7716619968414307, 0.7089900970458984, 0.6898159980773926, 0.7893221378326416, 1.18265700340271, 0.7456347942352295, 0.750507116317749, 0.7952189445495605, 0.7376399040222168, 0.7517681121826172, 0.8263039588928223, 0.7493801116943359, 0.7080750465393066, 0.7879648208618164, 0.8790550231933594, 0.7988698482513428, 0.7320520877838135, 0.9325027465820312, 0.8532106876373291, 0.7544262409210205, 0.8006651401519775, 0.8310601711273193, 0.8682339191436768, 0.7623653411865234]

    RESULT_1MB_SPLIT = [1.1742517948150635, 1.1134772300720215, 0.9016780853271484, 1.001666784286499, 0.9092018604278564, 0.8297281265258789, 0.9290361404418945, 0.8546397686004639, 0.8689637184143066, 0.9957008361816406, 1.2774591445922852, 0.8139886856079102, 1.0996010303497314, 0.8277318477630615, 0.8335480690002441, 0.9487249851226807, 1.1478300094604492, 0.9280059337615967, 0.8979752063751221, 0.924246072769165, 1.0000441074371338, 1.1015410423278809, 0.9015958309173584, 1.040191888809204, 0.9134747982025146, 0.9831669330596924, 0.8751790523529053, 0.8573727607727051, 1.0551128387451172, 0.8512709140777588, 1.6277320384979248, 0.9167706966400146, 0.9353458881378174, 0.9930400848388672, 0.9721279144287109, 0.8724532127380371, 0.8538200855255127, 0.9623696804046631, 1.3662290573120117, 0.96114182472229, 0.9550590515136719, 0.8778181076049805, 1.0306568145751953, 0.9462029933929443, 1.2372419834136963, 0.9356353282928467, 1.4671401977539062, 1.1761078834533691, 1.0282282829284668, 0.9573760032653809, 0.9137682914733887, 0.9962201118469238, 0.9667141437530518, 1.147907018661499, 0.9174978733062744, 1.5599570274353027, 0.8851377964019775, 0.9326550960540771, 1.0040969848632812, 0.9989330768585205, 0.891237735748291, 0.9831349849700928, 1.0316739082336426, 1.0379178524017334, 1.1431288719177246, 0.9392051696777344, 0.9051308631896973, 1.0408601760864258, 0.91326904296875, 0.8505198955535889, 1.0703141689300537, 1.192620038986206, 0.9623470306396484, 0.962677001953125, 0.9439527988433838, 0.9248840808868408, 0.9070191383361816, 0.8951821327209473, 0.9765470027923584, 0.8425769805908203, 1.4010937213897705, 0.8843741416931152, 0.9458749294281006, 1.016597032546997, 0.8173508644104004, 0.8530237674713135, 0.9423620700836182, 0.817180871963501, 0.8483288288116455, 0.8557870388031006, 0.974912166595459, 0.8989341259002686, 0.7927882671356201, 1.0657532215118408, 0.828770637512207, 1.1045129299163818, 0.8763449192047119, 1.232748031616211, 0.9410350322723389, 0.8550119400024414]

    RESULT_10MB_SPLIT = [2.226418972015381, 2.0966429710388184, 1.775270938873291, 1.9028148651123047, 1.8108150959014893, 1.7855618000030518, 1.7701268196105957, 1.896388053894043, 2.0240821838378906, 1.8633620738983154, 1.792712926864624, 1.7533888816833496, 2.533220052719116, 1.7771880626678467, 1.9204778671264648, 1.7123630046844482, 1.9623208045959473, 1.8298671245574951, 1.87070894241333, 1.9041693210601807, 1.84676194190979, 1.798274040222168, 1.8865840435028076, 1.7970471382141113, 1.845534086227417, 1.8687622547149658, 1.8737289905548096, 1.9378371238708496, 1.7862389087677002, 1.7946979999542236, 2.2183098793029785, 1.8271098136901855, 1.765503168106079, 1.8465368747711182, 1.912889003753662, 1.8033571243286133, 1.7312469482421875, 1.814579963684082, 1.7383100986480713, 1.846318006515503, 1.8182811737060547, 2.542620897293091, 2.0079879760742188, 1.8339629173278809, 1.8365821838378906, 1.9375653266906738, 1.857846975326538, 1.855659008026123, 1.895387887954712, 2.4074442386627197, 3.7972872257232666, 2.0281732082366943, 1.9784739017486572, 1.9388177394866943, 1.8567731380462646, 1.7721662521362305, 1.8328230381011963, 1.828861951828003, 1.8565349578857422, 1.8245301246643066, 1.7436509132385254, 1.7656700611114502, 2.050778865814209, 1.8411760330200195, 1.7767360210418701, 2.255782127380371, 1.9078710079193115, 1.9438719749450684, 2.289991855621338, 2.081873893737793, 1.9038851261138916, 1.8804688453674316, 1.953153133392334, 2.0379951000213623, 2.029499053955078, 1.8971190452575684, 1.9569909572601318, 1.926811933517456, 1.8131377696990967, 1.8175508975982666, 2.4172558784484863, 1.8237557411193848, 2.0794172286987305, 1.7838950157165527, 2.3985068798065186, 2.0806729793548584, 1.8632571697235107, 1.8636879920959473, 1.8925352096557617, 2.0116288661956787, 1.9119510650634766, 1.903825044631958, 2.3265507221221924, 1.7562570571899414, 2.4844748973846436, 2.0522067546844482, 2.076111078262329, 1.8881123065948486, 1.7828309535980225, 1.996474027633667]

    RESULT_1KB_SINGLE = [0.13649916648864746, 0.11046481132507324, 0.1195530891418457, 0.6561989784240723, 0.12811899185180664, 0.19019174575805664, 0.19321227073669434, 0.14149689674377441, 0.16582989692687988, 0.26858019828796387, 0.11812305450439453, 0.12259316444396973, 0.11412310600280762, 0.10590696334838867, 0.3199460506439209, 0.12511587142944336, 0.14856195449829102, 0.13388800621032715, 0.09807324409484863, 0.12552905082702637, 0.11821413040161133, 0.10348010063171387, 0.10329079627990723, 0.12455296516418457, 0.1036689281463623, 0.11202001571655273, 0.11823678016662598, 0.11376214027404785, 0.15531706809997559, 0.1034088134765625, 0.11187005043029785, 0.10598492622375488, 0.09995794296264648, 0.14079618453979492, 0.10399317741394043, 0.11170196533203125, 0.10559201240539551, 0.10360980033874512, 0.11220097541809082, 0.1019890308380127, 0.10148882865905762, 0.10649275779724121, 0.12743711471557617, 0.10466575622558594, 0.10311079025268555, 0.10213994979858398, 0.10241174697875977, 0.10267806053161621, 0.10807204246520996, 0.1248631477355957, 0.9461202621459961, 0.10355710983276367, 0.10434794425964355, 0.10209798812866211, 0.10917878150939941, 0.10799980163574219, 0.10942602157592773, 0.09944868087768555, 0.1127171516418457, 0.10437512397766113, 0.1021127700805664, 0.13465499877929688, 0.10901880264282227, 0.10438823699951172, 0.10152602195739746, 0.10349893569946289, 0.17860198020935059, 0.11529088020324707, 0.10332703590393066, 0.12239599227905273, 0.10763692855834961, 0.14809417724609375, 0.10384511947631836, 0.12155389785766602, 0.10124897956848145, 0.1114339828491211, 0.12027192115783691, 0.10592269897460938, 0.11711406707763672, 0.10553908348083496, 0.1219487190246582, 0.10057306289672852, 0.09986305236816406, 0.10601592063903809, 0.09627389907836914, 0.09551715850830078, 0.09671711921691895, 0.10169315338134766, 0.1176300048828125, 0.10608792304992676, 0.09908294677734375, 0.10182666778564453, 0.09943008422851562, 0.09587287902832031, 0.09677505493164062, 0.09739303588867188, 0.10005593299865723, 0.10267019271850586, 0.10769104957580566, 0.10495901107788086]

    RESULT_10KB_SINGLE = [0.16677403450012207, 0.11574101448059082, 0.11662101745605469, 0.1133270263671875, 0.11770391464233398, 0.1175999641418457, 0.15467619895935059, 0.14129114151000977, 0.11714482307434082, 0.10260605812072754, 0.10788822174072266, 0.09918522834777832, 0.12241220474243164, 0.12494087219238281, 0.11777997016906738, 0.15192294120788574, 0.14914608001708984, 0.12525391578674316, 0.11525988578796387, 0.1824040412902832, 0.10780882835388184, 0.09815692901611328, 0.11120486259460449, 0.2675938606262207, 0.10863614082336426, 0.10023021697998047, 0.11365079879760742, 0.10518717765808105, 0.10193729400634766, 0.10423111915588379, 0.1094820499420166, 0.10255217552185059, 0.10537981986999512, 0.10225987434387207, 0.11097383499145508, 0.1018671989440918, 0.24592208862304688, 0.10192322731018066, 0.11509513854980469, 0.12392902374267578, 0.10426497459411621, 0.10068988800048828, 0.10477423667907715, 0.576153039932251, 0.10152482986450195, 0.13038897514343262, 0.09695911407470703, 0.11072993278503418, 0.10840415954589844, 0.1138908863067627, 0.10277915000915527, 0.10409688949584961, 0.10064506530761719, 0.09578800201416016, 0.09342575073242188, 0.09661388397216797, 0.09657502174377441, 0.09819483757019043, 0.13358402252197266, 0.1034548282623291, 0.14364290237426758, 0.10165691375732422, 0.09482502937316895, 0.09764599800109863, 0.10089707374572754, 0.10179495811462402, 0.10612607002258301, 0.10454916954040527, 0.09995317459106445, 0.1025998592376709, 0.11214518547058105, 0.10018396377563477, 0.11920428276062012, 0.1004338264465332, 0.10550594329833984, 0.10083818435668945, 0.10400986671447754, 0.09937095642089844, 0.14378905296325684, 0.10207629203796387, 0.10811114311218262, 0.10300493240356445, 0.12745213508605957, 0.12653493881225586, 0.1080923080444336, 0.10645198822021484, 0.09940004348754883, 0.09957289695739746, 0.12418770790100098, 0.09908294677734375, 0.10298585891723633, 0.11270618438720703, 0.11543393135070801, 0.10133981704711914, 0.13149023056030273, 0.1004328727722168, 0.09838318824768066, 0.10015201568603516, 0.09971117973327637, 0.10005903244018555]

    RESULT_1MB_SINGLE = [0.3058440685272217, 0.2398240566253662, 0.20487093925476074, 0.23882389068603516, 0.2178959846496582, 0.2677450180053711, 0.3053860664367676, 0.21471214294433594, 0.2600390911102295, 0.2018260955810547, 0.20380806922912598, 0.20160317420959473, 0.21526288986206055, 0.21344280242919922, 0.2404160499572754, 0.22120904922485352, 0.22295188903808594, 0.22921204566955566, 0.23891115188598633, 0.33243393898010254, 0.20963501930236816, 0.1986560821533203, 0.3333721160888672, 0.20438885688781738, 0.2204761505126953, 0.2644648551940918, 0.20859575271606445, 0.22813177108764648, 0.20285320281982422, 0.2610008716583252, 0.20156431198120117, 0.20764517784118652, 0.21790623664855957, 0.20781993865966797, 0.21117901802062988, 0.19757318496704102, 0.21456003189086914, 0.20255398750305176, 0.20495080947875977, 0.20633888244628906, 0.28452610969543457, 0.21375012397766113, 0.21783804893493652, 0.20670104026794434, 0.2032780647277832, 0.20571494102478027, 0.1986081600189209, 0.24847984313964844, 0.20655369758605957, 0.24114394187927246, 0.19732999801635742, 0.2060389518737793, 0.31801605224609375, 0.20845389366149902, 0.2069990634918213, 0.20112156867980957, 0.24631714820861816, 0.21195602416992188, 0.23458600044250488, 0.21091079711914062, 0.20662283897399902, 0.20272183418273926, 0.2714071273803711, 0.22896409034729004, 0.2006380558013916, 0.22901701927185059, 0.22771000862121582, 0.2205350399017334, 0.28112316131591797, 0.23515582084655762, 0.333359956741333, 0.2237720489501953, 0.269334077835083, 0.2147519588470459, 0.22731995582580566, 0.22770094871520996, 0.26558899879455566, 0.2046670913696289, 0.22164082527160645, 0.21570706367492676, 0.22363495826721191, 0.6952672004699707, 0.21855807304382324, 0.2569541931152344, 0.24442100524902344, 0.2163078784942627, 0.2713780403137207, 0.24265813827514648, 0.2074136734008789, 0.20533490180969238, 0.2155921459197998, 0.209075927734375, 0.25675010681152344, 0.20788002014160156, 0.22029900550842285, 0.20532703399658203, 0.2270209789276123, 0.202164888381958, 0.2035388946533203, 0.21918892860412598]

    RESULT_10MB_SINGLE = [0.5909891128540039, 0.6022758483886719, 0.5773980617523193, 0.545781135559082, 0.5359058380126953, 0.5715987682342529, 0.6105000972747803, 0.5916180610656738, 0.6414768695831299, 0.6050879955291748, 0.5450432300567627, 0.5318028926849365, 0.5370938777923584, 0.555577278137207, 0.5775270462036133, 0.549443244934082, 0.5700769424438477, 0.5493350028991699, 0.5606987476348877, 0.5495290756225586, 0.6692662239074707, 0.5604972839355469, 0.5643000602722168, 0.5687518119812012, 0.5729191303253174, 0.5505826473236084, 0.5966670513153076, 0.7591180801391602, 0.5569291114807129, 0.5534257888793945, 0.5427091121673584, 0.5495190620422363, 0.5448858737945557, 0.543651819229126, 0.5443108081817627, 0.5407888889312744, 0.5886180400848389, 0.5350918769836426, 0.5526199340820312, 0.5836522579193115, 0.5588412284851074, 0.5490758419036865, 0.5591638088226318, 0.6904280185699463, 0.5238080024719238, 0.624669075012207, 0.5708270072937012, 0.5371718406677246, 0.5746438503265381, 0.5404300689697266, 0.7552108764648438, 0.6257927417755127, 0.6029818058013916, 0.6288890838623047, 0.5656309127807617, 0.585529088973999, 0.6493418216705322, 0.5448930263519287, 0.646942138671875, 0.675119161605835, 0.6313259601593018, 0.5407009124755859, 0.5551378726959229, 0.6651349067687988, 0.6267950534820557, 0.7322540283203125, 0.6421539783477783, 0.5709669589996338, 0.6693530082702637, 0.596808910369873, 0.5452120304107666, 0.5717277526855469, 0.549293041229248, 0.5557782649993896, 1.0798349380493164, 0.577343225479126, 0.6015551090240479, 0.5378232002258301, 0.5477538108825684, 0.5639410018920898, 0.5819799900054932, 0.551447868347168, 0.636193037033081, 0.5404767990112305, 0.5509638786315918, 0.5435402393341064, 0.5453839302062988, 0.6979351043701172, 0.5331869125366211, 0.6187489032745361, 0.5534148216247559, 0.5713438987731934, 0.5382370948791504, 0.5463817119598389, 0.5515429973602295, 0.5652821063995361, 0.5294721126556396, 0.5456171035766602, 0.7059619426727295, 0.5411767959594727]


    