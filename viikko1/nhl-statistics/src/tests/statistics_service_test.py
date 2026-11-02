import unittest
from statistics_service import StatisticsService, SortBy
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),     #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54),    # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53),    # 37+53 = 90
            Player("Yzerman", "DET", 42, 56),    # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)     # 35+89 = 124
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_returns_player_when_name_matches(self):
        player = self.stats.search("Kurri")

        self.assertEqual(player.name, "Kurri")
        self.assertEqual(player.team, "EDM")
        self.assertEqual(player.goals, 37)
        self.assertEqual(player.assists, 53)

    def test_search_returns_none_when_player_is_not_found(self):
        player = self.stats.search("Selanne")

        self.assertIsNone(player)

    def test_team_returns_players_from_given_team(self):
        players = self.stats.team("EDM")

        names = [player.name for player in players]

        self.assertEqual(names, ["Semenko", "Kurri", "Gretzky"])

    def test_team_returns_empty_list_when_team_has_no_players(self):
        players = self.stats.team("BOS")

        self.assertEqual(players, [])

    def test_top_returns_players_ordered_by_points_by_default(self):
        players = self.stats.top(2)

        names = [player.name for player in players]

        self.assertEqual(names, ["Gretzky", "Lemieux", "Yzerman"])

    def test_top_returns_players_ordered_by_points_when_sortby_is_points(self):
        players = self.stats.top(2, SortBy.POINTS)

        names = [player.name for player in players]

        self.assertEqual(names, ["Gretzky", "Lemieux", "Yzerman"])

    def test_top_returns_players_ordered_by_goals_when_sortby_is_goals(self):
        players = self.stats.top(2, SortBy.GOALS)

        names = [player.name for player in players]

        self.assertEqual(names, ["Lemieux", "Yzerman", "Kurri"])

    def test_top_returns_players_ordered_by_assists_when_sortby_is_assists(self):
        players = self.stats.top(2, SortBy.ASSISTS)

        names = [player.name for player in players]

        self.assertEqual(names, ["Gretzky", "Yzerman", "Lemieux"])

    def test_top_zero_returns_best_player(self):
        players = self.stats.top(0)

        names = [player.name for player in players]

        self.assertEqual(names, ["Gretzky"])


if __name__ == "__main__":
    unittest.main()
