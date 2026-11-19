from playwright.sync_api import Page, expect
def test_contact_form_submits(page: Page):
    name = "John Jingle"
    email = "johnjingle@example.com"
    phone = "12345678901"
    subject = "Booking question"
    message = "I would like to book a room for 2 nights."

    page.goto("https://automationintesting.online")

    page.get_by_test_id("ContactName").fill(name)
    page.get_by_test_id("ContactEmail").fill(email)
    page.get_by_test_id("ContactPhone").fill(phone)
    page.get_by_test_id("ContactSubject").fill(subject)
    page.get_by_test_id("ContactDescription").fill(message)

    page.get_by_role("button", name="Submit").click()

    expect(page.get_by_text(f"Thanks for getting in touch {name}")).to_be_visible()