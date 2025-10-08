"""PlacesPlacesSearchText tool implementation."""
import json
import logging
from typing import Any
import requests
from server import mcp

logger = logging.getLogger(__name__)


@mcp.tool()
def placesplacessearchtext(
    includedType: str = None,
    languageCode: str = None,
    locationBias: dict = None,
    locationRestriction: dict = None,
    maxResultCount: int = None,
    minRating: float = None,
    openNow: bool = None,
    priceLevels: list = None,
    rankPreference: str = None,
    regionCode: str = None,
    strictTypeFiltering: bool = None,
    textQuery: str = None
) -> str:
    """
    Text query based place search.
    
    Args:
        includedType: Input parameter: The requested place type. Full list of types supported: https://developers.google.com/maps/documentation/places/web-service/place-types. Only support one included type.
        languageCode: Input parameter: Place details will be displayed with the preferred language if available. If the language code is unspecified or unrecognized, place details of any language may be returned, with a preference for English if such details exist. Current list of supported languages: https://developers.google.com/maps/faq#languagesupport.
        locationBias: Input parameter: The region to search. This location serves as a bias which means results around given location might be returned.
        locationRestriction: Input parameter: The region to search. This location serves as a restriction which means results outside given location will not be returned.
        maxResultCount: Input parameter: Maximum number of results to return. It must be between 1 and 20, inclusively. The default is 20. If the number is unset, it falls back to the upper limit. If the number is set to negative or exceeds the upper limit, an INVALID_ARGUMENT error is returned.
        minRating: Input parameter: Filter out results whose average user rating is strictly less than this limit. A valid value must be a float between 0 and 5 (inclusively) at a 0.5 cadence i.e. [0, 0.5, 1.0, ... , 5.0] inclusively. The input rating will round up to the nearest 0.5(ceiling). For instance, a rating of 0.6 will eliminate all results with a less than 1.0 rating.
        openNow: Input parameter: Used to restrict the search to places that are currently open. The default is false.
        priceLevels: Input parameter: Used to restrict the search to places that are marked as certain price levels. Users can choose any combinations of price levels. Default to select all price levels.
        rankPreference: Input parameter: How results will be ranked in the response.
        regionCode: Input parameter: The Unicode country/region code (CLDR) of the location where the request is coming from. This parameter is used to display the place details, like region-specific place name, if available. The parameter can affect results based on applicable law. For more information, see https://www.unicode.org/cldr/charts/latest/supplemental/territory_language_information.html. Note that 3-digit region codes are not currently supported.
        strictTypeFiltering: Input parameter: Used to set strict type filtering for included_type. If set to true, only results of the same type will be returned. Default to false.
        textQuery: Input parameter: Required. The text query for textual search.
        
    Returns:
        JSON string result
    """
    from config import load_api_config
    config = load_api_config()
    # Build query parameters
    query_params = {}
    # Handle multiple authentication parameters
    if config.get("bearer_token"):
        query_params["access_token"] = config["bearer_token"]
    if config.get("api_key"):
        query_params["key"] = config["api_key"]
    if config.get("bearer_token"):
        query_params["oauth_token"] = config["bearer_token"]
    # Build request body
    request_body = {}
    if includedType is not None:
        request_body["includedType"] = includedType
    if languageCode is not None:
        request_body["languageCode"] = languageCode
    if locationBias is not None:
        request_body["locationBias"] = locationBias
    if locationRestriction is not None:
        request_body["locationRestriction"] = locationRestriction
    if maxResultCount is not None:
        request_body["maxResultCount"] = maxResultCount
    if minRating is not None:
        request_body["minRating"] = minRating
    if openNow is not None:
        request_body["openNow"] = openNow
    if priceLevels is not None:
        request_body["priceLevels"] = priceLevels
    if rankPreference is not None:
        request_body["rankPreference"] = rankPreference
    if regionCode is not None:
        request_body["regionCode"] = regionCode
    if strictTypeFiltering is not None:
        request_body["strictTypeFiltering"] = strictTypeFiltering
    if textQuery is not None:
        request_body["textQuery"] = textQuery
    
    # Build URL
    url = f"{config['base_url']}/v1/places:searchText"
    
    # Build headers
    headers = {
        "Accept": "application/json",
        "X-Request-Source": "Codeglide-MCP-generator",
    }
    headers["Content-Type"] = "application/json"
    # Set authentication
    # Handle multiple authentication parameters
    
    # Add custom headers
    
    try:
        # Make API request
        response = requests.request(
            method="POST",
            url=url,
            params=query_params,
            headers=headers,
            json=request_body,
            timeout=30
        )
        
        if response.status_code >= 400:
            return json.dumps({
                "error": f"API error ({response.status_code})",
                "message": response.text
            })
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            return response.text
            
    except requests.RequestException as e:
        logger.error(f"Request failed: {e}")
        return json.dumps({"error": f"Request failed: {str(e)}"})
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return json.dumps({"error": f"Error: {str(e)}"})