
# map names based on https://www.powerpyx.com/black-myth-wukong-all-shrines-fast-travel-points/
map_code_to_names = {'hei_feng_shan': 'Black Wind Mountain',  # 第一回-黑风山
                     'huang_feng_zhai': 'Yellow Wind Sage',  # 第二回-黄风岭
                     '03_xueshanjing': 'The New West - Snowhill Path',  # 小西天-雪山径
                     '03_fututa': 'The New West - Pagoda Realm - Inside Pagoda',  # 小西天-浮屠塔
                     '03_futujie': 'The New West - Pagoda Realm - Outside Pagoda',  # 小西天-浮图界
                     '03_kuhai': 'The New West - Bitter Lake',  # 小西天-苦海
                     '03_jilegu': 'The New West - Valley of Ecstasy',  # 小西天-极乐谷
                     '03_xiaoleiyinsi': 'The New West - New Thunderclap Temple'}  # 小西天-小雷音
map_codes = list(map_code_to_names.keys())
z_level_code_to_names = {10: '1x', 11: '2x', 12: '4x',
                         13: '8x'}  # 8x is the highest resolution

start_map_id = 48


def map_id_to_code(map_id):
    return map_codes[map_id-start_map_id]


map_id_to_landmark_catalog_ids = {
    48: [
        3266,
        3267,
        3268,
        3269,
        3270,
        3271,
        3273,
        3274,
        3275,
        3276,
        3280,
        3281,
        3282,
        3278,
        3279,
        3277,
        3306,
        3283,
        3284
    ],
    49: [3286, 3287, 3288, 3289, 3290, 3291, 3293, 3294, 3295, 3296, 3298, 3305, 3304, 3299, 3300, 3301, 3307, 3302, 3303],
    50: [
        3308,
        3309,
        3310,
        3311,
        3312,
        3313,
        3314,
        3315,
        3316,
        3317,
        3321,
        3322,
        3323,
        3319,
        3320,
        0,  # no medicinal ingredient catalog for this map somehow...?
        3326,
        3324,
        3325
    ],
    51: [
        3327,
        3328,
        3329,
        3330,
        3331,
        3332,
        3333,
        3334,
        3335,
        3336,
        3340,
        3341,
        3342,
        3338,
        3339,
        0,
        3345,
        3343,
        3344
    ],
    52: [
        3346,
        3347,
        3348,
        3349,
        3350,
        3351,
        3352,
        3353,
        3354,
        3355,
        3359,
        3360,
        3361,
        3357,
        3358,
        0,
        3364,
        3362,
        3363
    ],
    53: [
        3365,
        3366,
        3367,
        3368,
        3369,
        3370,
        3371,
        3372,
        3373,
        3374,
        3378,
        3379,
        3380,
        3376,
        3377,
        0,
        3383,
        3381,
        3382
    ],
    54: [
        3384,
        3385,
        3386,
        3387,
        3388,
        3389,
        3390,
        3391,
        3392,
        3393,
        3396,
        3397,
        3398,
        3394,
        3395,
        0,
        3401,
        3399,
        3400
    ],
    55: [
        3402,
        3403,
        3404,
        3405,
        3406,
        3407,
        3408,
        3409,
        3410,
        3411,
        3414,
        3415,
        3416,
        3412,
        3413,
        0,
        3419,
        3417,
        3418
    ]
}


def catalog_id_to_uniform_id(map_id, catalog_id):
    return map_id_to_landmark_catalog_ids[map_id].index(catalog_id)


map_landmark_catalog_names = [
    'Shrine',  # 土地庙
    'Meditation Spot',  # 打坐蒲团
    'Chest',  # 宝箱
    'Pill',  # 仙丹
    'Vessel/Drink/Soak',  # 酒食
    'Formula',  # 丹方
    'Key Item',  # 要紧事物
    'Curio',  # 珍玩
    'Vessel',  # 法宝
    'Spirit',  # 精魄
    'Characters',  # 人物
    'Yaoguai Chief',  # 头目
    'Yaoguai King',  # 妖王
    'Luojia Fragrant Vine',  # 落伽香藤
    'Awaken Wine Worm',  # 三冬虫
    'Medicinal Ingredient',  # 药材
    'Rare Ingredient',  # 稀罕材料
    'Tips and Tricks',  # 留言提醒
    'Secret Location',  # 隐藏地点
]

map_anchors = {
    'hei_feng_shan': {
        'web': [[-0.13587041838590608, 0.26905836640487735], # 见谛
               [-1.253772285911566, 0.5692847538414867]], #碧藕
        'local': [[7403, 6626],
                  [891, 4878]], # at 8x resolution
    },
    'huang_feng_zhai': {
        'web': [[-1.2040625754265477, 1.062259280971574], # 铁中血
               [-0.29189122847145654, 0.5509396676100806]], # 玲珑内丹
        'local': [[1176, 1993],
                 [6494, 4994]],
    },
    '03_xueshanjing': {
        'web': [[-1.1221909879623126, 0.16076290430738993], # 起始地点
               [-0.46047132702861404, 0.7692143135299574]],  # 亢金龙
        'local': [[1654, 7259],
                 [5506, 3719]],
    },
    '03_fututa': {
        'web': [[-1.1715378595996526, 0.34360900946099093], # 魔将-莲眼
               [-0.31222953005399745, 0.8100871926730235]], # 耗子
        'local': [[684*2, 3095*2],
                 [3186*2, 1735*2]],
    },
    '03_futujie': {
        'web': [[-1.1168555475601636, 0.2822094179851291], # 经筒外土地庙
               [-0.33812067550087477, 0.9701764200557506]], # 苦海南岸
        'local': [[1685, 6553],
                 [6221, 2543]],
    },
    '03_kuhai': {
        'web': [[-1.0569062390813713, 0.23444529086823707], # 亢金星君
               [-0.5934632198811016, 0.7285464860428306]], # 极乐谷快活林 - 土地庙
        'local': [[2037, 6830],
                 [6729, 652]],
    },
    '03_jilegu': {
        'web': [[-0.20438169525559147, 0.18576154927470157], # 极乐谷瓜田 - 土地庙
                [-0.7763339673036853, 0.8788296625803724]], # 九转仙丹
        'local': [[7002, 7108],
                 [3670, 3072]],
    },
    '03_xiaoleiyinsi': {
        'web': [[-1.090609931083577, 0.82769852311786], # 九转仙丹
               [-0.271213270294993, 0.556794015266334]], # 海上僧
        'local': [[919*2, 1683*2],
                 [3307*2, 2476*2]],
    }
}

def landmark_id_to_catalog_name(map_id, landmark_id):
    return map_landmark_catalog_names[map_id_to_landmark_catalog_ids[map_id].index(landmark_id)]

def convert_to_snake_case(input_string):
    lowercase_string = input_string.lower()
    snake_case_string = lowercase_string.replace(" ", "_")
    
    return snake_case_string