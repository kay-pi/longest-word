from longest_word.game import Game
import string

class TestGame:
    def test_game_initialization(self):
            # setup
            new_game = Game()

            # exercise
            grid = new_game.grid

            # verify
            assert type(grid) == list
            assert len(grid) == 9
            for letter in grid:
                assert letter in string.ascii_uppercase

    def test_number_is_invalid(self):
        new_game = Game()
        
        assert new_game.is_valid(837495893) is False
        
    def test_numbers_mixed_is_invalid(self):
        new_game = Game()
        
        assert new_game.is_valid('h5h6h6i65') is False
    
    def test_empty_word_is_invalid(self):
        # setup
        new_game = Game()
        # verify
        assert new_game.is_valid('') is False