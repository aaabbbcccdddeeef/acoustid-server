from acoustid.models import Account, Application, Fingerprint, Meta, Track, TrackMeta

TEST_2_LENGTH = 320
TEST_2_FP = 'AQABVtuUZFGShAqO-h9OHD96SvhwBVNCKQnOIYmiIc-ENwF7TDe8Hr0W_AjhvRCP2sfT4DTS7zjyOYeqaI-RSxee5RmaWzhOHnlcaB6HnPgpdE-DkWIH2ysYG_Eh9zJCyfCXGOdw-EGoD2p69IavWOhzMD-a9tBx9FgPVz2qNDvQH3744ISIXRKeHto5_MhyeMtxc-COnYJ_lHLwRAgPvShz_Hga4zd8HD9UKXWOPP3xRLmGnlbQHKfxGPeRvAt6UngMvcF-gkpRi0bUZjGaH6FUHb_xGDt6aHmM__ghfkmH70B4fWiuCj8y8uj3oImZY8d3NFWWHuGF-3hCPEd_uEOyE_nw4w8ueXi24znCHOHxSWtw9BnSBzrSHF2Y4S0e_EioZoh9XMGfo2dqNMeP80aQPM5xGT9efMeTYL-KIqmHdDraHs-P8IcYjoj0I7_Q43iJ9BF64nSKKth2SjG-cvCHH-2OL8txHsUt9HhF4LiK5j16lAf1FkjvQiN55FSOkkOPkmj4GK-OH80eIeyh98HhE_qhPwjzKAV-HJ2OZkd4Q_vhp0d_6Id-_IeWW9CKoP3RKM-Bo3mOfvhxND_6HMgZ6EfXHB-8Q8-iok1znOi-ozmx54P2Dg5V_PCgLxy8KiH6C0cbHU3Ebtiho9Rxw8er47tw7jgRNxl84ziPJ-B1_DiNNClzaGSCvMGPGxePMD5qZYEuAwdTXYSYcIkmodc2nMqg_WgqBk_yBdVx0vCjQD8uhNRxXTgvVFSOSOmx61C1KMaNsFwM93h-PBdmFm8o45nxDabx48cTbGl4hHuhasjSwPtxPvAV1A7yQMukREERR-nxL8j-EbWYQ8sj4joABQQmjQhkjLFCKSAo4QoxYiQwQhgmkGjCKGAIMMA4BIwQwjhAFMBUCCUAYEIxpYxUCDlEjJYOScSMgsIIAgADwjKEFBAUCkMEMYAagoARzAAHCDCIISKANkgYYBiQwgDDjHEMIGWZFUBQLhgohBGkhECOMEAMIYghogTgQghgiSLCYUegAsJApIQjxABNDFWCa6AIAQ4Q4KgAgIABgGDCMNGIMgQJRQAQTACpgBNIJkUcBMkpoKAgXCjAgAAGKIcYIVAYbZgwggkEmKLEiYGYAYQQShFAAAQBFEEAEuEIgwYRQoARnBkAmAGMEAGFGIgQBigCwAkABEIA'
TEST_2_FP_RAW = [-772063964, -772066012, -1007079116, -1011011276, -1027788492, -1029889740, -1031261916, -1031269084, -1031270620, -1031021744, -1031079600, -1031078425, -1031032346, -1018580506, -1018646290, -1022775046, -1056337446, -1056261686, -1073039030, -1073039013, -1068976005, -1001867175, -733365175, -733302711, -737435575, -603332504, -603365272, -737516311, -188076117, -175490390, -745993558, -758642022, -767030630, -1034347878, -1038412133, -1039584631, -1039654264, -1034345784, -1030086056, -1011141092, -1045873092, -1045939676, -1045947803, -2132276505, -2132259914, -2140415082, -2140472938, -2140481130, -2140546634, -2140603929, -2144802523, -2144536267, -2123540203, -2115147515, -2081855203, -2098598611, -2098606801, -2098606737, -2106995329, -2090217989, -2123638309, -2140477173, -2140477173, -2123634405, -2106992325, -2107061957, -2107061991, -2107007715, -1033140963, -1023769329, -1025864433, -1026913002, -1010133962, -1017409482, -1017540482, -1022848902, -1056337830, -1056271030, -1056261302, -1073038501, -1068975271, -1060587447, -993477559, -1001672631, -737435575, -737566615, -737550231, -737419031, 1422585259, 1955228586, 1367940010, 1388841914, 1380453258, 1376328586, 1376458634, 1107956618, 1107899017, 1113072281, 1121657497, 1119494811, 1135224479, 1135226615, 1139489511, 1130891874, 1126713938, 1109977859, 1114237187, 1122691331, 1122695431, 1122687255, 1114233125, 1130944869, 1126746469, 1097554247, 1105885511, 1105885511, 1135270230, 1122523494, 1114135910, 1109939695, 1093236223, 1076520335, 1080714635, 1089107851, 11092923, 11010986, 15209450, 15492074, 7103274, 2913082, 2905882, 2940681, 2947848, 7138056, 32303368, 61716744, 44932552, 1118668232, 1118406137, 1122600424, 1110167912, 1110167848, 1110106424, 1122689305, 1118495003, 1118478714, 1118540010, 1122599146, 1110016234, 1110147562, 1110094153, 1076535560, 1076538376, -1058363384, -794183656, -794249176, -790063064, -261519320, -261519319, -529562582, -529628886, -530153430, -530280406, -534465494, -534459350, -517027794, -517027778, -517056387, 1630428508, 1634606924, 1643060940, -508616995, -508740929, -475252054, -487834709, -496223301, -496231493, -496092485, -488752486, -489735542, -494125366, -494125542, 1641889598, 1627335998, 1617898782, 1613703454, 1614756622, 537664270, 541854222, 541854238, 541874782, 558651982, 558168910, 558168910, 558168398, 566360398, 1636039038, 1669593454, 1938028670, 1942087766, 1942087766, 1665394807, 1631779173, 1640192868, 1640221300, 1640483428, 1640487796, 1631902020, 1627682884, 553932868, 554654068, 554589029, 567179879, 562985575, 562846279, 562879301, 558684487, 554678646, 554678646, 558873462, 567262070, 563067366, 562936022, 567064775, 558692565, 1628436725, 1661925605, 1661893095, 1666087909, 592329573, 567032663, 567032133, 567032132, 1640840020, 1909340900, 1909340900, -238142748, -775079212, -775152956, -1043580220, -1047774524, -2121450764, -2138162460, -2138162460, -2138232091, -2121520409, -2117330313, -2124670345, -2124604585, -2092205227, -2083848891, -2083787451, -2117489195, -2117550619, -2124902943, -2139517453, -2139383405, -2122597997, -2122598221, -2093090639, -2095162991, -2107737727, -2107754111, -2108805231, -2099495199, -2099499291, -2097402137, -2098451465, -2098709513, -2098717737, -2081859113, -2123773481, -2140434985, -2140496425, -2140428906, -2132171338, -2132236874, -2065124170, -2023181130, -2039964482, -2044162882, -2044098306, -2111137761, -2111117043, -2111165684, -2144720372, -2140460532, -2132132340, -2136328643, -2136407507, -2136471761, -2136471761, -2132277457, -2114187977, -2091268651, -2083809851, -2083872379, -2117361257, -2117552729, -2141681241, -2139584009, -2143708937, -2143618857, -2126874411, -2126894891, -2093339196, -2105923644, -2099628348, -2103836012, -2103966047, -2099751259, -2097639449, -2031579161, -2039763466, -2031375914, -2014728234, -2056675370, -2056548654, -2073127278, -2077251950, -2077233262, -2077266510, -2077332302, -2073154382, -2014434126, -2031143722, -2039794617, -2039792379, -2039792868, -2107033028, -2081936836, -2136462820, -2136265204, -2136263155, -2136456385, -2136456401, -2132228626, -2122791506, -2091070041, -2107647561, -2108769915, -2100384379]


def create_sample_data(ctx):
    acct1 = Account(name='user1', apikey='user1_api_key')
    ctx.db.add(acct1)

    app1 = Application(name='app1', apikey='app1_api_key', version='1.0', account=acct1)
    ctx.db.add(app1)

    tr1 = Track(gid='eb31d1c3-950e-468b-9e36-e46fa75b1291')
    ctx.db.add(tr1)

    m1 = Meta(track='Custom Track', artist='Custom Artist')
    ctx.db.add(m1)

    ctx.db.add(TrackMeta(track=tr1, meta=m1, submission_count=1))

    fp1 = Fingerprint(id=1, track=tr1, fingerprint=TEST_2_FP_RAW, length=TEST_2_LENGTH, submission_count=1)
    ctx.db.add(fp1)