import json
from pathlib import Path
from datetime import datetime
from typing import Any


def save_to_archive(data: Any, filename_prefix: str, archive_folder: str = ".archive") -> Path:
    """
    Save data to a JSON file in the archive folder with a timestamp.
    
    Args:
        data: The data object to save (must be JSON serializable)
        filename_prefix: The prefix for the filename (e.g., "eval_results")
        archive_folder: The name of the archive folder (default: ".archive")
    
    Returns:
        Path: The path to the created archive file
    """
    # Create archive directory relative to the caller's location
    archive_dir = Path.cwd() / archive_folder
    archive_dir.mkdir(exist_ok=True)
    
    # Generate timestamp and filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_file = archive_dir / f"{filename_prefix}_{timestamp}.json"
    
    # Save data to JSON file
    with open(archive_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"Results saved to: {archive_file}")
    
    return archive_file
