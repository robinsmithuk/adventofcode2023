using System.IO;
using System.Linq;

string[] readFile(string fileName)
{
    string[] content = File.ReadAllLines(fileName);
    return content;
}

List<Game> parseLines(string[] lines)
{
    List<Game> lineList = new List<Game>();

    foreach (var line in lines)
    {
        var game = new Game();

        string s = line.Substring(41).Replace("  ", " ").Trim();

        game.CardNumber = int.Parse(line.Substring(6, 2).Trim());
        game.WinningNumbers = line.Substring(9, 30).Replace("  ", " ").Trim().Split(" ").Select(int.Parse).ToList();
        game.LineNumbers = line.Substring(41).Replace("  ", " ").Trim().Split(" ").Select(int.Parse).ToList();
        game.MatchedNumbers = game.WinningNumbers.Intersect(game.LineNumbers).ToList();
        game.Score = calculateScore(game);

        lineList.Add(game);
    }

    return lineList;
}

int calculateScore(Game? game)
{
    int score = 0;

    if (game != null) 
    {
        if (game.MatchedNumbers.Count == 1)
            score = 1;
        else if (game.MatchedNumbers.Count > 1)
            score = (int)(Math.Pow(2, (game.MatchedNumbers.Count - 1)));
    }

    return score;
}

int getTotalScore(List<Game> gamesList)
{
    return gamesList.Sum(game => game.Score);
}

var lines = readFile("day5-input.txt");
var gamesList = parseLines(lines);
var total = getTotalScore(gamesList);

Console.WriteLine($"Total Score: {total}");
Console.ReadLine();

class Game
{
    public int CardNumber { get; set; }
    public List<int>? WinningNumbers { get; set; }
    public List<int>? LineNumbers { get; set; }
    public List<int>? MatchedNumbers { get; set; }
    public int Score { get; set; }
}

