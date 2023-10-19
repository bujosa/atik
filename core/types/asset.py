import math
import pandas as pd
from settings import env
from settings.client import create_gql_client
from core.queries.asset import getAssetsQuery
from core.mutations.asset import createAssetMutation
from functions.generate_slug import generate_slug
from collections import namedtuple

class Asset:
    def __init__(self):
        self.client = create_gql_client(env.URL, env.JWT)

    def add(self):
        """Create a asset in api."""

        assets = self.fromApi()
        assetsFromCsv = self.get()

        for asset in assetsFromCsv:
                try:
                    if asset.symbol in assets:
                        print("Asset already exists")
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
            assets[asset['symbol']] = asset

        return assets


    def get(self):
        """Get assets from csv."""
        df = pd.read_csv("./data/clean_data.csv", low_memory=False, encoding='latin-1')
        asset = namedtuple('asset', df.columns)
        assets = []
        for row in df.itertuples(index=False):
            assets.append(asset(*row))

        return assets
