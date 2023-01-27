from regular_price import *
from weekly_sales import *
import click
import time

@click.command()
@click.option('--sitemap_url')
@click.option('--dotesports_url')
@click.option('--onlyweeklysale', is_flag=True)
def run(onlyweeklysale, sitemap_url : str = "https://www.mobafire.com/sitemap-skins.xml", dotesports_url : str = "https://dotesports.com/league-of-legends/news/league-of-legends-weekly-champion-and-skin-sale"):
    if onlyweeklysale == False:
        liste_url = get_skins_url_per_champion(sitemap_skin_url = sitemap_url)
        final_dict = get_skins_prices_all(liste_url_per_champion = liste_url)
        export_dict_to_json("export/regular_prices.json", final_dict)
    sales_week = get_sales(url_dote_page = dotesports_url)
    export_name = "export/weekly_sale_prices-" + time.strftime("%Y%m%d") + ".json"
    export_dict_to_json(export_name, sales_week)

if __name__ == '__main__':
    run()