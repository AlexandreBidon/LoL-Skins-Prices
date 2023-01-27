from regular_price import *
import click

@click.command()
@click.option('--sitemap_url')
def run(sitemap_url : str):
    liste_url = get_skins_url_per_champion(sitemap_skin_url = sitemap_url)
    final_dict = get_skins_prices_all(liste_url_per_champion = liste_url)
    export_dict_to_json("export/regular_prices.json", final_dict)

if __name__ == '__main__':
    run()