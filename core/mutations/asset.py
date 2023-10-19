from gql import gql

createAssetMutation = gql(
    """
    mutation CreateAsset($input: CreateAssetInput!){
        createAsset(input: $input){
            id
        }
    }
  """
)
