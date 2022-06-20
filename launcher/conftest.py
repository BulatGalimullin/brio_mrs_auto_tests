import os
import subprocess
import sys
import time
import winreg

import pytest


def pytest_addoption(parser):
    parser.addoption('--mrs_version', action='store', default=None,
                     help='Choose version of the MRS application. MRS builds should be stored in C:/MRS_builds/<build '
                          'version>')


def get_build_path(root, element):
    for root_path, _, files in os.walk(root):
        for name in files:
            full_path = os.path.join(root_path, name)
            if element in full_path:
                return full_path


@pytest.fixture(scope="session", autouse=True)
def mrs(request):
    mrs_version = request.config.getoption('mrs_version')
    if mrs_version is None:
        sys.exit("Choose version of the MRS application. MRS builds should be stored in C:/MRS_builds/<build_version>")
    else:
        mrs_executable = get_build_path("C:/", mrs_version)
        '''
        set language to eng through Windows registry API
        '''
        brio_registry_key = winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER,r"SOFTWARE\BRIO MRS\BRIO MRS", 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(brio_registry_key, "Account.User-1.LanguageIndex_h2678697189", 0, winreg.REG_DWORD, 1) # 1 in the end means set language to eng

        mrs = subprocess.Popen(mrs_executable, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(10)
    yield
    mrs.kill()
    '''
    clear registry of MRS app
    '''
    brio_registry_clean_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\BRIO MRS", 0,
                                        winreg.KEY_SET_VALUE)
    winreg.DeleteKey(brio_registry_clean_key,'BRIO MRS')



