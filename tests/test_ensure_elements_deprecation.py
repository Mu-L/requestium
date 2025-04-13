import pytest
import requestium


def test_deprecation_warning_for_ensure_element_locators_with_underscores() -> None:
    with requestium.Session() as session:
        session.driver.get("http://the-internet.herokuapp.com")
        with pytest.warns(DeprecationWarning):
            session.driver.ensure_element("class_name", "no-js")
