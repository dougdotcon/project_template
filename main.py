"""
Main module of the Disney reviews analyzer.
Manages the main program loop and coordinates operations between modules.
"""
from pathlib import Path
from typing import List, Callable
from process import (
    load_reviews,
    Review,
    get_reviews_by_park,
    count_reviews_by_park_and_location,
    avg_rating_by_park_year,
    reviews_count_per_park,
    avg_rating_per_park,
    top_locations_for_park,
    avg_monthly_rating,
    avg_rating_per_park_location,
    park_summary,
)
import tui
import visual
from exporter import TxtExporter, CsvExporter, JsonExporter

EXPORTERS = {"TXT": TxtExporter, "CSV": CsvExporter, "JSON": JsonExporter}

def handle_view(reviews: List[Review]) -> None:
    """Manages the data viewing submenu.

    Args:
        reviews: List of loaded reviews
    """
    while True:
        try:
            option = tui.view_menu()
            if option == "1":
                park = tui.ask("Park")
                if not park:
                    tui.show_msg("Park cannot be empty.")
                    continue
                data = get_reviews_by_park(reviews, park)
                tui.show_reviews(data)
            elif option == "2":
                park = tui.ask("Park")
                loc = tui.ask("Reviewer location")
                if not park or not loc:
                    tui.show_msg("Park and location cannot be empty.")
                    continue
                total = count_reviews_by_park_and_location(reviews, park, loc)
                tui.show_msg(f"Total: {total} review(s)")
            elif option == "3":
                park = tui.ask("Park")
                year = tui.ask("Year (YYYY)")
                if not park or not year:
                    tui.show_msg("Park and year cannot be empty.")
                    continue
                if not year.isdigit() or len(year) != 4:
                    tui.show_msg("Year must be in YYYY format.")
                    continue
                avg = avg_rating_by_park_year(reviews, park, year)
                tui.show_msg(f"Average for {park} in {year}: {avg:.2f}" if avg else "No data.")
            elif option == "4":
                stats = avg_rating_per_park_location(reviews)
                tui.show_table(stats)
            elif option.upper() == "X":
                break
            else:
                tui.invalid_choice()
        except (ValueError, ZeroDivisionError) as e:
            tui.show_msg(f"Error processing data: {e}")

def handle_graph(reviews: List[Review]) -> None:
    """Manages the graph generation submenu.

    Args:
        reviews: List of loaded reviews
    """
    while True:
        try:
            option = tui.graph_menu()
            if option == "1":
                cnts = reviews_count_per_park(reviews)
                visual.pie_reviews_per_park(cnts)
            elif option == "2":
                avgs = avg_rating_per_park(reviews)
                visual.bar_avg_rating_per_park(avgs)
            elif option == "3":
                park = tui.ask("Park")
                if not park:
                    tui.show_msg("Park cannot be empty.")
                    continue
                data = top_locations_for_park(reviews, park)
                visual.bar_top_locations(data, park)
            elif option == "4":
                park = tui.ask("Park")
                if not park:
                    tui.show_msg("Park cannot be empty.")
                    continue
                data = avg_monthly_rating(reviews, park)
                visual.bar_monthly_rating(data, park)
            elif option.upper() == "X":
                break
            else:
                tui.invalid_choice()
        except Exception as e:
            tui.show_msg(f"Error generating graph: {e}")

def handle_export(reviews: List[Review]) -> None:
    """Manages the data export functionality.

    Args:
        reviews: List of loaded reviews
    """
    try:
        fmt = tui.export_menu()
        if not fmt:
            tui.show_msg("Format cannot be empty.")
            return
            
        cls = EXPORTERS.get(fmt.upper())
        if not cls:
            tui.invalid_choice()
            return
            
        path = Path(f"summary.{fmt.lower()}")
        summary = park_summary(reviews)
        cls().export(summary, path)
        tui.show_msg(f"File saved at {path.absolute()}")
    except Exception as e:
        tui.show_msg(f"Error exporting: {e}")

def main() -> None:
    """Main function that manages the program loop."""
    tui.banner()
    try:
        csv_path = Path(__file__).parent / "data" / "disneyland_reviews.csv"
        reviews = load_reviews(csv_path)
        tui.show_msg(f"Dataset loaded with {len(reviews):,} lines.\n")

        while True:
            try:
                choice = tui.main_menu()
                if choice.upper() == "A":
                    handle_view(reviews)
                elif choice.upper() == "B":
                    handle_graph(reviews)
                elif choice.upper() == "C":
                    handle_export(reviews)
                elif choice.upper() == "X":
                    tui.show_msg("Exiting...")
                    break
                else:
                    tui.invalid_choice()
            except KeyboardInterrupt:
                tui.show_msg("\nOperation cancelled by user.")
                continue
    except KeyboardInterrupt:
        tui.show_msg("\nProgram terminated by user.")
    except Exception as e:
        tui.show_msg(f"Fatal error: {e}")

if __name__ == "__main__":
    main()
