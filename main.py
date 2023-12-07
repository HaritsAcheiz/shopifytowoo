import pandas as pd
from dataclasses import dataclass

@dataclass
class ShopifytoWoo():

    def main(self):
        df = pd.read_csv('products_export_1 (1) - products_export_1.csv')
        print(df.head())

if __name__ == '__main__':
    converter = ShopifytoWoo()
    converter.main()
