from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .group_assignment_target import GroupAssignmentTarget

from .group_assignment_target import GroupAssignmentTarget

@dataclass
class ExclusionGroupAssignmentTarget(GroupAssignmentTarget):
    """
    Represents a group that should be excluded from an assignment.
    """
    # The OdataType property
    OdataType: Optional[str] = "#microsoft.graph.exclusionGroupAssignmentTarget"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ExclusionGroupAssignmentTarget:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExclusionGroupAssignmentTarget
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ExclusionGroupAssignmentTarget()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .group_assignment_target import GroupAssignmentTarget

        from .group_assignment_target import GroupAssignmentTarget

        fields: Dict[str, Callable[[Any], None]] = {
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
    

