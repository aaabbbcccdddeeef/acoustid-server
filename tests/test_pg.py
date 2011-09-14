# Copyright (C) 2011 Lukas Lalinsky
# Distributed under the MIT license, see the LICENSE file for details.

from nose.tools import *
from sqlalchemy import sql
from tests import prepare_database, with_database, TEST_1A_FP_RAW, TEST_1B_FP_RAW, TEST_1C_FP_RAW, TEST_1D_FP_RAW, TEST_2_FP_RAW
from acoustid import const
from acoustid.data.fingerprint import insert_fingerprint


@with_database
def test_bad_match_not_unique_enough(conn):
    fp1 = [91747667,89638259,97899875,97903987,89650515,89638227,89511283,89646451,89650547,97895795,97907059,89515347,89642323,89638227,91616627,91743571,89642355,97867123,97903987,89519443,89638227,89511283,89646419,89650515,97895795,97907059,89515347,89650515,89638227,89519475,89646451,89642355,89511283,97903987,89515347,89638227,89511283,89515347,89650515,98026867,97898867,97903955,89650515,89638227,89511283,89646451,89642355,89507187,97908083,89515347,89642323,89511283,89515347,89650515,98026867,97898867,97903955,89650515,89638227,89511283,91743603,89650547,89507187,97908083,89515347,89642323,89507155,89519443,89650515,89642355,97898867,97902963,89519443,89638227,89511283,89646451,89650515,89507187,97899891,89515379,89650515,89638227,89519475,89646419,89642355,97898867,97902963,89515347,89638227,89511283,91612499,89650515,89638259,97899891,97903987,89650515,89638227,89511283,89646451,89642355,97894771,97907059,89498897,123196753,125162865,125166929,125302097,123192689,123065827,118842867,91698643,91703251,100091891,100091875,99903459,99902803,97870147,89642307,89638227,89638259,91616627,91743571,89642355,89511283,97903987,89519443,89638227,89511283,89646419,89650515,97895795,97907059,89515347,89650515,89638227,91616627,89646451,89642355,89511283,97903987,89515347,89638227,89511283,89515347,89650515,98026867,97898867,89515347,89650515,89638227,91608435,91743603,89642355,89507187,97908083,89515347,89642323,89511283,89515347,89650515,98026867,97898867,97903955,89650515,89638227,89511283,91743603,89650545,89507185,97908081,89515347,89609555,89474387,89519443,89650547,89642355,97898867,89515347,89519443,89638227,89511283,89646419,89650515,89507187,89511283,89515347,89650515,89638227,89519475,89646451,89642355,97899891,97903987,89515347,89638227,91608435,91612499,89650515,89638259,97899891,97903987,89650515,89638227,89511283,89646451,89642355,97899891,97907059,89515347,89642323,89511283,91612499,91747667,89638259,97899891,97903987,89650515,89638227,89511283,89646451,89650547,97895795,97890675,89498961,89625937,123176273,125154673,125281617,123196785,123064817,123036659,91699155,91686866,100075490,100075490,99890658,97789266,97871171,89609539,89638211,89638227,91616627,91743603,89642355,89511283,97903987,89515347,89642323,89511283,89515347,89650515,98026867,97898867,97903955,89650515,89638227,91608435,91743603,89642355,89507187,97908083,89515347,89642323,89511283,89515347,89650515,98026867,97898867,97903955,89650515,89638227,91608435,91743603,91747699,89507187,97908083,89515347,89642323,89507155,89519443,89650515,89642355,97898867,97903955,89519443,89638227,91608435,91743603,89650513,89507185,97899891,89515347,89650515,89507155,89519475,89646451,89642355,97898867,97902963,89515347,89638227,91608435,91612499,91747667,89638259,97899891,97903987,89650515,89507155,89511283,89646451,89642355,97895795,97907059,89515347,89642323,91608435,91612499,91747667,89638259,97899891,97903987,89650515,89638227,89511283,89646419,89650547,97895795,97907059,89515347,89642323,91735411,91616625,91744081,91739507,97899891,97903987,97908051,89638259,89511283,89646419,89650515,98026867,97907059,97903955,89650515,89507187,91600241,91727121,89626416,1205179184,1205182768,1205182736,1180143920,1444255600,1463134032,1463287376,1467403889,1442301797,1442103655,-704847513,-713236153,-680078009,-680069177,-713621545,-705243177,-671821337,-671813145,-680205849,-684240569,-684305081,-717848745,-713654409,-705210521,-709602969,-705367705,-705367737,-680069817,1467414471,1433862103,1442240503,1475727847,1475670503,1467277799,1463112007,1463178567,1429634903,1433829239,1442273127,1437880679,1442083175,1442111815,1433859399,1433859527,1433862103,1442240503,1442174439,1475670503,1467277799,1467347271,1463178567,1362523991,1366720375,1442273143,1442076007,-705367705,-705371817,-713559737,-680069819,-713621547,-705243147,-671754267,-671821339,-671817241,-680234665,-684305081,-717851273,-713654409,-705208969,-705407641,-705408665,-704843449,-713035449,1400304967,1366753239,1366745079,1475859959,-671821337,-671813145,-680201769,-684306105,-784960169,-780763305,-772382857,-705341593,-705400473,-705371817,-713690809,-680069689,-713623595,-713621513,-671623177,-671821337,-671813145,-680205993,-684306105,-717851305,-713654441,-713662601,-705341595,-705408667,-705400491,-713756347,-713624249,-713621673,-713622666,-705176718,-705373726,-705364766,-713760618,-214511482,-230788730,-231329386]
    fp2 = [91739475,91604339,91616627,91612499,89642323,91604339,91616627,91743571,89642355,91607411,91612531,91747667,91735411,91608435,91613011,91748179,91604339,91608435,91612531,89642323,91604339,91616627,91612499,89642323,89507187,91616627,91743571,91739507,91608435,91613043,91747667,91735411,91608435,91612531,89650515,89638227,91608435,91612529,89650515,89507187,91616627,91612499,89642323,91604339,91616627,91744083,91739475,91608435,91612531,91747795,91735507,91608563,91612499,91747667,91604339,91607411,91612531,91747667,91735411,91617139,91613011,91739475,91604339,91616627,91743571,89642451,91608435,91612531,91747667,89638259,91607411,91612531,91747667,91735411,91608435,91613011,91739987,91604339,91616627,91612499,89642323,91604339,91616627,91743571,89642355,91608435,91612531,91747667,91735411,91608435,91613011,91747667,91604339,91608435,91612531,89650513,91604337,91608433,91612499,89642323,89507187,91616627,89646417,391632209,393598323,393602547,393736659,393724403,393597431,393569270,360149975,368461523,100026211,99894627,359949671,357852487,89539591,89572679,91669843,91735411,91617139,91744083,91739475,91608435,91612531,91747667,91735507,91608435,91612531,89650515,89507187,91607411,91612531,91739475,91735411,91616627,91613011,91739475,91604339,91616627,91612499,89642323,91608435,91612531,91747667,91735411,91608435,91612531,91747667,91735411,91608435,91613011,91739475,91604339,91616627,91612499,89642323,91604337,91616625,91612499,89642355,89511283,91612531,89650515,89638259,91608435,91612499,91747667,91604339,91608435,91612531,91747795,91604467,91608563,91612627,91739603,91604339,91616627,91612499,91739507,91608435,91613043,91748179,91735411,91608435,91612531,91747667,91735507,91608435,91612531,89650515,89507187,91616627,91612531,91739475,91735411,91617139,91613011,91739475,91604339,91612531,91743571,91735379,91608435,91612499,91747667,91735411,91607411,91612531,91747667,91735411,91608435,91613011,91739475,91604339,91616627,91612499,89642323,91604337,91616625,89650513,89642355,89511283,91612465,89650515,123192691,125162867,125166931,125292883,125157875,125137394,91579346,100029399,100026195,100091747,99894627,97805671,97871175,97928519,97961287,98025975,97907703,89514869,89651025,89507189,89453925,89515381,89650517,89638231,89511287,89617751,89609559,97867255,97871351,98006487,97994199,89510391,89514867,89650001,89638261,89453925,89515381,89650517,89642325,89642359,89617751,89609559,89511415,97904119,98035159,97994199,89506295,89449463,89645909,89642325,89511285,89449845,89515349,89642325,89642359,89617751,89609559,89478647,89515511,98035159,98026967,89506295,89453559,89645911,89642325,89507189,89449845,89515381,89642325,89642327,89617751,89609559,89478647,97908215,98035159,98031063,89506295,89519095,98034519,98031445,89507189,89453925,89515381,89650517,89642327,89642359,89609559,89609591,97875447,97904119,98039255,98025975,90035191,90039159,98038613,89507189,89453925,89515381,89650517,89642327,89642359,89617751,97998167,97867255,97904119,98039255,89605591,90034679,90039287,90174293,89638261,89445733,89449845,89650517,89642325,89642359,89617751,89605463,89478519,89482615,98002263,89605459,89998835,90007027,89612759,97997175,97866613,97838069,97903573,92723029,96982903,88397159,84206951,84272247,84329543,88524103,89571655,89506295,89449463,89646037,98030933,89507189,89449845,89515349,89642325,89642327,89609559,89609559,97867127,97908087,97903959,98031063,89506295,89519095,89645911,98031445,123061621,123004261,89515381,89650517,89642327,89642359,89609559,97998199,97875319,97903991,98031063,89637335,89510903,90039157,89651029,123061621,123008357,123069813,89650517,89642325,89642359,89617751,89605463,89478518,89515511,98039255,89605591,89510391,90039287,98039765,131585397,123008357,123004277,89646421,89642327,89642359,89617751,89605462,97899894,97903990,98035031,89637335,89506295,89514999,98035669,98031061,123065717,89449845,89515349,89642325,89642359,89650519,97998167,97899894,97908086,98035031,89642327,89506295,89519095,89647061,131585877,123061621,123004277,89515349,89642325,89642327,89642327,89609559,97867126,97875318,97903959,98031063,89637367,89519095,89515893,89642325,123061621,123004261,123069813,123204949,89638229,89642359,89609559,97998198,97867126,97871223,98006359,89605459,89478515,89482743,98005461,97862645,131396581,131458037,93844437,92718933,96781671,88405351,84206695,84337735,84329799,89572679,89571671,89506807,89514997,98035669,89638261,123000181,123004277,123200853,123196757,89642359,89650519,97994071,97899894,97903990,98035031,89638231,89506295,89514999,89647061,89642325,123065717,89449845,89515349,89642325,89642359,89617751,97998167,97867126,97908086,98035031,98029911,89506295,89519095,89647061,89642325,123061621,123004277,123069813,89650517,89642327,89642359,89609559,97867126,97875318,97903991,98031063,89637367,89518583,89515989,98030933,123061621,123004261,123069813,89650517,89638231,89642359,89609559,97998198,97875318,97903990,98039255,89637335,89510903,89514997,98039765,123061621,123008357,123069813,123204949,89642325,89642359,89617751,97994070,97899894,97903990,98035030,89638359,89506807,89514999,89647061,89642357,123000181,123004277,89515349,89642325,89642359,89617751,97994071,97899894,97903990,98035031,98025943,89506295,89519095,89647061,89642325,123065717,123004277,89515349,89642325,89642359,89609559,89605463,97863030,97875318,98002263,89593175,223675763,223688051,223814999,1305941783,1297418038,1305749302,1301620246,1301688854,1233256982,1233130086,1216357094,1216373734,1216411110,1220605415,1220597235,1220793792,1212347840,1229125072,1258747248,1258804592,1258411348,1262609748,1262611797,1329855863,1329855974,1296260598,1304452566,1304485334,1304679894,1304678871,1304679383,1229452149,1229452133,1229452581,1229321509,1262780183,1271168790,1254457110,1254323510,1254257958,1271092598,1237370326,1237382614,1220605414,1220605411,1220793809,1212338624,1229124048,1292038512,1325651248,1325520656,1325528900,1329688405,1329819125,1329757671,1329815030,1304514006,1304452502,1304548822,1304679895,1304613319,1296290773,1296561013,1296561445,1296430373,1262779703,1271168279,1271234326,1254325558,1254257958,1271027046,1270957558,1237374422,1220605366,1220605351,1220597169,1220728256,1212347840,1296232912,1292038512,1325651216,1325520148,1329719124,1329720661,1329855847,1329823206,1329683958,1304452502,1304483222,1304548758,1304678871,1304679383,1296298997,1296560997,1296430373,1296430391,1329889047,1329889046,1321565974,1321434406,1321366822,1338201590,1338033622,1304483222,1287714214,1287714215,1287902673,1279447488,1296232912,1292103984,1291964720,1291966228,1291941652,1329688405,1329687925,1329823207,1338138102,1338199446,1338066326,1338070422,1304679831,1304679383,1296282583,1296150901,1296150885,1296150821,1329705269,1329706261,1329708309,1312931125,1308866613,1308793877,1308806421,1325581573,1325809989,256262469,197542261,163869153,155509217,155510257,155514353,155510241,155248083,155383107,188925250,188925298,189003026,188962130,197150579,163604323,163799889,163730241,164053489,155505121,155575793,155514353,155510241,155248115,155383107,188925250,188925298,188994930,155407634,163663730,163608419,163669841,163730241,163987953,163889633,155510257,155514353,155510241,155510259,155379011,188929346,188925266,188994866,188970770,188827410,163600227,163604337,163738433,163987953,163922401,155510257,155514353,155514337,155510243,155444547,155374914,188925266,188994930,155415826,155274578,163600227,163604339,163734353,163725777,163922401,155513313,155510257,155514353,155510241,155313491,155374915,188925266,188990770,189003026,188962066,163595635,163604323,163734353,163725649,163922401,155513313,155575793,155514353,155510241,155248083,155383107,188925250,188925298,189003090,155408210,197150579,163604323,163799889,163730241,164053489,155505121,155575793,155514353,155510241,155248115,155383107,188925250,188925266,188994930,155408146,163663730,163592035,163653457,163723009,164039985,163843425,155460977,189035889,188801377,197190499,197305282,163746754,163678178,155237858,151054818,151054834,155385287,155375045,163726789,163987921,163922401,155509233,155514353,155514337,155510243,155444547,155374914,188925266,188994866,188970258,155403538,163600243,163604339,163734353,163725777,163922401,155513313,155575793,155514353,155510243,155313491,155383107,188925266,188990834,189003026,155407698,163600243,163604323,163734353,163725761,163922401,155513313,155575793,155514353,155510241,155248115,155383107,188925250,188925298,189003090,155408210,163596146,163604323,163799889,163730241,164053489,155505121,155575793,155514353,155510241,155248115,155383107,188929346,188925266,155440498,155415890,163661682,163608419,163669841,163738433,163725809,155501025,155510257,155514353,155514337,155248099,155379011,188929346,188925266,188994866,188970258,188957970,163600243,163604337,163738577,163725777,163922401,155510241,155514353,155514353,155510243,155444547,155374914,188925266,188990770,189003026,155403602,163600227,163604339,163734481,163725777,163923425,155481569,155545073,155467123,155463011,155264339,155332930,222430034]
    query = sql.select([sql.func.acoustid_compare2(fp1, fp2, 80)])
    score = conn.execute(query).scalar()
    assert_less(score, const.TRACK_MERGE_THRESHOLD)


@with_database
def test_self_match_too_few_unique(conn):
    fp = [91615607,91607415,91616087,91746647,91739479,91607415,91611511,91583831,91575671,100004215,100005207,100128087,125292919,91611511,91746647,91607415,91607927,91743063,91739479,91575671,91583863,91616599,91608439,125161847,91611479,91746647,91734359,99996023,100000119,91746647,91738999,91616087,91617111,91608951,91608951,91612535,91616599,91607415,91607415,91611479,91738455,91738487,91615607,91615575,91607415,91607415,91743063,91739991,91576183,91584375,91612535,91608439,91574647,91615607,91615575,91738455,91607415,91742583,91746647,91738487,91616119,91616087,91739479,91608439,91612535,91616599,91608439,125161847,91611479,91738455,91738487,91615607,91615575,91738487,91738999,91743063,91748183,91604343,91608439,91612535,91583863,91575671,91582839,91615575,91738455,91738487,91742583,91746647,91607927,91607927,91743063,91739991,91608951,91616631,91616599,91608439,91607415,91611479,91746647,91738455,91615607,91611511,91738487,91738487,91615575,91747671,91608407,91608439,91612535,91747671,91607415,91616119,91616087,91738967,91738999,91743095,91615575,91607415,91607415,100131159,91739479,91739511,91616631,91616599,91608439,125161847,100000119,91746647,91738455,91607415,91611511,91746647,91607927,91616119,91616087,91739991,91608951,91612535,91583831,91574647,91607415,100000087,100127063,91738487,91615607,91615575,91738487,91607927,91743063,91748183,91572087,91575671,91612535,91583863,91574647,91582839,91615575,91738455,99996023,100131191,91746647,91738487,91616119,91616087,91739479,91608439,91612535,91616599,91574647,91607415,91611479,91746647,91738487,100004215,100000087,91738487,91738487,91743063,91747671,91604343,91608439,91612535,91747671,91607927,91616119,91616087,91607383,91738487,91742583,91746647,91607415,91607927,91743063,91739991,91576183,91584375,91582807,91574647,125129079,99967319,100102487,100127063,99996023,100000119,100135255,91738487,91616087,91616087,91608919,91607927,91611511,91615575,91574647,91615607,91611479,91738455,91738487,91746679,91615575,91607415,91607927,91611991,91739991,91608951,91616631,91612535,91607415,91607415,91611511,91746647,91738455,91738487,91742583,91746647,91607415,91616119,91616087,91739991,91608439,91612535,91616599,91608439,91607415,91611479,91738455,91738487,91615607,91615575,91607415,91607415,91742551,91747671,91571543,91575671,91612535,91616759,91574647,91582839,91615575,91738455,133681527,100131191,91746647,91738999,91616119,91743063,91739479,91608439,91583863,91583831,91575671,91574647,91611479,91746647,91738487,100004215,100000119,91738487,91738999,91743063,91748183,91604855,91608951,91612535,91615575,91574647,91615607,91615575,91738455,91738487,91742583,91746647,91607415,91607927,91611991,91739991,91608439,91616631,91616631,91608439,91607415,91611479,91746647,91738455,91607415,91611511,91746647,91738999,91616087,91748183,91608951,91608439,91579767,91583831,91574647,91574647,91611479,100127063,100127095,100004215,91615575,91607415,91607927,91743063,91739991,91604855,91607927,91611511,91607415,91607415,100004215,91615575,91738455,91738487,91742583,91746647,91607415,91615607,91615575,91739479,91608439,91612535,91616599,91574647,125161847,91611479,91746647,91738487,91615607,91615575,91738487,91607415,91743063,91747159,91604855,91575671,91612535,91583863,91574647,91582839,99971415,100127063,100127095,100131191,100135255,91607415,91616119,91611479,91739479,91608439,91583863,91616599,91608439,91607415,91611479,91746647,91607415,99996023,100000119,91738487,91738999,91616087,91617111,91608951,91608951,91611511,91582807,91574647,125137271,100004183,100127063,91738487,91611511,91615575,91607415,91607415,91743063,91739991,91608951,91584375,91579767,91574647,91574647,99971447,100135255,100127063,100127095,100131191,100135255,91607927,91616087,91617111,91608951,91608951,91612535,91583831,91574647,91607415,100000087,91738455,91738487,91746679,91746647,91738487,91607927,91611991,91748183,91604855,91608439,91612535,91575671,91574647,100004215,100004183,91738455,91738487,91742583,91746647,91607415,91616119,91616087,91739991,91576183,91579767,91583831,91575671,91574645,99967351,100102487,100127095,100004215,91742551,91738455,91738487,91615575,91616599,91608439,125171063,91612535,91739479,91706743,91616119,91611479,91607415,91607415,91742583,91746647,125288791,125162359,125170135,91616727,125162999,125171063,91747671,125293911,125161847,125166455,91615575,91607415,91607415,91742583,91738455,91738487,91616087,91616087,91608951,91617143,91613047,91714903,91702647,91574647,91611511,91615575,91738487,91746679,91746647,125292887,125293431,91616087,91616215,91608951,91617143,91743607,91739511,133551479,133558647,100004183,91607383,91738487,91742583,91746647,91738487,91607415,91615575,91608439,91616631,91612535,91747671,91702647,91607927,91611511,91615575,91738487,91746679,91746647,91739479,125293559,91616215,91617239,91608951,91616631,91743607,91739479,91574647,91582839,91582807,91574647,91738487,91743575,91739479,91735383,91607927,91611511,91616631,91616631,125166967,91747671,125289815,125161847,91611511,91615575,91607415,91746679,91743575,91739479,125293943,125170039,91616599,91608439,91616631,91743607,91739479,91735895,91607927,91612023,91616119,91616119,91743095,91747667,91735379,91607411,91615603,91615607,91616631,91616631,125302099,125293907,125292915,91616115,91615603,91607415,91615607,91743571,91739475,91735891,91607923,91615603,91615607,91615607,125298039,125293911,125289811,125161843,125165943,125170039,125170039,91747671,91747671,91735383,91738487,91612023,91616119,91607415,91615607,125298007,125293911,125289847,125170039,125170039,125170039,125171063,91743575,91673943,91735383,74830707,74834807,91616119,91615607,91612535,125302099,125289811,125161843,125165939,125170035,125170039,125302135,91747667,91739475,91739507,91616115,91615575,91608439,91616631,91743571,91739475,125289811,91607411,91615603,91615603,91615607,91743575,91739473,125289809,125162867,91611507,91615607,91615607,91612535,91747671,125289815,133677431,133558647,99938679,99997047,91616631,91743575,91674455,91735891,91607923,91550071,91541879,91615591,91743575,125302099,125257041,125161841,91615601,91615607,91616631,91743575,91747671,91735891,91734899,91616115,91616119,91583335,91579255,91710803,91706707,91702643,99971441,99971155,99963251,100005239,91743571,91739475,91735379,91603795,91615603,91615591,91616615,125298039,125302611,125290323,91603827,100004339,100004339,100004215,91742583,91747667,91735379,125289843,91615603,91615603,91616631,125166967,1199040339,1199036243,1198999411,1207292787,1173746547,1173746547,1165357939,1165484883,1165423955,1165477203,1165350259,1174271347,1173747059,1165358455,1165354327,91747667,125290323,125288819,100528499,100528499,100495735,92107127,91743571,91739603,91735539,100004211,100004183,99997175,125171191,125298135,1199035735,1199032151,1198904183,1198912375,1198912375,1198912375,1165452119,1165456215,1165443415,1173836151,1173713271,1173713271,99972471,91579735,91714903,91706707,91701619,100495731,100430199,100520311,100528503,91743703,91739603,125289939,125161939,91615735,91616743,125167079,125298167,125269335,125257559,125162355,125170039,125170039,91615607,91742551,91747671,91735383,91608439,91611511,91616631,91608439,91616631,91743575,91739479,91740019,91616115,91550071,91607415,91615607,91743571,91739475,91735379,91607411,91615603,91615603,91616627,125298035,125293907,125289811,125161843,91611507,91615603,91615603,91746675,91747667,91739475,91739507,91615603,91615571,91608435,91616627,91743571,125293907,125289843,91607411,91615603,91615603,91615601,91742545,125293905,125289809,125162865,125166961,125171061,125171063,91612535,91747671,91735891,100123507,100004723,91616119,91607927,92140407,91710803,91706707,91702643,100487539,100495699,99971447,91583863,125265235,125261139,125257043,125124979,99971443,100004211,100004215,100132183,91748163,125290451,125159379,125161971,91615735,125171175,125166967,125298007,125293911,125289303,125170551,125170039,91607415,91615607,91743575,91673943,91735379,91607927,91550583,91517799,91584359,91711319,91714899,91702611,91570547,99971443,100004211,100004215,100131159,125302231,125290451,125290455,125163511,125171191,125171175,125167079,91743703,91739479,91738455,91615575,91550039,91607415,91615607,91743575,91673943,91703123,91607923,91615603,91615607,91615607,91612535,125302103,125289811,125161843,125170039,125170039,125170039,91747703,91747671,91739479,74962291,74838903,74838903,91607415,91616631,91743571,125293907,125289843,125161843,91615603,91615603,91615603,91743571,91739475,91735379,91607411,91611507,91615603,91615603,125166963,125302099,125289811,125161843,125170035,125170003,125161847,91747703,91743571,91739475,91735411,91615603,91615571,91607415,125170039,125298003,125293907,125289811,125161843,133558643,133525879,99971447,91710807,91714887]
    query = sql.select([sql.func.acoustid_compare2(fp, fp, 80)])
    score = conn.execute(query).scalar()
    assert_greater_equal(score, 1.0)


@with_database
def test_match_similar_1(conn):
    query = sql.select([sql.func.acoustid_compare2(TEST_1A_FP_RAW, TEST_1B_FP_RAW, 80)])
    score = conn.execute(query).scalar()
    assert_greater_equal(score, const.FINGERPRINT_MERGE_THRESHOLD)


@with_database
def test_match_similar_2(conn):
    query = sql.select([sql.func.acoustid_compare2(TEST_1A_FP_RAW, TEST_1C_FP_RAW, 80)])
    score = conn.execute(query).scalar()
    assert_greater_equal(score, const.TRACK_MERGE_THRESHOLD)


@with_database
def test_match_similar_3(conn):
    query = sql.select([sql.func.acoustid_compare2(TEST_1A_FP_RAW, TEST_1D_FP_RAW, 80)])
    score = conn.execute(query).scalar()
    assert_less(score, const.TRACK_MERGE_THRESHOLD)


@with_database
def test_match_different(conn):
    query = sql.select([sql.func.acoustid_compare2(TEST_1A_FP_RAW, TEST_2_FP_RAW, 80)])
    score = conn.execute(query).scalar()
    assert_less(score, const.TRACK_MERGE_THRESHOLD)



