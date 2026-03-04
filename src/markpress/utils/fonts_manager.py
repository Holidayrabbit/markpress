# import os
# import platform
# import urllib.request
# from pathlib import Path
# from reportlab.pdfbase import pdfmetrics
# from reportlab.pdfbase.ttfonts import TTFont
#
# from markpress.utils.utils import get_font_path
#
# # 缓存锚点与静态资产目录
# GLOBAL_FONT_CACHE = Path.home() / ".markpress" / "fonts"
#
# # 云端资产路由表
# CLOUD_FONTS = {
#     "WenYuanSansSC.ttf": "https://cdn.jsdelivr.net/gh/HUSTerCH/markpress-assets@main/fonts/WenYuanSansSC.ttf",
#     "WenYuanSansSC-Bold.ttf": "https://cdn.jsdelivr.net/gh/HUSTerCH/markpress-assets@main/fonts/WenYuanSansSC-Bold.ttf",
#     "WenYuanSansSC-Italic.ttf": "https://cdn.jsdelivr.net/gh/HUSTerCH/markpress-assets@main/fonts/WenYuanSansSC-Italic.ttf",
#     "WenYuanSansSC-Bold-Italic.ttf": "https://cdn.jsdelivr.net/gh/HUSTerCH/markpress-assets@main/fonts/WenYuanSansSC-Bold-Italic.ttf",
#
#     "WenYuanSerifSC.ttf": "https://cdn.jsdelivr.net/gh/HUSTerCH/markpress-assets@main/fonts/WenYuanSerifSC.ttf",
#     "WenYuanSerifSC-Bold.ttf": "https://cdn.jsdelivr.net/gh/HUSTerCH/markpress-assets@main/fonts/WenYuanSerifSC-Bold.ttf",
#     "WenYuanSerifSC-Italic.ttf": "https://cdn.jsdelivr.net/gh/HUSTerCH/markpress-assets@main/fonts/WenYuanSerifSC-Italic.ttf",
#     "WenYuanSerifSC-Bold-Italic.ttf": "https://cdn.jsdelivr.net/gh/HUSTerCH/markpress-assets@main/fonts/WenYuanSerifSC-Bold-Italic.ttf",
# }
#
#
# def resolve_and_register_font(logical_name: str, font_filename: str, font_type: str = "sans"):
#     """
#     核动力字体挂载管线：静态直读 -> 云端拉取 -> 宿主寄生
#     """
#     # [第一防线]：静态捆绑资产 (Harmony, JetBrains)
#     try:
#         with get_font_path(font_filename) as font_path:
#             if Path(font_path).exists():
#                 pdfmetrics.registerFont(TTFont(logical_name, str(font_path)))
#                 return
#     except Exception as e:
#         pass
#
#     # 云端动态资产
#     if font_filename in CLOUD_FONTS:
#         GLOBAL_FONT_CACHE.mkdir(parents=True, exist_ok=True)
#         cache_path = GLOBAL_FONT_CACHE / font_filename
#         if not cache_path.exists():
#             url = CLOUD_FONTS[font_filename]
#
#             try:
#                 print(f"[MarkPress] 首次渲染，正在从云端拉取重型字体资产: {font_filename} ...")
#                 # 工业级工具应使用带超时的 request，这里做极简演示
#                 urllib.request.urlretrieve(url, str(cache_path))
#                 print(f"[MarkPress] 资产 {font_filename} 挂载完成。")
#             except Exception as e:
#                 if cache_path.exists():
#                     cache_path.unlink()  # 销毁残缺文件
#                 print(f"[Warn] 云端拉取失败 ({e})，准备降级。")
#
#         if cache_path.exists():
#             pdfmetrics.registerFont(TTFont(logical_name, str(cache_path)))
#             return
#
#     # [第三防线]：使用HarmonyOS静态资源字体和JetBrainsMono
#
#     raise RuntimeError(f"渲染引擎崩溃：无法解析字体 {font_filename}，且兜底失效。")
import os
import urllib.request
from pathlib import Path
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from markpress.utils.utils import get_font_path

# 缓存锚点
GLOBAL_FONT_CACHE = Path.home() / ".markpress" / "fonts"

# 云端资产路由表
CLOUD_FONTS = {
    "WenYuanSansSC.ttf": "https://cdn.jsdelivr.net/gh/HUSTerCH/markpress-assets@main/fonts/WenYuanSansSC.ttf",
    "WenYuanSansSC-Bold.ttf": "https://cdn.jsdelivr.net/gh/HUSTerCH/markpress-assets@main/fonts/WenYuanSansSC-Bold.ttf",
    "WenYuanSansSC-Italic.ttf": "https://cdn.jsdelivr.net/gh/HUSTerCH/markpress-assets@main/fonts/WenYuanSansSC-Italic.ttf",
    "WenYuanSansSC-Bold-Italic.ttf": "https://cdn.jsdelivr.net/gh/HUSTerCH/markpress-assets@main/fonts/WenYuanSansSC-Bold-Italic.ttf",

    "WenYuanSerifSC.ttf": "https://cdn.jsdelivr.net/gh/HUSTerCH/markpress-assets@main/fonts/WenYuanSerifSC.ttf",
    "WenYuanSerifSC-Bold.ttf": "https://cdn.jsdelivr.net/gh/HUSTerCH/markpress-assets@main/fonts/WenYuanSerifSC-Bold.ttf",
    "WenYuanSerifSC-Italic.ttf": "https://cdn.jsdelivr.net/gh/HUSTerCH/markpress-assets@main/fonts/WenYuanSerifSC-Italic.ttf",
    "WenYuanSerifSC-Bold-Italic.ttf": "https://cdn.jsdelivr.net/gh/HUSTerCH/markpress-assets@main/fonts/WenYuanSerifSC-Bold-Italic.ttf",
}

# 家族血统图谱
FONT_FAMILIES = {
    "WenYuanSansSC": [
        "WenYuanSansSC.ttf", "WenYuanSansSC-Bold.ttf",
        "WenYuanSansSC-Italic.ttf", "WenYuanSansSC-Bold-Italic.ttf"
    ],
    "WenYuanSerifSC": [
        "WenYuanSerifSC.ttf", "WenYuanSerifSC-Bold.ttf",
        "WenYuanSerifSC-Italic.ttf", "WenYuanSerifSC-Bold-Italic.ttf"
    ]
}

# 家族污染黑名单：只要下载失败过一次，整个家族都会被打入冷宫
FAILED_FAMILIES = set()


def get_family_name(font_filename: str) -> str:
    """根据文件名溯源其所属的家族"""
    for family, members in FONT_FAMILIES.items():
        if font_filename in members:
            return family
    return None


def get_static_fallback_filename(original_filename: str, font_type: str) -> str:
    """极其精确的降级映射：保留字重与斜体属性，映射到内置静态资产"""
    suffix = ""
    name_no_ext = original_filename.replace(".ttf", "")

    # 提取样式后缀
    if name_no_ext.endswith("-Bold-Italic"):
        suffix = "-Bold-Italic"
    elif name_no_ext.endswith("-Bold"):
        suffix = "-Bold"
    elif name_no_ext.endswith("-Italic"):
        suffix = "-Italic"

    # 核心降级逻辑：代码字体回退给 JetBrains，正文/衬线字体全部回退给 Harmony
    base = "JetBrainsMono" if font_type == "mono" else "HarmonySC"
    return f"{base}{suffix}.ttf"


def execute_static_fallback(logical_name: str, original_filename: str, font_type: str):
    """终极兜底执行器"""
    fallback_filename = get_static_fallback_filename(original_filename, font_type)

    try:
        with get_font_path(fallback_filename) as font_path:
            if Path(font_path).exists():
                print(f"[MarkPress 降级] {original_filename} 已安全降级为静态资产 -> {fallback_filename}")
                pdfmetrics.registerFont(TTFont(logical_name, str(font_path)))
                return
    except Exception as e:
        raise RuntimeError(f"渲染引擎崩溃：兜底资产 {fallback_filename} 加载失败 ({e})，请检查 assets 目录。")

    raise RuntimeError(f"渲染引擎崩溃：兜底资产 {fallback_filename} 物理文件缺失！")


def resolve_and_register_font(logical_name: str, font_filename: str, font_type: str = "sans"):
    """
    核动力字体挂载管线：静态直读 -> 云端原子拉取 -> 静态强兜底
    """
    family_name = get_family_name(font_filename)

    # [第零防线]：如果该字体所在的家族已经被污染，直接降级
    if family_name and family_name in FAILED_FAMILIES:
        execute_static_fallback(logical_name, font_filename, font_type)
        return

    # [第一防线]：本地静态捆绑资产 (Harmony, JetBrains)
    # 如果它压根不在云端列表里，说明它本身就是静态兜底资产，直接尝试读取
    if font_filename not in CLOUD_FONTS:
        try:
            with get_font_path(font_filename) as font_path:
                if Path(font_path).exists():
                    pdfmetrics.registerFont(TTFont(logical_name, str(font_path)))
                    return
        except Exception:
            pass

    # [第二防线]：云端动态资产
    if font_filename in CLOUD_FONTS:
        GLOBAL_FONT_CACHE.mkdir(parents=True, exist_ok=True)

        # 提取同家族的所有成员
        family_members = FONT_FAMILIES.get(family_name, [font_filename])
        family_is_intact = True

        # 【核心逻辑：原子化拉取】只要用到家族里任意一个字，瞬间把整个家族的 4 个字重全部拉下来

        for member in family_members:
            cache_path = GLOBAL_FONT_CACHE / member
            if not cache_path.exists():
                url = CLOUD_FONTS[member]
                try:
                    print(f"[MarkPress 云端挂载] 正在拉取家族字体资产: {member} ...")
                    urllib.request.urlretrieve(url, str(cache_path))
                except Exception as e:
                    print(f"[Warn] 字体 {member} 拉取失败 ({e})！")
                    if cache_path.exists():
                        cache_path.unlink()
                    family_is_intact = False
                    break  # 家族基因破损，立即停止拉取其他成员

        # 家族完整无缺，正常注册目标字体
        if family_is_intact:
            cache_path = GLOBAL_FONT_CACHE / font_filename
            pdfmetrics.registerFont(TTFont(logical_name, str(cache_path)))
            return
        else:
            # 家族破损，将其打入黑名单，防止后续渲染时同一个家族的代码继续尝试下载
            if family_name:
                FAILED_FAMILIES.add(family_name)

    # [第三防线]：静态资源兜底
    # 走到这一步，只有两种可能：云端拉取失败，或者本地静态资源缺失
    execute_static_fallback(logical_name, font_filename, font_type)