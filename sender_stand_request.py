import configuration
import data
import requests
# Создание нового заказа
def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,  # подставялем полный url
                         json=data.order_body)  # тело
# Получение трек номера в формате string
def get_track_no():
    return str(post_new_order().json()["track"]) # получаем трек заказа в формате string

# Поиск заказа по трек номеру
def get_order(track_no):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH + "?t=" + track_no)
    # подставялем url, содержащий номер трека
