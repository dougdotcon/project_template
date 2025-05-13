"""
Module responsible for graph generation using matplotlib.
Contains functions for visualizing different aspects of Disney reviews.
"""
from typing import Dict
import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt

def _fmt_title(title: str) -> None:
    """Formats the graph title with standard size and layout.

    Args:
        title: Graph title text
    """
    plt.title(title, fontsize=12)
    plt.tight_layout()

def pie_reviews_per_park(counts: Dict[str, int]) -> None:
    """Generates pie chart with reviews distribution by park.

    Args:
        counts: Dictionary with review count by park
    """
    plt.figure(figsize=(10, 6))
    plt.pie(counts.values(), labels=counts.keys(), autopct="%d")
    _fmt_title("Number of Reviews by Park")
    plt.show()

def bar_avg_rating_per_park(avgs: Dict[str, float]) -> None:
    """Generates bar chart with average ratings by park.

    Args:
        avgs: Dictionary with average rating by park
    """
    plt.figure(figsize=(10, 6))
    plt.bar(avgs.keys(), avgs.values())
    _fmt_title("Average Rating by Park")
    plt.ylabel("Average Rating")
    plt.show()

def bar_top_locations(data: Dict[str, float], park: str) -> None:
    """Generates bar chart with top locations by average rating.

    Args:
        data: Dictionary with averages by location
        park: Park name for the title
    """
    plt.figure(figsize=(12, 6))
    plt.bar(data.keys(), data.values())
    _fmt_title(f"Top 10 Locations by Average Rating – {park}")
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Average Rating")
    plt.show()

def bar_monthly_rating(data: Dict[str, float], park: str) -> None:
    """Generates bar chart with monthly rating averages.

    Args:
        data: Dictionary with averages by month
        park: Park name for the title
    """
    plt.figure(figsize=(10, 6))
    plt.bar(data.keys(), data.values())
    _fmt_title(f"Monthly Rating Average – {park}")
    plt.ylabel("Average Rating")
    plt.show()

matplotlib.rcParams['font.size'] = 10
matplotlib.rcParams['figure.autolayout'] = True
