import sender_stand_request
import data


# Получение трека заказа
def get_track():
    response = sender_stand_request.post_new_order(data.order_body)
    track = response.json()["track"]
    return track

# Влад Гончаров, 11-я когорта — Финальный проект. Инженер по тестированию плюс

# Проверка, что при запросе информации о заказе по треку, возвращается статус 200
def test_positive_assert():
    track_id = get_track()
    order_info = sender_stand_request.get_get_order_info(track_id)
    assert order_info.status_code == 200
