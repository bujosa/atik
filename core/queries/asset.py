from gql import gql

getAssetsQuery = gql(
    """
    query{
        getAssets{
            slug
            id
            name
            symbol
      }
    }
  """
)
