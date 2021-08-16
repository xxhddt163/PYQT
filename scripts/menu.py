from os.path import join


def menu_to_file(path, choose):
    """
    将选择的程序转换成文件
    :param choose: 选择的软件
    :param path: 文件保存路径
    :return: None
    """
    with open(join(path, "menu.txt"), "w") as menu_file:
        if 'sys_cra' in choose:
            choose.remove('sys_cra')
        menu_file.write("、".join(choose))


def menu_format(choice_list):
    """将中文选单格式为菜单简写名"""

    menu_dir = {"微信": "Wechat",
                "Net Framework3": "NF3",
                "360驱动大师": "360drv",
                "谷歌浏览器": "Chrome",
                "腾讯视频": "TXvideo",
                "爱奇艺(推荐)": "IQIYI",
                "DirectX9": "DX",
                "网易云音乐": "163music",
                "搜狗输入法": "SougouPY",
                "QQ音乐": "QQmusic",
                "钉钉": "Dtalk",
                "酷狗音乐(推荐)": "Kugou",
                "2345浏览器(推荐)": "2345explorer",
                "2345拼音输入法(推荐)": "2345pinyin",
                "WPS(推荐)": "WPS",
                "系统优化": "sys_cra",
                "天正建筑T20": "T20",
                "PhotoShop CS3": "PSCS3",
                "PhotoShop CC2018": "PSCC2018",
                "Office 2013 Professional": "OFFICE2013",
                "Premiere CC2018": "PRCC2018",
                "迅雷11": "Xunlei",
                "NotePad++": "npplus",
                "百度网盘": "baidu_Netdisk",
                "班智达输入法": "bzdsrf"
                }

    menu_temp = choice_list.copy()
    for item in menu_temp:
        if item in menu_dir:
            menu_temp[menu_temp.index(item)] = menu_dir[item]
    return menu_temp

