"""
Unittests to test the functions of the Class Player

Unfortunately, a name must first be entered and then the game must be ended by entering "exit" before the tests can run. 
This problem should be solved later!
"""

import os
import json
import unittest
import Play_the_game as game

class Player_test(unittest.TestCase):
    """
    Test class for the file Play_the_game.py
    """ 
    def setUp(self):
        # Create a test_highscore.json for test purpose
        self.test_highscore_path = "test_highscore.json"
        # Create the test class from Play_the_game
        self.player = game.Player("Test_Human", path_highscore=self.test_highscore_path)
        # Make a bigger test_highscore
        self.test_highscore = {"15000": [["Heiko"], [1,0]], "500": [["Basti", "Ronny"], [1,3]], 
                          "1000":[ ["Peter", "Gabi"], [1,0]], "5000": [["Hans", "Begüm"], [1,4]],
                          "25000": [["best_human_player_win"], [1,4]]}
        

    def tearDown(self):
        # Cleaning after testing, i.e. rm test_highscore.json
        if os.path.exists(self.test_highscore_path):
            os.remove(self.test_highscore_path)

    def test_init_(self):
        self.assertEqual(self.player.name, "Test_Human")
        self.assertIsNone(self.player.difficulty)
        self.assertIsNone(self.player.ai_trained)
        self.assertEqual(self.player.path_highscore, self.test_highscore_path)
        self.assertEqual(self.player.highscore, {})

    def test_save_highscore(self):
        # Save the test_highscore
        self.player.highscore = self.test_highscore
        self.player.save_highscore()

        # Load the test_highscore
        with open(self.test_highscore_path, "r") as json_file:
            load_highscore = json.load(json_file)
        self.assertEqual(load_highscore, self.test_highscore)

    def test_get_highscore_data(self):
        # Test save and load test_highscore
        self.player.highscore = {"15000" : [["Test_Human"], [0,1]]}
        self.player.save_highscore()
        get_highscore = self.player.get_highscore_data()
        self.assertEqual(get_highscore, {"15000" : [["Test_Human"], [0,1]]})

        # Test if highscore.json is createt if not exist
        self.tearDown() # rm test_highscore first
        get_highscore = self.player.get_highscore_data()
        self.assertEqual(get_highscore, {})

    def test_get_highscore_1st_place(self):
        # If highscore == {}
        self.player.highscore = {}
        result = self.player.get_highscore_1st_place()
        self.assertEqual(result, 0)

        # If highscore
        self.player.highscore = self.test_highscore
        result = self.player.get_highscore_1st_place()
        self.assertEqual(result, 25000)


if __name__ == '__main__':
    unittest.main()


