"""
Text User Interface (TUI) module.
Contains all text input and output functions for the program.
"""
from typing import Dict, List
from process import Review

BANNER = """
╔════════════════════════════════════════╗
║   DISNEYLAND REVIEWS ANALYSER v1.0     ║
╚════════════════════════════════════════╝
"""

def banner() -> None:
    """Displays the initial program banner."""
    print(BANNER)

def ask(label: str) -> str:
    """Requests user input with a label.

    Args:
        label: Text to display before input

    Returns:
        User input text, stripped of whitespace
    """
    return input(f"{label}: ").strip()

def show_msg(msg: str) -> None:
    """Displays a message to the user.

    Args:
        msg: Message to display
    """
    print(msg)

def invalid_choice() -> None:
    """Displays invalid option message."""
    print("Invalid option.\n")

def main_menu() -> str:
    """Displays the main menu and requests choice.

    Returns:
        User's chosen option
    """
    print(
        "[A] View data\n"
        "[B] Graphs\n"
        "[C] Export summary\n"
        "[X] Exit"
    )
    return ask("Choice")

def view_menu() -> str:
    """Displays the data view menu and requests choice.

    Returns:
        User's chosen option
    """
    print(
        "\n=== DATA VIEW MENU ===\n"
        "1) List reviews by park\n"
        "2) Number of reviews by park and location\n"
        "3) Annual rating average by park\n"
        "4) Average by park and location (table)\n"
        "[X] Back"
    )
    return ask("Choice")

def graph_menu() -> str:
    """Displays the graph menu and requests choice.

    Returns:
        User's chosen option
    """
    print(
        "\n=== GRAPHS MENU ===\n"
        "1) Reviews by park (pie)\n"
        "2) Average rating by park (bar)\n"
        "3) Top 10 locations for a park (bar)\n"
        "4) Monthly average for a park (bar)\n"
        "[X] Back"
    )
    return ask("Choice")

def export_menu() -> str:
    """Displays the export menu and requests format.

    Returns:
        User's chosen format (TXT/CSV/JSON)
    """
    print("\n=== EXPORT SUMMARY === (TXT / CSV / JSON)")
    return ask("Format")

def show_reviews(reviews: List[Review]) -> None:
    """Displays formatted list of reviews.

    Args:
        reviews: List of reviews to display
    """
    for r in reviews:
        print(f"{r.id} | {r.rating}⭐ | {r.year_month} | {r.location}")
    print(f"Total: {len(reviews)} review(s)\n")

def show_table(stats: Dict[str, Dict[str, float]]) -> None:
    """Displays statistics table by park and location.

    Args:
        stats: Nested dictionary with averages by park and location
    """
    for park, locs in stats.items():
        print(f"\n### {park}")
        for loc, avg in sorted(locs.items(), key=lambda x: x[1], reverse=True):
            print(f"{loc:<30} {avg:>4.2f}")
    print()
