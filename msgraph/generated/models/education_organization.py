from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .education_external_source import EducationExternalSource
    from .education_school import EducationSchool
    from .entity import Entity

from .entity import Entity

@dataclass
class EducationOrganization(Entity):
    # Organization description.
    description: Optional[str] = None
    # Organization display name.
    display_name: Optional[str] = None
    # Source where this organization was created from. Possible values are: sis, manual.
    external_source: Optional[EducationExternalSource] = None
    # The name of the external source this resource was generated from.
    external_source_detail: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationOrganization:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EducationOrganization
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationSchool".casefold():
            from .education_school import EducationSchool

            return EducationSchool()
        return EducationOrganization()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .education_external_source import EducationExternalSource
        from .education_school import EducationSchool
        from .entity import Entity

        from .education_external_source import EducationExternalSource
        from .education_school import EducationSchool
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "external_source": lambda n : setattr(self, 'external_source', n.get_enum_value(EducationExternalSource)),
            "external_source_detail": lambda n : setattr(self, 'external_source_detail', n.get_str_value()),
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
        writer.write_str_value("description", self.description)
        writer.write_str_value("display_name", self.display_name)
        writer.write_enum_value("external_source", self.external_source)
        writer.write_str_value("external_source_detail", self.external_source_detail)
    

