"""PlacesPlacesPhotosGetMedia tool implementation."""
import json
import logging
from typing import Any
import requests
from server import mcp

logger = logging.getLogger(__name__)


@mcp.tool()
def placesplacesphotosgetmedia(
    name: str,
    maxHeightPx: int = None,
    maxWidthPx: int = None,
    skipHttpRedirect: bool = None
) -> str:
    """
    Get a photo media with a photo reference string.
    
    Args:
        name: Required. The resource name of a photo media in the format: `places/{place_id}/photos/{photo_reference}/media`. The resource name of a photo as returned in a Place object's `photos.name` field comes with the format `places/{place_id}/photos/{photo_reference}`. You need to append `/media` at the end of the photo resource to get the photo media resource name.
        maxHeightPx: Optional. Specifies the maximum desired height, in pixels, of the image. If the image is smaller than the values specified, the original image will be returned. If the image is larger in either dimension, it will be scaled to match the smaller of the two dimensions, restricted to its original aspect ratio. Both the max_height_px and max_width_px properties accept an integer between 1 and 4800, inclusively. If the value is not within the allowed range, an INVALID_ARGUMENT error will be returned. At least one of max_height_px or max_width_px needs to be specified. If neither max_height_px nor max_width_px is specified, an INVALID_ARGUMENT error will be returned.
        maxWidthPx: Optional. Specifies the maximum desired width, in pixels, of the image. If the image is smaller than the values specified, the original image will be returned. If the image is larger in either dimension, it will be scaled to match the smaller of the two dimensions, restricted to its original aspect ratio. Both the max_height_px and max_width_px properties accept an integer between 1 and 4800, inclusively. If the value is not within the allowed range, an INVALID_ARGUMENT error will be returned. At least one of max_height_px or max_width_px needs to be specified. If neither max_height_px nor max_width_px is specified, an INVALID_ARGUMENT error will be returned.
        skipHttpRedirect: Optional. If set, skip the default HTTP redirect behavior and render a text format (for example, in JSON format for HTTP use case) response. If not set, an HTTP redirect will be issued to redirect the call to the image media. This option is ignored for non-HTTP requests.
        
    Returns:
        JSON string result
    """
    from config import load_api_config
    config = load_api_config()
    # Validate required path parameters
    if not name:
        return json.dumps({"error": "Missing required path parameter: name"})
    # Build query parameters
    query_params = {}
    if maxHeightPx is not None:
        query_params["maxHeightPx"] = maxHeightPx
    if maxWidthPx is not None:
        query_params["maxWidthPx"] = maxWidthPx
    if skipHttpRedirect is not None:
        query_params["skipHttpRedirect"] = skipHttpRedirect
    # Handle multiple authentication parameters
    if config.get("bearer_token"):
        query_params["access_token"] = config["bearer_token"]
    if config.get("api_key"):
        query_params["key"] = config["api_key"]
    if config.get("bearer_token"):
        query_params["oauth_token"] = config["bearer_token"]
    
    # Build URL
    url = f"{config['base_url']}/v1/{name}"
    
    # Build headers
    headers = {
        "Accept": "application/json",
        "X-Request-Source": "Codeglide-MCP-generator",
    }
    # Set authentication
    # Handle multiple authentication parameters
    
    # Add custom headers
    
    try:
        # Make API request
        response = requests.request(
            method="GET",
            url=url,
            params=query_params,
            headers=headers,
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