from app.db.base_table_interface import BaseInterface
from app.db.models.user.model import UserModel


class UserInterFace(BaseInterface):
    model = UserModel