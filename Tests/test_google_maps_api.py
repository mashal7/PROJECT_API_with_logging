from utils.API import GoogleMapsApi
from utils.checking import Checking

class TestCreatePlace:
    '''Изменение и удаление новой локации'''

    def test_create_new_place(self):
        print('Метод POST')
        #result_post: Response = GoogleMapsApi.create_new_place()
        result_post = GoogleMapsApi.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get('place_id')
        Checking.check_status_code(result_post, 200)
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_value(result_post, 'status', 'OK')

        print('метод GET_POST')
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'address', '29, side layout, cohen 09')

        print('метод PUT')
        result_put = GoogleMapsApi.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ['msg'])
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')

        print('метод GET_PUT')
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get,['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])

        print('метод DELETE')
        result_del = GoogleMapsApi.delete_new_place(place_id)
        Checking.check_status_code(result_del, 200)
        Checking.check_json_token(result_del, ['status'])

        print('метод GET_DELETE')
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_token(result_get,['msg'])
        Checking.check_json_search_word_in_value(result_get,'msg', 'failed')

        print('Тестирование "Создание и изменение новой локации" прошло успешно')
