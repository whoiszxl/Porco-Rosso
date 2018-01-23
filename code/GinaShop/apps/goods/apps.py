from django.apps import AppConfig


class GoodsConfig(AppConfig):
    name = 'goods'
    # 配置xadmin后台的主菜单栏文字
    verbose_name = "商品管理"
