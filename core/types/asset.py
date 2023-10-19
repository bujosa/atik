import math
import pandas as pd
from config.env import env
from config.client import create_gql_client
from core.queries import getAssetsQuery
from core.mutations import createAssetMutation
from functions.generate_slug import generate_slug

class Asset:
    def __init__(self):
        self.client = create_gql_client(env.URL, env.JWT)

    def add(self):
        """Create a asset in api."""

        assets = self.fromApi()
        assetsFromCsv = self.get()

        print(assetsFromCsv)

        for asset in assetsFromCsv:
                try:
                    if (asset == math.nan):
                        continue

                    if generate_slug(asset) in assets:
                        continue

                    params = {
                        "input": {
                            "name": asset.name,
                            "url": asset.url,
                            "symbol": asset.symbol,
                        }
                    }

                    result = self.client.execute(
                        createAssetMutation, variable_values=params)
                    
                    print(result)

                except Exception as e:
                    print("Error: " + str(e))

    def fromApi(self):
        """Get assets from the API."""

        getAssetsResult = self.client.execute(
            getAssetsQuery)['getAssets']

        assets = {}
        for asset in getAssetsResult:
            assets[asset['slug']] = asset

        return assets


    def get(self):
        """Get assets from csv."""
        df = pd.read_csv("../../data/clean_data.csv", low_memory=False, encoding='latin-1')

        return df.tolist()