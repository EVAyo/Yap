import os
import json

def js_dp(obj, path):
    json.dump(obj, open(path, 'w', encoding='utf-8'), ensure_ascii=False)

def js_ld(path):
    return json.load(open(path, 'r', encoding='utf-8'))


def exist_or_create_json(path):
    if not os.path.exists(path):
        js_dp([], path)


root_paths = [
    'dumps/',
    'text_dumps/',
    'dumps3',
    'dumps4.0',
    'dumps4.0_tx',
    'dumps4.0_tx2',
    'dumps4.0_tx3',
    'dumps4.0_tx4',
    'dumps4.0_tx5',
    'dumps4.0_tx6',
    'dumps4.0_tx7',
    'dumps4.0_pph',
    'dumps4.0_syfs',
    'dumps4.0_xs',
    'dumps4.0_yjls',
    'dumps4.0_longx',
    'dumps4.0_longx2',
    'dumps4.0_longx3',
    'dumps4.1_longx',
]

error_paths = set([

    # "dumps/17_raw.jpg",
    # "text_dumps/15279_raw.jpg",
    # "dumps4.0_tx/620_3_的_raw.jpg",
    # "dumps4.0_tx3/975_4_奇械机芯齿轮_raw.jpg",
    # "dumps4.0_tx3/976_2_奇械机芯齿轮_raw.jpg",
    # "dumps/166_raw.jpg",
    # "dumps/254_raw.jpg",
    # "dumps4.0_tx3/909_3_奇械机芯齿轮_raw.jpg",
    # "dumps4.0_tx3/913_3_奇械机芯齿_raw.jpg",
])

# 抛弃掉y方向歪的太离谱的
drop_paths = set([
    "dumps4.0_tx/620_3_的_raw.jpg",
    "dumps4.0/5496_1__raw.jpg",
    "dumps4.0_tx4/1118_3_宝姆凝_raw.jpg",
    "dumps4.0_tx7/397_1_兽萝_raw.jpg",
    
    "dumps/563_raw.jpg",
    "dumps/781_raw.jpg",
    "dumps/914_raw.jpg",
    "dumps/6703_raw.jpg",
    "dumps/6791_raw.jpg",
    "dumps/6660_raw.jpg",
    "dumps/9399_raw.jpg",
    "dumps/9400_raw.jpg",
    "dumps/9423_raw.jpg",
    "dumps/9401_raw.jpg",
    "dumps/9402_raw.jpg",
    "dumps/781_raw.jpg",
    "dumps/9828_raw.jpg",
    "dumps/1950_raw.jpg",
    "text_dumps/20596_raw.jpg",
    "text_dumps/2549_raw.jpg",
    "text_dumps/20597_raw.jpg",
    "text_dumps/20598_raw.jpg",
    "dumps3/1889_教官的面叶_raw.jpg",
    "dumps4.0_tx/764_2_冒险家_raw.jpg",
    "dumps4.0_tx/999_2_冒险家_raw.jpg",
    "dumps4.0_tx/1804_2_浊水的一_raw.jpg",
    "dumps4.0_tx2/534_0_浊水的一_raw.jpg",
    "dumps4.0_tx2/575_1_兽鸦印_raw.jpg",
    "dumps4.0_tx3/153_1_铁_raw.jpg",
    "text_dumps/8088_raw.jpg",
    "text_dumps/8099_raw.jpg",
    "text_dumps/8712_raw.jpg",
    "text_dumps/9359_raw.jpg",
    "text_dumps/9771_raw.jpg",
    "text_dumps/10575_raw.jpg",
    "text_dumps/10899_raw.jpg",
    "text_dumps/13565_raw.jpg",
    "text_dumps/13873_raw.jpg",
    "text_dumps/16089_raw.jpg",
    "text_dumps/21096_raw.jpg",
    "text_dumps/21110_raw.jpg",
    "text_dumps/23755_raw.jpg",
    "text_dumps/27649_raw.jpg",
    "text_dumps/33216_raw.jpg",
    "text_dumps/34326_raw.jpg",
    "dumps3/960_日人果_raw.jpg",
    "dumps3/1155_破损的面具_raw.jpg",
    "dumps3/1339_破损的面具_raw.jpg",
    "dumps3/1407_归兽鸦_raw.jpg",
    "dumps3/2046_孢_raw.jpg",
    "dumps3/2205_固者_raw.jpg",
    "dumps3/2295_来自的处_raw.jpg",
    "dumps4.0_tx/409_3_的洛_raw.jpg",
    "dumps4.0_tx/412_3_的_raw.jpg",
    "dumps4.0_tx/469_2_枯的一的_raw.jpg",
    "dumps4.0_tx/772_1_游医的枭孢_raw.jpg",
    "dumps4.0_tx/1113_3_游医的方巾_raw.jpg",
    "dumps4.0_tx/1800_2_浊水的一_raw.jpg",
    "dumps4.0_tx/1804_2_浊水的一_raw.jpg",
    "dumps4.0_tx2/150_3_地脉的新_raw.jpg",
    "dumps4.0_tx2/155_2_史莱姆凝液_raw.jpg",
    "dumps4.0_tx2/575_1_兽鸦印_raw.jpg",
    "dumps4.0_tx2/589_2_浊水的一_raw.jpg",
    "dumps4.0_tx2/617_2_浊水的一掬_raw.jpg",
    "dumps4.0_tx3/48_1_号_raw.jpg",
    "dumps4.0_tx3/153_1_铁_raw.jpg",
    "dumps4.0_tx3/185_4_混沌回路_raw.jpg",
    "dumps4.0_tx3/362_4_击_raw.jpg",
    "dumps4.0_tx4/185_2_战狂的时计_raw.jpg",
    "dumps4.0_tx4/325_1_混沌核_raw.jpg",
    "dumps4.0_tx4/408_3_兽肉_raw.jpg",
    "dumps4.0_tx4/509_2_大英雄的_raw.jpg",
    "dumps4.0_tx4/1134_2_沉重号角_raw.jpg",
    "dumps4.0_tx4/1155_2_混沌回路_raw.jpg",
    "dumps4.0_tx7/141_3_珊瑚真珠_raw.jpg",
    "dumps4.0_syfs/170_1_结地破的旧枝_raw.jpg",
    "dumps4.0_xs/37_2_蕈兽孢子_raw.jpg",
    "dumps4.0_longx/125_2_何人珍藏放_raw.jpg",
    "dumps4.0_longx/162_3_来自何处的放之花_raw.jpg",
    "dumps4.0_longx/200_4_何」淡通之_raw.jpg",
    "dumps4.0_longx/442_1_地野的枯_raw.jpg",
    "dumps4.0_longx/1003_4_士官的_raw.jpg",
    "dumps4.0_longx/1128_2_异界晶命_raw.jpg",
    "dumps4.0_longx/1672_1_藏的印_raw.jpg",
    "dumps/10794_raw.jpg",
    "dumps/11532_raw.jpg",
    "text_dumps/9341_raw.jpg",
    "dumps4.0_tx/157_2_浊水的一滴_raw.jpg",
    "dumps4.0_tx/666_2_芭_raw.jpg",
    "dumps4.0_tx3/493_1_地脉的旧_raw.jpg",
    "dumps4.0_tx3/992_1_精关正齿轮_raw.jpg",
    "dumps4.0_syfs/250_3_地脉的旧枝_raw.jpg",
    "dumps4.0_xs/2_1_蕈兽孢_raw.jpg",
    "dumps4.0_yjls/60_2_混沌容置_raw.jpg",
    "dumps4.0_longx/1125_4_隙间之_raw.jpg",
    "text_dumps/2555_raw.jpg",
    "text_dumps/32605_raw.jpg",
    "dumps/3751_raw.jpg",
    "dumps/4623_raw.jpg",
    "dumps/10811_raw.jpg",
    "text_dumps/16630_raw.jpg",
    "text_dumps/18909_raw.jpg",
    "text_dumps/19003_raw.jpg",
    "text_dumps/20896_raw.jpg",
    "dumps4.0_tx3/899_2_须彩蔷薇_raw.jpg",
    "dumps4.0_tx5/176_3_混沌机眼_raw.jpg",
    "dumps4.0_longx/556_3_地脉的枯_raw.jpg",
    "dumps/3237_raw.jpg",
    "dumps/6201_raw.jpg",
    "dumps/7024_raw.jpg",
    "dumps/12515_raw.jpg",
    "dumps/13114_raw.jpg",
    "dumps/14733_raw.jpg",
    "dumps/16196_raw.jpg",
    "dumps/18225_raw.jpg",
    "text_dumps/23970_raw.jpg",
    "dumps4.0/1047_2__raw.jpg",
    "dumps4.0_tx/1158_0_胡_raw.jpg",
    "dumps4.0_tx3/825_3_胡萝_raw.jpg",
    "dumps4.0_tx3/930_2_奇械机芯齿_raw.jpg",
    "dumps4.0_tx4/147_2_烹饪_raw.jpg",
    "dumps4.0_tx7/22_2_蘑灯_raw.jpg",
    "dumps4.0_tx7/38_2_蘑_raw.jpg",
    "dumps4.0_xs/78_2_动荷_raw.jpg",
    "dumps4.0_xs/131_2_须弥蔷薇_raw.jpg",
    "dumps4.0_longx/891_3_蒂尘_raw.jpg",
    "dumps4.0_longx/1642_1_新异的印_raw.jpg",
    "dumps/6177_raw.jpg",
    "dumps/6186_raw.jpg",
    "dumps/6218_raw.jpg",
    "dumps/6432_raw.jpg",
    "dumps/6729_raw.jpg",
    "dumps/16201_raw.jpg",
    "dumps/19296_raw.jpg",
    "text_dumps/25398_raw.jpg",
    "dumps3/69_菜_raw.jpg",
    "dumps4.0/1986_1__raw.jpg",
    "dumps4.0_tx/494_2_异凝_raw.jpg",
    "dumps4.0_tx4/1015_2_异海凝珠_raw.jpg",
    "dumps4.0_tx4/1117_2_黑铜号角_raw.jpg",
    "dumps4.0_pph/60_1_史莱姆原浆_raw.jpg",
    "dumps4.0_longx3/347_2_褪色红绸_raw.jpg",
    "dumps4.0_tx5/264_3_混沌机关_raw.jpg",
    "dumps/10800_raw.jpg",
    "text_dumps/11925_raw.jpg",
    "dumps4.0_tx2/349_3_方_raw.jpg",
    "dumps4.0_tx5/319_2_混沌模块_raw.jpg",
    "dumps/265_raw.jpg",
    "dumps/2614_raw.jpg",
    "dumps4.0_xs/134_2_须弥蔷薇_raw.jpg",
    "dumps/4569_raw.jpg",
    "dumps/16277_raw.jpg",
    "text_dumps/6983_raw.jpg",
    "text_dumps/11824_raw.jpg",
    "text_dumps/15279_raw.jpg",
    "dumps3/895_破损的面具_raw.jpg",
    "dumps4.0_tx/519_3_异色结晶藏_raw.jpg",
    "dumps4.0_tx/527_2_幸运儿银冠_raw.jpg",
    "dumps4.0_tx/1387_4_破损的面具_raw.jpg",
    "dumps4.0_longx/1151_2_须博_raw.jpg",
    "dumps4.0_longx/1304_2_混沌炉关_raw.jpg",
    "dumps/3277_raw.jpg",
    "text_dumps/18900_raw.jpg",
    "dumps3/2098_铜的_raw.jpg",
    "dumps4.0_longx/1346_2_新兵的徽记_raw.jpg",
    "dumps4.0_tx7/507_1_寻宝鸦印_raw.jpg",
    "dumps4.0_tx/1239_2_兽齿_raw.jpg",
    "dumps4.0_tx/1513_2_瑚_raw.jpg",
    "dumps/3268_raw.jpg",
    "dumps/3444_raw.jpg",
    "dumps/4655_raw.jpg",
    "dumps/11595_raw.jpg",
    "dumps/4118_raw.jpg",
    "dumps/9463_raw.jpg",
    "dumps3/1027_破脂_raw.jpg",
    "text_dumps/9148_raw.jpg",
    "text_dumps/15871_raw.jpg",
    "dumps3/1248_兽肉_raw.jpg",
    "dumps4.0_tx4/1167_2_菫色红绸_raw.jpg",
    "dumps/166_raw.jpg",
    "dumps/254_raw.jpg",
    "dumps/380_raw.jpg",
    "dumps/3713_raw.jpg",
    "dumps/3911_raw.jpg",
    "dumps/7052_raw.jpg",
    "dumps/7407_raw.jpg",
    "dumps/9420_raw.jpg",
    "dumps/10755_raw.jpg",
    "dumps/10759_raw.jpg",
    "dumps/12327_raw.jpg",
    "dumps/12970_raw.jpg",
    "dumps/14726_raw.jpg",
    "dumps/14793_raw.jpg",
    "dumps/14910_raw.jpg",
    "dumps/17377_raw.jpg",
    "text_dumps/157_raw.jpg",
    "text_dumps/4502_raw.jpg",
    "text_dumps/6345_raw.jpg",
    "text_dumps/12769_raw.jpg",
    "text_dumps/15503_raw.jpg",
    "text_dumps/15868_raw.jpg",
    "text_dumps/19150_raw.jpg",
    "text_dumps/20690_raw.jpg",
    "text_dumps/27907_raw.jpg",
    "dumps3/227_战脉的枯叶_raw.jpg",
    "dumps3/645_沉重号角_raw.jpg",
    "dumps3/1223_破官的_raw.jpg",
    "dumps3/1428_教官的怀叶_raw.jpg",
    "dumps3/1430_教金的面_raw.jpg",
    "dumps3/1682_教官的怀脊_raw.jpg",
    "dumps3/2097_重时_raw.jpg",
    "dumps4.0/1257_2_浊水的一_raw.jpg",
    "dumps4.0/6315_0__raw.jpg",
    "dumps4.0_tx/18_3_浊水的一_raw.jpg",
    "dumps4.0_tx/200_2_辉光棱_raw.jpg",
    "dumps4.0_tx/339_1_破损的面具_raw.jpg",
    "dumps4.0_tx/672_2_冒险家_raw.jpg",
    "dumps4.0_tx/684_1_破缺棱晶_raw.jpg",
    "dumps4.0_tx/762_2_七天神像_raw.jpg",
    "dumps4.0_tx/778_1_游医的_raw.jpg",
    "dumps4.0_tx/1086_2_调查_raw.jpg",
    "dumps4.0_tx/1771_3_教官的余心_raw.jpg",
    "dumps4.0_tx/1893_2_奇械机芯齿_raw.jpg",
    "dumps4.0_tx/2036_1_柔灯铃_raw.jpg",
    "dumps4.0_tx2/547_1_之_raw.jpg",
    "dumps4.0_tx3/357_1_官_raw.jpg",
    "dumps4.0_tx3/378_3_香云晶_raw.jpg",
    "dumps4.0_tx3/568_1_黑铜号角_raw.jpg",
    "dumps4.0_tx3/946_2_史莱姆凝液_raw.jpg",
    "dumps4.0_tx4/289_1_混云沌粉_raw.jpg",
    "dumps4.0_tx4/507_2_大英雄的_raw.jpg",
    "dumps4.0_tx6/136_2_墩_raw.jpg",
    "dumps4.0_tx5/386_2_混金鲈_raw.jpg",
    "dumps4.0_tx7/226_2_狂风蘑_raw.jpg",
    "dumps4.0_pph/23_3_光花蜜_raw.jpg",
    "dumps4.0_syfs/234_2_地脉的旧枝_raw.jpg",
    "dumps4.0_longx/935_2_奇械机芯齿船_raw.jpg",
    "dumps4.0_longx/1129_1_军结晶_raw.jpg",
    "dumps4.0_longx/1908_1_接兽的_raw.jpg",
    "dumps4.0_longx/2139_2_锲纹的_raw.jpg",
    "dumps/10756_raw.jpg",
    "text_dumps/34002_raw.jpg",
    "dumps4.0_tx/1131_2_冒险家金杯_raw.jpg",
    "dumps4.0_tx/1967_2_奇械机芯齿_raw.jpg",
    "dumps4.0_tx3/913_3_奇械机芯齿_raw.jpg",
    "dumps/16160_raw.jpg",
    "dumps4.0_tx/1055_2_查_raw.jpg",
    "dumps4.0_syfs/119_2_牢固的箭簇_raw.jpg",
    "text_dumps/9420_raw.jpg",
    "text_dumps/12630_raw.jpg",
    "dumps3/1411_教虚绘_raw.jpg",
    "dumps3/2262_胡萝卜_raw.jpg",
    "text_dumps/21099_raw.jpg",
    "dumps4.0_tx/159_2_浊水的一_raw.jpg",
    "dumps4.0_tx2/608_1_调_raw.jpg",
    "text_dumps/9360_raw.jpg",
    "text_dumps/14780_raw.jpg",
    "text_dumps/20968_raw.jpg",
    "dumps3/1164_破损的面具_raw.jpg",
    "dumps4.0/1252_2_浊水的一_raw.jpg",
    "dumps4.0_tx/39_3_隙间之核_raw.jpg",
    "text_dumps/925_raw.jpg",
    "dumps4.0_tx4/990_2_激活回响海螺_raw.jpg",
    "dumps4.0_tx3/484_4_督察长祭刀_raw.jpg",
    "dumps4.0/732_2_浊水的一掬_raw.jpg",
    "dumps4.0/1002_2_浊水的一_raw.jpg",
    "dumps4.0/1007_2_浊水的一_raw.jpg",
    "dumps4.0/1022_2_浊水的一_raw.jpg",
    "dumps4.0/1057_2_浊水的一掬_raw.jpg",
    "dumps4.0/1262_2_浊水的一_raw.jpg",
    "dumps4.0/1268_3_浊水的一_raw.jpg",
    "dumps4.0/1277_2_浊水的一_raw.jpg",
    "dumps4.0/1282_2_浊水的一_raw.jpg",
    "dumps4.0/1287_2_浊水的一_raw.jpg",
    "dumps4.0/1292_2_浊水的一_raw.jpg",
    "dumps4.0/1297_2_浊水的一_raw.jpg",
    "dumps4.0/1302_2_浊水的一滴_raw.jpg",
    "dumps4.0_tx/53_2_浊水的一废_raw.jpg",
    "dumps4.0_tx/56_2_浊水的一_raw.jpg",
    "dumps4.0_tx/57_2_浊水的一_raw.jpg",
    "dumps4.0_tx/60_2_浊水的一滴_raw.jpg",
    "dumps4.0_tx/67_2_浊水的一_raw.jpg",
    "dumps4.0_tx/70_2_浊水的一_raw.jpg",
    "dumps4.0_tx/85_2_浊水的一_raw.jpg",
    "dumps4.0_tx/86_2_浊水的一_raw.jpg",
    "dumps4.0_tx/87_2_浊水的一_raw.jpg",
    "dumps4.0_tx/88_2_浊水的一_raw.jpg",
    "dumps4.0_tx/89_2_浊水的一片_raw.jpg",
    "dumps4.0_tx/154_2_浊水的一_raw.jpg",
    "dumps4.0/1012_2_浊水的一滴_raw.jpg",
    "dumps4.0/1223_3_浊水的一_raw.jpg",
    "dumps4.0/1232_2_浊水的一滴_raw.jpg",
    "dumps4.0/1247_2_浊水的一_raw.jpg",
    "dumps4.0/1250_0_浊水的一_raw.jpg",
    "dumps4.0_tx/65_0_浊水的一_raw.jpg",
    "dumps4.0_tx/1799_3_浊水的一_raw.jpg",
    "text_dumps/3818_raw.jpg",
    "dumps4.0_longx/969_1_寻生轮_raw.jpg",
    "dumps/31_raw.jpg",
    "dumps/6655_raw.jpg",
    "text_dumps/3818_raw.jpg",
    "dumps3/476_微_raw.jpg",
    "dumps4.0_tx2/102_3_混沌装置_raw.jpg",
    "dumps4.0_tx7/291_2_花_raw.jpg",
    "dumps4.0_longx/969_1_寻生轮_raw.jpg",
    "dumps/573_raw.jpg",
    "dumps/6518_raw.jpg",
    "dumps/6735_raw.jpg",
    "dumps/9396_raw.jpg",
    "dumps/9398_raw.jpg",
    "dumps/9419_raw.jpg",
    "dumps/9496_raw.jpg",
    "dumps/9510_raw.jpg",
    "dumps/9511_raw.jpg",
    "dumps/13003_raw.jpg",
    "dumps/13563_raw.jpg",
    "dumps/18204_raw.jpg",
    "text_dumps/8795_raw.jpg",
    "text_dumps/15472_raw.jpg",
    "text_dumps/23342_raw.jpg",
    "dumps3/75_魔晶花_raw.jpg",
    "dumps3/377_导能绘卷_raw.jpg",
    "dumps3/1729_混沌菌核_raw.jpg",
    "dumps4.0_tx/1758_2_天活菌核_raw.jpg",
    "dumps4.0_tx/1801_2_浊水的一_raw.jpg",
    "dumps4.0_tx3/415_4_饪_raw.jpg",
    "dumps4.0_tx3/965_0_史莱姆浆_raw.jpg",
    "dumps4.0_tx4/327_2_精致的宝箱_raw.jpg",
    "dumps4.0_yjls/56_3_混沌纽块_raw.jpg", 
    "dumps/3185_raw.jpg",
    "dumps/10807_raw.jpg",
    "dumps/11165_raw.jpg",
    "dumps/11205_raw.jpg",
    "dumps/14362_raw.jpg",
    "dumps/14751_raw.jpg",
    "dumps/18429_raw.jpg",
    "dumps/18472_raw.jpg",
    "dumps/19235_raw.jpg",
    "text_dumps/140_raw.jpg",
    "text_dumps/1397_raw.jpg",
    "text_dumps/1801_raw.jpg",
    "text_dumps/2247_raw.jpg",
    "text_dumps/5735_raw.jpg",
    "text_dumps/5736_raw.jpg",
    "text_dumps/7121_raw.jpg",
    "text_dumps/8114_raw.jpg",
    "text_dumps/11268_raw.jpg",
    "text_dumps/13228_raw.jpg",
    "text_dumps/13872_raw.jpg",
    "text_dumps/13985_raw.jpg",
    "text_dumps/15685_raw.jpg",
    "text_dumps/19299_raw.jpg",
    "text_dumps/20098_raw.jpg",
    "text_dumps/20616_raw.jpg",
    "text_dumps/21348_raw.jpg",
    "text_dumps/22269_raw.jpg",
    "text_dumps/24351_raw.jpg",
    "text_dumps/26114_raw.jpg",
    "text_dumps/30603_raw.jpg",
    "text_dumps/33806_raw.jpg",
    "dumps3/223_雾肉_raw.jpg",
    "dumps3/263_苹果_raw.jpg",
    "dumps3/1264_残脉的旧枝_raw.jpg",
    "dumps3/2093_来自处_raw.jpg",
    "dumps4.0/22_2__raw.jpg",
    "dumps4.0/2287_2__raw.jpg",
    "dumps4.0_tx/40_2_隙间之核_raw.jpg",
    "dumps4.0_tx/526_2_精致的宝箱_raw.jpg",
    "dumps4.0_tx/829_2_幸运儿绿冠_raw.jpg",
    "dumps4.0_tx/1088_3_白铁块_raw.jpg",
    "dumps4.0_tx/1202_3_虚灯芯之_raw.jpg",
    "dumps4.0_tx/1467_2_污秽的面具_raw.jpg",
    "dumps4.0_tx/1515_3_黑晶号角_raw.jpg",
    "dumps4.0_tx/1542_2_苹果_raw.jpg",
    "dumps4.0_tx/1572_4_墩_raw.jpg",
    "dumps4.0_tx/1706_2_珍藏之花_raw.jpg",
    "dumps4.0_tx/1736_2_何人所珍藏之花_raw.jpg",
    "dumps4.0_tx/1948_1_战狂的鬼面_raw.jpg",
    "dumps4.0_tx/2055_1_兽肉_raw.jpg",
    "dumps4.0_tx/2063_2_芒性能量块_raw.jpg",
    "dumps4.0_tx2/5_2_史莱姆清_raw.jpg",
    "dumps4.0_tx3/177_2_混沌回路_raw.jpg",
    "dumps4.0_tx3/599_2_金鱼草芯_raw.jpg",
    "dumps4.0_tx3/691_4_须弥面具_raw.jpg",
    "dumps4.0_tx3/824_2_蓝角蜥_raw.jpg",
    "dumps4.0_tx3/977_1_奇械机芯齿轮_raw.jpg",
    "dumps4.0_tx4/946_3_士官的徽记_raw.jpg",
    "dumps4.0_tx5/232_3_荧光孢粉_raw.jpg",
    "dumps4.0_tx5/247_2_焰_raw.jpg",
    "dumps4.0_tx5/293_2_混沌枢纽_raw.jpg",
    "dumps4.0_tx5/308_2_召唤草种子_raw.jpg",
    "dumps4.0_tx6/234_2_须弥蔷薇_raw.jpg",
    "dumps4.0_tx7/8_2_幽灯蕈_raw.jpg",
    "dumps4.0_tx7/52_2_幽灯蕈_raw.jpg",
    "dumps4.0_tx7/58_2_琉百号_raw.jpg",
    "dumps4.0_tx7/84_2_铁焱_raw.jpg",
    "dumps4.0_tx7/91_2_洛心_raw.jpg",
    "dumps4.0_tx7/447_2_泡泡铃_raw.jpg",
    "dumps4.0_tx7/460_2_泡泡桔_raw.jpg",
    "dumps4.0_tx7/538_2_鬼兜虫_raw.jpg",
    "dumps4.0_xs/24_4_蕈兽孢子_raw.jpg",
    "dumps4.0_xs/35_3_孢囊晶尘_raw.jpg",
    "dumps4.0_xs/87_3_荧光孢粉_raw.jpg",
    "dumps4.0_xs/98_3_荧光孢粉_raw.jpg",
    "dumps4.0_xs/140_2_苹果_raw.jpg",
    "dumps4.0_xs/153_2_月莲_raw.jpg",
    "dumps4.0_yjls/23_3_混沌容器_raw.jpg",
    "dumps4.0_yjls/33_4_水晶块_raw.jpg",
    "dumps4.0_yjls/39_4_混沌锚栓_raw.jpg",
    "dumps4.0_yjls/108_2_枣椰_raw.jpg",
    "dumps4.0_longx/306_2_地脉的枯叶_raw.jpg",
    "dumps4.0_longx/397_3_带_raw.jpg",
    "dumps4.0_longx/712_3_浊水的水_raw.jpg",
    "dumps4.0_longx3/390_2_帕蒂沙兰_raw.jpg",
    "dumps4.0_longx3/542_2_启动_raw.jpg",
    'dumps4.0_longx3/599_2_游医的怀钟_raw.jpg',
    'dumps4.0_longx3/235_2_蓝鳍鲈鱼_raw.jpg', 
'dumps4.0_longx/1630_3_督察长祭刀_raw.jpg',
'dumps4.0_longx/1596_1_污的_raw.jpg',
'dumps4.0_longx/1066_3_初的浊水_raw.jpg',
'dumps4.0_longx/834_2_安_raw.jpg',
'dumps4.0_longx/441_0_地脉的枝_raw.jpg',
'dumps4.0_yjls/14_2_混沌模块_raw.jpg',
'dumps4.0_pph/38_4_骗骗花蜜_raw.jpg',
'dumps4.0_pph/1_3_原素花蜜_raw.jpg',
'dumps4.0_tx7/426_2_柔灯_raw.jpg',
'dumps4.0_tx7/252_2_烹饪_raw.jpg',
'dumps4.0_tx7/241_3_胡萝卜_raw.jpg',
'dumps4.0_tx6/181_1_岩弥沌森_raw.jpg',
'dumps4.0_tx4/1081_3_沉重号角_raw.jpg',
'dumps4.0_tx4/1050_2_开世突触_raw.jpg',
'dumps4.0_tx4/1011_2_汐藻_raw.jpg',
'dumps4.0_tx4/455_2_牢固的箭簇_raw.jpg',
'dumps4.0_tx4/267_0_久雨莲_raw.jpg',
'dumps4.0_tx3/401_2_饪_raw.jpg',
'dumps4.0_tx2/11_2_冒险家怀羽_raw.jpg',
'dumps4.0_tx/2066_2_合齿矿_raw.jpg',
'dumps4.0_tx/2062_2_芒性能量块_raw.jpg',
'dumps4.0_tx/1765_2_何人所珍藏之花_raw.jpg',
'dumps4.0_tx/1449_0_污秽的面具_raw.jpg',
'dumps4.0_tx/1017_2_幸运儿之杯_raw.jpg',
'dumps4.0_tx/696_2_阅读_raw.jpg',
'dumps4.0_tx/472_3_「正义」的教_raw.jpg',
'dumps4.0_tx/34_3_世_raw.jpg',
'dumps4.0/1334_4_幸运儿沙漏_raw.jpg',
'dumps4.0/1008_3__raw.jpg',
'dumps4.0/645_0__raw.jpg',
'dumps3/2070_损的珍具_raw.jpg',
'dumps3/2061_教损的箭表_raw.jpg',
'dumps3/255_史莱姆清_raw.jpg',
'text_dumps/28920_raw.jpg',
'text_dumps/27371_raw.jpg',
'text_dumps/26336_raw.jpg',
'text_dumps/24688_raw.jpg',
'text_dumps/24443_raw.jpg',
'text_dumps/24352_raw.jpg',
'text_dumps/22433_raw.jpg',
'text_dumps/18840_raw.jpg',
'text_dumps/15985_raw.jpg',
'text_dumps/13984_raw.jpg',
'text_dumps/9058_raw.jpg',
'text_dumps/3541_raw.jpg',
'dumps/19328_raw.jpg',
'dumps/18807_raw.jpg',
'dumps/18089_raw.jpg',
'dumps/17241_raw.jpg',
'dumps/14923_raw.jpg',
'dumps/14750_raw.jpg',
'dumps/14715_raw.jpg',
'dumps/11705_raw.jpg',
'dumps/11467_raw.jpg',
'dumps/9950_raw.jpg',
'dumps/4849_raw.jpg',
'dumps/3941_raw.jpg',
'dumps/1890_raw.jpg',
'dumps4.0_longx/1590_3_蕈兽孢子_raw.jpg',
'dumps4.0_longx/384_2_地脉的时_raw.jpg',
'dumps4.0_yjls/1_3_香辛果_raw.jpg',
'dumps4.0_xs/59_2_艾孢子_raw.jpg',
'dumps4.0_pph/116_3_微光花蜜_raw.jpg',
'dumps4.0_tx7/431_2_柔灯铃_raw.jpg',
'dumps4.0_tx7/403_4_柔灯铃_raw.jpg',
'dumps4.0_tx6/210_3_墩绘_raw.jpg',
'dumps4.0_tx5/321_2_香辛果_raw.jpg',
'dumps4.0_tx3/996_3_芬凝晶_raw.jpg',
'dumps4.0_tx3/937_2_洁草_raw.jpg',
'dumps4.0_tx3/648_2_烈焰花_raw.jpg',
'dumps4.0_tx3/49_2_萤火虫_raw.jpg',
'dumps4.0_tx/818_2_冒险家_raw.jpg',
'dumps3/1431_教金的_raw.jpg',
'text_dumps/1039_raw.jpg',
'dumps/17946_raw.jpg',
'dumps/15004_raw.jpg',
'dumps/10943_raw.jpg',
'dumps/10754_raw.jpg',
'dumps/4820_raw.jpg',
'dumps/2126_raw.jpg',
'dumps/946_raw.jpg',
'dumps/2790_raw.jpg',
'text_dumps/1039_raw.jpg',
'dumps3/1163_破损的面具_raw.jpg',
'dumps3/1431_教金的_raw.jpg',
'dumps3/1459_日果_raw.jpg',
'dumps4.0_tx/258_2_奥特_raw.jpg',
'dumps4.0_tx3/690_3_黑尾_raw.jpg',
'dumps4.0_tx4/1127_2_破损的面具_raw.jpg',
'dumps4.0_tx5/368_2_混沌机块_raw.jpg',
'dumps4.0_longx/1446_4_的_raw.jpg',
'dumps4.0_longx3/452_2_幸运儿绿花_raw.jpg',
'text_dumps/24194_raw.jpg',
'dumps4.0_tx6/220_1_白铁块_raw.jpg',
'dumps4.0_syfs/160_2_不祥的面具_raw.jpg',
'dumps/219_raw.jpg',
'dumps/2599_raw.jpg',
'dumps/2879_raw.jpg',
'dumps/3757_raw.jpg',
'dumps/3930_raw.jpg',
'dumps/4291_raw.jpg',
'dumps/4473_raw.jpg',
'dumps/6200_raw.jpg',
'dumps/9407_raw.jpg',
'dumps/11042_raw.jpg',
'dumps/12540_raw.jpg',
'dumps/12547_raw.jpg',
'dumps/13558_raw.jpg',
'dumps/15006_raw.jpg',
'dumps/17626_raw.jpg',
'dumps/18384_raw.jpg',
'dumps/18487_raw.jpg',
'text_dumps/6342_raw.jpg',
'text_dumps/7028_raw.jpg',
'text_dumps/8442_raw.jpg',
'text_dumps/9377_raw.jpg',
'text_dumps/9687_raw.jpg',
'text_dumps/9895_raw.jpg',
'text_dumps/10716_raw.jpg',
'text_dumps/11054_raw.jpg',
'text_dumps/11236_raw.jpg',
'text_dumps/11570_raw.jpg',
'text_dumps/11806_raw.jpg',
'text_dumps/13983_raw.jpg',
'text_dumps/15169_raw.jpg',
'text_dumps/17797_raw.jpg',
'text_dumps/18761_raw.jpg',
'text_dumps/20020_raw.jpg',
'text_dumps/20795_raw.jpg',
'text_dumps/22460_raw.jpg',
'text_dumps/23337_raw.jpg',
'text_dumps/23744_raw.jpg',
'text_dumps/25283_raw.jpg',
'text_dumps/27104_raw.jpg',
'text_dumps/27924_raw.jpg',
'text_dumps/27963_raw.jpg',
'text_dumps/28858_raw.jpg',
'text_dumps/29859_raw.jpg',
'text_dumps/29905_raw.jpg',
'text_dumps/29906_raw.jpg',
'text_dumps/30590_raw.jpg',
'text_dumps/30791_raw.jpg',
'text_dumps/30802_raw.jpg',
'dumps3/380_自萝号面_raw.jpg',
'dumps3/1203_失_raw.jpg',
'dumps3/1238_卷心菜_raw.jpg',
'dumps3/1285_破官_raw.jpg',
'dumps3/1406_薄囊_raw.jpg',
'dumps3/1432_故人绘_raw.jpg',
'dumps3/1675_蛋_raw.jpg',
'dumps4.0/1972_2__raw.jpg',
'dumps4.0/5879_4__raw.jpg',
'dumps4.0_tx/408_3_的洛劳_raw.jpg',
'dumps4.0_tx/413_3_的_raw.jpg',
'dumps4.0_tx/828_2_调查_raw.jpg',
'dumps4.0_tx/945_2_调查_raw.jpg',
'dumps4.0_tx/946_2_游医的银莲_raw.jpg',
'dumps4.0_tx/964_3_尉官的徽记_raw.jpg',
'dumps4.0_tx/971_1_士官的徽记_raw.jpg',
'dumps4.0_tx/989_2_调查_raw.jpg',
'dumps4.0_tx/1008_3_冒险家怀表_raw.jpg',
'dumps4.0_tx/1056_2_调查_raw.jpg',
'dumps4.0_tx/1386_3_黑铜号角_raw.jpg',
'dumps4.0_tx/1674_2_灵花_raw.jpg',
'dumps4.0_tx3/110_3_化_raw.jpg',
'dumps4.0_tx4/103_2_烈焰花_raw.jpg',
'dumps4.0_tx4/187_1_性的_raw.jpg',
'dumps4.0_tx4/198_2_地脉的旧_raw.jpg',
'dumps4.0_tx4/406_2_茉洁草_raw.jpg',
'dumps4.0_tx4/983_2_激活回响海螺_raw.jpg',
'dumps4.0_tx4/996_2_苍晶螺_raw.jpg',
'dumps4.0_tx5/194_2_须弥蔷薇_raw.jpg',
'dumps4.0_tx5/210_3_香辛果_raw.jpg',
'dumps4.0_tx5/227_3_香辛果_raw.jpg',
'dumps4.0_tx6/187_2_失活菌核_raw.jpg',
'dumps4.0_tx7/361_1_灯_raw.jpg',
'dumps4.0_tx7/34_2_甜甜_raw.jpg',
'dumps4.0_tx7/79_2_霓裳花_raw.jpg',
'dumps4.0_tx7/86_2_琉璃百合_raw.jpg',
'dumps4.0_tx7/158_2_松果_raw.jpg',
'dumps4.0_tx7/162_2_铁块_raw.jpg',
'dumps4.0_tx7/249_2_慕风蘑菇_raw.jpg',
'dumps4.0_tx7/274_3_落号_raw.jpg',
'dumps4.0_tx7/461_2_茉洁草_raw.jpg',
'dumps4.0_tx7/525_2_薄荷_raw.jpg',
'dumps4.0_pph/2_4_骗骗花蜜_raw.jpg',
'dumps4.0_pph/52_1_微光花蜜_raw.jpg',
'dumps4.0_syfs/75_0_的旧_raw.jpg',
'dumps4.0_syfs/180_1_破损的面具_raw.jpg',
'dumps4.0_longx/118_2_古何的佣兵笔底_raw.jpg',
'dumps4.0_longx3/154_2_寻宝鸦印_raw.jpg',
'dumps4.0_longx3/619_2_冒险家之花_raw.jpg',
'dumps/1011_raw.jpg',
'dumps/1752_raw.jpg',
'dumps/2926_raw.jpg',
'dumps/3308_raw.jpg',
'dumps/3443_raw.jpg',
'dumps/4622_raw.jpg',
'dumps/6213_raw.jpg',
'dumps/7050_raw.jpg',
'dumps/8257_raw.jpg',
'dumps/9362_raw.jpg',
'dumps/9826_raw.jpg',
'dumps/10813_raw.jpg',
'dumps/12356_raw.jpg',
'dumps/12395_raw.jpg',
'dumps/12531_raw.jpg',
'dumps/12870_raw.jpg', 
'dumps/15319_raw.jpg',
'dumps/16058_raw.jpg',
'dumps/17207_raw.jpg',
'dumps/17525_raw.jpg',
'dumps/17720_raw.jpg',
'dumps/18285_raw.jpg',
'dumps/18998_raw.jpg',
'dumps/19283_raw.jpg',
'dumps/19556_raw.jpg',
'text_dumps/145_raw.jpg',
'text_dumps/2414_raw.jpg',
'text_dumps/3604_raw.jpg',
'text_dumps/4225_raw.jpg',
'text_dumps/4635_raw.jpg',
'text_dumps/7746_raw.jpg',
'text_dumps/20595_raw.jpg',
'text_dumps/20978_raw.jpg',
'text_dumps/21670_raw.jpg',
'text_dumps/21933_raw.jpg',
'dumps/25_raw.jpg',
'dumps/1009_raw.jpg',
'dumps/2426_raw.jpg',
'dumps/4578_raw.jpg',
'dumps/6609_raw.jpg',
'dumps/6691_raw.jpg',
'dumps/8251_raw.jpg',
'dumps/9668_raw.jpg',
'dumps/11451_raw.jpg',
'dumps/12382_raw.jpg',
'dumps/14349_raw.jpg',
'dumps/14459_raw.jpg',
'dumps/14970_raw.jpg',
'dumps/17614_raw.jpg',
'dumps/18006_raw.jpg',
'dumps/18273_raw.jpg',
'dumps/19286_raw.jpg',
'text_dumps/881_raw.jpg',
'text_dumps/888_raw.jpg',
'text_dumps/3767_raw.jpg',
'text_dumps/7236_raw.jpg',
'text_dumps/7814_raw.jpg',
'text_dumps/9144_raw.jpg',
'text_dumps/13820_raw.jpg',
'text_dumps/14239_raw.jpg',
'text_dumps/14515_raw.jpg',
'text_dumps/20585_raw.jpg',
'text_dumps/20956_raw.jpg',
'text_dumps/22833_raw.jpg',
'text_dumps/22926_raw.jpg',
'text_dumps/24175_raw.jpg',
'text_dumps/24438_raw.jpg',
'text_dumps/24758_raw.jpg',
'text_dumps/24872_raw.jpg',
'text_dumps/25411_raw.jpg',
'text_dumps/25558_raw.jpg',
'text_dumps/26836_raw.jpg',
'text_dumps/32047_raw.jpg',
'text_dumps/33811_raw.jpg',
'dumps3/368_蕈兽孢子_raw.jpg',
'dumps3/1755_教的怀_raw.jpg',
'dumps3/2145_破兽爪_raw.jpg',
'dumps3/2221_兽肉_raw.jpg',
'dumps3/2331_薄蛋_raw.jpg',
'dumps4.0_tx/359_4_沉重号角_raw.jpg',
'dumps4.0_tx/517_2_异海凝珠_raw.jpg',
'dumps4.0_tx/518_2_异海之块_raw.jpg',
'dumps4.0_tx/995_2_调查_raw.jpg',
'dumps4.0_tx/1012_2_幸运儿绿花_raw.jpg',
'dumps4.0_tx/1029_2_幸运儿之杯_raw.jpg',
])
