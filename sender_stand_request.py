import configuration
import requests
import data

# Создание нового заказа
def post_new_order(body):
    return requests.post(
                            configuration.URL_SERVICE + configuration.CREATE_ORDER,
                            json=body
                         )


# Запрос на получение информации о заказе по треку
def get_get_order_info(track_id):
    return requests.get(
                            configuration.URL_SERVICE + configuration.GET_ORDER_PATH + "?t=" + str(track_id)

                        )


