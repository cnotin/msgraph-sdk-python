from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package_resource_environment import AccessPackageResourceEnvironment
    from .access_package_resource_role import AccessPackageResourceRole
    from .access_package_resource_scope import AccessPackageResourceScope
    from .entity import Entity

from .entity import Entity

@dataclass
class AccessPackageResource(Entity):
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # A description for the resource.
    description: Optional[str] = None
    # The display name of the resource, such as the application name, group name or site name.
    display_name: Optional[str] = None
    # Contains the environment information for the resource. This can be set using either the @odata.bind annotation or the environment's originId.Supports $expand.
    environment: Optional[AccessPackageResourceEnvironment] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The unique identifier of the resource in the origin system. In the case of a Microsoft Entra group, this is the identifier of the group.
    origin_id: Optional[str] = None
    # The type of the resource in the origin system, such as SharePointOnline, AadApplication or AadGroup.
    origin_system: Optional[str] = None
    # Read-only. Nullable. Supports $expand.
    roles: Optional[List[AccessPackageResourceRole]] = None
    # Read-only. Nullable. Supports $expand.
    scopes: Optional[List[AccessPackageResourceScope]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageResource
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AccessPackageResource()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .access_package_resource_environment import AccessPackageResourceEnvironment
        from .access_package_resource_role import AccessPackageResourceRole
        from .access_package_resource_scope import AccessPackageResourceScope
        from .entity import Entity

        from .access_package_resource_environment import AccessPackageResourceEnvironment
        from .access_package_resource_role import AccessPackageResourceRole
        from .access_package_resource_scope import AccessPackageResourceScope
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "environment": lambda n : setattr(self, 'environment', n.get_object_value(AccessPackageResourceEnvironment)),
            "modified_date_time": lambda n : setattr(self, 'modified_date_time', n.get_datetime_value()),
            "origin_id": lambda n : setattr(self, 'origin_id', n.get_str_value()),
            "origin_system": lambda n : setattr(self, 'origin_system', n.get_str_value()),
            "roles": lambda n : setattr(self, 'roles', n.get_collection_of_object_values(AccessPackageResourceRole)),
            "scopes": lambda n : setattr(self, 'scopes', n.get_collection_of_object_values(AccessPackageResourceScope)),
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
        writer.write_datetime_value("created_date_time", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("display_name", self.display_name)
        writer.write_object_value("environment", self.environment)
        writer.write_datetime_value("modified_date_time", self.modified_date_time)
        writer.write_str_value("origin_id", self.origin_id)
        writer.write_str_value("origin_system", self.origin_system)
        writer.write_collection_of_object_values("roles", self.roles)
        writer.write_collection_of_object_values("scopes", self.scopes)
    

