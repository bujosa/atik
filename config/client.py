"""Module containing the logic for creating a graphql client."""
from gql.transport.requests import RequestsHTTPTransport
from gql import Client


def create_gql_client(url: str, jwt=None):
    """Create a GraphQL client."""
    if jwt is None:
        headers = None
    else:
        headers = {"Authorization": f"Bearer {jwt}"}

    transport = RequestsHTTPTransport(url=url, use_json=True, headers=headers)

    client = Client(transport=transport, fetch_schema_from_transport=False)

    return client
