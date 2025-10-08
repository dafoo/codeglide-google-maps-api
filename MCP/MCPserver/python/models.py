"""Data models for places_api_new."""
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field


class GoogleGeoTypeViewport(BaseModel):
    """GoogleGeoTypeViewport schema from the OpenAPI specification."""
    high: GoogleTypeLatLng = Field(alias="high")  # An object that represents a latitude/longitude pair. This is expressed as a pair of doubles to represent degrees latitude and degrees longitude. Unless specified otherwise, this object must conform to the WGS84 standard. Values must be within normalized ranges.
    low: GoogleTypeLatLng = Field(alias="low")  # An object that represents a latitude/longitude pair. This is expressed as a pair of doubles to represent degrees latitude and degrees longitude. Unless specified otherwise, this object must conform to the WGS84 standard. Values must be within normalized ranges.
    
    class Config:
        populate_by_name = True


class GoogleMapsPlacesV1AuthorAttribution(BaseModel):
    """GoogleMapsPlacesV1AuthorAttribution schema from the OpenAPI specification."""
    display_name: str = Field(alias="displayName")  # Name of the author of the Photo or Review.
    photo_uri: str = Field(alias="photoUri")  # Profile photo URI of the author of the Photo or Review.
    uri: str = Field(alias="uri")  # URI of the author of the Photo or Review.
    
    class Config:
        populate_by_name = True


class GoogleMapsPlacesV1AutocompletePlacesRequest(BaseModel):
    """GoogleMapsPlacesV1AutocompletePlacesRequest schema from the OpenAPI specification."""
    include_query_predictions: bool = Field(alias="includeQueryPredictions")  # Optional. If true, the response will include both Place and query predictions. Otherwise the response will only return Place predictions.
    included_primary_types: List[str] = Field(alias="includedPrimaryTypes")  # Optional. Included primary Place type (for example, \"restaurant\" or \"gas_station\") from https://developers.google.com/maps/documentation/places/web-service/place-types. A Place is only returned if its primary type is included in this list. Up to 5 values can be specified. If no types are specified, all Place types are returned.
    included_region_codes: List[str] = Field(alias="includedRegionCodes")  # Optional. Only include results in the specified regions, specified as up to 15 CLDR two-character region codes. An empty set will not restrict the results. If both `location_restriction` and `included_region_codes` are set, the results will be located in the area of intersection.
    input: str = Field(alias="input")  # Required. The text string on which to search.
    input_offset: int = Field(alias="inputOffset")  # Optional. A zero-based Unicode character offset of `input` indicating the cursor position in `input`. The cursor position may influence what predictions are returned. If empty, defaults to the length of `input`.
    language_code: str = Field(alias="languageCode")  # Optional. The language in which to return results. Defaults to en-US. The results may be in mixed languages if the language used in `input` is different from `language_code` or if the returned Place does not have a translation from the local language to `language_code`.
    location_bias: Any = Field(alias="locationBias")  # The region to search. The results may be biased around the specified region.
    location_restriction: Any = Field(alias="locationRestriction")  # The region to search. The results will be restricted to the specified region.
    origin: GoogleTypeLatLng = Field(alias="origin")  # An object that represents a latitude/longitude pair. This is expressed as a pair of doubles to represent degrees latitude and degrees longitude. Unless specified otherwise, this object must conform to the WGS84 standard. Values must be within normalized ranges.
    region_code: str = Field(alias="regionCode")  # Optional. The region code, specified as a CLDR two-character region code. This affects address formatting, result ranking, and may influence what results are returned. This does not restrict results to the specified region. To restrict results to a region, use `region_code_restriction`.
    session_token: str = Field(alias="sessionToken")  # Optional. A string which identifies an Autocomplete session for billing purposes. Must be a URL and filename safe base64 string with at most 36 ASCII characters in length. Otherwise an INVALID_ARGUMENT error is returned. The session begins when the user starts typing a query, and concludes when they select a place and a call to Place Details or Address Validation is made. Each session can have multiple queries, followed by one Place Details or Address Validation request. The credentials used for each request within a session must belong to the same Google Cloud Console project. Once a session has concluded, the token is no longer valid; your app must generate a fresh token for each session. If the `session_token` parameter is omitted, or if you reuse a session token, the session is charged as if no session token was provided (each request is billed separately). We recommend the following guidelines: * Use session tokens for all Place Autocomplete calls. * Generate a fresh token for each session. Using a version 4 UUID is recommended. * Ensure that the credentials used for all Place Autocomplete, Place Details, and Address Validation requests within a session belong to the same Cloud Console project. * Be sure to pass a unique session token for each new session. Using the same token for more than one session will result in each request being billed individually.
    
    class Config:
        populate_by_name = True


class GoogleMapsPlacesV1AutocompletePlacesResponse(BaseModel):
    """GoogleMapsPlacesV1AutocompletePlacesResponse schema from the OpenAPI specification."""
    suggestions: List[GoogleMapsPlacesV1AutocompletePlacesResponseSuggestion] = Field(alias="suggestions")  # Contains a list of suggestions, ordered in descending order of relevance.
    
    class Config:
        populate_by_name = True


class GoogleMapsPlacesV1AutocompletePlacesResponseSuggestion(BaseModel):
    """GoogleMapsPlacesV1AutocompletePlacesResponseSuggestion schema from the OpenAPI specification."""
    place_prediction: GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionPlacePrediction = Field(alias="placePrediction")  # Prediction results for a Place Autocomplete prediction.
    query_prediction: GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionQueryPrediction = Field(alias="queryPrediction")  # Prediction results for a Query Autocomplete prediction.
    
    class Config:
        populate_by_name = True


class GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionFormattableText(BaseModel):
    """GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionFormattableText schema from the OpenAPI specification."""
    matches: List[GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionStringRange] = Field(alias="matches")  # A list of string ranges identifying where the input request matched in `text`. The ranges can be used to format specific parts of `text`. The substrings may not be exact matches of `input` if the matching was determined by criteria other than string matching (for example, spell corrections or transliterations). These values are Unicode character offsets of `text`. The ranges are guaranteed to be ordered in increasing offset values.
    text: str = Field(alias="text")  # Text that may be used as is or formatted with `matches`.
    
    class Config:
        populate_by_name = True


class GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionPlacePrediction(BaseModel):
    """GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionPlacePrediction schema from the OpenAPI specification."""
    distance_meters: int = Field(alias="distanceMeters")  # The length of the geodesic in meters from `origin` if `origin` is specified. Certain predictions such as routes may not populate this field.
    place: str = Field(alias="place")  # The resource name of the suggested Place. This name can be used in other APIs that accept Place names.
    place_id: str = Field(alias="placeId")  # The unique identifier of the suggested Place. This identifier can be used in other APIs that accept Place IDs.
    structured_format: GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionStructuredFormat = Field(alias="structuredFormat")  # Contains a breakdown of a Place or query prediction into main text and secondary text. For Place predictions, the main text contains the specific name of the Place. For query predictions, the main text contains the query. The secondary text contains additional disambiguating features (such as a city or region) to further identify the Place or refine the query.
    text: GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionFormattableText = Field(alias="text")  # Text representing a Place or query prediction. The text may be used as is or formatted.
    types: List[str] = Field(alias="types")  # List of types that apply to this Place from Table A or Table B in https://developers.google.com/maps/documentation/places/web-service/place-types. A type is a categorization of a Place. Places with shared types will share similar characteristics.
    
    class Config:
        populate_by_name = True


class GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionQueryPrediction(BaseModel):
    """GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionQueryPrediction schema from the OpenAPI specification."""
    structured_format: GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionStructuredFormat = Field(alias="structuredFormat")  # Contains a breakdown of a Place or query prediction into main text and secondary text. For Place predictions, the main text contains the specific name of the Place. For query predictions, the main text contains the query. The secondary text contains additional disambiguating features (such as a city or region) to further identify the Place or refine the query.
    text: GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionFormattableText = Field(alias="text")  # Text representing a Place or query prediction. The text may be used as is or formatted.
    
    class Config:
        populate_by_name = True


class GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionStringRange(BaseModel):
    """GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionStringRange schema from the OpenAPI specification."""
    end_offset: int = Field(alias="endOffset")  # Zero-based offset of the last Unicode character (exclusive).
    start_offset: int = Field(alias="startOffset")  # Zero-based offset of the first Unicode character of the string (inclusive).
    
    class Config:
        populate_by_name = True


class GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionStructuredFormat(BaseModel):
    """GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionStructuredFormat schema from the OpenAPI specification."""
    main_text: GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionFormattableText = Field(alias="mainText")  # Text representing a Place or query prediction. The text may be used as is or formatted.
    secondary_text: GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionFormattableText = Field(alias="secondaryText")  # Text representing a Place or query prediction. The text may be used as is or formatted.
    
    class Config:
        populate_by_name = True


class GoogleMapsPlacesV1Circle(BaseModel):
    """GoogleMapsPlacesV1Circle schema from the OpenAPI specification."""
    center: GoogleTypeLatLng = Field(alias="center")  # An object that represents a latitude/longitude pair. This is expressed as a pair of doubles to represent degrees latitude and degrees longitude. Unless specified otherwise, this object must conform to the WGS84 standard. Values must be within normalized ranges.
    radius: float = Field(alias="radius")  # Required. Radius measured in meters. The radius must be within [0.0, 50000.0].
    
    class Config:
        populate_by_name = True


class GoogleMapsPlacesV1EVChargeOptions(BaseModel):
    """GoogleMapsPlacesV1EVChargeOptions schema from the OpenAPI specification."""
    connector_aggregation: List[GoogleMapsPlacesV1EVChargeOptionsConnectorAggregation] = Field(alias="connectorAggregation")  # A list of EV charging connector aggregations that contain connectors of the same type and same charge rate.
    connector_count: int = Field(alias="connectorCount")  # Number of connectors at this station. However, because some ports can have multiple connectors but only be able to charge one car at a time (e.g.) the number of connectors may be greater than the total number of cars which can charge simultaneously.
    
    class Config:
        populate_by_name = True


class GoogleMapsPlacesV1EVChargeOptionsConnectorAggregation(BaseModel):
    """GoogleMapsPlacesV1EVChargeOptionsConnectorAggregation schema from the OpenAPI specification."""
    availability_last_update_time: str = Field(alias="availabilityLastUpdateTime")  # The timestamp when the connector availability information in this aggregation was last updated.
    available_count: int = Field(alias="availableCount")  # Number of connectors in this aggregation that are currently available.
    count: int = Field(alias="count")  # Number of connectors in this aggregation.
    max_charge_rate_kw: float = Field(alias="maxChargeRateKw")  # The static max charging rate in kw of each connector in the aggregation.
    out_of_service_count: int = Field(alias="outOfServiceCount")  # Number of connectors in this aggregation that are currently out of service.
    type_field: str = Field(alias="type")  # The connector type of this aggregation.
    
    class Config:
        populate_by_name = True


class GoogleMapsPlacesV1FuelOptions(BaseModel):
    """GoogleMapsPlacesV1FuelOptions schema from the OpenAPI specification."""
    fuel_prices: List[GoogleMapsPlacesV1FuelOptionsFuelPrice] = Field(alias="fuelPrices")  # The last known fuel price for each type of fuel this station has. There is one entry per fuel type this station has. Order is not important.
    
    class Config:
        populate_by_name = True


class GoogleMapsPlacesV1FuelOptionsFuelPrice(BaseModel):
    """GoogleMapsPlacesV1FuelOptionsFuelPrice schema from the OpenAPI specification."""
    price: GoogleTypeMoney = Field(alias="price")  # Represents an amount of money with its currency type.
    type_field: str = Field(alias="type")  # The type of fuel.
    update_time: str = Field(alias="updateTime")  # The time the fuel price was last updated.
    
    class Config:
        populate_by_name = True


class GoogleMapsPlacesV1Photo(BaseModel):
    """GoogleMapsPlacesV1Photo schema from the OpenAPI specification."""
    author_attributions: List[GoogleMapsPlacesV1AuthorAttribution] = Field(alias="authorAttributions")  # This photo\'s authors.
    height_px: int = Field(alias="heightPx")  # The maximum available height, in pixels.
    name: str = Field(alias="name")  # Identifier. A reference representing this place photo which may be used to look up this place photo again (also called the API \"resource\" name: `places/{place_id}/photos/{photo}`).
    width_px: int = Field(alias="widthPx")  # The maximum available width, in pixels.
    
    class Config:
        populate_by_name = True


class GoogleMapsPlacesV1PhotoMedia(BaseModel):
    """GoogleMapsPlacesV1PhotoMedia schema from the OpenAPI specification."""
    name: str = Field(alias="name")  # The resource name of a photo media in the format: `places/{place_id}/photos/{photo_reference}/media`.
    photo_uri: str = Field(alias="photoUri")  # A short-lived uri that can be used to render the photo.
    
    class Config:
        populate_by_name = True


class GoogleMapsPlacesV1Place(BaseModel):
    """GoogleMapsPlacesV1Place schema from the OpenAPI specification."""
    accessibility_options: GoogleMapsPlacesV1PlaceAccessibilityOptions = Field(alias="accessibilityOptions")  # Information about the accessibility options a place offers.
    address_components: List[GoogleMapsPlacesV1PlaceAddressComponent] = Field(alias="addressComponents")  # Repeated components for each locality level. Note the following facts about the address_components[] array: - The array of address components may contain more components than the formatted_address. - The array does not necessarily include all the political entities that contain an address, apart from those included in the formatted_address. To retrieve all the political entities that contain a specific address, you should use reverse geocoding, passing the latitude/longitude of the address as a parameter to the request. - The format of the response is not guaranteed to remain the same between requests. In particular, the number of address_components varies based on the address requested and can change over time for the same address. A component can change position in the array. The type of the component can change. A particular component may be missing in a later response.
    adr_format_address: str = Field(alias="adrFormatAddress")  # The place\'s address in adr microformat: http://microformats.org/wiki/adr.
    allows_dogs: bool = Field(alias="allowsDogs")  # Place allows dogs.
    attributions: List[GoogleMapsPlacesV1PlaceAttribution] = Field(alias="attributions")  # A set of data provider that must be shown with this result.
    business_status: str = Field(alias="businessStatus")  # The business status for the place.
    curbside_pickup: bool = Field(alias="curbsidePickup")  # Specifies if the business supports curbside pickup.
    current_opening_hours: GoogleMapsPlacesV1PlaceOpeningHours = Field(alias="currentOpeningHours")  # Information about business hour of the place.
    current_secondary_opening_hours: List[GoogleMapsPlacesV1PlaceOpeningHours] = Field(alias="currentSecondaryOpeningHours")  # Contains an array of entries for the next seven days including information about secondary hours of a business. Secondary hours are different from a business\'s main hours. For example, a restaurant can specify drive through hours or delivery hours as its secondary hours. This field populates the type subfield, which draws from a predefined list of opening hours types (such as DRIVE_THROUGH, PICKUP, or TAKEOUT) based on the types of the place. This field includes the special_days subfield of all hours, set for dates that have exceptional hours.
    delivery: bool = Field(alias="delivery")  # Specifies if the business supports delivery.
    dine_in: bool = Field(alias="dineIn")  # Specifies if the business supports indoor or outdoor seating options.
    display_name: GoogleTypeLocalizedText = Field(alias="displayName")  # Localized variant of a text in a particular language.
    editorial_summary: GoogleTypeLocalizedText = Field(alias="editorialSummary")  # Localized variant of a text in a particular language.
    ev_charge_options: GoogleMapsPlacesV1EVChargeOptions = Field(alias="evChargeOptions")  # Information about the EV Charge Station hosted in Place. Terminology follows https://afdc.energy.gov/fuels/electricity_infrastructure.html One port could charge one car at a time. One port has one or more connectors. One station has one or more ports.
    formatted_address: str = Field(alias="formattedAddress")  # A full, human-readable address for this place.
    fuel_options: GoogleMapsPlacesV1FuelOptions = Field(alias="fuelOptions")  # The most recent information about fuel options in a gas station. This information is updated regularly.
    good_for_children: bool = Field(alias="goodForChildren")  # Place is good for children.
    good_for_groups: bool = Field(alias="goodForGroups")  # Place accommodates groups.
    good_for_watching_sports: bool = Field(alias="goodForWatchingSports")  # Place is suitable for watching sports.
    google_maps_uri: str = Field(alias="googleMapsUri")  # A URL providing more information about this place.
    icon_background_color: str = Field(alias="iconBackgroundColor")  # Background color for icon_mask in hex format, e.g. #909CE1.
    icon_mask_base_uri: str = Field(alias="iconMaskBaseUri")  # A truncated URL to an icon mask. User can access different icon type by appending type suffix to the end (eg, \".svg\" or \".png\").
    id_field: str = Field(alias="id")  # The unique identifier of a place.
    international_phone_number: str = Field(alias="internationalPhoneNumber")  # A human-readable phone number for the place, in international format.
    live_music: bool = Field(alias="liveMusic")  # Place provides live music.
    location: GoogleTypeLatLng = Field(alias="location")  # An object that represents a latitude/longitude pair. This is expressed as a pair of doubles to represent degrees latitude and degrees longitude. Unless specified otherwise, this object must conform to the WGS84 standard. Values must be within normalized ranges.
    menu_for_children: bool = Field(alias="menuForChildren")  # Place has a children\'s menu.
    name: str = Field(alias="name")  # This Place\'s resource name, in `places/{place_id}` format. Can be used to look up the Place.
    national_phone_number: str = Field(alias="nationalPhoneNumber")  # A human-readable phone number for the place, in national format.
    outdoor_seating: bool = Field(alias="outdoorSeating")  # Place provides outdoor seating.
    parking_options: GoogleMapsPlacesV1PlaceParkingOptions = Field(alias="parkingOptions")  # Information about parking options for the place. A parking lot could support more than one option at the same time.
    payment_options: GoogleMapsPlacesV1PlacePaymentOptions = Field(alias="paymentOptions")  # Payment options the place accepts.
    photos: List[GoogleMapsPlacesV1Photo] = Field(alias="photos")  # Information (including references) about photos of this place. A maximum of 10 photos can be returned.
    plus_code: GoogleMapsPlacesV1PlacePlusCode = Field(alias="plusCode")  # Plus code (http://plus.codes) is a location reference with two formats: global code defining a 14mx14m (1/8000th of a degree) or smaller rectangle, and compound code, replacing the prefix with a reference location.
    price_level: str = Field(alias="priceLevel")  # Price level of the place.
    primary_type: str = Field(alias="primaryType")  # The primary type of the given result. This type must one of the Places API supported types. For example, \"restaurant\", \"cafe\", \"airport\", etc. A place can only have a single primary type. For the complete list of possible values, see Table A and Table B at https://developers.google.com/maps/documentation/places/web-service/place-types
    primary_type_display_name: GoogleTypeLocalizedText = Field(alias="primaryTypeDisplayName")  # Localized variant of a text in a particular language.
    rating: float = Field(alias="rating")  # A rating between 1.0 and 5.0, based on user reviews of this place.
    regular_opening_hours: GoogleMapsPlacesV1PlaceOpeningHours = Field(alias="regularOpeningHours")  # Information about business hour of the place.
    regular_secondary_opening_hours: List[GoogleMapsPlacesV1PlaceOpeningHours] = Field(alias="regularSecondaryOpeningHours")  # Contains an array of entries for information about regular secondary hours of a business. Secondary hours are different from a business\'s main hours. For example, a restaurant can specify drive through hours or delivery hours as its secondary hours. This field populates the type subfield, which draws from a predefined list of opening hours types (such as DRIVE_THROUGH, PICKUP, or TAKEOUT) based on the types of the place.
    reservable: bool = Field(alias="reservable")  # Specifies if the place supports reservations.
    restroom: bool = Field(alias="restroom")  # Place has restroom.
    reviews: List[GoogleMapsPlacesV1Review] = Field(alias="reviews")  # List of reviews about this place, sorted by relevance. A maximum of 5 reviews can be returned.
    serves_beer: bool = Field(alias="servesBeer")  # Specifies if the place serves beer.
    serves_breakfast: bool = Field(alias="servesBreakfast")  # Specifies if the place serves breakfast.
    serves_brunch: bool = Field(alias="servesBrunch")  # Specifies if the place serves brunch.
    serves_cocktails: bool = Field(alias="servesCocktails")  # Place serves cocktails.
    serves_coffee: bool = Field(alias="servesCoffee")  # Place serves coffee.
    serves_dessert: bool = Field(alias="servesDessert")  # Place serves dessert.
    serves_dinner: bool = Field(alias="servesDinner")  # Specifies if the place serves dinner.
    serves_lunch: bool = Field(alias="servesLunch")  # Specifies if the place serves lunch.
    serves_vegetarian_food: bool = Field(alias="servesVegetarianFood")  # Specifies if the place serves vegetarian food.
    serves_wine: bool = Field(alias="servesWine")  # Specifies if the place serves wine.
    short_formatted_address: str = Field(alias="shortFormattedAddress")  # A short, human-readable address for this place.
    sub_destinations: List[GoogleMapsPlacesV1PlaceSubDestination] = Field(alias="subDestinations")  # A list of sub destinations related to the place.
    takeout: bool = Field(alias="takeout")  # Specifies if the business supports takeout.
    types: List[str] = Field(alias="types")  # A set of type tags for this result. For example, \"political\" and \"locality\". For the complete list of possible values, see Table A and Table B at https://developers.google.com/maps/documentation/places/web-service/place-types
    user_rating_count: int = Field(alias="userRatingCount")  # The total number of reviews (with or without text) for this place.
    utc_offset_minutes: int = Field(alias="utcOffsetMinutes")  # Number of minutes this place\'s timezone is currently offset from UTC. This is expressed in minutes to support timezones that are offset by fractions of an hour, e.g. X hours and 15 minutes.
    viewport: GoogleGeoTypeViewport = Field(alias="viewport")  # A latitude-longitude viewport, represented as two diagonally opposite `low` and `high` points. A viewport is considered a closed region, i.e. it includes its boundary. The latitude bounds must range between -90 to 90 degrees inclusive, and the longitude bounds must range between -180 to 180 degrees inclusive. Various cases include: - If `low` = `high`, the viewport consists of that single point. - If `low.longitude` > `high.longitude`, the longitude range is inverted (the viewport crosses the 180 degree longitude line). - If `low.longitude` = -180 degrees and `high.longitude` = 180 degrees, the viewport includes all longitudes. - If `low.longitude` = 180 degrees and `high.longitude` = -180 degrees, the longitude range is empty. - If `low.latitude` > `high.latitude`, the latitude range is empty. Both `low` and `high` must be populated, and the represented box cannot be empty (as specified by the definitions above). An empty viewport will result in an error. For example, this viewport fully encloses New York City: { \"low\": { \"latitude\": 40.477398, \"longitude\": -74.259087 }, \"high\": { \"latitude\": 40.91618, \"longitude\": -73.70018 } }
    website_uri: str = Field(alias="websiteUri")  # The authoritative website for this place, e.g. a business\' homepage. Note that for places that are part of a chain (e.g. an IKEA store), this will usually be the website for the individual store, not the overall chain.
    
    class Config:
        populate_by_name = True


class GoogleMapsPlacesV1PlaceAccessibilityOptions(BaseModel):
    """GoogleMapsPlacesV1PlaceAccessibilityOptions schema from the OpenAPI specification."""
    wheelchair_accessible_entrance: bool = Field(alias="wheelchairAccessibleEntrance")  # Places has wheelchair accessible entrance.
    wheelchair_accessible_parking: bool = Field(alias="wheelchairAccessibleParking")  # Place offers wheelchair accessible parking.
    wheelchair_accessible_restroom: bool = Field(alias="wheelchairAccessibleRestroom")  # Place has wheelchair accessible restroom.
    wheelchair_accessible_seating: bool = Field(alias="wheelchairAccessibleSeating")  # Place has wheelchair accessible seating.
    
    class Config:
        populate_by_name = True


class GoogleMapsPlacesV1PlaceAddressComponent(BaseModel):
    """GoogleMapsPlacesV1PlaceAddressComponent schema from the OpenAPI specification."""
    language_code: str = Field(alias="languageCode")  # The language used to format this components, in CLDR notation.
    long_text: str = Field(alias="longText")  # The full text description or name of the address component. For example, an address component for the country Australia may have a long_name of \"Australia\".
    short_text: str = Field(alias="shortText")  # An abbreviated textual name for the address component, if available. For example, an address component for the country of Australia may have a short_name of \"AU\".
    types: List[str] = Field(alias="types")  # An array indicating the type(s) of the address component.
    
    class Config:
        populate_by_name = True


class GoogleMapsPlacesV1PlaceAttribution(BaseModel):
    """GoogleMapsPlacesV1PlaceAttribution schema from the OpenAPI specification."""
    provider: str = Field(alias="provider")  # Name of the Place\'s data provider.
    provider_uri: str = Field(alias="providerUri")  # URI to the Place\'s data provider.
    
    class Config:
        populate_by_name = True


class GoogleMapsPlacesV1PlaceOpeningHours(BaseModel):
    """GoogleMapsPlacesV1PlaceOpeningHours schema from the OpenAPI specification."""
    open_now: bool = Field(alias="openNow")  # Is this place open right now? Always present unless we lack time-of-day or timezone data for these opening hours.
    periods: List[GoogleMapsPlacesV1PlaceOpeningHoursPeriod] = Field(alias="periods")  # The periods that this place is open during the week. The periods are in chronological order, starting with Sunday in the place-local timezone. An empty (but not absent) value indicates a place that is never open, e.g. because it is closed temporarily for renovations.
    secondary_hours_type: str = Field(alias="secondaryHoursType")  # A type string used to identify the type of secondary hours.
    special_days: List[GoogleMapsPlacesV1PlaceOpeningHoursSpecialDay] = Field(alias="specialDays")  # Structured information for special days that fall within the period that the returned opening hours cover. Special days are days that could impact the business hours of a place, e.g. Christmas day. Set for current_opening_hours and current_secondary_opening_hours if there are exceptional hours.
    weekday_descriptions: List[str] = Field(alias="weekdayDescriptions")  # Localized strings describing the opening hours of this place, one string for each day of the week. Will be empty if the hours are unknown or could not be converted to localized text. Example: \"Sun: 18:00–06:00\"
    
    class Config:
        populate_by_name = True


class GoogleMapsPlacesV1PlaceOpeningHoursPeriod(BaseModel):
    """GoogleMapsPlacesV1PlaceOpeningHoursPeriod schema from the OpenAPI specification."""
    close: GoogleMapsPlacesV1PlaceOpeningHoursPeriodPoint = Field(alias="close")  # Status changing points.
    open: GoogleMapsPlacesV1PlaceOpeningHoursPeriodPoint = Field(alias="open")  # Status changing points.
    
    class Config:
        populate_by_name = True


class GoogleMapsPlacesV1PlaceOpeningHoursPeriodPoint(BaseModel):
    """GoogleMapsPlacesV1PlaceOpeningHoursPeriodPoint schema from the OpenAPI specification."""
    date: GoogleTypeDate = Field(alias="date")  # Represents a whole or partial calendar date, such as a birthday. The time of day and time zone are either specified elsewhere or are insignificant. The date is relative to the Gregorian Calendar. This can represent one of the following: * A full date, with non-zero year, month, and day values. * A month and day, with a zero year (for example, an anniversary). * A year on its own, with a zero month and a zero day. * A year and month, with a zero day (for example, a credit card expiration date). Related types: * google.type.TimeOfDay * google.type.DateTime * google.protobuf.Timestamp
    day: int = Field(alias="day")  # A day of the week, as an integer in the range 0-6. 0 is Sunday, 1 is Monday, etc.
    hour: int = Field(alias="hour")  # The hour in 2 digits. Ranges from 00 to 23.
    minute: int = Field(alias="minute")  # The minute in 2 digits. Ranges from 00 to 59.
    truncated: bool = Field(alias="truncated")  # Whether or not this endpoint was truncated. Truncation occurs when the real hours are outside the times we are willing to return hours between, so we truncate the hours back to these boundaries. This ensures that at most 24 * 7 hours from midnight of the day of the request are returned.
    
    class Config:
        populate_by_name = True


class GoogleMapsPlacesV1PlaceOpeningHoursSpecialDay(BaseModel):
    """GoogleMapsPlacesV1PlaceOpeningHoursSpecialDay schema from the OpenAPI specification."""
    date: GoogleTypeDate = Field(alias="date")  # Represents a whole or partial calendar date, such as a birthday. The time of day and time zone are either specified elsewhere or are insignificant. The date is relative to the Gregorian Calendar. This can represent one of the following: * A full date, with non-zero year, month, and day values. * A month and day, with a zero year (for example, an anniversary). * A year on its own, with a zero month and a zero day. * A year and month, with a zero day (for example, a credit card expiration date). Related types: * google.type.TimeOfDay * google.type.DateTime * google.protobuf.Timestamp
    
    class Config:
        populate_by_name = True


class GoogleMapsPlacesV1PlaceParkingOptions(BaseModel):
    """GoogleMapsPlacesV1PlaceParkingOptions schema from the OpenAPI specification."""
    free_garage_parking: bool = Field(alias="freeGarageParking")  # Place offers free garage parking.
    free_parking_lot: bool = Field(alias="freeParkingLot")  # Place offers free parking lots.
    free_street_parking: bool = Field(alias="freeStreetParking")  # Place offers free street parking.
    paid_garage_parking: bool = Field(alias="paidGarageParking")  # Place offers paid garage parking.
    paid_parking_lot: bool = Field(alias="paidParkingLot")  # Place offers paid parking lots.
    paid_street_parking: bool = Field(alias="paidStreetParking")  # Place offers paid street parking.
    valet_parking: bool = Field(alias="valetParking")  # Place offers valet parking.
    
    class Config:
        populate_by_name = True


class GoogleMapsPlacesV1PlacePaymentOptions(BaseModel):
    """GoogleMapsPlacesV1PlacePaymentOptions schema from the OpenAPI specification."""
    accepts_cash_only: bool = Field(alias="acceptsCashOnly")  # Place accepts cash only as payment. Places with this attribute may still accept other payment methods.
    accepts_credit_cards: bool = Field(alias="acceptsCreditCards")  # Place accepts credit cards as payment.
    accepts_debit_cards: bool = Field(alias="acceptsDebitCards")  # Place accepts debit cards as payment.
    accepts_nfc: bool = Field(alias="acceptsNfc")  # Place accepts NFC payments.
    
    class Config:
        populate_by_name = True


class GoogleMapsPlacesV1PlacePlusCode(BaseModel):
    """GoogleMapsPlacesV1PlacePlusCode schema from the OpenAPI specification."""
    compound_code: str = Field(alias="compoundCode")  # Place\'s compound code, such as \"33GV+HQ, Ramberg, Norway\", containing the suffix of the global code and replacing the prefix with a formatted name of a reference entity.
    global_code: str = Field(alias="globalCode")  # Place\'s global (full) code, such as \"9FWM33GV+HQ\", representing an 1/8000 by 1/8000 degree area (~14 by 14 meters).
    
    class Config:
        populate_by_name = True


class GoogleMapsPlacesV1PlaceSubDestination(BaseModel):
    """GoogleMapsPlacesV1PlaceSubDestination schema from the OpenAPI specification."""
    id_field: str = Field(alias="id")  # The place id of the sub destination.
    name: str = Field(alias="name")  # The resource name of the sub destination.
    
    class Config:
        populate_by_name = True


class GoogleMapsPlacesV1Review(BaseModel):
    """GoogleMapsPlacesV1Review schema from the OpenAPI specification."""
    author_attribution: GoogleMapsPlacesV1AuthorAttribution = Field(alias="authorAttribution")  # Information about the author of the UGC data. Used in Photo, and Review.
    name: str = Field(alias="name")  # A reference representing this place review which may be used to look up this place review again (also called the API \"resource\" name: `places/{place_id}/reviews/{review}`).
    original_text: GoogleTypeLocalizedText = Field(alias="originalText")  # Localized variant of a text in a particular language.
    publish_time: str = Field(alias="publishTime")  # Timestamp for the review.
    rating: float = Field(alias="rating")  # A number between 1.0 and 5.0, also called the number of stars.
    relative_publish_time_description: str = Field(alias="relativePublishTimeDescription")  # A string of formatted recent time, expressing the review time relative to the current time in a form appropriate for the language and country.
    text: GoogleTypeLocalizedText = Field(alias="text")  # Localized variant of a text in a particular language.
    
    class Config:
        populate_by_name = True


class GoogleMapsPlacesV1SearchNearbyRequest(BaseModel):
    """GoogleMapsPlacesV1SearchNearbyRequest schema from the OpenAPI specification."""
    excluded_primary_types: List[str] = Field(alias="excludedPrimaryTypes")  # Excluded primary Place type (e.g. \"restaurant\" or \"gas_station\") from https://developers.google.com/maps/documentation/places/web-service/place-types. Up to 50 types from [Table A](https://developers.google.com/maps/documentation/places/web-service/place-types#table-a) may be specified. If there are any conflicting primary types, i.e. a type appears in both included_primary_types and excluded_primary_types, an INVALID_ARGUMENT error is returned. If a Place type is specified with multiple type restrictions, only places that satisfy all of the restrictions are returned. For example, if we have {included_types = [\"restaurant\"], excluded_primary_types = [\"restaurant\"]}, the returned places provide \"restaurant\" related services but do not operate primarily as \"restaurants\".
    excluded_types: List[str] = Field(alias="excludedTypes")  # Excluded Place type (eg, \"restaurant\" or \"gas_station\") from https://developers.google.com/maps/documentation/places/web-service/place-types. Up to 50 types from [Table A](https://developers.google.com/maps/documentation/places/web-service/place-types#table-a) may be specified. If the client provides both included_types (e.g. restaurant) and excluded_types (e.g. cafe), then the response should include places that are restaurant but not cafe. The response includes places that match at least one of the included_types and none of the excluded_types. If there are any conflicting types, i.e. a type appears in both included_types and excluded_types, an INVALID_ARGUMENT error is returned. If a Place type is specified with multiple type restrictions, only places that satisfy all of the restrictions are returned. For example, if we have {included_types = [\"restaurant\"], excluded_primary_types = [\"restaurant\"]}, the returned places provide \"restaurant\" related services but do not operate primarily as \"restaurants\".
    included_primary_types: List[str] = Field(alias="includedPrimaryTypes")  # Included primary Place type (e.g. \"restaurant\" or \"gas_station\") from https://developers.google.com/maps/documentation/places/web-service/place-types. A place can only have a single primary type from the supported types table associated with it. Up to 50 types from [Table A](https://developers.google.com/maps/documentation/places/web-service/place-types#table-a) may be specified. If there are any conflicting primary types, i.e. a type appears in both included_primary_types and excluded_primary_types, an INVALID_ARGUMENT error is returned. If a Place type is specified with multiple type restrictions, only places that satisfy all of the restrictions are returned. For example, if we have {included_types = [\"restaurant\"], excluded_primary_types = [\"restaurant\"]}, the returned places provide \"restaurant\" related services but do not operate primarily as \"restaurants\".
    included_types: List[str] = Field(alias="includedTypes")  # Included Place type (eg, \"restaurant\" or \"gas_station\") from https://developers.google.com/maps/documentation/places/web-service/place-types. Up to 50 types from [Table A](https://developers.google.com/maps/documentation/places/web-service/place-types#table-a) may be specified. If there are any conflicting types, i.e. a type appears in both included_types and excluded_types, an INVALID_ARGUMENT error is returned. If a Place type is specified with multiple type restrictions, only places that satisfy all of the restrictions are returned. For example, if we have {included_types = [\"restaurant\"], excluded_primary_types = [\"restaurant\"]}, the returned places provide \"restaurant\" related services but do not operate primarily as \"restaurants\".
    language_code: str = Field(alias="languageCode")  # Place details will be displayed with the preferred language if available. If the language code is unspecified or unrecognized, place details of any language may be returned, with a preference for English if such details exist. Current list of supported languages: https://developers.google.com/maps/faq#languagesupport.
    location_restriction: GoogleMapsPlacesV1SearchNearbyRequestLocationRestriction = Field(alias="locationRestriction")  # The region to search.
    max_result_count: int = Field(alias="maxResultCount")  # Maximum number of results to return. It must be between 1 and 20 (default), inclusively. If the number is unset, it falls back to the upper limit. If the number is set to negative or exceeds the upper limit, an INVALID_ARGUMENT error is returned.
    rank_preference: str = Field(alias="rankPreference")  # How results will be ranked in the response.
    region_code: str = Field(alias="regionCode")  # The Unicode country/region code (CLDR) of the location where the request is coming from. This parameter is used to display the place details, like region-specific place name, if available. The parameter can affect results based on applicable law. For more information, see https://www.unicode.org/cldr/charts/latest/supplemental/territory_language_information.html. Note that 3-digit region codes are not currently supported.
    
    class Config:
        populate_by_name = True


class GoogleMapsPlacesV1SearchNearbyRequestLocationRestriction(BaseModel):
    """GoogleMapsPlacesV1SearchNearbyRequestLocationRestriction schema from the OpenAPI specification."""
    circle: GoogleMapsPlacesV1Circle = Field(alias="circle")  # Circle with a LatLng as center and radius.
    
    class Config:
        populate_by_name = True


class GoogleMapsPlacesV1SearchNearbyResponse(BaseModel):
    """GoogleMapsPlacesV1SearchNearbyResponse schema from the OpenAPI specification."""
    places: List[GoogleMapsPlacesV1Place] = Field(alias="places")  # A list of places that meets user\'s requirements like places types, number of places and specific location restriction.
    
    class Config:
        populate_by_name = True


class GoogleMapsPlacesV1SearchTextRequest(BaseModel):
    """GoogleMapsPlacesV1SearchTextRequest schema from the OpenAPI specification."""
    included_type: str = Field(alias="includedType")  # The requested place type. Full list of types supported: https://developers.google.com/maps/documentation/places/web-service/place-types. Only support one included type.
    language_code: str = Field(alias="languageCode")  # Place details will be displayed with the preferred language if available. If the language code is unspecified or unrecognized, place details of any language may be returned, with a preference for English if such details exist. Current list of supported languages: https://developers.google.com/maps/faq#languagesupport.
    location_bias: Any = Field(alias="locationBias")  # The region to search. This location serves as a bias which means results around given location might be returned.
    location_restriction: GoogleMapsPlacesV1SearchTextRequestLocationRestriction = Field(alias="locationRestriction")  # The region to search. This location serves as a restriction which means results outside given location will not be returned.
    max_result_count: int = Field(alias="maxResultCount")  # Maximum number of results to return. It must be between 1 and 20, inclusively. The default is 20. If the number is unset, it falls back to the upper limit. If the number is set to negative or exceeds the upper limit, an INVALID_ARGUMENT error is returned.
    min_rating: float = Field(alias="minRating")  # Filter out results whose average user rating is strictly less than this limit. A valid value must be a float between 0 and 5 (inclusively) at a 0.5 cadence i.e. [0, 0.5, 1.0, ... , 5.0] inclusively. The input rating will round up to the nearest 0.5(ceiling). For instance, a rating of 0.6 will eliminate all results with a less than 1.0 rating.
    open_now: bool = Field(alias="openNow")  # Used to restrict the search to places that are currently open. The default is false.
    price_levels: List[str] = Field(alias="priceLevels")  # Used to restrict the search to places that are marked as certain price levels. Users can choose any combinations of price levels. Default to select all price levels.
    rank_preference: str = Field(alias="rankPreference")  # How results will be ranked in the response.
    region_code: str = Field(alias="regionCode")  # The Unicode country/region code (CLDR) of the location where the request is coming from. This parameter is used to display the place details, like region-specific place name, if available. The parameter can affect results based on applicable law. For more information, see https://www.unicode.org/cldr/charts/latest/supplemental/territory_language_information.html. Note that 3-digit region codes are not currently supported.
    strict_type_filtering: bool = Field(alias="strictTypeFiltering")  # Used to set strict type filtering for included_type. If set to true, only results of the same type will be returned. Default to false.
    text_query: str = Field(alias="textQuery")  # Required. The text query for textual search.
    
    class Config:
        populate_by_name = True


class GoogleMapsPlacesV1SearchTextRequestLocationRestriction(BaseModel):
    """GoogleMapsPlacesV1SearchTextRequestLocationRestriction schema from the OpenAPI specification."""
    rectangle: GoogleGeoTypeViewport = Field(alias="rectangle")  # A latitude-longitude viewport, represented as two diagonally opposite `low` and `high` points. A viewport is considered a closed region, i.e. it includes its boundary. The latitude bounds must range between -90 to 90 degrees inclusive, and the longitude bounds must range between -180 to 180 degrees inclusive. Various cases include: - If `low` = `high`, the viewport consists of that single point. - If `low.longitude` > `high.longitude`, the longitude range is inverted (the viewport crosses the 180 degree longitude line). - If `low.longitude` = -180 degrees and `high.longitude` = 180 degrees, the viewport includes all longitudes. - If `low.longitude` = 180 degrees and `high.longitude` = -180 degrees, the longitude range is empty. - If `low.latitude` > `high.latitude`, the latitude range is empty. Both `low` and `high` must be populated, and the represented box cannot be empty (as specified by the definitions above). An empty viewport will result in an error. For example, this viewport fully encloses New York City: { \"low\": { \"latitude\": 40.477398, \"longitude\": -74.259087 }, \"high\": { \"latitude\": 40.91618, \"longitude\": -73.70018 } }
    
    class Config:
        populate_by_name = True


class GoogleMapsPlacesV1SearchTextResponse(BaseModel):
    """GoogleMapsPlacesV1SearchTextResponse schema from the OpenAPI specification."""
    places: List[GoogleMapsPlacesV1Place] = Field(alias="places")  # A list of places that meet the user\'s text search criteria.
    
    class Config:
        populate_by_name = True


class GoogleTypeDate(BaseModel):
    """GoogleTypeDate schema from the OpenAPI specification."""
    day: int = Field(alias="day")  # Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn\'t significant.
    month: int = Field(alias="month")  # Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day.
    year: int = Field(alias="year")  # Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year.
    
    class Config:
        populate_by_name = True


class GoogleTypeLatLng(BaseModel):
    """GoogleTypeLatLng schema from the OpenAPI specification."""
    latitude: float = Field(alias="latitude")  # The latitude in degrees. It must be in the range [-90.0, +90.0].
    longitude: float = Field(alias="longitude")  # The longitude in degrees. It must be in the range [-180.0, +180.0].
    
    class Config:
        populate_by_name = True


class GoogleTypeLocalizedText(BaseModel):
    """GoogleTypeLocalizedText schema from the OpenAPI specification."""
    language_code: str = Field(alias="languageCode")  # The text\'s BCP-47 language code, such as \"en-US\" or \"sr-Latn\". For more information, see http://www.unicode.org/reports/tr35/#Unicode_locale_identifier.
    text: str = Field(alias="text")  # Localized string in the language corresponding to language_code below.
    
    class Config:
        populate_by_name = True


class GoogleTypeMoney(BaseModel):
    """GoogleTypeMoney schema from the OpenAPI specification."""
    currency_code: str = Field(alias="currencyCode")  # The three-letter currency code defined in ISO 4217.
    nanos: int = Field(alias="nanos")  # Number of nano (10^-9) units of the amount. The value must be between -999,999,999 and +999,999,999 inclusive. If `units` is positive, `nanos` must be positive or zero. If `units` is zero, `nanos` can be positive, zero, or negative. If `units` is negative, `nanos` must be negative or zero. For example $-1.75 is represented as `units`=-1 and `nanos`=-750,000,000.
    units: str = Field(alias="units")  # The whole units of the amount. For example if `currencyCode` is `\"USD\"`, then 1 unit is one US dollar.
    
    class Config:
        populate_by_name = True