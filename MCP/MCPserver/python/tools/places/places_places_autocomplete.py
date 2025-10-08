"""PlacesPlacesAutocomplete tool implementation."""
import json
import logging
from typing import Any
import requests
from server import mcp

logger = logging.getLogger(__name__)


@mcp.tool()
def placesplacesautocomplete(
    includeQueryPredictions: bool = None,
    includedPrimaryTypes: list = None,
    includedRegionCodes: list = None,
    input: str = None,
    inputOffset: int = None,
    languageCode: str = None,
    locationBias: dict = None,
    locationRestriction: dict = None,
    origin: dict = None,
    regionCode: str = None,
    sessionToken: str = None
) -> str:
    """
    Returns predictions for the given input.
    
    Args:
        includeQueryPredictions: Input parameter: Optional. If true, the response will include both Place and query predictions. Otherwise the response will only return Place predictions.
        includedPrimaryTypes: Input parameter: Optional. Included primary Place type (for example, \"restaurant\" or \"gas_station\") from https://developers.google.com/maps/documentation/places/web-service/place-types. A Place is only returned if its primary type is included in this list. Up to 5 values can be specified. If no types are specified, all Place types are returned.
        includedRegionCodes: Input parameter: Optional. Only include results in the specified regions, specified as up to 15 CLDR two-character region codes. An empty set will not restrict the results. If both `location_restriction` and `included_region_codes` are set, the results will be located in the area of intersection.
        input: Input parameter: Required. The text string on which to search.
        inputOffset: Input parameter: Optional. A zero-based Unicode character offset of `input` indicating the cursor position in `input`. The cursor position may influence what predictions are returned. If empty, defaults to the length of `input`.
        languageCode: Input parameter: Optional. The language in which to return results. Defaults to en-US. The results may be in mixed languages if the language used in `input` is different from `language_code` or if the returned Place does not have a translation from the local language to `language_code`.
        locationBias: Input parameter: The region to search. The results may be biased around the specified region.
        locationRestriction: Input parameter: The region to search. The results will be restricted to the specified region.
        origin: Input parameter: An object that represents a latitude/longitude pair. This is expressed as a pair of doubles to represent degrees latitude and degrees longitude. Unless specified otherwise, this object must conform to the WGS84 standard. Values must be within normalized ranges.
        regionCode: Input parameter: Optional. The region code, specified as a CLDR two-character region code. This affects address formatting, result ranking, and may influence what results are returned. This does not restrict results to the specified region. To restrict results to a region, use `region_code_restriction`.
        sessionToken: Input parameter: Optional. A string which identifies an Autocomplete session for billing purposes. Must be a URL and filename safe base64 string with at most 36 ASCII characters in length. Otherwise an INVALID_ARGUMENT error is returned. The session begins when the user starts typing a query, and concludes when they select a place and a call to Place Details or Address Validation is made. Each session can have multiple queries, followed by one Place Details or Address Validation request. The credentials used for each request within a session must belong to the same Google Cloud Console project. Once a session has concluded, the token is no longer valid; your app must generate a fresh token for each session. If the `session_token` parameter is omitted, or if you reuse a session token, the session is charged as if no session token was provided (each request is billed separately). We recommend the following guidelines: * Use session tokens for all Place Autocomplete calls. * Generate a fresh token for each session. Using a version 4 UUID is recommended. * Ensure that the credentials used for all Place Autocomplete, Place Details, and Address Validation requests within a session belong to the same Cloud Console project. * Be sure to pass a unique session token for each new session. Using the same token for more than one session will result in each request being billed individually.
        
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
    if includeQueryPredictions is not None:
        request_body["includeQueryPredictions"] = includeQueryPredictions
    if includedPrimaryTypes is not None:
        request_body["includedPrimaryTypes"] = includedPrimaryTypes
    if includedRegionCodes is not None:
        request_body["includedRegionCodes"] = includedRegionCodes
    if input is not None:
        request_body["input"] = input
    if inputOffset is not None:
        request_body["inputOffset"] = inputOffset
    if languageCode is not None:
        request_body["languageCode"] = languageCode
    if locationBias is not None:
        request_body["locationBias"] = locationBias
    if locationRestriction is not None:
        request_body["locationRestriction"] = locationRestriction
    if origin is not None:
        request_body["origin"] = origin
    if regionCode is not None:
        request_body["regionCode"] = regionCode
    if sessionToken is not None:
        request_body["sessionToken"] = sessionToken
    
    # Build URL
    url = f"{config['base_url']}/v1/places:autocomplete"
    
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