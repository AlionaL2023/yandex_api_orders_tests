import sender_stand_request

# Тест 1. Успешное создание заказа и получение информации о заказе по его track номеру
def test_1_create_order_get_order_success_response():
    track = sender_stand_request.get_track_no() # создаем заказ и получаем его трек номер в формате string
    assert sender_stand_request.get_order(track).status_code == 200 # ищем заказ по трек номеру, сравниваем код ответа