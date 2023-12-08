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
                          "25000": [["Test_Human"], [0,1]]}
        

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

    def test_new_highscore_player_wins(self):
        # reset highscore to empty
        self.player.highscore = {}

        # Case 1: new highscore with player "Test_Human" and difficulty "1000"
        self.player.difficulty = 1000
        self.player.new_highscore(winner=self.player.name)
        expected_highscore = {"1000": [["Test_Human"], [0, 1]]}
        self.assertEqual(self.player.highscore, expected_highscore)

        # Case 2: no new highscore but player wins again
        self.player.new_highscore(winner=self.player.name)
        expected_highscore = {"1000": [["Test_Human"], [0, 2]]}
        self.assertEqual(self.player.highscore, expected_highscore)

        # Case 3: no new highscore but AI wins
        self.player.new_highscore(winner="AI")
        expected_highscore = {"1000": [["Test_Human"], [1, 2]]}
        self.assertEqual(self.player.highscore, expected_highscore)

    def test_new_highscore_ai_wins(self):
        # reset highscore to empty
        self.player.highscore = {}

        # Case 1: new game with player "Test_Human" and difficulty "1000" but AI wins
        self.player.difficulty = 1000
        self.player.new_highscore(winner="AI")
        expected_highscore = {"1000": [[], [1, 0]]}
        self.assertEqual(self.player.highscore, expected_highscore)

        # Case 1: no new highscore but AI wins again
        self.player.new_highscore(winner="AI")
        expected_highscore = {"1000": [[], [2, 0]]}
        self.assertEqual(self.player.highscore, expected_highscore)

        # Case 3: no new highscore but player wins
        self.player.new_highscore(winner=self.player.name)
        expected_highscore = {"1000": [["Test_Human"], [2, 1]]}
        self.assertEqual(self.player.highscore, expected_highscore)





if __name__ == '__main__':
    unittest.main()


