__author__ = 'Jia'

# Two Sum
# Given an array of integers, find two numbers such that they add up to a specific target number.
# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be
# less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
# You may assume that each input would have exactly one solution.
# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2
class Solution:
    def twoSum(self, numbers, target):
        m = {}
        for i in range(1, len(numbers) + 1):
            if (target - numbers[i - 1]) in m:
                return [m[target - numbers[i - 1]], i]
            else:
                m[numbers[i - 1]] = i
        return [-1, -1]


s = Solution()
import datetime
t = datetime.datetime.now()
print s.twoSum([0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,104,106,108,110,112,114,116,118,120,122,124,126,128,130,132,134,136,138,140,142,144,146,148,150,152,154,156,158,160,162,164,166,168,170,172,174,176,178,180,182,184,186,188,190,192,194,196,198,200,202,204,206,208,210,212,214,216,218,220,222,224,226,228,230,232,234,236,238,240,242,244,246,248,250,252,254,256,258,260,262,264,266,268,270,272,274,276,278,280,282,284,286,288,290,292,294,296,298,300,302,304,306,308,310,312,314,316,318,320,322,324,326,328,330,332,334,336,338,340,342,344,346,348,350,352,354,356,358,360,362,364,366,368,370,372,374,376,378,380,382,384,386,388,390,392,394,396,398,400,402,404,406,408,410,412,414,416,418,420,422,424,426,428,430,432,434,436,438,440,442,444,446,448,450,452,454,456,458,460,462,464,466,468,470,472,474,476,478,480,482,484,486,488,490,492,494,496,498,500,502,504,506,508,510,512,514,516,518,520,522,524,526,528,530,532,534,536,538,540,542,544,546,548,550,552,554,556,558,560,562,564,566,568,570,572,574,576,578,580,582,584,586,588,590,592,594,596,598,600,602,604,606,608,610,612,614,616,618,620,622,624,626,628,630,632,634,636,638,640,642,644,646,648,650,652,654,656,658,660,662,664,666,668,670,672,674,676,678,680,682,684,686,688,690,692,694,696,698,700,702,704,706,708,710,712,714,716,718,720,722,724,726,728,730,732,734,736,738,740,742,744,746,748,750,752,754,756,758,760,762,764,766,768,770,772,774,776,778,780,782,784,786,788,790,792,794,796,798,800,802,804,806,808,810,812,814,816,818,820,822,824,826,828,830,832,834,836,838,840,842,844,846,848,850,852,854,856,858,860,862,864,866,868,870,872,874,876,878,880,882,884,886,888,890,892,894,896,898,900,902,904,906,908,910,912,914,916,918,920,922,924,926,928,930,932,934,936,938,940,942,944,946,948,950,952,954,956,958,960,962,964,966,968,970,972,974,976,978,980,982,984,986,988,990,992,994,996,998,1000,1002,1004,1006,1008,1010,1012,1014,1016,1018,1020,1022,1024,1026,1028,1030,1032,1034,1036,1038,1040,1042,1044,1046,1048,1050,1052,1054,1056,1058,1060,1062,1064,1066,1068,1070,1072,1074,1076,1078,1080,1082,1084,1086,1088,1090,1092,1094,1096,1098,1100,1102,1104,1106,1108,1110,1112,1114,1116,1118,1120,1122,1124,1126,1128,1130,1132,1134,1136,1138,1140,1142,1144,1146,1148,1150,1152,1154,1156,1158,1160,1162,1164,1166,1168,1170,1172,1174,1176,1178,1180,1182,1184,1186,1188,1190,1192,1194,1196,1198,1200,1202,1204,1206,1208,1210,1212,1214,1216,1218,1220,1222,1224,1226,1228,1230,1232,1234,1236,1238,1240,1242,1244,1246,1248,1250,1252,1254,1256,1258,1260,1262,1264,1266,1268,1270,1272,1274,1276,1278,1280,1282,1284,1286,1288,1290,1292,1294,1296,1298,1300,1302,1304,1306,1308,1310,1312,1314,1316,1318,1320,1322,1324,1326,1328,1330,1332,1334,1336,1338,1340,1342,1344,1346,1348,1350,1352,1354,1356,1358,1360,1362,1364,1366,1368,1370,1372,1374,1376,1378,1380,1382,1384,1386,1388,1390,1392,1394,1396,1398,1400,1402,1404,1406,1408,1410,1412,1414,1416,1418,1420,1422,1424,1426,1428,1430,1432,1434,1436,1438,1440,1442,1444,1446,1448,1450,1452,1454,1456,1458,1460,1462,1464,1466,1468,1470,1472,1474,1476,1478,1480,1482,1484,1486,1488,1490,1492,1494,1496,1498,1500,1502,1504,1506,1508,1510,1512,1514,1516,1518,1520,1522,1524,1526,1528,1530,1532,1534,1536,1538,1540,1542,1544,1546,1548,1550,1552,1554,1556,1558,1560,1562,1564,1566,1568,1570,1572,1574,1576,1578,1580,1582,1584,1586,1588,1590,1592,1594,1596,1598,1600,1602,1604,1606,1608,1610,1612,1614,1616,1618,1620,1622,1624,1626,1628,1630,1632,1634,1636,1638,1640,1642,1644,1646,1648,1650,1652,1654,1656,1658,1660,1662,1664,1666,1668,1670,1672,1674,1676,1678,1680,1682,1684,1686,1688,1690,1692,1694,1696,1698,1700,1702,1704,1706,1708,1710,1712,1714,1716,1718,1720,1722,1724,1726,1728,1730,1732,1734,1736,1738,1740,1742,1744,1746,1748,1750,1752,1754,1756,1758,1760,1762,1764,1766,1768,1770,1772,1774,1776,1778,1780,1782,1784,1786,1788,1790,1792,1794,1796,1798,1800,1802,1804,1806,1808,1810,1812,1814,1816,1818,1820,1822,1824,1826,1828,1830,1832,1834,1836,1838,1840,1842,1844,1846,1848,1850,1852,1854,1856,1858,1860,1862,1864,1866,1868,1870,1872,1874,1876,1878,1880,1882,1884,1886,1888,1890,1892,1894,1896,1898,1900,1902,1904,1906,1908,1910,1912,1914,1916,1918,1920,1922,1924,1926,1928,1930,1932,1934,1936,1938,1940,1942,1944,1946,1948,1950,1952,1954,1956,1958,1960,1962,1964,1966,1968,1970,1972,1974,1976,1978,1980,1982,1984,1986,1988,1990,1992,1994,1996,1998,2000,2002,2004,2006,2008,2010,2012,2014,2016,2018,2020,2022,2024,2026,2028,2030,2032,2034,2036,2038,2040,2042,2044,2046,2048,2050,2052,2054,2056,2058,2060,2062,2064,2066,2068,2070,2072,2074,2076,2078,2080,2082,2084,2086,2088,2090,2092,2094,2096,2098,2100,2102,2104,2106,2108,2110,2112,2114,2116,2118,2120,2122,2124,2126,2128,2130,2132,2134,2136,2138,2140,2142,2144,2146,2148,2150,2152,2154,2156,2158,2160,2162,2164,2166,2168,2170,2172,2174,2176,2178,2180,2182,2184,2186,2188,2190,2192,2194,2196,2198,2200,2202,2204,2206,2208,2210,2212,2214,2216,2218,2220,2222,2224,2226,2228,2230,2232,2234,2236,2238,2240,2242,2244,2246,2248,2250,2252,2254,2256,2258,2260,2262,2264,2266,2268,2270,2272,2274,2276,2278,2280,2282,2284,2286,2288,2290,2292,2294,2296,2298,2300,2302,2304,2306,2308,2310,2312,2314,2316,2318,2320,2322,2324,2326,2328,2330,2332,2334,2336,2338,2340,2342,2344,2346,2348,2350,2352,2354,2356,2358,2360,2362,2364,2366,2368,2370,2372,2374,2376,2378,2380,2382,2384,2386,2388,2390,2392,2394,2396,2398,2400,2402,2404,2406,2408,2410,2412,2414,2416,2418,2420,2422,2424,2426,2428,2430,2432,2434,2436,2438,2440,2442,2444,2446,2448,2450,2452,2454,2456,2458,2460,2462,2464,2466,2468,2470,2472,2474,2476,2478,2480,2482,2484,2486,2488,2490,2492,2494,2496,2498,2500,2502,2504,2506,2508,2510,2512,2514,2516,2518,2520,2522,2524,2526,2528,2530,2532,2534,2536,2538,2540,2542,2544,2546,2548,2550,2552,2554,2556,2558,2560,2562,2564,2566,2568,2570,2572,2574,2576,2578,2580,2582,2584,2586,2588,2590,2592,2594,2596,2598,2600,2602,2604,2606,2608,2610,2612,2614,2616,2618,2620,2622,2624,2626,2628,2630,2632,2634,2636,2638,2640,2642,2644,2646,2648,2650,2652,2654,2656,2658,2660,2662,2664,2666,2668,2670,2672,2674,2676,2678,2680,2682,2684,2686,2688,2690,2692,2694,2696,2698,2700,2702,2704,2706,2708,2710,2712,2714,2716,2718,2720,2722,2724,2726,2728,2730,2732,2734,2736,2738,2740,2742,2744,2746,2748,2750,2752,2754,2756,2758,2760,2762,2764,2766,2768,2770,2772,2774,2776,2778,2780,2782,2784,2786,2788,2790,2792,2794,2796,2798,2800,2802,2804,2806,2808,2810,2812,2814,2816,2818,2820,2822,2824,2826,2828,2830,2832,2834,2836,2838,2840,2842,2844,2846,2848,2850,2852,2854,2856,2858,2860,2862,2864,2866,2868,2870,2872,2874,2876,2878,2880,2882,2884,2886,2888,2890,2892,2894,2896,2898,2900,2902,2904,2906,2908,2910,2912,2914,2916,2918,2920,2922,2924,2926,2928,2930,2932,2934,2936,2938,2940,2942,2944,2946,2948,2950,2952,2954,2956,2958,2960,2962,2964,2966,2968,2970,2972,2974,2976,2978,2980,2982,2984,2986,2988,2990,2992,2994,2996,2998,3000,3002,3004,3006,3008,3010,3012,3014,3016,3018,3020,3022,3024,3026,3028,3030,3032,3034,3036,3038,3040,3042,3044,3046,3048,3050,3052,3054,3056,3058,3060,3062,3064,3066,3068,3070,3072,3074,3076,3078,3080,3082,3084,3086,3088,3090,3092,3094,3096,3098,3100,3102,3104,3106,3108,3110,3112,3114,3116,3118,3120,3122,3124,3126,3128,3130,3132,3134,3136,3138,3140,3142,3144,3146,3148,3150,3152,3154,3156,3158,3160,3162,3164,3166,3168,3170,3172,3174,3176,3178,3180,3182,3184,3186,3188,3190,3192,3194,3196,3198,3200,3202,3204,3206,3208,3210,3212,3214,3216,3218,3220,3222,3224,3226,3228,3230,3232,3234,3236,3238,3240,3242,3244,3246,3248,3250,3252,3254,3256,3258,3260,3262,3264,3266,3268,3270,3272,3274,3276,3278,3280,3282,3284,3286,3288,3290,3292,3294,3296,3298,3300,3302,3304,3306,3308,3310,3312,3314,3316,3318,3320,3322,3324,3326,3328,3330,3332,3334,3336,3338,3340,3342,3344,3346,3348,3350,3352,3354,3356,3358,3360,3362,3364,3366,3368,3370,3372,3374,3376,3378,3380,3382,3384,3386,3388,3390,3392,3394,3396,3398,3400,3402,3404,3406,3408,3410,3412,3414,3416,3418,3420,3422,3424,3426,3428,3430,3432,3434,3436,3438,3440,3442,3444,3446,3448,3450,3452,3454,3456,3458,3460,3462,3464,3466,3468,3470,3472,3474,3476,3478,3480,3482,3484,3486,3488,3490,3492,3494,3496,3498,3500,3502,3504,3506,3508,3510,3512,3514,3516,3518,3520,3522,3524,3526,3528,3530,3532,3534,3536,3538,3540,3542,3544,3546,3548,3550,3552,3554,3556,3558,3560,3562,3564,3566,3568,3570,3572,3574,3576,3578,3580,3582,3584,3586,3588,3590,3592,3594,3596,3598,3600,3602,3604,3606,3608,3610,3612,3614,3616,3618,3620,3622,3624,3626,3628,3630,3632,3634,3636,3638,3640,3642,3644,3646,3648,3650,3652,3654,3656,3658,3660,3662,3664,3666,3668,3670,3672,3674,3676,3678,3680,3682,3684,3686,3688,3690,3692,3694,3696,3698,3700,3702,3704,3706,3708,3710,3712,3714,3716,3718,3720,3722,3724,3726,3728,3730,3732,3734,3736,3738,3740,3742,3744,3746,3748,3750,3752,3754,3756,3758,3760,3762,3764,3766,3768,3770,3772,3774,3776,3778,3780,3782,3784,3786,3788,3790,3792,3794,3796,3798,3800,3802,3804,3806,3808,3810,3812,3814,3816,3818,3820,3822,3824,3826,3828,3830,3832,3834,3836,3838,3840,3842,3844,3846,3848,3850,3852,3854,3856,3858,3860,3862,3864,3866,3868,3870,3872,3874,3876,3878,3880,3882,3884,3886,3888,3890,3892,3894,3896,3898,3900,3902,3904,3906,3908,3910,3912,3914,3916,3918,3920,3922,3924,3926,3928,3930,3932,3934,3936,3938,3940,3942,3944,3946,3948,3950,3952,3954,3956,3958,3960,3962,3964,3966,3968,3970,3972,3974,3976,3978,3980,3982,3984,3986,3988,3990,3992,3994,3996,3998,4000,4002,4004,4006,4008,4010,4012,4014,4016,4018,4020,4022,4024,4026,4028,4030,4032,4034,4036,4038,4040,4042,4044,4046,4048,4050,4052,4054,4056,4058,4060,4062,4064,4066,4068,4070,4072,4074,4076,4078,4080,4082,4084,4086,4088,4090,4092,4094,4096,4098,4100,4102,4104,4106,4108,4110,4112,4114,4116,4118,4120,4122,4124,4126,4128,4130,4132,4134,4136,4138,4140,4142,4144,4146,4148,4150,4152,4154,4156,4158,4160,4162,4164,4166,4168,4170,4172,4174,4176,4178,4180,4182,4184,4186,4188,4190,4192,4194,4196,4198,4200,4202,4204,4206,4208,4210,4212,4214,4216,4218,4220,4222,4224,4226,4228,4230,4232,4234,4236,4238,4240,4242,4244,4246,4248,4250,4252,4254,4256,4258,4260,4262,4264,4266,4268,4270,4272,4274,4276,4278,4280,4282,4284,4286,4288,4290,4292,4294,4296,4298,4300,4302,4304,4306,4308,4310,4312,4314,4316,4318,4320,4322,4324,4326,4328,4330,4332,4334,4336,4338,4340,4342,4344,4346,4348,4350,4352,4354,4356,4358,4360,4362,4364,4366,4368,4370,4372,4374,4376,4378,4380,4382,4384,4386,4388,4390,4392,4394,4396,4398,4400,4402,4404,4406,4408,4410,4412,4414,4416,4418,4420,4422,4424,4426,4428,4430,4432,4434,4436,4438,4440,4442,4444,4446,4448,4450,4452,4454,4456,4458,4460,4462,4464,4466,4468,4470,4472,4474,4476,4478,4480,4482,4484,4486,4488,4490,4492,4494,4496,4498,4500,4502,4504,4506,4508,4510,4512,4514,4516,4518,4520,4522,4524,4526,4528,4530,4532,4534,4536,4538,4540,4542,4544,4546,4548,4550,4552,4554,4556,4558,4560,4562,4564,4566,4568,4570,4572,4574,4576,4578,4580,4582,4584,4586,4588,4590,4592,4594,4596,4598,4600,4602,4604,4606,4608,4610,4612,4614,4616,4618,4620,4622,4624,4626,4628,4630,4632,4634,4636,4638,4640,4642,4644,4646,4648,4650,4652,4654,4656,4658,4660,4662,4664,4666,4668,4670,4672,4674,4676,4678,4680,4682,4684,4686,4688,4690,4692,4694,4696,4698,4700,4702,4704,4706,4708,4710,4712,4714,4716,4718,4720,4722,4724,4726,4728,4730,4732,4734,4736,4738,4740,4742,4744,4746,4748,4750,4752,4754,4756,4758,4760,4762,4764,4766,4768,4770,4772,4774,4776,4778,4780,4782,4784,4786,4788,4790,4792,4794,4796,4798,4800,4802,4804,4806,4808,4810,4812,4814,4816,4818,4820,4822,4824,4826,4828,4830,4832,4834,4836,4838,4840,4842,4844,4846,4848,4850,4852,4854,4856,4858,4860,4862,4864,4866,4868,4870,4872,4874,4876,4878,4880,4882,4884,4886,4888,4890,4892,4894,4896,4898,4900,4902,4904,4906,4908,4910,4912,4914,4916,4918,4920,4922,4924,4926,4928,4930,4932,4934,4936,4938,4940,4942,4944,4946,4948,4950,4952,4954,4956,4958,4960,4962,4964,4966,4968,4970,4972,4974,4976,4978,4980,4982,4984,4986,4988,4990,4992,4994,4996,4998,5000,5002,5004,5006,5008,5010,5012,5014,5016,5018,5020,5022,5024,5026,5028,5030,5032,5034,5036,5038,5040,5042,5044,5046,5048,5050,5052,5054,5056,5058,5060,5062,5064,5066,5068,5070,5072,5074,5076,5078,5080,5082,5084,5086,5088,5090,5092,5094,5096,5098,5100,5102,5104,5106,5108,5110,5112,5114,5116,5118,5120,5122,5124,5126,5128,5130,5132,5134,5136,5138,5140,5142,5144,5146,5148,5150,5152,5154,5156,5158,5160,5162,5164,5166,5168,5170,5172,5174,5176,5178,5180,5182,5184,5186,5188,5190,5192,5194,5196,5198,5200,5202,5204,5206,5208,5210,5212,5214,5216,5218,5220,5222,5224,5226,5228,5230,5232,5234,5236,5238,5240,5242,5244,5246,5248,5250,5252,5254,5256,5258,5260,5262,5264,5266,5268,5270,5272,5274,5276,5278,5280,5282,5284,5286,5288,5290,5292,5294,5296,5298,5300,5302,5304,5306,5308,5310,5312,5314,5316,5318,5320,5322,5324,5326,5328,5330,5332,5334,5336,5338,5340,5342,5344,5346,5348,5350,5352,5354,5356,5358,5360,5362,5364,5366,5368,5370,5372,5374,5376,5378,5380,5382,5384,5386,5388,5390,5392,5394,5396,5398,5400,5402,5404,5406,5408,5410,5412,5414,5416,5418,5420,5422,5424,5426,5428,5430,5432,5434,5436,5438,5440,5442,5444,5446,5448,5450,5452,5454,5456,5458,5460,5462,5464,5466,5468,5470,5472,5474,5476,5478,5480,5482,5484,5486,5488,5490,5492,5494,5496,5498,5500,5502,5504,5506,5508,5510,5512,5514,5516,5518,5520,5522,5524,5526,5528,5530,5532,5534,5536,5538,5540,5542,5544,5546,5548,5550,5552,5554,5556,5558,5560,5562,5564,5566,5568,5570,5572,5574,5576,5578,5580,5582,5584,5586,5588,5590,5592,5594,5596,5598,5600,5602,5604,5606,5608,5610,5612,5614,5616,5618,5620,5622,5624,5626,5628,5630,5632,5634,5636,5638,5640,5642,5644,5646,5648,5650,5652,5654,5656,5658,5660,5662,5664,5666,5668,5670,5672,5674,5676,5678,5680,5682,5684,5686,5688,5690,5692,5694,5696,5698,5700,5702,5704,5706,5708,5710,5712,5714,5716,5718,5720,5722,5724,5726,5728,5730,5732,5734,5736,5738,5740,5742,5744,5746,5748,5750,5752,5754,5756,5758,5760,5762,5764,5766,5768,5770,5772,5774,5776,5778,5780,5782,5784,5786,5788,5790,5792,5794,5796,5798,5800,5802,5804,5806,5808,5810,5812,5814,5816,5818,5820,5822,5824,5826,5828,5830,5832,5834,5836,5838,5840,5842,5844,5846,5848,5850,5852,5854,5856,5858,5860,5862,5864,5866,5868,5870,5872,5874,5876,5878,5880,5882,5884,5886,5888,5890,5892,5894,5896,5898,5900,5902,5904,5906,5908,5910,5912,5914,5916,5918,5920,5922,5924,5926,5928,5930,5932,5934,5936,5938,5940,5942,5944,5946,5948,5950,5952,5954,5956,5958,5960,5962,5964,5966,5968,5970,5972,5974,5976,5978,5980,5982,5984,5986,5988,5990,5992,5994,5996,5998,6000,6002,6004,6006,6008,6010,6012,6014,6016,6018,6020,6022,6024,6026,6028,6030,6032,6034,6036,6038,6040,6042,6044,6046,6048,6050,6052,6054,6056,6058,6060,6062,6064,6066,6068,6070,6072,6074,6076,6078,6080,6082,6084,6086,6088,6090,6092,6094,6096,6098,6100,6102,6104,6106,6108,6110,6112,6114,6116,6118,6120,6122,6124,6126,6128,6130,6132,6134,6136,6138,6140,6142,6144,6146,6148,6150,6152,6154,6156,6158,6160,6162,6164,6166,6168,6170,6172,6174,6176,6178,6180,6182,6184,6186,6188,6190,6192,6194,6196,6198,6200,6202,6204,6206,6208,6210,6212,6214,6216,6218,6220,6222,6224,6226,6228,6230,6232,6234,6236,6238,6240,6242,6244,6246,6248,6250,6252,6254,6256,6258,6260,6262,6264,6266,6268,6270,6272,6274,6276,6278,6280,6282,6284,6286,6288,6290,6292,6294,6296,6298,6300,6302,6304,6306,6308,6310,6312,6314,6316,6318,6320,6322,6324,6326,6328,6330,6332,6334,6336,6338,6340,6342,6344,6346,6348,6350,6352,6354,6356,6358,6360,6362,6364,6366,6368,6370,6372,6374,6376,6378,6380,6382,6384,6386,6388,6390,6392,6394,6396,6398,6400,6402,6404,6406,6408,6410,6412,6414,6416,6418,6420,6422,6424,6426,6428,6430,6432,6434,6436,6438,6440,6442,6444,6446,6448,6450,6452,6454,6456,6458,6460,6462,6464,6466,6468,6470,6472,6474,6476,6478,6480,6482,6484,6486,6488,6490,6492,6494,6496,6498,6500,6502,6504,6506,6508,6510,6512,6514,6516,6518,6520,6522,6524,6526,6528,6530,6532,6534,6536,6538,6540,6542,6544,6546,6548,6550,6552,6554,6556,6558,6560,6562,6564,6566,6568,6570,6572,6574,6576,6578,6580,6582,6584,6586,6588,6590,6592,6594,6596,6598,6600,6602,6604,6606,6608,6610,6612,6614,6616,6618,6620,6622,6624,6626,6628,6630,6632,6634,6636,6638,6640,6642,6644,6646,6648,6650,6652,6654,6656,6658,6660,6662,6664,6666,6668,6670,6672,6674,6676,6678,6680,6682,6684,6686,6688,6690,6692,6694,6696,6698,6700,6702,6704,6706,6708,6710,6712,6714,6716,6718,6720,6722,6724,6726,6728,6730,6732,6734,6736,6738,6740,6742,6744,6746,6748,6750,6752,6754,6756,6758,6760,6762,6764,6766,6768,6770,6772,6774,6776,6778,6780,6782,6784,6786,6788,6790,6792,6794,6796,6798,6800,6802,6804,6806,6808,6810,6812,6814,6816,6818,6820,6822,6824,6826,6828,6830,6832,6834,6836,6838,6840,6842,6844,6846,6848,6850,6852,6854,6856,6858,6860,6862,6864,6866,6868,6870,6872,6874,6876,6878,6880,6882,6884,6886,6888,6890,6892,6894,6896,6898,6900,6902,6904,6906,6908,6910,6912,6914,6916,6918,6920,6922,6924,6926,6928,6930,6932,6934,6936,6938,6940,6942,6944,6946,6948,6950,6952,6954,6956,6958,6960,6962,6964,6966,6968,6970,6972,6974,6976,6978,6980,6982,6984,6986,6988,6990,6992,6994,6996,6998,7000,7002,7004,7006,7008,7010,7012,7014,7016,7018,7020,7022,7024,7026,7028,7030,7032,7034,7036,7038,7040,7042,7044,7046,7048,7050,7052,7054,7056,7058,7060,7062,7064,7066,7068,7070,7072,7074,7076,7078,7080,7082,7084,7086,7088,7090,7092,7094,7096,7098,7100,7102,7104,7106,7108,7110,7112,7114,7116,7118,7120,7122,7124,7126,7128,7130,7132,7134,7136,7138,7140,7142,7144,7146,7148,7150,7152,7154,7156,7158,7160,7162,7164,7166,7168,7170,7172,7174,7176,7178,7180,7182,7184,7186,7188,7190,7192,7194,7196,7198,7200,7202,7204,7206,7208,7210,7212,7214,7216,7218,7220,7222,7224,7226,7228,7230,7232,7234,7236,7238,7240,7242,7244,7246,7248,7250,7252,7254,7256,7258,7260,7262,7264,7266,7268,7270,7272,7274,7276,7278,7280,7282,7284,7286,7288,7290,7292,7294,7296,7298,7300,7302,7304,7306,7308,7310,7312,7314,7316,7318,7320,7322,7324,7326,7328,7330,7332,7334,7336,7338,7340,7342,7344,7346,7348,7350,7352,7354,7356,7358,7360,7362,7364,7366,7368,7370,7372,7374,7376,7378,7380,7382,7384,7386,7388,7390,7392,7394,7396,7398,7400,7402,7404,7406,7408,7410,7412,7414,7416,7418,7420,7422,7424,7426,7428,7430,7432,7434,7436,7438,7440,7442,7444,7446,7448,7450,7452,7454,7456,7458,7460,7462,7464,7466,7468,7470,7472,7474,7476,7478,7480,7482,7484,7486,7488,7490,7492,7494,7496,7498,7500,7502,7504,7506,7508,7510,7512,7514,7516,7518,7520,7522,7524,7526,7528,7530,7532,7534,7536,7538,7540,7542,7544,7546,7548,7550,7552,7554,7556,7558,7560,7562,7564,7566,7568,7570,7572,7574,7576,7578,7580,7582,7584,7586,7588,7590,7592,7594,7596,7598,7600,7602,7604,7606,7608,7610,7612,7614,7616,7618,7620,7622,7624,7626,7628,7630,7632,7634,7636,7638,7640,7642,7644,7646,7648,7650,7652,7654,7656,7658,7660,7662,7664,7666,7668,7670,7672,7674,7676,7678,7680,7682,7684,7686,7688,7690,7692,7694,7696,7698,7700,7702,7704,7706,7708,7710,7712,7714,7716,7718,7720,7722,7724,7726,7728,7730,7732,7734,7736,7738,7740,7742,7744,7746,7748,7750,7752,7754,7756,7758,7760,7762,7764,7766,7768,7770,7772,7774,7776,7778,7780,7782,7784,7786,7788,7790,7792,7794,7796,7798,7800,7802,7804,7806,7808,7810,7812,7814,7816,7818,7820,7822,7824,7826,7828,7830,7832,7834,7836,7838,7840,7842,7844,7846,7848,7850,7852,7854,7856,7858,7860,7862,7864,7866,7868,7870,7872,7874,7876,7878,7880,7882,7884,7886,7888,7890,7892,7894,7896,7898,7900,7902,7904,7906,7908,7910,7912,7914,7916,7918,7920,7922,7924,7926,7928,7930,7932,7934,7936,7938,7940,7942,7944,7946,7948,7950,7952,7954,7956,7958,7960,7962,7964,7966,7968,7970,7972,7974,7976,7978,7980,7982,7984,7986,7988,7990,7992,7994,7996,7998,8000,8002,8004,8006,8008,8010,8012,8014,8016,8018,8020,8022,8024,8026,8028,8030,8032,8034,8036,8038,8040,8042,8044,8046,8048,8050,8052,8054,8056,8058,8060,8062,8064,8066,8068,8070,8072,8074,8076,8078,8080,8082,8084,8086,8088,8090,8092,8094,8096,8098,8100,8102,8104,8106,8108,8110,8112,8114,8116,8118,8120,8122,8124,8126,8128,8130,8132,8134,8136,8138,8140,8142,8144,8146,8148,8150,8152,8154,8156,8158,8160,8162,8164,8166,8168,8170,8172,8174,8176,8178,8180,8182,8184,8186,8188,8190,8192,8194,8196,8198,8200,8202,8204,8206,8208,8210,8212,8214,8216,8218,8220,8222,8224,8226,8228,8230,8232,8234,8236,8238,8240,8242,8244,8246,8248,8250,8252,8254,8256,8258,8260,8262,8264,8266,8268,8270,8272,8274,8276,8278,8280,8282,8284,8286,8288,8290,8292,8294,8296,8298,8300,8302,8304,8306,8308,8310,8312,8314,8316,8318,8320,8322,8324,8326,8328,8330,8332,8334,8336,8338,8340,8342,8344,8346,8348,8350,8352,8354,8356,8358,8360,8362,8364,8366,8368,8370,8372,8374,8376,8378,8380,8382,8384,8386,8388,8390,8392,8394,8396,8398,8400,8402,8404,8406,8408,8410,8412,8414,8416,8418,8420,8422,8424,8426,8428,8430,8432,8434,8436,8438,8440,8442,8444,8446,8448,8450,8452,8454,8456,8458,8460,8462,8464,8466,8468,8470,8472,8474,8476,8478,8480,8482,8484,8486,8488,8490,8492,8494,8496,8498,8500,8502,8504,8506,8508,8510,8512,8514,8516,8518,8520,8522,8524,8526,8528,8530,8532,8534,8536,8538,8540,8542,8544,8546,8548,8550,8552,8554,8556,8558,8560,8562,8564,8566,8568,8570,8572,8574,8576,8578,8580,8582,8584,8586,8588,8590,8592,8594,8596,8598,8600,8602,8604,8606,8608,8610,8612,8614,8616,8618,8620,8622,8624,8626,8628,8630,8632,8634,8636,8638,8640,8642,8644,8646,8648,8650,8652,8654,8656,8658,8660,8662,8664,8666,8668,8670,8672,8674,8676,8678,8680,8682,8684,8686,8688,8690,8692,8694,8696,8698,8700,8702,8704,8706,8708,8710,8712,8714,8716,8718,8720,8722,8724,8726,8728,8730,8732,8734,8736,8738,8740,8742,8744,8746,8748,8750,8752,8754,8756,8758,8760,8762,8764,8766,8768,8770,8772,8774,8776,8778,8780,8782,8784,8786,8788,8790,8792,8794,8796,8798,8800,8802,8804,8806,8808,8810,8812,8814,8816,8818,8820,8822,8824,8826,8828,8830,8832,8834,8836,8838,8840,8842,8844,8846,8848,8850,8852,8854,8856,8858,8860,8862,8864,8866,8868,8870,8872,8874,8876,8878,8880,8882,8884,8886,8888,8890,8892,8894,8896,8898,8900,8902,8904,8906,8908,8910,8912,8914,8916,8918,8920,8922,8924,8926,8928,8930,8932,8934,8936,8938,8940,8942,8944,8946,8948,8950,8952,8954,8956,8958,8960,8962,8964,8966,8968,8970,8972,8974,8976,8978,8980,8982,8984,8986,8988,8990,8992,8994,8996,8998,9000,9002,9004,9006,9008,9010,9012,9014,9016,9018,9020,9022,9024,9026,9028,9030,9032,9034,9036,9038,9040,9042,9044,9046,9048,9050,9052,9054,9056,9058,9060,9062,9064,9066,9068,9070,9072,9074,9076,9078,9080,9082,9084,9086,9088,9090,9092,9094,9096,9098,9100,9102,9104,9106,9108,9110,9112,9114,9116,9118,9120,9122,9124,9126,9128,9130,9132,9134,9136,9138,9140,9142,9144,9146,9148,9150,9152,9154,9156,9158,9160,9162,9164,9166,9168,9170,9172,9174,9176,9178,9180,9182,9184,9186,9188,9190,9192,9194,9196,9198,9200,9202,9204,9206,9208,9210,9212,9214,9216,9218,9220,9222,9224,9226,9228,9230,9232,9234,9236,9238,9240,9242,9244,9246,9248,9250,9252,9254,9256,9258,9260,9262,9264,9266,9268,9270,9272,9274,9276,9278,9280,9282,9284,9286,9288,9290,9292,9294,9296,9298,9300,9302,9304,9306,9308,9310,9312,9314,9316,9318,9320,9322,9324,9326,9328,9330,9332,9334,9336,9338,9340,9342,9344,9346,9348,9350,9352,9354,9356,9358,9360,9362,9364,9366,9368,9370,9372,9374,9376,9378,9380,9382,9384,9386,9388,9390,9392,9394,9396,9398,9400,9402,9404,9406,9408,9410,9412,9414,9416,9418,9420,9422,9424,9426,9428,9430,9432,9434,9436,9438,9440,9442,9444,9446,9448,9450,9452,9454,9456,9458,9460,9462,9464,9466,9468,9470,9472,9474,9476,9478,9480,9482,9484,9486,9488,9490,9492,9494,9496,9498,9500,9502,9504,9506,9508,9510,9512,9514,9516,9518,9520,9522,9524,9526,9528,9530,9532,9534,9536,9538,9540,9542,9544,9546,9548,9550,9552,9554,9556,9558,9560,9562,9564,9566,9568,9570,9572,9574,9576,9578,9580,9582,9584,9586,9588,9590,9592,9594,9596,9598,9600,9602,9604,9606,9608,9610,9612,9614,9616,9618,9620,9622,9624,9626,9628,9630,9632,9634,9636,9638,9640,9642,9644,9646,9648,9650,9652,9654,9656,9658,9660,9662,9664,9666,9668,9670,9672,9674,9676,9678,9680,9682,9684,9686,9688,9690,9692,9694,9696,9698,9700,9702,9704,9706,9708,9710,9712,9714,9716,9718,9720,9722,9724,9726,9728,9730,9732,9734,9736,9738,9740,9742,9744,9746,9748,9750,9752,9754,9756,9758,9760,9762,9764,9766,9768,9770,9772,9774,9776,9778,9780,9782,9784,9786,9788,9790,9792,9794,9796,9798,9800,9802,9804,9806,9808,9810,9812,9814,9816,9818,9820,9822,9824,9826,9828,9830,9832,9834,9836,9838,9840,9842,9844,9846,9848,9850,9852,9854,9856,9858,9860,9862,9864,9866,9868,9870,9872,9874,9876,9878,9880,9882,9884,9886,9888,9890,9892,9894,9896,9898,9900,9902,9904,9906,9908,9910,9912,9914,9916,9918,9920,9922,9924,9926,9928,9930,9932,9934,9936,9938,9940,9942,9944,9946,9948,9950,9952,9954,9956,9958,9960,9962,9964,9966,9968,9970,9972,9974,9976,9978,9980,9982,9984,9986,9988,9990,9992,9994,9996,9998,10000,10002,10004,10006,10008,10010,10012,10014,10016,10018,10020,10022,10024,10026,10028,10030,10032,10034,10036,10038,10040,10042,10044,10046,10048,10050,10052,10054,10056,10058,10060,10062,10064,10066,10068,10070,10072,10074,10076,10078,10080,10082,10084,10086,10088,10090,10092,10094,10096,10098,10100,10102,10104,10106,10108,10110,10112,10114,10116,10118,10120,10122,10124,10126,10128,10130,10132,10134,10136,10138,10140,10142,10144,10146,10148,10150,10152,10154,10156,10158,10160,10162,10164,10166,10168,10170,10172,10174,10176,10178,10180,10182,10184,10186,10188,10190,10192,10194,10196,10198,10200], 10202)
print datetime.datetime.now() - t