import asyncio
import time
import json
from colorama import init, Fore
from urllib.parse import urljoin
from playwright.async_api import async_playwright

init(autoreset=True)

async def scrape_page(page, url):
    await page.goto(url)
    post_elements = await page.query_selector_all('.quote')
    link_author = []
    data_for_author = []
    data_for_quote = []

    for post_element in post_elements:
        link_element = await post_element.query_selector('a')
        link_href = await link_element.get_attribute('href')
        link_author.append(link_href)

        author_element = await post_element.query_selector(".author")
        author = await author_element.text_content()

        quote_element = await post_element.query_selector(".text")
        quote = await quote_element.text_content()

        tags = []
        tag_elements = await post_element.query_selector_all(".tag")
        for tag_element in tag_elements:
            tag = await tag_element.text_content()
            tags.append(tag)

        quote_data = {
            'author': author,
            'quote': quote,
            'tags': tags
        }

        data_for_quote.append(quote_data)

    # Using set to avoid redundant requests
    unique_links = set(link_author)
    for link in unique_links:
        full_url = urljoin(url, link)
        await page.goto(full_url)

        author_name_element = await page.query_selector('.author-title')
        author_name = await author_name_element.text_content()

        born_date_element = await page.query_selector('.author-born-date')
        born_date = await born_date_element.text_content()

        born_location_element = await page.query_selector('.author-born-location')
        born_location = await born_location_element.text_content()

        description_element = await page.query_selector('.author-description')
        description = await description_element.text_content()

        author_data = {
            'fullname': author_name,
            'born_date': born_date,
            'born_location': born_location,
            'description': description
        }

        data_for_author.append(author_data)

    return data_for_author, data_for_quote

async def scrapping_data():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        base_url = 'http://quotes.toscrape.com'
        next_selector = '.next > a'
        data_for_author = []
        data_for_quote = []

        while True:
            author_results, quote_results = await scrape_page(page, base_url)
            data_for_author.extend(author_results)
            data_for_quote.extend(quote_results)

            next_button = await page.query_selector(next_selector)
            if next_button:
                next_url = await next_button.get_attribute('href')
                next_url = urljoin(base_url, next_url)
                base_url = next_url
            else:
                break

        # Ensure 'json' directory exists
        import os
        os.makedirs('json', exist_ok=True)

        with open('json/authors.json', 'w', encoding='utf-8') as json_file:
            json.dump(data_for_author, json_file, ensure_ascii=False, indent=4)
        with open('json/quotes.json', 'w', encoding='utf-8') as json_file:
            json.dump(data_for_quote, json_file, ensure_ascii=False, indent=4)

        await browser.close()

if __name__ == '__main__':
    start_time = time.time()
    print(Fore.BLUE + "Start scrapping")
    asyncio.run(scrapping_data())
    print(Fore.GREEN + "Finished scrapping")
    end_time = time.time()
    execution_time = end_time - start_time
    print("Scraping done for" + Fore.RED + f" {execution_time:.2f} sec")
