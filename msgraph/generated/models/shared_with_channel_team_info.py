from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .conversation_member import ConversationMember
    from .team_info import TeamInfo

from .team_info import TeamInfo

@dataclass
class SharedWithChannelTeamInfo(TeamInfo):
    # A collection of team members who have access to the shared channel.
    allowed_members: Optional[List[ConversationMember]] = None
    # Indicates whether the team is the host of the channel.
    is_host_team: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SharedWithChannelTeamInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SharedWithChannelTeamInfo
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SharedWithChannelTeamInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .conversation_member import ConversationMember
        from .team_info import TeamInfo

        from .conversation_member import ConversationMember
        from .team_info import TeamInfo

        fields: Dict[str, Callable[[Any], None]] = {
            "allowed_members": lambda n : setattr(self, 'allowed_members', n.get_collection_of_object_values(ConversationMember)),
            "is_host_team": lambda n : setattr(self, 'is_host_team', n.get_bool_value()),
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
        writer.write_collection_of_object_values("allowed_members", self.allowed_members)
        writer.write_bool_value("is_host_team", self.is_host_team)
    

