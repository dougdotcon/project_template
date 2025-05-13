"""
Unit tests for the process.py module.
"""
from pathlib import Path
import pytest
from process import (
    Review,
    load_reviews,
    avg_rating_by_park_year,
    reviews_count_per_park,
    avg_rating_per_park,
    park_summary
)

# Test data
SAMPLE_REVIEWS = [
    Review(id=1, rating=5, year_month="2019-01", location="Brazil", park="Disneyland Paris"),
    Review(id=2, rating=4, year_month="2019-01", location="USA", park="Disneyland Paris"),
    Review(id=3, rating=3, year_month="2019-02", location="France", park="Disneyland Paris"),
    Review(id=4, rating=5, year_month="2020-01", location="Brazil", park="Disney World Orlando"),
    Review(id=5, rating=4, year_month="2020-01", location="USA", park="Disney World Orlando"),
]

def test_load_reviews():
    """Tests if load_reviews function loads the correct number of lines."""
    csv_path = Path(__file__).parent.parent / "data" / "disneyland_reviews.csv"
    reviews = load_reviews(csv_path)
    assert len(reviews) > 0, "Dataset should contain reviews"
    assert all(isinstance(r, Review) for r in reviews), "All entries should be Reviews"

def test_avg_rating_by_park_year():
    """Tests annual average calculation with known dataset."""
    # Average for Disneyland Paris in 2019: (5 + 4 + 3) / 3 = 4.0
    avg = avg_rating_by_park_year(SAMPLE_REVIEWS, "Disneyland Paris", "2019")
    assert avg == 4.0

    # Average for Disney World in 2020: (5 + 4) / 2 = 4.5
    avg = avg_rating_by_park_year(SAMPLE_REVIEWS, "Disney World Orlando", "2020")
    assert avg == 4.5

    # Year with no data should return None
    avg = avg_rating_by_park_year(SAMPLE_REVIEWS, "Disneyland Paris", "2020")
    assert avg is None

def test_reviews_count_per_park():
    """Tests review count by park."""
    counts = reviews_count_per_park(SAMPLE_REVIEWS)
    assert counts["Disneyland Paris"] == 3
    assert counts["Disney World Orlando"] == 2

def test_avg_rating_per_park():
    """Tests average rating calculation by park."""
    avgs = avg_rating_per_park(SAMPLE_REVIEWS)
    # Disneyland Paris: (5 + 4 + 3) / 3 = 4.0
    assert avgs["Disneyland Paris"] == 4.0
    # Disney World: (5 + 4) / 2 = 4.5
    assert avgs["Disney World Orlando"] == 4.5

def test_park_summary():
    """Tests park summary generation."""
    summary = park_summary(SAMPLE_REVIEWS)
    
    paris = summary["Disneyland Paris"]
    assert paris["reviews"] == 3
    assert paris["positive"] == 2  # ratings >= 4
    assert paris["avg"] == 4.0
    assert paris["countries"] == 3  # Brazil, USA, France
    
    orlando = summary["Disney World Orlando"]
    assert orlando["reviews"] == 2
    assert orlando["positive"] == 2  # ratings >= 4
    assert orlando["avg"] == 4.5
    assert orlando["countries"] == 2  # Brazil, USA