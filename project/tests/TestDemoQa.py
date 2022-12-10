import pytest
from framework.browser.Singleton import Singleton
from framework.driver.Alerts import Alerts
from framework.driver.Handles import Handles
from framework.driver.IFrameUtils import IFrameUtils
from framework.driver.JsUtils import JsUtils
from project.pages.submenu.AlertsPage import AlertsForm
from project.pages.submenu.BrowserWindowsPage import BrowserWindowsForm
from project.pages.submenu.DatePickerPage import DatePickerForm
from project.pages.panel.ElementsPage import ElementsForm
from project.pages.HomePage import HomeForm
from project.pages.submenu.LinksPage import LinksForm
from project.pages.submenu.NestedPage import NestedForm
from project.pages.submenu.UpDownLoadPage import UpDownLoadForm
from project.pages.submenu.WebTablesPage import WebTablesForm
from project.pages.panel.WidgetsPage import WidgetsForm
from project.pages.frames.FrameChildPage import FrameChildForm
from project.pages.frames.FrameSmallPage import FrameSmallForm
from project.pages.tabs.SamplePage import SampleForm
from project.pages.frames.FrameBigPage import FrameBigForm
from project.pages.frames.FrameParentPage import FrameParentForm
from project.pages.submenu.FramesPage import FramesForm
from project.utils.SysUtils import SysUtils
from project.utils.TimeUtils import TimeUtils
from project.utils.GetUtils import GetUtils
from project.utils.Utils import Utils


@pytest.mark.usefixtures('open_page')
class TestDemoQa:

    def test_alerts(self):
        home = HomeForm()
        alerts = AlertsForm()
        assert home.is_page_opened(), "Home page is not opened"
        JsUtils().scroll_to_the_bottom(GetUtils().get_script('scroll_script'))
        home.click_alerts_menu()
        JsUtils().scroll_to_the_bottom(GetUtils().get_script('scroll_script'))
        alerts.click_button_alerts_menu()
        alerts.click_button_alert()
        assert Alerts.alert_text() == GetUtils().get_checks('alert_text'), "Alert is not opened"
        Alerts.accept_alert()
        assert Alerts.alert_is_not_present(), "Alert did not close"
        alerts.click_button_confirm_box()
        assert Alerts.alert_text() == GetUtils().get_checks('confirm_text'), "Confirm box is not opened"
        Alerts.accept_alert()
        assert Alerts.alert_is_not_present(), "Confirm box did not close"
        assert alerts.text_in_confirm_box() == GetUtils().get_checks('confirm_field'), "Text is not sent"
        JsUtils().scroll_to_the_bottom(GetUtils().get_script('scroll_script'))
        alerts.click_button_prompt()
        assert Alerts.alert_text() == GetUtils().get_checks('prompt_text'), "Prompt is not opened"
        random_text = Utils().generate_text()
        Alerts.send_data(random_text)
        Alerts.accept_alert()
        assert Alerts.alert_is_not_present(), "Prompt did not close"
        assert alerts.text_in_prompt() == random_text, "The text does not correspond"

    def test_iframes(self):
        home = HomeForm()
        alerts = AlertsForm()
        nested = NestedForm()
        frames = FramesForm()
        iframe_parent = FrameParentForm()
        iframe_child = FrameChildForm()
        frame_big = FrameBigForm()
        frame_small = FrameSmallForm()
        assert home.is_page_opened(), "Home page is not opened"
        JsUtils().scroll_to_the_bottom(GetUtils().get_script('scroll_script'))
        home.click_alerts_menu()
        assert alerts.is_page_opened(), "Alerts page is not opened"
        alerts.remove_footer()
        alerts.remove_iframe()
        JsUtils().scroll_to_the_bottom(GetUtils().get_script('scroll_script'))
        alerts.click_button_nested_frames()
        assert nested.is_page_opened(), "Nested frames page is not opened"
        JsUtils().scroll_to_the_bottom(GetUtils().get_script('scroll_script'))
        nested.switch_to_iframe()
        assert iframe_parent.get_iframe_parent_text() == GetUtils().get_checks('parent_text'), "Expected text is missing"
        iframe_parent.switch_to_iframe()
        assert iframe_child.get_iframe_child_text() == GetUtils().get_checks('child_text'), "Expected text is missing"
        IFrameUtils().switch_to_default_iframe()
        nested.click_button_frames()
        assert frames.is_page_opened(), "Frames page is not opened"
        JsUtils().scroll_to_the_bottom(GetUtils().get_script('scroll_script'))
        frames.switch_to_big_iframe()
        big_frame_text = frame_big.get_big_text()
        IFrameUtils().switch_to_default_iframe()
        frames.switch_to_small_iframe()
        small_frame_text = frame_small.get_small_text()
        assert big_frame_text == small_frame_text, "The texts differ"

    @pytest.mark.parametrize('user_number', ('1', '2'))
    def test_user_form(self, user_number):
        home = HomeForm()
        tables = WebTablesForm()
        elements = ElementsForm()
        assert home.is_page_opened(), "Home page is not opened"
        JsUtils().scroll_to_the_bottom(GetUtils().get_script('scroll_script'))
        home.click_elements_menu()
        assert elements.is_page_opened(), "Elements page is not opened"
        JsUtils().scroll_to_the_bottom(GetUtils().get_script('scroll_script'))
        elements.click_web_tables_menu()
        assert tables.is_page_opened(), "Tables page is not opened"
        tables.click_button_add()
        tables.send_data_to_registration_form(GetUtils().get_user_data(user_number))
        user_data_dict = GetUtils().get_user_data(user_number)
        tables.click_submit_button()
        table_content = tables.get_table_text()
        assert Utils().user_data_in_table(user_data_dict, table_content), "User's data was not entered"
        rows_before_delete = tables.count_rows_in_table()
        JsUtils().scroll_to_the_bottom(GetUtils().get_script('scroll_script'))
        tables.click_button_delete_record()
        table_content = tables.get_table_text()
        rows_after_delete = tables.count_rows_in_table()
        assert rows_before_delete > rows_after_delete, "The number of rows did not change"
        assert Utils().user_data_in_table(user_data_dict, table_content) is False, "The data was not deleted"

    def test_handles(self):
        home = HomeForm()
        alerts = AlertsForm()
        windows = BrowserWindowsForm()
        sample = SampleForm()
        links = LinksForm()
        assert home.is_page_opened(), "Home page is not opened"
        JsUtils().scroll_to_the_bottom(GetUtils().get_script('scroll_script'))
        home.click_alerts_menu()
        assert alerts.is_page_opened(), "Alerts page is not opened"
        JsUtils().scroll_to_the_bottom(GetUtils().get_script('scroll_script'))
        alerts.click_button_browser_windows()
        assert windows.is_page_opened(), "Windows page is not opened"
        original = Handles.handle_current_window()
        windows.click_button_new_tab()
        Handles.switch_to_new_window()
        assert sample.is_page_opened(), "Sample page is not opened"
        current_url = Singleton().get_current_url()
        assert GetUtils().get_checks('sample') in current_url, "Tab /sample is not opened"
        Handles().close_tab()
        Handles.switch_to_original(original)
        assert windows.is_page_opened(), "Windows page is not opened"
        JsUtils().scroll_to_the_bottom(GetUtils().get_script('scroll_script'))
        windows.click_button_elements_menu()
        JsUtils().scroll_to_the_bottom(GetUtils().get_script('scroll_script'))
        windows.click_button_links_submenu()
        Handles.switch_to_new_window()
        original = Handles.handle_current_window()
        assert links.is_page_opened(), "The page is not opened"
        links.click_button_home()
        Handles.switch_to_new_window()
        assert home.is_page_opened(), "The page is not opened"
        Handles.switch_to_original(original)
        assert links.is_page_opened(), "The page is not opened"

    def test_date_picker(self):
        home = HomeForm()
        widgets = WidgetsForm()
        date_picker = DatePickerForm()
        assert home.is_page_opened(), "Home page is not opened"
        JsUtils().scroll_to_the_bottom(GetUtils().get_script('scroll_script'))
        home.click_widgets_menu()
        assert widgets.is_page_opened(), "Widgets page is not opened"
        JsUtils().scroll_to_the_bottom(GetUtils().get_script('scroll_script'))
        widgets.click_button_date_picker()
        assert date_picker.is_page_opened(), "Date picker page is not opened"
        date_picker.click_on_field_select_date()
        date_in_field = date_picker.get_data_from_field_select_date()
        assert date_in_field == TimeUtils.get_current_date(), "The date in the field does not match the current date"
        date_and_time_from_field = date_picker.get_data_from_field_date_and_time()
        assert date_and_time_from_field == TimeUtils.get_current_date_and_time(), "The date and time in the field" \
                                                                              " does not match the current date"
        date_picker.click_on_field_select_date()
        date_picker.select_nearest_month_and_year()
        date_picker.select_29_february()
        selected_date_in_field = date_picker.get_data_from_field_select_date()
        assert selected_date_in_field == TimeUtils.get_desired_date(), "The value in the field does not match the set value"

    @pytest.mark.usefixtures('clear_folder')
    def test_file_download_upload(self):
        home = HomeForm()
        elements = ElementsForm()
        ul_dl = UpDownLoadForm()
        assert home.is_page_opened(), "Home page is not opened"
        JsUtils().scroll_to_the_bottom(GetUtils().get_script('scroll_script'))
        home.click_elements_menu()
        assert elements.is_page_opened(), "Elements page is not opened"
        JsUtils().scroll_to_the_bottom(GetUtils().get_script('scroll_script'))
        elements.click_button_upload_and_download()
        ul_dl.is_page_opened()
        files_before_dl = SysUtils().get_files_number()
        ul_dl.click_button_download()
        SysUtils().is_download_started(files_before_dl)
        assert SysUtils().is_file_downloaded() is True, "File is not downloaded"
        ul_dl.upload_file_to_webpage()
        file_name = SysUtils().get_downloaded_file_name()
        file_path = ul_dl.get_uploaded_file_path()
        assert file_name in file_path, "The file path does not contain the file name"
