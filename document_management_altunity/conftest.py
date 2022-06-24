import time
import winreg

import pytest
from altunityrunner import *


@pytest.fixture
def altdriver():
    driver = AltUnityDriver()
    # driver.load_scene("MainScene")
    yield driver
    time.sleep(5)
    driver.stop()
    # driver.unload_scene("MainScene")
    brio_registry_clean_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\Unity\UnityEditor\BRIO MRS", 0,
                                             winreg.KEY_SET_VALUE)
    print(brio_registry_clean_key)
    winreg.DeleteKey(brio_registry_clean_key, 'BRIO MRS')
