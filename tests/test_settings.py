from lib.settings import GameSettings


class TestGameSettings:
    def test_sets_properties(self):
        h = 123
        w = 321
        settings = GameSettings(w, h)

        assert settings.height == h
        assert settings.width == w
        assert settings.screen_size == (w, h)
