from pathlib import Path

import pytest
from PIL import Image


@pytest.fixture
def image1():
    """Create image1 and automatically close after test."""
    path = Path("test") / "images" / "acolchado.jpg"
    with Image.open(path) as image:
        yield image


@pytest.fixture
def image2():
    """Create image2 and automatically close after test."""
    path = Path("test") / "images" / "sheet.jpg"
    with Image.open(path) as image:
        yield image


@pytest.fixture
def xord_image():
    """Create xord_image and automatically close after test."""
    path = Path("test") / "images" / "xord_image.jpg"
    with Image.open(path) as image:
        yield image