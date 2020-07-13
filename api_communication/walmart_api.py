import requests
from bs4 import BeautifulSoup
import unittest
from typing import List, Dict
from pprint import pprint


def searchToHTML(search_term: str) -> str:
    response = requests.get(f'https://www.walmart.com/search/?query={search_term}')
    return response.text


def getData(html: str) -> Dict:
    dict_titles = dict()
    soup = BeautifulSoup(html, 'html.parser')
    list_items = soup.find_all(**{"data-automation-id": "search-result-gridview-items"})
    for child in list_items[0].children:
        title_element = child.find_all(**{"data-type": "itemTitles"})
        price = None
        for price in child.find_all("span", class_="price-main"):
            price = price.find_all("span", class_="visuallyhidden")[0].text
        if title_element:
            # @@ what happends when there is more than one title that is the same
            dict_titles[title_element[0].text] = {'price': price}
    return dict_titles


def search(search_term: str) -> Dict:
    return getData(searchToHTML(search_term))


class TestScrape(unittest.TestCase):
    def test_number2pencil(self):
        with open('number2pencil.html', 'r', encoding='utf-8') as test_pencil:
            list_titles = getData(test_pencil)
            self.assertEqual(list_titles, {
                'Ticonderoga Soft Pencil - Yellow - Pre-Sharpened 30 Count': {'price': '$6.57'},
                'Ticonderoga Pencil, 24 Count, Unsharpened': {'price': '$11.29'},
                'ARTEZA #2 HB Wood Cased Graphite Pencils, Pack of 72, Bulk, Pre-Sharpened with Latex Free Erasers, Bulk pack, Smooth write for Exams, School, Office, Drawing and Sketching': {
                    'price': '$16.99'},
                'Dixon Ticonderoga #2 HB Soft Pencils, 0.5 mm, 18 Count': {'price': '$9.09'},
                'Pen + Gear No. 2 Wood Pencils, Yellow, 8 Count': {'price': '$0.47'},
                'Ticonderoga Pencil 96 Count': {'price': '$16.26'},
                'Write Dudes U.S.A. Gold #2 HB Premium Wood Pencils, 8 count': {'price': '$6.83'},
                'Dixon Economy - #2 Soft - Yellow 144 ct': {'price': '$14.62'},
                'Pen + Gear Yellow Pencil, 20 count': {'price': None},
                'Pen + Gear No. 2 Wood Pencils, Assorted Designs, 30 Count': {'price': '$2.97'}})


#if __name__ == "__main__":
    #main()

"""
search query: #2 pencil
url: https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=%232+pencil
first result url: https://www.amazon.com/ARTEZA-Graphite-Pencils-Pre-Sharpened-Sketching/dp/B076DGMLT6/ref=redir_mobile_desktop?ie=UTF8&aaxitk=FxmcWTdaluI.paeoymxxmw&hsa_cr_id=3754349710301&ref_=sb_s_sparkle
first result url with price: https://www.amazon.com/gp/slredirect/picassoRedirect.html/ref=pa_sp_atf_aps_sr_pg1_1?ie=UTF8&adId=A0652428YW5X83R66NLY&url=%2FAmazonBasics-Pre-sharpened-Wood-Cased-Pencils%2Fdp%2FB071JM699B%2Fref%3Dsr_1_1_sspa%3Fdchild%3D1%26keywords%3D%25232%2Bpencil%26qid%3D1590187719%26sr%3D8-1-spons%26psc%3D1&qualifier=1590187719&id=1199134334266290&widgetName=sp_atf
Interesting HTML for product: <div data-asin="B071JM699B" data-index="1" data-uuid="4fd8c37e-7f77-4824-891a-c07672470510" data-component-type="s-search-result" class="sg-col-4-of-24 sg-col-4-of-12 sg-col-4-of-36 s-result-item s-asin sg-col-4-of-28 sg-col-4-of-16 AdHolder sg-col sg-col-4-of-20 sg-col-4-of-32">
"""
# class="search-product-result"
# id="searchProductResult"
# tabindex="-1"
# soup =
# soup.find_all(class=re.compile(r"^result\d+"))
