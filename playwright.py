
from playwright.sync_api import sync_playwright
import pandas as pd

def scrape_quotes():

        browser = p.chromium.launch(headless=False)   = browser.new_page()
        page.goto("http://quotes.toscrape.com/")

        quotes_data = []


        while True:

            quotes = page.query_selector_all(".quote")

            for quote in quotes:

                text = quote.query_selector(".text").inner_text()
                author = quote.query_selector(".author").inner_text()
                tags = [tag.inner_text() for tag in quote.query_selector_all(".tag")]


                quotes_data.append({
                    "Text": text,
                    "Author": author,
                    "Tags": ", ".join(tags)
                })


            next_button = page.query_selector(".next > a")
            if next_button:
                next_button.click()
                page.wait_for_load_state("load")
            else:
                break


        df = pd.DataFrame(quotes_data)
        df.to_csv("quotes.csv", index=False)

        browser.close()
        print("Dados coletados e salvos em 'quotes.csv'.")

if __name__ == "__main__":
    scrape_quotes()
