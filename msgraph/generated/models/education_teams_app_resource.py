from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .education_resource import EducationResource

from .education_resource import EducationResource

@dataclass
class EducationTeamsAppResource(EducationResource):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.educationTeamsAppResource"
    # URL that points to the icon of the app.
    app_icon_web_url: Optional[str] = None
    # Teams app ID of the application.
    app_id: Optional[str] = None
    # URL for the app resource that will be opened by Teams.
    teams_embedded_content_url: Optional[str] = None
    # URL for the app resource that can be opened in the browser.
    web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationTeamsAppResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EducationTeamsAppResource
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EducationTeamsAppResource()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .education_resource import EducationResource

        from .education_resource import EducationResource

        fields: Dict[str, Callable[[Any], None]] = {
            "app_icon_web_url": lambda n : setattr(self, 'app_icon_web_url', n.get_str_value()),
            "app_id": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "teams_embedded_content_url": lambda n : setattr(self, 'teams_embedded_content_url', n.get_str_value()),
            "web_url": lambda n : setattr(self, 'web_url', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("app_icon_web_url", self.app_icon_web_url)
        writer.write_str_value("app_id", self.app_id)
        writer.write_str_value("teams_embedded_content_url", self.teams_embedded_content_url)
        writer.write_str_value("web_url", self.web_url)
    

