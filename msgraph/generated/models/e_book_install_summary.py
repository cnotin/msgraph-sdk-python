from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class EBookInstallSummary(Entity):
    # Number of Devices that have failed to install this book.
    failed_device_count: Optional[int] = None
    # Number of Users that have 1 or more device that failed to install this book.
    failed_user_count: Optional[int] = None
    # Number of Devices that have successfully installed this book.
    installed_device_count: Optional[int] = None
    # Number of Users whose devices have all succeeded to install this book.
    installed_user_count: Optional[int] = None
    # Number of Devices that does not have this book installed.
    not_installed_device_count: Optional[int] = None
    # Number of Users that did not install this book.
    not_installed_user_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EBookInstallSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EBookInstallSummary
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EBookInstallSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "failedDeviceCount": lambda n : setattr(self, 'failed_device_count', n.get_int_value()),
            "failedUserCount": lambda n : setattr(self, 'failed_user_count', n.get_int_value()),
            "installedDeviceCount": lambda n : setattr(self, 'installed_device_count', n.get_int_value()),
            "installedUserCount": lambda n : setattr(self, 'installed_user_count', n.get_int_value()),
            "notInstalledDeviceCount": lambda n : setattr(self, 'not_installed_device_count', n.get_int_value()),
            "notInstalledUserCount": lambda n : setattr(self, 'not_installed_user_count', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_int_value("failedDeviceCount", self.failed_device_count)
        writer.write_int_value("failedUserCount", self.failed_user_count)
        writer.write_int_value("installedDeviceCount", self.installed_device_count)
        writer.write_int_value("installedUserCount", self.installed_user_count)
        writer.write_int_value("notInstalledDeviceCount", self.not_installed_device_count)
        writer.write_int_value("notInstalledUserCount", self.not_installed_user_count)
    

