# src/utils.py

import os
import sys
from PySide6.QtCore import QSize, QByteArray, Qt, QFile, QIODevice
from PySide6.QtGui import QColor, QPixmap

def get_resource_path(relative_path):
    """
    Get path to resource.
    Always returns a Qt resource path (:/...) since all assets are compiled
    into resources_rc.py and available via the Qt resource system in both
    dev and packaged environments.
    """
    return f":/{relative_path.replace(os.path.sep, '/')}"

def create_colored_pixmap(icon_path: str, color: QColor, size: QSize) -> QPixmap:
    """
    Loads an SVG icon from a file path or a Qt resource path,
    replaces its 'currentColor' with a specified QColor,
    and returns it as a scaled QPixmap.
    """
    try:
        qfile = QFile(icon_path)
        if not qfile.open(QIODevice.OpenModeFlag.ReadOnly | QIODevice.OpenModeFlag.Text):
            raise IOError(f"Cannot open resource file: {icon_path}")

        svg_data = qfile.readAll().data().decode('utf-8')
        qfile.close()
        
        colored_svg_data = svg_data.replace('currentColor', color.name())
        byte_array = QByteArray(colored_svg_data.encode('utf-8'))
        
        pixmap = QPixmap()
        pixmap.loadFromData(byte_array)
        
        return pixmap.scaled(size, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
    except Exception as e:
        print(f"Error creating colored pixmap for {icon_path}: {e}")
        return QPixmap()
def format_seconds_to_hms(seconds: int) -> str:
    """Formats a duration in seconds to a HH:MM:SS string."""
    if not isinstance(seconds, (int, float)) or seconds < 0:
        return "--:--"
    
    h, rem = divmod(int(seconds), 3600)
    m, s = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"

def get_app_data_path():
    """Returns the path to the application's data directory."""
    # This function is moved here to prevent circular imports.
    from src.config.app_config import APP_DATA_DIR
    base_path = os.getenv('LOCALAPPDATA')
    if not base_path:
        base_path = os.path.expanduser("~")
    return os.path.join(base_path, APP_DATA_DIR)

def get_image_path(relative_path):
    """
    Get absolute path to a downloaded image asset.
    Images are always stored in the AppData directory (downloaded by asset_downloader).
    """
    base_path = get_app_data_path()

    # Normalize separators
    normalized_path = relative_path.replace('/', os.path.sep).replace('\\', os.path.sep)

    # Strip leading 'data' folder if present (e.g. 'data/Bosses_locations/...' -> 'Bosses_locations/...')
    parts = normalized_path.split(os.path.sep)
    if parts and parts[0].lower() == 'data':
        normalized_path = os.path.join(*parts[1:]) if len(parts) > 1 else ''

    return os.path.join(base_path, normalized_path)