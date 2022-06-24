import pytest
from guibot.config import GlobalConfig
from guibot.finder import TextFinder
from guibot.guibot import GuiBot
from guibot.region import Region
from guibot.target import Text


@pytest.mark.test
class TestAuthentication:
    def test_first_authentication_through_local_document_management(self):
        GlobalConfig.smooth_mouse_drag = False
        guibot = GuiBot()
        guibot.add_path('images')
        finder = TextFinder()
        finder.params["ocr"]["backend"] = "tesserocr"
        finder.params["ocr"]["language"] = "rus"

        region = Region(cv=TextFinder())
        image = Region()

        region.type_at("local", Text("Login"))
        region.type_at("123", Text("Password"))
        region.type_at("1", Text("Set PIN"))
        region.type_at("1", Text("Confirm PIN"))
        region.click(Text("Sign In"))
        image.wait('empty_widget')
        assert image.sample('empty_widget') > 0.95, 'Not possible to add new widget, probably not authorized'
