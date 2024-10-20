import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.utils import split_equal, split_exact, split_percentage

def test_split_equal():
    amount = 3000
    participants = [1, 2, 3]
    split = split_equal(amount, participants)
    assert split == {1: 1000, 2: 1000, 3: 1000}

def test_split_exact():
    amounts = {1: 1000, 2: 1500, 3: 500}
    split = split_exact(amounts)
    assert split == {1: 1000, 2: 1500, 3: 500}

def test_split_percentage():
    amount = 4000
    percentages = {1: 50, 2: 30, 3: 20}
    split = split_percentage(amount, percentages)
    assert split == {1: 2000, 2: 1200, 3: 800}
