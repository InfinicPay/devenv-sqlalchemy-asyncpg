from app.db_models.user import User

USERS = {
    "user_1": User(
        email="user_1_email@test.com",
        name="user_1_name",
        surname="user_1_surname",
    ),
    "user_2": User(
        email="user_2_email@test.comT",
        name="user_2_name",
        surname="user_2_surname",
    ),
    "user_3": User(
        email="user_3_email@test.com",
        name="user_3_name",
        surname="user_3_surname",
    ),
}