from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    # 配置xadmin后台的主菜单栏文字
    verbose_name = "用户管理"
