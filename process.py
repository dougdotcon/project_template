"""
This module handles data processing for the Disney Reviews Dataset.
Contains functions for loading, filtering, and calculating statistics about reviews.
"""
from __future__ import annotations
import csv
from dataclasses import dataclass
from collections import defaultdict, Counter, OrderedDict
from pathlib import Path
from typing import Dict, List, Optional, Set, Union

@dataclass(frozen=True)
class Review:
    """Represents a review from the Disney dataset.

    Args:
        id: Unique review ID
        rating: Given rating (1-5)
        year_month: Date in YYYY-MM format
        location: Reviewer's location
        park: Disney park name
    """
    id: int
    rating: int
    year_month: str
    location: str
    park: str

def load_reviews(csv_path: Union[str, Path]) -> list[Review]:
    """Loads reviews from CSV file.

    Args:
        csv_path: Path to the CSV file

    Returns:
        List of Review objects loaded from CSV
    """
    csv_path = Path(csv_path)
    if not csv_path.is_absolute():
        csv_path = Path(__file__).parent / csv_path

    with open(csv_path, encoding="utf-8") as fp:
        reader = csv.DictReader(fp)
        return [
            Review(
                id=int(r["Review_ID"]),
                rating=int(r["Rating"]),
                year_month=r["Year_Month"],
                location=r["Reviewer_Location"],
                park=r["Branch"],
            )
            for r in reader
        ]

# ---------- Simple Filters ---------- #
def get_reviews_by_park(reviews: List[Review], park: str) -> List[Review]:
    """Filters reviews by park.

    Args:
        reviews: List of reviews
        park: Park name

    Returns:
        Reviews only from the specified park
    """
    return [r for r in reviews if r.park.lower() == park.lower()]

def count_reviews_by_park_and_location(reviews: List[Review], park: str, loc: str) -> int:
    """Counts reviews by park and location.

    Args:
        reviews: List of reviews
        park: Park name
        loc: Location to search (partial)

    Returns:
        Number of reviews matching the criteria
    """
    return sum(
        1
        for r in reviews
        if r.park.lower() == park.lower() and loc.lower() in r.location.lower()
    )

def avg_rating_by_park_year(reviews: List[Review], park: str, year: str) -> Optional[float]:
    """Calculates average rating by park and year.

    Args:
        reviews: List of reviews
        park: Park name
        year: Year (YYYY)

    Returns:
        Average rating or None if no data
    """
    ratings = [
        r.rating
        for r in reviews
        if r.park.lower() == park.lower() and r.year_month.startswith(str(year))
    ]
    return sum(ratings) / len(ratings) if ratings else None

# ---------- Statistics for Graphs ---------- #
def reviews_count_per_park(reviews: List[Review]) -> Dict[str, int]:
    """Counts number of reviews per park.

    Args:
        reviews: List of reviews

    Returns:
        Dictionary with review count per park
    """
    c = Counter(r.park for r in reviews)
    return dict(c)

def avg_rating_per_park(reviews: List[Review]) -> Dict[str, float]:
    """Calculates average rating per park.

    Args:
        reviews: List of reviews

    Returns:
        Dictionary with average rating per park
    """
    stats = defaultdict(list)
    for r in reviews:
        stats[r.park].append(r.rating)
    return {p: sum(v) / len(v) for p, v in stats.items()}

def top_locations_for_park(reviews: List[Review], park: str, top: int = 10) -> Dict[str, float]:
    """Lists locations with best averages for a park.

    Args:
        reviews: List of reviews
        park: Park name
        top: Number of locations to return (default: 10)

    Returns:
        Dictionary with top N locations and their averages
    """
    stats = defaultdict(list)
    for r in reviews:
        if r.park.lower() == park.lower():
            stats[r.location].append(r.rating)
    avgs = {loc: sum(v) / len(v) for loc, v in stats.items()}
    return dict(sorted(avgs.items(), key=lambda x: x[1], reverse=True)[:top])

def avg_monthly_rating(reviews: List[Review], park: str) -> OrderedDict:
    """Calculates monthly average rating for a park.

    Args:
        reviews: List of reviews
        park: Park name

    Returns:
        OrderedDict with monthly averages ordered from Jan to Dec
    """
    month_map = {
        '01': 'Jan', '02': 'Feb', '03': 'Mar',
        '04': 'Apr', '05': 'May', '06': 'Jun',
        '07': 'Jul', '08': 'Aug', '09': 'Sep',
        '10': 'Oct', '11': 'Nov', '12': 'Dec'
    }
    
    stats = defaultdict(list)
    for r in reviews:
        if r.park.lower() == park.lower():
            _, month = r.year_month.split("-")
            month_name = month_map.get(month)
            if month_name:
                stats[month_name].append(r.rating)
    
    ordered = OrderedDict()
    for month_name in month_map.values():
        ordered[month_name] = (
            sum(stats[month_name]) / len(stats[month_name])
            if month_name in stats and stats[month_name]
            else 0
        )
    return ordered

# ---------- Section D ---------- #
def avg_rating_per_park_location(reviews: List[Review]) -> Dict[str, Dict[str, float]]:
    """Calculates average rating by park and location.

    Args:
        reviews: List of reviews

    Returns:
        Nested dictionary with averages by park and location
    """
    tmp: Dict[str, Dict[str, List[int]]] = defaultdict(lambda: defaultdict(list))
    for r in reviews:
        tmp[r.park][r.location].append(r.rating)
    return {
        p: {loc: sum(v) / len(v) for loc, v in inner.items()}
        for p, inner in tmp.items()
    }

# ---------- Export summary ---------- #
def park_summary(reviews: List[Review]) -> Dict[str, Dict[str, Union[int, float, Set[str]]]]:
    """Generates statistical summary by park.

    Args:
        reviews: List of reviews

    Returns:
        Dictionary with statistics per park (total reviews, positives, average, countries)
    """
    summ = defaultdict(lambda: {"reviews": 0, "positive": 0, "avg": 0.0, "countries": set()})
    for r in reviews:
        s = summ[r.park]
        s["reviews"] += 1
        s["positive"] += r.rating >= 4
        s["avg"] += r.rating
        s["countries"].add(r.location)
    
    for s in summ.values():
        s["avg"] = round(s["avg"] / s["reviews"], 2)
        s["countries"] = len(s["countries"])
    return summ
