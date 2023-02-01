import random


class Outcome:
    """
    Each number has a variety of Outcome i.e. ("Red" 1:1)
    Test: test = Outcome("test",5), then test.winAmount(5) = 25
    Chapter 5, pages 37-43
    """
    def __init__(self, name: str, odds: int):
        self.name = str(name)
        self.odds = int(odds)


    def winAmount(self, amount:float) -> float:
        return self.odds * amount


    def __eq__(self, other) -> bool:
        return self.name == other.name


    def __ne__(self, other) -> bool:
        return self.name != other.name


    def __hash__(self) -> int:
        return hash(self.name)


    def __str__(self):
        return "{name:s} ({odds:d}:1)".format_map(vars(self))


    def __repr__(self):
        return "{class_:s}({name!r}, {odds!r})".format(
            class_=type(self).__name__, **vars(self))


class Bin(frozenset):
    """
    Each bin will have 12-14 Outcomes
    Frozenset means a unique values, fixed once created
    Extended (inheirts all methods from frozenset e.g. .add())
    Chapter 6, pageas 45-48
    """
    pass



class Wheel:
    """
    Contains 38 bins
    Responsible for Random Number Generation (RNG)
    Chapter 7, pages 49-52
    """
    def __init__(self):
        self.bins = list(Bin() for _ in range(38))
        self.rng = random.Random()
        self.rng.seed(4)


    def addOutcome(self, number: int, outcome):
        self.bins[number] = Bin(self.bins[number] | Bin[outcome])


    def next(self):
        return self.rng.randint(0, 37) #TODO


    def get(self, bin):
        return self.bins[bin]


class BinBuilder:
  """
  Creates all of the winning Outcomes and adds them to each bin on the wheel
  Each bin has 12-14 different ways that it can be a winner e.g. 1 can be straight, street, corner...
  Chapter 8, pages 53-58
  """

  def buildBins(self, wheel):
    pass

  def straightBets(self):
    """
    Bet on a single number paying at 35:1
    38 bets / 38 outcomes
    """
    outcomes = []
    for n in range(0, 37):
      bin = Outcome(str(n), 35)
      a = (n, bin.__repr__())
      outcomes.append(a)

    #bin = Outcome("0", 35)
    #y = (0, bin.__repr__())
    #outcomes.append(y)
    bin = Outcome("00", 35)
    x = (37, bin.__repr__())
    outcomes.append(x)
    return outcomes

  def splitBets(self):
    """
    Adjacent pair of numbers (column or row) paying at 17:1
    114 bets / 114 outcomes
    """
    outcomes = []
    return outcomes

  def streetBets(self):
    """
    3 numbers in a single row paying at 11:1
    12 possible bets / 36 outcomes
    """
    outcomes = []
    return outcomes

  def lineBets(self):
    """
    A 6 number block (2 street bets) paying at 5:1
    11 possible bets
    """
    outcomes = []
    return outcomes

  def dozenBets(self):
    """
    Each number is member of one of three dozens paying at 2:1
    3 possible bets
    """
    outcomes = []
    return outcomes

  def cornerBets(self):
    """
    A square of 4 numbers paying at 8:1
    22 possible bets / 88 outcomes
    """
    outcomes = []
    return outcomes

  def outsideBets(self):
    """
    All other bets e.g. Red/Black, Low/High, Even/Odd
    """
    outcomes = []
    return outcomes

bb = BinBuilder()
print(bb.straightBets())
print(len(bb.straightBets()))
