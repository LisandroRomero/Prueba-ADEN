import xmlrpc.client
from config import settings


class OdooClient:

    def __init__(self):
        self.url = settings.ODOO_URL
        self.db = settings.ODOO_DB
        self.username = settings.ODOO_USERNAME
        self.password = settings.ODOO_PASSWORD
        

        self.common = xmlrpc.client.ServerProxy(f"{self.url}/xmlrpc/2/common")

        self.uid = self.common.authenticate(
            self.db,
            self.username,
            self.password,
            {}
        )

        self.models = xmlrpc.client.ServerProxy(f"{self.url}/xmlrpc/2/object")

    def execute(self, model, method, args=None, kwargs=None):
        args = args or []
        kwargs = kwargs or {}
        return self.models.execute_kw(
            self.db,
            self.uid,
            self.password,
            model,
            method,
            args,
            kwargs
        )