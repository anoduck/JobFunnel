"""Fer Loading of Buster Captcha Solver in Selenium
"""
import logging
from selenium import webdriver
from webdriver.webdriver.firefox.options import Options
from jobfunnel.backend.tools import Logger
from jobfunnel.backend.tools import get_webdriver

# -------------------------------------------------
#    ___      _                ____    __
#   / _ \____(_)  _____ ____  / __/__ / /___ _____
#  / // / __/ / |/ / -_) __/ _\ \/ -_) __/ // / _ \
# /____/_/ /_/|___/\__/_/   /___/\__/\__/\_,_/ .__/
#                                           /_/
# -------------------------------------------------

class CaptchaBuster(Logger):
    """Class used to add captcha buster plugin to session of webdriver
    """

    def __init__(self, driver, log_level: int = logging.INFO,
                 log_file: str = None) -> None:
        """Init

        TODO: Figure out what the hell needs to be in this init.

        Args:
            buster_loc: location of buster extension

        """
        super().__init__(
            level=log_level,
            file_path=logfile,
        )
        


def driver_setup(driver):
    profile = webdriver.FirefoxProfile()
    profile.add_extension("buster_captcha_solver.xpi")
    opts = Options()
    opts.add_argument(
        '--user-agent=Mozilla/5.0 CK={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'  # noqa: E501
    )
    opts.add_argument("--headless")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--lang=en-US")
    # opts.add_argument("--host-rules='MAP gunbroker.com 127.0.0.1:5000'")
    # opts.add_argument("--dns-prefetch-disable")
    opts.set_capability("javascript.enabled", True)
    # opts.set_preference("security.fileuri.strict_origin_policy", False)
    # driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
    return driver
