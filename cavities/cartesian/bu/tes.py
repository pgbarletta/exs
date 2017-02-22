from pymol.cgo import *
from pymol import cmd

cmd.load("avg_1hvr_apo.pdb")
cmd.show("cartoon")
tes_null_1 = [
	COLOR,  1,	0,	0,
# new cell
	SPHERE,	47.464,	44.613,	26.256,	0.5,
# new cell
	SPHERE,	47.0018,	44.9494,	26.9513,	0.5,
# new cell
	SPHERE,	46.5396,	45.2858,	27.6466,	0.5,
# new cell
	SPHERE,	46.0774,	45.6222,	28.3419,	0.5,
# new cell
	SPHERE,	45.6152,	45.9586,	29.0372,	0.5,
# new cell
	SPHERE,	45.153,	46.295,	29.7325,	0.5,
# new cell
	SPHERE,	44.6908,	46.6314,	30.4278,	0.5,
# new cell
	SPHERE,	44.2286,	46.9678,	31.1231,	0.5,
# new cell
	SPHERE,	43.7664,	47.3042,	31.8184,	0.5,
# new cell
	SPHERE,	43.3042,	47.6406,	32.5137,	0.5,
# new cell
	SPHERE,	42.842,	47.977,	33.209,	0.5,
# new cell
	SPHERE,	47.3969,	44.8072,	27.3412,	0.5,
# new cell
	SPHERE,	46.9347,	45.1436,	28.0365,	0.5,
# new cell
	SPHERE,	46.4725,	45.48,	28.7318,	0.5,
# new cell
	SPHERE,	46.0103,	45.8164,	29.4271,	0.5,
# new cell
	SPHERE,	45.5481,	46.1528,	30.1224,	0.5,
# new cell
	SPHERE,	45.0859,	46.4892,	30.8177,	0.5,
# new cell
	SPHERE,	44.6237,	46.8256,	31.513,	0.5,
# new cell
	SPHERE,	44.1615,	47.162,	32.2083,	0.5,
# new cell
	SPHERE,	43.6993,	47.4984,	32.9036,	0.5,
# new cell
	SPHERE,	43.2371,	47.8348,	33.5989,	0.5,
# new cell
	SPHERE,	47.3298,	45.0014,	28.4264,	0.5,
# new cell
	SPHERE,	46.8676,	45.3378,	29.1217,	0.5,
# new cell
	SPHERE,	46.4054,	45.6742,	29.817,	0.5,
# new cell
	SPHERE,	45.9432,	46.0106,	30.5123,	0.5,
# new cell
	SPHERE,	45.481,	46.347,	31.2076,	0.5,
# new cell
	SPHERE,	45.0188,	46.6834,	31.9029,	0.5,
# new cell
	SPHERE,	44.5566,	47.0198,	32.5982,	0.5,
# new cell
	SPHERE,	44.0944,	47.3562,	33.2935,	0.5,
# new cell
	SPHERE,	43.6322,	47.6926,	33.9888,	0.5,
# new cell
	SPHERE,	47.2627,	45.1956,	29.5116,	0.5,
# new cell
	SPHERE,	46.8005,	45.532,	30.2069,	0.5,
# new cell
	SPHERE,	46.3383,	45.8684,	30.9022,	0.5,
# new cell
	SPHERE,	45.8761,	46.2048,	31.5975,	0.5,
# new cell
	SPHERE,	45.4139,	46.5412,	32.2928,	0.5,
# new cell
	SPHERE,	44.9517,	46.8776,	32.9881,	0.5,
# new cell
	SPHERE,	44.4895,	47.214,	33.6834,	0.5,
# new cell
	SPHERE,	44.0273,	47.5504,	34.3787,	0.5,
# new cell
	SPHERE,	47.1956,	45.3898,	30.5968,	0.5,
# new cell
	SPHERE,	46.7334,	45.7262,	31.2921,	0.5,
# new cell
	SPHERE,	46.2712,	46.0626,	31.9874,	0.5,
# new cell
	SPHERE,	45.809,	46.399,	32.6827,	0.5,
# new cell
	SPHERE,	45.3468,	46.7354,	33.378,	0.5,
# new cell
	SPHERE,	44.8846,	47.0718,	34.0733,	0.5,
# new cell
	SPHERE,	44.4224,	47.4082,	34.7686,	0.5,
# new cell
	SPHERE,	47.1285,	45.584,	31.682,	0.5,
# new cell
	SPHERE,	46.6663,	45.9204,	32.3773,	0.5,
# new cell
	SPHERE,	46.2041,	46.2568,	33.0726,	0.5,
# new cell
	SPHERE,	45.7419,	46.5932,	33.7679,	0.5,
# new cell
	SPHERE,	45.2797,	46.9296,	34.4632,	0.5,
# new cell
	SPHERE,	44.8175,	47.266,	35.1585,	0.5,
# new cell
	SPHERE,	47.0614,	45.7782,	32.7672,	0.5,
# new cell
	SPHERE,	46.5992,	46.1146,	33.4625,	0.5,
# new cell
	SPHERE,	46.137,	46.451,	34.1578,	0.5,
# new cell
	SPHERE,	45.6748,	46.7874,	34.8531,	0.5,
# new cell
	SPHERE,	45.2126,	47.1238,	35.5484,	0.5,
# new cell
	SPHERE,	46.9943,	45.9724,	33.8524,	0.5,
# new cell
	SPHERE,	46.5321,	46.3088,	34.5477,	0.5,
# new cell
	SPHERE,	46.0699,	46.6452,	35.243,	0.5,
# new cell
	SPHERE,	45.6077,	46.9816,	35.9383,	0.5,
# new cell
	SPHERE,	46.9272,	46.1666,	34.9376,	0.5,
# new cell
	SPHERE,	46.465,	46.503,	35.6329,	0.5,
# new cell
	SPHERE,	46.0028,	46.8394,	36.3282,	0.5,
# new cell
	SPHERE,	46.8601,	46.3608,	36.0228,	0.5,
# new cell
	SPHERE,	46.3979,	46.6972,	36.7181,	0.5,
# new cell
	SPHERE,	46.793,	46.555,	37.108,	0.5,
# new cell
	SPHERE,	47.326,	45.0108,	27.2305,	0.5,
# new cell
	SPHERE,	46.8638,	45.3472,	27.9258,	0.5,
# new cell
	SPHERE,	46.4016,	45.6836,	28.6211,	0.5,
# new cell
	SPHERE,	45.9394,	46.02,	29.3164,	0.5,
# new cell
	SPHERE,	45.4772,	46.3564,	30.0117,	0.5,
# new cell
	SPHERE,	45.015,	46.6928,	30.707,	0.5,
# new cell
	SPHERE,	44.5528,	47.0292,	31.4023,	0.5,
# new cell
	SPHERE,	44.0906,	47.3656,	32.0976,	0.5,
# new cell
	SPHERE,	43.6284,	47.702,	32.7929,	0.5,
# new cell
	SPHERE,	43.1662,	48.0384,	33.4882,	0.5,
# new cell
	SPHERE,	47.2589,	45.205,	28.3157,	0.5,
# new cell
	SPHERE,	46.7967,	45.5414,	29.011,	0.5,
# new cell
	SPHERE,	46.3345,	45.8778,	29.7063,	0.5,
# new cell
	SPHERE,	45.8723,	46.2142,	30.4016,	0.5,
# new cell
	SPHERE,	45.4101,	46.5506,	31.0969,	0.5,
# new cell
	SPHERE,	44.9479,	46.887,	31.7922,	0.5,
# new cell
	SPHERE,	44.4857,	47.2234,	32.4875,	0.5,
# new cell
	SPHERE,	44.0235,	47.5598,	33.1828,	0.5,
# new cell
	SPHERE,	43.5613,	47.8962,	33.8781,	0.5,
# new cell
	SPHERE,	47.1918,	45.3992,	29.4009,	0.5,
# new cell
	SPHERE,	46.7296,	45.7356,	30.0962,	0.5,
# new cell
	SPHERE,	46.2674,	46.072,	30.7915,	0.5,
# new cell
	SPHERE,	45.8052,	46.4084,	31.4868,	0.5,
# new cell
	SPHERE,	45.343,	46.7448,	32.1821,	0.5,
# new cell
	SPHERE,	44.8808,	47.0812,	32.8774,	0.5,
# new cell
	SPHERE,	44.4186,	47.4176,	33.5727,	0.5,
# new cell
	SPHERE,	43.9564,	47.754,	34.268,	0.5,
# new cell
	SPHERE,	47.1247,	45.5934,	30.4861,	0.5,
# new cell
	SPHERE,	46.6625,	45.9298,	31.1814,	0.5,
# new cell
	SPHERE,	46.2003,	46.2662,	31.8767,	0.5,
# new cell
	SPHERE,	45.7381,	46.6026,	32.572,	0.5,
# new cell
	SPHERE,	45.2759,	46.939,	33.2673,	0.5,
# new cell
	SPHERE,	44.8137,	47.2754,	33.9626,	0.5,
# new cell
	SPHERE,	44.3515,	47.6118,	34.6579,	0.5,
# new cell
	SPHERE,	47.0576,	45.7876,	31.5713,	0.5,
# new cell
	SPHERE,	46.5954,	46.124,	32.2666,	0.5,
# new cell
	SPHERE,	46.1332,	46.4604,	32.9619,	0.5,
# new cell
	SPHERE,	45.671,	46.7968,	33.6572,	0.5,
# new cell
	SPHERE,	45.2088,	47.1332,	34.3525,	0.5,
# new cell
	SPHERE,	44.7466,	47.4696,	35.0478,	0.5,
# new cell
	SPHERE,	46.9905,	45.9818,	32.6565,	0.5,
# new cell
	SPHERE,	46.5283,	46.3182,	33.3518,	0.5,
# new cell
	SPHERE,	46.0661,	46.6546,	34.0471,	0.5,
# new cell
	SPHERE,	45.6039,	46.991,	34.7424,	0.5,
# new cell
	SPHERE,	45.1417,	47.3274,	35.4377,	0.5,
# new cell
	SPHERE,	46.9234,	46.176,	33.7417,	0.5,
# new cell
	SPHERE,	46.4612,	46.5124,	34.437,	0.5,
# new cell
	SPHERE,	45.999,	46.8488,	35.1323,	0.5,
# new cell
	SPHERE,	45.5368,	47.1852,	35.8276,	0.5,
# new cell
	SPHERE,	46.8563,	46.3702,	34.8269,	0.5,
# new cell
	SPHERE,	46.3941,	46.7066,	35.5222,	0.5,
# new cell
	SPHERE,	45.9319,	47.043,	36.2175,	0.5,
# new cell
	SPHERE,	46.7892,	46.5644,	35.9121,	0.5,
# new cell
	SPHERE,	46.327,	46.9008,	36.6074,	0.5,
# new cell
	SPHERE,	46.7221,	46.7586,	36.9973,	0.5,
# new cell
	SPHERE,	47.188,	45.4086,	28.205,	0.5,
# new cell
	SPHERE,	46.7258,	45.745,	28.9003,	0.5,
# new cell
	SPHERE,	46.2636,	46.0814,	29.5956,	0.5,
# new cell
	SPHERE,	45.8014,	46.4178,	30.2909,	0.5,
# new cell
	SPHERE,	45.3392,	46.7542,	30.9862,	0.5,
# new cell
	SPHERE,	44.877,	47.0906,	31.6815,	0.5,
# new cell
	SPHERE,	44.4148,	47.427,	32.3768,	0.5,
# new cell
	SPHERE,	43.9526,	47.7634,	33.0721,	0.5,
# new cell
	SPHERE,	43.4904,	48.0998,	33.7674,	0.5,
# new cell
	SPHERE,	47.1209,	45.6028,	29.2902,	0.5,
# new cell
	SPHERE,	46.6587,	45.9392,	29.9855,	0.5,
# new cell
	SPHERE,	46.1965,	46.2756,	30.6808,	0.5,
# new cell
	SPHERE,	45.7343,	46.612,	31.3761,	0.5,
# new cell
	SPHERE,	45.2721,	46.9484,	32.0714,	0.5,
# new cell
	SPHERE,	44.8099,	47.2848,	32.7667,	0.5,
# new cell
	SPHERE,	44.3477,	47.6212,	33.462,	0.5,
# new cell
	SPHERE,	43.8855,	47.9576,	34.1573,	0.5,
# new cell
	SPHERE,	47.0538,	45.797,	30.3754,	0.5,
# new cell
	SPHERE,	46.5916,	46.1334,	31.0707,	0.5,
# new cell
	SPHERE,	46.1294,	46.4698,	31.766,	0.5,
# new cell
	SPHERE,	45.6672,	46.8062,	32.4613,	0.5,
# new cell
	SPHERE,	45.205,	47.1426,	33.1566,	0.5,
# new cell
	SPHERE,	44.7428,	47.479,	33.8519,	0.5,
# new cell
	SPHERE,	44.2806,	47.8154,	34.5472,	0.5,
# new cell
	SPHERE,	46.9867,	45.9912,	31.4606,	0.5,
# new cell
	SPHERE,	46.5245,	46.3276,	32.1559,	0.5,
# new cell
	SPHERE,	46.0623,	46.664,	32.8512,	0.5,
# new cell
	SPHERE,	45.6001,	47.0004,	33.5465,	0.5,
# new cell
	SPHERE,	45.1379,	47.3368,	34.2418,	0.5,
# new cell
	SPHERE,	44.6757,	47.6732,	34.9371,	0.5,
# new cell
	SPHERE,	46.9196,	46.1854,	32.5458,	0.5,
# new cell
	SPHERE,	46.4574,	46.5218,	33.2411,	0.5,
# new cell
	SPHERE,	45.9952,	46.8582,	33.9364,	0.5,
# new cell
	SPHERE,	45.533,	47.1946,	34.6317,	0.5,
# new cell
	SPHERE,	45.0708,	47.531,	35.327,	0.5,
# new cell
	SPHERE,	46.8525,	46.3796,	33.631,	0.5,
# new cell
	SPHERE,	46.3903,	46.716,	34.3263,	0.5,
# new cell
	SPHERE,	45.9281,	47.0524,	35.0216,	0.5,
# new cell
	SPHERE,	45.4659,	47.3888,	35.7169,	0.5,
# new cell
	SPHERE,	46.7854,	46.5738,	34.7162,	0.5,
# new cell
	SPHERE,	46.3232,	46.9102,	35.4115,	0.5,
# new cell
	SPHERE,	45.861,	47.2466,	36.1068,	0.5,
# new cell
	SPHERE,	46.7183,	46.768,	35.8014,	0.5,
# new cell
	SPHERE,	46.2561,	47.1044,	36.4967,	0.5,
# new cell
	SPHERE,	46.6512,	46.9622,	36.8866,	0.5,
# new cell
	SPHERE,	47.05,	45.8064,	29.1795,	0.5,
# new cell
	SPHERE,	46.5878,	46.1428,	29.8748,	0.5,
# new cell
	SPHERE,	46.1256,	46.4792,	30.5701,	0.5,
# new cell
	SPHERE,	45.6634,	46.8156,	31.2654,	0.5,
# new cell
	SPHERE,	45.2012,	47.152,	31.9607,	0.5,
# new cell
	SPHERE,	44.739,	47.4884,	32.656,	0.5,
# new cell
	SPHERE,	44.2768,	47.8248,	33.3513,	0.5,
# new cell
	SPHERE,	43.8146,	48.1612,	34.0466,	0.5,
# new cell
	SPHERE,	46.9829,	46.0006,	30.2647,	0.5,
# new cell
	SPHERE,	46.5207,	46.337,	30.96,	0.5,
# new cell
	SPHERE,	46.0585,	46.6734,	31.6553,	0.5,
# new cell
	SPHERE,	45.5963,	47.0098,	32.3506,	0.5,
# new cell
	SPHERE,	45.1341,	47.3462,	33.0459,	0.5,
# new cell
	SPHERE,	44.6719,	47.6826,	33.7412,	0.5,
# new cell
	SPHERE,	44.2097,	48.019,	34.4365,	0.5,
# new cell
	SPHERE,	46.9158,	46.1948,	31.3499,	0.5,
# new cell
	SPHERE,	46.4536,	46.5312,	32.0452,	0.5,
# new cell
	SPHERE,	45.9914,	46.8676,	32.7405,	0.5,
# new cell
	SPHERE,	45.5292,	47.204,	33.4358,	0.5,
# new cell
	SPHERE,	45.067,	47.5404,	34.1311,	0.5,
# new cell
	SPHERE,	44.6048,	47.8768,	34.8264,	0.5,
# new cell
	SPHERE,	46.8487,	46.389,	32.4351,	0.5,
# new cell
	SPHERE,	46.3865,	46.7254,	33.1304,	0.5,
# new cell
	SPHERE,	45.9243,	47.0618,	33.8257,	0.5,
# new cell
	SPHERE,	45.4621,	47.3982,	34.521,	0.5,
# new cell
	SPHERE,	44.9999,	47.7346,	35.2163,	0.5,
# new cell
	SPHERE,	46.7816,	46.5832,	33.5203,	0.5,
# new cell
	SPHERE,	46.3194,	46.9196,	34.2156,	0.5,
# new cell
	SPHERE,	45.8572,	47.256,	34.9109,	0.5,
# new cell
	SPHERE,	45.395,	47.5924,	35.6062,	0.5,
# new cell
	SPHERE,	46.7145,	46.7774,	34.6055,	0.5,
# new cell
	SPHERE,	46.2523,	47.1138,	35.3008,	0.5,
# new cell
	SPHERE,	45.7901,	47.4502,	35.9961,	0.5,
# new cell
	SPHERE,	46.6474,	46.9716,	35.6907,	0.5,
# new cell
	SPHERE,	46.1852,	47.308,	36.386,	0.5,
# new cell
	SPHERE,	46.5803,	47.1658,	36.7759,	0.5,
# new cell
	SPHERE,	46.912,	46.2042,	30.154,	0.5,
# new cell
	SPHERE,	46.4498,	46.5406,	30.8493,	0.5,
# new cell
	SPHERE,	45.9876,	46.877,	31.5446,	0.5,
# new cell
	SPHERE,	45.5254,	47.2134,	32.2399,	0.5,
# new cell
	SPHERE,	45.0632,	47.5498,	32.9352,	0.5,
# new cell
	SPHERE,	44.601,	47.8862,	33.6305,	0.5,
# new cell
	SPHERE,	44.1388,	48.2226,	34.3258,	0.5,
# new cell
	SPHERE,	46.8449,	46.3984,	31.2392,	0.5,
# new cell
	SPHERE,	46.3827,	46.7348,	31.9345,	0.5,
# new cell
	SPHERE,	45.9205,	47.0712,	32.6298,	0.5,
# new cell
	SPHERE,	45.4583,	47.4076,	33.3251,	0.5,
# new cell
	SPHERE,	44.9961,	47.744,	34.0204,	0.5,
# new cell
	SPHERE,	44.5339,	48.0804,	34.7157,	0.5,
# new cell
	SPHERE,	46.7778,	46.5926,	32.3244,	0.5,
# new cell
	SPHERE,	46.3156,	46.929,	33.0197,	0.5,
# new cell
	SPHERE,	45.8534,	47.2654,	33.715,	0.5,
# new cell
	SPHERE,	45.3912,	47.6018,	34.4103,	0.5,
# new cell
	SPHERE,	44.929,	47.9382,	35.1056,	0.5,
# new cell
	SPHERE,	46.7107,	46.7868,	33.4096,	0.5,
# new cell
	SPHERE,	46.2485,	47.1232,	34.1049,	0.5,
# new cell
	SPHERE,	45.7863,	47.4596,	34.8002,	0.5,
# new cell
	SPHERE,	45.3241,	47.796,	35.4955,	0.5,
# new cell
	SPHERE,	46.6436,	46.981,	34.4948,	0.5,
# new cell
	SPHERE,	46.1814,	47.3174,	35.1901,	0.5,
# new cell
	SPHERE,	45.7192,	47.6538,	35.8854,	0.5,
# new cell
	SPHERE,	46.5765,	47.1752,	35.58,	0.5,
# new cell
	SPHERE,	46.1143,	47.5116,	36.2753,	0.5,
# new cell
	SPHERE,	46.5094,	47.3694,	36.6652,	0.5,
# new cell
	SPHERE,	46.774,	46.602,	31.1285,	0.5,
# new cell
	SPHERE,	46.3118,	46.9384,	31.8238,	0.5,
# new cell
	SPHERE,	45.8496,	47.2748,	32.5191,	0.5,
# new cell
	SPHERE,	45.3874,	47.6112,	33.2144,	0.5,
# new cell
	SPHERE,	44.9252,	47.9476,	33.9097,	0.5,
# new cell
	SPHERE,	44.463,	48.284,	34.605,	0.5,
# new cell
	SPHERE,	46.7069,	46.7962,	32.2137,	0.5,
# new cell
	SPHERE,	46.2447,	47.1326,	32.909,	0.5,
# new cell
	SPHERE,	45.7825,	47.469,	33.6043,	0.5,
# new cell
	SPHERE,	45.3203,	47.8054,	34.2996,	0.5,
# new cell
	SPHERE,	44.8581,	48.1418,	34.9949,	0.5,
# new cell
	SPHERE,	46.6398,	46.9904,	33.2989,	0.5,
# new cell
	SPHERE,	46.1776,	47.3268,	33.9942,	0.5,
# new cell
	SPHERE,	45.7154,	47.6632,	34.6895,	0.5,
# new cell
	SPHERE,	45.2532,	47.9996,	35.3848,	0.5,
# new cell
	SPHERE,	46.5727,	47.1846,	34.3841,	0.5,
# new cell
	SPHERE,	46.1105,	47.521,	35.0794,	0.5,
# new cell
	SPHERE,	45.6483,	47.8574,	35.7747,	0.5,
# new cell
	SPHERE,	46.5056,	47.3788,	35.4693,	0.5,
# new cell
	SPHERE,	46.0434,	47.7152,	36.1646,	0.5,
# new cell
	SPHERE,	46.4385,	47.573,	36.5545,	0.5,
# new cell
	SPHERE,	46.636,	46.9998,	32.103,	0.5,
# new cell
	SPHERE,	46.1738,	47.3362,	32.7983,	0.5,
# new cell
	SPHERE,	45.7116,	47.6726,	33.4936,	0.5,
# new cell
	SPHERE,	45.2494,	48.009,	34.1889,	0.5,
# new cell
	SPHERE,	44.7872,	48.3454,	34.8842,	0.5,
# new cell
	SPHERE,	46.5689,	47.194,	33.1882,	0.5,
# new cell
	SPHERE,	46.1067,	47.5304,	33.8835,	0.5,
# new cell
	SPHERE,	45.6445,	47.8668,	34.5788,	0.5,
# new cell
	SPHERE,	45.1823,	48.2032,	35.2741,	0.5,
# new cell
	SPHERE,	46.5018,	47.3882,	34.2734,	0.5,
# new cell
	SPHERE,	46.0396,	47.7246,	34.9687,	0.5,
# new cell
	SPHERE,	45.5774,	48.061,	35.664,	0.5,
# new cell
	SPHERE,	46.4347,	47.5824,	35.3586,	0.5,
# new cell
	SPHERE,	45.9725,	47.9188,	36.0539,	0.5,
# new cell
	SPHERE,	46.3676,	47.7766,	36.4438,	0.5,
# new cell
	SPHERE,	46.498,	47.3976,	33.0775,	0.5,
# new cell
	SPHERE,	46.0358,	47.734,	33.7728,	0.5,
# new cell
	SPHERE,	45.5736,	48.0704,	34.4681,	0.5,
# new cell
	SPHERE,	45.1114,	48.4068,	35.1634,	0.5,
# new cell
	SPHERE,	46.4309,	47.5918,	34.1627,	0.5,
# new cell
	SPHERE,	45.9687,	47.9282,	34.858,	0.5,
# new cell
	SPHERE,	45.5065,	48.2646,	35.5533,	0.5,
# new cell
	SPHERE,	46.3638,	47.786,	35.2479,	0.5,
# new cell
	SPHERE,	45.9016,	48.1224,	35.9432,	0.5,
# new cell
	SPHERE,	46.2967,	47.9802,	36.3331,	0.5,
# new cell
	SPHERE,	46.36,	47.7954,	34.052,	0.5,
# new cell
	SPHERE,	45.8978,	48.1318,	34.7473,	0.5,
# new cell
	SPHERE,	45.4356,	48.4682,	35.4426,	0.5,
# new cell
	SPHERE,	46.2929,	47.9896,	35.1372,	0.5,
# new cell
	SPHERE,	45.8307,	48.326,	35.8325,	0.5,
# new cell
	SPHERE,	46.2258,	48.1838,	36.2224,	0.5,
# new cell
	SPHERE,	46.222,	48.1932,	35.0265,	0.5,
# new cell
	SPHERE,	45.7598,	48.5296,	35.7218,	0.5,
# new cell
	SPHERE,	46.1549,	48.3874,	36.1117,	0.5,
# new cell
	SPHERE,	46.084,	48.591,	36.001,	0.5,
# new cell
	SPHERE,	46.793,	46.555,	37.108,	0.5,
# new cell
	SPHERE,	47.3767,	46.6818,	36.5481,	0.5,
# new cell
	SPHERE,	47.9604,	46.8086,	35.9882,	0.5,
# new cell
	SPHERE,	48.5441,	46.9354,	35.4283,	0.5,
# new cell
	SPHERE,	49.1278,	47.0622,	34.8684,	0.5,
# new cell
	SPHERE,	49.7115,	47.189,	34.3085,	0.5,
# new cell
	SPHERE,	50.2952,	47.3158,	33.7486,	0.5,
# new cell
	SPHERE,	50.8789,	47.4426,	33.1887,	0.5,
# new cell
	SPHERE,	51.4626,	47.5694,	32.6288,	0.5,
# new cell
	SPHERE,	52.0463,	47.6962,	32.0689,	0.5,
# new cell
	SPHERE,	52.63,	47.823,	31.509,	0.5,
# new cell
	SPHERE,	47.0277,	46.9979,	37.0134,	0.5,
# new cell
	SPHERE,	47.6114,	47.1247,	36.4535,	0.5,
# new cell
	SPHERE,	48.1951,	47.2515,	35.8936,	0.5,
# new cell
	SPHERE,	48.7788,	47.3783,	35.3337,	0.5,
# new cell
	SPHERE,	49.3625,	47.5051,	34.7738,	0.5,
# new cell
	SPHERE,	49.9462,	47.6319,	34.2139,	0.5,
# new cell
	SPHERE,	50.5299,	47.7587,	33.654,	0.5,
# new cell
	SPHERE,	51.1136,	47.8855,	33.0941,	0.5,
# new cell
	SPHERE,	51.6973,	48.0123,	32.5342,	0.5,
# new cell
	SPHERE,	52.281,	48.1391,	31.9743,	0.5,
# new cell
	SPHERE,	47.2624,	47.4408,	36.9188,	0.5,
# new cell
	SPHERE,	47.8461,	47.5676,	36.3589,	0.5,
# new cell
	SPHERE,	48.4298,	47.6944,	35.799,	0.5,
# new cell
	SPHERE,	49.0135,	47.8212,	35.2391,	0.5,
# new cell
	SPHERE,	49.5972,	47.948,	34.6792,	0.5,
# new cell
	SPHERE,	50.1809,	48.0748,	34.1193,	0.5,
# new cell
	SPHERE,	50.7646,	48.2016,	33.5594,	0.5,
# new cell
	SPHERE,	51.3483,	48.3284,	32.9995,	0.5,
# new cell
	SPHERE,	51.932,	48.4552,	32.4396,	0.5,
# new cell
	SPHERE,	47.4971,	47.8837,	36.8242,	0.5,
# new cell
	SPHERE,	48.0808,	48.0105,	36.2643,	0.5,
# new cell
	SPHERE,	48.6645,	48.1373,	35.7044,	0.5,
# new cell
	SPHERE,	49.2482,	48.2641,	35.1445,	0.5,
# new cell
	SPHERE,	49.8319,	48.3909,	34.5846,	0.5,
# new cell
	SPHERE,	50.4156,	48.5177,	34.0247,	0.5,
# new cell
	SPHERE,	50.9993,	48.6445,	33.4648,	0.5,
# new cell
	SPHERE,	51.583,	48.7713,	32.9049,	0.5,
# new cell
	SPHERE,	47.7318,	48.3266,	36.7296,	0.5,
# new cell
	SPHERE,	48.3155,	48.4534,	36.1697,	0.5,
# new cell
	SPHERE,	48.8992,	48.5802,	35.6098,	0.5,
# new cell
	SPHERE,	49.4829,	48.707,	35.0499,	0.5,
# new cell
	SPHERE,	50.0666,	48.8338,	34.49,	0.5,
# new cell
	SPHERE,	50.6503,	48.9606,	33.9301,	0.5,
# new cell
	SPHERE,	51.234,	49.0874,	33.3702,	0.5,
# new cell
	SPHERE,	47.9665,	48.7695,	36.635,	0.5,
# new cell
	SPHERE,	48.5502,	48.8963,	36.0751,	0.5,
# new cell
	SPHERE,	49.1339,	49.0231,	35.5152,	0.5,
# new cell
	SPHERE,	49.7176,	49.1499,	34.9553,	0.5,
# new cell
	SPHERE,	50.3013,	49.2767,	34.3954,	0.5,
# new cell
	SPHERE,	50.885,	49.4035,	33.8355,	0.5,
# new cell
	SPHERE,	48.2012,	49.2124,	36.5404,	0.5,
# new cell
	SPHERE,	48.7849,	49.3392,	35.9805,	0.5,
# new cell
	SPHERE,	49.3686,	49.466,	35.4206,	0.5,
# new cell
	SPHERE,	49.9523,	49.5928,	34.8607,	0.5,
# new cell
	SPHERE,	50.536,	49.7196,	34.3008,	0.5,
# new cell
	SPHERE,	48.4359,	49.6553,	36.4458,	0.5,
# new cell
	SPHERE,	49.0196,	49.7821,	35.8859,	0.5,
# new cell
	SPHERE,	49.6033,	49.9089,	35.326,	0.5,
# new cell
	SPHERE,	50.187,	50.0357,	34.7661,	0.5,
# new cell
	SPHERE,	48.6706,	50.0982,	36.3512,	0.5,
# new cell
	SPHERE,	49.2543,	50.225,	35.7913,	0.5,
# new cell
	SPHERE,	49.838,	50.3518,	35.2314,	0.5,
# new cell
	SPHERE,	48.9053,	50.5411,	36.2566,	0.5,
# new cell
	SPHERE,	49.489,	50.6679,	35.6967,	0.5,
# new cell
	SPHERE,	49.14,	50.984,	36.162,	0.5,
# new cell
	SPHERE,	47.0926,	46.8052,	37.1945,	0.5,
# new cell
	SPHERE,	47.6763,	46.932,	36.6346,	0.5,
# new cell
	SPHERE,	48.26,	47.0588,	36.0747,	0.5,
# new cell
	SPHERE,	48.8437,	47.1856,	35.5148,	0.5,
# new cell
	SPHERE,	49.4274,	47.3124,	34.9549,	0.5,
# new cell
	SPHERE,	50.0111,	47.4392,	34.395,	0.5,
# new cell
	SPHERE,	50.5948,	47.566,	33.8351,	0.5,
# new cell
	SPHERE,	51.1785,	47.6928,	33.2752,	0.5,
# new cell
	SPHERE,	51.7622,	47.8196,	32.7153,	0.5,
# new cell
	SPHERE,	52.3459,	47.9464,	32.1554,	0.5,
# new cell
	SPHERE,	47.3273,	47.2481,	37.0999,	0.5,
# new cell
	SPHERE,	47.911,	47.3749,	36.54,	0.5,
# new cell
	SPHERE,	48.4947,	47.5017,	35.9801,	0.5,
# new cell
	SPHERE,	49.0784,	47.6285,	35.4202,	0.5,
# new cell
	SPHERE,	49.6621,	47.7553,	34.8603,	0.5,
# new cell
	SPHERE,	50.2458,	47.8821,	34.3004,	0.5,
# new cell
	SPHERE,	50.8295,	48.0089,	33.7405,	0.5,
# new cell
	SPHERE,	51.4132,	48.1357,	33.1806,	0.5,
# new cell
	SPHERE,	51.9969,	48.2625,	32.6207,	0.5,
# new cell
	SPHERE,	47.562,	47.691,	37.0053,	0.5,
# new cell
	SPHERE,	48.1457,	47.8178,	36.4454,	0.5,
# new cell
	SPHERE,	48.7294,	47.9446,	35.8855,	0.5,
# new cell
	SPHERE,	49.3131,	48.0714,	35.3256,	0.5,
# new cell
	SPHERE,	49.8968,	48.1982,	34.7657,	0.5,
# new cell
	SPHERE,	50.4805,	48.325,	34.2058,	0.5,
# new cell
	SPHERE,	51.0642,	48.4518,	33.6459,	0.5,
# new cell
	SPHERE,	51.6479,	48.5786,	33.086,	0.5,
# new cell
	SPHERE,	47.7967,	48.1339,	36.9107,	0.5,
# new cell
	SPHERE,	48.3804,	48.2607,	36.3508,	0.5,
# new cell
	SPHERE,	48.9641,	48.3875,	35.7909,	0.5,
# new cell
	SPHERE,	49.5478,	48.5143,	35.231,	0.5,
# new cell
	SPHERE,	50.1315,	48.6411,	34.6711,	0.5,
# new cell
	SPHERE,	50.7152,	48.7679,	34.1112,	0.5,
# new cell
	SPHERE,	51.2989,	48.8947,	33.5513,	0.5,
# new cell
	SPHERE,	48.0314,	48.5768,	36.8161,	0.5,
# new cell
	SPHERE,	48.6151,	48.7036,	36.2562,	0.5,
# new cell
	SPHERE,	49.1988,	48.8304,	35.6963,	0.5,
# new cell
	SPHERE,	49.7825,	48.9572,	35.1364,	0.5,
# new cell
	SPHERE,	50.3662,	49.084,	34.5765,	0.5,
# new cell
	SPHERE,	50.9499,	49.2108,	34.0166,	0.5,
# new cell
	SPHERE,	48.2661,	49.0197,	36.7215,	0.5,
# new cell
	SPHERE,	48.8498,	49.1465,	36.1616,	0.5,
# new cell
	SPHERE,	49.4335,	49.2733,	35.6017,	0.5,
# new cell
	SPHERE,	50.0172,	49.4001,	35.0418,	0.5,
# new cell
	SPHERE,	50.6009,	49.5269,	34.4819,	0.5,
# new cell
	SPHERE,	48.5008,	49.4626,	36.6269,	0.5,
# new cell
	SPHERE,	49.0845,	49.5894,	36.067,	0.5,
# new cell
	SPHERE,	49.6682,	49.7162,	35.5071,	0.5,
# new cell
	SPHERE,	50.2519,	49.843,	34.9472,	0.5,
# new cell
	SPHERE,	48.7355,	49.9055,	36.5323,	0.5,
# new cell
	SPHERE,	49.3192,	50.0323,	35.9724,	0.5,
# new cell
	SPHERE,	49.9029,	50.1591,	35.4125,	0.5,
# new cell
	SPHERE,	48.9702,	50.3484,	36.4377,	0.5,
# new cell
	SPHERE,	49.5539,	50.4752,	35.8778,	0.5,
# new cell
	SPHERE,	49.2049,	50.7913,	36.3431,	0.5,
# new cell
	SPHERE,	47.3922,	47.0554,	37.281,	0.5,
# new cell
	SPHERE,	47.9759,	47.1822,	36.7211,	0.5,
# new cell
	SPHERE,	48.5596,	47.309,	36.1612,	0.5,
# new cell
	SPHERE,	49.1433,	47.4358,	35.6013,	0.5,
# new cell
	SPHERE,	49.727,	47.5626,	35.0414,	0.5,
# new cell
	SPHERE,	50.3107,	47.6894,	34.4815,	0.5,
# new cell
	SPHERE,	50.8944,	47.8162,	33.9216,	0.5,
# new cell
	SPHERE,	51.4781,	47.943,	33.3617,	0.5,
# new cell
	SPHERE,	52.0618,	48.0698,	32.8018,	0.5,
# new cell
	SPHERE,	47.6269,	47.4983,	37.1864,	0.5,
# new cell
	SPHERE,	48.2106,	47.6251,	36.6265,	0.5,
# new cell
	SPHERE,	48.7943,	47.7519,	36.0666,	0.5,
# new cell
	SPHERE,	49.378,	47.8787,	35.5067,	0.5,
# new cell
	SPHERE,	49.9617,	48.0055,	34.9468,	0.5,
# new cell
	SPHERE,	50.5454,	48.1323,	34.3869,	0.5,
# new cell
	SPHERE,	51.1291,	48.2591,	33.827,	0.5,
# new cell
	SPHERE,	51.7128,	48.3859,	33.2671,	0.5,
# new cell
	SPHERE,	47.8616,	47.9412,	37.0918,	0.5,
# new cell
	SPHERE,	48.4453,	48.068,	36.5319,	0.5,
# new cell
	SPHERE,	49.029,	48.1948,	35.972,	0.5,
# new cell
	SPHERE,	49.6127,	48.3216,	35.4121,	0.5,
# new cell
	SPHERE,	50.1964,	48.4484,	34.8522,	0.5,
# new cell
	SPHERE,	50.7801,	48.5752,	34.2923,	0.5,
# new cell
	SPHERE,	51.3638,	48.702,	33.7324,	0.5,
# new cell
	SPHERE,	48.0963,	48.3841,	36.9972,	0.5,
# new cell
	SPHERE,	48.68,	48.5109,	36.4373,	0.5,
# new cell
	SPHERE,	49.2637,	48.6377,	35.8774,	0.5,
# new cell
	SPHERE,	49.8474,	48.7645,	35.3175,	0.5,
# new cell
	SPHERE,	50.4311,	48.8913,	34.7576,	0.5,
# new cell
	SPHERE,	51.0148,	49.0181,	34.1977,	0.5,
# new cell
	SPHERE,	48.331,	48.827,	36.9026,	0.5,
# new cell
	SPHERE,	48.9147,	48.9538,	36.3427,	0.5,
# new cell
	SPHERE,	49.4984,	49.0806,	35.7828,	0.5,
# new cell
	SPHERE,	50.0821,	49.2074,	35.2229,	0.5,
# new cell
	SPHERE,	50.6658,	49.3342,	34.663,	0.5,
# new cell
	SPHERE,	48.5657,	49.2699,	36.808,	0.5,
# new cell
	SPHERE,	49.1494,	49.3967,	36.2481,	0.5,
# new cell
	SPHERE,	49.7331,	49.5235,	35.6882,	0.5,
# new cell
	SPHERE,	50.3168,	49.6503,	35.1283,	0.5,
# new cell
	SPHERE,	48.8004,	49.7128,	36.7134,	0.5,
# new cell
	SPHERE,	49.3841,	49.8396,	36.1535,	0.5,
# new cell
	SPHERE,	49.9678,	49.9664,	35.5936,	0.5,
# new cell
	SPHERE,	49.0351,	50.1557,	36.6188,	0.5,
# new cell
	SPHERE,	49.6188,	50.2825,	36.0589,	0.5,
# new cell
	SPHERE,	49.2698,	50.5986,	36.5242,	0.5,
# new cell
	SPHERE,	47.6918,	47.3056,	37.3675,	0.5,
# new cell
	SPHERE,	48.2755,	47.4324,	36.8076,	0.5,
# new cell
	SPHERE,	48.8592,	47.5592,	36.2477,	0.5,
# new cell
	SPHERE,	49.4429,	47.686,	35.6878,	0.5,
# new cell
	SPHERE,	50.0266,	47.8128,	35.1279,	0.5,
# new cell
	SPHERE,	50.6103,	47.9396,	34.568,	0.5,
# new cell
	SPHERE,	51.194,	48.0664,	34.0081,	0.5,
# new cell
	SPHERE,	51.7777,	48.1932,	33.4482,	0.5,
# new cell
	SPHERE,	47.9265,	47.7485,	37.2729,	0.5,
# new cell
	SPHERE,	48.5102,	47.8753,	36.713,	0.5,
# new cell
	SPHERE,	49.0939,	48.0021,	36.1531,	0.5,
# new cell
	SPHERE,	49.6776,	48.1289,	35.5932,	0.5,
# new cell
	SPHERE,	50.2613,	48.2557,	35.0333,	0.5,
# new cell
	SPHERE,	50.845,	48.3825,	34.4734,	0.5,
# new cell
	SPHERE,	51.4287,	48.5093,	33.9135,	0.5,
# new cell
	SPHERE,	48.1612,	48.1914,	37.1783,	0.5,
# new cell
	SPHERE,	48.7449,	48.3182,	36.6184,	0.5,
# new cell
	SPHERE,	49.3286,	48.445,	36.0585,	0.5,
# new cell
	SPHERE,	49.9123,	48.5718,	35.4986,	0.5,
# new cell
	SPHERE,	50.496,	48.6986,	34.9387,	0.5,
# new cell
	SPHERE,	51.0797,	48.8254,	34.3788,	0.5,
# new cell
	SPHERE,	48.3959,	48.6343,	37.0837,	0.5,
# new cell
	SPHERE,	48.9796,	48.7611,	36.5238,	0.5,
# new cell
	SPHERE,	49.5633,	48.8879,	35.9639,	0.5,
# new cell
	SPHERE,	50.147,	49.0147,	35.404,	0.5,
# new cell
	SPHERE,	50.7307,	49.1415,	34.8441,	0.5,
# new cell
	SPHERE,	48.6306,	49.0772,	36.9891,	0.5,
# new cell
	SPHERE,	49.2143,	49.204,	36.4292,	0.5,
# new cell
	SPHERE,	49.798,	49.3308,	35.8693,	0.5,
# new cell
	SPHERE,	50.3817,	49.4576,	35.3094,	0.5,
# new cell
	SPHERE,	48.8653,	49.5201,	36.8945,	0.5,
# new cell
	SPHERE,	49.449,	49.6469,	36.3346,	0.5,
# new cell
	SPHERE,	50.0327,	49.7737,	35.7747,	0.5,
# new cell
	SPHERE,	49.1,	49.963,	36.7999,	0.5,
# new cell
	SPHERE,	49.6837,	50.0898,	36.24,	0.5,
# new cell
	SPHERE,	49.3347,	50.4059,	36.7053,	0.5,
# new cell
	SPHERE,	47.9914,	47.5558,	37.454,	0.5,
# new cell
	SPHERE,	48.5751,	47.6826,	36.8941,	0.5,
# new cell
	SPHERE,	49.1588,	47.8094,	36.3342,	0.5,
# new cell
	SPHERE,	49.7425,	47.9362,	35.7743,	0.5,
# new cell
	SPHERE,	50.3262,	48.063,	35.2144,	0.5,
# new cell
	SPHERE,	50.9099,	48.1898,	34.6545,	0.5,
# new cell
	SPHERE,	51.4936,	48.3166,	34.0946,	0.5,
# new cell
	SPHERE,	48.2261,	47.9987,	37.3594,	0.5,
# new cell
	SPHERE,	48.8098,	48.1255,	36.7995,	0.5,
# new cell
	SPHERE,	49.3935,	48.2523,	36.2396,	0.5,
# new cell
	SPHERE,	49.9772,	48.3791,	35.6797,	0.5,
# new cell
	SPHERE,	50.5609,	48.5059,	35.1198,	0.5,
# new cell
	SPHERE,	51.1446,	48.6327,	34.5599,	0.5,
# new cell
	SPHERE,	48.4608,	48.4416,	37.2648,	0.5,
# new cell
	SPHERE,	49.0445,	48.5684,	36.7049,	0.5,
# new cell
	SPHERE,	49.6282,	48.6952,	36.145,	0.5,
# new cell
	SPHERE,	50.2119,	48.822,	35.5851,	0.5,
# new cell
	SPHERE,	50.7956,	48.9488,	35.0252,	0.5,
# new cell
	SPHERE,	48.6955,	48.8845,	37.1702,	0.5,
# new cell
	SPHERE,	49.2792,	49.0113,	36.6103,	0.5,
# new cell
	SPHERE,	49.8629,	49.1381,	36.0504,	0.5,
# new cell
	SPHERE,	50.4466,	49.2649,	35.4905,	0.5,
# new cell
	SPHERE,	48.9302,	49.3274,	37.0756,	0.5,
# new cell
	SPHERE,	49.5139,	49.4542,	36.5157,	0.5,
# new cell
	SPHERE,	50.0976,	49.581,	35.9558,	0.5,
# new cell
	SPHERE,	49.1649,	49.7703,	36.981,	0.5,
# new cell
	SPHERE,	49.7486,	49.8971,	36.4211,	0.5,
# new cell
	SPHERE,	49.3996,	50.2132,	36.8864,	0.5,
# new cell
	SPHERE,	48.291,	47.806,	37.5405,	0.5,
# new cell
	SPHERE,	48.8747,	47.9328,	36.9806,	0.5,
# new cell
	SPHERE,	49.4584,	48.0596,	36.4207,	0.5,
# new cell
	SPHERE,	50.0421,	48.1864,	35.8608,	0.5,
# new cell
	SPHERE,	50.6258,	48.3132,	35.3009,	0.5,
# new cell
	SPHERE,	51.2095,	48.44,	34.741,	0.5,
# new cell
	SPHERE,	48.5257,	48.2489,	37.4459,	0.5,
# new cell
	SPHERE,	49.1094,	48.3757,	36.886,	0.5,
# new cell
	SPHERE,	49.6931,	48.5025,	36.3261,	0.5,
# new cell
	SPHERE,	50.2768,	48.6293,	35.7662,	0.5,
# new cell
	SPHERE,	50.8605,	48.7561,	35.2063,	0.5,
# new cell
	SPHERE,	48.7604,	48.6918,	37.3513,	0.5,
# new cell
	SPHERE,	49.3441,	48.8186,	36.7914,	0.5,
# new cell
	SPHERE,	49.9278,	48.9454,	36.2315,	0.5,
# new cell
	SPHERE,	50.5115,	49.0722,	35.6716,	0.5,
# new cell
	SPHERE,	48.9951,	49.1347,	37.2567,	0.5,
# new cell
	SPHERE,	49.5788,	49.2615,	36.6968,	0.5,
# new cell
	SPHERE,	50.1625,	49.3883,	36.1369,	0.5,
# new cell
	SPHERE,	49.2298,	49.5776,	37.1621,	0.5,
# new cell
	SPHERE,	49.8135,	49.7044,	36.6022,	0.5,
# new cell
	SPHERE,	49.4645,	50.0205,	37.0675,	0.5,
# new cell
	SPHERE,	48.5906,	48.0562,	37.627,	0.5,
# new cell
	SPHERE,	49.1743,	48.183,	37.0671,	0.5,
# new cell
	SPHERE,	49.758,	48.3098,	36.5072,	0.5,
# new cell
	SPHERE,	50.3417,	48.4366,	35.9473,	0.5,
# new cell
	SPHERE,	50.9254,	48.5634,	35.3874,	0.5,
# new cell
	SPHERE,	48.8253,	48.4991,	37.5324,	0.5,
# new cell
	SPHERE,	49.409,	48.6259,	36.9725,	0.5,
# new cell
	SPHERE,	49.9927,	48.7527,	36.4126,	0.5,
# new cell
	SPHERE,	50.5764,	48.8795,	35.8527,	0.5,
# new cell
	SPHERE,	49.06,	48.942,	37.4378,	0.5,
# new cell
	SPHERE,	49.6437,	49.0688,	36.8779,	0.5,
# new cell
	SPHERE,	50.2274,	49.1956,	36.318,	0.5,
# new cell
	SPHERE,	49.2947,	49.3849,	37.3432,	0.5,
# new cell
	SPHERE,	49.8784,	49.5117,	36.7833,	0.5,
# new cell
	SPHERE,	49.5294,	49.8278,	37.2486,	0.5,
# new cell
	SPHERE,	48.8902,	48.3064,	37.7135,	0.5,
# new cell
	SPHERE,	49.4739,	48.4332,	37.1536,	0.5,
# new cell
	SPHERE,	50.0576,	48.56,	36.5937,	0.5,
# new cell
	SPHERE,	50.6413,	48.6868,	36.0338,	0.5,
# new cell
	SPHERE,	49.1249,	48.7493,	37.6189,	0.5,
# new cell
	SPHERE,	49.7086,	48.8761,	37.059,	0.5,
# new cell
	SPHERE,	50.2923,	49.0029,	36.4991,	0.5,
# new cell
	SPHERE,	49.3596,	49.1922,	37.5243,	0.5,
# new cell
	SPHERE,	49.9433,	49.319,	36.9644,	0.5,
# new cell
	SPHERE,	49.5943,	49.6351,	37.4297,	0.5,
# new cell
	SPHERE,	49.1898,	48.5566,	37.8,	0.5,
# new cell
	SPHERE,	49.7735,	48.6834,	37.2401,	0.5,
# new cell
	SPHERE,	50.3572,	48.8102,	36.6802,	0.5,
# new cell
	SPHERE,	49.4245,	48.9995,	37.7054,	0.5,
# new cell
	SPHERE,	50.0082,	49.1263,	37.1455,	0.5,
# new cell
	SPHERE,	49.6592,	49.4424,	37.6108,	0.5,
# new cell
	SPHERE,	49.4894,	48.8068,	37.8865,	0.5,
# new cell
	SPHERE,	50.0731,	48.9336,	37.3266,	0.5,
# new cell
	SPHERE,	49.7241,	49.2497,	37.7919,	0.5,
# new cell
	SPHERE,	49.789,	49.057,	37.973,	0.5,
# new cell
	SPHERE,	46.793,	46.555,	37.108,	0.5,
# new cell
	SPHERE,	47.0277,	46.9979,	37.0134,	0.5,
# new cell
	SPHERE,	47.2624,	47.4408,	36.9188,	0.5,
# new cell
	SPHERE,	47.4971,	47.8837,	36.8242,	0.5,
# new cell
	SPHERE,	47.7318,	48.3266,	36.7296,	0.5,
# new cell
	SPHERE,	47.9665,	48.7695,	36.635,	0.5,
# new cell
	SPHERE,	48.2012,	49.2124,	36.5404,	0.5,
# new cell
	SPHERE,	48.4359,	49.6553,	36.4458,	0.5,
# new cell
	SPHERE,	48.6706,	50.0982,	36.3512,	0.5,
# new cell
	SPHERE,	48.9053,	50.5411,	36.2566,	0.5,
# new cell
	SPHERE,	49.14,	50.984,	36.162,	0.5,
# new cell
	SPHERE,	47.3767,	46.6818,	36.5481,	0.5,
# new cell
	SPHERE,	47.6114,	47.1247,	36.4535,	0.5,
# new cell
	SPHERE,	47.8461,	47.5676,	36.3589,	0.5,
# new cell
	SPHERE,	48.0808,	48.0105,	36.2643,	0.5,
# new cell
	SPHERE,	48.3155,	48.4534,	36.1697,	0.5,
# new cell
	SPHERE,	48.5502,	48.8963,	36.0751,	0.5,
# new cell
	SPHERE,	48.7849,	49.3392,	35.9805,	0.5,
# new cell
	SPHERE,	49.0196,	49.7821,	35.8859,	0.5,
# new cell
	SPHERE,	49.2543,	50.225,	35.7913,	0.5,
# new cell
	SPHERE,	49.489,	50.6679,	35.6967,	0.5,
# new cell
	SPHERE,	47.9604,	46.8086,	35.9882,	0.5,
# new cell
	SPHERE,	48.1951,	47.2515,	35.8936,	0.5,
# new cell
	SPHERE,	48.4298,	47.6944,	35.799,	0.5,
# new cell
	SPHERE,	48.6645,	48.1373,	35.7044,	0.5,
# new cell
	SPHERE,	48.8992,	48.5802,	35.6098,	0.5,
# new cell
	SPHERE,	49.1339,	49.0231,	35.5152,	0.5,
# new cell
	SPHERE,	49.3686,	49.466,	35.4206,	0.5,
# new cell
	SPHERE,	49.6033,	49.9089,	35.326,	0.5,
# new cell
	SPHERE,	49.838,	50.3518,	35.2314,	0.5,
# new cell
	SPHERE,	48.5441,	46.9354,	35.4283,	0.5,
# new cell
	SPHERE,	48.7788,	47.3783,	35.3337,	0.5,
# new cell
	SPHERE,	49.0135,	47.8212,	35.2391,	0.5,
# new cell
	SPHERE,	49.2482,	48.2641,	35.1445,	0.5,
# new cell
	SPHERE,	49.4829,	48.707,	35.0499,	0.5,
# new cell
	SPHERE,	49.7176,	49.1499,	34.9553,	0.5,
# new cell
	SPHERE,	49.9523,	49.5928,	34.8607,	0.5,
# new cell
	SPHERE,	50.187,	50.0357,	34.7661,	0.5,
# new cell
	SPHERE,	49.1278,	47.0622,	34.8684,	0.5,
# new cell
	SPHERE,	49.3625,	47.5051,	34.7738,	0.5,
# new cell
	SPHERE,	49.5972,	47.948,	34.6792,	0.5,
# new cell
	SPHERE,	49.8319,	48.3909,	34.5846,	0.5,
# new cell
	SPHERE,	50.0666,	48.8338,	34.49,	0.5,
# new cell
	SPHERE,	50.3013,	49.2767,	34.3954,	0.5,
# new cell
	SPHERE,	50.536,	49.7196,	34.3008,	0.5,
# new cell
	SPHERE,	49.7115,	47.189,	34.3085,	0.5,
# new cell
	SPHERE,	49.9462,	47.6319,	34.2139,	0.5,
# new cell
	SPHERE,	50.1809,	48.0748,	34.1193,	0.5,
# new cell
	SPHERE,	50.4156,	48.5177,	34.0247,	0.5,
# new cell
	SPHERE,	50.6503,	48.9606,	33.9301,	0.5,
# new cell
	SPHERE,	50.885,	49.4035,	33.8355,	0.5,
# new cell
	SPHERE,	50.2952,	47.3158,	33.7486,	0.5,
# new cell
	SPHERE,	50.5299,	47.7587,	33.654,	0.5,
# new cell
	SPHERE,	50.7646,	48.2016,	33.5594,	0.5,
# new cell
	SPHERE,	50.9993,	48.6445,	33.4648,	0.5,
# new cell
	SPHERE,	51.234,	49.0874,	33.3702,	0.5,
# new cell
	SPHERE,	50.8789,	47.4426,	33.1887,	0.5,
# new cell
	SPHERE,	51.1136,	47.8855,	33.0941,	0.5,
# new cell
	SPHERE,	51.3483,	48.3284,	32.9995,	0.5,
# new cell
	SPHERE,	51.583,	48.7713,	32.9049,	0.5,
# new cell
	SPHERE,	51.4626,	47.5694,	32.6288,	0.5,
# new cell
	SPHERE,	51.6973,	48.0123,	32.5342,	0.5,
# new cell
	SPHERE,	51.932,	48.4552,	32.4396,	0.5,
# new cell
	SPHERE,	52.0463,	47.6962,	32.0689,	0.5,
# new cell
	SPHERE,	52.281,	48.1391,	31.9743,	0.5,
# new cell
	SPHERE,	52.63,	47.823,	31.509,	0.5,
# new cell
	SPHERE,	46.723,	46.7598,	36.9981,	0.5,
# new cell
	SPHERE,	46.9577,	47.2027,	36.9035,	0.5,
# new cell
	SPHERE,	47.1924,	47.6456,	36.8089,	0.5,
# new cell
	SPHERE,	47.4271,	48.0885,	36.7143,	0.5,
# new cell
	SPHERE,	47.6618,	48.5314,	36.6197,	0.5,
# new cell
	SPHERE,	47.8965,	48.9743,	36.5251,	0.5,
# new cell
	SPHERE,	48.1312,	49.4172,	36.4305,	0.5,
# new cell
	SPHERE,	48.3659,	49.8601,	36.3359,	0.5,
# new cell
	SPHERE,	48.6006,	50.303,	36.2413,	0.5,
# new cell
	SPHERE,	48.8353,	50.7459,	36.1467,	0.5,
# new cell
	SPHERE,	47.3067,	46.8866,	36.4382,	0.5,
# new cell
	SPHERE,	47.5414,	47.3295,	36.3436,	0.5,
# new cell
	SPHERE,	47.7761,	47.7724,	36.249,	0.5,
# new cell
	SPHERE,	48.0108,	48.2153,	36.1544,	0.5,
# new cell
	SPHERE,	48.2455,	48.6582,	36.0598,	0.5,
# new cell
	SPHERE,	48.4802,	49.1011,	35.9652,	0.5,
# new cell
	SPHERE,	48.7149,	49.544,	35.8706,	0.5,
# new cell
	SPHERE,	48.9496,	49.9869,	35.776,	0.5,
# new cell
	SPHERE,	49.1843,	50.4298,	35.6814,	0.5,
# new cell
	SPHERE,	47.8904,	47.0134,	35.8783,	0.5,
# new cell
	SPHERE,	48.1251,	47.4563,	35.7837,	0.5,
# new cell
	SPHERE,	48.3598,	47.8992,	35.6891,	0.5,
# new cell
	SPHERE,	48.5945,	48.3421,	35.5945,	0.5,
# new cell
	SPHERE,	48.8292,	48.785,	35.4999,	0.5,
# new cell
	SPHERE,	49.0639,	49.2279,	35.4053,	0.5,
# new cell
	SPHERE,	49.2986,	49.6708,	35.3107,	0.5,
# new cell
	SPHERE,	49.5333,	50.1137,	35.2161,	0.5,
# new cell
	SPHERE,	48.4741,	47.1402,	35.3184,	0.5,
# new cell
	SPHERE,	48.7088,	47.5831,	35.2238,	0.5,
# new cell
	SPHERE,	48.9435,	48.026,	35.1292,	0.5,
# new cell
	SPHERE,	49.1782,	48.4689,	35.0346,	0.5,
# new cell
	SPHERE,	49.4129,	48.9118,	34.94,	0.5,
# new cell
	SPHERE,	49.6476,	49.3547,	34.8454,	0.5,
# new cell
	SPHERE,	49.8823,	49.7976,	34.7508,	0.5,
# new cell
	SPHERE,	49.0578,	47.267,	34.7585,	0.5,
# new cell
	SPHERE,	49.2925,	47.7099,	34.6639,	0.5,
# new cell
	SPHERE,	49.5272,	48.1528,	34.5693,	0.5,
# new cell
	SPHERE,	49.7619,	48.5957,	34.4747,	0.5,
# new cell
	SPHERE,	49.9966,	49.0386,	34.3801,	0.5,
# new cell
	SPHERE,	50.2313,	49.4815,	34.2855,	0.5,
# new cell
	SPHERE,	49.6415,	47.3938,	34.1986,	0.5,
# new cell
	SPHERE,	49.8762,	47.8367,	34.104,	0.5,
# new cell
	SPHERE,	50.1109,	48.2796,	34.0094,	0.5,
# new cell
	SPHERE,	50.3456,	48.7225,	33.9148,	0.5,
# new cell
	SPHERE,	50.5803,	49.1654,	33.8202,	0.5,
# new cell
	SPHERE,	50.2252,	47.5206,	33.6387,	0.5,
# new cell
	SPHERE,	50.4599,	47.9635,	33.5441,	0.5,
# new cell
	SPHERE,	50.6946,	48.4064,	33.4495,	0.5,
# new cell
	SPHERE,	50.9293,	48.8493,	33.3549,	0.5,
# new cell
	SPHERE,	50.8089,	47.6474,	33.0788,	0.5,
# new cell
	SPHERE,	51.0436,	48.0903,	32.9842,	0.5,
# new cell
	SPHERE,	51.2783,	48.5332,	32.8896,	0.5,
# new cell
	SPHERE,	51.3926,	47.7742,	32.5189,	0.5,
# new cell
	SPHERE,	51.6273,	48.2171,	32.4243,	0.5,
# new cell
	SPHERE,	51.9763,	47.901,	31.959,	0.5,
# new cell
	SPHERE,	46.653,	46.9646,	36.8882,	0.5,
# new cell
	SPHERE,	46.8877,	47.4075,	36.7936,	0.5,
# new cell
	SPHERE,	47.1224,	47.8504,	36.699,	0.5,
# new cell
	SPHERE,	47.3571,	48.2933,	36.6044,	0.5,
# new cell
	SPHERE,	47.5918,	48.7362,	36.5098,	0.5,
# new cell
	SPHERE,	47.8265,	49.1791,	36.4152,	0.5,
# new cell
	SPHERE,	48.0612,	49.622,	36.3206,	0.5,
# new cell
	SPHERE,	48.2959,	50.0649,	36.226,	0.5,
# new cell
	SPHERE,	48.5306,	50.5078,	36.1314,	0.5,
# new cell
	SPHERE,	47.2367,	47.0914,	36.3283,	0.5,
# new cell
	SPHERE,	47.4714,	47.5343,	36.2337,	0.5,
# new cell
	SPHERE,	47.7061,	47.9772,	36.1391,	0.5,
# new cell
	SPHERE,	47.9408,	48.4201,	36.0445,	0.5,
# new cell
	SPHERE,	48.1755,	48.863,	35.9499,	0.5,
# new cell
	SPHERE,	48.4102,	49.3059,	35.8553,	0.5,
# new cell
	SPHERE,	48.6449,	49.7488,	35.7607,	0.5,
# new cell
	SPHERE,	48.8796,	50.1917,	35.6661,	0.5,
# new cell
	SPHERE,	47.8204,	47.2182,	35.7684,	0.5,
# new cell
	SPHERE,	48.0551,	47.6611,	35.6738,	0.5,
# new cell
	SPHERE,	48.2898,	48.104,	35.5792,	0.5,
# new cell
	SPHERE,	48.5245,	48.5469,	35.4846,	0.5,
# new cell
	SPHERE,	48.7592,	48.9898,	35.39,	0.5,
# new cell
	SPHERE,	48.9939,	49.4327,	35.2954,	0.5,
# new cell
	SPHERE,	49.2286,	49.8756,	35.2008,	0.5,
# new cell
	SPHERE,	48.4041,	47.345,	35.2085,	0.5,
# new cell
	SPHERE,	48.6388,	47.7879,	35.1139,	0.5,
# new cell
	SPHERE,	48.8735,	48.2308,	35.0193,	0.5,
# new cell
	SPHERE,	49.1082,	48.6737,	34.9247,	0.5,
# new cell
	SPHERE,	49.3429,	49.1166,	34.8301,	0.5,
# new cell
	SPHERE,	49.5776,	49.5595,	34.7355,	0.5,
# new cell
	SPHERE,	48.9878,	47.4718,	34.6486,	0.5,
# new cell
	SPHERE,	49.2225,	47.9147,	34.554,	0.5,
# new cell
	SPHERE,	49.4572,	48.3576,	34.4594,	0.5,
# new cell
	SPHERE,	49.6919,	48.8005,	34.3648,	0.5,
# new cell
	SPHERE,	49.9266,	49.2434,	34.2702,	0.5,
# new cell
	SPHERE,	49.5715,	47.5986,	34.0887,	0.5,
# new cell
	SPHERE,	49.8062,	48.0415,	33.9941,	0.5,
# new cell
	SPHERE,	50.0409,	48.4844,	33.8995,	0.5,
# new cell
	SPHERE,	50.2756,	48.9273,	33.8049,	0.5,
# new cell
	SPHERE,	50.1552,	47.7254,	33.5288,	0.5,
# new cell
	SPHERE,	50.3899,	48.1683,	33.4342,	0.5,
# new cell
	SPHERE,	50.6246,	48.6112,	33.3396,	0.5,
# new cell
	SPHERE,	50.7389,	47.8522,	32.9689,	0.5,
# new cell
	SPHERE,	50.9736,	48.2951,	32.8743,	0.5,
# new cell
	SPHERE,	51.3226,	47.979,	32.409,	0.5,
# new cell
	SPHERE,	46.583,	47.1694,	36.7783,	0.5,
# new cell
	SPHERE,	46.8177,	47.6123,	36.6837,	0.5,
# new cell
	SPHERE,	47.0524,	48.0552,	36.5891,	0.5,
# new cell
	SPHERE,	47.2871,	48.4981,	36.4945,	0.5,
# new cell
	SPHERE,	47.5218,	48.941,	36.3999,	0.5,
# new cell
	SPHERE,	47.7565,	49.3839,	36.3053,	0.5,
# new cell
	SPHERE,	47.9912,	49.8268,	36.2107,	0.5,
# new cell
	SPHERE,	48.2259,	50.2697,	36.1161,	0.5,
# new cell
	SPHERE,	47.1667,	47.2962,	36.2184,	0.5,
# new cell
	SPHERE,	47.4014,	47.7391,	36.1238,	0.5,
# new cell
	SPHERE,	47.6361,	48.182,	36.0292,	0.5,
# new cell
	SPHERE,	47.8708,	48.6249,	35.9346,	0.5,
# new cell
	SPHERE,	48.1055,	49.0678,	35.84,	0.5,
# new cell
	SPHERE,	48.3402,	49.5107,	35.7454,	0.5,
# new cell
	SPHERE,	48.5749,	49.9536,	35.6508,	0.5,
# new cell
	SPHERE,	47.7504,	47.423,	35.6585,	0.5,
# new cell
	SPHERE,	47.9851,	47.8659,	35.5639,	0.5,
# new cell
	SPHERE,	48.2198,	48.3088,	35.4693,	0.5,
# new cell
	SPHERE,	48.4545,	48.7517,	35.3747,	0.5,
# new cell
	SPHERE,	48.6892,	49.1946,	35.2801,	0.5,
# new cell
	SPHERE,	48.9239,	49.6375,	35.1855,	0.5,
# new cell
	SPHERE,	48.3341,	47.5498,	35.0986,	0.5,
# new cell
	SPHERE,	48.5688,	47.9927,	35.004,	0.5,
# new cell
	SPHERE,	48.8035,	48.4356,	34.9094,	0.5,
# new cell
	SPHERE,	49.0382,	48.8785,	34.8148,	0.5,
# new cell
	SPHERE,	49.2729,	49.3214,	34.7202,	0.5,
# new cell
	SPHERE,	48.9178,	47.6766,	34.5387,	0.5,
# new cell
	SPHERE,	49.1525,	48.1195,	34.4441,	0.5,
# new cell
	SPHERE,	49.3872,	48.5624,	34.3495,	0.5,
# new cell
	SPHERE,	49.6219,	49.0053,	34.2549,	0.5,
# new cell
	SPHERE,	49.5015,	47.8034,	33.9788,	0.5,
# new cell
	SPHERE,	49.7362,	48.2463,	33.8842,	0.5,
# new cell
	SPHERE,	49.9709,	48.6892,	33.7896,	0.5,
# new cell
	SPHERE,	50.0852,	47.9302,	33.4189,	0.5,
# new cell
	SPHERE,	50.3199,	48.3731,	33.3243,	0.5,
# new cell
	SPHERE,	50.6689,	48.057,	32.859,	0.5,
# new cell
	SPHERE,	46.513,	47.3742,	36.6684,	0.5,
# new cell
	SPHERE,	46.7477,	47.8171,	36.5738,	0.5,
# new cell
	SPHERE,	46.9824,	48.26,	36.4792,	0.5,
# new cell
	SPHERE,	47.2171,	48.7029,	36.3846,	0.5,
# new cell
	SPHERE,	47.4518,	49.1458,	36.29,	0.5,
# new cell
	SPHERE,	47.6865,	49.5887,	36.1954,	0.5,
# new cell
	SPHERE,	47.9212,	50.0316,	36.1008,	0.5,
# new cell
	SPHERE,	47.0967,	47.501,	36.1085,	0.5,
# new cell
	SPHERE,	47.3314,	47.9439,	36.0139,	0.5,
# new cell
	SPHERE,	47.5661,	48.3868,	35.9193,	0.5,
# new cell
	SPHERE,	47.8008,	48.8297,	35.8247,	0.5,
# new cell
	SPHERE,	48.0355,	49.2726,	35.7301,	0.5,
# new cell
	SPHERE,	48.2702,	49.7155,	35.6355,	0.5,
# new cell
	SPHERE,	47.6804,	47.6278,	35.5486,	0.5,
# new cell
	SPHERE,	47.9151,	48.0707,	35.454,	0.5,
# new cell
	SPHERE,	48.1498,	48.5136,	35.3594,	0.5,
# new cell
	SPHERE,	48.3845,	48.9565,	35.2648,	0.5,
# new cell
	SPHERE,	48.6192,	49.3994,	35.1702,	0.5,
# new cell
	SPHERE,	48.2641,	47.7546,	34.9887,	0.5,
# new cell
	SPHERE,	48.4988,	48.1975,	34.8941,	0.5,
# new cell
	SPHERE,	48.7335,	48.6404,	34.7995,	0.5,
# new cell
	SPHERE,	48.9682,	49.0833,	34.7049,	0.5,
# new cell
	SPHERE,	48.8478,	47.8814,	34.4288,	0.5,
# new cell
	SPHERE,	49.0825,	48.3243,	34.3342,	0.5,
# new cell
	SPHERE,	49.3172,	48.7672,	34.2396,	0.5,
# new cell
	SPHERE,	49.4315,	48.0082,	33.8689,	0.5,
# new cell
	SPHERE,	49.6662,	48.4511,	33.7743,	0.5,
# new cell
	SPHERE,	50.0152,	48.135,	33.309,	0.5,
# new cell
	SPHERE,	46.443,	47.579,	36.5585,	0.5,
# new cell
	SPHERE,	46.6777,	48.0219,	36.4639,	0.5,
# new cell
	SPHERE,	46.9124,	48.4648,	36.3693,	0.5,
# new cell
	SPHERE,	47.1471,	48.9077,	36.2747,	0.5,
# new cell
	SPHERE,	47.3818,	49.3506,	36.1801,	0.5,
# new cell
	SPHERE,	47.6165,	49.7935,	36.0855,	0.5,
# new cell
	SPHERE,	47.0267,	47.7058,	35.9986,	0.5,
# new cell
	SPHERE,	47.2614,	48.1487,	35.904,	0.5,
# new cell
	SPHERE,	47.4961,	48.5916,	35.8094,	0.5,
# new cell
	SPHERE,	47.7308,	49.0345,	35.7148,	0.5,
# new cell
	SPHERE,	47.9655,	49.4774,	35.6202,	0.5,
# new cell
	SPHERE,	47.6104,	47.8326,	35.4387,	0.5,
# new cell
	SPHERE,	47.8451,	48.2755,	35.3441,	0.5,
# new cell
	SPHERE,	48.0798,	48.7184,	35.2495,	0.5,
# new cell
	SPHERE,	48.3145,	49.1613,	35.1549,	0.5,
# new cell
	SPHERE,	48.1941,	47.9594,	34.8788,	0.5,
# new cell
	SPHERE,	48.4288,	48.4023,	34.7842,	0.5,
# new cell
	SPHERE,	48.6635,	48.8452,	34.6896,	0.5,
# new cell
	SPHERE,	48.7778,	48.0862,	34.3189,	0.5,
# new cell
	SPHERE,	49.0125,	48.5291,	34.2243,	0.5,
# new cell
	SPHERE,	49.3615,	48.213,	33.759,	0.5,
# new cell
	SPHERE,	46.373,	47.7838,	36.4486,	0.5,
# new cell
	SPHERE,	46.6077,	48.2267,	36.354,	0.5,
# new cell
	SPHERE,	46.8424,	48.6696,	36.2594,	0.5,
# new cell
	SPHERE,	47.0771,	49.1125,	36.1648,	0.5,
# new cell
	SPHERE,	47.3118,	49.5554,	36.0702,	0.5,
# new cell
	SPHERE,	46.9567,	47.9106,	35.8887,	0.5,
# new cell
	SPHERE,	47.1914,	48.3535,	35.7941,	0.5,
# new cell
	SPHERE,	47.4261,	48.7964,	35.6995,	0.5,
# new cell
	SPHERE,	47.6608,	49.2393,	35.6049,	0.5,
# new cell
	SPHERE,	47.5404,	48.0374,	35.3288,	0.5,
# new cell
	SPHERE,	47.7751,	48.4803,	35.2342,	0.5,
# new cell
	SPHERE,	48.0098,	48.9232,	35.1396,	0.5,
# new cell
	SPHERE,	48.1241,	48.1642,	34.7689,	0.5,
# new cell
	SPHERE,	48.3588,	48.6071,	34.6743,	0.5,
# new cell
	SPHERE,	48.7078,	48.291,	34.209,	0.5,
# new cell
	SPHERE,	46.303,	47.9886,	36.3387,	0.5,
# new cell
	SPHERE,	46.5377,	48.4315,	36.2441,	0.5,
# new cell
	SPHERE,	46.7724,	48.8744,	36.1495,	0.5,
# new cell
	SPHERE,	47.0071,	49.3173,	36.0549,	0.5,
# new cell
	SPHERE,	46.8867,	48.1154,	35.7788,	0.5,
# new cell
	SPHERE,	47.1214,	48.5583,	35.6842,	0.5,
# new cell
	SPHERE,	47.3561,	49.0012,	35.5896,	0.5,
# new cell
	SPHERE,	47.4704,	48.2422,	35.2189,	0.5,
# new cell
	SPHERE,	47.7051,	48.6851,	35.1243,	0.5,
# new cell
	SPHERE,	48.0541,	48.369,	34.659,	0.5,
# new cell
	SPHERE,	46.233,	48.1934,	36.2288,	0.5,
# new cell
	SPHERE,	46.4677,	48.6363,	36.1342,	0.5,
# new cell
	SPHERE,	46.7024,	49.0792,	36.0396,	0.5,
# new cell
	SPHERE,	46.8167,	48.3202,	35.6689,	0.5,
# new cell
	SPHERE,	47.0514,	48.7631,	35.5743,	0.5,
# new cell
	SPHERE,	47.4004,	48.447,	35.109,	0.5,
# new cell
	SPHERE,	46.163,	48.3982,	36.1189,	0.5,
# new cell
	SPHERE,	46.3977,	48.8411,	36.0243,	0.5,
# new cell
	SPHERE,	46.7467,	48.525,	35.559,	0.5,
# new cell
	SPHERE,	46.093,	48.603,	36.009,	0.5,
# new cell
	SPHERE,	43.39,	39.642,	35.368,	0.5,
# new cell
	SPHERE,	43.7303,	40.3333,	35.542,	0.5,
# new cell
	SPHERE,	44.0706,	41.0246,	35.716,	0.5,
# new cell
	SPHERE,	44.4109,	41.7159,	35.89,	0.5,
# new cell
	SPHERE,	44.7512,	42.4072,	36.064,	0.5,
# new cell
	SPHERE,	45.0915,	43.0985,	36.238,	0.5,
# new cell
	SPHERE,	45.4318,	43.7898,	36.412,	0.5,
# new cell
	SPHERE,	45.7721,	44.4811,	36.586,	0.5,
# new cell
	SPHERE,	46.1124,	45.1724,	36.76,	0.5,
# new cell
	SPHERE,	46.4527,	45.8637,	36.934,	0.5,
# new cell
	SPHERE,	46.793,	46.555,	37.108,	0.5,
# new cell
	SPHERE,	43.3352,	40.4755,	35.1521,	0.5,
# new cell
	SPHERE,	43.6755,	41.1668,	35.3261,	0.5,
# new cell
	SPHERE,	44.0158,	41.8581,	35.5001,	0.5,
# new cell
	SPHERE,	44.3561,	42.5494,	35.6741,	0.5,
# new cell
	SPHERE,	44.6964,	43.2407,	35.8481,	0.5,
# new cell
	SPHERE,	45.0367,	43.932,	36.0221,	0.5,
# new cell
	SPHERE,	45.377,	44.6233,	36.1961,	0.5,
# new cell
	SPHERE,	45.7173,	45.3146,	36.3701,	0.5,
# new cell
	SPHERE,	46.0576,	46.0059,	36.5441,	0.5,
# new cell
	SPHERE,	46.3979,	46.6972,	36.7181,	0.5,
# new cell
	SPHERE,	43.2804,	41.309,	34.9362,	0.5,
# new cell
	SPHERE,	43.6207,	42.0003,	35.1102,	0.5,
# new cell
	SPHERE,	43.961,	42.6916,	35.2842,	0.5,
# new cell
	SPHERE,	44.3013,	43.3829,	35.4582,	0.5,
# new cell
	SPHERE,	44.6416,	44.0742,	35.6322,	0.5,
# new cell
	SPHERE,	44.9819,	44.7655,	35.8062,	0.5,
# new cell
	SPHERE,	45.3222,	45.4568,	35.9802,	0.5,
# new cell
	SPHERE,	45.6625,	46.1481,	36.1542,	0.5,
# new cell
	SPHERE,	46.0028,	46.8394,	36.3282,	0.5,
# new cell
	SPHERE,	43.2256,	42.1425,	34.7203,	0.5,
# new cell
	SPHERE,	43.5659,	42.8338,	34.8943,	0.5,
# new cell
	SPHERE,	43.9062,	43.5251,	35.0683,	0.5,
# new cell
	SPHERE,	44.2465,	44.2164,	35.2423,	0.5,
# new cell
	SPHERE,	44.5868,	44.9077,	35.4163,	0.5,
# new cell
	SPHERE,	44.9271,	45.599,	35.5903,	0.5,
# new cell
	SPHERE,	45.2674,	46.2903,	35.7643,	0.5,
# new cell
	SPHERE,	45.6077,	46.9816,	35.9383,	0.5,
# new cell
	SPHERE,	43.1708,	42.976,	34.5044,	0.5,
# new cell
	SPHERE,	43.5111,	43.6673,	34.6784,	0.5,
# new cell
	SPHERE,	43.8514,	44.3586,	34.8524,	0.5,
# new cell
	SPHERE,	44.1917,	45.0499,	35.0264,	0.5,
# new cell
	SPHERE,	44.532,	45.7412,	35.2004,	0.5,
# new cell
	SPHERE,	44.8723,	46.4325,	35.3744,	0.5,
# new cell
	SPHERE,	45.2126,	47.1238,	35.5484,	0.5,
# new cell
	SPHERE,	43.116,	43.8095,	34.2885,	0.5,
# new cell
	SPHERE,	43.4563,	44.5008,	34.4625,	0.5,
# new cell
	SPHERE,	43.7966,	45.1921,	34.6365,	0.5,
# new cell
	SPHERE,	44.1369,	45.8834,	34.8105,	0.5,
# new cell
	SPHERE,	44.4772,	46.5747,	34.9845,	0.5,
# new cell
	SPHERE,	44.8175,	47.266,	35.1585,	0.5,
# new cell
	SPHERE,	43.0612,	44.643,	34.0726,	0.5,
# new cell
	SPHERE,	43.4015,	45.3343,	34.2466,	0.5,
# new cell
	SPHERE,	43.7418,	46.0256,	34.4206,	0.5,
# new cell
	SPHERE,	44.0821,	46.7169,	34.5946,	0.5,
# new cell
	SPHERE,	44.4224,	47.4082,	34.7686,	0.5,
# new cell
	SPHERE,	43.0064,	45.4765,	33.8567,	0.5,
# new cell
	SPHERE,	43.3467,	46.1678,	34.0307,	0.5,
# new cell
	SPHERE,	43.687,	46.8591,	34.2047,	0.5,
# new cell
	SPHERE,	44.0273,	47.5504,	34.3787,	0.5,
# new cell
	SPHERE,	42.9516,	46.31,	33.6408,	0.5,
# new cell
	SPHERE,	43.2919,	47.0013,	33.8148,	0.5,
# new cell
	SPHERE,	43.6322,	47.6926,	33.9888,	0.5,
# new cell
	SPHERE,	42.8968,	47.1435,	33.4249,	0.5,
# new cell
	SPHERE,	43.2371,	47.8348,	33.5989,	0.5,
# new cell
	SPHERE,	42.842,	47.977,	33.209,	0.5,
# new cell
	SPHERE,	43.1656,	40.152,	35.3437,	0.5,
# new cell
	SPHERE,	43.5059,	40.8433,	35.5177,	0.5,
# new cell
	SPHERE,	43.8462,	41.5346,	35.6917,	0.5,
# new cell
	SPHERE,	44.1865,	42.2259,	35.8657,	0.5,
# new cell
	SPHERE,	44.5268,	42.9172,	36.0397,	0.5,
# new cell
	SPHERE,	44.8671,	43.6085,	36.2137,	0.5,
# new cell
	SPHERE,	45.2074,	44.2998,	36.3877,	0.5,
# new cell
	SPHERE,	45.5477,	44.9911,	36.5617,	0.5,
# new cell
	SPHERE,	45.888,	45.6824,	36.7357,	0.5,
# new cell
	SPHERE,	46.2283,	46.3737,	36.9097,	0.5,
# new cell
	SPHERE,	43.1108,	40.9855,	35.1278,	0.5,
# new cell
	SPHERE,	43.4511,	41.6768,	35.3018,	0.5,
# new cell
	SPHERE,	43.7914,	42.3681,	35.4758,	0.5,
# new cell
	SPHERE,	44.1317,	43.0594,	35.6498,	0.5,
# new cell
	SPHERE,	44.472,	43.7507,	35.8238,	0.5,
# new cell
	SPHERE,	44.8123,	44.442,	35.9978,	0.5,
# new cell
	SPHERE,	45.1526,	45.1333,	36.1718,	0.5,
# new cell
	SPHERE,	45.4929,	45.8246,	36.3458,	0.5,
# new cell
	SPHERE,	45.8332,	46.5159,	36.5198,	0.5,
# new cell
	SPHERE,	43.056,	41.819,	34.9119,	0.5,
# new cell
	SPHERE,	43.3963,	42.5103,	35.0859,	0.5,
# new cell
	SPHERE,	43.7366,	43.2016,	35.2599,	0.5,
# new cell
	SPHERE,	44.0769,	43.8929,	35.4339,	0.5,
# new cell
	SPHERE,	44.4172,	44.5842,	35.6079,	0.5,
# new cell
	SPHERE,	44.7575,	45.2755,	35.7819,	0.5,
# new cell
	SPHERE,	45.0978,	45.9668,	35.9559,	0.5,
# new cell
	SPHERE,	45.4381,	46.6581,	36.1299,	0.5,
# new cell
	SPHERE,	43.0012,	42.6525,	34.696,	0.5,
# new cell
	SPHERE,	43.3415,	43.3438,	34.87,	0.5,
# new cell
	SPHERE,	43.6818,	44.0351,	35.044,	0.5,
# new cell
	SPHERE,	44.0221,	44.7264,	35.218,	0.5,
# new cell
	SPHERE,	44.3624,	45.4177,	35.392,	0.5,
# new cell
	SPHERE,	44.7027,	46.109,	35.566,	0.5,
# new cell
	SPHERE,	45.043,	46.8003,	35.74,	0.5,
# new cell
	SPHERE,	42.9464,	43.486,	34.4801,	0.5,
# new cell
	SPHERE,	43.2867,	44.1773,	34.6541,	0.5,
# new cell
	SPHERE,	43.627,	44.8686,	34.8281,	0.5,
# new cell
	SPHERE,	43.9673,	45.5599,	35.0021,	0.5,
# new cell
	SPHERE,	44.3076,	46.2512,	35.1761,	0.5,
# new cell
	SPHERE,	44.6479,	46.9425,	35.3501,	0.5,
# new cell
	SPHERE,	42.8916,	44.3195,	34.2642,	0.5,
# new cell
	SPHERE,	43.2319,	45.0108,	34.4382,	0.5,
# new cell
	SPHERE,	43.5722,	45.7021,	34.6122,	0.5,
# new cell
	SPHERE,	43.9125,	46.3934,	34.7862,	0.5,
# new cell
	SPHERE,	44.2528,	47.0847,	34.9602,	0.5,
# new cell
	SPHERE,	42.8368,	45.153,	34.0483,	0.5,
# new cell
	SPHERE,	43.1771,	45.8443,	34.2223,	0.5,
# new cell
	SPHERE,	43.5174,	46.5356,	34.3963,	0.5,
# new cell
	SPHERE,	43.8577,	47.2269,	34.5703,	0.5,
# new cell
	SPHERE,	42.782,	45.9865,	33.8324,	0.5,
# new cell
	SPHERE,	43.1223,	46.6778,	34.0064,	0.5,
# new cell
	SPHERE,	43.4626,	47.3691,	34.1804,	0.5,
# new cell
	SPHERE,	42.7272,	46.82,	33.6165,	0.5,
# new cell
	SPHERE,	43.0675,	47.5113,	33.7905,	0.5,
# new cell
	SPHERE,	42.6724,	47.6535,	33.4006,	0.5,
# new cell
	SPHERE,	42.9412,	40.662,	35.3194,	0.5,
# new cell
	SPHERE,	43.2815,	41.3533,	35.4934,	0.5,
# new cell
	SPHERE,	43.6218,	42.0446,	35.6674,	0.5,
# new cell
	SPHERE,	43.9621,	42.7359,	35.8414,	0.5,
# new cell
	SPHERE,	44.3024,	43.4272,	36.0154,	0.5,
# new cell
	SPHERE,	44.6427,	44.1185,	36.1894,	0.5,
# new cell
	SPHERE,	44.983,	44.8098,	36.3634,	0.5,
# new cell
	SPHERE,	45.3233,	45.5011,	36.5374,	0.5,
# new cell
	SPHERE,	45.6636,	46.1924,	36.7114,	0.5,
# new cell
	SPHERE,	42.8864,	41.4955,	35.1035,	0.5,
# new cell
	SPHERE,	43.2267,	42.1868,	35.2775,	0.5,
# new cell
	SPHERE,	43.567,	42.8781,	35.4515,	0.5,
# new cell
	SPHERE,	43.9073,	43.5694,	35.6255,	0.5,
# new cell
	SPHERE,	44.2476,	44.2607,	35.7995,	0.5,
# new cell
	SPHERE,	44.5879,	44.952,	35.9735,	0.5,
# new cell
	SPHERE,	44.9282,	45.6433,	36.1475,	0.5,
# new cell
	SPHERE,	45.2685,	46.3346,	36.3215,	0.5,
# new cell
	SPHERE,	42.8316,	42.329,	34.8876,	0.5,
# new cell
	SPHERE,	43.1719,	43.0203,	35.0616,	0.5,
# new cell
	SPHERE,	43.5122,	43.7116,	35.2356,	0.5,
# new cell
	SPHERE,	43.8525,	44.4029,	35.4096,	0.5,
# new cell
	SPHERE,	44.1928,	45.0942,	35.5836,	0.5,
# new cell
	SPHERE,	44.5331,	45.7855,	35.7576,	0.5,
# new cell
	SPHERE,	44.8734,	46.4768,	35.9316,	0.5,
# new cell
	SPHERE,	42.7768,	43.1625,	34.6717,	0.5,
# new cell
	SPHERE,	43.1171,	43.8538,	34.8457,	0.5,
# new cell
	SPHERE,	43.4574,	44.5451,	35.0197,	0.5,
# new cell
	SPHERE,	43.7977,	45.2364,	35.1937,	0.5,
# new cell
	SPHERE,	44.138,	45.9277,	35.3677,	0.5,
# new cell
	SPHERE,	44.4783,	46.619,	35.5417,	0.5,
# new cell
	SPHERE,	42.722,	43.996,	34.4558,	0.5,
# new cell
	SPHERE,	43.0623,	44.6873,	34.6298,	0.5,
# new cell
	SPHERE,	43.4026,	45.3786,	34.8038,	0.5,
# new cell
	SPHERE,	43.7429,	46.0699,	34.9778,	0.5,
# new cell
	SPHERE,	44.0832,	46.7612,	35.1518,	0.5,
# new cell
	SPHERE,	42.6672,	44.8295,	34.2399,	0.5,
# new cell
	SPHERE,	43.0075,	45.5208,	34.4139,	0.5,
# new cell
	SPHERE,	43.3478,	46.2121,	34.5879,	0.5,
# new cell
	SPHERE,	43.6881,	46.9034,	34.7619,	0.5,
# new cell
	SPHERE,	42.6124,	45.663,	34.024,	0.5,
# new cell
	SPHERE,	42.9527,	46.3543,	34.198,	0.5,
# new cell
	SPHERE,	43.293,	47.0456,	34.372,	0.5,
# new cell
	SPHERE,	42.5576,	46.4965,	33.8081,	0.5,
# new cell
	SPHERE,	42.8979,	47.1878,	33.9821,	0.5,
# new cell
	SPHERE,	42.5028,	47.33,	33.5922,	0.5,
# new cell
	SPHERE,	42.7168,	41.172,	35.2951,	0.5,
# new cell
	SPHERE,	43.0571,	41.8633,	35.4691,	0.5,
# new cell
	SPHERE,	43.3974,	42.5546,	35.6431,	0.5,
# new cell
	SPHERE,	43.7377,	43.2459,	35.8171,	0.5,
# new cell
	SPHERE,	44.078,	43.9372,	35.9911,	0.5,
# new cell
	SPHERE,	44.4183,	44.6285,	36.1651,	0.5,
# new cell
	SPHERE,	44.7586,	45.3198,	36.3391,	0.5,
# new cell
	SPHERE,	45.0989,	46.0111,	36.5131,	0.5,
# new cell
	SPHERE,	42.662,	42.0055,	35.0792,	0.5,
# new cell
	SPHERE,	43.0023,	42.6968,	35.2532,	0.5,
# new cell
	SPHERE,	43.3426,	43.3881,	35.4272,	0.5,
# new cell
	SPHERE,	43.6829,	44.0794,	35.6012,	0.5,
# new cell
	SPHERE,	44.0232,	44.7707,	35.7752,	0.5,
# new cell
	SPHERE,	44.3635,	45.462,	35.9492,	0.5,
# new cell
	SPHERE,	44.7038,	46.1533,	36.1232,	0.5,
# new cell
	SPHERE,	42.6072,	42.839,	34.8633,	0.5,
# new cell
	SPHERE,	42.9475,	43.5303,	35.0373,	0.5,
# new cell
	SPHERE,	43.2878,	44.2216,	35.2113,	0.5,
# new cell
	SPHERE,	43.6281,	44.9129,	35.3853,	0.5,
# new cell
	SPHERE,	43.9684,	45.6042,	35.5593,	0.5,
# new cell
	SPHERE,	44.3087,	46.2955,	35.7333,	0.5,
# new cell
	SPHERE,	42.5524,	43.6725,	34.6474,	0.5,
# new cell
	SPHERE,	42.8927,	44.3638,	34.8214,	0.5,
# new cell
	SPHERE,	43.233,	45.0551,	34.9954,	0.5,
# new cell
	SPHERE,	43.5733,	45.7464,	35.1694,	0.5,
# new cell
	SPHERE,	43.9136,	46.4377,	35.3434,	0.5,
# new cell
	SPHERE,	42.4976,	44.506,	34.4315,	0.5,
# new cell
	SPHERE,	42.8379,	45.1973,	34.6055,	0.5,
# new cell
	SPHERE,	43.1782,	45.8886,	34.7795,	0.5,
# new cell
	SPHERE,	43.5185,	46.5799,	34.9535,	0.5,
# new cell
	SPHERE,	42.4428,	45.3395,	34.2156,	0.5,
# new cell
	SPHERE,	42.7831,	46.0308,	34.3896,	0.5,
# new cell
	SPHERE,	43.1234,	46.7221,	34.5636,	0.5,
# new cell
	SPHERE,	42.388,	46.173,	33.9997,	0.5,
# new cell
	SPHERE,	42.7283,	46.8643,	34.1737,	0.5,
# new cell
	SPHERE,	42.3332,	47.0065,	33.7838,	0.5,
# new cell
	SPHERE,	42.4924,	41.682,	35.2708,	0.5,
# new cell
	SPHERE,	42.8327,	42.3733,	35.4448,	0.5,
# new cell
	SPHERE,	43.173,	43.0646,	35.6188,	0.5,
# new cell
	SPHERE,	43.5133,	43.7559,	35.7928,	0.5,
# new cell
	SPHERE,	43.8536,	44.4472,	35.9668,	0.5,
# new cell
	SPHERE,	44.1939,	45.1385,	36.1408,	0.5,
# new cell
	SPHERE,	44.5342,	45.8298,	36.3148,	0.5,
# new cell
	SPHERE,	42.4376,	42.5155,	35.0549,	0.5,
# new cell
	SPHERE,	42.7779,	43.2068,	35.2289,	0.5,
# new cell
	SPHERE,	43.1182,	43.8981,	35.4029,	0.5,
# new cell
	SPHERE,	43.4585,	44.5894,	35.5769,	0.5,
# new cell
	SPHERE,	43.7988,	45.2807,	35.7509,	0.5,
# new cell
	SPHERE,	44.1391,	45.972,	35.9249,	0.5,
# new cell
	SPHERE,	42.3828,	43.349,	34.839,	0.5,
# new cell
	SPHERE,	42.7231,	44.0403,	35.013,	0.5,
# new cell
	SPHERE,	43.0634,	44.7316,	35.187,	0.5,
# new cell
	SPHERE,	43.4037,	45.4229,	35.361,	0.5,
# new cell
	SPHERE,	43.744,	46.1142,	35.535,	0.5,
# new cell
	SPHERE,	42.328,	44.1825,	34.6231,	0.5,
# new cell
	SPHERE,	42.6683,	44.8738,	34.7971,	0.5,
# new cell
	SPHERE,	43.0086,	45.5651,	34.9711,	0.5,
# new cell
	SPHERE,	43.3489,	46.2564,	35.1451,	0.5,
# new cell
	SPHERE,	42.2732,	45.016,	34.4072,	0.5,
# new cell
	SPHERE,	42.6135,	45.7073,	34.5812,	0.5,
# new cell
	SPHERE,	42.9538,	46.3986,	34.7552,	0.5,
# new cell
	SPHERE,	42.2184,	45.8495,	34.1913,	0.5,
# new cell
	SPHERE,	42.5587,	46.5408,	34.3653,	0.5,
# new cell
	SPHERE,	42.1636,	46.683,	33.9754,	0.5,
# new cell
	SPHERE,	42.268,	42.192,	35.2465,	0.5,
# new cell
	SPHERE,	42.6083,	42.8833,	35.4205,	0.5,
# new cell
	SPHERE,	42.9486,	43.5746,	35.5945,	0.5,
# new cell
	SPHERE,	43.2889,	44.2659,	35.7685,	0.5,
# new cell
	SPHERE,	43.6292,	44.9572,	35.9425,	0.5,
# new cell
	SPHERE,	43.9695,	45.6485,	36.1165,	0.5,
# new cell
	SPHERE,	42.2132,	43.0255,	35.0306,	0.5,
# new cell
	SPHERE,	42.5535,	43.7168,	35.2046,	0.5,
# new cell
	SPHERE,	42.8938,	44.4081,	35.3786,	0.5,
# new cell
	SPHERE,	43.2341,	45.0994,	35.5526,	0.5,
# new cell
	SPHERE,	43.5744,	45.7907,	35.7266,	0.5,
# new cell
	SPHERE,	42.1584,	43.859,	34.8147,	0.5,
# new cell
	SPHERE,	42.4987,	44.5503,	34.9887,	0.5,
# new cell
	SPHERE,	42.839,	45.2416,	35.1627,	0.5,
# new cell
	SPHERE,	43.1793,	45.9329,	35.3367,	0.5,
# new cell
	SPHERE,	42.1036,	44.6925,	34.5988,	0.5,
# new cell
	SPHERE,	42.4439,	45.3838,	34.7728,	0.5,
# new cell
	SPHERE,	42.7842,	46.0751,	34.9468,	0.5,
# new cell
	SPHERE,	42.0488,	45.526,	34.3829,	0.5,
# new cell
	SPHERE,	42.3891,	46.2173,	34.5569,	0.5,
# new cell
	SPHERE,	41.994,	46.3595,	34.167,	0.5,
# new cell
	SPHERE,	42.0436,	42.702,	35.2222,	0.5,
# new cell
	SPHERE,	42.3839,	43.3933,	35.3962,	0.5,
# new cell
	SPHERE,	42.7242,	44.0846,	35.5702,	0.5,
# new cell
	SPHERE,	43.0645,	44.7759,	35.7442,	0.5,
# new cell
	SPHERE,	43.4048,	45.4672,	35.9182,	0.5,
# new cell
	SPHERE,	41.9888,	43.5355,	35.0063,	0.5,
# new cell
	SPHERE,	42.3291,	44.2268,	35.1803,	0.5,
# new cell
	SPHERE,	42.6694,	44.9181,	35.3543,	0.5,
# new cell
	SPHERE,	43.0097,	45.6094,	35.5283,	0.5,
# new cell
	SPHERE,	41.934,	44.369,	34.7904,	0.5,
# new cell
	SPHERE,	42.2743,	45.0603,	34.9644,	0.5,
# new cell
	SPHERE,	42.6146,	45.7516,	35.1384,	0.5,
# new cell
	SPHERE,	41.8792,	45.2025,	34.5745,	0.5,
# new cell
	SPHERE,	42.2195,	45.8938,	34.7485,	0.5,
# new cell
	SPHERE,	41.8244,	46.036,	34.3586,	0.5,
# new cell
	SPHERE,	41.8192,	43.212,	35.1979,	0.5,
# new cell
	SPHERE,	42.1595,	43.9033,	35.3719,	0.5,
# new cell
	SPHERE,	42.4998,	44.5946,	35.5459,	0.5,
# new cell
	SPHERE,	42.8401,	45.2859,	35.7199,	0.5,
# new cell
	SPHERE,	41.7644,	44.0455,	34.982,	0.5,
# new cell
	SPHERE,	42.1047,	44.7368,	35.156,	0.5,
# new cell
	SPHERE,	42.445,	45.4281,	35.33,	0.5,
# new cell
	SPHERE,	41.7096,	44.879,	34.7661,	0.5,
# new cell
	SPHERE,	42.0499,	45.5703,	34.9401,	0.5,
# new cell
	SPHERE,	41.6548,	45.7125,	34.5502,	0.5,
# new cell
	SPHERE,	41.5948,	43.722,	35.1736,	0.5,
# new cell
	SPHERE,	41.9351,	44.4133,	35.3476,	0.5,
# new cell
	SPHERE,	42.2754,	45.1046,	35.5216,	0.5,
# new cell
	SPHERE,	41.54,	44.5555,	34.9577,	0.5,
# new cell
	SPHERE,	41.8803,	45.2468,	35.1317,	0.5,
# new cell
	SPHERE,	41.4852,	45.389,	34.7418,	0.5,
# new cell
	SPHERE,	41.3704,	44.232,	35.1493,	0.5,
# new cell
	SPHERE,	41.7107,	44.9233,	35.3233,	0.5,
# new cell
	SPHERE,	41.3156,	45.0655,	34.9334,	0.5,
# new cell
	SPHERE,	41.146,	44.742,	35.125,	0.5,
# new cell
	SPHERE,	49.14,	50.984,	36.162,	0.5,
# new cell
	SPHERE,	49.1864,	51.0498,	35.7188,	0.5,
# new cell
	SPHERE,	49.2328,	51.1156,	35.2756,	0.5,
# new cell
	SPHERE,	49.2792,	51.1814,	34.8324,	0.5,
# new cell
	SPHERE,	49.3256,	51.2472,	34.3892,	0.5,
# new cell
	SPHERE,	49.372,	51.313,	33.946,	0.5,
# new cell
	SPHERE,	49.4184,	51.3788,	33.5028,	0.5,
# new cell
	SPHERE,	49.4648,	51.4446,	33.0596,	0.5,
# new cell
	SPHERE,	49.5112,	51.5104,	32.6164,	0.5,
# new cell
	SPHERE,	49.5576,	51.5762,	32.1732,	0.5,
# new cell
	SPHERE,	49.604,	51.642,	31.73,	0.5,
# new cell
	SPHERE,	49.489,	50.6679,	35.6967,	0.5,
# new cell
	SPHERE,	49.5354,	50.7337,	35.2535,	0.5,
# new cell
	SPHERE,	49.5818,	50.7995,	34.8103,	0.5,
# new cell
	SPHERE,	49.6282,	50.8653,	34.3671,	0.5,
# new cell
	SPHERE,	49.6746,	50.9311,	33.9239,	0.5,
# new cell
	SPHERE,	49.721,	50.9969,	33.4807,	0.5,
# new cell
	SPHERE,	49.7674,	51.0627,	33.0375,	0.5,
# new cell
	SPHERE,	49.8138,	51.1285,	32.5943,	0.5,
# new cell
	SPHERE,	49.8602,	51.1943,	32.1511,	0.5,
# new cell
	SPHERE,	49.9066,	51.2601,	31.7079,	0.5,
# new cell
	SPHERE,	49.838,	50.3518,	35.2314,	0.5,
# new cell
	SPHERE,	49.8844,	50.4176,	34.7882,	0.5,
# new cell
	SPHERE,	49.9308,	50.4834,	34.345,	0.5,
# new cell
	SPHERE,	49.9772,	50.5492,	33.9018,	0.5,
# new cell
	SPHERE,	50.0236,	50.615,	33.4586,	0.5,
# new cell
	SPHERE,	50.07,	50.6808,	33.0154,	0.5,
# new cell
	SPHERE,	50.1164,	50.7466,	32.5722,	0.5,
# new cell
	SPHERE,	50.1628,	50.8124,	32.129,	0.5,
# new cell
	SPHERE,	50.2092,	50.8782,	31.6858,	0.5,
# new cell
	SPHERE,	50.187,	50.0357,	34.7661,	0.5,
# new cell
	SPHERE,	50.2334,	50.1015,	34.3229,	0.5,
# new cell
	SPHERE,	50.2798,	50.1673,	33.8797,	0.5,
# new cell
	SPHERE,	50.3262,	50.2331,	33.4365,	0.5,
# new cell
	SPHERE,	50.3726,	50.2989,	32.9933,	0.5,
# new cell
	SPHERE,	50.419,	50.3647,	32.5501,	0.5,
# new cell
	SPHERE,	50.4654,	50.4305,	32.1069,	0.5,
# new cell
	SPHERE,	50.5118,	50.4963,	31.6637,	0.5,
# new cell
	SPHERE,	50.536,	49.7196,	34.3008,	0.5,
# new cell
	SPHERE,	50.5824,	49.7854,	33.8576,	0.5,
# new cell
	SPHERE,	50.6288,	49.8512,	33.4144,	0.5,
# new cell
	SPHERE,	50.6752,	49.917,	32.9712,	0.5,
# new cell
	SPHERE,	50.7216,	49.9828,	32.528,	0.5,
# new cell
	SPHERE,	50.768,	50.0486,	32.0848,	0.5,
# new cell
	SPHERE,	50.8144,	50.1144,	31.6416,	0.5,
# new cell
	SPHERE,	50.885,	49.4035,	33.8355,	0.5,
# new cell
	SPHERE,	50.9314,	49.4693,	33.3923,	0.5,
# new cell
	SPHERE,	50.9778,	49.5351,	32.9491,	0.5,
# new cell
	SPHERE,	51.0242,	49.6009,	32.5059,	0.5,
# new cell
	SPHERE,	51.0706,	49.6667,	32.0627,	0.5,
# new cell
	SPHERE,	51.117,	49.7325,	31.6195,	0.5,
# new cell
	SPHERE,	51.234,	49.0874,	33.3702,	0.5,
# new cell
	SPHERE,	51.2804,	49.1532,	32.927,	0.5,
# new cell
	SPHERE,	51.3268,	49.219,	32.4838,	0.5,
# new cell
	SPHERE,	51.3732,	49.2848,	32.0406,	0.5,
# new cell
	SPHERE,	51.4196,	49.3506,	31.5974,	0.5,
# new cell
	SPHERE,	51.583,	48.7713,	32.9049,	0.5,
# new cell
	SPHERE,	51.6294,	48.8371,	32.4617,	0.5,
# new cell
	SPHERE,	51.6758,	48.9029,	32.0185,	0.5,
# new cell
	SPHERE,	51.7222,	48.9687,	31.5753,	0.5,
# new cell
	SPHERE,	51.932,	48.4552,	32.4396,	0.5,
# new cell
	SPHERE,	51.9784,	48.521,	31.9964,	0.5,
# new cell
	SPHERE,	52.0248,	48.5868,	31.5532,	0.5,
# new cell
	SPHERE,	52.281,	48.1391,	31.9743,	0.5,
# new cell
	SPHERE,	52.3274,	48.2049,	31.5311,	0.5,
# new cell
	SPHERE,	52.63,	47.823,	31.509,	0.5,
# new cell
	SPHERE,	48.8353,	50.7459,	36.1467,	0.5,
# new cell
	SPHERE,	48.8817,	50.8117,	35.7035,	0.5,
# new cell
	SPHERE,	48.9281,	50.8775,	35.2603,	0.5,
# new cell
	SPHERE,	48.9745,	50.9433,	34.8171,	0.5,
# new cell
	SPHERE,	49.0209,	51.0091,	34.3739,	0.5,
# new cell
	SPHERE,	49.0673,	51.0749,	33.9307,	0.5,
# new cell
	SPHERE,	49.1137,	51.1407,	33.4875,	0.5,
# new cell
	SPHERE,	49.1601,	51.2065,	33.0443,	0.5,
# new cell
	SPHERE,	49.2065,	51.2723,	32.6011,	0.5,
# new cell
	SPHERE,	49.2529,	51.3381,	32.1579,	0.5,
# new cell
	SPHERE,	49.1843,	50.4298,	35.6814,	0.5,
# new cell
	SPHERE,	49.2307,	50.4956,	35.2382,	0.5,
# new cell
	SPHERE,	49.2771,	50.5614,	34.795,	0.5,
# new cell
	SPHERE,	49.3235,	50.6272,	34.3518,	0.5,
# new cell
	SPHERE,	49.3699,	50.693,	33.9086,	0.5,
# new cell
	SPHERE,	49.4163,	50.7588,	33.4654,	0.5,
# new cell
	SPHERE,	49.4627,	50.8246,	33.0222,	0.5,
# new cell
	SPHERE,	49.5091,	50.8904,	32.579,	0.5,
# new cell
	SPHERE,	49.5555,	50.9562,	32.1358,	0.5,
# new cell
	SPHERE,	49.5333,	50.1137,	35.2161,	0.5,
# new cell
	SPHERE,	49.5797,	50.1795,	34.7729,	0.5,
# new cell
	SPHERE,	49.6261,	50.2453,	34.3297,	0.5,
# new cell
	SPHERE,	49.6725,	50.3111,	33.8865,	0.5,
# new cell
	SPHERE,	49.7189,	50.3769,	33.4433,	0.5,
# new cell
	SPHERE,	49.7653,	50.4427,	33.0001,	0.5,
# new cell
	SPHERE,	49.8117,	50.5085,	32.5569,	0.5,
# new cell
	SPHERE,	49.8581,	50.5743,	32.1137,	0.5,
# new cell
	SPHERE,	49.8823,	49.7976,	34.7508,	0.5,
# new cell
	SPHERE,	49.9287,	49.8634,	34.3076,	0.5,
# new cell
	SPHERE,	49.9751,	49.9292,	33.8644,	0.5,
# new cell
	SPHERE,	50.0215,	49.995,	33.4212,	0.5,
# new cell
	SPHERE,	50.0679,	50.0608,	32.978,	0.5,
# new cell
	SPHERE,	50.1143,	50.1266,	32.5348,	0.5,
# new cell
	SPHERE,	50.1607,	50.1924,	32.0916,	0.5,
# new cell
	SPHERE,	50.2313,	49.4815,	34.2855,	0.5,
# new cell
	SPHERE,	50.2777,	49.5473,	33.8423,	0.5,
# new cell
	SPHERE,	50.3241,	49.6131,	33.3991,	0.5,
# new cell
	SPHERE,	50.3705,	49.6789,	32.9559,	0.5,
# new cell
	SPHERE,	50.4169,	49.7447,	32.5127,	0.5,
# new cell
	SPHERE,	50.4633,	49.8105,	32.0695,	0.5,
# new cell
	SPHERE,	50.5803,	49.1654,	33.8202,	0.5,
# new cell
	SPHERE,	50.6267,	49.2312,	33.377,	0.5,
# new cell
	SPHERE,	50.6731,	49.297,	32.9338,	0.5,
# new cell
	SPHERE,	50.7195,	49.3628,	32.4906,	0.5,
# new cell
	SPHERE,	50.7659,	49.4286,	32.0474,	0.5,
# new cell
	SPHERE,	50.9293,	48.8493,	33.3549,	0.5,
# new cell
	SPHERE,	50.9757,	48.9151,	32.9117,	0.5,
# new cell
	SPHERE,	51.0221,	48.9809,	32.4685,	0.5,
# new cell
	SPHERE,	51.0685,	49.0467,	32.0253,	0.5,
# new cell
	SPHERE,	51.2783,	48.5332,	32.8896,	0.5,
# new cell
	SPHERE,	51.3247,	48.599,	32.4464,	0.5,
# new cell
	SPHERE,	51.3711,	48.6648,	32.0032,	0.5,
# new cell
	SPHERE,	51.6273,	48.2171,	32.4243,	0.5,
# new cell
	SPHERE,	51.6737,	48.2829,	31.9811,	0.5,
# new cell
	SPHERE,	51.9763,	47.901,	31.959,	0.5,
# new cell
	SPHERE,	48.5306,	50.5078,	36.1314,	0.5,
# new cell
	SPHERE,	48.577,	50.5736,	35.6882,	0.5,
# new cell
	SPHERE,	48.6234,	50.6394,	35.245,	0.5,
# new cell
	SPHERE,	48.6698,	50.7052,	34.8018,	0.5,
# new cell
	SPHERE,	48.7162,	50.771,	34.3586,	0.5,
# new cell
	SPHERE,	48.7626,	50.8368,	33.9154,	0.5,
# new cell
	SPHERE,	48.809,	50.9026,	33.4722,	0.5,
# new cell
	SPHERE,	48.8554,	50.9684,	33.029,	0.5,
# new cell
	SPHERE,	48.9018,	51.0342,	32.5858,	0.5,
# new cell
	SPHERE,	48.8796,	50.1917,	35.6661,	0.5,
# new cell
	SPHERE,	48.926,	50.2575,	35.2229,	0.5,
# new cell
	SPHERE,	48.9724,	50.3233,	34.7797,	0.5,
# new cell
	SPHERE,	49.0188,	50.3891,	34.3365,	0.5,
# new cell
	SPHERE,	49.0652,	50.4549,	33.8933,	0.5,
# new cell
	SPHERE,	49.1116,	50.5207,	33.4501,	0.5,
# new cell
	SPHERE,	49.158,	50.5865,	33.0069,	0.5,
# new cell
	SPHERE,	49.2044,	50.6523,	32.5637,	0.5,
# new cell
	SPHERE,	49.2286,	49.8756,	35.2008,	0.5,
# new cell
	SPHERE,	49.275,	49.9414,	34.7576,	0.5,
# new cell
	SPHERE,	49.3214,	50.0072,	34.3144,	0.5,
# new cell
	SPHERE,	49.3678,	50.073,	33.8712,	0.5,
# new cell
	SPHERE,	49.4142,	50.1388,	33.428,	0.5,
# new cell
	SPHERE,	49.4606,	50.2046,	32.9848,	0.5,
# new cell
	SPHERE,	49.507,	50.2704,	32.5416,	0.5,
# new cell
	SPHERE,	49.5776,	49.5595,	34.7355,	0.5,
# new cell
	SPHERE,	49.624,	49.6253,	34.2923,	0.5,
# new cell
	SPHERE,	49.6704,	49.6911,	33.8491,	0.5,
# new cell
	SPHERE,	49.7168,	49.7569,	33.4059,	0.5,
# new cell
	SPHERE,	49.7632,	49.8227,	32.9627,	0.5,
# new cell
	SPHERE,	49.8096,	49.8885,	32.5195,	0.5,
# new cell
	SPHERE,	49.9266,	49.2434,	34.2702,	0.5,
# new cell
	SPHERE,	49.973,	49.3092,	33.827,	0.5,
# new cell
	SPHERE,	50.0194,	49.375,	33.3838,	0.5,
# new cell
	SPHERE,	50.0658,	49.4408,	32.9406,	0.5,
# new cell
	SPHERE,	50.1122,	49.5066,	32.4974,	0.5,
# new cell
	SPHERE,	50.2756,	48.9273,	33.8049,	0.5,
# new cell
	SPHERE,	50.322,	48.9931,	33.3617,	0.5,
# new cell
	SPHERE,	50.3684,	49.0589,	32.9185,	0.5,
# new cell
	SPHERE,	50.4148,	49.1247,	32.4753,	0.5,
# new cell
	SPHERE,	50.6246,	48.6112,	33.3396,	0.5,
# new cell
	SPHERE,	50.671,	48.677,	32.8964,	0.5,
# new cell
	SPHERE,	50.7174,	48.7428,	32.4532,	0.5,
# new cell
	SPHERE,	50.9736,	48.2951,	32.8743,	0.5,
# new cell
	SPHERE,	51.02,	48.3609,	32.4311,	0.5,
# new cell
	SPHERE,	51.3226,	47.979,	32.409,	0.5,
# new cell
	SPHERE,	48.2259,	50.2697,	36.1161,	0.5,
# new cell
	SPHERE,	48.2723,	50.3355,	35.6729,	0.5,
# new cell
	SPHERE,	48.3187,	50.4013,	35.2297,	0.5,
# new cell
	SPHERE,	48.3651,	50.4671,	34.7865,	0.5,
# new cell
	SPHERE,	48.4115,	50.5329,	34.3433,	0.5,
# new cell
	SPHERE,	48.4579,	50.5987,	33.9001,	0.5,
# new cell
	SPHERE,	48.5043,	50.6645,	33.4569,	0.5,
# new cell
	SPHERE,	48.5507,	50.7303,	33.0137,	0.5,
# new cell
	SPHERE,	48.5749,	49.9536,	35.6508,	0.5,
# new cell
	SPHERE,	48.6213,	50.0194,	35.2076,	0.5,
# new cell
	SPHERE,	48.6677,	50.0852,	34.7644,	0.5,
# new cell
	SPHERE,	48.7141,	50.151,	34.3212,	0.5,
# new cell
	SPHERE,	48.7605,	50.2168,	33.878,	0.5,
# new cell
	SPHERE,	48.8069,	50.2826,	33.4348,	0.5,
# new cell
	SPHERE,	48.8533,	50.3484,	32.9916,	0.5,
# new cell
	SPHERE,	48.9239,	49.6375,	35.1855,	0.5,
# new cell
	SPHERE,	48.9703,	49.7033,	34.7423,	0.5,
# new cell
	SPHERE,	49.0167,	49.7691,	34.2991,	0.5,
# new cell
	SPHERE,	49.0631,	49.8349,	33.8559,	0.5,
# new cell
	SPHERE,	49.1095,	49.9007,	33.4127,	0.5,
# new cell
	SPHERE,	49.1559,	49.9665,	32.9695,	0.5,
# new cell
	SPHERE,	49.2729,	49.3214,	34.7202,	0.5,
# new cell
	SPHERE,	49.3193,	49.3872,	34.277,	0.5,
# new cell
	SPHERE,	49.3657,	49.453,	33.8338,	0.5,
# new cell
	SPHERE,	49.4121,	49.5188,	33.3906,	0.5,
# new cell
	SPHERE,	49.4585,	49.5846,	32.9474,	0.5,
# new cell
	SPHERE,	49.6219,	49.0053,	34.2549,	0.5,
# new cell
	SPHERE,	49.6683,	49.0711,	33.8117,	0.5,
# new cell
	SPHERE,	49.7147,	49.1369,	33.3685,	0.5,
# new cell
	SPHERE,	49.7611,	49.2027,	32.9253,	0.5,
# new cell
	SPHERE,	49.9709,	48.6892,	33.7896,	0.5,
# new cell
	SPHERE,	50.0173,	48.755,	33.3464,	0.5,
# new cell
	SPHERE,	50.0637,	48.8208,	32.9032,	0.5,
# new cell
	SPHERE,	50.3199,	48.3731,	33.3243,	0.5,
# new cell
	SPHERE,	50.3663,	48.4389,	32.8811,	0.5,
# new cell
	SPHERE,	50.6689,	48.057,	32.859,	0.5,
# new cell
	SPHERE,	47.9212,	50.0316,	36.1008,	0.5,
# new cell
	SPHERE,	47.9676,	50.0974,	35.6576,	0.5,
# new cell
	SPHERE,	48.014,	50.1632,	35.2144,	0.5,
# new cell
	SPHERE,	48.0604,	50.229,	34.7712,	0.5,
# new cell
	SPHERE,	48.1068,	50.2948,	34.328,	0.5,
# new cell
	SPHERE,	48.1532,	50.3606,	33.8848,	0.5,
# new cell
	SPHERE,	48.1996,	50.4264,	33.4416,	0.5,
# new cell
	SPHERE,	48.2702,	49.7155,	35.6355,	0.5,
# new cell
	SPHERE,	48.3166,	49.7813,	35.1923,	0.5,
# new cell
	SPHERE,	48.363,	49.8471,	34.7491,	0.5,
# new cell
	SPHERE,	48.4094,	49.9129,	34.3059,	0.5,
# new cell
	SPHERE,	48.4558,	49.9787,	33.8627,	0.5,
# new cell
	SPHERE,	48.5022,	50.0445,	33.4195,	0.5,
# new cell
	SPHERE,	48.6192,	49.3994,	35.1702,	0.5,
# new cell
	SPHERE,	48.6656,	49.4652,	34.727,	0.5,
# new cell
	SPHERE,	48.712,	49.531,	34.2838,	0.5,
# new cell
	SPHERE,	48.7584,	49.5968,	33.8406,	0.5,
# new cell
	SPHERE,	48.8048,	49.6626,	33.3974,	0.5,
# new cell
	SPHERE,	48.9682,	49.0833,	34.7049,	0.5,
# new cell
	SPHERE,	49.0146,	49.1491,	34.2617,	0.5,
# new cell
	SPHERE,	49.061,	49.2149,	33.8185,	0.5,
# new cell
	SPHERE,	49.1074,	49.2807,	33.3753,	0.5,
# new cell
	SPHERE,	49.3172,	48.7672,	34.2396,	0.5,
# new cell
	SPHERE,	49.3636,	48.833,	33.7964,	0.5,
# new cell
	SPHERE,	49.41,	48.8988,	33.3532,	0.5,
# new cell
	SPHERE,	49.6662,	48.4511,	33.7743,	0.5,
# new cell
	SPHERE,	49.7126,	48.5169,	33.3311,	0.5,
# new cell
	SPHERE,	50.0152,	48.135,	33.309,	0.5,
# new cell
	SPHERE,	47.6165,	49.7935,	36.0855,	0.5,
# new cell
	SPHERE,	47.6629,	49.8593,	35.6423,	0.5,
# new cell
	SPHERE,	47.7093,	49.9251,	35.1991,	0.5,
# new cell
	SPHERE,	47.7557,	49.9909,	34.7559,	0.5,
# new cell
	SPHERE,	47.8021,	50.0567,	34.3127,	0.5,
# new cell
	SPHERE,	47.8485,	50.1225,	33.8695,	0.5,
# new cell
	SPHERE,	47.9655,	49.4774,	35.6202,	0.5,
# new cell
	SPHERE,	48.0119,	49.5432,	35.177,	0.5,
# new cell
	SPHERE,	48.0583,	49.609,	34.7338,	0.5,
# new cell
	SPHERE,	48.1047,	49.6748,	34.2906,	0.5,
# new cell
	SPHERE,	48.1511,	49.7406,	33.8474,	0.5,
# new cell
	SPHERE,	48.3145,	49.1613,	35.1549,	0.5,
# new cell
	SPHERE,	48.3609,	49.2271,	34.7117,	0.5,
# new cell
	SPHERE,	48.4073,	49.2929,	34.2685,	0.5,
# new cell
	SPHERE,	48.4537,	49.3587,	33.8253,	0.5,
# new cell
	SPHERE,	48.6635,	48.8452,	34.6896,	0.5,
# new cell
	SPHERE,	48.7099,	48.911,	34.2464,	0.5,
# new cell
	SPHERE,	48.7563,	48.9768,	33.8032,	0.5,
# new cell
	SPHERE,	49.0125,	48.5291,	34.2243,	0.5,
# new cell
	SPHERE,	49.0589,	48.5949,	33.7811,	0.5,
# new cell
	SPHERE,	49.3615,	48.213,	33.759,	0.5,
# new cell
	SPHERE,	47.3118,	49.5554,	36.0702,	0.5,
# new cell
	SPHERE,	47.3582,	49.6212,	35.627,	0.5,
# new cell
	SPHERE,	47.4046,	49.687,	35.1838,	0.5,
# new cell
	SPHERE,	47.451,	49.7528,	34.7406,	0.5,
# new cell
	SPHERE,	47.4974,	49.8186,	34.2974,	0.5,
# new cell
	SPHERE,	47.6608,	49.2393,	35.6049,	0.5,
# new cell
	SPHERE,	47.7072,	49.3051,	35.1617,	0.5,
# new cell
	SPHERE,	47.7536,	49.3709,	34.7185,	0.5,
# new cell
	SPHERE,	47.8,	49.4367,	34.2753,	0.5,
# new cell
	SPHERE,	48.0098,	48.9232,	35.1396,	0.5,
# new cell
	SPHERE,	48.0562,	48.989,	34.6964,	0.5,
# new cell
	SPHERE,	48.1026,	49.0548,	34.2532,	0.5,
# new cell
	SPHERE,	48.3588,	48.6071,	34.6743,	0.5,
# new cell
	SPHERE,	48.4052,	48.6729,	34.2311,	0.5,
# new cell
	SPHERE,	48.7078,	48.291,	34.209,	0.5,
# new cell
	SPHERE,	47.0071,	49.3173,	36.0549,	0.5,
# new cell
	SPHERE,	47.0535,	49.3831,	35.6117,	0.5,
# new cell
	SPHERE,	47.0999,	49.4489,	35.1685,	0.5,
# new cell
	SPHERE,	47.1463,	49.5147,	34.7253,	0.5,
# new cell
	SPHERE,	47.3561,	49.0012,	35.5896,	0.5,
# new cell
	SPHERE,	47.4025,	49.067,	35.1464,	0.5,
# new cell
	SPHERE,	47.4489,	49.1328,	34.7032,	0.5,
# new cell
	SPHERE,	47.7051,	48.6851,	35.1243,	0.5,
# new cell
	SPHERE,	47.7515,	48.7509,	34.6811,	0.5,
# new cell
	SPHERE,	48.0541,	48.369,	34.659,	0.5,
# new cell
	SPHERE,	46.7024,	49.0792,	36.0396,	0.5,
# new cell
	SPHERE,	46.7488,	49.145,	35.5964,	0.5,
# new cell
	SPHERE,	46.7952,	49.2108,	35.1532,	0.5,
# new cell
	SPHERE,	47.0514,	48.7631,	35.5743,	0.5,
# new cell
	SPHERE,	47.0978,	48.8289,	35.1311,	0.5,
# new cell
	SPHERE,	47.4004,	48.447,	35.109,	0.5,
# new cell
	SPHERE,	46.3977,	48.8411,	36.0243,	0.5,
# new cell
	SPHERE,	46.4441,	48.9069,	35.5811,	0.5,
# new cell
	SPHERE,	46.7467,	48.525,	35.559,	0.5,
# new cell
	SPHERE,	46.093,	48.603,	36.009,	0.5,
# new cell
	SPHERE,	46.084,	48.591,	36.001,	0.5,
# new cell
	SPHERE,	46.222,	48.1932,	35.0265,	0.5,
# new cell
	SPHERE,	46.36,	47.7954,	34.052,	0.5,
# new cell
	SPHERE,	46.498,	47.3976,	33.0775,	0.5,
# new cell
	SPHERE,	46.636,	46.9998,	32.103,	0.5,
# new cell
	SPHERE,	46.774,	46.602,	31.1285,	0.5,
# new cell
	SPHERE,	46.912,	46.2042,	30.154,	0.5,
# new cell
	SPHERE,	47.05,	45.8064,	29.1795,	0.5,
# new cell
	SPHERE,	47.188,	45.4086,	28.205,	0.5,
# new cell
	SPHERE,	47.326,	45.0108,	27.2305,	0.5,
# new cell
	SPHERE,	47.464,	44.613,	26.256,	0.5,
# new cell
	SPHERE,	46.7386,	48.5142,	35.5518,	0.5,
# new cell
	SPHERE,	46.8766,	48.1164,	34.5773,	0.5,
# new cell
	SPHERE,	47.0146,	47.7186,	33.6028,	0.5,
# new cell
	SPHERE,	47.1526,	47.3208,	32.6283,	0.5,
# new cell
	SPHERE,	47.2906,	46.923,	31.6538,	0.5,
# new cell
	SPHERE,	47.4286,	46.5252,	30.6793,	0.5,
# new cell
	SPHERE,	47.5666,	46.1274,	29.7048,	0.5,
# new cell
	SPHERE,	47.7046,	45.7296,	28.7303,	0.5,
# new cell
	SPHERE,	47.8426,	45.3318,	27.7558,	0.5,
# new cell
	SPHERE,	47.9806,	44.934,	26.7813,	0.5,
# new cell
	SPHERE,	47.3932,	48.4374,	35.1026,	0.5,
# new cell
	SPHERE,	47.5312,	48.0396,	34.1281,	0.5,
# new cell
	SPHERE,	47.6692,	47.6418,	33.1536,	0.5,
# new cell
	SPHERE,	47.8072,	47.244,	32.1791,	0.5,
# new cell
	SPHERE,	47.9452,	46.8462,	31.2046,	0.5,
# new cell
	SPHERE,	48.0832,	46.4484,	30.2301,	0.5,
# new cell
	SPHERE,	48.2212,	46.0506,	29.2556,	0.5,
# new cell
	SPHERE,	48.3592,	45.6528,	28.2811,	0.5,
# new cell
	SPHERE,	48.4972,	45.255,	27.3066,	0.5,
# new cell
	SPHERE,	48.0478,	48.3606,	34.6534,	0.5,
# new cell
	SPHERE,	48.1858,	47.9628,	33.6789,	0.5,
# new cell
	SPHERE,	48.3238,	47.565,	32.7044,	0.5,
# new cell
	SPHERE,	48.4618,	47.1672,	31.7299,	0.5,
# new cell
	SPHERE,	48.5998,	46.7694,	30.7554,	0.5,
# new cell
	SPHERE,	48.7378,	46.3716,	29.7809,	0.5,
# new cell
	SPHERE,	48.8758,	45.9738,	28.8064,	0.5,
# new cell
	SPHERE,	49.0138,	45.576,	27.8319,	0.5,
# new cell
	SPHERE,	48.7024,	48.2838,	34.2042,	0.5,
# new cell
	SPHERE,	48.8404,	47.886,	33.2297,	0.5,
# new cell
	SPHERE,	48.9784,	47.4882,	32.2552,	0.5,
# new cell
	SPHERE,	49.1164,	47.0904,	31.2807,	0.5,
# new cell
	SPHERE,	49.2544,	46.6926,	30.3062,	0.5,
# new cell
	SPHERE,	49.3924,	46.2948,	29.3317,	0.5,
# new cell
	SPHERE,	49.5304,	45.897,	28.3572,	0.5,
# new cell
	SPHERE,	49.357,	48.207,	33.755,	0.5,
# new cell
	SPHERE,	49.495,	47.8092,	32.7805,	0.5,
# new cell
	SPHERE,	49.633,	47.4114,	31.806,	0.5,
# new cell
	SPHERE,	49.771,	47.0136,	30.8315,	0.5,
# new cell
	SPHERE,	49.909,	46.6158,	29.857,	0.5,
# new cell
	SPHERE,	50.047,	46.218,	28.8825,	0.5,
# new cell
	SPHERE,	50.0116,	48.1302,	33.3058,	0.5,
# new cell
	SPHERE,	50.1496,	47.7324,	32.3313,	0.5,
# new cell
	SPHERE,	50.2876,	47.3346,	31.3568,	0.5,
# new cell
	SPHERE,	50.4256,	46.9368,	30.3823,	0.5,
# new cell
	SPHERE,	50.5636,	46.539,	29.4078,	0.5,
# new cell
	SPHERE,	50.6662,	48.0534,	32.8566,	0.5,
# new cell
	SPHERE,	50.8042,	47.6556,	31.8821,	0.5,
# new cell
	SPHERE,	50.9422,	47.2578,	30.9076,	0.5,
# new cell
	SPHERE,	51.0802,	46.86,	29.9331,	0.5,
# new cell
	SPHERE,	51.3208,	47.9766,	32.4074,	0.5,
# new cell
	SPHERE,	51.4588,	47.5788,	31.4329,	0.5,
# new cell
	SPHERE,	51.5968,	47.181,	30.4584,	0.5,
# new cell
	SPHERE,	51.9754,	47.8998,	31.9582,	0.5,
# new cell
	SPHERE,	52.1134,	47.502,	30.9837,	0.5,
# new cell
	SPHERE,	52.63,	47.823,	31.509,	0.5,
# new cell
	SPHERE,	46.1549,	48.3874,	36.1117,	0.5,
# new cell
	SPHERE,	46.2929,	47.9896,	35.1372,	0.5,
# new cell
	SPHERE,	46.4309,	47.5918,	34.1627,	0.5,
# new cell
	SPHERE,	46.5689,	47.194,	33.1882,	0.5,
# new cell
	SPHERE,	46.7069,	46.7962,	32.2137,	0.5,
# new cell
	SPHERE,	46.8449,	46.3984,	31.2392,	0.5,
# new cell
	SPHERE,	46.9829,	46.0006,	30.2647,	0.5,
# new cell
	SPHERE,	47.1209,	45.6028,	29.2902,	0.5,
# new cell
	SPHERE,	47.2589,	45.205,	28.3157,	0.5,
# new cell
	SPHERE,	47.3969,	44.8072,	27.3412,	0.5,
# new cell
	SPHERE,	46.8095,	48.3106,	35.6625,	0.5,
# new cell
	SPHERE,	46.9475,	47.9128,	34.688,	0.5,
# new cell
	SPHERE,	47.0855,	47.515,	33.7135,	0.5,
# new cell
	SPHERE,	47.2235,	47.1172,	32.739,	0.5,
# new cell
	SPHERE,	47.3615,	46.7194,	31.7645,	0.5,
# new cell
	SPHERE,	47.4995,	46.3216,	30.79,	0.5,
# new cell
	SPHERE,	47.6375,	45.9238,	29.8155,	0.5,
# new cell
	SPHERE,	47.7755,	45.526,	28.841,	0.5,
# new cell
	SPHERE,	47.9135,	45.1282,	27.8665,	0.5,
# new cell
	SPHERE,	47.4641,	48.2338,	35.2133,	0.5,
# new cell
	SPHERE,	47.6021,	47.836,	34.2388,	0.5,
# new cell
	SPHERE,	47.7401,	47.4382,	33.2643,	0.5,
# new cell
	SPHERE,	47.8781,	47.0404,	32.2898,	0.5,
# new cell
	SPHERE,	48.0161,	46.6426,	31.3153,	0.5,
# new cell
	SPHERE,	48.1541,	46.2448,	30.3408,	0.5,
# new cell
	SPHERE,	48.2921,	45.847,	29.3663,	0.5,
# new cell
	SPHERE,	48.4301,	45.4492,	28.3918,	0.5,
# new cell
	SPHERE,	48.1187,	48.157,	34.7641,	0.5,
# new cell
	SPHERE,	48.2567,	47.7592,	33.7896,	0.5,
# new cell
	SPHERE,	48.3947,	47.3614,	32.8151,	0.5,
# new cell
	SPHERE,	48.5327,	46.9636,	31.8406,	0.5,
# new cell
	SPHERE,	48.6707,	46.5658,	30.8661,	0.5,
# new cell
	SPHERE,	48.8087,	46.168,	29.8916,	0.5,
# new cell
	SPHERE,	48.9467,	45.7702,	28.9171,	0.5,
# new cell
	SPHERE,	48.7733,	48.0802,	34.3149,	0.5,
# new cell
	SPHERE,	48.9113,	47.6824,	33.3404,	0.5,
# new cell
	SPHERE,	49.0493,	47.2846,	32.3659,	0.5,
# new cell
	SPHERE,	49.1873,	46.8868,	31.3914,	0.5,
# new cell
	SPHERE,	49.3253,	46.489,	30.4169,	0.5,
# new cell
	SPHERE,	49.4633,	46.0912,	29.4424,	0.5,
# new cell
	SPHERE,	49.4279,	48.0034,	33.8657,	0.5,
# new cell
	SPHERE,	49.5659,	47.6056,	32.8912,	0.5,
# new cell
	SPHERE,	49.7039,	47.2078,	31.9167,	0.5,
# new cell
	SPHERE,	49.8419,	46.81,	30.9422,	0.5,
# new cell
	SPHERE,	49.9799,	46.4122,	29.9677,	0.5,
# new cell
	SPHERE,	50.0825,	47.9266,	33.4165,	0.5,
# new cell
	SPHERE,	50.2205,	47.5288,	32.442,	0.5,
# new cell
	SPHERE,	50.3585,	47.131,	31.4675,	0.5,
# new cell
	SPHERE,	50.4965,	46.7332,	30.493,	0.5,
# new cell
	SPHERE,	50.7371,	47.8498,	32.9673,	0.5,
# new cell
	SPHERE,	50.8751,	47.452,	31.9928,	0.5,
# new cell
	SPHERE,	51.0131,	47.0542,	31.0183,	0.5,
# new cell
	SPHERE,	51.3917,	47.773,	32.5181,	0.5,
# new cell
	SPHERE,	51.5297,	47.3752,	31.5436,	0.5,
# new cell
	SPHERE,	52.0463,	47.6962,	32.0689,	0.5,
# new cell
	SPHERE,	46.2258,	48.1838,	36.2224,	0.5,
# new cell
	SPHERE,	46.3638,	47.786,	35.2479,	0.5,
# new cell
	SPHERE,	46.5018,	47.3882,	34.2734,	0.5,
# new cell
	SPHERE,	46.6398,	46.9904,	33.2989,	0.5,
# new cell
	SPHERE,	46.7778,	46.5926,	32.3244,	0.5,
# new cell
	SPHERE,	46.9158,	46.1948,	31.3499,	0.5,
# new cell
	SPHERE,	47.0538,	45.797,	30.3754,	0.5,
# new cell
	SPHERE,	47.1918,	45.3992,	29.4009,	0.5,
# new cell
	SPHERE,	47.3298,	45.0014,	28.4264,	0.5,
# new cell
	SPHERE,	46.8804,	48.107,	35.7732,	0.5,
# new cell
	SPHERE,	47.0184,	47.7092,	34.7987,	0.5,
# new cell
	SPHERE,	47.1564,	47.3114,	33.8242,	0.5,
# new cell
	SPHERE,	47.2944,	46.9136,	32.8497,	0.5,
# new cell
	SPHERE,	47.4324,	46.5158,	31.8752,	0.5,
# new cell
	SPHERE,	47.5704,	46.118,	30.9007,	0.5,
# new cell
	SPHERE,	47.7084,	45.7202,	29.9262,	0.5,
# new cell
	SPHERE,	47.8464,	45.3224,	28.9517,	0.5,
# new cell
	SPHERE,	47.535,	48.0302,	35.324,	0.5,
# new cell
	SPHERE,	47.673,	47.6324,	34.3495,	0.5,
# new cell
	SPHERE,	47.811,	47.2346,	33.375,	0.5,
# new cell
	SPHERE,	47.949,	46.8368,	32.4005,	0.5,
# new cell
	SPHERE,	48.087,	46.439,	31.426,	0.5,
# new cell
	SPHERE,	48.225,	46.0412,	30.4515,	0.5,
# new cell
	SPHERE,	48.363,	45.6434,	29.477,	0.5,
# new cell
	SPHERE,	48.1896,	47.9534,	34.8748,	0.5,
# new cell
	SPHERE,	48.3276,	47.5556,	33.9003,	0.5,
# new cell
	SPHERE,	48.4656,	47.1578,	32.9258,	0.5,
# new cell
	SPHERE,	48.6036,	46.76,	31.9513,	0.5,
# new cell
	SPHERE,	48.7416,	46.3622,	30.9768,	0.5,
# new cell
	SPHERE,	48.8796,	45.9644,	30.0023,	0.5,
# new cell
	SPHERE,	48.8442,	47.8766,	34.4256,	0.5,
# new cell
	SPHERE,	48.9822,	47.4788,	33.4511,	0.5,
# new cell
	SPHERE,	49.1202,	47.081,	32.4766,	0.5,
# new cell
	SPHERE,	49.2582,	46.6832,	31.5021,	0.5,
# new cell
	SPHERE,	49.3962,	46.2854,	30.5276,	0.5,
# new cell
	SPHERE,	49.4988,	47.7998,	33.9764,	0.5,
# new cell
	SPHERE,	49.6368,	47.402,	33.0019,	0.5,
# new cell
	SPHERE,	49.7748,	47.0042,	32.0274,	0.5,
# new cell
	SPHERE,	49.9128,	46.6064,	31.0529,	0.5,
# new cell
	SPHERE,	50.1534,	47.723,	33.5272,	0.5,
# new cell
	SPHERE,	50.2914,	47.3252,	32.5527,	0.5,
# new cell
	SPHERE,	50.4294,	46.9274,	31.5782,	0.5,
# new cell
	SPHERE,	50.808,	47.6462,	33.078,	0.5,
# new cell
	SPHERE,	50.946,	47.2484,	32.1035,	0.5,
# new cell
	SPHERE,	51.4626,	47.5694,	32.6288,	0.5,
# new cell
	SPHERE,	46.2967,	47.9802,	36.3331,	0.5,
# new cell
	SPHERE,	46.4347,	47.5824,	35.3586,	0.5,
# new cell
	SPHERE,	46.5727,	47.1846,	34.3841,	0.5,
# new cell
	SPHERE,	46.7107,	46.7868,	33.4096,	0.5,
# new cell
	SPHERE,	46.8487,	46.389,	32.4351,	0.5,
# new cell
	SPHERE,	46.9867,	45.9912,	31.4606,	0.5,
# new cell
	SPHERE,	47.1247,	45.5934,	30.4861,	0.5,
# new cell
	SPHERE,	47.2627,	45.1956,	29.5116,	0.5,
# new cell
	SPHERE,	46.9513,	47.9034,	35.8839,	0.5,
# new cell
	SPHERE,	47.0893,	47.5056,	34.9094,	0.5,
# new cell
	SPHERE,	47.2273,	47.1078,	33.9349,	0.5,
# new cell
	SPHERE,	47.3653,	46.71,	32.9604,	0.5,
# new cell
	SPHERE,	47.5033,	46.3122,	31.9859,	0.5,
# new cell
	SPHERE,	47.6413,	45.9144,	31.0114,	0.5,
# new cell
	SPHERE,	47.7793,	45.5166,	30.0369,	0.5,
# new cell
	SPHERE,	47.6059,	47.8266,	35.4347,	0.5,
# new cell
	SPHERE,	47.7439,	47.4288,	34.4602,	0.5,
# new cell
	SPHERE,	47.8819,	47.031,	33.4857,	0.5,
# new cell
	SPHERE,	48.0199,	46.6332,	32.5112,	0.5,
# new cell
	SPHERE,	48.1579,	46.2354,	31.5367,	0.5,
# new cell
	SPHERE,	48.2959,	45.8376,	30.5622,	0.5,
# new cell
	SPHERE,	48.2605,	47.7498,	34.9855,	0.5,
# new cell
	SPHERE,	48.3985,	47.352,	34.011,	0.5,
# new cell
	SPHERE,	48.5365,	46.9542,	33.0365,	0.5,
# new cell
	SPHERE,	48.6745,	46.5564,	32.062,	0.5,
# new cell
	SPHERE,	48.8125,	46.1586,	31.0875,	0.5,
# new cell
	SPHERE,	48.9151,	47.673,	34.5363,	0.5,
# new cell
	SPHERE,	49.0531,	47.2752,	33.5618,	0.5,
# new cell
	SPHERE,	49.1911,	46.8774,	32.5873,	0.5,
# new cell
	SPHERE,	49.3291,	46.4796,	31.6128,	0.5,
# new cell
	SPHERE,	49.5697,	47.5962,	34.0871,	0.5,
# new cell
	SPHERE,	49.7077,	47.1984,	33.1126,	0.5,
# new cell
	SPHERE,	49.8457,	46.8006,	32.1381,	0.5,
# new cell
	SPHERE,	50.2243,	47.5194,	33.6379,	0.5,
# new cell
	SPHERE,	50.3623,	47.1216,	32.6634,	0.5,
# new cell
	SPHERE,	50.8789,	47.4426,	33.1887,	0.5,
# new cell
	SPHERE,	46.3676,	47.7766,	36.4438,	0.5,
# new cell
	SPHERE,	46.5056,	47.3788,	35.4693,	0.5,
# new cell
	SPHERE,	46.6436,	46.981,	34.4948,	0.5,
# new cell
	SPHERE,	46.7816,	46.5832,	33.5203,	0.5,
# new cell
	SPHERE,	46.9196,	46.1854,	32.5458,	0.5,
# new cell
	SPHERE,	47.0576,	45.7876,	31.5713,	0.5,
# new cell
	SPHERE,	47.1956,	45.3898,	30.5968,	0.5,
# new cell
	SPHERE,	47.0222,	47.6998,	35.9946,	0.5,
# new cell
	SPHERE,	47.1602,	47.302,	35.0201,	0.5,
# new cell
	SPHERE,	47.2982,	46.9042,	34.0456,	0.5,
# new cell
	SPHERE,	47.4362,	46.5064,	33.0711,	0.5,
# new cell
	SPHERE,	47.5742,	46.1086,	32.0966,	0.5,
# new cell
	SPHERE,	47.7122,	45.7108,	31.1221,	0.5,
# new cell
	SPHERE,	47.6768,	47.623,	35.5454,	0.5,
# new cell
	SPHERE,	47.8148,	47.2252,	34.5709,	0.5,
# new cell
	SPHERE,	47.9528,	46.8274,	33.5964,	0.5,
# new cell
	SPHERE,	48.0908,	46.4296,	32.6219,	0.5,
# new cell
	SPHERE,	48.2288,	46.0318,	31.6474,	0.5,
# new cell
	SPHERE,	48.3314,	47.5462,	35.0962,	0.5,
# new cell
	SPHERE,	48.4694,	47.1484,	34.1217,	0.5,
# new cell
	SPHERE,	48.6074,	46.7506,	33.1472,	0.5,
# new cell
	SPHERE,	48.7454,	46.3528,	32.1727,	0.5,
# new cell
	SPHERE,	48.986,	47.4694,	34.647,	0.5,
# new cell
	SPHERE,	49.124,	47.0716,	33.6725,	0.5,
# new cell
	SPHERE,	49.262,	46.6738,	32.698,	0.5,
# new cell
	SPHERE,	49.6406,	47.3926,	34.1978,	0.5,
# new cell
	SPHERE,	49.7786,	46.9948,	33.2233,	0.5,
# new cell
	SPHERE,	50.2952,	47.3158,	33.7486,	0.5,
# new cell
	SPHERE,	46.4385,	47.573,	36.5545,	0.5,
# new cell
	SPHERE,	46.5765,	47.1752,	35.58,	0.5,
# new cell
	SPHERE,	46.7145,	46.7774,	34.6055,	0.5,
# new cell
	SPHERE,	46.8525,	46.3796,	33.631,	0.5,
# new cell
	SPHERE,	46.9905,	45.9818,	32.6565,	0.5,
# new cell
	SPHERE,	47.1285,	45.584,	31.682,	0.5,
# new cell
	SPHERE,	47.0931,	47.4962,	36.1053,	0.5,
# new cell
	SPHERE,	47.2311,	47.0984,	35.1308,	0.5,
# new cell
	SPHERE,	47.3691,	46.7006,	34.1563,	0.5,
# new cell
	SPHERE,	47.5071,	46.3028,	33.1818,	0.5,
# new cell
	SPHERE,	47.6451,	45.905,	32.2073,	0.5,
# new cell
	SPHERE,	47.7477,	47.4194,	35.6561,	0.5,
# new cell
	SPHERE,	47.8857,	47.0216,	34.6816,	0.5,
# new cell
	SPHERE,	48.0237,	46.6238,	33.7071,	0.5,
# new cell
	SPHERE,	48.1617,	46.226,	32.7326,	0.5,
# new cell
	SPHERE,	48.4023,	47.3426,	35.2069,	0.5,
# new cell
	SPHERE,	48.5403,	46.9448,	34.2324,	0.5,
# new cell
	SPHERE,	48.6783,	46.547,	33.2579,	0.5,
# new cell
	SPHERE,	49.0569,	47.2658,	34.7577,	0.5,
# new cell
	SPHERE,	49.1949,	46.868,	33.7832,	0.5,
# new cell
	SPHERE,	49.7115,	47.189,	34.3085,	0.5,
# new cell
	SPHERE,	46.5094,	47.3694,	36.6652,	0.5,
# new cell
	SPHERE,	46.6474,	46.9716,	35.6907,	0.5,
# new cell
	SPHERE,	46.7854,	46.5738,	34.7162,	0.5,
# new cell
	SPHERE,	46.9234,	46.176,	33.7417,	0.5,
# new cell
	SPHERE,	47.0614,	45.7782,	32.7672,	0.5,
# new cell
	SPHERE,	47.164,	47.2926,	36.216,	0.5,
# new cell
	SPHERE,	47.302,	46.8948,	35.2415,	0.5,
# new cell
	SPHERE,	47.44,	46.497,	34.267,	0.5,
# new cell
	SPHERE,	47.578,	46.0992,	33.2925,	0.5,
# new cell
	SPHERE,	47.8186,	47.2158,	35.7668,	0.5,
# new cell
	SPHERE,	47.9566,	46.818,	34.7923,	0.5,
# new cell
	SPHERE,	48.0946,	46.4202,	33.8178,	0.5,
# new cell
	SPHERE,	48.4732,	47.139,	35.3176,	0.5,
# new cell
	SPHERE,	48.6112,	46.7412,	34.3431,	0.5,
# new cell
	SPHERE,	49.1278,	47.0622,	34.8684,	0.5,
# new cell
	SPHERE,	46.5803,	47.1658,	36.7759,	0.5,
# new cell
	SPHERE,	46.7183,	46.768,	35.8014,	0.5,
# new cell
	SPHERE,	46.8563,	46.3702,	34.8269,	0.5,
# new cell
	SPHERE,	46.9943,	45.9724,	33.8524,	0.5,
# new cell
	SPHERE,	47.2349,	47.089,	36.3267,	0.5,
# new cell
	SPHERE,	47.3729,	46.6912,	35.3522,	0.5,
# new cell
	SPHERE,	47.5109,	46.2934,	34.3777,	0.5,
# new cell
	SPHERE,	47.8895,	47.0122,	35.8775,	0.5,
# new cell
	SPHERE,	48.0275,	46.6144,	34.903,	0.5,
# new cell
	SPHERE,	48.5441,	46.9354,	35.4283,	0.5,
# new cell
	SPHERE,	46.6512,	46.9622,	36.8866,	0.5,
# new cell
	SPHERE,	46.7892,	46.5644,	35.9121,	0.5,
# new cell
	SPHERE,	46.9272,	46.1666,	34.9376,	0.5,
# new cell
	SPHERE,	47.3058,	46.8854,	36.4374,	0.5,
# new cell
	SPHERE,	47.4438,	46.4876,	35.4629,	0.5,
# new cell
	SPHERE,	47.9604,	46.8086,	35.9882,	0.5,
# new cell
	SPHERE,	46.7221,	46.7586,	36.9973,	0.5,
# new cell
	SPHERE,	46.8601,	46.3608,	36.0228,	0.5,
# new cell
	SPHERE,	47.3767,	46.6818,	36.5481,	0.5,
# new cell
	SPHERE,	46.793,	46.555,	37.108,	0.5,
# new cell
	SPHERE,	46.084,	48.591,	36.001,	0.5,
# new cell
	SPHERE,	45.7598,	48.5296,	35.7218,	0.5,
# new cell
	SPHERE,	45.4356,	48.4682,	35.4426,	0.5,
# new cell
	SPHERE,	45.1114,	48.4068,	35.1634,	0.5,
# new cell
	SPHERE,	44.7872,	48.3454,	34.8842,	0.5,
# new cell
	SPHERE,	44.463,	48.284,	34.605,	0.5,
# new cell
	SPHERE,	44.1388,	48.2226,	34.3258,	0.5,
# new cell
	SPHERE,	43.8146,	48.1612,	34.0466,	0.5,
# new cell
	SPHERE,	43.4904,	48.0998,	33.7674,	0.5,
# new cell
	SPHERE,	43.1662,	48.0384,	33.4882,	0.5,
# new cell
	SPHERE,	42.842,	47.977,	33.209,	0.5,
# new cell
	SPHERE,	46.7386,	48.5142,	35.5518,	0.5,
# new cell
	SPHERE,	46.4144,	48.4528,	35.2726,	0.5,
# new cell
	SPHERE,	46.0902,	48.3914,	34.9934,	0.5,
# new cell
	SPHERE,	45.766,	48.33,	34.7142,	0.5,
# new cell
	SPHERE,	45.4418,	48.2686,	34.435,	0.5,
# new cell
	SPHERE,	45.1176,	48.2072,	34.1558,	0.5,
# new cell
	SPHERE,	44.7934,	48.1458,	33.8766,	0.5,
# new cell
	SPHERE,	44.4692,	48.0844,	33.5974,	0.5,
# new cell
	SPHERE,	44.145,	48.023,	33.3182,	0.5,
# new cell
	SPHERE,	43.8208,	47.9616,	33.039,	0.5,
# new cell
	SPHERE,	47.3932,	48.4374,	35.1026,	0.5,
# new cell
	SPHERE,	47.069,	48.376,	34.8234,	0.5,
# new cell
	SPHERE,	46.7448,	48.3146,	34.5442,	0.5,
# new cell
	SPHERE,	46.4206,	48.2532,	34.265,	0.5,
# new cell
	SPHERE,	46.0964,	48.1918,	33.9858,	0.5,
# new cell
	SPHERE,	45.7722,	48.1304,	33.7066,	0.5,
# new cell
	SPHERE,	45.448,	48.069,	33.4274,	0.5,
# new cell
	SPHERE,	45.1238,	48.0076,	33.1482,	0.5,
# new cell
	SPHERE,	44.7996,	47.9462,	32.869,	0.5,
# new cell
	SPHERE,	48.0478,	48.3606,	34.6534,	0.5,
# new cell
	SPHERE,	47.7236,	48.2992,	34.3742,	0.5,
# new cell
	SPHERE,	47.3994,	48.2378,	34.095,	0.5,
# new cell
	SPHERE,	47.0752,	48.1764,	33.8158,	0.5,
# new cell
	SPHERE,	46.751,	48.115,	33.5366,	0.5,
# new cell
	SPHERE,	46.4268,	48.0536,	33.2574,	0.5,
# new cell
	SPHERE,	46.1026,	47.9922,	32.9782,	0.5,
# new cell
	SPHERE,	45.7784,	47.9308,	32.699,	0.5,
# new cell
	SPHERE,	48.7024,	48.2838,	34.2042,	0.5,
# new cell
	SPHERE,	48.3782,	48.2224,	33.925,	0.5,
# new cell
	SPHERE,	48.054,	48.161,	33.6458,	0.5,
# new cell
	SPHERE,	47.7298,	48.0996,	33.3666,	0.5,
# new cell
	SPHERE,	47.4056,	48.0382,	33.0874,	0.5,
# new cell
	SPHERE,	47.0814,	47.9768,	32.8082,	0.5,
# new cell
	SPHERE,	46.7572,	47.9154,	32.529,	0.5,
# new cell
	SPHERE,	49.357,	48.207,	33.755,	0.5,
# new cell
	SPHERE,	49.0328,	48.1456,	33.4758,	0.5,
# new cell
	SPHERE,	48.7086,	48.0842,	33.1966,	0.5,
# new cell
	SPHERE,	48.3844,	48.0228,	32.9174,	0.5,
# new cell
	SPHERE,	48.0602,	47.9614,	32.6382,	0.5,
# new cell
	SPHERE,	47.736,	47.9,	32.359,	0.5,
# new cell
	SPHERE,	50.0116,	48.1302,	33.3058,	0.5,
# new cell
	SPHERE,	49.6874,	48.0688,	33.0266,	0.5,
# new cell
	SPHERE,	49.3632,	48.0074,	32.7474,	0.5,
# new cell
	SPHERE,	49.039,	47.946,	32.4682,	0.5,
# new cell
	SPHERE,	48.7148,	47.8846,	32.189,	0.5,
# new cell
	SPHERE,	50.6662,	48.0534,	32.8566,	0.5,
# new cell
	SPHERE,	50.342,	47.992,	32.5774,	0.5,
# new cell
	SPHERE,	50.0178,	47.9306,	32.2982,	0.5,
# new cell
	SPHERE,	49.6936,	47.8692,	32.019,	0.5,
# new cell
	SPHERE,	51.3208,	47.9766,	32.4074,	0.5,
# new cell
	SPHERE,	50.9966,	47.9152,	32.1282,	0.5,
# new cell
	SPHERE,	50.6724,	47.8538,	31.849,	0.5,
# new cell
	SPHERE,	51.9754,	47.8998,	31.9582,	0.5,
# new cell
	SPHERE,	51.6512,	47.8384,	31.679,	0.5,
# new cell
	SPHERE,	52.63,	47.823,	31.509,	0.5,
# new cell
	SPHERE,	46.222,	48.1932,	35.0265,	0.5,
# new cell
	SPHERE,	45.8978,	48.1318,	34.7473,	0.5,
# new cell
	SPHERE,	45.5736,	48.0704,	34.4681,	0.5,
# new cell
	SPHERE,	45.2494,	48.009,	34.1889,	0.5,
# new cell
	SPHERE,	44.9252,	47.9476,	33.9097,	0.5,
# new cell
	SPHERE,	44.601,	47.8862,	33.6305,	0.5,
# new cell
	SPHERE,	44.2768,	47.8248,	33.3513,	0.5,
# new cell
	SPHERE,	43.9526,	47.7634,	33.0721,	0.5,
# new cell
	SPHERE,	43.6284,	47.702,	32.7929,	0.5,
# new cell
	SPHERE,	43.3042,	47.6406,	32.5137,	0.5,
# new cell
	SPHERE,	46.8766,	48.1164,	34.5773,	0.5,
# new cell
	SPHERE,	46.5524,	48.055,	34.2981,	0.5,
# new cell
	SPHERE,	46.2282,	47.9936,	34.0189,	0.5,
# new cell
	SPHERE,	45.904,	47.9322,	33.7397,	0.5,
# new cell
	SPHERE,	45.5798,	47.8708,	33.4605,	0.5,
# new cell
	SPHERE,	45.2556,	47.8094,	33.1813,	0.5,
# new cell
	SPHERE,	44.9314,	47.748,	32.9021,	0.5,
# new cell
	SPHERE,	44.6072,	47.6866,	32.6229,	0.5,
# new cell
	SPHERE,	44.283,	47.6252,	32.3437,	0.5,
# new cell
	SPHERE,	47.5312,	48.0396,	34.1281,	0.5,
# new cell
	SPHERE,	47.207,	47.9782,	33.8489,	0.5,
# new cell
	SPHERE,	46.8828,	47.9168,	33.5697,	0.5,
# new cell
	SPHERE,	46.5586,	47.8554,	33.2905,	0.5,
# new cell
	SPHERE,	46.2344,	47.794,	33.0113,	0.5,
# new cell
	SPHERE,	45.9102,	47.7326,	32.7321,	0.5,
# new cell
	SPHERE,	45.586,	47.6712,	32.4529,	0.5,
# new cell
	SPHERE,	45.2618,	47.6098,	32.1737,	0.5,
# new cell
	SPHERE,	48.1858,	47.9628,	33.6789,	0.5,
# new cell
	SPHERE,	47.8616,	47.9014,	33.3997,	0.5,
# new cell
	SPHERE,	47.5374,	47.84,	33.1205,	0.5,
# new cell
	SPHERE,	47.2132,	47.7786,	32.8413,	0.5,
# new cell
	SPHERE,	46.889,	47.7172,	32.5621,	0.5,
# new cell
	SPHERE,	46.5648,	47.6558,	32.2829,	0.5,
# new cell
	SPHERE,	46.2406,	47.5944,	32.0037,	0.5,
# new cell
	SPHERE,	48.8404,	47.886,	33.2297,	0.5,
# new cell
	SPHERE,	48.5162,	47.8246,	32.9505,	0.5,
# new cell
	SPHERE,	48.192,	47.7632,	32.6713,	0.5,
# new cell
	SPHERE,	47.8678,	47.7018,	32.3921,	0.5,
# new cell
	SPHERE,	47.5436,	47.6404,	32.1129,	0.5,
# new cell
	SPHERE,	47.2194,	47.579,	31.8337,	0.5,
# new cell
	SPHERE,	49.495,	47.8092,	32.7805,	0.5,
# new cell
	SPHERE,	49.1708,	47.7478,	32.5013,	0.5,
# new cell
	SPHERE,	48.8466,	47.6864,	32.2221,	0.5,
# new cell
	SPHERE,	48.5224,	47.625,	31.9429,	0.5,
# new cell
	SPHERE,	48.1982,	47.5636,	31.6637,	0.5,
# new cell
	SPHERE,	50.1496,	47.7324,	32.3313,	0.5,
# new cell
	SPHERE,	49.8254,	47.671,	32.0521,	0.5,
# new cell
	SPHERE,	49.5012,	47.6096,	31.7729,	0.5,
# new cell
	SPHERE,	49.177,	47.5482,	31.4937,	0.5,
# new cell
	SPHERE,	50.8042,	47.6556,	31.8821,	0.5,
# new cell
	SPHERE,	50.48,	47.5942,	31.6029,	0.5,
# new cell
	SPHERE,	50.1558,	47.5328,	31.3237,	0.5,
# new cell
	SPHERE,	51.4588,	47.5788,	31.4329,	0.5,
# new cell
	SPHERE,	51.1346,	47.5174,	31.1537,	0.5,
# new cell
	SPHERE,	52.1134,	47.502,	30.9837,	0.5,
# new cell
	SPHERE,	46.36,	47.7954,	34.052,	0.5,
# new cell
	SPHERE,	46.0358,	47.734,	33.7728,	0.5,
# new cell
	SPHERE,	45.7116,	47.6726,	33.4936,	0.5,
# new cell
	SPHERE,	45.3874,	47.6112,	33.2144,	0.5,
# new cell
	SPHERE,	45.0632,	47.5498,	32.9352,	0.5,
# new cell
	SPHERE,	44.739,	47.4884,	32.656,	0.5,
# new cell
	SPHERE,	44.4148,	47.427,	32.3768,	0.5,
# new cell
	SPHERE,	44.0906,	47.3656,	32.0976,	0.5,
# new cell
	SPHERE,	43.7664,	47.3042,	31.8184,	0.5,
# new cell
	SPHERE,	47.0146,	47.7186,	33.6028,	0.5,
# new cell
	SPHERE,	46.6904,	47.6572,	33.3236,	0.5,
# new cell
	SPHERE,	46.3662,	47.5958,	33.0444,	0.5,
# new cell
	SPHERE,	46.042,	47.5344,	32.7652,	0.5,
# new cell
	SPHERE,	45.7178,	47.473,	32.486,	0.5,
# new cell
	SPHERE,	45.3936,	47.4116,	32.2068,	0.5,
# new cell
	SPHERE,	45.0694,	47.3502,	31.9276,	0.5,
# new cell
	SPHERE,	44.7452,	47.2888,	31.6484,	0.5,
# new cell
	SPHERE,	47.6692,	47.6418,	33.1536,	0.5,
# new cell
	SPHERE,	47.345,	47.5804,	32.8744,	0.5,
# new cell
	SPHERE,	47.0208,	47.519,	32.5952,	0.5,
# new cell
	SPHERE,	46.6966,	47.4576,	32.316,	0.5,
# new cell
	SPHERE,	46.3724,	47.3962,	32.0368,	0.5,
# new cell
	SPHERE,	46.0482,	47.3348,	31.7576,	0.5,
# new cell
	SPHERE,	45.724,	47.2734,	31.4784,	0.5,
# new cell
	SPHERE,	48.3238,	47.565,	32.7044,	0.5,
# new cell
	SPHERE,	47.9996,	47.5036,	32.4252,	0.5,
# new cell
	SPHERE,	47.6754,	47.4422,	32.146,	0.5,
# new cell
	SPHERE,	47.3512,	47.3808,	31.8668,	0.5,
# new cell
	SPHERE,	47.027,	47.3194,	31.5876,	0.5,
# new cell
	SPHERE,	46.7028,	47.258,	31.3084,	0.5,
# new cell
	SPHERE,	48.9784,	47.4882,	32.2552,	0.5,
# new cell
	SPHERE,	48.6542,	47.4268,	31.976,	0.5,
# new cell
	SPHERE,	48.33,	47.3654,	31.6968,	0.5,
# new cell
	SPHERE,	48.0058,	47.304,	31.4176,	0.5,
# new cell
	SPHERE,	47.6816,	47.2426,	31.1384,	0.5,
# new cell
	SPHERE,	49.633,	47.4114,	31.806,	0.5,
# new cell
	SPHERE,	49.3088,	47.35,	31.5268,	0.5,
# new cell
	SPHERE,	48.9846,	47.2886,	31.2476,	0.5,
# new cell
	SPHERE,	48.6604,	47.2272,	30.9684,	0.5,
# new cell
	SPHERE,	50.2876,	47.3346,	31.3568,	0.5,
# new cell
	SPHERE,	49.9634,	47.2732,	31.0776,	0.5,
# new cell
	SPHERE,	49.6392,	47.2118,	30.7984,	0.5,
# new cell
	SPHERE,	50.9422,	47.2578,	30.9076,	0.5,
# new cell
	SPHERE,	50.618,	47.1964,	30.6284,	0.5,
# new cell
	SPHERE,	51.5968,	47.181,	30.4584,	0.5,
# new cell
	SPHERE,	46.498,	47.3976,	33.0775,	0.5,
# new cell
	SPHERE,	46.1738,	47.3362,	32.7983,	0.5,
# new cell
	SPHERE,	45.8496,	47.2748,	32.5191,	0.5,
# new cell
	SPHERE,	45.5254,	47.2134,	32.2399,	0.5,
# new cell
	SPHERE,	45.2012,	47.152,	31.9607,	0.5,
# new cell
	SPHERE,	44.877,	47.0906,	31.6815,	0.5,
# new cell
	SPHERE,	44.5528,	47.0292,	31.4023,	0.5,
# new cell
	SPHERE,	44.2286,	46.9678,	31.1231,	0.5,
# new cell
	SPHERE,	47.1526,	47.3208,	32.6283,	0.5,
# new cell
	SPHERE,	46.8284,	47.2594,	32.3491,	0.5,
# new cell
	SPHERE,	46.5042,	47.198,	32.0699,	0.5,
# new cell
	SPHERE,	46.18,	47.1366,	31.7907,	0.5,
# new cell
	SPHERE,	45.8558,	47.0752,	31.5115,	0.5,
# new cell
	SPHERE,	45.5316,	47.0138,	31.2323,	0.5,
# new cell
	SPHERE,	45.2074,	46.9524,	30.9531,	0.5,
# new cell
	SPHERE,	47.8072,	47.244,	32.1791,	0.5,
# new cell
	SPHERE,	47.483,	47.1826,	31.8999,	0.5,
# new cell
	SPHERE,	47.1588,	47.1212,	31.6207,	0.5,
# new cell
	SPHERE,	46.8346,	47.0598,	31.3415,	0.5,
# new cell
	SPHERE,	46.5104,	46.9984,	31.0623,	0.5,
# new cell
	SPHERE,	46.1862,	46.937,	30.7831,	0.5,
# new cell
	SPHERE,	48.4618,	47.1672,	31.7299,	0.5,
# new cell
	SPHERE,	48.1376,	47.1058,	31.4507,	0.5,
# new cell
	SPHERE,	47.8134,	47.0444,	31.1715,	0.5,
# new cell
	SPHERE,	47.4892,	46.983,	30.8923,	0.5,
# new cell
	SPHERE,	47.165,	46.9216,	30.6131,	0.5,
# new cell
	SPHERE,	49.1164,	47.0904,	31.2807,	0.5,
# new cell
	SPHERE,	48.7922,	47.029,	31.0015,	0.5,
# new cell
	SPHERE,	48.468,	46.9676,	30.7223,	0.5,
# new cell
	SPHERE,	48.1438,	46.9062,	30.4431,	0.5,
# new cell
	SPHERE,	49.771,	47.0136,	30.8315,	0.5,
# new cell
	SPHERE,	49.4468,	46.9522,	30.5523,	0.5,
# new cell
	SPHERE,	49.1226,	46.8908,	30.2731,	0.5,
# new cell
	SPHERE,	50.4256,	46.9368,	30.3823,	0.5,
# new cell
	SPHERE,	50.1014,	46.8754,	30.1031,	0.5,
# new cell
	SPHERE,	51.0802,	46.86,	29.9331,	0.5,
# new cell
	SPHERE,	46.636,	46.9998,	32.103,	0.5,
# new cell
	SPHERE,	46.3118,	46.9384,	31.8238,	0.5,
# new cell
	SPHERE,	45.9876,	46.877,	31.5446,	0.5,
# new cell
	SPHERE,	45.6634,	46.8156,	31.2654,	0.5,
# new cell
	SPHERE,	45.3392,	46.7542,	30.9862,	0.5,
# new cell
	SPHERE,	45.015,	46.6928,	30.707,	0.5,
# new cell
	SPHERE,	44.6908,	46.6314,	30.4278,	0.5,
# new cell
	SPHERE,	47.2906,	46.923,	31.6538,	0.5,
# new cell
	SPHERE,	46.9664,	46.8616,	31.3746,	0.5,
# new cell
	SPHERE,	46.6422,	46.8002,	31.0954,	0.5,
# new cell
	SPHERE,	46.318,	46.7388,	30.8162,	0.5,
# new cell
	SPHERE,	45.9938,	46.6774,	30.537,	0.5,
# new cell
	SPHERE,	45.6696,	46.616,	30.2578,	0.5,
# new cell
	SPHERE,	47.9452,	46.8462,	31.2046,	0.5,
# new cell
	SPHERE,	47.621,	46.7848,	30.9254,	0.5,
# new cell
	SPHERE,	47.2968,	46.7234,	30.6462,	0.5,
# new cell
	SPHERE,	46.9726,	46.662,	30.367,	0.5,
# new cell
	SPHERE,	46.6484,	46.6006,	30.0878,	0.5,
# new cell
	SPHERE,	48.5998,	46.7694,	30.7554,	0.5,
# new cell
	SPHERE,	48.2756,	46.708,	30.4762,	0.5,
# new cell
	SPHERE,	47.9514,	46.6466,	30.197,	0.5,
# new cell
	SPHERE,	47.6272,	46.5852,	29.9178,	0.5,
# new cell
	SPHERE,	49.2544,	46.6926,	30.3062,	0.5,
# new cell
	SPHERE,	48.9302,	46.6312,	30.027,	0.5,
# new cell
	SPHERE,	48.606,	46.5698,	29.7478,	0.5,
# new cell
	SPHERE,	49.909,	46.6158,	29.857,	0.5,
# new cell
	SPHERE,	49.5848,	46.5544,	29.5778,	0.5,
# new cell
	SPHERE,	50.5636,	46.539,	29.4078,	0.5,
# new cell
	SPHERE,	46.774,	46.602,	31.1285,	0.5,
# new cell
	SPHERE,	46.4498,	46.5406,	30.8493,	0.5,
# new cell
	SPHERE,	46.1256,	46.4792,	30.5701,	0.5,
# new cell
	SPHERE,	45.8014,	46.4178,	30.2909,	0.5,
# new cell
	SPHERE,	45.4772,	46.3564,	30.0117,	0.5,
# new cell
	SPHERE,	45.153,	46.295,	29.7325,	0.5,
# new cell
	SPHERE,	47.4286,	46.5252,	30.6793,	0.5,
# new cell
	SPHERE,	47.1044,	46.4638,	30.4001,	0.5,
# new cell
	SPHERE,	46.7802,	46.4024,	30.1209,	0.5,
# new cell
	SPHERE,	46.456,	46.341,	29.8417,	0.5,
# new cell
	SPHERE,	46.1318,	46.2796,	29.5625,	0.5,
# new cell
	SPHERE,	48.0832,	46.4484,	30.2301,	0.5,
# new cell
	SPHERE,	47.759,	46.387,	29.9509,	0.5,
# new cell
	SPHERE,	47.4348,	46.3256,	29.6717,	0.5,
# new cell
	SPHERE,	47.1106,	46.2642,	29.3925,	0.5,
# new cell
	SPHERE,	48.7378,	46.3716,	29.7809,	0.5,
# new cell
	SPHERE,	48.4136,	46.3102,	29.5017,	0.5,
# new cell
	SPHERE,	48.0894,	46.2488,	29.2225,	0.5,
# new cell
	SPHERE,	49.3924,	46.2948,	29.3317,	0.5,
# new cell
	SPHERE,	49.0682,	46.2334,	29.0525,	0.5,
# new cell
	SPHERE,	50.047,	46.218,	28.8825,	0.5,
# new cell
	SPHERE,	46.912,	46.2042,	30.154,	0.5,
# new cell
	SPHERE,	46.5878,	46.1428,	29.8748,	0.5,
# new cell
	SPHERE,	46.2636,	46.0814,	29.5956,	0.5,
# new cell
	SPHERE,	45.9394,	46.02,	29.3164,	0.5,
# new cell
	SPHERE,	45.6152,	45.9586,	29.0372,	0.5,
# new cell
	SPHERE,	47.5666,	46.1274,	29.7048,	0.5,
# new cell
	SPHERE,	47.2424,	46.066,	29.4256,	0.5,
# new cell
	SPHERE,	46.9182,	46.0046,	29.1464,	0.5,
# new cell
	SPHERE,	46.594,	45.9432,	28.8672,	0.5,
# new cell
	SPHERE,	48.2212,	46.0506,	29.2556,	0.5,
# new cell
	SPHERE,	47.897,	45.9892,	28.9764,	0.5,
# new cell
	SPHERE,	47.5728,	45.9278,	28.6972,	0.5,
# new cell
	SPHERE,	48.8758,	45.9738,	28.8064,	0.5,
# new cell
	SPHERE,	48.5516,	45.9124,	28.5272,	0.5,
# new cell
	SPHERE,	49.5304,	45.897,	28.3572,	0.5,
# new cell
	SPHERE,	47.05,	45.8064,	29.1795,	0.5,
# new cell
	SPHERE,	46.7258,	45.745,	28.9003,	0.5,
# new cell
	SPHERE,	46.4016,	45.6836,	28.6211,	0.5,
# new cell
	SPHERE,	46.0774,	45.6222,	28.3419,	0.5,
# new cell
	SPHERE,	47.7046,	45.7296,	28.7303,	0.5,
# new cell
	SPHERE,	47.3804,	45.6682,	28.4511,	0.5,
# new cell
	SPHERE,	47.0562,	45.6068,	28.1719,	0.5,
# new cell
	SPHERE,	48.3592,	45.6528,	28.2811,	0.5,
# new cell
	SPHERE,	48.035,	45.5914,	28.0019,	0.5,
# new cell
	SPHERE,	49.0138,	45.576,	27.8319,	0.5,
# new cell
	SPHERE,	47.188,	45.4086,	28.205,	0.5,
# new cell
	SPHERE,	46.8638,	45.3472,	27.9258,	0.5,
# new cell
	SPHERE,	46.5396,	45.2858,	27.6466,	0.5,
# new cell
	SPHERE,	47.8426,	45.3318,	27.7558,	0.5,
# new cell
	SPHERE,	47.5184,	45.2704,	27.4766,	0.5,
# new cell
	SPHERE,	48.4972,	45.255,	27.3066,	0.5,
# new cell
	SPHERE,	47.326,	45.0108,	27.2305,	0.5,
# new cell
	SPHERE,	47.0018,	44.9494,	26.9513,	0.5,
# new cell
	SPHERE,	47.9806,	44.934,	26.7813,	0.5,
# new cell
	SPHERE,	47.464,	44.613,	26.256,	0.5,
# new cell
	SPHERE,	45.919,	43.192,	26.334,	0.5,
# new cell
	SPHERE,	45.6113,	43.6705,	27.0215,	0.5,
# new cell
	SPHERE,	45.3036,	44.149,	27.709,	0.5,
# new cell
	SPHERE,	44.9959,	44.6275,	28.3965,	0.5,
# new cell
	SPHERE,	44.6882,	45.106,	29.084,	0.5,
# new cell
	SPHERE,	44.3805,	45.5845,	29.7715,	0.5,
# new cell
	SPHERE,	44.0728,	46.063,	30.459,	0.5,
# new cell
	SPHERE,	43.7651,	46.5415,	31.1465,	0.5,
# new cell
	SPHERE,	43.4574,	47.02,	31.834,	0.5,
# new cell
	SPHERE,	43.1497,	47.4985,	32.5215,	0.5,
# new cell
	SPHERE,	42.842,	47.977,	33.209,	0.5,
# new cell
	SPHERE,	46.0064,	43.5283,	27.4114,	0.5,
# new cell
	SPHERE,	45.6987,	44.0068,	28.0989,	0.5,
# new cell
	SPHERE,	45.391,	44.4853,	28.7864,	0.5,
# new cell
	SPHERE,	45.0833,	44.9638,	29.4739,	0.5,
# new cell
	SPHERE,	44.7756,	45.4423,	30.1614,	0.5,
# new cell
	SPHERE,	44.4679,	45.9208,	30.8489,	0.5,
# new cell
	SPHERE,	44.1602,	46.3993,	31.5364,	0.5,
# new cell
	SPHERE,	43.8525,	46.8778,	32.2239,	0.5,
# new cell
	SPHERE,	43.5448,	47.3563,	32.9114,	0.5,
# new cell
	SPHERE,	43.2371,	47.8348,	33.5989,	0.5,
# new cell
	SPHERE,	46.0938,	43.8646,	28.4888,	0.5,
# new cell
	SPHERE,	45.7861,	44.3431,	29.1763,	0.5,
# new cell
	SPHERE,	45.4784,	44.8216,	29.8638,	0.5,
# new cell
	SPHERE,	45.1707,	45.3001,	30.5513,	0.5,
# new cell
	SPHERE,	44.863,	45.7786,	31.2388,	0.5,
# new cell
	SPHERE,	44.5553,	46.2571,	31.9263,	0.5,
# new cell
	SPHERE,	44.2476,	46.7356,	32.6138,	0.5,
# new cell
	SPHERE,	43.9399,	47.2141,	33.3013,	0.5,
# new cell
	SPHERE,	43.6322,	47.6926,	33.9888,	0.5,
# new cell
	SPHERE,	46.1812,	44.2009,	29.5662,	0.5,
# new cell
	SPHERE,	45.8735,	44.6794,	30.2537,	0.5,
# new cell
	SPHERE,	45.5658,	45.1579,	30.9412,	0.5,
# new cell
	SPHERE,	45.2581,	45.6364,	31.6287,	0.5,
# new cell
	SPHERE,	44.9504,	46.1149,	32.3162,	0.5,
# new cell
	SPHERE,	44.6427,	46.5934,	33.0037,	0.5,
# new cell
	SPHERE,	44.335,	47.0719,	33.6912,	0.5,
# new cell
	SPHERE,	44.0273,	47.5504,	34.3787,	0.5,
# new cell
	SPHERE,	46.2686,	44.5372,	30.6436,	0.5,
# new cell
	SPHERE,	45.9609,	45.0157,	31.3311,	0.5,
# new cell
	SPHERE,	45.6532,	45.4942,	32.0186,	0.5,
# new cell
	SPHERE,	45.3455,	45.9727,	32.7061,	0.5,
# new cell
	SPHERE,	45.0378,	46.4512,	33.3936,	0.5,
# new cell
	SPHERE,	44.7301,	46.9297,	34.0811,	0.5,
# new cell
	SPHERE,	44.4224,	47.4082,	34.7686,	0.5,
# new cell
	SPHERE,	46.356,	44.8735,	31.721,	0.5,
# new cell
	SPHERE,	46.0483,	45.352,	32.4085,	0.5,
# new cell
	SPHERE,	45.7406,	45.8305,	33.096,	0.5,
# new cell
	SPHERE,	45.4329,	46.309,	33.7835,	0.5,
# new cell
	SPHERE,	45.1252,	46.7875,	34.471,	0.5,
# new cell
	SPHERE,	44.8175,	47.266,	35.1585,	0.5,
# new cell
	SPHERE,	46.4434,	45.2098,	32.7984,	0.5,
# new cell
	SPHERE,	46.1357,	45.6883,	33.4859,	0.5,
# new cell
	SPHERE,	45.828,	46.1668,	34.1734,	0.5,
# new cell
	SPHERE,	45.5203,	46.6453,	34.8609,	0.5,
# new cell
	SPHERE,	45.2126,	47.1238,	35.5484,	0.5,
# new cell
	SPHERE,	46.5308,	45.5461,	33.8758,	0.5,
# new cell
	SPHERE,	46.2231,	46.0246,	34.5633,	0.5,
# new cell
	SPHERE,	45.9154,	46.5031,	35.2508,	0.5,
# new cell
	SPHERE,	45.6077,	46.9816,	35.9383,	0.5,
# new cell
	SPHERE,	46.6182,	45.8824,	34.9532,	0.5,
# new cell
	SPHERE,	46.3105,	46.3609,	35.6407,	0.5,
# new cell
	SPHERE,	46.0028,	46.8394,	36.3282,	0.5,
# new cell
	SPHERE,	46.7056,	46.2187,	36.0306,	0.5,
# new cell
	SPHERE,	46.3979,	46.6972,	36.7181,	0.5,
# new cell
	SPHERE,	46.793,	46.555,	37.108,	0.5,
# new cell
	SPHERE,	46.0735,	43.3341,	26.3262,	0.5,
# new cell
	SPHERE,	45.7658,	43.8126,	27.0137,	0.5,
# new cell
	SPHERE,	45.4581,	44.2911,	27.7012,	0.5,
# new cell
	SPHERE,	45.1504,	44.7696,	28.3887,	0.5,
# new cell
	SPHERE,	44.8427,	45.2481,	29.0762,	0.5,
# new cell
	SPHERE,	44.535,	45.7266,	29.7637,	0.5,
# new cell
	SPHERE,	44.2273,	46.2051,	30.4512,	0.5,
# new cell
	SPHERE,	43.9196,	46.6836,	31.1387,	0.5,
# new cell
	SPHERE,	43.6119,	47.1621,	31.8262,	0.5,
# new cell
	SPHERE,	43.3042,	47.6406,	32.5137,	0.5,
# new cell
	SPHERE,	46.1609,	43.6704,	27.4036,	0.5,
# new cell
	SPHERE,	45.8532,	44.1489,	28.0911,	0.5,
# new cell
	SPHERE,	45.5455,	44.6274,	28.7786,	0.5,
# new cell
	SPHERE,	45.2378,	45.1059,	29.4661,	0.5,
# new cell
	SPHERE,	44.9301,	45.5844,	30.1536,	0.5,
# new cell
	SPHERE,	44.6224,	46.0629,	30.8411,	0.5,
# new cell
	SPHERE,	44.3147,	46.5414,	31.5286,	0.5,
# new cell
	SPHERE,	44.007,	47.0199,	32.2161,	0.5,
# new cell
	SPHERE,	43.6993,	47.4984,	32.9036,	0.5,
# new cell
	SPHERE,	46.2483,	44.0067,	28.481,	0.5,
# new cell
	SPHERE,	45.9406,	44.4852,	29.1685,	0.5,
# new cell
	SPHERE,	45.6329,	44.9637,	29.856,	0.5,
# new cell
	SPHERE,	45.3252,	45.4422,	30.5435,	0.5,
# new cell
	SPHERE,	45.0175,	45.9207,	31.231,	0.5,
# new cell
	SPHERE,	44.7098,	46.3992,	31.9185,	0.5,
# new cell
	SPHERE,	44.4021,	46.8777,	32.606,	0.5,
# new cell
	SPHERE,	44.0944,	47.3562,	33.2935,	0.5,
# new cell
	SPHERE,	46.3357,	44.343,	29.5584,	0.5,
# new cell
	SPHERE,	46.028,	44.8215,	30.2459,	0.5,
# new cell
	SPHERE,	45.7203,	45.3,	30.9334,	0.5,
# new cell
	SPHERE,	45.4126,	45.7785,	31.6209,	0.5,
# new cell
	SPHERE,	45.1049,	46.257,	32.3084,	0.5,
# new cell
	SPHERE,	44.7972,	46.7355,	32.9959,	0.5,
# new cell
	SPHERE,	44.4895,	47.214,	33.6834,	0.5,
# new cell
	SPHERE,	46.4231,	44.6793,	30.6358,	0.5,
# new cell
	SPHERE,	46.1154,	45.1578,	31.3233,	0.5,
# new cell
	SPHERE,	45.8077,	45.6363,	32.0108,	0.5,
# new cell
	SPHERE,	45.5,	46.1148,	32.6983,	0.5,
# new cell
	SPHERE,	45.1923,	46.5933,	33.3858,	0.5,
# new cell
	SPHERE,	44.8846,	47.0718,	34.0733,	0.5,
# new cell
	SPHERE,	46.5105,	45.0156,	31.7132,	0.5,
# new cell
	SPHERE,	46.2028,	45.4941,	32.4007,	0.5,
# new cell
	SPHERE,	45.8951,	45.9726,	33.0882,	0.5,
# new cell
	SPHERE,	45.5874,	46.4511,	33.7757,	0.5,
# new cell
	SPHERE,	45.2797,	46.9296,	34.4632,	0.5,
# new cell
	SPHERE,	46.5979,	45.3519,	32.7906,	0.5,
# new cell
	SPHERE,	46.2902,	45.8304,	33.4781,	0.5,
# new cell
	SPHERE,	45.9825,	46.3089,	34.1656,	0.5,
# new cell
	SPHERE,	45.6748,	46.7874,	34.8531,	0.5,
# new cell
	SPHERE,	46.6853,	45.6882,	33.868,	0.5,
# new cell
	SPHERE,	46.3776,	46.1667,	34.5555,	0.5,
# new cell
	SPHERE,	46.0699,	46.6452,	35.243,	0.5,
# new cell
	SPHERE,	46.7727,	46.0245,	34.9454,	0.5,
# new cell
	SPHERE,	46.465,	46.503,	35.6329,	0.5,
# new cell
	SPHERE,	46.8601,	46.3608,	36.0228,	0.5,
# new cell
	SPHERE,	46.228,	43.4762,	26.3184,	0.5,
# new cell
	SPHERE,	45.9203,	43.9547,	27.0059,	0.5,
# new cell
	SPHERE,	45.6126,	44.4332,	27.6934,	0.5,
# new cell
	SPHERE,	45.3049,	44.9117,	28.3809,	0.5,
# new cell
	SPHERE,	44.9972,	45.3902,	29.0684,	0.5,
# new cell
	SPHERE,	44.6895,	45.8687,	29.7559,	0.5,
# new cell
	SPHERE,	44.3818,	46.3472,	30.4434,	0.5,
# new cell
	SPHERE,	44.0741,	46.8257,	31.1309,	0.5,
# new cell
	SPHERE,	43.7664,	47.3042,	31.8184,	0.5,
# new cell
	SPHERE,	46.3154,	43.8125,	27.3958,	0.5,
# new cell
	SPHERE,	46.0077,	44.291,	28.0833,	0.5,
# new cell
	SPHERE,	45.7,	44.7695,	28.7708,	0.5,
# new cell
	SPHERE,	45.3923,	45.248,	29.4583,	0.5,
# new cell
	SPHERE,	45.0846,	45.7265,	30.1458,	0.5,
# new cell
	SPHERE,	44.7769,	46.205,	30.8333,	0.5,
# new cell
	SPHERE,	44.4692,	46.6835,	31.5208,	0.5,
# new cell
	SPHERE,	44.1615,	47.162,	32.2083,	0.5,
# new cell
	SPHERE,	46.4028,	44.1488,	28.4732,	0.5,
# new cell
	SPHERE,	46.0951,	44.6273,	29.1607,	0.5,
# new cell
	SPHERE,	45.7874,	45.1058,	29.8482,	0.5,
# new cell
	SPHERE,	45.4797,	45.5843,	30.5357,	0.5,
# new cell
	SPHERE,	45.172,	46.0628,	31.2232,	0.5,
# new cell
	SPHERE,	44.8643,	46.5413,	31.9107,	0.5,
# new cell
	SPHERE,	44.5566,	47.0198,	32.5982,	0.5,
# new cell
	SPHERE,	46.4902,	44.4851,	29.5506,	0.5,
# new cell
	SPHERE,	46.1825,	44.9636,	30.2381,	0.5,
# new cell
	SPHERE,	45.8748,	45.4421,	30.9256,	0.5,
# new cell
	SPHERE,	45.5671,	45.9206,	31.6131,	0.5,
# new cell
	SPHERE,	45.2594,	46.3991,	32.3006,	0.5,
# new cell
	SPHERE,	44.9517,	46.8776,	32.9881,	0.5,
# new cell
	SPHERE,	46.5776,	44.8214,	30.628,	0.5,
# new cell
	SPHERE,	46.2699,	45.2999,	31.3155,	0.5,
# new cell
	SPHERE,	45.9622,	45.7784,	32.003,	0.5,
# new cell
	SPHERE,	45.6545,	46.2569,	32.6905,	0.5,
# new cell
	SPHERE,	45.3468,	46.7354,	33.378,	0.5,
# new cell
	SPHERE,	46.665,	45.1577,	31.7054,	0.5,
# new cell
	SPHERE,	46.3573,	45.6362,	32.3929,	0.5,
# new cell
	SPHERE,	46.0496,	46.1147,	33.0804,	0.5,
# new cell
	SPHERE,	45.7419,	46.5932,	33.7679,	0.5,
# new cell
	SPHERE,	46.7524,	45.494,	32.7828,	0.5,
# new cell
	SPHERE,	46.4447,	45.9725,	33.4703,	0.5,
# new cell
	SPHERE,	46.137,	46.451,	34.1578,	0.5,
# new cell
	SPHERE,	46.8398,	45.8303,	33.8602,	0.5,
# new cell
	SPHERE,	46.5321,	46.3088,	34.5477,	0.5,
# new cell
	SPHERE,	46.9272,	46.1666,	34.9376,	0.5,
# new cell
	SPHERE,	46.3825,	43.6183,	26.3106,	0.5,
# new cell
	SPHERE,	46.0748,	44.0968,	26.9981,	0.5,
# new cell
	SPHERE,	45.7671,	44.5753,	27.6856,	0.5,
# new cell
	SPHERE,	45.4594,	45.0538,	28.3731,	0.5,
# new cell
	SPHERE,	45.1517,	45.5323,	29.0606,	0.5,
# new cell
	SPHERE,	44.844,	46.0108,	29.7481,	0.5,
# new cell
	SPHERE,	44.5363,	46.4893,	30.4356,	0.5,
# new cell
	SPHERE,	44.2286,	46.9678,	31.1231,	0.5,
# new cell
	SPHERE,	46.4699,	43.9546,	27.388,	0.5,
# new cell
	SPHERE,	46.1622,	44.4331,	28.0755,	0.5,
# new cell
	SPHERE,	45.8545,	44.9116,	28.763,	0.5,
# new cell
	SPHERE,	45.5468,	45.3901,	29.4505,	0.5,
# new cell
	SPHERE,	45.2391,	45.8686,	30.138,	0.5,
# new cell
	SPHERE,	44.9314,	46.3471,	30.8255,	0.5,
# new cell
	SPHERE,	44.6237,	46.8256,	31.513,	0.5,
# new cell
	SPHERE,	46.5573,	44.2909,	28.4654,	0.5,
# new cell
	SPHERE,	46.2496,	44.7694,	29.1529,	0.5,
# new cell
	SPHERE,	45.9419,	45.2479,	29.8404,	0.5,
# new cell
	SPHERE,	45.6342,	45.7264,	30.5279,	0.5,
# new cell
	SPHERE,	45.3265,	46.2049,	31.2154,	0.5,
# new cell
	SPHERE,	45.0188,	46.6834,	31.9029,	0.5,
# new cell
	SPHERE,	46.6447,	44.6272,	29.5428,	0.5,
# new cell
	SPHERE,	46.337,	45.1057,	30.2303,	0.5,
# new cell
	SPHERE,	46.0293,	45.5842,	30.9178,	0.5,
# new cell
	SPHERE,	45.7216,	46.0627,	31.6053,	0.5,
# new cell
	SPHERE,	45.4139,	46.5412,	32.2928,	0.5,
# new cell
	SPHERE,	46.7321,	44.9635,	30.6202,	0.5,
# new cell
	SPHERE,	46.4244,	45.442,	31.3077,	0.5,
# new cell
	SPHERE,	46.1167,	45.9205,	31.9952,	0.5,
# new cell
	SPHERE,	45.809,	46.399,	32.6827,	0.5,
# new cell
	SPHERE,	46.8195,	45.2998,	31.6976,	0.5,
# new cell
	SPHERE,	46.5118,	45.7783,	32.3851,	0.5,
# new cell
	SPHERE,	46.2041,	46.2568,	33.0726,	0.5,
# new cell
	SPHERE,	46.9069,	45.6361,	32.775,	0.5,
# new cell
	SPHERE,	46.5992,	46.1146,	33.4625,	0.5,
# new cell
	SPHERE,	46.9943,	45.9724,	33.8524,	0.5,
# new cell
	SPHERE,	46.537,	43.7604,	26.3028,	0.5,
# new cell
	SPHERE,	46.2293,	44.2389,	26.9903,	0.5,
# new cell
	SPHERE,	45.9216,	44.7174,	27.6778,	0.5,
# new cell
	SPHERE,	45.6139,	45.1959,	28.3653,	0.5,
# new cell
	SPHERE,	45.3062,	45.6744,	29.0528,	0.5,
# new cell
	SPHERE,	44.9985,	46.1529,	29.7403,	0.5,
# new cell
	SPHERE,	44.6908,	46.6314,	30.4278,	0.5,
# new cell
	SPHERE,	46.6244,	44.0967,	27.3802,	0.5,
# new cell
	SPHERE,	46.3167,	44.5752,	28.0677,	0.5,
# new cell
	SPHERE,	46.009,	45.0537,	28.7552,	0.5,
# new cell
	SPHERE,	45.7013,	45.5322,	29.4427,	0.5,
# new cell
	SPHERE,	45.3936,	46.0107,	30.1302,	0.5,
# new cell
	SPHERE,	45.0859,	46.4892,	30.8177,	0.5,
# new cell
	SPHERE,	46.7118,	44.433,	28.4576,	0.5,
# new cell
	SPHERE,	46.4041,	44.9115,	29.1451,	0.5,
# new cell
	SPHERE,	46.0964,	45.39,	29.8326,	0.5,
# new cell
	SPHERE,	45.7887,	45.8685,	30.5201,	0.5,
# new cell
	SPHERE,	45.481,	46.347,	31.2076,	0.5,
# new cell
	SPHERE,	46.7992,	44.7693,	29.535,	0.5,
# new cell
	SPHERE,	46.4915,	45.2478,	30.2225,	0.5,
# new cell
	SPHERE,	46.1838,	45.7263,	30.91,	0.5,
# new cell
	SPHERE,	45.8761,	46.2048,	31.5975,	0.5,
# new cell
	SPHERE,	46.8866,	45.1056,	30.6124,	0.5,
# new cell
	SPHERE,	46.5789,	45.5841,	31.2999,	0.5,
# new cell
	SPHERE,	46.2712,	46.0626,	31.9874,	0.5,
# new cell
	SPHERE,	46.974,	45.4419,	31.6898,	0.5,
# new cell
	SPHERE,	46.6663,	45.9204,	32.3773,	0.5,
# new cell
	SPHERE,	47.0614,	45.7782,	32.7672,	0.5,
# new cell
	SPHERE,	46.6915,	43.9025,	26.295,	0.5,
# new cell
	SPHERE,	46.3838,	44.381,	26.9825,	0.5,
# new cell
	SPHERE,	46.0761,	44.8595,	27.67,	0.5,
# new cell
	SPHERE,	45.7684,	45.338,	28.3575,	0.5,
# new cell
	SPHERE,	45.4607,	45.8165,	29.045,	0.5,
# new cell
	SPHERE,	45.153,	46.295,	29.7325,	0.5,
# new cell
	SPHERE,	46.7789,	44.2388,	27.3724,	0.5,
# new cell
	SPHERE,	46.4712,	44.7173,	28.0599,	0.5,
# new cell
	SPHERE,	46.1635,	45.1958,	28.7474,	0.5,
# new cell
	SPHERE,	45.8558,	45.6743,	29.4349,	0.5,
# new cell
	SPHERE,	45.5481,	46.1528,	30.1224,	0.5,
# new cell
	SPHERE,	46.8663,	44.5751,	28.4498,	0.5,
# new cell
	SPHERE,	46.5586,	45.0536,	29.1373,	0.5,
# new cell
	SPHERE,	46.2509,	45.5321,	29.8248,	0.5,
# new cell
	SPHERE,	45.9432,	46.0106,	30.5123,	0.5,
# new cell
	SPHERE,	46.9537,	44.9114,	29.5272,	0.5,
# new cell
	SPHERE,	46.646,	45.3899,	30.2147,	0.5,
# new cell
	SPHERE,	46.3383,	45.8684,	30.9022,	0.5,
# new cell
	SPHERE,	47.0411,	45.2477,	30.6046,	0.5,
# new cell
	SPHERE,	46.7334,	45.7262,	31.2921,	0.5,
# new cell
	SPHERE,	47.1285,	45.584,	31.682,	0.5,
# new cell
	SPHERE,	46.846,	44.0446,	26.2872,	0.5,
# new cell
	SPHERE,	46.5383,	44.5231,	26.9747,	0.5,
# new cell
	SPHERE,	46.2306,	45.0016,	27.6622,	0.5,
# new cell
	SPHERE,	45.9229,	45.4801,	28.3497,	0.5,
# new cell
	SPHERE,	45.6152,	45.9586,	29.0372,	0.5,
# new cell
	SPHERE,	46.9334,	44.3809,	27.3646,	0.5,
# new cell
	SPHERE,	46.6257,	44.8594,	28.0521,	0.5,
# new cell
	SPHERE,	46.318,	45.3379,	28.7396,	0.5,
# new cell
	SPHERE,	46.0103,	45.8164,	29.4271,	0.5,
# new cell
	SPHERE,	47.0208,	44.7172,	28.442,	0.5,
# new cell
	SPHERE,	46.7131,	45.1957,	29.1295,	0.5,
# new cell
	SPHERE,	46.4054,	45.6742,	29.817,	0.5,
# new cell
	SPHERE,	47.1082,	45.0535,	29.5194,	0.5,
# new cell
	SPHERE,	46.8005,	45.532,	30.2069,	0.5,
# new cell
	SPHERE,	47.1956,	45.3898,	30.5968,	0.5,
# new cell
	SPHERE,	47.0005,	44.1867,	26.2794,	0.5,
# new cell
	SPHERE,	46.6928,	44.6652,	26.9669,	0.5,
# new cell
	SPHERE,	46.3851,	45.1437,	27.6544,	0.5,
# new cell
	SPHERE,	46.0774,	45.6222,	28.3419,	0.5,
# new cell
	SPHERE,	47.0879,	44.523,	27.3568,	0.5,
# new cell
	SPHERE,	46.7802,	45.0015,	28.0443,	0.5,
# new cell
	SPHERE,	46.4725,	45.48,	28.7318,	0.5,
# new cell
	SPHERE,	47.1753,	44.8593,	28.4342,	0.5,
# new cell
	SPHERE,	46.8676,	45.3378,	29.1217,	0.5,
# new cell
	SPHERE,	47.2627,	45.1956,	29.5116,	0.5,
# new cell
	SPHERE,	47.155,	44.3288,	26.2716,	0.5,
# new cell
	SPHERE,	46.8473,	44.8073,	26.9591,	0.5,
# new cell
	SPHERE,	46.5396,	45.2858,	27.6466,	0.5,
# new cell
	SPHERE,	47.2424,	44.6651,	27.349,	0.5,
# new cell
	SPHERE,	46.9347,	45.1436,	28.0365,	0.5,
# new cell
	SPHERE,	47.3298,	45.0014,	28.4264,	0.5,
# new cell
	SPHERE,	47.3095,	44.4709,	26.2638,	0.5,
# new cell
	SPHERE,	47.0018,	44.9494,	26.9513,	0.5,
# new cell
	SPHERE,	47.3969,	44.8072,	27.3412,	0.5,
# new cell
	SPHERE,	47.464,	44.613,	26.256,	0.5,
# new cell
	SPHERE,	41.256,	36.085,	32.538,	0.5,
# new cell
	SPHERE,	41.6379,	35.9535,	32.6712,	0.5,
# new cell
	SPHERE,	42.0198,	35.822,	32.8044,	0.5,
# new cell
	SPHERE,	42.4017,	35.6905,	32.9376,	0.5,
# new cell
	SPHERE,	42.7836,	35.559,	33.0708,	0.5,
# new cell
	SPHERE,	43.1655,	35.4275,	33.204,	0.5,
# new cell
	SPHERE,	43.5474,	35.296,	33.3372,	0.5,
# new cell
	SPHERE,	43.9293,	35.1645,	33.4704,	0.5,
# new cell
	SPHERE,	44.3112,	35.033,	33.6036,	0.5,
# new cell
	SPHERE,	44.6931,	34.9015,	33.7368,	0.5,
# new cell
	SPHERE,	45.075,	34.77,	33.87,	0.5,
# new cell
	SPHERE,	41.9266,	36.055,	32.322,	0.5,
# new cell
	SPHERE,	42.3085,	35.9235,	32.4552,	0.5,
# new cell
	SPHERE,	42.6904,	35.792,	32.5884,	0.5,
# new cell
	SPHERE,	43.0723,	35.6605,	32.7216,	0.5,
# new cell
	SPHERE,	43.4542,	35.529,	32.8548,	0.5,
# new cell
	SPHERE,	43.8361,	35.3975,	32.988,	0.5,
# new cell
	SPHERE,	44.218,	35.266,	33.1212,	0.5,
# new cell
	SPHERE,	44.5999,	35.1345,	33.2544,	0.5,
# new cell
	SPHERE,	44.9818,	35.003,	33.3876,	0.5,
# new cell
	SPHERE,	45.3637,	34.8715,	33.5208,	0.5,
# new cell
	SPHERE,	42.5972,	36.025,	32.106,	0.5,
# new cell
	SPHERE,	42.9791,	35.8935,	32.2392,	0.5,
# new cell
	SPHERE,	43.361,	35.762,	32.3724,	0.5,
# new cell
	SPHERE,	43.7429,	35.6305,	32.5056,	0.5,
# new cell
	SPHERE,	44.1248,	35.499,	32.6388,	0.5,
# new cell
	SPHERE,	44.5067,	35.3675,	32.772,	0.5,
# new cell
	SPHERE,	44.8886,	35.236,	32.9052,	0.5,
# new cell
	SPHERE,	45.2705,	35.1045,	33.0384,	0.5,
# new cell
	SPHERE,	45.6524,	34.973,	33.1716,	0.5,
# new cell
	SPHERE,	43.2678,	35.995,	31.89,	0.5,
# new cell
	SPHERE,	43.6497,	35.8635,	32.0232,	0.5,
# new cell
	SPHERE,	44.0316,	35.732,	32.1564,	0.5,
# new cell
	SPHERE,	44.4135,	35.6005,	32.2896,	0.5,
# new cell
	SPHERE,	44.7954,	35.469,	32.4228,	0.5,
# new cell
	SPHERE,	45.1773,	35.3375,	32.556,	0.5,
# new cell
	SPHERE,	45.5592,	35.206,	32.6892,	0.5,
# new cell
	SPHERE,	45.9411,	35.0745,	32.8224,	0.5,
# new cell
	SPHERE,	43.9384,	35.965,	31.674,	0.5,
# new cell
	SPHERE,	44.3203,	35.8335,	31.8072,	0.5,
# new cell
	SPHERE,	44.7022,	35.702,	31.9404,	0.5,
# new cell
	SPHERE,	45.0841,	35.5705,	32.0736,	0.5,
# new cell
	SPHERE,	45.466,	35.439,	32.2068,	0.5,
# new cell
	SPHERE,	45.8479,	35.3075,	32.34,	0.5,
# new cell
	SPHERE,	46.2298,	35.176,	32.4732,	0.5,
# new cell
	SPHERE,	44.609,	35.935,	31.458,	0.5,
# new cell
	SPHERE,	44.9909,	35.8035,	31.5912,	0.5,
# new cell
	SPHERE,	45.3728,	35.672,	31.7244,	0.5,
# new cell
	SPHERE,	45.7547,	35.5405,	31.8576,	0.5,
# new cell
	SPHERE,	46.1366,	35.409,	31.9908,	0.5,
# new cell
	SPHERE,	46.5185,	35.2775,	32.124,	0.5,
# new cell
	SPHERE,	45.2796,	35.905,	31.242,	0.5,
# new cell
	SPHERE,	45.6615,	35.7735,	31.3752,	0.5,
# new cell
	SPHERE,	46.0434,	35.642,	31.5084,	0.5,
# new cell
	SPHERE,	46.4253,	35.5105,	31.6416,	0.5,
# new cell
	SPHERE,	46.8072,	35.379,	31.7748,	0.5,
# new cell
	SPHERE,	45.9502,	35.875,	31.026,	0.5,
# new cell
	SPHERE,	46.3321,	35.7435,	31.1592,	0.5,
# new cell
	SPHERE,	46.714,	35.612,	31.2924,	0.5,
# new cell
	SPHERE,	47.0959,	35.4805,	31.4256,	0.5,
# new cell
	SPHERE,	46.6208,	35.845,	30.81,	0.5,
# new cell
	SPHERE,	47.0027,	35.7135,	30.9432,	0.5,
# new cell
	SPHERE,	47.3846,	35.582,	31.0764,	0.5,
# new cell
	SPHERE,	47.2914,	35.815,	30.594,	0.5,
# new cell
	SPHERE,	47.6733,	35.6835,	30.7272,	0.5,
# new cell
	SPHERE,	47.962,	35.785,	30.378,	0.5,
# new cell
	SPHERE,	41.4698,	36.4394,	32.8211,	0.5,
# new cell
	SPHERE,	41.8517,	36.3079,	32.9543,	0.5,
# new cell
	SPHERE,	42.2336,	36.1764,	33.0875,	0.5,
# new cell
	SPHERE,	42.6155,	36.0449,	33.2207,	0.5,
# new cell
	SPHERE,	42.9974,	35.9134,	33.3539,	0.5,
# new cell
	SPHERE,	43.3793,	35.7819,	33.4871,	0.5,
# new cell
	SPHERE,	43.7612,	35.6504,	33.6203,	0.5,
# new cell
	SPHERE,	44.1431,	35.5189,	33.7535,	0.5,
# new cell
	SPHERE,	44.525,	35.3874,	33.8867,	0.5,
# new cell
	SPHERE,	44.9069,	35.2559,	34.0199,	0.5,
# new cell
	SPHERE,	42.1404,	36.4094,	32.6051,	0.5,
# new cell
	SPHERE,	42.5223,	36.2779,	32.7383,	0.5,
# new cell
	SPHERE,	42.9042,	36.1464,	32.8715,	0.5,
# new cell
	SPHERE,	43.2861,	36.0149,	33.0047,	0.5,
# new cell
	SPHERE,	43.668,	35.8834,	33.1379,	0.5,
# new cell
	SPHERE,	44.0499,	35.7519,	33.2711,	0.5,
# new cell
	SPHERE,	44.4318,	35.6204,	33.4043,	0.5,
# new cell
	SPHERE,	44.8137,	35.4889,	33.5375,	0.5,
# new cell
	SPHERE,	45.1956,	35.3574,	33.6707,	0.5,
# new cell
	SPHERE,	42.811,	36.3794,	32.3891,	0.5,
# new cell
	SPHERE,	43.1929,	36.2479,	32.5223,	0.5,
# new cell
	SPHERE,	43.5748,	36.1164,	32.6555,	0.5,
# new cell
	SPHERE,	43.9567,	35.9849,	32.7887,	0.5,
# new cell
	SPHERE,	44.3386,	35.8534,	32.9219,	0.5,
# new cell
	SPHERE,	44.7205,	35.7219,	33.0551,	0.5,
# new cell
	SPHERE,	45.1024,	35.5904,	33.1883,	0.5,
# new cell
	SPHERE,	45.4843,	35.4589,	33.3215,	0.5,
# new cell
	SPHERE,	43.4816,	36.3494,	32.1731,	0.5,
# new cell
	SPHERE,	43.8635,	36.2179,	32.3063,	0.5,
# new cell
	SPHERE,	44.2454,	36.0864,	32.4395,	0.5,
# new cell
	SPHERE,	44.6273,	35.9549,	32.5727,	0.5,
# new cell
	SPHERE,	45.0092,	35.8234,	32.7059,	0.5,
# new cell
	SPHERE,	45.3911,	35.6919,	32.8391,	0.5,
# new cell
	SPHERE,	45.773,	35.5604,	32.9723,	0.5,
# new cell
	SPHERE,	44.1522,	36.3194,	31.9571,	0.5,
# new cell
	SPHERE,	44.5341,	36.1879,	32.0903,	0.5,
# new cell
	SPHERE,	44.916,	36.0564,	32.2235,	0.5,
# new cell
	SPHERE,	45.2979,	35.9249,	32.3567,	0.5,
# new cell
	SPHERE,	45.6798,	35.7934,	32.4899,	0.5,
# new cell
	SPHERE,	46.0617,	35.6619,	32.6231,	0.5,
# new cell
	SPHERE,	44.8228,	36.2894,	31.7411,	0.5,
# new cell
	SPHERE,	45.2047,	36.1579,	31.8743,	0.5,
# new cell
	SPHERE,	45.5866,	36.0264,	32.0075,	0.5,
# new cell
	SPHERE,	45.9685,	35.8949,	32.1407,	0.5,
# new cell
	SPHERE,	46.3504,	35.7634,	32.2739,	0.5,
# new cell
	SPHERE,	45.4934,	36.2594,	31.5251,	0.5,
# new cell
	SPHERE,	45.8753,	36.1279,	31.6583,	0.5,
# new cell
	SPHERE,	46.2572,	35.9964,	31.7915,	0.5,
# new cell
	SPHERE,	46.6391,	35.8649,	31.9247,	0.5,
# new cell
	SPHERE,	46.164,	36.2294,	31.3091,	0.5,
# new cell
	SPHERE,	46.5459,	36.0979,	31.4423,	0.5,
# new cell
	SPHERE,	46.9278,	35.9664,	31.5755,	0.5,
# new cell
	SPHERE,	46.8346,	36.1994,	31.0931,	0.5,
# new cell
	SPHERE,	47.2165,	36.0679,	31.2263,	0.5,
# new cell
	SPHERE,	47.5052,	36.1694,	30.8771,	0.5,
# new cell
	SPHERE,	41.6836,	36.7938,	33.1042,	0.5,
# new cell
	SPHERE,	42.0655,	36.6623,	33.2374,	0.5,
# new cell
	SPHERE,	42.4474,	36.5308,	33.3706,	0.5,
# new cell
	SPHERE,	42.8293,	36.3993,	33.5038,	0.5,
# new cell
	SPHERE,	43.2112,	36.2678,	33.637,	0.5,
# new cell
	SPHERE,	43.5931,	36.1363,	33.7702,	0.5,
# new cell
	SPHERE,	43.975,	36.0048,	33.9034,	0.5,
# new cell
	SPHERE,	44.3569,	35.8733,	34.0366,	0.5,
# new cell
	SPHERE,	44.7388,	35.7418,	34.1698,	0.5,
# new cell
	SPHERE,	42.3542,	36.7638,	32.8882,	0.5,
# new cell
	SPHERE,	42.7361,	36.6323,	33.0214,	0.5,
# new cell
	SPHERE,	43.118,	36.5008,	33.1546,	0.5,
# new cell
	SPHERE,	43.4999,	36.3693,	33.2878,	0.5,
# new cell
	SPHERE,	43.8818,	36.2378,	33.421,	0.5,
# new cell
	SPHERE,	44.2637,	36.1063,	33.5542,	0.5,
# new cell
	SPHERE,	44.6456,	35.9748,	33.6874,	0.5,
# new cell
	SPHERE,	45.0275,	35.8433,	33.8206,	0.5,
# new cell
	SPHERE,	43.0248,	36.7338,	32.6722,	0.5,
# new cell
	SPHERE,	43.4067,	36.6023,	32.8054,	0.5,
# new cell
	SPHERE,	43.7886,	36.4708,	32.9386,	0.5,
# new cell
	SPHERE,	44.1705,	36.3393,	33.0718,	0.5,
# new cell
	SPHERE,	44.5524,	36.2078,	33.205,	0.5,
# new cell
	SPHERE,	44.9343,	36.0763,	33.3382,	0.5,
# new cell
	SPHERE,	45.3162,	35.9448,	33.4714,	0.5,
# new cell
	SPHERE,	43.6954,	36.7038,	32.4562,	0.5,
# new cell
	SPHERE,	44.0773,	36.5723,	32.5894,	0.5,
# new cell
	SPHERE,	44.4592,	36.4408,	32.7226,	0.5,
# new cell
	SPHERE,	44.8411,	36.3093,	32.8558,	0.5,
# new cell
	SPHERE,	45.223,	36.1778,	32.989,	0.5,
# new cell
	SPHERE,	45.6049,	36.0463,	33.1222,	0.5,
# new cell
	SPHERE,	44.366,	36.6738,	32.2402,	0.5,
# new cell
	SPHERE,	44.7479,	36.5423,	32.3734,	0.5,
# new cell
	SPHERE,	45.1298,	36.4108,	32.5066,	0.5,
# new cell
	SPHERE,	45.5117,	36.2793,	32.6398,	0.5,
# new cell
	SPHERE,	45.8936,	36.1478,	32.773,	0.5,
# new cell
	SPHERE,	45.0366,	36.6438,	32.0242,	0.5,
# new cell
	SPHERE,	45.4185,	36.5123,	32.1574,	0.5,
# new cell
	SPHERE,	45.8004,	36.3808,	32.2906,	0.5,
# new cell
	SPHERE,	46.1823,	36.2493,	32.4238,	0.5,
# new cell
	SPHERE,	45.7072,	36.6138,	31.8082,	0.5,
# new cell
	SPHERE,	46.0891,	36.4823,	31.9414,	0.5,
# new cell
	SPHERE,	46.471,	36.3508,	32.0746,	0.5,
# new cell
	SPHERE,	46.3778,	36.5838,	31.5922,	0.5,
# new cell
	SPHERE,	46.7597,	36.4523,	31.7254,	0.5,
# new cell
	SPHERE,	47.0484,	36.5538,	31.3762,	0.5,
# new cell
	SPHERE,	41.8974,	37.1482,	33.3873,	0.5,
# new cell
	SPHERE,	42.2793,	37.0167,	33.5205,	0.5,
# new cell
	SPHERE,	42.6612,	36.8852,	33.6537,	0.5,
# new cell
	SPHERE,	43.0431,	36.7537,	33.7869,	0.5,
# new cell
	SPHERE,	43.425,	36.6222,	33.9201,	0.5,
# new cell
	SPHERE,	43.8069,	36.4907,	34.0533,	0.5,
# new cell
	SPHERE,	44.1888,	36.3592,	34.1865,	0.5,
# new cell
	SPHERE,	44.5707,	36.2277,	34.3197,	0.5,
# new cell
	SPHERE,	42.568,	37.1182,	33.1713,	0.5,
# new cell
	SPHERE,	42.9499,	36.9867,	33.3045,	0.5,
# new cell
	SPHERE,	43.3318,	36.8552,	33.4377,	0.5,
# new cell
	SPHERE,	43.7137,	36.7237,	33.5709,	0.5,
# new cell
	SPHERE,	44.0956,	36.5922,	33.7041,	0.5,
# new cell
	SPHERE,	44.4775,	36.4607,	33.8373,	0.5,
# new cell
	SPHERE,	44.8594,	36.3292,	33.9705,	0.5,
# new cell
	SPHERE,	43.2386,	37.0882,	32.9553,	0.5,
# new cell
	SPHERE,	43.6205,	36.9567,	33.0885,	0.5,
# new cell
	SPHERE,	44.0024,	36.8252,	33.2217,	0.5,
# new cell
	SPHERE,	44.3843,	36.6937,	33.3549,	0.5,
# new cell
	SPHERE,	44.7662,	36.5622,	33.4881,	0.5,
# new cell
	SPHERE,	45.1481,	36.4307,	33.6213,	0.5,
# new cell
	SPHERE,	43.9092,	37.0582,	32.7393,	0.5,
# new cell
	SPHERE,	44.2911,	36.9267,	32.8725,	0.5,
# new cell
	SPHERE,	44.673,	36.7952,	33.0057,	0.5,
# new cell
	SPHERE,	45.0549,	36.6637,	33.1389,	0.5,
# new cell
	SPHERE,	45.4368,	36.5322,	33.2721,	0.5,
# new cell
	SPHERE,	44.5798,	37.0282,	32.5233,	0.5,
# new cell
	SPHERE,	44.9617,	36.8967,	32.6565,	0.5,
# new cell
	SPHERE,	45.3436,	36.7652,	32.7897,	0.5,
# new cell
	SPHERE,	45.7255,	36.6337,	32.9229,	0.5,
# new cell
	SPHERE,	45.2504,	36.9982,	32.3073,	0.5,
# new cell
	SPHERE,	45.6323,	36.8667,	32.4405,	0.5,
# new cell
	SPHERE,	46.0142,	36.7352,	32.5737,	0.5,
# new cell
	SPHERE,	45.921,	36.9682,	32.0913,	0.5,
# new cell
	SPHERE,	46.3029,	36.8367,	32.2245,	0.5,
# new cell
	SPHERE,	46.5916,	36.9382,	31.8753,	0.5,
# new cell
	SPHERE,	42.1112,	37.5026,	33.6704,	0.5,
# new cell
	SPHERE,	42.4931,	37.3711,	33.8036,	0.5,
# new cell
	SPHERE,	42.875,	37.2396,	33.9368,	0.5,
# new cell
	SPHERE,	43.2569,	37.1081,	34.07,	0.5,
# new cell
	SPHERE,	43.6388,	36.9766,	34.2032,	0.5,
# new cell
	SPHERE,	44.0207,	36.8451,	34.3364,	0.5,
# new cell
	SPHERE,	44.4026,	36.7136,	34.4696,	0.5,
# new cell
	SPHERE,	42.7818,	37.4726,	33.4544,	0.5,
# new cell
	SPHERE,	43.1637,	37.3411,	33.5876,	0.5,
# new cell
	SPHERE,	43.5456,	37.2096,	33.7208,	0.5,
# new cell
	SPHERE,	43.9275,	37.0781,	33.854,	0.5,
# new cell
	SPHERE,	44.3094,	36.9466,	33.9872,	0.5,
# new cell
	SPHERE,	44.6913,	36.8151,	34.1204,	0.5,
# new cell
	SPHERE,	43.4524,	37.4426,	33.2384,	0.5,
# new cell
	SPHERE,	43.8343,	37.3111,	33.3716,	0.5,
# new cell
	SPHERE,	44.2162,	37.1796,	33.5048,	0.5,
# new cell
	SPHERE,	44.5981,	37.0481,	33.638,	0.5,
# new cell
	SPHERE,	44.98,	36.9166,	33.7712,	0.5,
# new cell
	SPHERE,	44.123,	37.4126,	33.0224,	0.5,
# new cell
	SPHERE,	44.5049,	37.2811,	33.1556,	0.5,
# new cell
	SPHERE,	44.8868,	37.1496,	33.2888,	0.5,
# new cell
	SPHERE,	45.2687,	37.0181,	33.422,	0.5,
# new cell
	SPHERE,	44.7936,	37.3826,	32.8064,	0.5,
# new cell
	SPHERE,	45.1755,	37.2511,	32.9396,	0.5,
# new cell
	SPHERE,	45.5574,	37.1196,	33.0728,	0.5,
# new cell
	SPHERE,	45.4642,	37.3526,	32.5904,	0.5,
# new cell
	SPHERE,	45.8461,	37.2211,	32.7236,	0.5,
# new cell
	SPHERE,	46.1348,	37.3226,	32.3744,	0.5,
# new cell
	SPHERE,	42.325,	37.857,	33.9535,	0.5,
# new cell
	SPHERE,	42.7069,	37.7255,	34.0867,	0.5,
# new cell
	SPHERE,	43.0888,	37.594,	34.2199,	0.5,
# new cell
	SPHERE,	43.4707,	37.4625,	34.3531,	0.5,
# new cell
	SPHERE,	43.8526,	37.331,	34.4863,	0.5,
# new cell
	SPHERE,	44.2345,	37.1995,	34.6195,	0.5,
# new cell
	SPHERE,	42.9956,	37.827,	33.7375,	0.5,
# new cell
	SPHERE,	43.3775,	37.6955,	33.8707,	0.5,
# new cell
	SPHERE,	43.7594,	37.564,	34.0039,	0.5,
# new cell
	SPHERE,	44.1413,	37.4325,	34.1371,	0.5,
# new cell
	SPHERE,	44.5232,	37.301,	34.2703,	0.5,
# new cell
	SPHERE,	43.6662,	37.797,	33.5215,	0.5,
# new cell
	SPHERE,	44.0481,	37.6655,	33.6547,	0.5,
# new cell
	SPHERE,	44.43,	37.534,	33.7879,	0.5,
# new cell
	SPHERE,	44.8119,	37.4025,	33.9211,	0.5,
# new cell
	SPHERE,	44.3368,	37.767,	33.3055,	0.5,
# new cell
	SPHERE,	44.7187,	37.6355,	33.4387,	0.5,
# new cell
	SPHERE,	45.1006,	37.504,	33.5719,	0.5,
# new cell
	SPHERE,	45.0074,	37.737,	33.0895,	0.5,
# new cell
	SPHERE,	45.3893,	37.6055,	33.2227,	0.5,
# new cell
	SPHERE,	45.678,	37.707,	32.8735,	0.5,
# new cell
	SPHERE,	42.5388,	38.2114,	34.2366,	0.5,
# new cell
	SPHERE,	42.9207,	38.0799,	34.3698,	0.5,
# new cell
	SPHERE,	43.3026,	37.9484,	34.503,	0.5,
# new cell
	SPHERE,	43.6845,	37.8169,	34.6362,	0.5,
# new cell
	SPHERE,	44.0664,	37.6854,	34.7694,	0.5,
# new cell
	SPHERE,	43.2094,	38.1814,	34.0206,	0.5,
# new cell
	SPHERE,	43.5913,	38.0499,	34.1538,	0.5,
# new cell
	SPHERE,	43.9732,	37.9184,	34.287,	0.5,
# new cell
	SPHERE,	44.3551,	37.7869,	34.4202,	0.5,
# new cell
	SPHERE,	43.88,	38.1514,	33.8046,	0.5,
# new cell
	SPHERE,	44.2619,	38.0199,	33.9378,	0.5,
# new cell
	SPHERE,	44.6438,	37.8884,	34.071,	0.5,
# new cell
	SPHERE,	44.5506,	38.1214,	33.5886,	0.5,
# new cell
	SPHERE,	44.9325,	37.9899,	33.7218,	0.5,
# new cell
	SPHERE,	45.2212,	38.0914,	33.3726,	0.5,
# new cell
	SPHERE,	42.7526,	38.5658,	34.5197,	0.5,
# new cell
	SPHERE,	43.1345,	38.4343,	34.6529,	0.5,
# new cell
	SPHERE,	43.5164,	38.3028,	34.7861,	0.5,
# new cell
	SPHERE,	43.8983,	38.1713,	34.9193,	0.5,
# new cell
	SPHERE,	43.4232,	38.5358,	34.3037,	0.5,
# new cell
	SPHERE,	43.8051,	38.4043,	34.4369,	0.5,
# new cell
	SPHERE,	44.187,	38.2728,	34.5701,	0.5,
# new cell
	SPHERE,	44.0938,	38.5058,	34.0877,	0.5,
# new cell
	SPHERE,	44.4757,	38.3743,	34.2209,	0.5,
# new cell
	SPHERE,	44.7644,	38.4758,	33.8717,	0.5,
# new cell
	SPHERE,	42.9664,	38.9202,	34.8028,	0.5,
# new cell
	SPHERE,	43.3483,	38.7887,	34.936,	0.5,
# new cell
	SPHERE,	43.7302,	38.6572,	35.0692,	0.5,
# new cell
	SPHERE,	43.637,	38.8902,	34.5868,	0.5,
# new cell
	SPHERE,	44.0189,	38.7587,	34.72,	0.5,
# new cell
	SPHERE,	44.3076,	38.8602,	34.3708,	0.5,
# new cell
	SPHERE,	43.1802,	39.2746,	35.0859,	0.5,
# new cell
	SPHERE,	43.5621,	39.1431,	35.2191,	0.5,
# new cell
	SPHERE,	43.8508,	39.2446,	34.8699,	0.5,
# new cell
	SPHERE,	43.394,	39.629,	35.369,	0.5,
# new cell
	SPHERE,	41.256,	36.085,	32.538,	0.5,
# new cell
	SPHERE,	41.9266,	36.055,	32.322,	0.5,
# new cell
	SPHERE,	42.5972,	36.025,	32.106,	0.5,
# new cell
	SPHERE,	43.2678,	35.995,	31.89,	0.5,
# new cell
	SPHERE,	43.9384,	35.965,	31.674,	0.5,
# new cell
	SPHERE,	44.609,	35.935,	31.458,	0.5,
# new cell
	SPHERE,	45.2796,	35.905,	31.242,	0.5,
# new cell
	SPHERE,	45.9502,	35.875,	31.026,	0.5,
# new cell
	SPHERE,	46.6208,	35.845,	30.81,	0.5,
# new cell
	SPHERE,	47.2914,	35.815,	30.594,	0.5,
# new cell
	SPHERE,	47.962,	35.785,	30.378,	0.5,
# new cell
	SPHERE,	41.3602,	36.0992,	32.1491,	0.5,
# new cell
	SPHERE,	42.0308,	36.0692,	31.9331,	0.5,
# new cell
	SPHERE,	42.7014,	36.0392,	31.7171,	0.5,
# new cell
	SPHERE,	43.372,	36.0092,	31.5011,	0.5,
# new cell
	SPHERE,	44.0426,	35.9792,	31.2851,	0.5,
# new cell
	SPHERE,	44.7132,	35.9492,	31.0691,	0.5,
# new cell
	SPHERE,	45.3838,	35.9192,	30.8531,	0.5,
# new cell
	SPHERE,	46.0544,	35.8892,	30.6371,	0.5,
# new cell
	SPHERE,	46.725,	35.8592,	30.4211,	0.5,
# new cell
	SPHERE,	47.3956,	35.8292,	30.2051,	0.5,
# new cell
	SPHERE,	41.4644,	36.1134,	31.7602,	0.5,
# new cell
	SPHERE,	42.135,	36.0834,	31.5442,	0.5,
# new cell
	SPHERE,	42.8056,	36.0534,	31.3282,	0.5,
# new cell
	SPHERE,	43.4762,	36.0234,	31.1122,	0.5,
# new cell
	SPHERE,	44.1468,	35.9934,	30.8962,	0.5,
# new cell
	SPHERE,	44.8174,	35.9634,	30.6802,	0.5,
# new cell
	SPHERE,	45.488,	35.9334,	30.4642,	0.5,
# new cell
	SPHERE,	46.1586,	35.9034,	30.2482,	0.5,
# new cell
	SPHERE,	46.8292,	35.8734,	30.0322,	0.5,
# new cell
	SPHERE,	41.5686,	36.1276,	31.3713,	0.5,
# new cell
	SPHERE,	42.2392,	36.0976,	31.1553,	0.5,
# new cell
	SPHERE,	42.9098,	36.0676,	30.9393,	0.5,
# new cell
	SPHERE,	43.5804,	36.0376,	30.7233,	0.5,
# new cell
	SPHERE,	44.251,	36.0076,	30.5073,	0.5,
# new cell
	SPHERE,	44.9216,	35.9776,	30.2913,	0.5,
# new cell
	SPHERE,	45.5922,	35.9476,	30.0753,	0.5,
# new cell
	SPHERE,	46.2628,	35.9176,	29.8593,	0.5,
# new cell
	SPHERE,	41.6728,	36.1418,	30.9824,	0.5,
# new cell
	SPHERE,	42.3434,	36.1118,	30.7664,	0.5,
# new cell
	SPHERE,	43.014,	36.0818,	30.5504,	0.5,
# new cell
	SPHERE,	43.6846,	36.0518,	30.3344,	0.5,
# new cell
	SPHERE,	44.3552,	36.0218,	30.1184,	0.5,
# new cell
	SPHERE,	45.0258,	35.9918,	29.9024,	0.5,
# new cell
	SPHERE,	45.6964,	35.9618,	29.6864,	0.5,
# new cell
	SPHERE,	41.777,	36.156,	30.5935,	0.5,
# new cell
	SPHERE,	42.4476,	36.126,	30.3775,	0.5,
# new cell
	SPHERE,	43.1182,	36.096,	30.1615,	0.5,
# new cell
	SPHERE,	43.7888,	36.066,	29.9455,	0.5,
# new cell
	SPHERE,	44.4594,	36.036,	29.7295,	0.5,
# new cell
	SPHERE,	45.13,	36.006,	29.5135,	0.5,
# new cell
	SPHERE,	41.8812,	36.1702,	30.2046,	0.5,
# new cell
	SPHERE,	42.5518,	36.1402,	29.9886,	0.5,
# new cell
	SPHERE,	43.2224,	36.1102,	29.7726,	0.5,
# new cell
	SPHERE,	43.893,	36.0802,	29.5566,	0.5,
# new cell
	SPHERE,	44.5636,	36.0502,	29.3406,	0.5,
# new cell
	SPHERE,	41.9854,	36.1844,	29.8157,	0.5,
# new cell
	SPHERE,	42.656,	36.1544,	29.5997,	0.5,
# new cell
	SPHERE,	43.3266,	36.1244,	29.3837,	0.5,
# new cell
	SPHERE,	43.9972,	36.0944,	29.1677,	0.5,
# new cell
	SPHERE,	42.0896,	36.1986,	29.4268,	0.5,
# new cell
	SPHERE,	42.7602,	36.1686,	29.2108,	0.5,
# new cell
	SPHERE,	43.4308,	36.1386,	28.9948,	0.5,
# new cell
	SPHERE,	42.1938,	36.2128,	29.0379,	0.5,
# new cell
	SPHERE,	42.8644,	36.1828,	28.8219,	0.5,
# new cell
	SPHERE,	42.298,	36.227,	28.649,	0.5,
# new cell
	SPHERE,	41.4698,	36.4394,	32.8211,	0.5,
# new cell
	SPHERE,	42.1404,	36.4094,	32.6051,	0.5,
# new cell
	SPHERE,	42.811,	36.3794,	32.3891,	0.5,
# new cell
	SPHERE,	43.4816,	36.3494,	32.1731,	0.5,
# new cell
	SPHERE,	44.1522,	36.3194,	31.9571,	0.5,
# new cell
	SPHERE,	44.8228,	36.2894,	31.7411,	0.5,
# new cell
	SPHERE,	45.4934,	36.2594,	31.5251,	0.5,
# new cell
	SPHERE,	46.164,	36.2294,	31.3091,	0.5,
# new cell
	SPHERE,	46.8346,	36.1994,	31.0931,	0.5,
# new cell
	SPHERE,	47.5052,	36.1694,	30.8771,	0.5,
# new cell
	SPHERE,	41.574,	36.4536,	32.4322,	0.5,
# new cell
	SPHERE,	42.2446,	36.4236,	32.2162,	0.5,
# new cell
	SPHERE,	42.9152,	36.3936,	32.0002,	0.5,
# new cell
	SPHERE,	43.5858,	36.3636,	31.7842,	0.5,
# new cell
	SPHERE,	44.2564,	36.3336,	31.5682,	0.5,
# new cell
	SPHERE,	44.927,	36.3036,	31.3522,	0.5,
# new cell
	SPHERE,	45.5976,	36.2736,	31.1362,	0.5,
# new cell
	SPHERE,	46.2682,	36.2436,	30.9202,	0.5,
# new cell
	SPHERE,	46.9388,	36.2136,	30.7042,	0.5,
# new cell
	SPHERE,	41.6782,	36.4678,	32.0433,	0.5,
# new cell
	SPHERE,	42.3488,	36.4378,	31.8273,	0.5,
# new cell
	SPHERE,	43.0194,	36.4078,	31.6113,	0.5,
# new cell
	SPHERE,	43.69,	36.3778,	31.3953,	0.5,
# new cell
	SPHERE,	44.3606,	36.3478,	31.1793,	0.5,
# new cell
	SPHERE,	45.0312,	36.3178,	30.9633,	0.5,
# new cell
	SPHERE,	45.7018,	36.2878,	30.7473,	0.5,
# new cell
	SPHERE,	46.3724,	36.2578,	30.5313,	0.5,
# new cell
	SPHERE,	41.7824,	36.482,	31.6544,	0.5,
# new cell
	SPHERE,	42.453,	36.452,	31.4384,	0.5,
# new cell
	SPHERE,	43.1236,	36.422,	31.2224,	0.5,
# new cell
	SPHERE,	43.7942,	36.392,	31.0064,	0.5,
# new cell
	SPHERE,	44.4648,	36.362,	30.7904,	0.5,
# new cell
	SPHERE,	45.1354,	36.332,	30.5744,	0.5,
# new cell
	SPHERE,	45.806,	36.302,	30.3584,	0.5,
# new cell
	SPHERE,	41.8866,	36.4962,	31.2655,	0.5,
# new cell
	SPHERE,	42.5572,	36.4662,	31.0495,	0.5,
# new cell
	SPHERE,	43.2278,	36.4362,	30.8335,	0.5,
# new cell
	SPHERE,	43.8984,	36.4062,	30.6175,	0.5,
# new cell
	SPHERE,	44.569,	36.3762,	30.4015,	0.5,
# new cell
	SPHERE,	45.2396,	36.3462,	30.1855,	0.5,
# new cell
	SPHERE,	41.9908,	36.5104,	30.8766,	0.5,
# new cell
	SPHERE,	42.6614,	36.4804,	30.6606,	0.5,
# new cell
	SPHERE,	43.332,	36.4504,	30.4446,	0.5,
# new cell
	SPHERE,	44.0026,	36.4204,	30.2286,	0.5,
# new cell
	SPHERE,	44.6732,	36.3904,	30.0126,	0.5,
# new cell
	SPHERE,	42.095,	36.5246,	30.4877,	0.5,
# new cell
	SPHERE,	42.7656,	36.4946,	30.2717,	0.5,
# new cell
	SPHERE,	43.4362,	36.4646,	30.0557,	0.5,
# new cell
	SPHERE,	44.1068,	36.4346,	29.8397,	0.5,
# new cell
	SPHERE,	42.1992,	36.5388,	30.0988,	0.5,
# new cell
	SPHERE,	42.8698,	36.5088,	29.8828,	0.5,
# new cell
	SPHERE,	43.5404,	36.4788,	29.6668,	0.5,
# new cell
	SPHERE,	42.3034,	36.553,	29.7099,	0.5,
# new cell
	SPHERE,	42.974,	36.523,	29.4939,	0.5,
# new cell
	SPHERE,	42.4076,	36.5672,	29.321,	0.5,
# new cell
	SPHERE,	41.6836,	36.7938,	33.1042,	0.5,
# new cell
	SPHERE,	42.3542,	36.7638,	32.8882,	0.5,
# new cell
	SPHERE,	43.0248,	36.7338,	32.6722,	0.5,
# new cell
	SPHERE,	43.6954,	36.7038,	32.4562,	0.5,
# new cell
	SPHERE,	44.366,	36.6738,	32.2402,	0.5,
# new cell
	SPHERE,	45.0366,	36.6438,	32.0242,	0.5,
# new cell
	SPHERE,	45.7072,	36.6138,	31.8082,	0.5,
# new cell
	SPHERE,	46.3778,	36.5838,	31.5922,	0.5,
# new cell
	SPHERE,	47.0484,	36.5538,	31.3762,	0.5,
# new cell
	SPHERE,	41.7878,	36.808,	32.7153,	0.5,
# new cell
	SPHERE,	42.4584,	36.778,	32.4993,	0.5,
# new cell
	SPHERE,	43.129,	36.748,	32.2833,	0.5,
# new cell
	SPHERE,	43.7996,	36.718,	32.0673,	0.5,
# new cell
	SPHERE,	44.4702,	36.688,	31.8513,	0.5,
# new cell
	SPHERE,	45.1408,	36.658,	31.6353,	0.5,
# new cell
	SPHERE,	45.8114,	36.628,	31.4193,	0.5,
# new cell
	SPHERE,	46.482,	36.598,	31.2033,	0.5,
# new cell
	SPHERE,	41.892,	36.8222,	32.3264,	0.5,
# new cell
	SPHERE,	42.5626,	36.7922,	32.1104,	0.5,
# new cell
	SPHERE,	43.2332,	36.7622,	31.8944,	0.5,
# new cell
	SPHERE,	43.9038,	36.7322,	31.6784,	0.5,
# new cell
	SPHERE,	44.5744,	36.7022,	31.4624,	0.5,
# new cell
	SPHERE,	45.245,	36.6722,	31.2464,	0.5,
# new cell
	SPHERE,	45.9156,	36.6422,	31.0304,	0.5,
# new cell
	SPHERE,	41.9962,	36.8364,	31.9375,	0.5,
# new cell
	SPHERE,	42.6668,	36.8064,	31.7215,	0.5,
# new cell
	SPHERE,	43.3374,	36.7764,	31.5055,	0.5,
# new cell
	SPHERE,	44.008,	36.7464,	31.2895,	0.5,
# new cell
	SPHERE,	44.6786,	36.7164,	31.0735,	0.5,
# new cell
	SPHERE,	45.3492,	36.6864,	30.8575,	0.5,
# new cell
	SPHERE,	42.1004,	36.8506,	31.5486,	0.5,
# new cell
	SPHERE,	42.771,	36.8206,	31.3326,	0.5,
# new cell
	SPHERE,	43.4416,	36.7906,	31.1166,	0.5,
# new cell
	SPHERE,	44.1122,	36.7606,	30.9006,	0.5,
# new cell
	SPHERE,	44.7828,	36.7306,	30.6846,	0.5,
# new cell
	SPHERE,	42.2046,	36.8648,	31.1597,	0.5,
# new cell
	SPHERE,	42.8752,	36.8348,	30.9437,	0.5,
# new cell
	SPHERE,	43.5458,	36.8048,	30.7277,	0.5,
# new cell
	SPHERE,	44.2164,	36.7748,	30.5117,	0.5,
# new cell
	SPHERE,	42.3088,	36.879,	30.7708,	0.5,
# new cell
	SPHERE,	42.9794,	36.849,	30.5548,	0.5,
# new cell
	SPHERE,	43.65,	36.819,	30.3388,	0.5,
# new cell
	SPHERE,	42.413,	36.8932,	30.3819,	0.5,
# new cell
	SPHERE,	43.0836,	36.8632,	30.1659,	0.5,
# new cell
	SPHERE,	42.5172,	36.9074,	29.993,	0.5,
# new cell
	SPHERE,	41.8974,	37.1482,	33.3873,	0.5,
# new cell
	SPHERE,	42.568,	37.1182,	33.1713,	0.5,
# new cell
	SPHERE,	43.2386,	37.0882,	32.9553,	0.5,
# new cell
	SPHERE,	43.9092,	37.0582,	32.7393,	0.5,
# new cell
	SPHERE,	44.5798,	37.0282,	32.5233,	0.5,
# new cell
	SPHERE,	45.2504,	36.9982,	32.3073,	0.5,
# new cell
	SPHERE,	45.921,	36.9682,	32.0913,	0.5,
# new cell
	SPHERE,	46.5916,	36.9382,	31.8753,	0.5,
# new cell
	SPHERE,	42.0016,	37.1624,	32.9984,	0.5,
# new cell
	SPHERE,	42.6722,	37.1324,	32.7824,	0.5,
# new cell
	SPHERE,	43.3428,	37.1024,	32.5664,	0.5,
# new cell
	SPHERE,	44.0134,	37.0724,	32.3504,	0.5,
# new cell
	SPHERE,	44.684,	37.0424,	32.1344,	0.5,
# new cell
	SPHERE,	45.3546,	37.0124,	31.9184,	0.5,
# new cell
	SPHERE,	46.0252,	36.9824,	31.7024,	0.5,
# new cell
	SPHERE,	42.1058,	37.1766,	32.6095,	0.5,
# new cell
	SPHERE,	42.7764,	37.1466,	32.3935,	0.5,
# new cell
	SPHERE,	43.447,	37.1166,	32.1775,	0.5,
# new cell
	SPHERE,	44.1176,	37.0866,	31.9615,	0.5,
# new cell
	SPHERE,	44.7882,	37.0566,	31.7455,	0.5,
# new cell
	SPHERE,	45.4588,	37.0266,	31.5295,	0.5,
# new cell
	SPHERE,	42.21,	37.1908,	32.2206,	0.5,
# new cell
	SPHERE,	42.8806,	37.1608,	32.0046,	0.5,
# new cell
	SPHERE,	43.5512,	37.1308,	31.7886,	0.5,
# new cell
	SPHERE,	44.2218,	37.1008,	31.5726,	0.5,
# new cell
	SPHERE,	44.8924,	37.0708,	31.3566,	0.5,
# new cell
	SPHERE,	42.3142,	37.205,	31.8317,	0.5,
# new cell
	SPHERE,	42.9848,	37.175,	31.6157,	0.5,
# new cell
	SPHERE,	43.6554,	37.145,	31.3997,	0.5,
# new cell
	SPHERE,	44.326,	37.115,	31.1837,	0.5,
# new cell
	SPHERE,	42.4184,	37.2192,	31.4428,	0.5,
# new cell
	SPHERE,	43.089,	37.1892,	31.2268,	0.5,
# new cell
	SPHERE,	43.7596,	37.1592,	31.0108,	0.5,
# new cell
	SPHERE,	42.5226,	37.2334,	31.0539,	0.5,
# new cell
	SPHERE,	43.1932,	37.2034,	30.8379,	0.5,
# new cell
	SPHERE,	42.6268,	37.2476,	30.665,	0.5,
# new cell
	SPHERE,	42.1112,	37.5026,	33.6704,	0.5,
# new cell
	SPHERE,	42.7818,	37.4726,	33.4544,	0.5,
# new cell
	SPHERE,	43.4524,	37.4426,	33.2384,	0.5,
# new cell
	SPHERE,	44.123,	37.4126,	33.0224,	0.5,
# new cell
	SPHERE,	44.7936,	37.3826,	32.8064,	0.5,
# new cell
	SPHERE,	45.4642,	37.3526,	32.5904,	0.5,
# new cell
	SPHERE,	46.1348,	37.3226,	32.3744,	0.5,
# new cell
	SPHERE,	42.2154,	37.5168,	33.2815,	0.5,
# new cell
	SPHERE,	42.886,	37.4868,	33.0655,	0.5,
# new cell
	SPHERE,	43.5566,	37.4568,	32.8495,	0.5,
# new cell
	SPHERE,	44.2272,	37.4268,	32.6335,	0.5,
# new cell
	SPHERE,	44.8978,	37.3968,	32.4175,	0.5,
# new cell
	SPHERE,	45.5684,	37.3668,	32.2015,	0.5,
# new cell
	SPHERE,	42.3196,	37.531,	32.8926,	0.5,
# new cell
	SPHERE,	42.9902,	37.501,	32.6766,	0.5,
# new cell
	SPHERE,	43.6608,	37.471,	32.4606,	0.5,
# new cell
	SPHERE,	44.3314,	37.441,	32.2446,	0.5,
# new cell
	SPHERE,	45.002,	37.411,	32.0286,	0.5,
# new cell
	SPHERE,	42.4238,	37.5452,	32.5037,	0.5,
# new cell
	SPHERE,	43.0944,	37.5152,	32.2877,	0.5,
# new cell
	SPHERE,	43.765,	37.4852,	32.0717,	0.5,
# new cell
	SPHERE,	44.4356,	37.4552,	31.8557,	0.5,
# new cell
	SPHERE,	42.528,	37.5594,	32.1148,	0.5,
# new cell
	SPHERE,	43.1986,	37.5294,	31.8988,	0.5,
# new cell
	SPHERE,	43.8692,	37.4994,	31.6828,	0.5,
# new cell
	SPHERE,	42.6322,	37.5736,	31.7259,	0.5,
# new cell
	SPHERE,	43.3028,	37.5436,	31.5099,	0.5,
# new cell
	SPHERE,	42.7364,	37.5878,	31.337,	0.5,
# new cell
	SPHERE,	42.325,	37.857,	33.9535,	0.5,
# new cell
	SPHERE,	42.9956,	37.827,	33.7375,	0.5,
# new cell
	SPHERE,	43.6662,	37.797,	33.5215,	0.5,
# new cell
	SPHERE,	44.3368,	37.767,	33.3055,	0.5,
# new cell
	SPHERE,	45.0074,	37.737,	33.0895,	0.5,
# new cell
	SPHERE,	45.678,	37.707,	32.8735,	0.5,
# new cell
	SPHERE,	42.4292,	37.8712,	33.5646,	0.5,
# new cell
	SPHERE,	43.0998,	37.8412,	33.3486,	0.5,
# new cell
	SPHERE,	43.7704,	37.8112,	33.1326,	0.5,
# new cell
	SPHERE,	44.441,	37.7812,	32.9166,	0.5,
# new cell
	SPHERE,	45.1116,	37.7512,	32.7006,	0.5,
# new cell
	SPHERE,	42.5334,	37.8854,	33.1757,	0.5,
# new cell
	SPHERE,	43.204,	37.8554,	32.9597,	0.5,
# new cell
	SPHERE,	43.8746,	37.8254,	32.7437,	0.5,
# new cell
	SPHERE,	44.5452,	37.7954,	32.5277,	0.5,
# new cell
	SPHERE,	42.6376,	37.8996,	32.7868,	0.5,
# new cell
	SPHERE,	43.3082,	37.8696,	32.5708,	0.5,
# new cell
	SPHERE,	43.9788,	37.8396,	32.3548,	0.5,
# new cell
	SPHERE,	42.7418,	37.9138,	32.3979,	0.5,
# new cell
	SPHERE,	43.4124,	37.8838,	32.1819,	0.5,
# new cell
	SPHERE,	42.846,	37.928,	32.009,	0.5,
# new cell
	SPHERE,	42.5388,	38.2114,	34.2366,	0.5,
# new cell
	SPHERE,	43.2094,	38.1814,	34.0206,	0.5,
# new cell
	SPHERE,	43.88,	38.1514,	33.8046,	0.5,
# new cell
	SPHERE,	44.5506,	38.1214,	33.5886,	0.5,
# new cell
	SPHERE,	45.2212,	38.0914,	33.3726,	0.5,
# new cell
	SPHERE,	42.643,	38.2256,	33.8477,	0.5,
# new cell
	SPHERE,	43.3136,	38.1956,	33.6317,	0.5,
# new cell
	SPHERE,	43.9842,	38.1656,	33.4157,	0.5,
# new cell
	SPHERE,	44.6548,	38.1356,	33.1997,	0.5,
# new cell
	SPHERE,	42.7472,	38.2398,	33.4588,	0.5,
# new cell
	SPHERE,	43.4178,	38.2098,	33.2428,	0.5,
# new cell
	SPHERE,	44.0884,	38.1798,	33.0268,	0.5,
# new cell
	SPHERE,	42.8514,	38.254,	33.0699,	0.5,
# new cell
	SPHERE,	43.522,	38.224,	32.8539,	0.5,
# new cell
	SPHERE,	42.9556,	38.2682,	32.681,	0.5,
# new cell
	SPHERE,	42.7526,	38.5658,	34.5197,	0.5,
# new cell
	SPHERE,	43.4232,	38.5358,	34.3037,	0.5,
# new cell
	SPHERE,	44.0938,	38.5058,	34.0877,	0.5,
# new cell
	SPHERE,	44.7644,	38.4758,	33.8717,	0.5,
# new cell
	SPHERE,	42.8568,	38.58,	34.1308,	0.5,
# new cell
	SPHERE,	43.5274,	38.55,	33.9148,	0.5,
# new cell
	SPHERE,	44.198,	38.52,	33.6988,	0.5,
# new cell
	SPHERE,	42.961,	38.5942,	33.7419,	0.5,
# new cell
	SPHERE,	43.6316,	38.5642,	33.5259,	0.5,
# new cell
	SPHERE,	43.0652,	38.6084,	33.353,	0.5,
# new cell
	SPHERE,	42.9664,	38.9202,	34.8028,	0.5,
# new cell
	SPHERE,	43.637,	38.8902,	34.5868,	0.5,
# new cell
	SPHERE,	44.3076,	38.8602,	34.3708,	0.5,
# new cell
	SPHERE,	43.0706,	38.9344,	34.4139,	0.5,
# new cell
	SPHERE,	43.7412,	38.9044,	34.1979,	0.5,
# new cell
	SPHERE,	43.1748,	38.9486,	34.025,	0.5,
# new cell
	SPHERE,	43.1802,	39.2746,	35.0859,	0.5,
# new cell
	SPHERE,	43.8508,	39.2446,	34.8699,	0.5,
# new cell
	SPHERE,	43.2844,	39.2888,	34.697,	0.5,
# new cell
	SPHERE,	43.394,	39.629,	35.369,	0.5,
	]
cmd.load_cgo(tes_null_1, 'tes_null_1',   1)
tes_null__border_1 = [
	COLOR,  1,	0,	0,
	LINEWIDTH, 1.0,
	BEGIN, LINES,
# new polyhedron
# new facet 1/2
	VERTEX,	42.832,	47.967,	33.199,	
# new facet 1/2
	VERTEX,	45.909,	43.202,	26.324,	
# new facet 1/2
	VERTEX,	41.136,	44.752,	35.135,	
# new facet 2/2
	VERTEX,	42.832,	47.967,	33.199,	
# new facet 2/2
	VERTEX,	45.909,	43.202,	26.324,	
# new facet 2/2
	VERTEX,	41.136,	44.752,	35.135,	
# new facet 1/2
	VERTEX,	39.1965,	43.907,	31.5366,	
# new facet 1/2
	VERTEX,	42.832,	47.967,	33.199,	
# new facet 1/2
	VERTEX,	41.136,	44.752,	35.135,	
# new facet 2/2
	VERTEX,	39.1965,	43.907,	31.5366,	
# new facet 2/2
	VERTEX,	42.832,	47.967,	33.199,	
# new facet 2/2
	VERTEX,	41.136,	44.752,	35.135,	
# new facet 1/2
	VERTEX,	39.1965,	43.907,	31.5366,	
# new facet 1/2
	VERTEX,	45.909,	43.202,	26.324,	
# new facet 1/2
	VERTEX,	42.832,	47.967,	33.199,	
# new facet 2/2
	VERTEX,	39.1965,	43.907,	31.5366,	
# new facet 2/2
	VERTEX,	45.909,	43.202,	26.324,	
# new facet 2/2
	VERTEX,	42.832,	47.967,	33.199,	
# new facet 1/2
	VERTEX,	39.1965,	43.907,	31.5366,	
# new facet 1/2
	VERTEX,	41.136,	44.752,	35.135,	
# new facet 1/2
	VERTEX,	45.909,	43.202,	26.324,	
# new facet 2/2
	VERTEX,	39.1965,	43.907,	31.5366,	
# new facet 2/2
	VERTEX,	41.136,	44.752,	35.135,	
# new facet 2/2
	VERTEX,	45.909,	43.202,	26.324,	
# new facet 1/2
	VERTEX,	42.832,	47.967,	33.199,	
# new facet 1/2
	VERTEX,	41.136,	44.752,	35.135,	
# new facet 1/2
	VERTEX,	39.1965,	43.907,	31.5366,	
# new facet 2/2
	VERTEX,	42.832,	47.967,	33.199,	
# new facet 2/2
	VERTEX,	41.136,	44.752,	35.135,	
# new facet 2/2
	VERTEX,	39.1965,	43.907,	31.5366,	
# new facet 1/2
	VERTEX,	40.8268,	43.3601,	29.905,	
# new facet 1/2
	VERTEX,	42.832,	47.967,	33.199,	
# new facet 1/2
	VERTEX,	39.1965,	43.907,	31.5366,	
# new facet 2/2
	VERTEX,	40.8268,	43.3601,	29.905,	
# new facet 2/2
	VERTEX,	42.832,	47.967,	33.199,	
# new facet 2/2
	VERTEX,	39.1965,	43.907,	31.5366,	
# new facet 1/2
	VERTEX,	40.8268,	43.3601,	29.905,	
# new facet 1/2
	VERTEX,	41.136,	44.752,	35.135,	
# new facet 1/2
	VERTEX,	42.832,	47.967,	33.199,	
# new facet 2/2
	VERTEX,	40.8268,	43.3601,	29.905,	
# new facet 2/2
	VERTEX,	41.136,	44.752,	35.135,	
# new facet 2/2
	VERTEX,	42.832,	47.967,	33.199,	
# new facet 1/2
	VERTEX,	40.8268,	43.3601,	29.905,	
# new facet 1/2
	VERTEX,	39.1965,	43.907,	31.5366,	
# new facet 1/2
	VERTEX,	41.136,	44.752,	35.135,	
# new facet 2/2
	VERTEX,	40.8268,	43.3601,	29.905,	
# new facet 2/2
	VERTEX,	39.1965,	43.907,	31.5366,	
# new facet 2/2
	VERTEX,	41.136,	44.752,	35.135,	
# new facet 1/2
	VERTEX,	41.136,	44.752,	35.135,	
# new facet 1/2
	VERTEX,	39.1965,	43.907,	31.5366,	
# new facet 1/2
	VERTEX,	40.8268,	43.3601,	29.905,	
# new facet 2/2
	VERTEX,	41.136,	44.752,	35.135,	
# new facet 2/2
	VERTEX,	39.1965,	43.907,	31.5366,	
# new facet 2/2
	VERTEX,	40.8268,	43.3601,	29.905,	
# new facet 1/2
	VERTEX,	38.9226,	43.516,	31.5881,	
# new facet 1/2
	VERTEX,	41.136,	44.752,	35.135,	
# new facet 1/2
	VERTEX,	40.8268,	43.3601,	29.905,	
# new facet 2/2
	VERTEX,	38.9226,	43.516,	31.5881,	
# new facet 2/2
	VERTEX,	41.136,	44.752,	35.135,	
# new facet 2/2
	VERTEX,	40.8268,	43.3601,	29.905,	
# new facet 1/2
	VERTEX,	38.9226,	43.516,	31.5881,	
# new facet 1/2
	VERTEX,	39.1965,	43.907,	31.5366,	
# new facet 1/2
	VERTEX,	41.136,	44.752,	35.135,	
# new facet 2/2
	VERTEX,	38.9226,	43.516,	31.5881,	
# new facet 2/2
	VERTEX,	39.1965,	43.907,	31.5366,	
# new facet 2/2
	VERTEX,	41.136,	44.752,	35.135,	
# new facet 1/2
	VERTEX,	38.9226,	43.516,	31.5881,	
# new facet 1/2
	VERTEX,	40.8268,	43.3601,	29.905,	
# new facet 1/2
	VERTEX,	39.1965,	43.907,	31.5366,	
# new facet 2/2
	VERTEX,	38.9226,	43.516,	31.5881,	
# new facet 2/2
	VERTEX,	40.8268,	43.3601,	29.905,	
# new facet 2/2
	VERTEX,	39.1965,	43.907,	31.5366,	
# new polyhedron
# new facet 1/2
	VERTEX,	46.783,	46.545,	37.098,	
# new facet 1/2
	VERTEX,	47.6744,	46.7204,	37.8114,	
# new facet 1/2
	VERTEX,	51.679,	44.1328,	33.6188,	
# new facet 2/2
	VERTEX,	46.783,	46.545,	37.098,	
# new facet 2/2
	VERTEX,	47.6744,	46.7204,	37.8114,	
# new facet 2/2
	VERTEX,	51.679,	44.1328,	33.6188,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 1/2
	VERTEX,	46.783,	46.545,	37.098,	
# new facet 1/2
	VERTEX,	51.679,	44.1328,	33.6188,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 2/2
	VERTEX,	46.783,	46.545,	37.098,	
# new facet 2/2
	VERTEX,	51.679,	44.1328,	33.6188,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 1/2
	VERTEX,	47.6744,	46.7204,	37.8114,	
# new facet 1/2
	VERTEX,	46.783,	46.545,	37.098,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 2/2
	VERTEX,	47.6744,	46.7204,	37.8114,	
# new facet 2/2
	VERTEX,	46.783,	46.545,	37.098,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 1/2
	VERTEX,	51.679,	44.1328,	33.6188,	
# new facet 1/2
	VERTEX,	47.6744,	46.7204,	37.8114,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 2/2
	VERTEX,	51.679,	44.1328,	33.6188,	
# new facet 2/2
	VERTEX,	47.6744,	46.7204,	37.8114,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 1/2
	VERTEX,	47.6744,	46.7204,	37.8114,	
# new facet 1/2
	VERTEX,	51.679,	44.1328,	33.6188,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 2/2
	VERTEX,	47.6744,	46.7204,	37.8114,	
# new facet 2/2
	VERTEX,	51.679,	44.1328,	33.6188,	
# new facet 1/2
	VERTEX,	48.7247,	46.9437,	38.0656,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 1/2
	VERTEX,	51.679,	44.1328,	33.6188,	
# new facet 2/2
	VERTEX,	48.7247,	46.9437,	38.0656,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 2/2
	VERTEX,	51.679,	44.1328,	33.6188,	
# new facet 1/2
	VERTEX,	48.7247,	46.9437,	38.0656,	
# new facet 1/2
	VERTEX,	47.6744,	46.7204,	37.8114,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 2/2
	VERTEX,	48.7247,	46.9437,	38.0656,	
# new facet 2/2
	VERTEX,	47.6744,	46.7204,	37.8114,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 1/2
	VERTEX,	48.7247,	46.9437,	38.0656,	
# new facet 1/2
	VERTEX,	51.679,	44.1328,	33.6188,	
# new facet 1/2
	VERTEX,	47.6744,	46.7204,	37.8114,	
# new facet 2/2
	VERTEX,	48.7247,	46.9437,	38.0656,	
# new facet 2/2
	VERTEX,	51.679,	44.1328,	33.6188,	
# new facet 2/2
	VERTEX,	47.6744,	46.7204,	37.8114,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 1/2
	VERTEX,	51.679,	44.1328,	33.6188,	
# new facet 1/2
	VERTEX,	48.7247,	46.9437,	38.0656,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 2/2
	VERTEX,	51.679,	44.1328,	33.6188,	
# new facet 2/2
	VERTEX,	48.7247,	46.9437,	38.0656,	
# new facet 1/2
	VERTEX,	52.7496,	47.3851,	31.6175,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 1/2
	VERTEX,	48.7247,	46.9437,	38.0656,	
# new facet 2/2
	VERTEX,	52.7496,	47.3851,	31.6175,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 2/2
	VERTEX,	48.7247,	46.9437,	38.0656,	
# new facet 1/2
	VERTEX,	52.7496,	47.3851,	31.6175,	
# new facet 1/2
	VERTEX,	51.679,	44.1328,	33.6188,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 2/2
	VERTEX,	52.7496,	47.3851,	31.6175,	
# new facet 2/2
	VERTEX,	51.679,	44.1328,	33.6188,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 1/2
	VERTEX,	52.7496,	47.3851,	31.6175,	
# new facet 1/2
	VERTEX,	48.7247,	46.9437,	38.0656,	
# new facet 1/2
	VERTEX,	51.679,	44.1328,	33.6188,	
# new facet 2/2
	VERTEX,	52.7496,	47.3851,	31.6175,	
# new facet 2/2
	VERTEX,	48.7247,	46.9437,	38.0656,	
# new facet 2/2
	VERTEX,	51.679,	44.1328,	33.6188,	
# new polyhedron
# new facet 1/2
	VERTEX,	50.075,	45.976,	26.599,	
# new facet 1/2
	VERTEX,	47.454,	44.623,	26.246,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 2/2
	VERTEX,	50.075,	45.976,	26.599,	
# new facet 2/2
	VERTEX,	47.454,	44.623,	26.246,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 1/2
	VERTEX,	52.3329,	41.6999,	31.6875,	
# new facet 1/2
	VERTEX,	50.075,	45.976,	26.599,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 2/2
	VERTEX,	52.3329,	41.6999,	31.6875,	
# new facet 2/2
	VERTEX,	50.075,	45.976,	26.599,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 1/2
	VERTEX,	52.3329,	41.6999,	31.6875,	
# new facet 1/2
	VERTEX,	47.454,	44.623,	26.246,	
# new facet 1/2
	VERTEX,	50.075,	45.976,	26.599,	
# new facet 2/2
	VERTEX,	52.3329,	41.6999,	31.6875,	
# new facet 2/2
	VERTEX,	47.454,	44.623,	26.246,	
# new facet 2/2
	VERTEX,	50.075,	45.976,	26.599,	
# new facet 1/2
	VERTEX,	52.3329,	41.6999,	31.6875,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 1/2
	VERTEX,	47.454,	44.623,	26.246,	
# new facet 2/2
	VERTEX,	52.3329,	41.6999,	31.6875,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 2/2
	VERTEX,	47.454,	44.623,	26.246,	
# new facet 1/2
	VERTEX,	50.075,	45.976,	26.599,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 1/2
	VERTEX,	52.3329,	41.6999,	31.6875,	
# new facet 2/2
	VERTEX,	50.075,	45.976,	26.599,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 2/2
	VERTEX,	52.3329,	41.6999,	31.6875,	
# new facet 1/2
	VERTEX,	52.335,	41.6976,	31.7035,	
# new facet 1/2
	VERTEX,	50.075,	45.976,	26.599,	
# new facet 1/2
	VERTEX,	52.3329,	41.6999,	31.6875,	
# new facet 2/2
	VERTEX,	52.335,	41.6976,	31.7035,	
# new facet 2/2
	VERTEX,	50.075,	45.976,	26.599,	
# new facet 2/2
	VERTEX,	52.3329,	41.6999,	31.6875,	
# new facet 1/2
	VERTEX,	52.335,	41.6976,	31.7035,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 1/2
	VERTEX,	50.075,	45.976,	26.599,	
# new facet 2/2
	VERTEX,	52.335,	41.6976,	31.7035,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 2/2
	VERTEX,	50.075,	45.976,	26.599,	
# new facet 1/2
	VERTEX,	52.335,	41.6976,	31.7035,	
# new facet 1/2
	VERTEX,	52.3329,	41.6999,	31.6875,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 2/2
	VERTEX,	52.335,	41.6976,	31.7035,	
# new facet 2/2
	VERTEX,	52.3329,	41.6999,	31.6875,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 1/2
	VERTEX,	52.3329,	41.6999,	31.6875,	
# new facet 1/2
	VERTEX,	52.335,	41.6976,	31.7035,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 2/2
	VERTEX,	52.3329,	41.6999,	31.6875,	
# new facet 2/2
	VERTEX,	52.335,	41.6976,	31.7035,	
# new facet 1/2
	VERTEX,	52.3731,	41.8482,	31.7318,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 1/2
	VERTEX,	52.335,	41.6976,	31.7035,	
# new facet 2/2
	VERTEX,	52.3731,	41.8482,	31.7318,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 2/2
	VERTEX,	52.335,	41.6976,	31.7035,	
# new facet 1/2
	VERTEX,	52.3731,	41.8482,	31.7318,	
# new facet 1/2
	VERTEX,	52.3329,	41.6999,	31.6875,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 2/2
	VERTEX,	52.3731,	41.8482,	31.7318,	
# new facet 2/2
	VERTEX,	52.3329,	41.6999,	31.6875,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 1/2
	VERTEX,	52.3731,	41.8482,	31.7318,	
# new facet 1/2
	VERTEX,	52.335,	41.6976,	31.7035,	
# new facet 1/2
	VERTEX,	52.3329,	41.6999,	31.6875,	
# new facet 2/2
	VERTEX,	52.3731,	41.8482,	31.7318,	
# new facet 2/2
	VERTEX,	52.335,	41.6976,	31.7035,	
# new facet 2/2
	VERTEX,	52.3329,	41.6999,	31.6875,	
# new polyhedron
# new facet 1/2
	VERTEX,	50.085,	45.986,	26.609,	
# new facet 1/2
	VERTEX,	51.7752,	45.1435,	27.7108,	
# new facet 1/2
	VERTEX,	50.3663,	44.5267,	26.6334,	
# new facet 2/2
	VERTEX,	50.085,	45.986,	26.609,	
# new facet 2/2
	VERTEX,	51.7752,	45.1435,	27.7108,	
# new facet 2/2
	VERTEX,	50.3663,	44.5267,	26.6334,	
# new facet 1/2
	VERTEX,	51.0423,	45.9302,	26.5378,	
# new facet 1/2
	VERTEX,	50.085,	45.986,	26.609,	
# new facet 1/2
	VERTEX,	50.3663,	44.5267,	26.6334,	
# new facet 2/2
	VERTEX,	51.0423,	45.9302,	26.5378,	
# new facet 2/2
	VERTEX,	50.085,	45.986,	26.609,	
# new facet 2/2
	VERTEX,	50.3663,	44.5267,	26.6334,	
# new facet 1/2
	VERTEX,	51.0423,	45.9302,	26.5378,	
# new facet 1/2
	VERTEX,	51.7752,	45.1435,	27.7108,	
# new facet 1/2
	VERTEX,	50.085,	45.986,	26.609,	
# new facet 2/2
	VERTEX,	51.0423,	45.9302,	26.5378,	
# new facet 2/2
	VERTEX,	51.7752,	45.1435,	27.7108,	
# new facet 2/2
	VERTEX,	50.085,	45.986,	26.609,	
# new facet 1/2
	VERTEX,	51.0423,	45.9302,	26.5378,	
# new facet 1/2
	VERTEX,	50.3663,	44.5267,	26.6334,	
# new facet 1/2
	VERTEX,	51.7752,	45.1435,	27.7108,	
# new facet 2/2
	VERTEX,	51.0423,	45.9302,	26.5378,	
# new facet 2/2
	VERTEX,	50.3663,	44.5267,	26.6334,	
# new facet 2/2
	VERTEX,	51.7752,	45.1435,	27.7108,	
# new polyhedron
# new facet 1/2
	VERTEX,	42.279,	36.23,	28.624,	
# new facet 1/2
	VERTEX,	44.2564,	41.0999,	26.1207,	
# new facet 1/2
	VERTEX,	39.0444,	42.8569,	31.1306,	
# new facet 2/2
	VERTEX,	42.279,	36.23,	28.624,	
# new facet 2/2
	VERTEX,	44.2564,	41.0999,	26.1207,	
# new facet 2/2
	VERTEX,	39.0444,	42.8569,	31.1306,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 1/2
	VERTEX,	42.279,	36.23,	28.624,	
# new facet 1/2
	VERTEX,	39.0444,	42.8569,	31.1306,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 2/2
	VERTEX,	42.279,	36.23,	28.624,	
# new facet 2/2
	VERTEX,	39.0444,	42.8569,	31.1306,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 1/2
	VERTEX,	44.2564,	41.0999,	26.1207,	
# new facet 1/2
	VERTEX,	42.279,	36.23,	28.624,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 2/2
	VERTEX,	44.2564,	41.0999,	26.1207,	
# new facet 2/2
	VERTEX,	42.279,	36.23,	28.624,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 1/2
	VERTEX,	39.0444,	42.8569,	31.1306,	
# new facet 1/2
	VERTEX,	44.2564,	41.0999,	26.1207,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 2/2
	VERTEX,	39.0444,	42.8569,	31.1306,	
# new facet 2/2
	VERTEX,	44.2564,	41.0999,	26.1207,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 1/2
	VERTEX,	44.2564,	41.0999,	26.1207,	
# new facet 1/2
	VERTEX,	39.0444,	42.8569,	31.1306,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 2/2
	VERTEX,	44.2564,	41.0999,	26.1207,	
# new facet 2/2
	VERTEX,	39.0444,	42.8569,	31.1306,	
# new facet 1/2
	VERTEX,	44.3838,	41.4032,	26.2168,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 1/2
	VERTEX,	39.0444,	42.8569,	31.1306,	
# new facet 2/2
	VERTEX,	44.3838,	41.4032,	26.2168,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 2/2
	VERTEX,	39.0444,	42.8569,	31.1306,	
# new facet 1/2
	VERTEX,	44.3838,	41.4032,	26.2168,	
# new facet 1/2
	VERTEX,	44.2564,	41.0999,	26.1207,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 2/2
	VERTEX,	44.3838,	41.4032,	26.2168,	
# new facet 2/2
	VERTEX,	44.2564,	41.0999,	26.1207,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 1/2
	VERTEX,	44.3838,	41.4032,	26.2168,	
# new facet 1/2
	VERTEX,	39.0444,	42.8569,	31.1306,	
# new facet 1/2
	VERTEX,	44.2564,	41.0999,	26.1207,	
# new facet 2/2
	VERTEX,	44.3838,	41.4032,	26.2168,	
# new facet 2/2
	VERTEX,	39.0444,	42.8569,	31.1306,	
# new facet 2/2
	VERTEX,	44.2564,	41.0999,	26.1207,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 1/2
	VERTEX,	39.0444,	42.8569,	31.1306,	
# new facet 1/2
	VERTEX,	44.3838,	41.4032,	26.2168,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 2/2
	VERTEX,	39.0444,	42.8569,	31.1306,	
# new facet 2/2
	VERTEX,	44.3838,	41.4032,	26.2168,	
# new facet 1/2
	VERTEX,	38.9328,	43.3237,	31.4927,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 1/2
	VERTEX,	44.3838,	41.4032,	26.2168,	
# new facet 2/2
	VERTEX,	38.9328,	43.3237,	31.4927,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 2/2
	VERTEX,	44.3838,	41.4032,	26.2168,	
# new facet 1/2
	VERTEX,	38.9328,	43.3237,	31.4927,	
# new facet 1/2
	VERTEX,	39.0444,	42.8569,	31.1306,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 2/2
	VERTEX,	38.9328,	43.3237,	31.4927,	
# new facet 2/2
	VERTEX,	39.0444,	42.8569,	31.1306,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 1/2
	VERTEX,	38.9328,	43.3237,	31.4927,	
# new facet 1/2
	VERTEX,	44.3838,	41.4032,	26.2168,	
# new facet 1/2
	VERTEX,	39.0444,	42.8569,	31.1306,	
# new facet 2/2
	VERTEX,	38.9328,	43.3237,	31.4927,	
# new facet 2/2
	VERTEX,	44.3838,	41.4032,	26.2168,	
# new facet 2/2
	VERTEX,	39.0444,	42.8569,	31.1306,	
# new polyhedron
# new facet 1/2
	VERTEX,	43.38,	39.632,	35.358,	
# new facet 1/2
	VERTEX,	39.3997,	41.6471,	33.6601,	
# new facet 1/2
	VERTEX,	38.9128,	43.3037,	31.4727,	
# new facet 2/2
	VERTEX,	43.38,	39.632,	35.358,	
# new facet 2/2
	VERTEX,	39.3997,	41.6471,	33.6601,	
# new facet 2/2
	VERTEX,	38.9128,	43.3037,	31.4727,	
# new facet 1/2
	VERTEX,	41.246,	36.095,	32.528,	
# new facet 1/2
	VERTEX,	43.38,	39.632,	35.358,	
# new facet 1/2
	VERTEX,	38.9128,	43.3037,	31.4727,	
# new facet 2/2
	VERTEX,	41.246,	36.095,	32.528,	
# new facet 2/2
	VERTEX,	43.38,	39.632,	35.358,	
# new facet 2/2
	VERTEX,	38.9128,	43.3037,	31.4727,	
# new facet 1/2
	VERTEX,	41.246,	36.095,	32.528,	
# new facet 1/2
	VERTEX,	39.3997,	41.6471,	33.6601,	
# new facet 1/2
	VERTEX,	43.38,	39.632,	35.358,	
# new facet 2/2
	VERTEX,	41.246,	36.095,	32.528,	
# new facet 2/2
	VERTEX,	39.3997,	41.6471,	33.6601,	
# new facet 2/2
	VERTEX,	43.38,	39.632,	35.358,	
# new facet 1/2
	VERTEX,	41.246,	36.095,	32.528,	
# new facet 1/2
	VERTEX,	38.9128,	43.3037,	31.4727,	
# new facet 1/2
	VERTEX,	39.3997,	41.6471,	33.6601,	
# new facet 2/2
	VERTEX,	41.246,	36.095,	32.528,	
# new facet 2/2
	VERTEX,	38.9128,	43.3037,	31.4727,	
# new facet 2/2
	VERTEX,	39.3997,	41.6471,	33.6601,	
# new facet 1/2
	VERTEX,	41.246,	36.095,	32.528,	
# new facet 1/2
	VERTEX,	39.3997,	41.6471,	33.6601,	
# new facet 1/2
	VERTEX,	38.9128,	43.3037,	31.4727,	
# new facet 2/2
	VERTEX,	41.246,	36.095,	32.528,	
# new facet 2/2
	VERTEX,	39.3997,	41.6471,	33.6601,	
# new facet 2/2
	VERTEX,	38.9128,	43.3037,	31.4727,	
# new facet 1/2
	VERTEX,	39.0276,	41.1508,	33.217,	
# new facet 1/2
	VERTEX,	41.246,	36.095,	32.528,	
# new facet 1/2
	VERTEX,	38.9128,	43.3037,	31.4727,	
# new facet 2/2
	VERTEX,	39.0276,	41.1508,	33.217,	
# new facet 2/2
	VERTEX,	41.246,	36.095,	32.528,	
# new facet 2/2
	VERTEX,	38.9128,	43.3037,	31.4727,	
# new facet 1/2
	VERTEX,	39.0276,	41.1508,	33.217,	
# new facet 1/2
	VERTEX,	39.3997,	41.6471,	33.6601,	
# new facet 1/2
	VERTEX,	41.246,	36.095,	32.528,	
# new facet 2/2
	VERTEX,	39.0276,	41.1508,	33.217,	
# new facet 2/2
	VERTEX,	39.3997,	41.6471,	33.6601,	
# new facet 2/2
	VERTEX,	41.246,	36.095,	32.528,	
# new facet 1/2
	VERTEX,	39.0276,	41.1508,	33.217,	
# new facet 1/2
	VERTEX,	38.9128,	43.3037,	31.4727,	
# new facet 1/2
	VERTEX,	39.3997,	41.6471,	33.6601,	
# new facet 2/2
	VERTEX,	39.0276,	41.1508,	33.217,	
# new facet 2/2
	VERTEX,	38.9128,	43.3037,	31.4727,	
# new facet 2/2
	VERTEX,	39.3997,	41.6471,	33.6601,	
# new facet 1/2
	VERTEX,	41.246,	36.095,	32.528,	
# new facet 1/2
	VERTEX,	38.9128,	43.3037,	31.4727,	
# new facet 1/2
	VERTEX,	39.0276,	41.1508,	33.217,	
# new facet 2/2
	VERTEX,	41.246,	36.095,	32.528,	
# new facet 2/2
	VERTEX,	38.9128,	43.3037,	31.4727,	
# new facet 2/2
	VERTEX,	39.0276,	41.1508,	33.217,	
# new facet 1/2
	VERTEX,	38.8958,	43.1194,	31.4173,	
# new facet 1/2
	VERTEX,	41.246,	36.095,	32.528,	
# new facet 1/2
	VERTEX,	39.0276,	41.1508,	33.217,	
# new facet 2/2
	VERTEX,	38.8958,	43.1194,	31.4173,	
# new facet 2/2
	VERTEX,	41.246,	36.095,	32.528,	
# new facet 2/2
	VERTEX,	39.0276,	41.1508,	33.217,	
# new facet 1/2
	VERTEX,	38.8958,	43.1194,	31.4173,	
# new facet 1/2
	VERTEX,	38.9128,	43.3037,	31.4727,	
# new facet 1/2
	VERTEX,	41.246,	36.095,	32.528,	
# new facet 2/2
	VERTEX,	38.8958,	43.1194,	31.4173,	
# new facet 2/2
	VERTEX,	38.9128,	43.3037,	31.4727,	
# new facet 2/2
	VERTEX,	41.246,	36.095,	32.528,	
# new facet 1/2
	VERTEX,	38.8958,	43.1194,	31.4173,	
# new facet 1/2
	VERTEX,	39.0276,	41.1508,	33.217,	
# new facet 1/2
	VERTEX,	38.9128,	43.3037,	31.4727,	
# new facet 2/2
	VERTEX,	38.8958,	43.1194,	31.4173,	
# new facet 2/2
	VERTEX,	39.0276,	41.1508,	33.217,	
# new facet 2/2
	VERTEX,	38.9128,	43.3037,	31.4727,	
# new polyhedron
# new facet 1/2
	VERTEX,	45.919,	43.192,	26.334,	
# new facet 1/2
	VERTEX,	45.6786,	43.4203,	26.4327,	
# new facet 1/2
	VERTEX,	45.2496,	44.0506,	26.9852,	
# new facet 2/2
	VERTEX,	45.919,	43.192,	26.334,	
# new facet 2/2
	VERTEX,	45.6786,	43.4203,	26.4327,	
# new facet 2/2
	VERTEX,	45.2496,	44.0506,	26.9852,	
# new facet 1/2
	VERTEX,	40.8168,	43.3501,	29.895,	
# new facet 1/2
	VERTEX,	45.919,	43.192,	26.334,	
# new facet 1/2
	VERTEX,	45.2496,	44.0506,	26.9852,	
# new facet 2/2
	VERTEX,	40.8168,	43.3501,	29.895,	
# new facet 2/2
	VERTEX,	45.919,	43.192,	26.334,	
# new facet 2/2
	VERTEX,	45.2496,	44.0506,	26.9852,	
# new facet 1/2
	VERTEX,	40.8168,	43.3501,	29.895,	
# new facet 1/2
	VERTEX,	45.6786,	43.4203,	26.4327,	
# new facet 1/2
	VERTEX,	45.919,	43.192,	26.334,	
# new facet 2/2
	VERTEX,	40.8168,	43.3501,	29.895,	
# new facet 2/2
	VERTEX,	45.6786,	43.4203,	26.4327,	
# new facet 2/2
	VERTEX,	45.919,	43.192,	26.334,	
# new facet 1/2
	VERTEX,	40.8168,	43.3501,	29.895,	
# new facet 1/2
	VERTEX,	45.2496,	44.0506,	26.9852,	
# new facet 1/2
	VERTEX,	45.6786,	43.4203,	26.4327,	
# new facet 2/2
	VERTEX,	40.8168,	43.3501,	29.895,	
# new facet 2/2
	VERTEX,	45.2496,	44.0506,	26.9852,	
# new facet 2/2
	VERTEX,	45.6786,	43.4203,	26.4327,	
# new polyhedron
# new facet 1/2
	VERTEX,	45.909,	43.182,	26.324,	
# new facet 1/2
	VERTEX,	40.8168,	43.3501,	29.895,	
# new facet 1/2
	VERTEX,	45.3614,	42.548,	26.2015,	
# new facet 2/2
	VERTEX,	45.909,	43.182,	26.324,	
# new facet 2/2
	VERTEX,	40.8168,	43.3501,	29.895,	
# new facet 2/2
	VERTEX,	45.3614,	42.548,	26.2015,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 1/2
	VERTEX,	45.909,	43.182,	26.324,	
# new facet 1/2
	VERTEX,	45.3614,	42.548,	26.2015,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 2/2
	VERTEX,	45.909,	43.182,	26.324,	
# new facet 2/2
	VERTEX,	45.3614,	42.548,	26.2015,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 1/2
	VERTEX,	40.8168,	43.3501,	29.895,	
# new facet 1/2
	VERTEX,	45.909,	43.182,	26.324,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 2/2
	VERTEX,	40.8168,	43.3501,	29.895,	
# new facet 2/2
	VERTEX,	45.909,	43.182,	26.324,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 1/2
	VERTEX,	45.3614,	42.548,	26.2015,	
# new facet 1/2
	VERTEX,	40.8168,	43.3501,	29.895,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 2/2
	VERTEX,	45.3614,	42.548,	26.2015,	
# new facet 2/2
	VERTEX,	40.8168,	43.3501,	29.895,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 1/2
	VERTEX,	40.8168,	43.3501,	29.895,	
# new facet 1/2
	VERTEX,	45.3614,	42.548,	26.2015,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 2/2
	VERTEX,	40.8168,	43.3501,	29.895,	
# new facet 2/2
	VERTEX,	45.3614,	42.548,	26.2015,	
# new facet 1/2
	VERTEX,	38.9228,	43.3137,	31.4827,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 1/2
	VERTEX,	45.3614,	42.548,	26.2015,	
# new facet 2/2
	VERTEX,	38.9228,	43.3137,	31.4827,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 2/2
	VERTEX,	45.3614,	42.548,	26.2015,	
# new facet 1/2
	VERTEX,	38.9228,	43.3137,	31.4827,	
# new facet 1/2
	VERTEX,	40.8168,	43.3501,	29.895,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 2/2
	VERTEX,	38.9228,	43.3137,	31.4827,	
# new facet 2/2
	VERTEX,	40.8168,	43.3501,	29.895,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 1/2
	VERTEX,	38.9228,	43.3137,	31.4827,	
# new facet 1/2
	VERTEX,	45.3614,	42.548,	26.2015,	
# new facet 1/2
	VERTEX,	40.8168,	43.3501,	29.895,	
# new facet 2/2
	VERTEX,	38.9228,	43.3137,	31.4827,	
# new facet 2/2
	VERTEX,	45.3614,	42.548,	26.2015,	
# new facet 2/2
	VERTEX,	40.8168,	43.3501,	29.895,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 1/2
	VERTEX,	45.3614,	42.548,	26.2015,	
# new facet 1/2
	VERTEX,	38.9228,	43.3137,	31.4827,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 2/2
	VERTEX,	45.3614,	42.548,	26.2015,	
# new facet 2/2
	VERTEX,	38.9228,	43.3137,	31.4827,	
# new facet 1/2
	VERTEX,	44.3938,	41.4132,	26.2268,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 1/2
	VERTEX,	38.9228,	43.3137,	31.4827,	
# new facet 2/2
	VERTEX,	44.3938,	41.4132,	26.2268,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 2/2
	VERTEX,	38.9228,	43.3137,	31.4827,	
# new facet 1/2
	VERTEX,	44.3938,	41.4132,	26.2268,	
# new facet 1/2
	VERTEX,	45.3614,	42.548,	26.2015,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 2/2
	VERTEX,	44.3938,	41.4132,	26.2268,	
# new facet 2/2
	VERTEX,	45.3614,	42.548,	26.2015,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 1/2
	VERTEX,	44.3938,	41.4132,	26.2268,	
# new facet 1/2
	VERTEX,	38.9228,	43.3137,	31.4827,	
# new facet 1/2
	VERTEX,	45.3614,	42.548,	26.2015,	
# new facet 2/2
	VERTEX,	44.3938,	41.4132,	26.2268,	
# new facet 2/2
	VERTEX,	38.9228,	43.3137,	31.4827,	
# new facet 2/2
	VERTEX,	45.3614,	42.548,	26.2015,	
# new polyhedron
# new facet 1/2
	VERTEX,	47.454,	44.603,	26.246,	
# new facet 1/2
	VERTEX,	42.832,	47.987,	33.199,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 2/2
	VERTEX,	47.454,	44.603,	26.246,	
# new facet 2/2
	VERTEX,	42.832,	47.987,	33.199,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 1/2
	VERTEX,	46.7598,	46.2366,	27.1813,	
# new facet 1/2
	VERTEX,	47.454,	44.603,	26.246,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 2/2
	VERTEX,	46.7598,	46.2366,	27.1813,	
# new facet 2/2
	VERTEX,	47.454,	44.603,	26.246,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 1/2
	VERTEX,	46.7598,	46.2366,	27.1813,	
# new facet 1/2
	VERTEX,	42.832,	47.987,	33.199,	
# new facet 1/2
	VERTEX,	47.454,	44.603,	26.246,	
# new facet 2/2
	VERTEX,	46.7598,	46.2366,	27.1813,	
# new facet 2/2
	VERTEX,	42.832,	47.987,	33.199,	
# new facet 2/2
	VERTEX,	47.454,	44.603,	26.246,	
# new facet 1/2
	VERTEX,	46.7598,	46.2366,	27.1813,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 1/2
	VERTEX,	42.832,	47.987,	33.199,	
# new facet 2/2
	VERTEX,	46.7598,	46.2366,	27.1813,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 2/2
	VERTEX,	42.832,	47.987,	33.199,	
# new facet 1/2
	VERTEX,	47.454,	44.603,	26.246,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 1/2
	VERTEX,	46.7598,	46.2366,	27.1813,	
# new facet 2/2
	VERTEX,	47.454,	44.603,	26.246,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 2/2
	VERTEX,	46.7598,	46.2366,	27.1813,	
# new facet 1/2
	VERTEX,	44.5981,	49.8916,	30.2091,	
# new facet 1/2
	VERTEX,	47.454,	44.603,	26.246,	
# new facet 1/2
	VERTEX,	46.7598,	46.2366,	27.1813,	
# new facet 2/2
	VERTEX,	44.5981,	49.8916,	30.2091,	
# new facet 2/2
	VERTEX,	47.454,	44.603,	26.246,	
# new facet 2/2
	VERTEX,	46.7598,	46.2366,	27.1813,	
# new facet 1/2
	VERTEX,	44.5981,	49.8916,	30.2091,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 1/2
	VERTEX,	47.454,	44.603,	26.246,	
# new facet 2/2
	VERTEX,	44.5981,	49.8916,	30.2091,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 2/2
	VERTEX,	47.454,	44.603,	26.246,	
# new facet 1/2
	VERTEX,	44.5981,	49.8916,	30.2091,	
# new facet 1/2
	VERTEX,	46.7598,	46.2366,	27.1813,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 2/2
	VERTEX,	44.5981,	49.8916,	30.2091,	
# new facet 2/2
	VERTEX,	46.7598,	46.2366,	27.1813,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 1/2
	VERTEX,	46.7598,	46.2366,	27.1813,	
# new facet 1/2
	VERTEX,	44.5981,	49.8916,	30.2091,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 2/2
	VERTEX,	46.7598,	46.2366,	27.1813,	
# new facet 2/2
	VERTEX,	44.5981,	49.8916,	30.2091,	
# new facet 1/2
	VERTEX,	45.6865,	50.1177,	29.7054,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 1/2
	VERTEX,	44.5981,	49.8916,	30.2091,	
# new facet 2/2
	VERTEX,	45.6865,	50.1177,	29.7054,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 2/2
	VERTEX,	44.5981,	49.8916,	30.2091,	
# new facet 1/2
	VERTEX,	45.6865,	50.1177,	29.7054,	
# new facet 1/2
	VERTEX,	46.7598,	46.2366,	27.1813,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 2/2
	VERTEX,	45.6865,	50.1177,	29.7054,	
# new facet 2/2
	VERTEX,	46.7598,	46.2366,	27.1813,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 1/2
	VERTEX,	45.6865,	50.1177,	29.7054,	
# new facet 1/2
	VERTEX,	44.5981,	49.8916,	30.2091,	
# new facet 1/2
	VERTEX,	46.7598,	46.2366,	27.1813,	
# new facet 2/2
	VERTEX,	45.6865,	50.1177,	29.7054,	
# new facet 2/2
	VERTEX,	44.5981,	49.8916,	30.2091,	
# new facet 2/2
	VERTEX,	46.7598,	46.2366,	27.1813,	
# new polyhedron
# new facet 1/2
	VERTEX,	50.711,	51.114,	31.37,	
# new facet 1/2
	VERTEX,	51.6122,	52.4673,	31.2357,	
# new facet 1/2
	VERTEX,	54.2491,	52.1714,	26.9894,	
# new facet 2/2
	VERTEX,	50.711,	51.114,	31.37,	
# new facet 2/2
	VERTEX,	51.6122,	52.4673,	31.2357,	
# new facet 2/2
	VERTEX,	54.2491,	52.1714,	26.9894,	
# new facet 1/2
	VERTEX,	53.3246,	50.4841,	29.7364,	
# new facet 1/2
	VERTEX,	50.711,	51.114,	31.37,	
# new facet 1/2
	VERTEX,	54.2491,	52.1714,	26.9894,	
# new facet 2/2
	VERTEX,	53.3246,	50.4841,	29.7364,	
# new facet 2/2
	VERTEX,	50.711,	51.114,	31.37,	
# new facet 2/2
	VERTEX,	54.2491,	52.1714,	26.9894,	
# new facet 1/2
	VERTEX,	53.3246,	50.4841,	29.7364,	
# new facet 1/2
	VERTEX,	51.6122,	52.4673,	31.2357,	
# new facet 1/2
	VERTEX,	50.711,	51.114,	31.37,	
# new facet 2/2
	VERTEX,	53.3246,	50.4841,	29.7364,	
# new facet 2/2
	VERTEX,	51.6122,	52.4673,	31.2357,	
# new facet 2/2
	VERTEX,	50.711,	51.114,	31.37,	
# new facet 1/2
	VERTEX,	53.3246,	50.4841,	29.7364,	
# new facet 1/2
	VERTEX,	54.2491,	52.1714,	26.9894,	
# new facet 1/2
	VERTEX,	51.6122,	52.4673,	31.2357,	
# new facet 2/2
	VERTEX,	53.3246,	50.4841,	29.7364,	
# new facet 2/2
	VERTEX,	54.2491,	52.1714,	26.9894,	
# new facet 2/2
	VERTEX,	51.6122,	52.4673,	31.2357,	
# new polyhedron
# new facet 1/2
	VERTEX,	43.38,	39.632,	35.358,	
# new facet 1/2
	VERTEX,	48.2511,	37.2948,	35.0295,	
# new facet 1/2
	VERTEX,	52.2914,	41.6703,	31.7533,	
# new facet 2/2
	VERTEX,	43.38,	39.632,	35.358,	
# new facet 2/2
	VERTEX,	48.2511,	37.2948,	35.0295,	
# new facet 2/2
	VERTEX,	52.2914,	41.6703,	31.7533,	
# new facet 1/2
	VERTEX,	46.783,	46.565,	37.098,	
# new facet 1/2
	VERTEX,	43.38,	39.632,	35.358,	
# new facet 1/2
	VERTEX,	52.2914,	41.6703,	31.7533,	
# new facet 2/2
	VERTEX,	46.783,	46.565,	37.098,	
# new facet 2/2
	VERTEX,	43.38,	39.632,	35.358,	
# new facet 2/2
	VERTEX,	52.2914,	41.6703,	31.7533,	
# new facet 1/2
	VERTEX,	46.783,	46.565,	37.098,	
# new facet 1/2
	VERTEX,	48.2511,	37.2948,	35.0295,	
# new facet 1/2
	VERTEX,	43.38,	39.632,	35.358,	
# new facet 2/2
	VERTEX,	46.783,	46.565,	37.098,	
# new facet 2/2
	VERTEX,	48.2511,	37.2948,	35.0295,	
# new facet 2/2
	VERTEX,	43.38,	39.632,	35.358,	
# new facet 1/2
	VERTEX,	46.783,	46.565,	37.098,	
# new facet 1/2
	VERTEX,	52.2914,	41.6703,	31.7533,	
# new facet 1/2
	VERTEX,	48.2511,	37.2948,	35.0295,	
# new facet 2/2
	VERTEX,	46.783,	46.565,	37.098,	
# new facet 2/2
	VERTEX,	52.2914,	41.6703,	31.7533,	
# new facet 2/2
	VERTEX,	48.2511,	37.2948,	35.0295,	
# new facet 1/2
	VERTEX,	46.783,	46.565,	37.098,	
# new facet 1/2
	VERTEX,	48.2511,	37.2948,	35.0295,	
# new facet 1/2
	VERTEX,	52.2914,	41.6703,	31.7533,	
# new facet 2/2
	VERTEX,	46.783,	46.565,	37.098,	
# new facet 2/2
	VERTEX,	48.2511,	37.2948,	35.0295,	
# new facet 2/2
	VERTEX,	52.2914,	41.6703,	31.7533,	
# new facet 1/2
	VERTEX,	48.7875,	38.3178,	35.3029,	
# new facet 1/2
	VERTEX,	46.783,	46.565,	37.098,	
# new facet 1/2
	VERTEX,	52.2914,	41.6703,	31.7533,	
# new facet 2/2
	VERTEX,	48.7875,	38.3178,	35.3029,	
# new facet 2/2
	VERTEX,	46.783,	46.565,	37.098,	
# new facet 2/2
	VERTEX,	52.2914,	41.6703,	31.7533,	
# new facet 1/2
	VERTEX,	48.7875,	38.3178,	35.3029,	
# new facet 1/2
	VERTEX,	48.2511,	37.2948,	35.0295,	
# new facet 1/2
	VERTEX,	46.783,	46.565,	37.098,	
# new facet 2/2
	VERTEX,	48.7875,	38.3178,	35.3029,	
# new facet 2/2
	VERTEX,	48.2511,	37.2948,	35.0295,	
# new facet 2/2
	VERTEX,	46.783,	46.565,	37.098,	
# new facet 1/2
	VERTEX,	48.7875,	38.3178,	35.3029,	
# new facet 1/2
	VERTEX,	52.2914,	41.6703,	31.7533,	
# new facet 1/2
	VERTEX,	48.2511,	37.2948,	35.0295,	
# new facet 2/2
	VERTEX,	48.7875,	38.3178,	35.3029,	
# new facet 2/2
	VERTEX,	52.2914,	41.6703,	31.7533,	
# new facet 2/2
	VERTEX,	48.2511,	37.2948,	35.0295,	
# new facet 1/2
	VERTEX,	46.783,	46.565,	37.098,	
# new facet 1/2
	VERTEX,	52.2914,	41.6703,	31.7533,	
# new facet 1/2
	VERTEX,	48.7875,	38.3178,	35.3029,	
# new facet 2/2
	VERTEX,	46.783,	46.565,	37.098,	
# new facet 2/2
	VERTEX,	52.2914,	41.6703,	31.7533,	
# new facet 2/2
	VERTEX,	48.7875,	38.3178,	35.3029,	
# new facet 1/2
	VERTEX,	52.3024,	41.7697,	31.8185,	
# new facet 1/2
	VERTEX,	46.783,	46.565,	37.098,	
# new facet 1/2
	VERTEX,	48.7875,	38.3178,	35.3029,	
# new facet 2/2
	VERTEX,	52.3024,	41.7697,	31.8185,	
# new facet 2/2
	VERTEX,	46.783,	46.565,	37.098,	
# new facet 2/2
	VERTEX,	48.7875,	38.3178,	35.3029,	
# new facet 1/2
	VERTEX,	52.3024,	41.7697,	31.8185,	
# new facet 1/2
	VERTEX,	52.2914,	41.6703,	31.7533,	
# new facet 1/2
	VERTEX,	46.783,	46.565,	37.098,	
# new facet 2/2
	VERTEX,	52.3024,	41.7697,	31.8185,	
# new facet 2/2
	VERTEX,	52.2914,	41.6703,	31.7533,	
# new facet 2/2
	VERTEX,	46.783,	46.565,	37.098,	
# new facet 1/2
	VERTEX,	52.3024,	41.7697,	31.8185,	
# new facet 1/2
	VERTEX,	48.7875,	38.3178,	35.3029,	
# new facet 1/2
	VERTEX,	52.2914,	41.6703,	31.7533,	
# new facet 2/2
	VERTEX,	52.3024,	41.7697,	31.8185,	
# new facet 2/2
	VERTEX,	48.7875,	38.3178,	35.3029,	
# new facet 2/2
	VERTEX,	52.2914,	41.6703,	31.7533,	
# new polyhedron
# new facet 1/2
	VERTEX,	46.793,	46.555,	37.108,	
# new facet 1/2
	VERTEX,	47.6744,	46.7204,	37.8114,	
# new facet 1/2
	VERTEX,	47.5201,	45.5895,	37.858,	
# new facet 2/2
	VERTEX,	46.793,	46.555,	37.108,	
# new facet 2/2
	VERTEX,	47.6744,	46.7204,	37.8114,	
# new facet 2/2
	VERTEX,	47.5201,	45.5895,	37.858,	
# new facet 1/2
	VERTEX,	52.2724,	41.7397,	31.7885,	
# new facet 1/2
	VERTEX,	46.793,	46.555,	37.108,	
# new facet 1/2
	VERTEX,	47.5201,	45.5895,	37.858,	
# new facet 2/2
	VERTEX,	52.2724,	41.7397,	31.7885,	
# new facet 2/2
	VERTEX,	46.793,	46.555,	37.108,	
# new facet 2/2
	VERTEX,	47.5201,	45.5895,	37.858,	
# new facet 1/2
	VERTEX,	52.2724,	41.7397,	31.7885,	
# new facet 1/2
	VERTEX,	47.6744,	46.7204,	37.8114,	
# new facet 1/2
	VERTEX,	46.793,	46.555,	37.108,	
# new facet 2/2
	VERTEX,	52.2724,	41.7397,	31.7885,	
# new facet 2/2
	VERTEX,	47.6744,	46.7204,	37.8114,	
# new facet 2/2
	VERTEX,	46.793,	46.555,	37.108,	
# new facet 1/2
	VERTEX,	52.2724,	41.7397,	31.7885,	
# new facet 1/2
	VERTEX,	47.5201,	45.5895,	37.858,	
# new facet 1/2
	VERTEX,	47.6744,	46.7204,	37.8114,	
# new facet 2/2
	VERTEX,	52.2724,	41.7397,	31.7885,	
# new facet 2/2
	VERTEX,	47.5201,	45.5895,	37.858,	
# new facet 2/2
	VERTEX,	47.6744,	46.7204,	37.8114,	
# new polyhedron
# new facet 1/2
	VERTEX,	46.793,	46.555,	37.108,	
# new facet 1/2
	VERTEX,	48.7675,	38.2978,	35.2829,	
# new facet 1/2
	VERTEX,	47.5201,	45.5895,	37.858,	
# new facet 2/2
	VERTEX,	46.793,	46.555,	37.108,	
# new facet 2/2
	VERTEX,	48.7675,	38.2978,	35.2829,	
# new facet 2/2
	VERTEX,	47.5201,	45.5895,	37.858,	
# new facet 1/2
	VERTEX,	52.2724,	41.7397,	31.7885,	
# new facet 1/2
	VERTEX,	46.793,	46.555,	37.108,	
# new facet 1/2
	VERTEX,	47.5201,	45.5895,	37.858,	
# new facet 2/2
	VERTEX,	52.2724,	41.7397,	31.7885,	
# new facet 2/2
	VERTEX,	46.793,	46.555,	37.108,	
# new facet 2/2
	VERTEX,	47.5201,	45.5895,	37.858,	
# new facet 1/2
	VERTEX,	52.2724,	41.7397,	31.7885,	
# new facet 1/2
	VERTEX,	48.7675,	38.2978,	35.2829,	
# new facet 1/2
	VERTEX,	46.793,	46.555,	37.108,	
# new facet 2/2
	VERTEX,	52.2724,	41.7397,	31.7885,	
# new facet 2/2
	VERTEX,	48.7675,	38.2978,	35.2829,	
# new facet 2/2
	VERTEX,	46.793,	46.555,	37.108,	
# new facet 1/2
	VERTEX,	52.2724,	41.7397,	31.7885,	
# new facet 1/2
	VERTEX,	47.5201,	45.5895,	37.858,	
# new facet 1/2
	VERTEX,	48.7675,	38.2978,	35.2829,	
# new facet 2/2
	VERTEX,	52.2724,	41.7397,	31.7885,	
# new facet 2/2
	VERTEX,	47.5201,	45.5895,	37.858,	
# new facet 2/2
	VERTEX,	48.7675,	38.2978,	35.2829,	
# new polyhedron
# new facet 1/2
	VERTEX,	41.136,	44.732,	35.115,	
# new facet 1/2
	VERTEX,	46.783,	46.565,	37.098,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 2/2
	VERTEX,	41.136,	44.732,	35.115,	
# new facet 2/2
	VERTEX,	46.783,	46.565,	37.098,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 1/2
	VERTEX,	41.5908,	44.7332,	35.8274,	
# new facet 1/2
	VERTEX,	41.136,	44.732,	35.115,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 2/2
	VERTEX,	41.5908,	44.7332,	35.8274,	
# new facet 2/2
	VERTEX,	41.136,	44.732,	35.115,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 1/2
	VERTEX,	41.5908,	44.7332,	35.8274,	
# new facet 1/2
	VERTEX,	46.783,	46.565,	37.098,	
# new facet 1/2
	VERTEX,	41.136,	44.732,	35.115,	
# new facet 2/2
	VERTEX,	41.5908,	44.7332,	35.8274,	
# new facet 2/2
	VERTEX,	46.783,	46.565,	37.098,	
# new facet 2/2
	VERTEX,	41.136,	44.732,	35.115,	
# new facet 1/2
	VERTEX,	41.5908,	44.7332,	35.8274,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 1/2
	VERTEX,	46.783,	46.565,	37.098,	
# new facet 2/2
	VERTEX,	41.5908,	44.7332,	35.8274,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 2/2
	VERTEX,	46.783,	46.565,	37.098,	
# new facet 1/2
	VERTEX,	41.136,	44.732,	35.115,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 1/2
	VERTEX,	41.5908,	44.7332,	35.8274,	
# new facet 2/2
	VERTEX,	41.136,	44.732,	35.115,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 2/2
	VERTEX,	41.5908,	44.7332,	35.8274,	
# new facet 1/2
	VERTEX,	45.4514,	45.9378,	37.3399,	
# new facet 1/2
	VERTEX,	41.136,	44.732,	35.115,	
# new facet 1/2
	VERTEX,	41.5908,	44.7332,	35.8274,	
# new facet 2/2
	VERTEX,	45.4514,	45.9378,	37.3399,	
# new facet 2/2
	VERTEX,	41.136,	44.732,	35.115,	
# new facet 2/2
	VERTEX,	41.5908,	44.7332,	35.8274,	
# new facet 1/2
	VERTEX,	45.4514,	45.9378,	37.3399,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 1/2
	VERTEX,	41.136,	44.732,	35.115,	
# new facet 2/2
	VERTEX,	45.4514,	45.9378,	37.3399,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 2/2
	VERTEX,	41.136,	44.732,	35.115,	
# new facet 1/2
	VERTEX,	45.4514,	45.9378,	37.3399,	
# new facet 1/2
	VERTEX,	41.5908,	44.7332,	35.8274,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 2/2
	VERTEX,	45.4514,	45.9378,	37.3399,	
# new facet 2/2
	VERTEX,	41.5908,	44.7332,	35.8274,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 1/2
	VERTEX,	41.5908,	44.7332,	35.8274,	
# new facet 1/2
	VERTEX,	45.4514,	45.9378,	37.3399,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 2/2
	VERTEX,	41.5908,	44.7332,	35.8274,	
# new facet 2/2
	VERTEX,	45.4514,	45.9378,	37.3399,	
# new facet 1/2
	VERTEX,	43.0818,	42.5543,	36.7539,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 1/2
	VERTEX,	45.4514,	45.9378,	37.3399,	
# new facet 2/2
	VERTEX,	43.0818,	42.5543,	36.7539,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 2/2
	VERTEX,	45.4514,	45.9378,	37.3399,	
# new facet 1/2
	VERTEX,	43.0818,	42.5543,	36.7539,	
# new facet 1/2
	VERTEX,	41.5908,	44.7332,	35.8274,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 2/2
	VERTEX,	43.0818,	42.5543,	36.7539,	
# new facet 2/2
	VERTEX,	41.5908,	44.7332,	35.8274,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 1/2
	VERTEX,	43.0818,	42.5543,	36.7539,	
# new facet 1/2
	VERTEX,	45.4514,	45.9378,	37.3399,	
# new facet 1/2
	VERTEX,	41.5908,	44.7332,	35.8274,	
# new facet 2/2
	VERTEX,	43.0818,	42.5543,	36.7539,	
# new facet 2/2
	VERTEX,	45.4514,	45.9378,	37.3399,	
# new facet 2/2
	VERTEX,	41.5908,	44.7332,	35.8274,	
# new polyhedron
# new facet 1/2
	VERTEX,	47.454,	44.603,	26.246,	
# new facet 1/2
	VERTEX,	50.06,	46.018,	26.594,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 2/2
	VERTEX,	47.454,	44.603,	26.246,	
# new facet 2/2
	VERTEX,	50.06,	46.018,	26.594,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 1/2
	VERTEX,	46.7598,	46.2366,	27.1813,	
# new facet 1/2
	VERTEX,	47.454,	44.603,	26.246,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 2/2
	VERTEX,	46.7598,	46.2366,	27.1813,	
# new facet 2/2
	VERTEX,	47.454,	44.603,	26.246,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 1/2
	VERTEX,	46.7598,	46.2366,	27.1813,	
# new facet 1/2
	VERTEX,	50.06,	46.018,	26.594,	
# new facet 1/2
	VERTEX,	47.454,	44.603,	26.246,	
# new facet 2/2
	VERTEX,	46.7598,	46.2366,	27.1813,	
# new facet 2/2
	VERTEX,	50.06,	46.018,	26.594,	
# new facet 2/2
	VERTEX,	47.454,	44.603,	26.246,	
# new facet 1/2
	VERTEX,	46.7598,	46.2366,	27.1813,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 1/2
	VERTEX,	50.06,	46.018,	26.594,	
# new facet 2/2
	VERTEX,	46.7598,	46.2366,	27.1813,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 2/2
	VERTEX,	50.06,	46.018,	26.594,	
# new facet 1/2
	VERTEX,	47.454,	44.603,	26.246,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 1/2
	VERTEX,	46.7598,	46.2366,	27.1813,	
# new facet 2/2
	VERTEX,	47.454,	44.603,	26.246,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 2/2
	VERTEX,	46.7598,	46.2366,	27.1813,	
# new facet 1/2
	VERTEX,	46.6239,	48.9504,	28.5893,	
# new facet 1/2
	VERTEX,	47.454,	44.603,	26.246,	
# new facet 1/2
	VERTEX,	46.7598,	46.2366,	27.1813,	
# new facet 2/2
	VERTEX,	46.6239,	48.9504,	28.5893,	
# new facet 2/2
	VERTEX,	47.454,	44.603,	26.246,	
# new facet 2/2
	VERTEX,	46.7598,	46.2366,	27.1813,	
# new facet 1/2
	VERTEX,	46.6239,	48.9504,	28.5893,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 1/2
	VERTEX,	47.454,	44.603,	26.246,	
# new facet 2/2
	VERTEX,	46.6239,	48.9504,	28.5893,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 2/2
	VERTEX,	47.454,	44.603,	26.246,	
# new facet 1/2
	VERTEX,	46.6239,	48.9504,	28.5893,	
# new facet 1/2
	VERTEX,	46.7598,	46.2366,	27.1813,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 2/2
	VERTEX,	46.6239,	48.9504,	28.5893,	
# new facet 2/2
	VERTEX,	46.7598,	46.2366,	27.1813,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 1/2
	VERTEX,	46.7598,	46.2366,	27.1813,	
# new facet 1/2
	VERTEX,	46.6239,	48.9504,	28.5893,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 2/2
	VERTEX,	46.7598,	46.2366,	27.1813,	
# new facet 2/2
	VERTEX,	46.6239,	48.9504,	28.5893,	
# new facet 1/2
	VERTEX,	45.6865,	50.1177,	29.7054,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 1/2
	VERTEX,	46.6239,	48.9504,	28.5893,	
# new facet 2/2
	VERTEX,	45.6865,	50.1177,	29.7054,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 2/2
	VERTEX,	46.6239,	48.9504,	28.5893,	
# new facet 1/2
	VERTEX,	45.6865,	50.1177,	29.7054,	
# new facet 1/2
	VERTEX,	46.7598,	46.2366,	27.1813,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 2/2
	VERTEX,	45.6865,	50.1177,	29.7054,	
# new facet 2/2
	VERTEX,	46.7598,	46.2366,	27.1813,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.519,	
# new facet 1/2
	VERTEX,	45.6865,	50.1177,	29.7054,	
# new facet 1/2
	VERTEX,	46.6239,	48.9504,	28.5893,	
# new facet 1/2
	VERTEX,	46.7598,	46.2366,	27.1813,	
# new facet 2/2
	VERTEX,	45.6865,	50.1177,	29.7054,	
# new facet 2/2
	VERTEX,	46.6239,	48.9504,	28.5893,	
# new facet 2/2
	VERTEX,	46.7598,	46.2366,	27.1813,	
# new polyhedron
# new facet 1/2
	VERTEX,	43.391,	39.634,	35.379,	
# new facet 1/2
	VERTEX,	43.6331,	40.3697,	36.9864,	
# new facet 1/2
	VERTEX,	45.9435,	37.9879,	38.0411,	
# new facet 2/2
	VERTEX,	43.391,	39.634,	35.379,	
# new facet 2/2
	VERTEX,	43.6331,	40.3697,	36.9864,	
# new facet 2/2
	VERTEX,	45.9435,	37.9879,	38.0411,	
# new facet 1/2
	VERTEX,	44.6764,	42.9686,	37.3645,	
# new facet 1/2
	VERTEX,	43.391,	39.634,	35.379,	
# new facet 1/2
	VERTEX,	45.9435,	37.9879,	38.0411,	
# new facet 2/2
	VERTEX,	44.6764,	42.9686,	37.3645,	
# new facet 2/2
	VERTEX,	43.391,	39.634,	35.379,	
# new facet 2/2
	VERTEX,	45.9435,	37.9879,	38.0411,	
# new facet 1/2
	VERTEX,	44.6764,	42.9686,	37.3645,	
# new facet 1/2
	VERTEX,	43.6331,	40.3697,	36.9864,	
# new facet 1/2
	VERTEX,	43.391,	39.634,	35.379,	
# new facet 2/2
	VERTEX,	44.6764,	42.9686,	37.3645,	
# new facet 2/2
	VERTEX,	43.6331,	40.3697,	36.9864,	
# new facet 2/2
	VERTEX,	43.391,	39.634,	35.379,	
# new facet 1/2
	VERTEX,	44.6764,	42.9686,	37.3645,	
# new facet 1/2
	VERTEX,	45.9435,	37.9879,	38.0411,	
# new facet 1/2
	VERTEX,	43.6331,	40.3697,	36.9864,	
# new facet 2/2
	VERTEX,	44.6764,	42.9686,	37.3645,	
# new facet 2/2
	VERTEX,	45.9435,	37.9879,	38.0411,	
# new facet 2/2
	VERTEX,	43.6331,	40.3697,	36.9864,	
# new polyhedron
# new facet 1/2
	VERTEX,	46.793,	46.555,	37.108,	
# new facet 1/2
	VERTEX,	46.3857,	46.0756,	37.5474,	
# new facet 1/2
	VERTEX,	47.5201,	45.5895,	37.858,	
# new facet 2/2
	VERTEX,	46.793,	46.555,	37.108,	
# new facet 2/2
	VERTEX,	46.3857,	46.0756,	37.5474,	
# new facet 2/2
	VERTEX,	47.5201,	45.5895,	37.858,	
# new facet 1/2
	VERTEX,	48.7675,	38.2978,	35.2829,	
# new facet 1/2
	VERTEX,	46.793,	46.555,	37.108,	
# new facet 1/2
	VERTEX,	47.5201,	45.5895,	37.858,	
# new facet 2/2
	VERTEX,	48.7675,	38.2978,	35.2829,	
# new facet 2/2
	VERTEX,	46.793,	46.555,	37.108,	
# new facet 2/2
	VERTEX,	47.5201,	45.5895,	37.858,	
# new facet 1/2
	VERTEX,	48.7675,	38.2978,	35.2829,	
# new facet 1/2
	VERTEX,	46.3857,	46.0756,	37.5474,	
# new facet 1/2
	VERTEX,	46.793,	46.555,	37.108,	
# new facet 2/2
	VERTEX,	48.7675,	38.2978,	35.2829,	
# new facet 2/2
	VERTEX,	46.3857,	46.0756,	37.5474,	
# new facet 2/2
	VERTEX,	46.793,	46.555,	37.108,	
# new facet 1/2
	VERTEX,	48.7675,	38.2978,	35.2829,	
# new facet 1/2
	VERTEX,	47.5201,	45.5895,	37.858,	
# new facet 1/2
	VERTEX,	46.3857,	46.0756,	37.5474,	
# new facet 2/2
	VERTEX,	48.7675,	38.2978,	35.2829,	
# new facet 2/2
	VERTEX,	47.5201,	45.5895,	37.858,	
# new facet 2/2
	VERTEX,	46.3857,	46.0756,	37.5474,	
# new polyhedron
# new facet 1/2
	VERTEX,	43.38,	39.632,	35.358,	
# new facet 1/2
	VERTEX,	44.6786,	42.9782,	37.3644,	
# new facet 1/2
	VERTEX,	48.2611,	37.3048,	35.0395,	
# new facet 2/2
	VERTEX,	43.38,	39.632,	35.358,	
# new facet 2/2
	VERTEX,	44.6786,	42.9782,	37.3644,	
# new facet 2/2
	VERTEX,	48.2611,	37.3048,	35.0395,	
# new facet 1/2
	VERTEX,	46.783,	46.565,	37.098,	
# new facet 1/2
	VERTEX,	43.38,	39.632,	35.358,	
# new facet 1/2
	VERTEX,	48.2611,	37.3048,	35.0395,	
# new facet 2/2
	VERTEX,	46.783,	46.565,	37.098,	
# new facet 2/2
	VERTEX,	43.38,	39.632,	35.358,	
# new facet 2/2
	VERTEX,	48.2611,	37.3048,	35.0395,	
# new facet 1/2
	VERTEX,	46.783,	46.565,	37.098,	
# new facet 1/2
	VERTEX,	44.6786,	42.9782,	37.3644,	
# new facet 1/2
	VERTEX,	43.38,	39.632,	35.358,	
# new facet 2/2
	VERTEX,	46.783,	46.565,	37.098,	
# new facet 2/2
	VERTEX,	44.6786,	42.9782,	37.3644,	
# new facet 2/2
	VERTEX,	43.38,	39.632,	35.358,	
# new facet 1/2
	VERTEX,	46.783,	46.565,	37.098,	
# new facet 1/2
	VERTEX,	48.2611,	37.3048,	35.0395,	
# new facet 1/2
	VERTEX,	44.6786,	42.9782,	37.3644,	
# new facet 2/2
	VERTEX,	46.783,	46.565,	37.098,	
# new facet 2/2
	VERTEX,	48.2611,	37.3048,	35.0395,	
# new facet 2/2
	VERTEX,	44.6786,	42.9782,	37.3644,	
# new facet 1/2
	VERTEX,	46.783,	46.565,	37.098,	
# new facet 1/2
	VERTEX,	44.6786,	42.9782,	37.3644,	
# new facet 1/2
	VERTEX,	48.2611,	37.3048,	35.0395,	
# new facet 2/2
	VERTEX,	46.783,	46.565,	37.098,	
# new facet 2/2
	VERTEX,	44.6786,	42.9782,	37.3644,	
# new facet 2/2
	VERTEX,	48.2611,	37.3048,	35.0395,	
# new facet 1/2
	VERTEX,	46.4057,	46.0956,	37.5674,	
# new facet 1/2
	VERTEX,	46.783,	46.565,	37.098,	
# new facet 1/2
	VERTEX,	48.2611,	37.3048,	35.0395,	
# new facet 2/2
	VERTEX,	46.4057,	46.0956,	37.5674,	
# new facet 2/2
	VERTEX,	46.783,	46.565,	37.098,	
# new facet 2/2
	VERTEX,	48.2611,	37.3048,	35.0395,	
# new facet 1/2
	VERTEX,	46.4057,	46.0956,	37.5674,	
# new facet 1/2
	VERTEX,	44.6786,	42.9782,	37.3644,	
# new facet 1/2
	VERTEX,	46.783,	46.565,	37.098,	
# new facet 2/2
	VERTEX,	46.4057,	46.0956,	37.5674,	
# new facet 2/2
	VERTEX,	44.6786,	42.9782,	37.3644,	
# new facet 2/2
	VERTEX,	46.783,	46.565,	37.098,	
# new facet 1/2
	VERTEX,	46.4057,	46.0956,	37.5674,	
# new facet 1/2
	VERTEX,	48.2611,	37.3048,	35.0395,	
# new facet 1/2
	VERTEX,	44.6786,	42.9782,	37.3644,	
# new facet 2/2
	VERTEX,	46.4057,	46.0956,	37.5674,	
# new facet 2/2
	VERTEX,	48.2611,	37.3048,	35.0395,	
# new facet 2/2
	VERTEX,	44.6786,	42.9782,	37.3644,	
# new facet 1/2
	VERTEX,	46.783,	46.565,	37.098,	
# new facet 1/2
	VERTEX,	48.2611,	37.3048,	35.0395,	
# new facet 1/2
	VERTEX,	46.4057,	46.0956,	37.5674,	
# new facet 2/2
	VERTEX,	46.783,	46.565,	37.098,	
# new facet 2/2
	VERTEX,	48.2611,	37.3048,	35.0395,	
# new facet 2/2
	VERTEX,	46.4057,	46.0956,	37.5674,	
# new facet 1/2
	VERTEX,	48.7975,	38.3278,	35.3129,	
# new facet 1/2
	VERTEX,	46.783,	46.565,	37.098,	
# new facet 1/2
	VERTEX,	46.4057,	46.0956,	37.5674,	
# new facet 2/2
	VERTEX,	48.7975,	38.3278,	35.3129,	
# new facet 2/2
	VERTEX,	46.783,	46.565,	37.098,	
# new facet 2/2
	VERTEX,	46.4057,	46.0956,	37.5674,	
# new facet 1/2
	VERTEX,	48.7975,	38.3278,	35.3129,	
# new facet 1/2
	VERTEX,	48.2611,	37.3048,	35.0395,	
# new facet 1/2
	VERTEX,	46.783,	46.565,	37.098,	
# new facet 2/2
	VERTEX,	48.7975,	38.3278,	35.3129,	
# new facet 2/2
	VERTEX,	48.2611,	37.3048,	35.0395,	
# new facet 2/2
	VERTEX,	46.783,	46.565,	37.098,	
# new facet 1/2
	VERTEX,	48.7975,	38.3278,	35.3129,	
# new facet 1/2
	VERTEX,	46.4057,	46.0956,	37.5674,	
# new facet 1/2
	VERTEX,	48.2611,	37.3048,	35.0395,	
# new facet 2/2
	VERTEX,	48.7975,	38.3278,	35.3129,	
# new facet 2/2
	VERTEX,	46.4057,	46.0956,	37.5674,	
# new facet 2/2
	VERTEX,	48.2611,	37.3048,	35.0395,	
# new polyhedron
# new facet 1/2
	VERTEX,	43.39,	39.642,	35.368,	
# new facet 1/2
	VERTEX,	44.6786,	42.9782,	37.3644,	
# new facet 1/2
	VERTEX,	45.9441,	37.9879,	38.0413,	
# new facet 2/2
	VERTEX,	43.39,	39.642,	35.368,	
# new facet 2/2
	VERTEX,	44.6786,	42.9782,	37.3644,	
# new facet 2/2
	VERTEX,	45.9441,	37.9879,	38.0413,	
# new facet 1/2
	VERTEX,	48.2511,	37.2948,	35.0295,	
# new facet 1/2
	VERTEX,	43.39,	39.642,	35.368,	
# new facet 1/2
	VERTEX,	45.9441,	37.9879,	38.0413,	
# new facet 2/2
	VERTEX,	48.2511,	37.2948,	35.0295,	
# new facet 2/2
	VERTEX,	43.39,	39.642,	35.368,	
# new facet 2/2
	VERTEX,	45.9441,	37.9879,	38.0413,	
# new facet 1/2
	VERTEX,	48.2511,	37.2948,	35.0295,	
# new facet 1/2
	VERTEX,	44.6786,	42.9782,	37.3644,	
# new facet 1/2
	VERTEX,	43.39,	39.642,	35.368,	
# new facet 2/2
	VERTEX,	48.2511,	37.2948,	35.0295,	
# new facet 2/2
	VERTEX,	44.6786,	42.9782,	37.3644,	
# new facet 2/2
	VERTEX,	43.39,	39.642,	35.368,	
# new facet 1/2
	VERTEX,	48.2511,	37.2948,	35.0295,	
# new facet 1/2
	VERTEX,	45.9441,	37.9879,	38.0413,	
# new facet 1/2
	VERTEX,	44.6786,	42.9782,	37.3644,	
# new facet 2/2
	VERTEX,	48.2511,	37.2948,	35.0295,	
# new facet 2/2
	VERTEX,	45.9441,	37.9879,	38.0413,	
# new facet 2/2
	VERTEX,	44.6786,	42.9782,	37.3644,	
# new polyhedron
# new facet 1/2
	VERTEX,	47.949,	35.764,	30.354,	
# new facet 1/2
	VERTEX,	44.708,	33.774,	32.864,	
# new facet 1/2
	VERTEX,	42.288,	36.237,	28.659,	
# new facet 2/2
	VERTEX,	47.949,	35.764,	30.354,	
# new facet 2/2
	VERTEX,	44.708,	33.774,	32.864,	
# new facet 2/2
	VERTEX,	42.288,	36.237,	28.659,	
# new facet 1/2
	VERTEX,	47.9428,	35.6517,	30.2361,	
# new facet 1/2
	VERTEX,	47.949,	35.764,	30.354,	
# new facet 1/2
	VERTEX,	42.288,	36.237,	28.659,	
# new facet 2/2
	VERTEX,	47.9428,	35.6517,	30.2361,	
# new facet 2/2
	VERTEX,	47.949,	35.764,	30.354,	
# new facet 2/2
	VERTEX,	42.288,	36.237,	28.659,	
# new facet 1/2
	VERTEX,	47.9428,	35.6517,	30.2361,	
# new facet 1/2
	VERTEX,	44.708,	33.774,	32.864,	
# new facet 1/2
	VERTEX,	47.949,	35.764,	30.354,	
# new facet 2/2
	VERTEX,	47.9428,	35.6517,	30.2361,	
# new facet 2/2
	VERTEX,	44.708,	33.774,	32.864,	
# new facet 2/2
	VERTEX,	47.949,	35.764,	30.354,	
# new facet 1/2
	VERTEX,	47.9428,	35.6517,	30.2361,	
# new facet 1/2
	VERTEX,	42.288,	36.237,	28.659,	
# new facet 1/2
	VERTEX,	44.708,	33.774,	32.864,	
# new facet 2/2
	VERTEX,	47.9428,	35.6517,	30.2361,	
# new facet 2/2
	VERTEX,	42.288,	36.237,	28.659,	
# new facet 2/2
	VERTEX,	44.708,	33.774,	32.864,	
# new facet 1/2
	VERTEX,	47.949,	35.764,	30.354,	
# new facet 1/2
	VERTEX,	42.288,	36.237,	28.659,	
# new facet 1/2
	VERTEX,	47.9428,	35.6517,	30.2361,	
# new facet 2/2
	VERTEX,	47.949,	35.764,	30.354,	
# new facet 2/2
	VERTEX,	42.288,	36.237,	28.659,	
# new facet 2/2
	VERTEX,	47.9428,	35.6517,	30.2361,	
# new facet 1/2
	VERTEX,	46.482,	33.7646,	30.1521,	
# new facet 1/2
	VERTEX,	47.949,	35.764,	30.354,	
# new facet 1/2
	VERTEX,	47.9428,	35.6517,	30.2361,	
# new facet 2/2
	VERTEX,	46.482,	33.7646,	30.1521,	
# new facet 2/2
	VERTEX,	47.949,	35.764,	30.354,	
# new facet 2/2
	VERTEX,	47.9428,	35.6517,	30.2361,	
# new facet 1/2
	VERTEX,	46.482,	33.7646,	30.1521,	
# new facet 1/2
	VERTEX,	42.288,	36.237,	28.659,	
# new facet 1/2
	VERTEX,	47.949,	35.764,	30.354,	
# new facet 2/2
	VERTEX,	46.482,	33.7646,	30.1521,	
# new facet 2/2
	VERTEX,	42.288,	36.237,	28.659,	
# new facet 2/2
	VERTEX,	47.949,	35.764,	30.354,	
# new facet 1/2
	VERTEX,	46.482,	33.7646,	30.1521,	
# new facet 1/2
	VERTEX,	47.9428,	35.6517,	30.2361,	
# new facet 1/2
	VERTEX,	42.288,	36.237,	28.659,	
# new facet 2/2
	VERTEX,	46.482,	33.7646,	30.1521,	
# new facet 2/2
	VERTEX,	47.9428,	35.6517,	30.2361,	
# new facet 2/2
	VERTEX,	42.288,	36.237,	28.659,	
# new facet 1/2
	VERTEX,	42.288,	36.237,	28.659,	
# new facet 1/2
	VERTEX,	47.9428,	35.6517,	30.2361,	
# new facet 1/2
	VERTEX,	46.482,	33.7646,	30.1521,	
# new facet 2/2
	VERTEX,	42.288,	36.237,	28.659,	
# new facet 2/2
	VERTEX,	47.9428,	35.6517,	30.2361,	
# new facet 2/2
	VERTEX,	46.482,	33.7646,	30.1521,	
# new facet 1/2
	VERTEX,	45.3658,	34.8458,	28.4406,	
# new facet 1/2
	VERTEX,	42.288,	36.237,	28.659,	
# new facet 1/2
	VERTEX,	46.482,	33.7646,	30.1521,	
# new facet 2/2
	VERTEX,	45.3658,	34.8458,	28.4406,	
# new facet 2/2
	VERTEX,	42.288,	36.237,	28.659,	
# new facet 2/2
	VERTEX,	46.482,	33.7646,	30.1521,	
# new facet 1/2
	VERTEX,	45.3658,	34.8458,	28.4406,	
# new facet 1/2
	VERTEX,	47.9428,	35.6517,	30.2361,	
# new facet 1/2
	VERTEX,	42.288,	36.237,	28.659,	
# new facet 2/2
	VERTEX,	45.3658,	34.8458,	28.4406,	
# new facet 2/2
	VERTEX,	47.9428,	35.6517,	30.2361,	
# new facet 2/2
	VERTEX,	42.288,	36.237,	28.659,	
# new facet 1/2
	VERTEX,	45.3658,	34.8458,	28.4406,	
# new facet 1/2
	VERTEX,	46.482,	33.7646,	30.1521,	
# new facet 1/2
	VERTEX,	47.9428,	35.6517,	30.2361,	
# new facet 2/2
	VERTEX,	45.3658,	34.8458,	28.4406,	
# new facet 2/2
	VERTEX,	46.482,	33.7646,	30.1521,	
# new facet 2/2
	VERTEX,	47.9428,	35.6517,	30.2361,	
# new polyhedron
# new facet 1/2
	VERTEX,	50.95,	39.887,	30.67,	
# new facet 1/2
	VERTEX,	50.3244,	38.8633,	32.1508,	
# new facet 1/2
	VERTEX,	52.3202,	41.6391,	31.7002,	
# new facet 2/2
	VERTEX,	50.95,	39.887,	30.67,	
# new facet 2/2
	VERTEX,	50.3244,	38.8633,	32.1508,	
# new facet 2/2
	VERTEX,	52.3202,	41.6391,	31.7002,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 1/2
	VERTEX,	50.95,	39.887,	30.67,	
# new facet 1/2
	VERTEX,	52.3202,	41.6391,	31.7002,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 2/2
	VERTEX,	50.95,	39.887,	30.67,	
# new facet 2/2
	VERTEX,	52.3202,	41.6391,	31.7002,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 1/2
	VERTEX,	50.3244,	38.8633,	32.1508,	
# new facet 1/2
	VERTEX,	50.95,	39.887,	30.67,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 2/2
	VERTEX,	50.3244,	38.8633,	32.1508,	
# new facet 2/2
	VERTEX,	50.95,	39.887,	30.67,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 1/2
	VERTEX,	52.3202,	41.6391,	31.7002,	
# new facet 1/2
	VERTEX,	50.3244,	38.8633,	32.1508,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 2/2
	VERTEX,	52.3202,	41.6391,	31.7002,	
# new facet 2/2
	VERTEX,	50.3244,	38.8633,	32.1508,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 1/2
	VERTEX,	50.3244,	38.8633,	32.1508,	
# new facet 1/2
	VERTEX,	52.3202,	41.6391,	31.7002,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 2/2
	VERTEX,	50.3244,	38.8633,	32.1508,	
# new facet 2/2
	VERTEX,	52.3202,	41.6391,	31.7002,	
# new facet 1/2
	VERTEX,	48.2711,	37.3148,	35.0495,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 1/2
	VERTEX,	52.3202,	41.6391,	31.7002,	
# new facet 2/2
	VERTEX,	48.2711,	37.3148,	35.0495,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 2/2
	VERTEX,	52.3202,	41.6391,	31.7002,	
# new facet 1/2
	VERTEX,	48.2711,	37.3148,	35.0495,	
# new facet 1/2
	VERTEX,	50.3244,	38.8633,	32.1508,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 2/2
	VERTEX,	48.2711,	37.3148,	35.0495,	
# new facet 2/2
	VERTEX,	50.3244,	38.8633,	32.1508,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 1/2
	VERTEX,	48.2711,	37.3148,	35.0495,	
# new facet 1/2
	VERTEX,	52.3202,	41.6391,	31.7002,	
# new facet 1/2
	VERTEX,	50.3244,	38.8633,	32.1508,	
# new facet 2/2
	VERTEX,	48.2711,	37.3148,	35.0495,	
# new facet 2/2
	VERTEX,	52.3202,	41.6391,	31.7002,	
# new facet 2/2
	VERTEX,	50.3244,	38.8633,	32.1508,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 1/2
	VERTEX,	52.3202,	41.6391,	31.7002,	
# new facet 1/2
	VERTEX,	48.2711,	37.3148,	35.0495,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 2/2
	VERTEX,	52.3202,	41.6391,	31.7002,	
# new facet 2/2
	VERTEX,	48.2711,	37.3148,	35.0495,	
# new facet 1/2
	VERTEX,	52.3114,	41.6903,	31.7733,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 1/2
	VERTEX,	48.2711,	37.3148,	35.0495,	
# new facet 2/2
	VERTEX,	52.3114,	41.6903,	31.7733,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 2/2
	VERTEX,	48.2711,	37.3148,	35.0495,	
# new facet 1/2
	VERTEX,	52.3114,	41.6903,	31.7733,	
# new facet 1/2
	VERTEX,	52.3202,	41.6391,	31.7002,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 2/2
	VERTEX,	52.3114,	41.6903,	31.7733,	
# new facet 2/2
	VERTEX,	52.3202,	41.6391,	31.7002,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 1/2
	VERTEX,	52.3114,	41.6903,	31.7733,	
# new facet 1/2
	VERTEX,	48.2711,	37.3148,	35.0495,	
# new facet 1/2
	VERTEX,	52.3202,	41.6391,	31.7002,	
# new facet 2/2
	VERTEX,	52.3114,	41.6903,	31.7733,	
# new facet 2/2
	VERTEX,	48.2711,	37.3148,	35.0495,	
# new facet 2/2
	VERTEX,	52.3202,	41.6391,	31.7002,	
# new polyhedron
# new facet 1/2
	VERTEX,	52.625,	47.818,	31.493,	
# new facet 1/2
	VERTEX,	52.8118,	47.9768,	31.3016,	
# new facet 1/2
	VERTEX,	49.8966,	47.5597,	26.0357,	
# new facet 2/2
	VERTEX,	52.625,	47.818,	31.493,	
# new facet 2/2
	VERTEX,	52.8118,	47.9768,	31.3016,	
# new facet 2/2
	VERTEX,	49.8966,	47.5597,	26.0357,	
# new facet 1/2
	VERTEX,	49.656,	51.427,	30.402,	
# new facet 1/2
	VERTEX,	52.625,	47.818,	31.493,	
# new facet 1/2
	VERTEX,	49.8966,	47.5597,	26.0357,	
# new facet 2/2
	VERTEX,	49.656,	51.427,	30.402,	
# new facet 2/2
	VERTEX,	52.625,	47.818,	31.493,	
# new facet 2/2
	VERTEX,	49.8966,	47.5597,	26.0357,	
# new facet 1/2
	VERTEX,	49.656,	51.427,	30.402,	
# new facet 1/2
	VERTEX,	52.8118,	47.9768,	31.3016,	
# new facet 1/2
	VERTEX,	52.625,	47.818,	31.493,	
# new facet 2/2
	VERTEX,	49.656,	51.427,	30.402,	
# new facet 2/2
	VERTEX,	52.8118,	47.9768,	31.3016,	
# new facet 2/2
	VERTEX,	52.625,	47.818,	31.493,	
# new facet 1/2
	VERTEX,	49.656,	51.427,	30.402,	
# new facet 1/2
	VERTEX,	49.8966,	47.5597,	26.0357,	
# new facet 1/2
	VERTEX,	52.8118,	47.9768,	31.3016,	
# new facet 2/2
	VERTEX,	49.656,	51.427,	30.402,	
# new facet 2/2
	VERTEX,	49.8966,	47.5597,	26.0357,	
# new facet 2/2
	VERTEX,	52.8118,	47.9768,	31.3016,	
# new facet 1/2
	VERTEX,	49.656,	51.427,	30.402,	
# new facet 1/2
	VERTEX,	52.8118,	47.9768,	31.3016,	
# new facet 1/2
	VERTEX,	49.8966,	47.5597,	26.0357,	
# new facet 2/2
	VERTEX,	49.656,	51.427,	30.402,	
# new facet 2/2
	VERTEX,	52.8118,	47.9768,	31.3016,	
# new facet 2/2
	VERTEX,	49.8966,	47.5597,	26.0357,	
# new facet 1/2
	VERTEX,	53.5601,	50.466,	29.1274,	
# new facet 1/2
	VERTEX,	49.656,	51.427,	30.402,	
# new facet 1/2
	VERTEX,	49.8966,	47.5597,	26.0357,	
# new facet 2/2
	VERTEX,	53.5601,	50.466,	29.1274,	
# new facet 2/2
	VERTEX,	49.656,	51.427,	30.402,	
# new facet 2/2
	VERTEX,	49.8966,	47.5597,	26.0357,	
# new facet 1/2
	VERTEX,	53.5601,	50.466,	29.1274,	
# new facet 1/2
	VERTEX,	52.8118,	47.9768,	31.3016,	
# new facet 1/2
	VERTEX,	49.656,	51.427,	30.402,	
# new facet 2/2
	VERTEX,	53.5601,	50.466,	29.1274,	
# new facet 2/2
	VERTEX,	52.8118,	47.9768,	31.3016,	
# new facet 2/2
	VERTEX,	49.656,	51.427,	30.402,	
# new facet 1/2
	VERTEX,	53.5601,	50.466,	29.1274,	
# new facet 1/2
	VERTEX,	49.8966,	47.5597,	26.0357,	
# new facet 1/2
	VERTEX,	52.8118,	47.9768,	31.3016,	
# new facet 2/2
	VERTEX,	53.5601,	50.466,	29.1274,	
# new facet 2/2
	VERTEX,	49.8966,	47.5597,	26.0357,	
# new facet 2/2
	VERTEX,	52.8118,	47.9768,	31.3016,	
# new facet 1/2
	VERTEX,	49.656,	51.427,	30.402,	
# new facet 1/2
	VERTEX,	49.8966,	47.5597,	26.0357,	
# new facet 1/2
	VERTEX,	53.5601,	50.466,	29.1274,	
# new facet 2/2
	VERTEX,	49.656,	51.427,	30.402,	
# new facet 2/2
	VERTEX,	49.8966,	47.5597,	26.0357,	
# new facet 2/2
	VERTEX,	53.5601,	50.466,	29.1274,	
# new facet 1/2
	VERTEX,	49.8399,	47.8279,	26.2203,	
# new facet 1/2
	VERTEX,	49.656,	51.427,	30.402,	
# new facet 1/2
	VERTEX,	53.5601,	50.466,	29.1274,	
# new facet 2/2
	VERTEX,	49.8399,	47.8279,	26.2203,	
# new facet 2/2
	VERTEX,	49.656,	51.427,	30.402,	
# new facet 2/2
	VERTEX,	53.5601,	50.466,	29.1274,	
# new facet 1/2
	VERTEX,	49.8399,	47.8279,	26.2203,	
# new facet 1/2
	VERTEX,	49.8966,	47.5597,	26.0357,	
# new facet 1/2
	VERTEX,	49.656,	51.427,	30.402,	
# new facet 2/2
	VERTEX,	49.8399,	47.8279,	26.2203,	
# new facet 2/2
	VERTEX,	49.8966,	47.5597,	26.0357,	
# new facet 2/2
	VERTEX,	49.656,	51.427,	30.402,	
# new facet 1/2
	VERTEX,	49.8399,	47.8279,	26.2203,	
# new facet 1/2
	VERTEX,	53.5601,	50.466,	29.1274,	
# new facet 1/2
	VERTEX,	49.8966,	47.5597,	26.0357,	
# new facet 2/2
	VERTEX,	49.8399,	47.8279,	26.2203,	
# new facet 2/2
	VERTEX,	53.5601,	50.466,	29.1274,	
# new facet 2/2
	VERTEX,	49.8966,	47.5597,	26.0357,	
# new polyhedron
# new facet 1/2
	VERTEX,	46.783,	46.545,	37.098,	
# new facet 1/2
	VERTEX,	51.669,	44.1228,	33.6088,	
# new facet 1/2
	VERTEX,	52.2824,	41.7497,	31.7985,	
# new facet 2/2
	VERTEX,	46.783,	46.545,	37.098,	
# new facet 2/2
	VERTEX,	51.669,	44.1228,	33.6088,	
# new facet 2/2
	VERTEX,	52.2824,	41.7497,	31.7985,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 1/2
	VERTEX,	46.783,	46.545,	37.098,	
# new facet 1/2
	VERTEX,	52.2824,	41.7497,	31.7985,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 2/2
	VERTEX,	46.783,	46.545,	37.098,	
# new facet 2/2
	VERTEX,	52.2824,	41.7497,	31.7985,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 1/2
	VERTEX,	51.669,	44.1228,	33.6088,	
# new facet 1/2
	VERTEX,	46.783,	46.545,	37.098,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 2/2
	VERTEX,	51.669,	44.1228,	33.6088,	
# new facet 2/2
	VERTEX,	46.783,	46.545,	37.098,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 1/2
	VERTEX,	52.2824,	41.7497,	31.7985,	
# new facet 1/2
	VERTEX,	51.669,	44.1228,	33.6088,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 2/2
	VERTEX,	52.2824,	41.7497,	31.7985,	
# new facet 2/2
	VERTEX,	51.669,	44.1228,	33.6088,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 1/2
	VERTEX,	51.669,	44.1228,	33.6088,	
# new facet 1/2
	VERTEX,	52.2824,	41.7497,	31.7985,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 2/2
	VERTEX,	51.669,	44.1228,	33.6088,	
# new facet 2/2
	VERTEX,	52.2824,	41.7497,	31.7985,	
# new facet 1/2
	VERTEX,	52.7396,	47.3751,	31.6075,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 1/2
	VERTEX,	52.2824,	41.7497,	31.7985,	
# new facet 2/2
	VERTEX,	52.7396,	47.3751,	31.6075,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 2/2
	VERTEX,	52.2824,	41.7497,	31.7985,	
# new facet 1/2
	VERTEX,	52.7396,	47.3751,	31.6075,	
# new facet 1/2
	VERTEX,	51.669,	44.1228,	33.6088,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 2/2
	VERTEX,	52.7396,	47.3751,	31.6075,	
# new facet 2/2
	VERTEX,	51.669,	44.1228,	33.6088,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 1/2
	VERTEX,	52.7396,	47.3751,	31.6075,	
# new facet 1/2
	VERTEX,	52.2824,	41.7497,	31.7985,	
# new facet 1/2
	VERTEX,	51.669,	44.1228,	33.6088,	
# new facet 2/2
	VERTEX,	52.7396,	47.3751,	31.6075,	
# new facet 2/2
	VERTEX,	52.2824,	41.7497,	31.7985,	
# new facet 2/2
	VERTEX,	51.669,	44.1228,	33.6088,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 1/2
	VERTEX,	52.2824,	41.7497,	31.7985,	
# new facet 1/2
	VERTEX,	52.7396,	47.3751,	31.6075,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 2/2
	VERTEX,	52.2824,	41.7497,	31.7985,	
# new facet 2/2
	VERTEX,	52.7396,	47.3751,	31.6075,	
# new facet 1/2
	VERTEX,	52.3831,	41.8582,	31.7418,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 1/2
	VERTEX,	52.7396,	47.3751,	31.6075,	
# new facet 2/2
	VERTEX,	52.3831,	41.8582,	31.7418,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 2/2
	VERTEX,	52.7396,	47.3751,	31.6075,	
# new facet 1/2
	VERTEX,	52.3831,	41.8582,	31.7418,	
# new facet 1/2
	VERTEX,	52.2824,	41.7497,	31.7985,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 2/2
	VERTEX,	52.3831,	41.8582,	31.7418,	
# new facet 2/2
	VERTEX,	52.2824,	41.7497,	31.7985,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 1/2
	VERTEX,	52.3831,	41.8582,	31.7418,	
# new facet 1/2
	VERTEX,	52.7396,	47.3751,	31.6075,	
# new facet 1/2
	VERTEX,	52.2824,	41.7497,	31.7985,	
# new facet 2/2
	VERTEX,	52.3831,	41.8582,	31.7418,	
# new facet 2/2
	VERTEX,	52.7396,	47.3751,	31.6075,	
# new facet 2/2
	VERTEX,	52.2824,	41.7497,	31.7985,	
# new polyhedron
# new facet 1/2
	VERTEX,	43.384,	39.619,	35.359,	
# new facet 1/2
	VERTEX,	47.6238,	35.9742,	33.8464,	
# new facet 1/2
	VERTEX,	48.2601,	37.3036,	35.0398,	
# new facet 2/2
	VERTEX,	43.384,	39.619,	35.359,	
# new facet 2/2
	VERTEX,	47.6238,	35.9742,	33.8464,	
# new facet 2/2
	VERTEX,	48.2601,	37.3036,	35.0398,	
# new facet 1/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 1/2
	VERTEX,	43.384,	39.619,	35.359,	
# new facet 1/2
	VERTEX,	48.2601,	37.3036,	35.0398,	
# new facet 2/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 2/2
	VERTEX,	43.384,	39.619,	35.359,	
# new facet 2/2
	VERTEX,	48.2601,	37.3036,	35.0398,	
# new facet 1/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 1/2
	VERTEX,	47.6238,	35.9742,	33.8464,	
# new facet 1/2
	VERTEX,	43.384,	39.619,	35.359,	
# new facet 2/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 2/2
	VERTEX,	47.6238,	35.9742,	33.8464,	
# new facet 2/2
	VERTEX,	43.384,	39.619,	35.359,	
# new facet 1/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 1/2
	VERTEX,	48.2601,	37.3036,	35.0398,	
# new facet 1/2
	VERTEX,	47.6238,	35.9742,	33.8464,	
# new facet 2/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 2/2
	VERTEX,	48.2601,	37.3036,	35.0398,	
# new facet 2/2
	VERTEX,	47.6238,	35.9742,	33.8464,	
# new facet 1/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 1/2
	VERTEX,	47.6238,	35.9742,	33.8464,	
# new facet 1/2
	VERTEX,	48.2601,	37.3036,	35.0398,	
# new facet 2/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 2/2
	VERTEX,	47.6238,	35.9742,	33.8464,	
# new facet 2/2
	VERTEX,	48.2601,	37.3036,	35.0398,	
# new facet 1/2
	VERTEX,	48.0771,	36.4114,	33.4819,	
# new facet 1/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 1/2
	VERTEX,	48.2601,	37.3036,	35.0398,	
# new facet 2/2
	VERTEX,	48.0771,	36.4114,	33.4819,	
# new facet 2/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 2/2
	VERTEX,	48.2601,	37.3036,	35.0398,	
# new facet 1/2
	VERTEX,	48.0771,	36.4114,	33.4819,	
# new facet 1/2
	VERTEX,	47.6238,	35.9742,	33.8464,	
# new facet 1/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 2/2
	VERTEX,	48.0771,	36.4114,	33.4819,	
# new facet 2/2
	VERTEX,	47.6238,	35.9742,	33.8464,	
# new facet 2/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 1/2
	VERTEX,	48.0771,	36.4114,	33.4819,	
# new facet 1/2
	VERTEX,	48.2601,	37.3036,	35.0398,	
# new facet 1/2
	VERTEX,	47.6238,	35.9742,	33.8464,	
# new facet 2/2
	VERTEX,	48.0771,	36.4114,	33.4819,	
# new facet 2/2
	VERTEX,	48.2601,	37.3036,	35.0398,	
# new facet 2/2
	VERTEX,	47.6238,	35.9742,	33.8464,	
# new facet 1/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 1/2
	VERTEX,	48.2601,	37.3036,	35.0398,	
# new facet 1/2
	VERTEX,	48.0771,	36.4114,	33.4819,	
# new facet 2/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 2/2
	VERTEX,	48.2601,	37.3036,	35.0398,	
# new facet 2/2
	VERTEX,	48.0771,	36.4114,	33.4819,	
# new facet 1/2
	VERTEX,	50.3544,	38.8933,	32.1808,	
# new facet 1/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 1/2
	VERTEX,	48.0771,	36.4114,	33.4819,	
# new facet 2/2
	VERTEX,	50.3544,	38.8933,	32.1808,	
# new facet 2/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 2/2
	VERTEX,	48.0771,	36.4114,	33.4819,	
# new facet 1/2
	VERTEX,	50.3544,	38.8933,	32.1808,	
# new facet 1/2
	VERTEX,	48.2601,	37.3036,	35.0398,	
# new facet 1/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 2/2
	VERTEX,	50.3544,	38.8933,	32.1808,	
# new facet 2/2
	VERTEX,	48.2601,	37.3036,	35.0398,	
# new facet 2/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 1/2
	VERTEX,	50.3544,	38.8933,	32.1808,	
# new facet 1/2
	VERTEX,	48.0771,	36.4114,	33.4819,	
# new facet 1/2
	VERTEX,	48.2601,	37.3036,	35.0398,	
# new facet 2/2
	VERTEX,	50.3544,	38.8933,	32.1808,	
# new facet 2/2
	VERTEX,	48.0771,	36.4114,	33.4819,	
# new facet 2/2
	VERTEX,	48.2601,	37.3036,	35.0398,	
# new polyhedron
# new facet 1/2
	VERTEX,	43.384,	39.619,	35.359,	
# new facet 1/2
	VERTEX,	48.5055,	36.4726,	30.2083,	
# new facet 1/2
	VERTEX,	47.6338,	35.9842,	33.8564,	
# new facet 2/2
	VERTEX,	43.384,	39.619,	35.359,	
# new facet 2/2
	VERTEX,	48.5055,	36.4726,	30.2083,	
# new facet 2/2
	VERTEX,	47.6338,	35.9842,	33.8564,	
# new facet 1/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 1/2
	VERTEX,	43.384,	39.619,	35.359,	
# new facet 1/2
	VERTEX,	47.6338,	35.9842,	33.8564,	
# new facet 2/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 2/2
	VERTEX,	43.384,	39.619,	35.359,	
# new facet 2/2
	VERTEX,	47.6338,	35.9842,	33.8564,	
# new facet 1/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 1/2
	VERTEX,	48.5055,	36.4726,	30.2083,	
# new facet 1/2
	VERTEX,	43.384,	39.619,	35.359,	
# new facet 2/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 2/2
	VERTEX,	48.5055,	36.4726,	30.2083,	
# new facet 2/2
	VERTEX,	43.384,	39.619,	35.359,	
# new facet 1/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 1/2
	VERTEX,	47.6338,	35.9842,	33.8564,	
# new facet 1/2
	VERTEX,	48.5055,	36.4726,	30.2083,	
# new facet 2/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 2/2
	VERTEX,	47.6338,	35.9842,	33.8564,	
# new facet 2/2
	VERTEX,	48.5055,	36.4726,	30.2083,	
# new facet 1/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 1/2
	VERTEX,	48.5055,	36.4726,	30.2083,	
# new facet 1/2
	VERTEX,	47.6338,	35.9842,	33.8564,	
# new facet 2/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 2/2
	VERTEX,	48.5055,	36.4726,	30.2083,	
# new facet 2/2
	VERTEX,	47.6338,	35.9842,	33.8564,	
# new facet 1/2
	VERTEX,	49.7995,	38.0702,	30.3538,	
# new facet 1/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 1/2
	VERTEX,	47.6338,	35.9842,	33.8564,	
# new facet 2/2
	VERTEX,	49.7995,	38.0702,	30.3538,	
# new facet 2/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 2/2
	VERTEX,	47.6338,	35.9842,	33.8564,	
# new facet 1/2
	VERTEX,	49.7995,	38.0702,	30.3538,	
# new facet 1/2
	VERTEX,	48.5055,	36.4726,	30.2083,	
# new facet 1/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 2/2
	VERTEX,	49.7995,	38.0702,	30.3538,	
# new facet 2/2
	VERTEX,	48.5055,	36.4726,	30.2083,	
# new facet 2/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 1/2
	VERTEX,	49.7995,	38.0702,	30.3538,	
# new facet 1/2
	VERTEX,	47.6338,	35.9842,	33.8564,	
# new facet 1/2
	VERTEX,	48.5055,	36.4726,	30.2083,	
# new facet 2/2
	VERTEX,	49.7995,	38.0702,	30.3538,	
# new facet 2/2
	VERTEX,	47.6338,	35.9842,	33.8564,	
# new facet 2/2
	VERTEX,	48.5055,	36.4726,	30.2083,	
# new facet 1/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 1/2
	VERTEX,	47.6338,	35.9842,	33.8564,	
# new facet 1/2
	VERTEX,	49.7995,	38.0702,	30.3538,	
# new facet 2/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 2/2
	VERTEX,	47.6338,	35.9842,	33.8564,	
# new facet 2/2
	VERTEX,	49.7995,	38.0702,	30.3538,	
# new facet 1/2
	VERTEX,	48.0871,	36.4214,	33.4919,	
# new facet 1/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 1/2
	VERTEX,	49.7995,	38.0702,	30.3538,	
# new facet 2/2
	VERTEX,	48.0871,	36.4214,	33.4919,	
# new facet 2/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 2/2
	VERTEX,	49.7995,	38.0702,	30.3538,	
# new facet 1/2
	VERTEX,	48.0871,	36.4214,	33.4919,	
# new facet 1/2
	VERTEX,	47.6338,	35.9842,	33.8564,	
# new facet 1/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 2/2
	VERTEX,	48.0871,	36.4214,	33.4919,	
# new facet 2/2
	VERTEX,	47.6338,	35.9842,	33.8564,	
# new facet 2/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 1/2
	VERTEX,	48.0871,	36.4214,	33.4919,	
# new facet 1/2
	VERTEX,	49.7995,	38.0702,	30.3538,	
# new facet 1/2
	VERTEX,	47.6338,	35.9842,	33.8564,	
# new facet 2/2
	VERTEX,	48.0871,	36.4214,	33.4919,	
# new facet 2/2
	VERTEX,	49.7995,	38.0702,	30.3538,	
# new facet 2/2
	VERTEX,	47.6338,	35.9842,	33.8564,	
# new polyhedron
# new facet 1/2
	VERTEX,	52.62,	47.813,	31.499,	
# new facet 1/2
	VERTEX,	49.646,	51.416,	30.413,	
# new facet 1/2
	VERTEX,	46.074,	48.601,	36.011,	
# new facet 2/2
	VERTEX,	52.62,	47.813,	31.499,	
# new facet 2/2
	VERTEX,	49.646,	51.416,	30.413,	
# new facet 2/2
	VERTEX,	46.074,	48.601,	36.011,	
# new facet 1/2
	VERTEX,	45.6665,	50.0977,	29.6854,	
# new facet 1/2
	VERTEX,	52.62,	47.813,	31.499,	
# new facet 1/2
	VERTEX,	46.074,	48.601,	36.011,	
# new facet 2/2
	VERTEX,	45.6665,	50.0977,	29.6854,	
# new facet 2/2
	VERTEX,	52.62,	47.813,	31.499,	
# new facet 2/2
	VERTEX,	46.074,	48.601,	36.011,	
# new facet 1/2
	VERTEX,	45.6665,	50.0977,	29.6854,	
# new facet 1/2
	VERTEX,	49.646,	51.416,	30.413,	
# new facet 1/2
	VERTEX,	52.62,	47.813,	31.499,	
# new facet 2/2
	VERTEX,	45.6665,	50.0977,	29.6854,	
# new facet 2/2
	VERTEX,	49.646,	51.416,	30.413,	
# new facet 2/2
	VERTEX,	52.62,	47.813,	31.499,	
# new facet 1/2
	VERTEX,	45.6665,	50.0977,	29.6854,	
# new facet 1/2
	VERTEX,	46.074,	48.601,	36.011,	
# new facet 1/2
	VERTEX,	49.646,	51.416,	30.413,	
# new facet 2/2
	VERTEX,	45.6665,	50.0977,	29.6854,	
# new facet 2/2
	VERTEX,	46.074,	48.601,	36.011,	
# new facet 2/2
	VERTEX,	49.646,	51.416,	30.413,	
# new facet 1/2
	VERTEX,	52.62,	47.813,	31.499,	
# new facet 1/2
	VERTEX,	46.074,	48.601,	36.011,	
# new facet 1/2
	VERTEX,	45.6665,	50.0977,	29.6854,	
# new facet 2/2
	VERTEX,	52.62,	47.813,	31.499,	
# new facet 2/2
	VERTEX,	46.074,	48.601,	36.011,	
# new facet 2/2
	VERTEX,	45.6665,	50.0977,	29.6854,	
# new facet 1/2
	VERTEX,	46.0251,	50.568,	29.7192,	
# new facet 1/2
	VERTEX,	52.62,	47.813,	31.499,	
# new facet 1/2
	VERTEX,	45.6665,	50.0977,	29.6854,	
# new facet 2/2
	VERTEX,	46.0251,	50.568,	29.7192,	
# new facet 2/2
	VERTEX,	52.62,	47.813,	31.499,	
# new facet 2/2
	VERTEX,	45.6665,	50.0977,	29.6854,	
# new facet 1/2
	VERTEX,	46.0251,	50.568,	29.7192,	
# new facet 1/2
	VERTEX,	46.074,	48.601,	36.011,	
# new facet 1/2
	VERTEX,	52.62,	47.813,	31.499,	
# new facet 2/2
	VERTEX,	46.0251,	50.568,	29.7192,	
# new facet 2/2
	VERTEX,	46.074,	48.601,	36.011,	
# new facet 2/2
	VERTEX,	52.62,	47.813,	31.499,	
# new facet 1/2
	VERTEX,	46.0251,	50.568,	29.7192,	
# new facet 1/2
	VERTEX,	45.6665,	50.0977,	29.6854,	
# new facet 1/2
	VERTEX,	46.074,	48.601,	36.011,	
# new facet 2/2
	VERTEX,	46.0251,	50.568,	29.7192,	
# new facet 2/2
	VERTEX,	45.6665,	50.0977,	29.6854,	
# new facet 2/2
	VERTEX,	46.074,	48.601,	36.011,	
# new facet 1/2
	VERTEX,	46.074,	48.601,	36.011,	
# new facet 1/2
	VERTEX,	45.6665,	50.0977,	29.6854,	
# new facet 1/2
	VERTEX,	46.0251,	50.568,	29.7192,	
# new facet 2/2
	VERTEX,	46.074,	48.601,	36.011,	
# new facet 2/2
	VERTEX,	45.6665,	50.0977,	29.6854,	
# new facet 2/2
	VERTEX,	46.0251,	50.568,	29.7192,	
# new facet 1/2
	VERTEX,	45.1017,	50.1928,	30.0775,	
# new facet 1/2
	VERTEX,	46.074,	48.601,	36.011,	
# new facet 1/2
	VERTEX,	46.0251,	50.568,	29.7192,	
# new facet 2/2
	VERTEX,	45.1017,	50.1928,	30.0775,	
# new facet 2/2
	VERTEX,	46.074,	48.601,	36.011,	
# new facet 2/2
	VERTEX,	46.0251,	50.568,	29.7192,	
# new facet 1/2
	VERTEX,	45.1017,	50.1928,	30.0775,	
# new facet 1/2
	VERTEX,	45.6665,	50.0977,	29.6854,	
# new facet 1/2
	VERTEX,	46.074,	48.601,	36.011,	
# new facet 2/2
	VERTEX,	45.1017,	50.1928,	30.0775,	
# new facet 2/2
	VERTEX,	45.6665,	50.0977,	29.6854,	
# new facet 2/2
	VERTEX,	46.074,	48.601,	36.011,	
# new facet 1/2
	VERTEX,	45.1017,	50.1928,	30.0775,	
# new facet 1/2
	VERTEX,	46.0251,	50.568,	29.7192,	
# new facet 1/2
	VERTEX,	45.6665,	50.0977,	29.6854,	
# new facet 2/2
	VERTEX,	45.1017,	50.1928,	30.0775,	
# new facet 2/2
	VERTEX,	46.0251,	50.568,	29.7192,	
# new facet 2/2
	VERTEX,	45.6665,	50.0977,	29.6854,	
# new polyhedron
# new facet 1/2
	VERTEX,	50.06,	45.998,	26.594,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 1/2
	VERTEX,	49.646,	51.416,	30.433,	
# new facet 2/2
	VERTEX,	50.06,	45.998,	26.594,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 2/2
	VERTEX,	49.646,	51.416,	30.433,	
# new facet 1/2
	VERTEX,	46.6139,	48.9404,	28.5793,	
# new facet 1/2
	VERTEX,	50.06,	45.998,	26.594,	
# new facet 1/2
	VERTEX,	49.646,	51.416,	30.433,	
# new facet 2/2
	VERTEX,	46.6139,	48.9404,	28.5793,	
# new facet 2/2
	VERTEX,	50.06,	45.998,	26.594,	
# new facet 2/2
	VERTEX,	49.646,	51.416,	30.433,	
# new facet 1/2
	VERTEX,	46.6139,	48.9404,	28.5793,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 1/2
	VERTEX,	50.06,	45.998,	26.594,	
# new facet 2/2
	VERTEX,	46.6139,	48.9404,	28.5793,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 2/2
	VERTEX,	50.06,	45.998,	26.594,	
# new facet 1/2
	VERTEX,	46.6139,	48.9404,	28.5793,	
# new facet 1/2
	VERTEX,	49.646,	51.416,	30.433,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 2/2
	VERTEX,	46.6139,	48.9404,	28.5793,	
# new facet 2/2
	VERTEX,	49.646,	51.416,	30.433,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 1/2
	VERTEX,	50.06,	45.998,	26.594,	
# new facet 1/2
	VERTEX,	49.646,	51.416,	30.433,	
# new facet 1/2
	VERTEX,	46.6139,	48.9404,	28.5793,	
# new facet 2/2
	VERTEX,	50.06,	45.998,	26.594,	
# new facet 2/2
	VERTEX,	49.646,	51.416,	30.433,	
# new facet 2/2
	VERTEX,	46.6139,	48.9404,	28.5793,	
# new facet 1/2
	VERTEX,	45.6765,	50.1077,	29.6954,	
# new facet 1/2
	VERTEX,	50.06,	45.998,	26.594,	
# new facet 1/2
	VERTEX,	46.6139,	48.9404,	28.5793,	
# new facet 2/2
	VERTEX,	45.6765,	50.1077,	29.6954,	
# new facet 2/2
	VERTEX,	50.06,	45.998,	26.594,	
# new facet 2/2
	VERTEX,	46.6139,	48.9404,	28.5793,	
# new facet 1/2
	VERTEX,	45.6765,	50.1077,	29.6954,	
# new facet 1/2
	VERTEX,	49.646,	51.416,	30.433,	
# new facet 1/2
	VERTEX,	50.06,	45.998,	26.594,	
# new facet 2/2
	VERTEX,	45.6765,	50.1077,	29.6954,	
# new facet 2/2
	VERTEX,	49.646,	51.416,	30.433,	
# new facet 2/2
	VERTEX,	50.06,	45.998,	26.594,	
# new facet 1/2
	VERTEX,	45.6765,	50.1077,	29.6954,	
# new facet 1/2
	VERTEX,	46.6139,	48.9404,	28.5793,	
# new facet 1/2
	VERTEX,	49.646,	51.416,	30.433,	
# new facet 2/2
	VERTEX,	45.6765,	50.1077,	29.6954,	
# new facet 2/2
	VERTEX,	46.6139,	48.9404,	28.5793,	
# new facet 2/2
	VERTEX,	49.646,	51.416,	30.433,	
# new facet 1/2
	VERTEX,	49.646,	51.416,	30.433,	
# new facet 1/2
	VERTEX,	46.6139,	48.9404,	28.5793,	
# new facet 1/2
	VERTEX,	45.6765,	50.1077,	29.6954,	
# new facet 2/2
	VERTEX,	49.646,	51.416,	30.433,	
# new facet 2/2
	VERTEX,	46.6139,	48.9404,	28.5793,	
# new facet 2/2
	VERTEX,	45.6765,	50.1077,	29.6954,	
# new facet 1/2
	VERTEX,	46.0351,	50.578,	29.7292,	
# new facet 1/2
	VERTEX,	49.646,	51.416,	30.433,	
# new facet 1/2
	VERTEX,	45.6765,	50.1077,	29.6954,	
# new facet 2/2
	VERTEX,	46.0351,	50.578,	29.7292,	
# new facet 2/2
	VERTEX,	49.646,	51.416,	30.433,	
# new facet 2/2
	VERTEX,	45.6765,	50.1077,	29.6954,	
# new facet 1/2
	VERTEX,	46.0351,	50.578,	29.7292,	
# new facet 1/2
	VERTEX,	46.6139,	48.9404,	28.5793,	
# new facet 1/2
	VERTEX,	49.646,	51.416,	30.433,	
# new facet 2/2
	VERTEX,	46.0351,	50.578,	29.7292,	
# new facet 2/2
	VERTEX,	46.6139,	48.9404,	28.5793,	
# new facet 2/2
	VERTEX,	49.646,	51.416,	30.433,	
# new facet 1/2
	VERTEX,	46.0351,	50.578,	29.7292,	
# new facet 1/2
	VERTEX,	45.6765,	50.1077,	29.6954,	
# new facet 1/2
	VERTEX,	46.6139,	48.9404,	28.5793,	
# new facet 2/2
	VERTEX,	46.0351,	50.578,	29.7292,	
# new facet 2/2
	VERTEX,	45.6765,	50.1077,	29.6954,	
# new facet 2/2
	VERTEX,	46.6139,	48.9404,	28.5793,	
# new polyhedron
# new facet 1/2
	VERTEX,	47.464,	44.613,	26.256,	
# new facet 1/2
	VERTEX,	46.92,	44.8843,	26.4321,	
# new facet 1/2
	VERTEX,	46.7668,	46.2238,	27.1711,	
# new facet 2/2
	VERTEX,	47.464,	44.613,	26.256,	
# new facet 2/2
	VERTEX,	46.92,	44.8843,	26.4321,	
# new facet 2/2
	VERTEX,	46.7668,	46.2238,	27.1711,	
# new facet 1/2
	VERTEX,	47.433,	44.883,	26.1371,	
# new facet 1/2
	VERTEX,	47.464,	44.613,	26.256,	
# new facet 1/2
	VERTEX,	46.7668,	46.2238,	27.1711,	
# new facet 2/2
	VERTEX,	47.433,	44.883,	26.1371,	
# new facet 2/2
	VERTEX,	47.464,	44.613,	26.256,	
# new facet 2/2
	VERTEX,	46.7668,	46.2238,	27.1711,	
# new facet 1/2
	VERTEX,	47.433,	44.883,	26.1371,	
# new facet 1/2
	VERTEX,	46.92,	44.8843,	26.4321,	
# new facet 1/2
	VERTEX,	47.464,	44.613,	26.256,	
# new facet 2/2
	VERTEX,	47.433,	44.883,	26.1371,	
# new facet 2/2
	VERTEX,	46.92,	44.8843,	26.4321,	
# new facet 2/2
	VERTEX,	47.464,	44.613,	26.256,	
# new facet 1/2
	VERTEX,	47.433,	44.883,	26.1371,	
# new facet 1/2
	VERTEX,	46.7668,	46.2238,	27.1711,	
# new facet 1/2
	VERTEX,	46.92,	44.8843,	26.4321,	
# new facet 2/2
	VERTEX,	47.433,	44.883,	26.1371,	
# new facet 2/2
	VERTEX,	46.7668,	46.2238,	27.1711,	
# new facet 2/2
	VERTEX,	46.92,	44.8843,	26.4321,	
# new polyhedron
# new facet 1/2
	VERTEX,	47.454,	44.603,	26.246,	
# new facet 1/2
	VERTEX,	45.9964,	45.5824,	27.3013,	
# new facet 1/2
	VERTEX,	46.7698,	46.2466,	27.1913,	
# new facet 2/2
	VERTEX,	47.454,	44.603,	26.246,	
# new facet 2/2
	VERTEX,	45.9964,	45.5824,	27.3013,	
# new facet 2/2
	VERTEX,	46.7698,	46.2466,	27.1913,	
# new facet 1/2
	VERTEX,	42.832,	47.987,	33.199,	
# new facet 1/2
	VERTEX,	47.454,	44.603,	26.246,	
# new facet 1/2
	VERTEX,	46.7698,	46.2466,	27.1913,	
# new facet 2/2
	VERTEX,	42.832,	47.987,	33.199,	
# new facet 2/2
	VERTEX,	47.454,	44.603,	26.246,	
# new facet 2/2
	VERTEX,	46.7698,	46.2466,	27.1913,	
# new facet 1/2
	VERTEX,	42.832,	47.987,	33.199,	
# new facet 1/2
	VERTEX,	45.9964,	45.5824,	27.3013,	
# new facet 1/2
	VERTEX,	47.454,	44.603,	26.246,	
# new facet 2/2
	VERTEX,	42.832,	47.987,	33.199,	
# new facet 2/2
	VERTEX,	45.9964,	45.5824,	27.3013,	
# new facet 2/2
	VERTEX,	47.454,	44.603,	26.246,	
# new facet 1/2
	VERTEX,	42.832,	47.987,	33.199,	
# new facet 1/2
	VERTEX,	46.7698,	46.2466,	27.1913,	
# new facet 1/2
	VERTEX,	45.9964,	45.5824,	27.3013,	
# new facet 2/2
	VERTEX,	42.832,	47.987,	33.199,	
# new facet 2/2
	VERTEX,	46.7698,	46.2466,	27.1913,	
# new facet 2/2
	VERTEX,	45.9964,	45.5824,	27.3013,	
# new facet 1/2
	VERTEX,	42.832,	47.987,	33.199,	
# new facet 1/2
	VERTEX,	45.9964,	45.5824,	27.3013,	
# new facet 1/2
	VERTEX,	46.7698,	46.2466,	27.1913,	
# new facet 2/2
	VERTEX,	42.832,	47.987,	33.199,	
# new facet 2/2
	VERTEX,	45.9964,	45.5824,	27.3013,	
# new facet 2/2
	VERTEX,	46.7698,	46.2466,	27.1913,	
# new facet 1/2
	VERTEX,	42.2963,	48.1631,	31.1899,	
# new facet 1/2
	VERTEX,	42.832,	47.987,	33.199,	
# new facet 1/2
	VERTEX,	46.7698,	46.2466,	27.1913,	
# new facet 2/2
	VERTEX,	42.2963,	48.1631,	31.1899,	
# new facet 2/2
	VERTEX,	42.832,	47.987,	33.199,	
# new facet 2/2
	VERTEX,	46.7698,	46.2466,	27.1913,	
# new facet 1/2
	VERTEX,	42.2963,	48.1631,	31.1899,	
# new facet 1/2
	VERTEX,	45.9964,	45.5824,	27.3013,	
# new facet 1/2
	VERTEX,	42.832,	47.987,	33.199,	
# new facet 2/2
	VERTEX,	42.2963,	48.1631,	31.1899,	
# new facet 2/2
	VERTEX,	45.9964,	45.5824,	27.3013,	
# new facet 2/2
	VERTEX,	42.832,	47.987,	33.199,	
# new facet 1/2
	VERTEX,	42.2963,	48.1631,	31.1899,	
# new facet 1/2
	VERTEX,	46.7698,	46.2466,	27.1913,	
# new facet 1/2
	VERTEX,	45.9964,	45.5824,	27.3013,	
# new facet 2/2
	VERTEX,	42.2963,	48.1631,	31.1899,	
# new facet 2/2
	VERTEX,	46.7698,	46.2466,	27.1913,	
# new facet 2/2
	VERTEX,	45.9964,	45.5824,	27.3013,	
# new facet 1/2
	VERTEX,	42.832,	47.987,	33.199,	
# new facet 1/2
	VERTEX,	46.7698,	46.2466,	27.1913,	
# new facet 1/2
	VERTEX,	42.2963,	48.1631,	31.1899,	
# new facet 2/2
	VERTEX,	42.832,	47.987,	33.199,	
# new facet 2/2
	VERTEX,	46.7698,	46.2466,	27.1913,	
# new facet 2/2
	VERTEX,	42.2963,	48.1631,	31.1899,	
# new facet 1/2
	VERTEX,	44.6181,	49.9116,	30.2291,	
# new facet 1/2
	VERTEX,	42.832,	47.987,	33.199,	
# new facet 1/2
	VERTEX,	42.2963,	48.1631,	31.1899,	
# new facet 2/2
	VERTEX,	44.6181,	49.9116,	30.2291,	
# new facet 2/2
	VERTEX,	42.832,	47.987,	33.199,	
# new facet 2/2
	VERTEX,	42.2963,	48.1631,	31.1899,	
# new facet 1/2
	VERTEX,	44.6181,	49.9116,	30.2291,	
# new facet 1/2
	VERTEX,	46.7698,	46.2466,	27.1913,	
# new facet 1/2
	VERTEX,	42.832,	47.987,	33.199,	
# new facet 2/2
	VERTEX,	44.6181,	49.9116,	30.2291,	
# new facet 2/2
	VERTEX,	46.7698,	46.2466,	27.1913,	
# new facet 2/2
	VERTEX,	42.832,	47.987,	33.199,	
# new facet 1/2
	VERTEX,	44.6181,	49.9116,	30.2291,	
# new facet 1/2
	VERTEX,	42.2963,	48.1631,	31.1899,	
# new facet 1/2
	VERTEX,	46.7698,	46.2466,	27.1913,	
# new facet 2/2
	VERTEX,	44.6181,	49.9116,	30.2291,	
# new facet 2/2
	VERTEX,	42.2963,	48.1631,	31.1899,	
# new facet 2/2
	VERTEX,	46.7698,	46.2466,	27.1913,	
# new polyhedron
# new facet 1/2
	VERTEX,	42.832,	47.967,	33.199,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 1/2
	VERTEX,	46.074,	48.601,	36.011,	
# new facet 2/2
	VERTEX,	42.832,	47.967,	33.199,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 2/2
	VERTEX,	46.074,	48.601,	36.011,	
# new facet 1/2
	VERTEX,	44.5881,	49.8816,	30.1991,	
# new facet 1/2
	VERTEX,	42.832,	47.967,	33.199,	
# new facet 1/2
	VERTEX,	46.074,	48.601,	36.011,	
# new facet 2/2
	VERTEX,	44.5881,	49.8816,	30.1991,	
# new facet 2/2
	VERTEX,	42.832,	47.967,	33.199,	
# new facet 2/2
	VERTEX,	46.074,	48.601,	36.011,	
# new facet 1/2
	VERTEX,	44.5881,	49.8816,	30.1991,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 1/2
	VERTEX,	42.832,	47.967,	33.199,	
# new facet 2/2
	VERTEX,	44.5881,	49.8816,	30.1991,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 2/2
	VERTEX,	42.832,	47.967,	33.199,	
# new facet 1/2
	VERTEX,	44.5881,	49.8816,	30.1991,	
# new facet 1/2
	VERTEX,	46.074,	48.601,	36.011,	
# new facet 1/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 2/2
	VERTEX,	44.5881,	49.8816,	30.1991,	
# new facet 2/2
	VERTEX,	46.074,	48.601,	36.011,	
# new facet 2/2
	VERTEX,	52.62,	47.833,	31.499,	
# new facet 1/2
	VERTEX,	42.832,	47.967,	33.199,	
# new facet 1/2
	VERTEX,	46.074,	48.601,	36.011,	
# new facet 1/2
	VERTEX,	44.5881,	49.8816,	30.1991,	
# new facet 2/2
	VERTEX,	42.832,	47.967,	33.199,	
# new facet 2/2
	VERTEX,	46.074,	48.601,	36.011,	
# new facet 2/2
	VERTEX,	44.5881,	49.8816,	30.1991,	
# new facet 1/2
	VERTEX,	45.6765,	50.1077,	29.6954,	
# new facet 1/2
	VERTEX,	42.832,	47.967,	33.199,	
# new facet 1/2
	VERTEX,	44.5881,	49.8816,	30.1991,	
# new facet 2/2
	VERTEX,	45.6765,	50.1077,	29.6954,	
# new facet 2/2
	VERTEX,	42.832,	47.967,	33.199,	
# new facet 2/2
	VERTEX,	44.5881,	49.8816,	30.1991,	
# new facet 1/2
	VERTEX,	45.6765,	50.1077,	29.6954,	
# new facet 1/2
	VERTEX,	46.074,	48.601,	36.011,	
# new facet 1/2
	VERTEX,	42.832,	47.967,	33.199,	
# new facet 2/2
	VERTEX,	45.6765,	50.1077,	29.6954,	
# new facet 2/2
	VERTEX,	46.074,	48.601,	36.011,	
# new facet 2/2
	VERTEX,	42.832,	47.967,	33.199,	
# new facet 1/2
	VERTEX,	45.6765,	50.1077,	29.6954,	
# new facet 1/2
	VERTEX,	44.5881,	49.8816,	30.1991,	
# new facet 1/2
	VERTEX,	46.074,	48.601,	36.011,	
# new facet 2/2
	VERTEX,	45.6765,	50.1077,	29.6954,	
# new facet 2/2
	VERTEX,	44.5881,	49.8816,	30.1991,	
# new facet 2/2
	VERTEX,	46.074,	48.601,	36.011,	
# new facet 1/2
	VERTEX,	46.074,	48.601,	36.011,	
# new facet 1/2
	VERTEX,	44.5881,	49.8816,	30.1991,	
# new facet 1/2
	VERTEX,	45.6765,	50.1077,	29.6954,	
# new facet 2/2
	VERTEX,	46.074,	48.601,	36.011,	
# new facet 2/2
	VERTEX,	44.5881,	49.8816,	30.1991,	
# new facet 2/2
	VERTEX,	45.6765,	50.1077,	29.6954,	
# new facet 1/2
	VERTEX,	45.1017,	50.1928,	30.0775,	
# new facet 1/2
	VERTEX,	46.074,	48.601,	36.011,	
# new facet 1/2
	VERTEX,	45.6765,	50.1077,	29.6954,	
# new facet 2/2
	VERTEX,	45.1017,	50.1928,	30.0775,	
# new facet 2/2
	VERTEX,	46.074,	48.601,	36.011,	
# new facet 2/2
	VERTEX,	45.6765,	50.1077,	29.6954,	
# new facet 1/2
	VERTEX,	45.1017,	50.1928,	30.0775,	
# new facet 1/2
	VERTEX,	44.5881,	49.8816,	30.1991,	
# new facet 1/2
	VERTEX,	46.074,	48.601,	36.011,	
# new facet 2/2
	VERTEX,	45.1017,	50.1928,	30.0775,	
# new facet 2/2
	VERTEX,	44.5881,	49.8816,	30.1991,	
# new facet 2/2
	VERTEX,	46.074,	48.601,	36.011,	
# new facet 1/2
	VERTEX,	45.1017,	50.1928,	30.0775,	
# new facet 1/2
	VERTEX,	45.6765,	50.1077,	29.6954,	
# new facet 1/2
	VERTEX,	44.5881,	49.8816,	30.1991,	
# new facet 2/2
	VERTEX,	45.1017,	50.1928,	30.0775,	
# new facet 2/2
	VERTEX,	45.6765,	50.1077,	29.6954,	
# new facet 2/2
	VERTEX,	44.5881,	49.8816,	30.1991,	
# new polyhedron
# new facet 1/2
	VERTEX,	42.289,	36.24,	28.634,	
# new facet 1/2
	VERTEX,	39.0344,	42.8469,	31.1206,	
# new facet 1/2
	VERTEX,	40.5504,	38.4546,	29.1001,	
# new facet 2/2
	VERTEX,	42.289,	36.24,	28.634,	
# new facet 2/2
	VERTEX,	39.0344,	42.8469,	31.1206,	
# new facet 2/2
	VERTEX,	40.5504,	38.4546,	29.1001,	
# new facet 1/2
	VERTEX,	40.4965,	37.0731,	29.7184,	
# new facet 1/2
	VERTEX,	42.289,	36.24,	28.634,	
# new facet 1/2
	VERTEX,	40.5504,	38.4546,	29.1001,	
# new facet 2/2
	VERTEX,	40.4965,	37.0731,	29.7184,	
# new facet 2/2
	VERTEX,	42.289,	36.24,	28.634,	
# new facet 2/2
	VERTEX,	40.5504,	38.4546,	29.1001,	
# new facet 1/2
	VERTEX,	40.4965,	37.0731,	29.7184,	
# new facet 1/2
	VERTEX,	39.0344,	42.8469,	31.1206,	
# new facet 1/2
	VERTEX,	42.289,	36.24,	28.634,	
# new facet 2/2
	VERTEX,	40.4965,	37.0731,	29.7184,	
# new facet 2/2
	VERTEX,	39.0344,	42.8469,	31.1206,	
# new facet 2/2
	VERTEX,	42.289,	36.24,	28.634,	
# new facet 1/2
	VERTEX,	40.4965,	37.0731,	29.7184,	
# new facet 1/2
	VERTEX,	40.5504,	38.4546,	29.1001,	
# new facet 1/2
	VERTEX,	39.0344,	42.8469,	31.1206,	
# new facet 2/2
	VERTEX,	40.4965,	37.0731,	29.7184,	
# new facet 2/2
	VERTEX,	40.5504,	38.4546,	29.1001,	
# new facet 2/2
	VERTEX,	39.0344,	42.8469,	31.1206,	
# new polyhedron
# new facet 1/2
	VERTEX,	42.279,	36.23,	28.624,	
# new facet 1/2
	VERTEX,	40.4965,	37.0731,	29.7184,	
# new facet 1/2
	VERTEX,	39.0444,	42.8569,	31.1306,	
# new facet 2/2
	VERTEX,	42.279,	36.23,	28.624,	
# new facet 2/2
	VERTEX,	40.4965,	37.0731,	29.7184,	
# new facet 2/2
	VERTEX,	39.0444,	42.8569,	31.1306,	
# new facet 1/2
	VERTEX,	40.058,	36.075,	32.378,	
# new facet 1/2
	VERTEX,	42.279,	36.23,	28.624,	
# new facet 1/2
	VERTEX,	39.0444,	42.8569,	31.1306,	
# new facet 2/2
	VERTEX,	40.058,	36.075,	32.378,	
# new facet 2/2
	VERTEX,	42.279,	36.23,	28.624,	
# new facet 2/2
	VERTEX,	39.0444,	42.8569,	31.1306,	
# new facet 1/2
	VERTEX,	40.058,	36.075,	32.378,	
# new facet 1/2
	VERTEX,	40.4965,	37.0731,	29.7184,	
# new facet 1/2
	VERTEX,	42.279,	36.23,	28.624,	
# new facet 2/2
	VERTEX,	40.058,	36.075,	32.378,	
# new facet 2/2
	VERTEX,	40.4965,	37.0731,	29.7184,	
# new facet 2/2
	VERTEX,	42.279,	36.23,	28.624,	
# new facet 1/2
	VERTEX,	40.058,	36.075,	32.378,	
# new facet 1/2
	VERTEX,	39.0444,	42.8569,	31.1306,	
# new facet 1/2
	VERTEX,	40.4965,	37.0731,	29.7184,	
# new facet 2/2
	VERTEX,	40.058,	36.075,	32.378,	
# new facet 2/2
	VERTEX,	39.0444,	42.8569,	31.1306,	
# new facet 2/2
	VERTEX,	40.4965,	37.0731,	29.7184,	
# new facet 1/2
	VERTEX,	40.058,	36.075,	32.378,	
# new facet 1/2
	VERTEX,	40.4965,	37.0731,	29.7184,	
# new facet 1/2
	VERTEX,	39.0444,	42.8569,	31.1306,	
# new facet 2/2
	VERTEX,	40.058,	36.075,	32.378,	
# new facet 2/2
	VERTEX,	40.4965,	37.0731,	29.7184,	
# new facet 2/2
	VERTEX,	39.0444,	42.8569,	31.1306,	
# new facet 1/2
	VERTEX,	39.3325,	36.7175,	32.3034,	
# new facet 1/2
	VERTEX,	40.058,	36.075,	32.378,	
# new facet 1/2
	VERTEX,	39.0444,	42.8569,	31.1306,	
# new facet 2/2
	VERTEX,	39.3325,	36.7175,	32.3034,	
# new facet 2/2
	VERTEX,	40.058,	36.075,	32.378,	
# new facet 2/2
	VERTEX,	39.0444,	42.8569,	31.1306,	
# new facet 1/2
	VERTEX,	39.3325,	36.7175,	32.3034,	
# new facet 1/2
	VERTEX,	40.4965,	37.0731,	29.7184,	
# new facet 1/2
	VERTEX,	40.058,	36.075,	32.378,	
# new facet 2/2
	VERTEX,	39.3325,	36.7175,	32.3034,	
# new facet 2/2
	VERTEX,	40.4965,	37.0731,	29.7184,	
# new facet 2/2
	VERTEX,	40.058,	36.075,	32.378,	
# new facet 1/2
	VERTEX,	39.3325,	36.7175,	32.3034,	
# new facet 1/2
	VERTEX,	39.0444,	42.8569,	31.1306,	
# new facet 1/2
	VERTEX,	40.4965,	37.0731,	29.7184,	
# new facet 2/2
	VERTEX,	39.3325,	36.7175,	32.3034,	
# new facet 2/2
	VERTEX,	39.0444,	42.8569,	31.1306,	
# new facet 2/2
	VERTEX,	40.4965,	37.0731,	29.7184,	
# new facet 1/2
	VERTEX,	40.058,	36.075,	32.378,	
# new facet 1/2
	VERTEX,	39.0444,	42.8569,	31.1306,	
# new facet 1/2
	VERTEX,	39.3325,	36.7175,	32.3034,	
# new facet 2/2
	VERTEX,	40.058,	36.075,	32.378,	
# new facet 2/2
	VERTEX,	39.0444,	42.8569,	31.1306,	
# new facet 2/2
	VERTEX,	39.3325,	36.7175,	32.3034,	
# new facet 1/2
	VERTEX,	38.8542,	43.0568,	31.4195,	
# new facet 1/2
	VERTEX,	40.058,	36.075,	32.378,	
# new facet 1/2
	VERTEX,	39.3325,	36.7175,	32.3034,	
# new facet 2/2
	VERTEX,	38.8542,	43.0568,	31.4195,	
# new facet 2/2
	VERTEX,	40.058,	36.075,	32.378,	
# new facet 2/2
	VERTEX,	39.3325,	36.7175,	32.3034,	
# new facet 1/2
	VERTEX,	38.8542,	43.0568,	31.4195,	
# new facet 1/2
	VERTEX,	39.0444,	42.8569,	31.1306,	
# new facet 1/2
	VERTEX,	40.058,	36.075,	32.378,	
# new facet 2/2
	VERTEX,	38.8542,	43.0568,	31.4195,	
# new facet 2/2
	VERTEX,	39.0444,	42.8569,	31.1306,	
# new facet 2/2
	VERTEX,	40.058,	36.075,	32.378,	
# new facet 1/2
	VERTEX,	38.8542,	43.0568,	31.4195,	
# new facet 1/2
	VERTEX,	39.3325,	36.7175,	32.3034,	
# new facet 1/2
	VERTEX,	39.0444,	42.8569,	31.1306,	
# new facet 2/2
	VERTEX,	38.8542,	43.0568,	31.4195,	
# new facet 2/2
	VERTEX,	39.3325,	36.7175,	32.3034,	
# new facet 2/2
	VERTEX,	39.0444,	42.8569,	31.1306,	
# new polyhedron
# new facet 1/2
	VERTEX,	42.279,	36.23,	28.624,	
# new facet 1/2
	VERTEX,	41.246,	36.095,	32.528,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 2/2
	VERTEX,	42.279,	36.23,	28.624,	
# new facet 2/2
	VERTEX,	41.246,	36.095,	32.528,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 1/2
	VERTEX,	39.0344,	42.8469,	31.1206,	
# new facet 1/2
	VERTEX,	42.279,	36.23,	28.624,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 2/2
	VERTEX,	39.0344,	42.8469,	31.1206,	
# new facet 2/2
	VERTEX,	42.279,	36.23,	28.624,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 1/2
	VERTEX,	39.0344,	42.8469,	31.1206,	
# new facet 1/2
	VERTEX,	41.246,	36.095,	32.528,	
# new facet 1/2
	VERTEX,	42.279,	36.23,	28.624,	
# new facet 2/2
	VERTEX,	39.0344,	42.8469,	31.1206,	
# new facet 2/2
	VERTEX,	41.246,	36.095,	32.528,	
# new facet 2/2
	VERTEX,	42.279,	36.23,	28.624,	
# new facet 1/2
	VERTEX,	39.0344,	42.8469,	31.1206,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 1/2
	VERTEX,	41.246,	36.095,	32.528,	
# new facet 2/2
	VERTEX,	39.0344,	42.8469,	31.1206,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 2/2
	VERTEX,	41.246,	36.095,	32.528,	
# new facet 1/2
	VERTEX,	42.279,	36.23,	28.624,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 1/2
	VERTEX,	39.0344,	42.8469,	31.1206,	
# new facet 2/2
	VERTEX,	42.279,	36.23,	28.624,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 2/2
	VERTEX,	39.0344,	42.8469,	31.1206,	
# new facet 1/2
	VERTEX,	38.8758,	43.0994,	31.3973,	
# new facet 1/2
	VERTEX,	42.279,	36.23,	28.624,	
# new facet 1/2
	VERTEX,	39.0344,	42.8469,	31.1206,	
# new facet 2/2
	VERTEX,	38.8758,	43.0994,	31.3973,	
# new facet 2/2
	VERTEX,	42.279,	36.23,	28.624,	
# new facet 2/2
	VERTEX,	39.0344,	42.8469,	31.1206,	
# new facet 1/2
	VERTEX,	38.8758,	43.0994,	31.3973,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 1/2
	VERTEX,	42.279,	36.23,	28.624,	
# new facet 2/2
	VERTEX,	38.8758,	43.0994,	31.3973,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 2/2
	VERTEX,	42.279,	36.23,	28.624,	
# new facet 1/2
	VERTEX,	38.8758,	43.0994,	31.3973,	
# new facet 1/2
	VERTEX,	39.0344,	42.8469,	31.1206,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 2/2
	VERTEX,	38.8758,	43.0994,	31.3973,	
# new facet 2/2
	VERTEX,	39.0344,	42.8469,	31.1206,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 1/2
	VERTEX,	39.0344,	42.8469,	31.1206,	
# new facet 1/2
	VERTEX,	38.8758,	43.0994,	31.3973,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 2/2
	VERTEX,	39.0344,	42.8469,	31.1206,	
# new facet 2/2
	VERTEX,	38.8758,	43.0994,	31.3973,	
# new facet 1/2
	VERTEX,	38.9228,	43.3137,	31.4827,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 1/2
	VERTEX,	38.8758,	43.0994,	31.3973,	
# new facet 2/2
	VERTEX,	38.9228,	43.3137,	31.4827,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 2/2
	VERTEX,	38.8758,	43.0994,	31.3973,	
# new facet 1/2
	VERTEX,	38.9228,	43.3137,	31.4827,	
# new facet 1/2
	VERTEX,	39.0344,	42.8469,	31.1206,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 2/2
	VERTEX,	38.9228,	43.3137,	31.4827,	
# new facet 2/2
	VERTEX,	39.0344,	42.8469,	31.1206,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 1/2
	VERTEX,	38.9228,	43.3137,	31.4827,	
# new facet 1/2
	VERTEX,	38.8758,	43.0994,	31.3973,	
# new facet 1/2
	VERTEX,	39.0344,	42.8469,	31.1206,	
# new facet 2/2
	VERTEX,	38.9228,	43.3137,	31.4827,	
# new facet 2/2
	VERTEX,	38.8758,	43.0994,	31.3973,	
# new facet 2/2
	VERTEX,	39.0344,	42.8469,	31.1206,	
# new polyhedron
# new facet 1/2
	VERTEX,	40.669,	35.53,	31.612,	
# new facet 1/2
	VERTEX,	40.1003,	35.5497,	31.0904,	
# new facet 1/2
	VERTEX,	39.6554,	36.4189,	31.717,	
# new facet 2/2
	VERTEX,	40.669,	35.53,	31.612,	
# new facet 2/2
	VERTEX,	40.1003,	35.5497,	31.0904,	
# new facet 2/2
	VERTEX,	39.6554,	36.4189,	31.717,	
# new facet 1/2
	VERTEX,	42.279,	36.25,	28.624,	
# new facet 1/2
	VERTEX,	40.669,	35.53,	31.612,	
# new facet 1/2
	VERTEX,	39.6554,	36.4189,	31.717,	
# new facet 2/2
	VERTEX,	42.279,	36.25,	28.624,	
# new facet 2/2
	VERTEX,	40.669,	35.53,	31.612,	
# new facet 2/2
	VERTEX,	39.6554,	36.4189,	31.717,	
# new facet 1/2
	VERTEX,	42.279,	36.25,	28.624,	
# new facet 1/2
	VERTEX,	40.1003,	35.5497,	31.0904,	
# new facet 1/2
	VERTEX,	40.669,	35.53,	31.612,	
# new facet 2/2
	VERTEX,	42.279,	36.25,	28.624,	
# new facet 2/2
	VERTEX,	40.1003,	35.5497,	31.0904,	
# new facet 2/2
	VERTEX,	40.669,	35.53,	31.612,	
# new facet 1/2
	VERTEX,	42.279,	36.25,	28.624,	
# new facet 1/2
	VERTEX,	39.6554,	36.4189,	31.717,	
# new facet 1/2
	VERTEX,	40.1003,	35.5497,	31.0904,	
# new facet 2/2
	VERTEX,	42.279,	36.25,	28.624,	
# new facet 2/2
	VERTEX,	39.6554,	36.4189,	31.717,	
# new facet 2/2
	VERTEX,	40.1003,	35.5497,	31.0904,	
# new facet 1/2
	VERTEX,	42.279,	36.25,	28.624,	
# new facet 1/2
	VERTEX,	40.1003,	35.5497,	31.0904,	
# new facet 1/2
	VERTEX,	39.6554,	36.4189,	31.717,	
# new facet 2/2
	VERTEX,	42.279,	36.25,	28.624,	
# new facet 2/2
	VERTEX,	40.1003,	35.5497,	31.0904,	
# new facet 2/2
	VERTEX,	39.6554,	36.4189,	31.717,	
# new facet 1/2
	VERTEX,	41.2752,	36.1305,	28.6069,	
# new facet 1/2
	VERTEX,	42.279,	36.25,	28.624,	
# new facet 1/2
	VERTEX,	39.6554,	36.4189,	31.717,	
# new facet 2/2
	VERTEX,	41.2752,	36.1305,	28.6069,	
# new facet 2/2
	VERTEX,	42.279,	36.25,	28.624,	
# new facet 2/2
	VERTEX,	39.6554,	36.4189,	31.717,	
# new facet 1/2
	VERTEX,	41.2752,	36.1305,	28.6069,	
# new facet 1/2
	VERTEX,	40.1003,	35.5497,	31.0904,	
# new facet 1/2
	VERTEX,	42.279,	36.25,	28.624,	
# new facet 2/2
	VERTEX,	41.2752,	36.1305,	28.6069,	
# new facet 2/2
	VERTEX,	40.1003,	35.5497,	31.0904,	
# new facet 2/2
	VERTEX,	42.279,	36.25,	28.624,	
# new facet 1/2
	VERTEX,	41.2752,	36.1305,	28.6069,	
# new facet 1/2
	VERTEX,	39.6554,	36.4189,	31.717,	
# new facet 1/2
	VERTEX,	40.1003,	35.5497,	31.0904,	
# new facet 2/2
	VERTEX,	41.2752,	36.1305,	28.6069,	
# new facet 2/2
	VERTEX,	39.6554,	36.4189,	31.717,	
# new facet 2/2
	VERTEX,	40.1003,	35.5497,	31.0904,	
# new facet 1/2
	VERTEX,	42.279,	36.25,	28.624,	
# new facet 1/2
	VERTEX,	39.6554,	36.4189,	31.717,	
# new facet 1/2
	VERTEX,	41.2752,	36.1305,	28.6069,	
# new facet 2/2
	VERTEX,	42.279,	36.25,	28.624,	
# new facet 2/2
	VERTEX,	39.6554,	36.4189,	31.717,	
# new facet 2/2
	VERTEX,	41.2752,	36.1305,	28.6069,	
# new facet 1/2
	VERTEX,	40.5265,	37.1031,	29.7484,	
# new facet 1/2
	VERTEX,	42.279,	36.25,	28.624,	
# new facet 1/2
	VERTEX,	41.2752,	36.1305,	28.6069,	
# new facet 2/2
	VERTEX,	40.5265,	37.1031,	29.7484,	
# new facet 2/2
	VERTEX,	42.279,	36.25,	28.624,	
# new facet 2/2
	VERTEX,	41.2752,	36.1305,	28.6069,	
# new facet 1/2
	VERTEX,	40.5265,	37.1031,	29.7484,	
# new facet 1/2
	VERTEX,	39.6554,	36.4189,	31.717,	
# new facet 1/2
	VERTEX,	42.279,	36.25,	28.624,	
# new facet 2/2
	VERTEX,	40.5265,	37.1031,	29.7484,	
# new facet 2/2
	VERTEX,	39.6554,	36.4189,	31.717,	
# new facet 2/2
	VERTEX,	42.279,	36.25,	28.624,	
# new facet 1/2
	VERTEX,	40.5265,	37.1031,	29.7484,	
# new facet 1/2
	VERTEX,	41.2752,	36.1305,	28.6069,	
# new facet 1/2
	VERTEX,	39.6554,	36.4189,	31.717,	
# new facet 2/2
	VERTEX,	40.5265,	37.1031,	29.7484,	
# new facet 2/2
	VERTEX,	41.2752,	36.1305,	28.6069,	
# new facet 2/2
	VERTEX,	39.6554,	36.4189,	31.717,	
# new polyhedron
# new facet 1/2
	VERTEX,	44.718,	33.764,	32.874,	
# new facet 1/2
	VERTEX,	43.0252,	32.388,	28.5802,	
# new facet 1/2
	VERTEX,	45.33,	31.641,	30.4979,	
# new facet 2/2
	VERTEX,	44.718,	33.764,	32.874,	
# new facet 2/2
	VERTEX,	43.0252,	32.388,	28.5802,	
# new facet 2/2
	VERTEX,	45.33,	31.641,	30.4979,	
# new facet 1/2
	VERTEX,	46.4713,	33.7481,	30.1458,	
# new facet 1/2
	VERTEX,	44.718,	33.764,	32.874,	
# new facet 1/2
	VERTEX,	45.33,	31.641,	30.4979,	
# new facet 2/2
	VERTEX,	46.4713,	33.7481,	30.1458,	
# new facet 2/2
	VERTEX,	44.718,	33.764,	32.874,	
# new facet 2/2
	VERTEX,	45.33,	31.641,	30.4979,	
# new facet 1/2
	VERTEX,	46.4713,	33.7481,	30.1458,	
# new facet 1/2
	VERTEX,	43.0252,	32.388,	28.5802,	
# new facet 1/2
	VERTEX,	44.718,	33.764,	32.874,	
# new facet 2/2
	VERTEX,	46.4713,	33.7481,	30.1458,	
# new facet 2/2
	VERTEX,	43.0252,	32.388,	28.5802,	
# new facet 2/2
	VERTEX,	44.718,	33.764,	32.874,	
# new facet 1/2
	VERTEX,	46.4713,	33.7481,	30.1458,	
# new facet 1/2
	VERTEX,	45.33,	31.641,	30.4979,	
# new facet 1/2
	VERTEX,	43.0252,	32.388,	28.5802,	
# new facet 2/2
	VERTEX,	46.4713,	33.7481,	30.1458,	
# new facet 2/2
	VERTEX,	45.33,	31.641,	30.4979,	
# new facet 2/2
	VERTEX,	43.0252,	32.388,	28.5802,	
# new polyhedron
# new facet 1/2
	VERTEX,	40.703,	35.539,	31.64,	
# new facet 1/2
	VERTEX,	41.8934,	33.6237,	29.5371,	
# new facet 1/2
	VERTEX,	40.1927,	34.5768,	31.7269,	
# new facet 2/2
	VERTEX,	40.703,	35.539,	31.64,	
# new facet 2/2
	VERTEX,	41.8934,	33.6237,	29.5371,	
# new facet 2/2
	VERTEX,	40.1927,	34.5768,	31.7269,	
# new facet 1/2
	VERTEX,	41.6591,	31.7756,	31.8904,	
# new facet 1/2
	VERTEX,	40.703,	35.539,	31.64,	
# new facet 1/2
	VERTEX,	40.1927,	34.5768,	31.7269,	
# new facet 2/2
	VERTEX,	41.6591,	31.7756,	31.8904,	
# new facet 2/2
	VERTEX,	40.703,	35.539,	31.64,	
# new facet 2/2
	VERTEX,	40.1927,	34.5768,	31.7269,	
# new facet 1/2
	VERTEX,	41.6591,	31.7756,	31.8904,	
# new facet 1/2
	VERTEX,	41.8934,	33.6237,	29.5371,	
# new facet 1/2
	VERTEX,	40.703,	35.539,	31.64,	
# new facet 2/2
	VERTEX,	41.6591,	31.7756,	31.8904,	
# new facet 2/2
	VERTEX,	41.8934,	33.6237,	29.5371,	
# new facet 2/2
	VERTEX,	40.703,	35.539,	31.64,	
# new facet 1/2
	VERTEX,	41.6591,	31.7756,	31.8904,	
# new facet 1/2
	VERTEX,	40.1927,	34.5768,	31.7269,	
# new facet 1/2
	VERTEX,	41.8934,	33.6237,	29.5371,	
# new facet 2/2
	VERTEX,	41.6591,	31.7756,	31.8904,	
# new facet 2/2
	VERTEX,	40.1927,	34.5768,	31.7269,	
# new facet 2/2
	VERTEX,	41.8934,	33.6237,	29.5371,	
# new polyhedron
# new facet 1/2
	VERTEX,	42.288,	36.217,	28.639,	
# new facet 1/2
	VERTEX,	40.693,	35.549,	31.63,	
# new facet 1/2
	VERTEX,	44.708,	33.774,	32.884,	
# new facet 2/2
	VERTEX,	42.288,	36.217,	28.639,	
# new facet 2/2
	VERTEX,	40.693,	35.549,	31.63,	
# new facet 2/2
	VERTEX,	44.708,	33.774,	32.884,	
# new facet 1/2
	VERTEX,	42.5948,	33.7121,	28.2333,	
# new facet 1/2
	VERTEX,	42.288,	36.217,	28.639,	
# new facet 1/2
	VERTEX,	44.708,	33.774,	32.884,	
# new facet 2/2
	VERTEX,	42.5948,	33.7121,	28.2333,	
# new facet 2/2
	VERTEX,	42.288,	36.217,	28.639,	
# new facet 2/2
	VERTEX,	44.708,	33.774,	32.884,	
# new facet 1/2
	VERTEX,	42.5948,	33.7121,	28.2333,	
# new facet 1/2
	VERTEX,	40.693,	35.549,	31.63,	
# new facet 1/2
	VERTEX,	42.288,	36.217,	28.639,	
# new facet 2/2
	VERTEX,	42.5948,	33.7121,	28.2333,	
# new facet 2/2
	VERTEX,	40.693,	35.549,	31.63,	
# new facet 2/2
	VERTEX,	42.288,	36.217,	28.639,	
# new facet 1/2
	VERTEX,	42.5948,	33.7121,	28.2333,	
# new facet 1/2
	VERTEX,	44.708,	33.774,	32.884,	
# new facet 1/2
	VERTEX,	40.693,	35.549,	31.63,	
# new facet 2/2
	VERTEX,	42.5948,	33.7121,	28.2333,	
# new facet 2/2
	VERTEX,	44.708,	33.774,	32.884,	
# new facet 2/2
	VERTEX,	40.693,	35.549,	31.63,	
# new facet 1/2
	VERTEX,	42.288,	36.217,	28.639,	
# new facet 1/2
	VERTEX,	44.708,	33.774,	32.884,	
# new facet 1/2
	VERTEX,	42.5948,	33.7121,	28.2333,	
# new facet 2/2
	VERTEX,	42.288,	36.217,	28.639,	
# new facet 2/2
	VERTEX,	44.708,	33.774,	32.884,	
# new facet 2/2
	VERTEX,	42.5948,	33.7121,	28.2333,	
# new facet 1/2
	VERTEX,	41.9034,	33.6337,	29.5471,	
# new facet 1/2
	VERTEX,	42.288,	36.217,	28.639,	
# new facet 1/2
	VERTEX,	42.5948,	33.7121,	28.2333,	
# new facet 2/2
	VERTEX,	41.9034,	33.6337,	29.5471,	
# new facet 2/2
	VERTEX,	42.288,	36.217,	28.639,	
# new facet 2/2
	VERTEX,	42.5948,	33.7121,	28.2333,	
# new facet 1/2
	VERTEX,	41.9034,	33.6337,	29.5471,	
# new facet 1/2
	VERTEX,	44.708,	33.774,	32.884,	
# new facet 1/2
	VERTEX,	42.288,	36.217,	28.639,	
# new facet 2/2
	VERTEX,	41.9034,	33.6337,	29.5471,	
# new facet 2/2
	VERTEX,	44.708,	33.774,	32.884,	
# new facet 2/2
	VERTEX,	42.288,	36.217,	28.639,	
# new facet 1/2
	VERTEX,	41.9034,	33.6337,	29.5471,	
# new facet 1/2
	VERTEX,	42.5948,	33.7121,	28.2333,	
# new facet 1/2
	VERTEX,	44.708,	33.774,	32.884,	
# new facet 2/2
	VERTEX,	41.9034,	33.6337,	29.5471,	
# new facet 2/2
	VERTEX,	42.5948,	33.7121,	28.2333,	
# new facet 2/2
	VERTEX,	44.708,	33.774,	32.884,	
# new facet 1/2
	VERTEX,	44.708,	33.774,	32.884,	
# new facet 1/2
	VERTEX,	42.5948,	33.7121,	28.2333,	
# new facet 1/2
	VERTEX,	41.9034,	33.6337,	29.5471,	
# new facet 2/2
	VERTEX,	44.708,	33.774,	32.884,	
# new facet 2/2
	VERTEX,	42.5948,	33.7121,	28.2333,	
# new facet 2/2
	VERTEX,	41.9034,	33.6337,	29.5471,	
# new facet 1/2
	VERTEX,	43.0328,	32.4223,	28.61,	
# new facet 1/2
	VERTEX,	44.708,	33.774,	32.884,	
# new facet 1/2
	VERTEX,	41.9034,	33.6337,	29.5471,	
# new facet 2/2
	VERTEX,	43.0328,	32.4223,	28.61,	
# new facet 2/2
	VERTEX,	44.708,	33.774,	32.884,	
# new facet 2/2
	VERTEX,	41.9034,	33.6337,	29.5471,	
# new facet 1/2
	VERTEX,	43.0328,	32.4223,	28.61,	
# new facet 1/2
	VERTEX,	42.5948,	33.7121,	28.2333,	
# new facet 1/2
	VERTEX,	44.708,	33.774,	32.884,	
# new facet 2/2
	VERTEX,	43.0328,	32.4223,	28.61,	
# new facet 2/2
	VERTEX,	42.5948,	33.7121,	28.2333,	
# new facet 2/2
	VERTEX,	44.708,	33.774,	32.884,	
# new facet 1/2
	VERTEX,	43.0328,	32.4223,	28.61,	
# new facet 1/2
	VERTEX,	41.9034,	33.6337,	29.5471,	
# new facet 1/2
	VERTEX,	42.5948,	33.7121,	28.2333,	
# new facet 2/2
	VERTEX,	43.0328,	32.4223,	28.61,	
# new facet 2/2
	VERTEX,	41.9034,	33.6337,	29.5471,	
# new facet 2/2
	VERTEX,	42.5948,	33.7121,	28.2333,	
# new polyhedron
# new facet 1/2
	VERTEX,	47.464,	44.613,	26.256,	
# new facet 1/2
	VERTEX,	46.92,	44.8843,	26.4321,	
# new facet 1/2
	VERTEX,	47.433,	44.883,	26.1371,	
# new facet 2/2
	VERTEX,	47.464,	44.613,	26.256,	
# new facet 2/2
	VERTEX,	46.92,	44.8843,	26.4321,	
# new facet 2/2
	VERTEX,	47.433,	44.883,	26.1371,	
# new facet 1/2
	VERTEX,	47.1581,	44.4824,	26.1001,	
# new facet 1/2
	VERTEX,	47.464,	44.613,	26.256,	
# new facet 1/2
	VERTEX,	47.433,	44.883,	26.1371,	
# new facet 2/2
	VERTEX,	47.1581,	44.4824,	26.1001,	
# new facet 2/2
	VERTEX,	47.464,	44.613,	26.256,	
# new facet 2/2
	VERTEX,	47.433,	44.883,	26.1371,	
# new facet 1/2
	VERTEX,	47.1581,	44.4824,	26.1001,	
# new facet 1/2
	VERTEX,	46.92,	44.8843,	26.4321,	
# new facet 1/2
	VERTEX,	47.464,	44.613,	26.256,	
# new facet 2/2
	VERTEX,	47.1581,	44.4824,	26.1001,	
# new facet 2/2
	VERTEX,	46.92,	44.8843,	26.4321,	
# new facet 2/2
	VERTEX,	47.464,	44.613,	26.256,	
# new facet 1/2
	VERTEX,	47.1581,	44.4824,	26.1001,	
# new facet 1/2
	VERTEX,	47.433,	44.883,	26.1371,	
# new facet 1/2
	VERTEX,	46.92,	44.8843,	26.4321,	
# new facet 2/2
	VERTEX,	47.1581,	44.4824,	26.1001,	
# new facet 2/2
	VERTEX,	47.433,	44.883,	26.1371,	
# new facet 2/2
	VERTEX,	46.92,	44.8843,	26.4321,	
# new polyhedron
# new facet 1/2
	VERTEX,	40.693,	35.529,	31.63,	
# new facet 1/2
	VERTEX,	41.6591,	31.7756,	31.8904,	
# new facet 1/2
	VERTEX,	41.9034,	33.6337,	29.5471,	
# new facet 2/2
	VERTEX,	40.693,	35.529,	31.63,	
# new facet 2/2
	VERTEX,	41.6591,	31.7756,	31.8904,	
# new facet 2/2
	VERTEX,	41.9034,	33.6337,	29.5471,	
# new facet 1/2
	VERTEX,	44.708,	33.774,	32.864,	
# new facet 1/2
	VERTEX,	40.693,	35.529,	31.63,	
# new facet 1/2
	VERTEX,	41.9034,	33.6337,	29.5471,	
# new facet 2/2
	VERTEX,	44.708,	33.774,	32.864,	
# new facet 2/2
	VERTEX,	40.693,	35.529,	31.63,	
# new facet 2/2
	VERTEX,	41.9034,	33.6337,	29.5471,	
# new facet 1/2
	VERTEX,	44.708,	33.774,	32.864,	
# new facet 1/2
	VERTEX,	41.6591,	31.7756,	31.8904,	
# new facet 1/2
	VERTEX,	40.693,	35.529,	31.63,	
# new facet 2/2
	VERTEX,	44.708,	33.774,	32.864,	
# new facet 2/2
	VERTEX,	41.6591,	31.7756,	31.8904,	
# new facet 2/2
	VERTEX,	40.693,	35.529,	31.63,	
# new facet 1/2
	VERTEX,	44.708,	33.774,	32.864,	
# new facet 1/2
	VERTEX,	41.9034,	33.6337,	29.5471,	
# new facet 1/2
	VERTEX,	41.6591,	31.7756,	31.8904,	
# new facet 2/2
	VERTEX,	44.708,	33.774,	32.864,	
# new facet 2/2
	VERTEX,	41.9034,	33.6337,	29.5471,	
# new facet 2/2
	VERTEX,	41.6591,	31.7756,	31.8904,	
# new facet 1/2
	VERTEX,	44.708,	33.774,	32.864,	
# new facet 1/2
	VERTEX,	41.6591,	31.7756,	31.8904,	
# new facet 1/2
	VERTEX,	41.9034,	33.6337,	29.5471,	
# new facet 2/2
	VERTEX,	44.708,	33.774,	32.864,	
# new facet 2/2
	VERTEX,	41.6591,	31.7756,	31.8904,	
# new facet 2/2
	VERTEX,	41.9034,	33.6337,	29.5471,	
# new facet 1/2
	VERTEX,	43.1716,	31.2503,	32.3706,	
# new facet 1/2
	VERTEX,	44.708,	33.774,	32.864,	
# new facet 1/2
	VERTEX,	41.9034,	33.6337,	29.5471,	
# new facet 2/2
	VERTEX,	43.1716,	31.2503,	32.3706,	
# new facet 2/2
	VERTEX,	44.708,	33.774,	32.864,	
# new facet 2/2
	VERTEX,	41.9034,	33.6337,	29.5471,	
# new facet 1/2
	VERTEX,	43.1716,	31.2503,	32.3706,	
# new facet 1/2
	VERTEX,	41.6591,	31.7756,	31.8904,	
# new facet 1/2
	VERTEX,	44.708,	33.774,	32.864,	
# new facet 2/2
	VERTEX,	43.1716,	31.2503,	32.3706,	
# new facet 2/2
	VERTEX,	41.6591,	31.7756,	31.8904,	
# new facet 2/2
	VERTEX,	44.708,	33.774,	32.864,	
# new facet 1/2
	VERTEX,	43.1716,	31.2503,	32.3706,	
# new facet 1/2
	VERTEX,	41.9034,	33.6337,	29.5471,	
# new facet 1/2
	VERTEX,	41.6591,	31.7756,	31.8904,	
# new facet 2/2
	VERTEX,	43.1716,	31.2503,	32.3706,	
# new facet 2/2
	VERTEX,	41.9034,	33.6337,	29.5471,	
# new facet 2/2
	VERTEX,	41.6591,	31.7756,	31.8904,	
# new facet 1/2
	VERTEX,	44.708,	33.774,	32.864,	
# new facet 1/2
	VERTEX,	41.9034,	33.6337,	29.5471,	
# new facet 1/2
	VERTEX,	43.1716,	31.2503,	32.3706,	
# new facet 2/2
	VERTEX,	44.708,	33.774,	32.864,	
# new facet 2/2
	VERTEX,	41.9034,	33.6337,	29.5471,	
# new facet 2/2
	VERTEX,	43.1716,	31.2503,	32.3706,	
# new facet 1/2
	VERTEX,	43.0428,	32.4323,	28.62,	
# new facet 1/2
	VERTEX,	44.708,	33.774,	32.864,	
# new facet 1/2
	VERTEX,	43.1716,	31.2503,	32.3706,	
# new facet 2/2
	VERTEX,	43.0428,	32.4323,	28.62,	
# new facet 2/2
	VERTEX,	44.708,	33.774,	32.864,	
# new facet 2/2
	VERTEX,	43.1716,	31.2503,	32.3706,	
# new facet 1/2
	VERTEX,	43.0428,	32.4323,	28.62,	
# new facet 1/2
	VERTEX,	41.9034,	33.6337,	29.5471,	
# new facet 1/2
	VERTEX,	44.708,	33.774,	32.864,	
# new facet 2/2
	VERTEX,	43.0428,	32.4323,	28.62,	
# new facet 2/2
	VERTEX,	41.9034,	33.6337,	29.5471,	
# new facet 2/2
	VERTEX,	44.708,	33.774,	32.864,	
# new facet 1/2
	VERTEX,	43.0428,	32.4323,	28.62,	
# new facet 1/2
	VERTEX,	43.1716,	31.2503,	32.3706,	
# new facet 1/2
	VERTEX,	41.9034,	33.6337,	29.5471,	
# new facet 2/2
	VERTEX,	43.0428,	32.4323,	28.62,	
# new facet 2/2
	VERTEX,	43.1716,	31.2503,	32.3706,	
# new facet 2/2
	VERTEX,	41.9034,	33.6337,	29.5471,	
# new polyhedron
# new facet 1/2
	VERTEX,	42.288,	36.217,	28.639,	
# new facet 1/2
	VERTEX,	42.6053,	33.7068,	28.2191,	
# new facet 1/2
	VERTEX,	45.3558,	34.8358,	28.4306,	
# new facet 2/2
	VERTEX,	42.288,	36.217,	28.639,	
# new facet 2/2
	VERTEX,	42.6053,	33.7068,	28.2191,	
# new facet 2/2
	VERTEX,	45.3558,	34.8358,	28.4306,	
# new facet 1/2
	VERTEX,	44.708,	33.774,	32.864,	
# new facet 1/2
	VERTEX,	42.288,	36.217,	28.639,	
# new facet 1/2
	VERTEX,	45.3558,	34.8358,	28.4306,	
# new facet 2/2
	VERTEX,	44.708,	33.774,	32.864,	
# new facet 2/2
	VERTEX,	42.288,	36.217,	28.639,	
# new facet 2/2
	VERTEX,	45.3558,	34.8358,	28.4306,	
# new facet 1/2
	VERTEX,	44.708,	33.774,	32.864,	
# new facet 1/2
	VERTEX,	42.6053,	33.7068,	28.2191,	
# new facet 1/2
	VERTEX,	42.288,	36.217,	28.639,	
# new facet 2/2
	VERTEX,	44.708,	33.774,	32.864,	
# new facet 2/2
	VERTEX,	42.6053,	33.7068,	28.2191,	
# new facet 2/2
	VERTEX,	42.288,	36.217,	28.639,	
# new facet 1/2
	VERTEX,	44.708,	33.774,	32.864,	
# new facet 1/2
	VERTEX,	45.3558,	34.8358,	28.4306,	
# new facet 1/2
	VERTEX,	42.6053,	33.7068,	28.2191,	
# new facet 2/2
	VERTEX,	44.708,	33.774,	32.864,	
# new facet 2/2
	VERTEX,	45.3558,	34.8358,	28.4306,	
# new facet 2/2
	VERTEX,	42.6053,	33.7068,	28.2191,	
# new facet 1/2
	VERTEX,	44.708,	33.774,	32.864,	
# new facet 1/2
	VERTEX,	42.6053,	33.7068,	28.2191,	
# new facet 1/2
	VERTEX,	45.3558,	34.8358,	28.4306,	
# new facet 2/2
	VERTEX,	44.708,	33.774,	32.864,	
# new facet 2/2
	VERTEX,	42.6053,	33.7068,	28.2191,	
# new facet 2/2
	VERTEX,	45.3558,	34.8358,	28.4306,	
# new facet 1/2
	VERTEX,	43.0438,	32.4267,	28.5871,	
# new facet 1/2
	VERTEX,	44.708,	33.774,	32.864,	
# new facet 1/2
	VERTEX,	45.3558,	34.8358,	28.4306,	
# new facet 2/2
	VERTEX,	43.0438,	32.4267,	28.5871,	
# new facet 2/2
	VERTEX,	44.708,	33.774,	32.864,	
# new facet 2/2
	VERTEX,	45.3558,	34.8358,	28.4306,	
# new facet 1/2
	VERTEX,	43.0438,	32.4267,	28.5871,	
# new facet 1/2
	VERTEX,	42.6053,	33.7068,	28.2191,	
# new facet 1/2
	VERTEX,	44.708,	33.774,	32.864,	
# new facet 2/2
	VERTEX,	43.0438,	32.4267,	28.5871,	
# new facet 2/2
	VERTEX,	42.6053,	33.7068,	28.2191,	
# new facet 2/2
	VERTEX,	44.708,	33.774,	32.864,	
# new facet 1/2
	VERTEX,	43.0438,	32.4267,	28.5871,	
# new facet 1/2
	VERTEX,	45.3558,	34.8358,	28.4306,	
# new facet 1/2
	VERTEX,	42.6053,	33.7068,	28.2191,	
# new facet 2/2
	VERTEX,	43.0438,	32.4267,	28.5871,	
# new facet 2/2
	VERTEX,	45.3558,	34.8358,	28.4306,	
# new facet 2/2
	VERTEX,	42.6053,	33.7068,	28.2191,	
# new facet 1/2
	VERTEX,	44.708,	33.774,	32.864,	
# new facet 1/2
	VERTEX,	45.3558,	34.8358,	28.4306,	
# new facet 1/2
	VERTEX,	43.0438,	32.4267,	28.5871,	
# new facet 2/2
	VERTEX,	44.708,	33.774,	32.864,	
# new facet 2/2
	VERTEX,	45.3558,	34.8358,	28.4306,	
# new facet 2/2
	VERTEX,	43.0438,	32.4267,	28.5871,	
# new facet 1/2
	VERTEX,	46.502,	33.7846,	30.1721,	
# new facet 1/2
	VERTEX,	44.708,	33.774,	32.864,	
# new facet 1/2
	VERTEX,	43.0438,	32.4267,	28.5871,	
# new facet 2/2
	VERTEX,	46.502,	33.7846,	30.1721,	
# new facet 2/2
	VERTEX,	44.708,	33.774,	32.864,	
# new facet 2/2
	VERTEX,	43.0438,	32.4267,	28.5871,	
# new facet 1/2
	VERTEX,	46.502,	33.7846,	30.1721,	
# new facet 1/2
	VERTEX,	45.3558,	34.8358,	28.4306,	
# new facet 1/2
	VERTEX,	44.708,	33.774,	32.864,	
# new facet 2/2
	VERTEX,	46.502,	33.7846,	30.1721,	
# new facet 2/2
	VERTEX,	45.3558,	34.8358,	28.4306,	
# new facet 2/2
	VERTEX,	44.708,	33.774,	32.864,	
# new facet 1/2
	VERTEX,	46.502,	33.7846,	30.1721,	
# new facet 1/2
	VERTEX,	43.0438,	32.4267,	28.5871,	
# new facet 1/2
	VERTEX,	45.3558,	34.8358,	28.4306,	
# new facet 2/2
	VERTEX,	46.502,	33.7846,	30.1721,	
# new facet 2/2
	VERTEX,	43.0438,	32.4267,	28.5871,	
# new facet 2/2
	VERTEX,	45.3558,	34.8358,	28.4306,	
# new polyhedron
# new facet 1/2
	VERTEX,	41.136,	44.732,	35.115,	
# new facet 1/2
	VERTEX,	45.909,	43.202,	26.324,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 2/2
	VERTEX,	41.136,	44.732,	35.115,	
# new facet 2/2
	VERTEX,	45.909,	43.202,	26.324,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 1/2
	VERTEX,	38.9026,	43.496,	31.5681,	
# new facet 1/2
	VERTEX,	41.136,	44.732,	35.115,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 2/2
	VERTEX,	38.9026,	43.496,	31.5681,	
# new facet 2/2
	VERTEX,	41.136,	44.732,	35.115,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 1/2
	VERTEX,	38.9026,	43.496,	31.5681,	
# new facet 1/2
	VERTEX,	45.909,	43.202,	26.324,	
# new facet 1/2
	VERTEX,	41.136,	44.732,	35.115,	
# new facet 2/2
	VERTEX,	38.9026,	43.496,	31.5681,	
# new facet 2/2
	VERTEX,	45.909,	43.202,	26.324,	
# new facet 2/2
	VERTEX,	41.136,	44.732,	35.115,	
# new facet 1/2
	VERTEX,	38.9026,	43.496,	31.5681,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 1/2
	VERTEX,	45.909,	43.202,	26.324,	
# new facet 2/2
	VERTEX,	38.9026,	43.496,	31.5681,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 2/2
	VERTEX,	45.909,	43.202,	26.324,	
# new facet 1/2
	VERTEX,	41.136,	44.732,	35.115,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 1/2
	VERTEX,	38.9026,	43.496,	31.5681,	
# new facet 2/2
	VERTEX,	41.136,	44.732,	35.115,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 2/2
	VERTEX,	38.9026,	43.496,	31.5681,	
# new facet 1/2
	VERTEX,	40.8268,	43.3601,	29.905,	
# new facet 1/2
	VERTEX,	41.136,	44.732,	35.115,	
# new facet 1/2
	VERTEX,	38.9026,	43.496,	31.5681,	
# new facet 2/2
	VERTEX,	40.8268,	43.3601,	29.905,	
# new facet 2/2
	VERTEX,	41.136,	44.732,	35.115,	
# new facet 2/2
	VERTEX,	38.9026,	43.496,	31.5681,	
# new facet 1/2
	VERTEX,	40.8268,	43.3601,	29.905,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 1/2
	VERTEX,	41.136,	44.732,	35.115,	
# new facet 2/2
	VERTEX,	40.8268,	43.3601,	29.905,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 2/2
	VERTEX,	41.136,	44.732,	35.115,	
# new facet 1/2
	VERTEX,	40.8268,	43.3601,	29.905,	
# new facet 1/2
	VERTEX,	38.9026,	43.496,	31.5681,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 2/2
	VERTEX,	40.8268,	43.3601,	29.905,	
# new facet 2/2
	VERTEX,	38.9026,	43.496,	31.5681,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 1/2
	VERTEX,	38.9026,	43.496,	31.5681,	
# new facet 1/2
	VERTEX,	40.8268,	43.3601,	29.905,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 2/2
	VERTEX,	38.9026,	43.496,	31.5681,	
# new facet 2/2
	VERTEX,	40.8268,	43.3601,	29.905,	
# new facet 1/2
	VERTEX,	38.9228,	43.3137,	31.4827,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 1/2
	VERTEX,	40.8268,	43.3601,	29.905,	
# new facet 2/2
	VERTEX,	38.9228,	43.3137,	31.4827,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 2/2
	VERTEX,	40.8268,	43.3601,	29.905,	
# new facet 1/2
	VERTEX,	38.9228,	43.3137,	31.4827,	
# new facet 1/2
	VERTEX,	38.9026,	43.496,	31.5681,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 2/2
	VERTEX,	38.9228,	43.3137,	31.4827,	
# new facet 2/2
	VERTEX,	38.9026,	43.496,	31.5681,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.378,	
# new facet 1/2
	VERTEX,	38.9228,	43.3137,	31.4827,	
# new facet 1/2
	VERTEX,	40.8268,	43.3601,	29.905,	
# new facet 1/2
	VERTEX,	38.9026,	43.496,	31.5681,	
# new facet 2/2
	VERTEX,	38.9228,	43.3137,	31.4827,	
# new facet 2/2
	VERTEX,	40.8268,	43.3601,	29.905,	
# new facet 2/2
	VERTEX,	38.9026,	43.496,	31.5681,	
# new polyhedron
# new facet 1/2
	VERTEX,	43.38,	39.632,	35.358,	
# new facet 1/2
	VERTEX,	42.288,	36.237,	28.639,	
# new facet 1/2
	VERTEX,	47.951,	35.799,	30.37,	
# new facet 2/2
	VERTEX,	43.38,	39.632,	35.358,	
# new facet 2/2
	VERTEX,	42.288,	36.237,	28.639,	
# new facet 2/2
	VERTEX,	47.951,	35.799,	30.37,	
# new facet 1/2
	VERTEX,	44.3638,	41.3832,	26.1968,	
# new facet 1/2
	VERTEX,	43.38,	39.632,	35.358,	
# new facet 1/2
	VERTEX,	47.951,	35.799,	30.37,	
# new facet 2/2
	VERTEX,	44.3638,	41.3832,	26.1968,	
# new facet 2/2
	VERTEX,	43.38,	39.632,	35.358,	
# new facet 2/2
	VERTEX,	47.951,	35.799,	30.37,	
# new facet 1/2
	VERTEX,	44.3638,	41.3832,	26.1968,	
# new facet 1/2
	VERTEX,	42.288,	36.237,	28.639,	
# new facet 1/2
	VERTEX,	43.38,	39.632,	35.358,	
# new facet 2/2
	VERTEX,	44.3638,	41.3832,	26.1968,	
# new facet 2/2
	VERTEX,	42.288,	36.237,	28.639,	
# new facet 2/2
	VERTEX,	43.38,	39.632,	35.358,	
# new facet 1/2
	VERTEX,	44.3638,	41.3832,	26.1968,	
# new facet 1/2
	VERTEX,	47.951,	35.799,	30.37,	
# new facet 1/2
	VERTEX,	42.288,	36.237,	28.639,	
# new facet 2/2
	VERTEX,	44.3638,	41.3832,	26.1968,	
# new facet 2/2
	VERTEX,	47.951,	35.799,	30.37,	
# new facet 2/2
	VERTEX,	42.288,	36.237,	28.639,	
# new facet 1/2
	VERTEX,	43.38,	39.632,	35.358,	
# new facet 1/2
	VERTEX,	47.951,	35.799,	30.37,	
# new facet 1/2
	VERTEX,	44.3638,	41.3832,	26.1968,	
# new facet 2/2
	VERTEX,	43.38,	39.632,	35.358,	
# new facet 2/2
	VERTEX,	47.951,	35.799,	30.37,	
# new facet 2/2
	VERTEX,	44.3638,	41.3832,	26.1968,	
# new facet 1/2
	VERTEX,	44.2678,	41.1112,	26.1305,	
# new facet 1/2
	VERTEX,	43.38,	39.632,	35.358,	
# new facet 1/2
	VERTEX,	44.3638,	41.3832,	26.1968,	
# new facet 2/2
	VERTEX,	44.2678,	41.1112,	26.1305,	
# new facet 2/2
	VERTEX,	43.38,	39.632,	35.358,	
# new facet 2/2
	VERTEX,	44.3638,	41.3832,	26.1968,	
# new facet 1/2
	VERTEX,	44.2678,	41.1112,	26.1305,	
# new facet 1/2
	VERTEX,	47.951,	35.799,	30.37,	
# new facet 1/2
	VERTEX,	43.38,	39.632,	35.358,	
# new facet 2/2
	VERTEX,	44.2678,	41.1112,	26.1305,	
# new facet 2/2
	VERTEX,	47.951,	35.799,	30.37,	
# new facet 2/2
	VERTEX,	43.38,	39.632,	35.358,	
# new facet 1/2
	VERTEX,	44.2678,	41.1112,	26.1305,	
# new facet 1/2
	VERTEX,	44.3638,	41.3832,	26.1968,	
# new facet 1/2
	VERTEX,	47.951,	35.799,	30.37,	
# new facet 2/2
	VERTEX,	44.2678,	41.1112,	26.1305,	
# new facet 2/2
	VERTEX,	44.3638,	41.3832,	26.1968,	
# new facet 2/2
	VERTEX,	47.951,	35.799,	30.37,	
# new facet 1/2
	VERTEX,	47.951,	35.799,	30.37,	
# new facet 1/2
	VERTEX,	44.3638,	41.3832,	26.1968,	
# new facet 1/2
	VERTEX,	44.2678,	41.1112,	26.1305,	
# new facet 2/2
	VERTEX,	47.951,	35.799,	30.37,	
# new facet 2/2
	VERTEX,	44.3638,	41.3832,	26.1968,	
# new facet 2/2
	VERTEX,	44.2678,	41.1112,	26.1305,	
# new facet 1/2
	VERTEX,	44.5088,	41.294,	26.092,	
# new facet 1/2
	VERTEX,	47.951,	35.799,	30.37,	
# new facet 1/2
	VERTEX,	44.2678,	41.1112,	26.1305,	
# new facet 2/2
	VERTEX,	44.5088,	41.294,	26.092,	
# new facet 2/2
	VERTEX,	47.951,	35.799,	30.37,	
# new facet 2/2
	VERTEX,	44.2678,	41.1112,	26.1305,	
# new facet 1/2
	VERTEX,	44.5088,	41.294,	26.092,	
# new facet 1/2
	VERTEX,	44.3638,	41.3832,	26.1968,	
# new facet 1/2
	VERTEX,	47.951,	35.799,	30.37,	
# new facet 2/2
	VERTEX,	44.5088,	41.294,	26.092,	
# new facet 2/2
	VERTEX,	44.3638,	41.3832,	26.1968,	
# new facet 2/2
	VERTEX,	47.951,	35.799,	30.37,	
# new facet 1/2
	VERTEX,	44.5088,	41.294,	26.092,	
# new facet 1/2
	VERTEX,	44.2678,	41.1112,	26.1305,	
# new facet 1/2
	VERTEX,	44.3638,	41.3832,	26.1968,	
# new facet 2/2
	VERTEX,	44.5088,	41.294,	26.092,	
# new facet 2/2
	VERTEX,	44.2678,	41.1112,	26.1305,	
# new facet 2/2
	VERTEX,	44.3638,	41.3832,	26.1968,	
# new polyhedron
# new facet 1/2
	VERTEX,	45.919,	43.192,	26.334,	
# new facet 1/2
	VERTEX,	45.6786,	43.4203,	26.4327,	
# new facet 1/2
	VERTEX,	40.8168,	43.3501,	29.895,	
# new facet 2/2
	VERTEX,	45.919,	43.192,	26.334,	
# new facet 2/2
	VERTEX,	45.6786,	43.4203,	26.4327,	
# new facet 2/2
	VERTEX,	40.8168,	43.3501,	29.895,	
# new facet 1/2
	VERTEX,	45.3514,	42.538,	26.1915,	
# new facet 1/2
	VERTEX,	45.919,	43.192,	26.334,	
# new facet 1/2
	VERTEX,	40.8168,	43.3501,	29.895,	
# new facet 2/2
	VERTEX,	45.3514,	42.538,	26.1915,	
# new facet 2/2
	VERTEX,	45.919,	43.192,	26.334,	
# new facet 2/2
	VERTEX,	40.8168,	43.3501,	29.895,	
# new facet 1/2
	VERTEX,	45.3514,	42.538,	26.1915,	
# new facet 1/2
	VERTEX,	45.6786,	43.4203,	26.4327,	
# new facet 1/2
	VERTEX,	45.919,	43.192,	26.334,	
# new facet 2/2
	VERTEX,	45.3514,	42.538,	26.1915,	
# new facet 2/2
	VERTEX,	45.6786,	43.4203,	26.4327,	
# new facet 2/2
	VERTEX,	45.919,	43.192,	26.334,	
# new facet 1/2
	VERTEX,	45.3514,	42.538,	26.1915,	
# new facet 1/2
	VERTEX,	40.8168,	43.3501,	29.895,	
# new facet 1/2
	VERTEX,	45.6786,	43.4203,	26.4327,	
# new facet 2/2
	VERTEX,	45.3514,	42.538,	26.1915,	
# new facet 2/2
	VERTEX,	40.8168,	43.3501,	29.895,	
# new facet 2/2
	VERTEX,	45.6786,	43.4203,	26.4327,	
# new polyhedron
# new facet 1/2
	VERTEX,	43.38,	39.632,	35.358,	
# new facet 1/2
	VERTEX,	48.5055,	36.473,	30.2081,	
# new facet 1/2
	VERTEX,	44.3738,	41.3932,	26.2068,	
# new facet 2/2
	VERTEX,	43.38,	39.632,	35.358,	
# new facet 2/2
	VERTEX,	48.5055,	36.473,	30.2081,	
# new facet 2/2
	VERTEX,	44.3738,	41.3932,	26.2068,	
# new facet 1/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 1/2
	VERTEX,	43.38,	39.632,	35.358,	
# new facet 1/2
	VERTEX,	44.3738,	41.3932,	26.2068,	
# new facet 2/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 2/2
	VERTEX,	43.38,	39.632,	35.358,	
# new facet 2/2
	VERTEX,	44.3738,	41.3932,	26.2068,	
# new facet 1/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 1/2
	VERTEX,	48.5055,	36.473,	30.2081,	
# new facet 1/2
	VERTEX,	43.38,	39.632,	35.358,	
# new facet 2/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 2/2
	VERTEX,	48.5055,	36.473,	30.2081,	
# new facet 2/2
	VERTEX,	43.38,	39.632,	35.358,	
# new facet 1/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 1/2
	VERTEX,	44.3738,	41.3932,	26.2068,	
# new facet 1/2
	VERTEX,	48.5055,	36.473,	30.2081,	
# new facet 2/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 2/2
	VERTEX,	44.3738,	41.3932,	26.2068,	
# new facet 2/2
	VERTEX,	48.5055,	36.473,	30.2081,	
# new facet 1/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 1/2
	VERTEX,	48.5055,	36.473,	30.2081,	
# new facet 1/2
	VERTEX,	44.3738,	41.3932,	26.2068,	
# new facet 2/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 2/2
	VERTEX,	48.5055,	36.473,	30.2081,	
# new facet 2/2
	VERTEX,	44.3738,	41.3932,	26.2068,	
# new facet 1/2
	VERTEX,	49.7995,	38.0702,	30.3538,	
# new facet 1/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 1/2
	VERTEX,	44.3738,	41.3932,	26.2068,	
# new facet 2/2
	VERTEX,	49.7995,	38.0702,	30.3538,	
# new facet 2/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 2/2
	VERTEX,	44.3738,	41.3932,	26.2068,	
# new facet 1/2
	VERTEX,	49.7995,	38.0702,	30.3538,	
# new facet 1/2
	VERTEX,	48.5055,	36.473,	30.2081,	
# new facet 1/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 2/2
	VERTEX,	49.7995,	38.0702,	30.3538,	
# new facet 2/2
	VERTEX,	48.5055,	36.473,	30.2081,	
# new facet 2/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 1/2
	VERTEX,	49.7995,	38.0702,	30.3538,	
# new facet 1/2
	VERTEX,	44.3738,	41.3932,	26.2068,	
# new facet 1/2
	VERTEX,	48.5055,	36.473,	30.2081,	
# new facet 2/2
	VERTEX,	49.7995,	38.0702,	30.3538,	
# new facet 2/2
	VERTEX,	44.3738,	41.3932,	26.2068,	
# new facet 2/2
	VERTEX,	48.5055,	36.473,	30.2081,	
# new facet 1/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 1/2
	VERTEX,	44.3738,	41.3932,	26.2068,	
# new facet 1/2
	VERTEX,	49.7995,	38.0702,	30.3538,	
# new facet 2/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 2/2
	VERTEX,	44.3738,	41.3932,	26.2068,	
# new facet 2/2
	VERTEX,	49.7995,	38.0702,	30.3538,	
# new facet 1/2
	VERTEX,	44.6009,	41.4178,	26.1102,	
# new facet 1/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 1/2
	VERTEX,	49.7995,	38.0702,	30.3538,	
# new facet 2/2
	VERTEX,	44.6009,	41.4178,	26.1102,	
# new facet 2/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 2/2
	VERTEX,	49.7995,	38.0702,	30.3538,	
# new facet 1/2
	VERTEX,	44.6009,	41.4178,	26.1102,	
# new facet 1/2
	VERTEX,	44.3738,	41.3932,	26.2068,	
# new facet 1/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 2/2
	VERTEX,	44.6009,	41.4178,	26.1102,	
# new facet 2/2
	VERTEX,	44.3738,	41.3932,	26.2068,	
# new facet 2/2
	VERTEX,	50.95,	39.907,	30.67,	
# new facet 1/2
	VERTEX,	44.6009,	41.4178,	26.1102,	
# new facet 1/2
	VERTEX,	49.7995,	38.0702,	30.3538,	
# new facet 1/2
	VERTEX,	44.3738,	41.3932,	26.2068,	
# new facet 2/2
	VERTEX,	44.6009,	41.4178,	26.1102,	
# new facet 2/2
	VERTEX,	49.7995,	38.0702,	30.3538,	
# new facet 2/2
	VERTEX,	44.3738,	41.3932,	26.2068,	
# new polyhedron
# new facet 1/2
	VERTEX,	45.909,	43.182,	26.324,	
# new facet 1/2
	VERTEX,	45.2496,	44.0506,	26.9852,	
# new facet 1/2
	VERTEX,	40.8268,	43.3601,	29.905,	
# new facet 2/2
	VERTEX,	45.909,	43.182,	26.324,	
# new facet 2/2
	VERTEX,	45.2496,	44.0506,	26.9852,	
# new facet 2/2
	VERTEX,	40.8268,	43.3601,	29.905,	
# new facet 1/2
	VERTEX,	42.832,	47.987,	33.199,	
# new facet 1/2
	VERTEX,	45.909,	43.182,	26.324,	
# new facet 1/2
	VERTEX,	40.8268,	43.3601,	29.905,	
# new facet 2/2
	VERTEX,	42.832,	47.987,	33.199,	
# new facet 2/2
	VERTEX,	45.909,	43.182,	26.324,	
# new facet 2/2
	VERTEX,	40.8268,	43.3601,	29.905,	
# new facet 1/2
	VERTEX,	42.832,	47.987,	33.199,	
# new facet 1/2
	VERTEX,	45.2496,	44.0506,	26.9852,	
# new facet 1/2
	VERTEX,	45.909,	43.182,	26.324,	
# new facet 2/2
	VERTEX,	42.832,	47.987,	33.199,	
# new facet 2/2
	VERTEX,	45.2496,	44.0506,	26.9852,	
# new facet 2/2
	VERTEX,	45.909,	43.182,	26.324,	
# new facet 1/2
	VERTEX,	42.832,	47.987,	33.199,	
# new facet 1/2
	VERTEX,	40.8268,	43.3601,	29.905,	
# new facet 1/2
	VERTEX,	45.2496,	44.0506,	26.9852,	
# new facet 2/2
	VERTEX,	42.832,	47.987,	33.199,	
# new facet 2/2
	VERTEX,	40.8268,	43.3601,	29.905,	
# new facet 2/2
	VERTEX,	45.2496,	44.0506,	26.9852,	
# new facet 1/2
	VERTEX,	42.832,	47.987,	33.199,	
# new facet 1/2
	VERTEX,	45.2496,	44.0506,	26.9852,	
# new facet 1/2
	VERTEX,	40.8268,	43.3601,	29.905,	
# new facet 2/2
	VERTEX,	42.832,	47.987,	33.199,	
# new facet 2/2
	VERTEX,	45.2496,	44.0506,	26.9852,	
# new facet 2/2
	VERTEX,	40.8268,	43.3601,	29.905,	
# new facet 1/2
	VERTEX,	42.2963,	48.1631,	31.1899,	
# new facet 1/2
	VERTEX,	42.832,	47.987,	33.199,	
# new facet 1/2
	VERTEX,	40.8268,	43.3601,	29.905,	
# new facet 2/2
	VERTEX,	42.2963,	48.1631,	31.1899,	
# new facet 2/2
	VERTEX,	42.832,	47.987,	33.199,	
# new facet 2/2
	VERTEX,	40.8268,	43.3601,	29.905,	
# new facet 1/2
	VERTEX,	42.2963,	48.1631,	31.1899,	
# new facet 1/2
	VERTEX,	45.2496,	44.0506,	26.9852,	
# new facet 1/2
	VERTEX,	42.832,	47.987,	33.199,	
# new facet 2/2
	VERTEX,	42.2963,	48.1631,	31.1899,	
# new facet 2/2
	VERTEX,	45.2496,	44.0506,	26.9852,	
# new facet 2/2
	VERTEX,	42.832,	47.987,	33.199,	
# new facet 1/2
	VERTEX,	42.2963,	48.1631,	31.1899,	
# new facet 1/2
	VERTEX,	40.8268,	43.3601,	29.905,	
# new facet 1/2
	VERTEX,	45.2496,	44.0506,	26.9852,	
# new facet 2/2
	VERTEX,	42.2963,	48.1631,	31.1899,	
# new facet 2/2
	VERTEX,	40.8268,	43.3601,	29.905,	
# new facet 2/2
	VERTEX,	45.2496,	44.0506,	26.9852,	
# new facet 1/2
	VERTEX,	42.832,	47.987,	33.199,	
# new facet 1/2
	VERTEX,	40.8268,	43.3601,	29.905,	
# new facet 1/2
	VERTEX,	42.2963,	48.1631,	31.1899,	
# new facet 2/2
	VERTEX,	42.832,	47.987,	33.199,	
# new facet 2/2
	VERTEX,	40.8268,	43.3601,	29.905,	
# new facet 2/2
	VERTEX,	42.2963,	48.1631,	31.1899,	
# new facet 1/2
	VERTEX,	39.2265,	43.937,	31.5666,	
# new facet 1/2
	VERTEX,	42.832,	47.987,	33.199,	
# new facet 1/2
	VERTEX,	42.2963,	48.1631,	31.1899,	
# new facet 2/2
	VERTEX,	39.2265,	43.937,	31.5666,	
# new facet 2/2
	VERTEX,	42.832,	47.987,	33.199,	
# new facet 2/2
	VERTEX,	42.2963,	48.1631,	31.1899,	
# new facet 1/2
	VERTEX,	39.2265,	43.937,	31.5666,	
# new facet 1/2
	VERTEX,	40.8268,	43.3601,	29.905,	
# new facet 1/2
	VERTEX,	42.832,	47.987,	33.199,	
# new facet 2/2
	VERTEX,	39.2265,	43.937,	31.5666,	
# new facet 2/2
	VERTEX,	40.8268,	43.3601,	29.905,	
# new facet 2/2
	VERTEX,	42.832,	47.987,	33.199,	
# new facet 1/2
	VERTEX,	39.2265,	43.937,	31.5666,	
# new facet 1/2
	VERTEX,	42.2963,	48.1631,	31.1899,	
# new facet 1/2
	VERTEX,	40.8268,	43.3601,	29.905,	
# new facet 2/2
	VERTEX,	39.2265,	43.937,	31.5666,	
# new facet 2/2
	VERTEX,	42.2963,	48.1631,	31.1899,	
# new facet 2/2
	VERTEX,	40.8268,	43.3601,	29.905,	
# new polyhedron
# new facet 1/2
	VERTEX,	42.289,	36.24,	28.634,	
# new facet 1/2
	VERTEX,	42.6216,	38.8752,	26.0618,	
# new facet 1/2
	VERTEX,	39.0344,	42.8469,	31.1206,	
# new facet 2/2
	VERTEX,	42.289,	36.24,	28.634,	
# new facet 2/2
	VERTEX,	42.6216,	38.8752,	26.0618,	
# new facet 2/2
	VERTEX,	39.0344,	42.8469,	31.1206,	
# new facet 1/2
	VERTEX,	44.2564,	41.0999,	26.1207,	
# new facet 1/2
	VERTEX,	42.289,	36.24,	28.634,	
# new facet 1/2
	VERTEX,	39.0344,	42.8469,	31.1206,	
# new facet 2/2
	VERTEX,	44.2564,	41.0999,	26.1207,	
# new facet 2/2
	VERTEX,	42.289,	36.24,	28.634,	
# new facet 2/2
	VERTEX,	39.0344,	42.8469,	31.1206,	
# new facet 1/2
	VERTEX,	44.2564,	41.0999,	26.1207,	
# new facet 1/2
	VERTEX,	42.6216,	38.8752,	26.0618,	
# new facet 1/2
	VERTEX,	42.289,	36.24,	28.634,	
# new facet 2/2
	VERTEX,	44.2564,	41.0999,	26.1207,	
# new facet 2/2
	VERTEX,	42.6216,	38.8752,	26.0618,	
# new facet 2/2
	VERTEX,	42.289,	36.24,	28.634,	
# new facet 1/2
	VERTEX,	44.2564,	41.0999,	26.1207,	
# new facet 1/2
	VERTEX,	39.0344,	42.8469,	31.1206,	
# new facet 1/2
	VERTEX,	42.6216,	38.8752,	26.0618,	
# new facet 2/2
	VERTEX,	44.2564,	41.0999,	26.1207,	
# new facet 2/2
	VERTEX,	39.0344,	42.8469,	31.1206,	
# new facet 2/2
	VERTEX,	42.6216,	38.8752,	26.0618,	
# new polyhedron
# new facet 1/2
	VERTEX,	45.909,	43.182,	26.324,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 1/2
	VERTEX,	50.95,	39.907,	30.69,	
# new facet 2/2
	VERTEX,	45.909,	43.182,	26.324,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 2/2
	VERTEX,	50.95,	39.907,	30.69,	
# new facet 1/2
	VERTEX,	45.3514,	42.538,	26.1915,	
# new facet 1/2
	VERTEX,	45.909,	43.182,	26.324,	
# new facet 1/2
	VERTEX,	50.95,	39.907,	30.69,	
# new facet 2/2
	VERTEX,	45.3514,	42.538,	26.1915,	
# new facet 2/2
	VERTEX,	45.909,	43.182,	26.324,	
# new facet 2/2
	VERTEX,	50.95,	39.907,	30.69,	
# new facet 1/2
	VERTEX,	45.3514,	42.538,	26.1915,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 1/2
	VERTEX,	45.909,	43.182,	26.324,	
# new facet 2/2
	VERTEX,	45.3514,	42.538,	26.1915,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 2/2
	VERTEX,	45.909,	43.182,	26.324,	
# new facet 1/2
	VERTEX,	45.3514,	42.538,	26.1915,	
# new facet 1/2
	VERTEX,	50.95,	39.907,	30.69,	
# new facet 1/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 2/2
	VERTEX,	45.3514,	42.538,	26.1915,	
# new facet 2/2
	VERTEX,	50.95,	39.907,	30.69,	
# new facet 2/2
	VERTEX,	43.38,	39.652,	35.358,	
# new facet 1/2
	VERTEX,	45.909,	43.182,	26.324,	
# new facet 1/2
	VERTEX,	50.95,	39.907,	30.69,	
# new facet 1/2
	VERTEX,	45.3514,	42.538,	26.1915,	
# new facet 2/2
	VERTEX,	45.909,	43.182,	26.324,	
# new facet 2/2
	VERTEX,	50.95,	39.907,	30.69,	
# new facet 2/2
	VERTEX,	45.3514,	42.538,	26.1915,	
# new facet 1/2
	VERTEX,	44.3738,	41.3932,	26.2068,	
# new facet 1/2
	VERTEX,	45.909,	43.182,	26.324,	
# new facet 1/2
	VERTEX,	45.3514,	42.538,	26.1915,	
# new facet 2/2
	VERTEX,	44.3738,	41.3932,	26.2068,	
# new facet 2/2
	VERTEX,	45.909,	43.182,	26.324,	
# new facet 2/2
	VERTEX,	45.3514,	42.538,	26.1915,	
# new facet 1/2
	VERTEX,	44.3738,	41.3932,	26.2068,	
# new facet 1/2
	VERTEX,	50.95,	39.907,	30.69,	
# new facet 1/2
	VERTEX,	45.909,	43.182,	26.324,	
# new facet 2/2
	VERTEX,	44.3738,	41.3932,	26.2068,	
# new facet 2/2
	VERTEX,	50.95,	39.907,	30.69,	
# new facet 2/2
	VERTEX,	45.909,	43.182,	26.324,	
# new facet 1/2
	VERTEX,	44.3738,	41.3932,	26.2068,	
# new facet 1/2
	VERTEX,	45.3514,	42.538,	26.1915,	
# new facet 1/2
	VERTEX,	50.95,	39.907,	30.69,	
# new facet 2/2
	VERTEX,	44.3738,	41.3932,	26.2068,	
# new facet 2/2
	VERTEX,	45.3514,	42.538,	26.1915,	
# new facet 2/2
	VERTEX,	50.95,	39.907,	30.69,	
# new facet 1/2
	VERTEX,	50.95,	39.907,	30.69,	
# new facet 1/2
	VERTEX,	45.3514,	42.538,	26.1915,	
# new facet 1/2
	VERTEX,	44.3738,	41.3932,	26.2068,	
# new facet 2/2
	VERTEX,	50.95,	39.907,	30.69,	
# new facet 2/2
	VERTEX,	45.3514,	42.538,	26.1915,	
# new facet 2/2
	VERTEX,	44.3738,	41.3932,	26.2068,	
# new facet 1/2
	VERTEX,	44.5909,	41.4078,	26.1002,	
# new facet 1/2
	VERTEX,	50.95,	39.907,	30.69,	
# new facet 1/2
	VERTEX,	44.3738,	41.3932,	26.2068,	
# new facet 2/2
	VERTEX,	44.5909,	41.4078,	26.1002,	
# new facet 2/2
	VERTEX,	50.95,	39.907,	30.69,	
# new facet 2/2
	VERTEX,	44.3738,	41.3932,	26.2068,	
# new facet 1/2
	VERTEX,	44.5909,	41.4078,	26.1002,	
# new facet 1/2
	VERTEX,	45.3514,	42.538,	26.1915,	
# new facet 1/2
	VERTEX,	50.95,	39.907,	30.69,	
# new facet 2/2
	VERTEX,	44.5909,	41.4078,	26.1002,	
# new facet 2/2
	VERTEX,	45.3514,	42.538,	26.1915,	
# new facet 2/2
	VERTEX,	50.95,	39.907,	30.69,	
# new facet 1/2
	VERTEX,	44.5909,	41.4078,	26.1002,	
# new facet 1/2
	VERTEX,	44.3738,	41.3932,	26.2068,	
# new facet 1/2
	VERTEX,	45.3514,	42.538,	26.1915,	
# new facet 2/2
	VERTEX,	44.5909,	41.4078,	26.1002,	
# new facet 2/2
	VERTEX,	44.3738,	41.3932,	26.2068,	
# new facet 2/2
	VERTEX,	45.3514,	42.538,	26.1915,	
# new polyhedron
# new facet 1/2
	VERTEX,	50.95,	39.887,	30.67,	
# new facet 1/2
	VERTEX,	50.9455,	40.2608,	29.9353,	
# new facet 1/2
	VERTEX,	50.4468,	39.1149,	30.2472,	
# new facet 2/2
	VERTEX,	50.95,	39.887,	30.67,	
# new facet 2/2
	VERTEX,	50.9455,	40.2608,	29.9353,	
# new facet 2/2
	VERTEX,	50.4468,	39.1149,	30.2472,	
# new facet 1/2
	VERTEX,	45.909,	43.202,	26.324,	
# new facet 1/2
	VERTEX,	50.95,	39.887,	30.67,	
# new facet 1/2
	VERTEX,	50.4468,	39.1149,	30.2472,	
# new facet 2/2
	VERTEX,	45.909,	43.202,	26.324,	
# new facet 2/2
	VERTEX,	50.95,	39.887,	30.67,	
# new facet 2/2
	VERTEX,	50.4468,	39.1149,	30.2472,	
# new facet 1/2
	VERTEX,	45.909,	43.202,	26.324,	
# new facet 1/2
	VERTEX,	50.9455,	40.2608,	29.9353,	
# new facet 1/2
	VERTEX,	50.95,	39.887,	30.67,	
# new facet 2/2
	VERTEX,	45.909,	43.202,	26.324,	
# new facet 2/2
	VERTEX,	50.9455,	40.2608,	29.9353,	
# new facet 2/2
	VERTEX,	50.95,	39.887,	30.67,	
# new facet 1/2
	VERTEX,	45.909,	43.202,	26.324,	
# new facet 1/2
	VERTEX,	50.4468,	39.1149,	30.2472,	
# new facet 1/2
	VERTEX,	50.9455,	40.2608,	29.9353,	
# new facet 2/2
	VERTEX,	45.909,	43.202,	26.324,	
# new facet 2/2
	VERTEX,	50.4468,	39.1149,	30.2472,	
# new facet 2/2
	VERTEX,	50.9455,	40.2608,	29.9353,	
# new facet 1/2
	VERTEX,	45.909,	43.202,	26.324,	
# new facet 1/2
	VERTEX,	50.9455,	40.2608,	29.9353,	
# new facet 1/2
	VERTEX,	50.4468,	39.1149,	30.2472,	
# new facet 2/2
	VERTEX,	45.909,	43.202,	26.324,	
# new facet 2/2
	VERTEX,	50.9455,	40.2608,	29.9353,	
# new facet 2/2
	VERTEX,	50.4468,	39.1149,	30.2472,	
# new facet 1/2
	VERTEX,	48.8477,	42.4267,	26.5556,	
# new facet 1/2
	VERTEX,	45.909,	43.202,	26.324,	
# new facet 1/2
	VERTEX,	50.4468,	39.1149,	30.2472,	
# new facet 2/2
	VERTEX,	48.8477,	42.4267,	26.5556,	
# new facet 2/2
	VERTEX,	45.909,	43.202,	26.324,	
# new facet 2/2
	VERTEX,	50.4468,	39.1149,	30.2472,	
# new facet 1/2
	VERTEX,	48.8477,	42.4267,	26.5556,	
# new facet 1/2
	VERTEX,	50.9455,	40.2608,	29.9353,	
# new facet 1/2
	VERTEX,	45.909,	43.202,	26.324,	
# new facet 2/2
	VERTEX,	48.8477,	42.4267,	26.5556,	
# new facet 2/2
	VERTEX,	50.9455,	40.2608,	29.9353,	
# new facet 2/2
	VERTEX,	45.909,	43.202,	26.324,	
# new facet 1/2
	VERTEX,	48.8477,	42.4267,	26.5556,	
# new facet 1/2
	VERTEX,	50.4468,	39.1149,	30.2472,	
# new facet 1/2
	VERTEX,	50.9455,	40.2608,	29.9353,	
# new facet 2/2
	VERTEX,	48.8477,	42.4267,	26.5556,	
# new facet 2/2
	VERTEX,	50.4468,	39.1149,	30.2472,	
# new facet 2/2
	VERTEX,	50.9455,	40.2608,	29.9353,	
# new facet 1/2
	VERTEX,	45.909,	43.202,	26.324,	
# new facet 1/2
	VERTEX,	50.4468,	39.1149,	30.2472,	
# new facet 1/2
	VERTEX,	48.8477,	42.4267,	26.5556,	
# new facet 2/2
	VERTEX,	45.909,	43.202,	26.324,	
# new facet 2/2
	VERTEX,	50.4468,	39.1149,	30.2472,	
# new facet 2/2
	VERTEX,	48.8477,	42.4267,	26.5556,	
# new facet 1/2
	VERTEX,	48.0133,	38.876,	28.1657,	
# new facet 1/2
	VERTEX,	45.909,	43.202,	26.324,	
# new facet 1/2
	VERTEX,	48.8477,	42.4267,	26.5556,	
# new facet 2/2
	VERTEX,	48.0133,	38.876,	28.1657,	
# new facet 2/2
	VERTEX,	45.909,	43.202,	26.324,	
# new facet 2/2
	VERTEX,	48.8477,	42.4267,	26.5556,	
# new facet 1/2
	VERTEX,	48.0133,	38.876,	28.1657,	
# new facet 1/2
	VERTEX,	50.4468,	39.1149,	30.2472,	
# new facet 1/2
	VERTEX,	45.909,	43.202,	26.324,	
# new facet 2/2
	VERTEX,	48.0133,	38.876,	28.1657,	
# new facet 2/2
	VERTEX,	50.4468,	39.1149,	30.2472,	
# new facet 2/2
	VERTEX,	45.909,	43.202,	26.324,	
# new facet 1/2
	VERTEX,	48.0133,	38.876,	28.1657,	
# new facet 1/2
	VERTEX,	48.8477,	42.4267,	26.5556,	
# new facet 1/2
	VERTEX,	50.4468,	39.1149,	30.2472,	
# new facet 2/2
	VERTEX,	48.0133,	38.876,	28.1657,	
# new facet 2/2
	VERTEX,	48.8477,	42.4267,	26.5556,	
# new facet 2/2
	VERTEX,	50.4468,	39.1149,	30.2472,	
# new polyhedron
# new facet 1/2
	VERTEX,	49.666,	51.417,	30.412,	
# new facet 1/2
	VERTEX,	54.3323,	52.235,	26.7446,	
# new facet 1/2
	VERTEX,	49.4986,	51.2739,	28.0586,	
# new facet 2/2
	VERTEX,	49.666,	51.417,	30.412,	
# new facet 2/2
	VERTEX,	54.3323,	52.235,	26.7446,	
# new facet 2/2
	VERTEX,	49.4986,	51.2739,	28.0586,	
# new facet 1/2
	VERTEX,	53.5401,	50.446,	29.1074,	
# new facet 1/2
	VERTEX,	49.666,	51.417,	30.412,	
# new facet 1/2
	VERTEX,	49.4986,	51.2739,	28.0586,	
# new facet 2/2
	VERTEX,	53.5401,	50.446,	29.1074,	
# new facet 2/2
	VERTEX,	49.666,	51.417,	30.412,	
# new facet 2/2
	VERTEX,	49.4986,	51.2739,	28.0586,	
# new facet 1/2
	VERTEX,	53.5401,	50.446,	29.1074,	
# new facet 1/2
	VERTEX,	54.3323,	52.235,	26.7446,	
# new facet 1/2
	VERTEX,	49.666,	51.417,	30.412,	
# new facet 2/2
	VERTEX,	53.5401,	50.446,	29.1074,	
# new facet 2/2
	VERTEX,	54.3323,	52.235,	26.7446,	
# new facet 2/2
	VERTEX,	49.666,	51.417,	30.412,	
# new facet 1/2
	VERTEX,	53.5401,	50.446,	29.1074,	
# new facet 1/2
	VERTEX,	49.4986,	51.2739,	28.0586,	
# new facet 1/2
	VERTEX,	54.3323,	52.235,	26.7446,	
# new facet 2/2
	VERTEX,	53.5401,	50.446,	29.1074,	
# new facet 2/2
	VERTEX,	49.4986,	51.2739,	28.0586,	
# new facet 2/2
	VERTEX,	54.3323,	52.235,	26.7446,	
# new polyhedron
# new facet 1/2
	VERTEX,	49.666,	51.417,	30.412,	
# new facet 1/2
	VERTEX,	49.4986,	51.2739,	28.0586,	
# new facet 1/2
	VERTEX,	49.8099,	47.7979,	26.1903,	
# new facet 2/2
	VERTEX,	49.666,	51.417,	30.412,	
# new facet 2/2
	VERTEX,	49.4986,	51.2739,	28.0586,	
# new facet 2/2
	VERTEX,	49.8099,	47.7979,	26.1903,	
# new facet 1/2
	VERTEX,	53.5401,	50.446,	29.1074,	
# new facet 1/2
	VERTEX,	49.666,	51.417,	30.412,	
# new facet 1/2
	VERTEX,	49.8099,	47.7979,	26.1903,	
# new facet 2/2
	VERTEX,	53.5401,	50.446,	29.1074,	
# new facet 2/2
	VERTEX,	49.666,	51.417,	30.412,	
# new facet 2/2
	VERTEX,	49.8099,	47.7979,	26.1903,	
# new facet 1/2
	VERTEX,	53.5401,	50.446,	29.1074,	
# new facet 1/2
	VERTEX,	49.4986,	51.2739,	28.0586,	
# new facet 1/2
	VERTEX,	49.666,	51.417,	30.412,	
# new facet 2/2
	VERTEX,	53.5401,	50.446,	29.1074,	
# new facet 2/2
	VERTEX,	49.4986,	51.2739,	28.0586,	
# new facet 2/2
	VERTEX,	49.666,	51.417,	30.412,	
# new facet 1/2
	VERTEX,	53.5401,	50.446,	29.1074,	
# new facet 1/2
	VERTEX,	49.8099,	47.7979,	26.1903,	
# new facet 1/2
	VERTEX,	49.4986,	51.2739,	28.0586,	
# new facet 2/2
	VERTEX,	53.5401,	50.446,	29.1074,	
# new facet 2/2
	VERTEX,	49.8099,	47.7979,	26.1903,	
# new facet 2/2
	VERTEX,	49.4986,	51.2739,	28.0586,	
# new polyhedron
# new facet 1/2
	VERTEX,	49.656,	51.406,	30.423,	
# new facet 1/2
	VERTEX,	46.028,	50.5609,	29.7032,	
# new facet 1/2
	VERTEX,	49.8093,	47.7961,	26.1898,	
# new facet 2/2
	VERTEX,	49.656,	51.406,	30.423,	
# new facet 2/2
	VERTEX,	46.028,	50.5609,	29.7032,	
# new facet 2/2
	VERTEX,	49.8093,	47.7961,	26.1898,	
# new facet 1/2
	VERTEX,	49.4938,	51.2687,	28.0588,	
# new facet 1/2
	VERTEX,	49.656,	51.406,	30.423,	
# new facet 1/2
	VERTEX,	49.8093,	47.7961,	26.1898,	
# new facet 2/2
	VERTEX,	49.4938,	51.2687,	28.0588,	
# new facet 2/2
	VERTEX,	49.656,	51.406,	30.423,	
# new facet 2/2
	VERTEX,	49.8093,	47.7961,	26.1898,	
# new facet 1/2
	VERTEX,	49.4938,	51.2687,	28.0588,	
# new facet 1/2
	VERTEX,	46.028,	50.5609,	29.7032,	
# new facet 1/2
	VERTEX,	49.656,	51.406,	30.423,	
# new facet 2/2
	VERTEX,	49.4938,	51.2687,	28.0588,	
# new facet 2/2
	VERTEX,	46.028,	50.5609,	29.7032,	
# new facet 2/2
	VERTEX,	49.656,	51.406,	30.423,	
# new facet 1/2
	VERTEX,	49.4938,	51.2687,	28.0588,	
# new facet 1/2
	VERTEX,	49.8093,	47.7961,	26.1898,	
# new facet 1/2
	VERTEX,	46.028,	50.5609,	29.7032,	
# new facet 2/2
	VERTEX,	49.4938,	51.2687,	28.0588,	
# new facet 2/2
	VERTEX,	49.8093,	47.7961,	26.1898,	
# new facet 2/2
	VERTEX,	46.028,	50.5609,	29.7032,	
# new polyhedron
# new facet 1/2
	VERTEX,	52.635,	47.828,	31.503,	
# new facet 1/2
	VERTEX,	53.5411,	47.2116,	28.3452,	
# new facet 1/2
	VERTEX,	49.8866,	47.5497,	26.0257,	
# new facet 2/2
	VERTEX,	52.635,	47.828,	31.503,	
# new facet 2/2
	VERTEX,	53.5411,	47.2116,	28.3452,	
# new facet 2/2
	VERTEX,	49.8866,	47.5497,	26.0257,	
# new facet 1/2
	VERTEX,	52.8118,	47.9768,	31.3016,	
# new facet 1/2
	VERTEX,	52.635,	47.828,	31.503,	
# new facet 1/2
	VERTEX,	49.8866,	47.5497,	26.0257,	
# new facet 2/2
	VERTEX,	52.8118,	47.9768,	31.3016,	
# new facet 2/2
	VERTEX,	52.635,	47.828,	31.503,	
# new facet 2/2
	VERTEX,	49.8866,	47.5497,	26.0257,	
# new facet 1/2
	VERTEX,	52.8118,	47.9768,	31.3016,	
# new facet 1/2
	VERTEX,	53.5411,	47.2116,	28.3452,	
# new facet 1/2
	VERTEX,	52.635,	47.828,	31.503,	
# new facet 2/2
	VERTEX,	52.8118,	47.9768,	31.3016,	
# new facet 2/2
	VERTEX,	53.5411,	47.2116,	28.3452,	
# new facet 2/2
	VERTEX,	52.635,	47.828,	31.503,	
# new facet 1/2
	VERTEX,	52.8118,	47.9768,	31.3016,	
# new facet 1/2
	VERTEX,	49.8866,	47.5497,	26.0257,	
# new facet 1/2
	VERTEX,	53.5411,	47.2116,	28.3452,	
# new facet 2/2
	VERTEX,	52.8118,	47.9768,	31.3016,	
# new facet 2/2
	VERTEX,	49.8866,	47.5497,	26.0257,	
# new facet 2/2
	VERTEX,	53.5411,	47.2116,	28.3452,	
# new polyhedron
# new facet 1/2
	VERTEX,	47.454,	44.603,	26.246,	
# new facet 1/2
	VERTEX,	47.433,	44.883,	26.1371,	
# new facet 1/2
	VERTEX,	46.7768,	46.2338,	27.1811,	
# new facet 2/2
	VERTEX,	47.454,	44.603,	26.246,	
# new facet 2/2
	VERTEX,	47.433,	44.883,	26.1371,	
# new facet 2/2
	VERTEX,	46.7768,	46.2338,	27.1811,	
# new facet 1/2
	VERTEX,	49.167,	45.973,	26.2,	
# new facet 1/2
	VERTEX,	47.454,	44.603,	26.246,	
# new facet 1/2
	VERTEX,	46.7768,	46.2338,	27.1811,	
# new facet 2/2
	VERTEX,	49.167,	45.973,	26.2,	
# new facet 2/2
	VERTEX,	47.454,	44.603,	26.246,	
# new facet 2/2
	VERTEX,	46.7768,	46.2338,	27.1811,	
# new facet 1/2
	VERTEX,	49.167,	45.973,	26.2,	
# new facet 1/2
	VERTEX,	47.433,	44.883,	26.1371,	
# new facet 1/2
	VERTEX,	47.454,	44.603,	26.246,	
# new facet 2/2
	VERTEX,	49.167,	45.973,	26.2,	
# new facet 2/2
	VERTEX,	47.433,	44.883,	26.1371,	
# new facet 2/2
	VERTEX,	47.454,	44.603,	26.246,	
# new facet 1/2
	VERTEX,	49.167,	45.973,	26.2,	
# new facet 1/2
	VERTEX,	46.7768,	46.2338,	27.1811,	
# new facet 1/2
	VERTEX,	47.433,	44.883,	26.1371,	
# new facet 2/2
	VERTEX,	49.167,	45.973,	26.2,	
# new facet 2/2
	VERTEX,	46.7768,	46.2338,	27.1811,	
# new facet 2/2
	VERTEX,	47.433,	44.883,	26.1371,	
# new facet 1/2
	VERTEX,	49.167,	45.973,	26.2,	
# new facet 1/2
	VERTEX,	47.433,	44.883,	26.1371,	
# new facet 1/2
	VERTEX,	46.7768,	46.2338,	27.1811,	
# new facet 2/2
	VERTEX,	49.167,	45.973,	26.2,	
# new facet 2/2
	VERTEX,	47.433,	44.883,	26.1371,	
# new facet 2/2
	VERTEX,	46.7768,	46.2338,	27.1811,	
# new facet 1/2
	VERTEX,	48.981,	46.3877,	26.0021,	
# new facet 1/2
	VERTEX,	49.167,	45.973,	26.2,	
# new facet 1/2
	VERTEX,	46.7768,	46.2338,	27.1811,	
# new facet 2/2
	VERTEX,	48.981,	46.3877,	26.0021,	
# new facet 2/2
	VERTEX,	49.167,	45.973,	26.2,	
# new facet 2/2
	VERTEX,	46.7768,	46.2338,	27.1811,	
# new facet 1/2
	VERTEX,	48.981,	46.3877,	26.0021,	
# new facet 1/2
	VERTEX,	47.433,	44.883,	26.1371,	
# new facet 1/2
	VERTEX,	49.167,	45.973,	26.2,	
# new facet 2/2
	VERTEX,	48.981,	46.3877,	26.0021,	
# new facet 2/2
	VERTEX,	47.433,	44.883,	26.1371,	
# new facet 2/2
	VERTEX,	49.167,	45.973,	26.2,	
# new facet 1/2
	VERTEX,	48.981,	46.3877,	26.0021,	
# new facet 1/2
	VERTEX,	46.7768,	46.2338,	27.1811,	
# new facet 1/2
	VERTEX,	47.433,	44.883,	26.1371,	
# new facet 2/2
	VERTEX,	48.981,	46.3877,	26.0021,	
# new facet 2/2
	VERTEX,	46.7768,	46.2338,	27.1811,	
# new facet 2/2
	VERTEX,	47.433,	44.883,	26.1371,	
# new facet 1/2
	VERTEX,	49.167,	45.973,	26.2,	
# new facet 1/2
	VERTEX,	46.7768,	46.2338,	27.1811,	
# new facet 1/2
	VERTEX,	48.981,	46.3877,	26.0021,	
# new facet 2/2
	VERTEX,	49.167,	45.973,	26.2,	
# new facet 2/2
	VERTEX,	46.7768,	46.2338,	27.1811,	
# new facet 2/2
	VERTEX,	48.981,	46.3877,	26.0021,	
# new facet 1/2
	VERTEX,	47.3414,	47.9362,	27.7065,	
# new facet 1/2
	VERTEX,	49.167,	45.973,	26.2,	
# new facet 1/2
	VERTEX,	48.981,	46.3877,	26.0021,	
# new facet 2/2
	VERTEX,	47.3414,	47.9362,	27.7065,	
# new facet 2/2
	VERTEX,	49.167,	45.973,	26.2,	
# new facet 2/2
	VERTEX,	48.981,	46.3877,	26.0021,	
# new facet 1/2
	VERTEX,	47.3414,	47.9362,	27.7065,	
# new facet 1/2
	VERTEX,	46.7768,	46.2338,	27.1811,	
# new facet 1/2
	VERTEX,	49.167,	45.973,	26.2,	
# new facet 2/2
	VERTEX,	47.3414,	47.9362,	27.7065,	
# new facet 2/2
	VERTEX,	46.7768,	46.2338,	27.1811,	
# new facet 2/2
	VERTEX,	49.167,	45.973,	26.2,	
# new facet 1/2
	VERTEX,	47.3414,	47.9362,	27.7065,	
# new facet 1/2
	VERTEX,	48.981,	46.3877,	26.0021,	
# new facet 1/2
	VERTEX,	46.7768,	46.2338,	27.1811,	
# new facet 2/2
	VERTEX,	47.3414,	47.9362,	27.7065,	
# new facet 2/2
	VERTEX,	48.981,	46.3877,	26.0021,	
# new facet 2/2
	VERTEX,	46.7768,	46.2338,	27.1811,	
# new polyhedron
# new facet 1/2
	VERTEX,	45.919,	43.192,	26.334,	
# new facet 1/2
	VERTEX,	47.5305,	42.2727,	25.5592,	
# new facet 1/2
	VERTEX,	47.9833,	38.846,	28.1357,	
# new facet 2/2
	VERTEX,	45.919,	43.192,	26.334,	
# new facet 2/2
	VERTEX,	47.5305,	42.2727,	25.5592,	
# new facet 2/2
	VERTEX,	47.9833,	38.846,	28.1357,	
# new facet 1/2
	VERTEX,	45.3514,	42.538,	26.1915,	
# new facet 1/2
	VERTEX,	45.919,	43.192,	26.334,	
# new facet 1/2
	VERTEX,	47.9833,	38.846,	28.1357,	
# new facet 2/2
	VERTEX,	45.3514,	42.538,	26.1915,	
# new facet 2/2
	VERTEX,	45.919,	43.192,	26.334,	
# new facet 2/2
	VERTEX,	47.9833,	38.846,	28.1357,	
# new facet 1/2
	VERTEX,	45.3514,	42.538,	26.1915,	
# new facet 1/2
	VERTEX,	47.5305,	42.2727,	25.5592,	
# new facet 1/2
	VERTEX,	45.919,	43.192,	26.334,	
# new facet 2/2
	VERTEX,	45.3514,	42.538,	26.1915,	
# new facet 2/2
	VERTEX,	47.5305,	42.2727,	25.5592,	
# new facet 2/2
	VERTEX,	45.919,	43.192,	26.334,	
# new facet 1/2
	VERTEX,	45.3514,	42.538,	26.1915,	
# new facet 1/2
	VERTEX,	47.9833,	38.846,	28.1357,	
# new facet 1/2
	VERTEX,	47.5305,	42.2727,	25.5592,	
# new facet 2/2
	VERTEX,	45.3514,	42.538,	26.1915,	
# new facet 2/2
	VERTEX,	47.9833,	38.846,	28.1357,	
# new facet 2/2
	VERTEX,	47.5305,	42.2727,	25.5592,	
# new polyhedron
# new facet 1/2
	VERTEX,	45.919,	43.192,	26.334,	
# new facet 1/2
	VERTEX,	48.8277,	42.4067,	26.5356,	
# new facet 1/2
	VERTEX,	47.5305,	42.2727,	25.5592,	
# new facet 2/2
	VERTEX,	45.919,	43.192,	26.334,	
# new facet 2/2
	VERTEX,	48.8277,	42.4067,	26.5356,	
# new facet 2/2
	VERTEX,	47.5305,	42.2727,	25.5592,	
# new facet 1/2
	VERTEX,	47.9833,	38.846,	28.1357,	
# new facet 1/2
	VERTEX,	45.919,	43.192,	26.334,	
# new facet 1/2
	VERTEX,	47.5305,	42.2727,	25.5592,	
# new facet 2/2
	VERTEX,	47.9833,	38.846,	28.1357,	
# new facet 2/2
	VERTEX,	45.919,	43.192,	26.334,	
# new facet 2/2
	VERTEX,	47.5305,	42.2727,	25.5592,	
# new facet 1/2
	VERTEX,	47.9833,	38.846,	28.1357,	
# new facet 1/2
	VERTEX,	48.8277,	42.4067,	26.5356,	
# new facet 1/2
	VERTEX,	45.919,	43.192,	26.334,	
# new facet 2/2
	VERTEX,	47.9833,	38.846,	28.1357,	
# new facet 2/2
	VERTEX,	48.8277,	42.4067,	26.5356,	
# new facet 2/2
	VERTEX,	45.919,	43.192,	26.334,	
# new facet 1/2
	VERTEX,	47.9833,	38.846,	28.1357,	
# new facet 1/2
	VERTEX,	47.5305,	42.2727,	25.5592,	
# new facet 1/2
	VERTEX,	48.8277,	42.4067,	26.5356,	
# new facet 2/2
	VERTEX,	47.9833,	38.846,	28.1357,	
# new facet 2/2
	VERTEX,	47.5305,	42.2727,	25.5592,	
# new facet 2/2
	VERTEX,	48.8277,	42.4067,	26.5356,	
	]
cmd.load_cgo(tes_null__border_1, 'tes_null__border_1',   1)
