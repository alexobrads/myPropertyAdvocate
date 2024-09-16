from dataclasses import dataclass, field
from typing import List, Dict, Optional


@dataclass
class AddressParts:
    displayAddress: Optional[str] = None
    displayType: Optional[str] = None
    stateAbbreviation: Optional[str] = None
    postcode: Optional[str] = None
    suburb: Optional[str] = None
    streetNumber: Optional[str] = None
    street: Optional[str] = None


@dataclass
class AdvertiserIdentifiers:
    advertiserType: Optional[str] = None
    advertiserId: Optional[int] = None
    contactIds: List[int] = field(default_factory=list)
    agentIds: List[str] = field(default_factory=list)


@dataclass
class GeoLocation:
    lat: Optional[float] = None
    lon: Optional[float] = None


@dataclass
class InspectionDetails:
    inspections: List[str] = field(default_factory=list)
    pastInspections: List[str] = field(default_factory=list)
    isByAppointmentOnly: Optional[bool] = None


@dataclass
class Media:
    category: Optional[str] = None
    type: Optional[str] = None
    url: Optional[str] = None


@dataclass
class PriceDetails:
    displayPrice: Optional[str] = None
    canDisplayPrice: Optional[bool] = None


@dataclass
class SoldDetails:
    canDisplayPrice: Optional[bool] = None
    soldAction: Optional[str] = None
    soldDate: Optional[str] = None
    soldPrice: Optional[int] = None
    source: Optional[str] = None


@dataclass
class SaleDetails:
    soldDetails: Optional[SoldDetails] = None
    tenderDetails: Dict = field(default_factory=dict)
    tenantDetails: Dict = field(default_factory=dict)
    saleMethod: Optional[str] = None


@dataclass
class StatementOfInformation:
    estimatedPrice: Dict = field(default_factory=dict)
    suburbMedianPrice: Dict = field(default_factory=dict)
    documentationUrl: Optional[str] = None


@dataclass
class Property:
    addressParts: Optional[AddressParts] = None
    advertiserIdentifiers: Optional[AdvertiserIdentifiers] = None
    inspectionDetails: Optional[InspectionDetails] = None
    saleDetails: Optional[SaleDetails] = None
    priceDetails: Optional[PriceDetails] = None
    media: List[Media] = field(default_factory=list)
    geoLocation: Optional[GeoLocation] = None
    statementOfInformation: Optional[StatementOfInformation] = None
    buildingAreaSqm: Optional[float] = None
    bathrooms: Optional[int] = None
    bedrooms: Optional[int] = None
    carspaces: Optional[int] = None
    channel: Optional[str] = None
    dateListed: Optional[str] = None
    dateUpdated: Optional[str] = None
    description: Optional[str] = None
    headline: Optional[str] = None
    id: Optional[int] = None
    isNewDevelopment: Optional[bool] = None
    objective: Optional[str] = None
    propertyTypes: List[str] = field(default_factory=list)
    status: Optional[str] = None
    apmIdentifiers: Dict = field(default_factory=dict)
    propertyId: Optional[str] = None
    features: List[str] = field(default_factory=list)
    saleMode: Optional[str] = None
    seoUrl: Optional[str] = None
    energyEfficiencyRating: Optional[int] = None
    virtualTourUrl: Optional[str] = None
    landAreaSqm: Optional[int] = None
    numberOfDwellings: Optional[int] = None
