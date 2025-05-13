"""
Module responsible for data export in different formats.
Implements abstract and concrete classes for TXT, CSV, and JSON export.
"""
from abc import ABC, abstractmethod
from pathlib import Path
import csv
import json
from typing import Dict, Union, Any

class Exporter(ABC):
    """Base abstract class for data exporters."""
    
    @abstractmethod
    def export(self, summary: Dict[str, Dict[str, Union[int, float, int]]], path: Path) -> None:
        """Exports data summary to a file.

        Args:
            summary: Dictionary with summarized data by park
            path: Path where the file will be saved
        """
        pass

class TxtExporter(Exporter):
    """Exporter for plain text format (.txt)."""
    
    def export(self, summary: Dict[str, Dict[str, Union[int, float, int]]], path: Path) -> None:
        """Exports data in text format, one park per line with indentation.

        Args:
            summary: Dictionary with summarized data by park
            path: Path where the .txt file will be saved
        """
        with open(path, "w", encoding="utf-8") as fp:
            for park, data in summary.items():
                fp.write(f"{park}\n")
                for k, v in data.items():
                    fp.write(f"  {k}: {v}\n")
                fp.write("\n")

class CsvExporter(Exporter):
    """Exporter for CSV format."""
    
    def export(self, summary: Dict[str, Dict[str, Union[int, float, int]]], path: Path) -> None:
        """Exports data in CSV format with header.

        Args:
            summary: Dictionary with summarized data by park
            path: Path where the .csv file will be saved
        """
        header = ["Park", "reviews", "positive", "avg", "countries"]
        with open(path, "w", newline="", encoding="utf-8") as fp:
            writer = csv.writer(fp)
            writer.writerow(header)
            for park, data in summary.items():
                writer.writerow([park] + list(data.values()))

class JsonExporter(Exporter):
    """Exporter for JSON format."""
    
    def export(self, summary: Dict[str, Dict[str, Union[int, float, int]]], path: Path) -> None:
        """Exports data in indented JSON format.

        Args:
            summary: Dictionary with summarized data by park
            path: Path where the .json file will be saved
        """
        with open(path, "w", encoding="utf-8") as fp:
            json.dump(summary, fp, indent=2, ensure_ascii=False)