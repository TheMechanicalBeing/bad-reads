from flask import redirect, url_for
from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user


class SecureModelView(ModelView):
    edit_modal = True
    create_modal = True

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for("initial"))


class SecureIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccesible_callback(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for("initial"))
