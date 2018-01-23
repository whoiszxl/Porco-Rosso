from django.apps import AppConfig


class UserOperationConfig(AppConfig):
    name = 'user_operation'
    # 配置xadmin后台的主菜单栏文字
    verbose_name = "用户操作管理"
