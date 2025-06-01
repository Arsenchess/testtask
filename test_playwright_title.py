import pytest
from playwright.sync_api import Page, expect

def test_page_title(page: Page):
    page.goto("https://playwright.dev/")
    expected_title = "Fast and reliable end-to-end testing for modern web apps | Playwright"
    expect(page).to_have_title(expected_title)

    # pytest.\test_playwright_title.py --browser chromium,firefox