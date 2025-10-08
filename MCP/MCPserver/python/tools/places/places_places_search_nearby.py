"""PlacesPlacesSearchNearby tool implementation."""
import json
import logging
from typing import Any
import requests
from server import mcp

logger = logging.getLogger(__name__)


@mcp.tool()
def placesplacessearchnearby(
    excludedPrimaryTypes: list = None,
    excludedTypes: list = None,
    includedPrimaryTypes: list = None,
    includedTypes: list = None,
    languageCode: str = None,
    locationRestriction: dict = None,
    maxResultCount: int = None,
    rankPreference: str = None,
    regionCode: str = None
) -> str:
    """
    Search for places near locations.
    
    Args:
        excludedPrimaryTypes: Input parameter: Excluded primary Place type (e.g. \"restaurant\" or \"gas_station\") from https://developers.google.com/maps/documentation/places/web-service/place-types. Up to 50 types from [Table A](https://developers.google.com/maps/documentation/places/web-service/place-types#table-a) may be specified. If there are any conflicting primary types, i.e. a type appears in both included_primary_types and excluded_primary_types, an INVALID_ARGUMENT error is returned. If a Place type is specified with multiple type restrictions, only places that satisfy all of the restrictions are returned. For example, if we have {included_types = [\"restaurant\"], excluded_primary_types = [\"restaurant\"]}, the returned places provide \"restaurant\" related services but do not operate primarily as \"restaurants\".
        excludedTypes: Input parameter: Excluded Place type (eg, \"restaurant\" or \"gas_station\") from https://developers.google.com/maps/documentation/places/web-service/place-types. Up to 50 types from [Table A](https://developers.google.com/maps/documentation/places/web-service/place-types#table-a) may be specified. If the client provides both included_types (e.g. restaurant) and excluded_types (e.g. cafe), then the response should include places that are restaurant but not cafe. The response includes places that match at least one of the included_types and none of the excluded_types. If there are any conflicting types, i.e. a type appears in both included_types and excluded_types, an INVALID_ARGUMENT error is returned. If a Place type is specified with multiple type restrictions, only places that satisfy all of the restrictions are returned. For example, if we have {included_types = [\"restaurant\"], excluded_primary_types = [\"restaurant\"]}, the returned places provide \"restaurant\" related services but do not operate primarily as \"restaurants\".
        includedPrimaryTypes: Input parameter: Included primary Place type (e.g. \"restaurant\" or \"gas_station\") from https://developers.google.com/maps/documentation/places/web-service/place-types. A place can only have a single primary type from the supported types table associated with it. Up to 50 types from [Table A](https://developers.google.com/maps/documentation/places/web-service/place-types#table-a) may be specified. If there are any conflicting primary types, i.e. a type appears in both included_primary_types and excluded_primary_types, an INVALID_ARGUMENT error is returned. If a Place type is specified with multiple type restrictions, only places that satisfy all of the restrictions are returned. For example, if we have {included_types = [\"restaurant\"], excluded_primary_types = [\"restaurant\"]}, the returned places provide \"restaurant\" related services but do not operate primarily as \"restaurants\".
        includedTypes: Input parameter: Included Place type (eg, \"restaurant\" or \"gas_station\") from https://developers.google.com/maps/documentation/places/web-service/place-types. Up to 50 types from [Table A](https://developers.google.com/maps/documentation/places/web-service/place-types#table-a) may be specified. If there are any conflicting types, i.e. a type appears in both included_types and excluded_types, an INVALID_ARGUMENT error is returned. If a Place type is specified with multiple type restrictions, only places that satisfy all of the restrictions are returned. For example, if we have {included_types = [\"restaurant\"], excluded_primary_types = [\"restaurant\"]}, the returned places provide \"restaurant\" related services but do not operate primarily as \"restaurants\".
        languageCode: Input parameter: Place details will be displayed with the preferred language if available. If the language code is unspecified or unrecognized, place details of any language may be returned, with a preference for English if such details exist. Current list of supported languages: https://developers.google.com/maps/faq#languagesupport.
        locationRestriction: Input parameter: The region to search.
        maxResultCount: Input parameter: Maximum number of results to return. It must be between 1 and 20 (default), inclusively. If the number is unset, it falls back to the upper limit. If the number is set to negative or exceeds the upper limit, an INVALID_ARGUMENT error is returned.
        rankPreference: Input parameter: How results will be ranked in the response.
        regionCode: Input parameter: The Unicode country/region code (CLDR) of the location where the request is coming from. This parameter is used to display the place details, like region-specific place name, if available. The parameter can affect results based on applicable law. For more information, see https://www.unicode.org/cldr/charts/latest/supplemental/territory_language_information.html. Note that 3-digit region codes are not currently supported.
        
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
    if excludedPrimaryTypes is not None:
        request_body["excludedPrimaryTypes"] = excludedPrimaryTypes
    if excludedTypes is not None:
        request_body["excludedTypes"] = excludedTypes
    if includedPrimaryTypes is not None:
        request_body["includedPrimaryTypes"] = includedPrimaryTypes
    if includedTypes is not None:
        request_body["includedTypes"] = includedTypes
    if languageCode is not None:
        request_body["languageCode"] = languageCode
    if locationRestriction is not None:
        request_body["locationRestriction"] = locationRestriction
    if maxResultCount is not None:
        request_body["maxResultCount"] = maxResultCount
    if rankPreference is not None:
        request_body["rankPreference"] = rankPreference
    if regionCode is not None:
        request_body["regionCode"] = regionCode
    
    # Build URL
    url = f"{config['base_url']}/v1/places:searchNearby"
    
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