from .services import get_random, get_pong

class TestGetRandom():
    def __init__(self) -> None:
        self.test_default_range()
        self.test_custom_range()
        self.test_start_greater_than_end()
        self.test_get_pong()
        
        
    def test_default_range(self):
        result = get_random()
        assert 1 <= result <= 6, "test_default_range: ERROR"
        print("test_default_range: SUCCESS")
        

    def test_custom_range(self):
        result = get_random(10, 15)
        assert 10 <= result <= 15, "test_custom_range: ERROR"
        print("test_custom_range: SUCCESS")

    def test_start_greater_than_end(self):
        try:
            print(get_random(15, 10))
            print("test_start_greater_than_end: SUCCESS")
        except:
            print("test_start_greater_than_end: ERROR")

    def test_get_pong(self):
        result = get_pong()
        assert result == "pong" , "test_get_pong: ERROR"
        print("test_get_pong: SUCCESS")
        