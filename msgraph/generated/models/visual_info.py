from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .image_info import ImageInfo
    from .json import Json

@dataclass
class VisualInfo(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    BackingStore: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Optional. JSON object used to represent an icon which represents the application used to generate the activity
    attribution: Optional[ImageInfo] = None
    # Optional. Background color used to render the activity in the UI - brand color for the application source of the activity. Must be a valid hex color
    background_color: Optional[str] = None
    # Optional. Custom piece of data - JSON object used to provide custom content to render the activity in the Windows Shell UI
    content: Optional[Json] = None
    # Optional. Longer text description of the user's unique activity (example: document name, first sentence, and/or metadata)
    description: Optional[str] = None
    # Required. Short text description of the user's unique activity (for example, document name in cases where an activity refers to document creation)
    display_text: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VisualInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VisualInfo
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return VisualInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .image_info import ImageInfo
        from .json import Json

        from .image_info import ImageInfo
        from .json import Json

        fields: Dict[str, Callable[[Any], None]] = {
            "attribution": lambda n : setattr(self, 'attribution', n.get_object_value(ImageInfo)),
            "backgroundColor": lambda n : setattr(self, 'background_color', n.get_str_value()),
            "content": lambda n : setattr(self, 'content', n.get_object_value(Json)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayText": lambda n : setattr(self, 'display_text', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("attribution", self.attribution)
        writer.write_str_value("backgroundColor", self.background_color)
        writer.write_object_value("content", self.content)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayText", self.display_text)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

