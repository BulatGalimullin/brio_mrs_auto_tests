import pytest

from .pages.dashboard_page import DashboardPage


class TestDocumentManagementWithAltUnity:

    @pytest.mark.alt
    def test_first_authorization(self, altdriver):
        self.dashboard_page = DashboardPage(altdriver)
        self.dashboard_page.login('local', '123', '1')
