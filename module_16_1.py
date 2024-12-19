from fastapi import FastAPI
app = FastAPI()


@app.get('/user/admin')
async def admin_panel():
    return 'Вы вошли как администратор'


@app.get('/user/{user_id}')
async def id_u(user_id: int = 10):
    return f'Вы вошли как пользователь № {user_id}'


@app.get('/user')
async def user_info(username: str = 'Ivan', age: int = 24):
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'


@app.get('/')
async def welcome() -> str:
    return 'Главная страница'
