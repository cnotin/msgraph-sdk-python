from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert_detection import AlertDetection
    from .alert_feedback import AlertFeedback
    from .alert_history_state import AlertHistoryState
    from .alert_severity import AlertSeverity
    from .alert_status import AlertStatus
    from .alert_trigger import AlertTrigger
    from .cloud_app_security_state import CloudAppSecurityState
    from .entity import Entity
    from .file_security_state import FileSecurityState
    from .host_security_state import HostSecurityState
    from .investigation_security_state import InvestigationSecurityState
    from .malware_state import MalwareState
    from .message_security_state import MessageSecurityState
    from .network_connection import NetworkConnection
    from .process import Process
    from .registry_key_state import RegistryKeyState
    from .security_resource import SecurityResource
    from .security_vendor_information import SecurityVendorInformation
    from .uri_click_security_state import UriClickSecurityState
    from .user_security_state import UserSecurityState
    from .vulnerability_state import VulnerabilityState

from .entity import Entity

@dataclass
class Alert(Entity):
    # Name or alias of the activity group (attacker) this alert is attributed to.
    activity_group_name: Optional[str] = None
    # The alertDetections property
    alert_detections: Optional[List[AlertDetection]] = None
    # Name of the analyst the alert is assigned to for triage, investigation, or remediation (supports update).
    assigned_to: Optional[str] = None
    # Azure subscription ID, present if this alert is related to an Azure resource.
    azure_subscription_id: Optional[str] = None
    # Microsoft Entra tenant ID. Required.
    azure_tenant_id: Optional[str] = None
    # Category of the alert (for example, credentialTheft, ransomware, etc.).
    category: Optional[str] = None
    # Time at which the alert was closed. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z (supports update).
    closed_date_time: Optional[datetime.datetime] = None
    # Security-related stateful information generated by the provider about the cloud application/s related to this alert.
    cloud_app_states: Optional[List[CloudAppSecurityState]] = None
    # Customer-provided comments on alert (for customer alert management) (supports update).
    comments: Optional[List[str]] = None
    # Confidence of the detection logic (percentage between 1-100).
    confidence: Optional[int] = None
    # Time at which the alert was created by the alert provider. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Required.
    created_date_time: Optional[datetime.datetime] = None
    # Alert description.
    description: Optional[str] = None
    # Set of alerts related to this alert entity (each alert is pushed to the SIEM as a separate record).
    detection_ids: Optional[List[str]] = None
    # Time at which the event(s) that served as the trigger(s) to generate the alert occurred. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Required.
    event_date_time: Optional[datetime.datetime] = None
    # Analyst feedback on the alert. Possible values are: unknown, truePositive, falsePositive, benignPositive. (supports update)
    feedback: Optional[AlertFeedback] = None
    # Security-related stateful information generated by the provider about the file(s) related to this alert.
    file_states: Optional[List[FileSecurityState]] = None
    # The historyStates property
    history_states: Optional[List[AlertHistoryState]] = None
    # Security-related stateful information generated by the provider about the host(s) related to this alert.
    host_states: Optional[List[HostSecurityState]] = None
    # IDs of incidents related to current alert.
    incident_ids: Optional[List[str]] = None
    # The investigationSecurityStates property
    investigation_security_states: Optional[List[InvestigationSecurityState]] = None
    # The lastEventDateTime property
    last_event_date_time: Optional[datetime.datetime] = None
    # Time at which the alert entity was last modified. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    last_modified_date_time: Optional[datetime.datetime] = None
    # Threat Intelligence pertaining to malware related to this alert.
    malware_states: Optional[List[MalwareState]] = None
    # The messageSecurityStates property
    message_security_states: Optional[List[MessageSecurityState]] = None
    # Security-related stateful information generated by the provider about the network connection(s) related to this alert.
    network_connections: Optional[List[NetworkConnection]] = None
    # The OdataType property
    OdataType: Optional[str] = None
    # Security-related stateful information generated by the provider about the process or processes related to this alert.
    processes: Optional[List[Process]] = None
    # Vendor/provider recommended action(s) to take as a result of the alert (for example, isolate machine, enforce2FA, reimage host).
    recommended_actions: Optional[List[str]] = None
    # Security-related stateful information generated by the provider about the registry keys related to this alert.
    registry_key_states: Optional[List[RegistryKeyState]] = None
    # Resources related to current alert. For example, for some alerts this can have the Azure Resource value.
    security_resources: Optional[List[SecurityResource]] = None
    # The severity property
    severity: Optional[AlertSeverity] = None
    # Hyperlinks (URIs) to the source material related to the alert, for example, provider's user interface for alerts or log search, etc.
    source_materials: Optional[List[str]] = None
    # The status property
    status: Optional[AlertStatus] = None
    # User-definable labels that can be applied to an alert and can serve as filter conditions (for example 'HVA', 'SAW', etc.) (supports update).
    tags: Optional[List[str]] = None
    # Alert title. Required.
    title: Optional[str] = None
    # Security-related information about the specific properties that triggered the alert (properties appearing in the alert). Alerts might contain information about multiple users, hosts, files, ip addresses. This field indicates which properties triggered the alert generation.
    triggers: Optional[List[AlertTrigger]] = None
    # The uriClickSecurityStates property
    uri_click_security_states: Optional[List[UriClickSecurityState]] = None
    # Security-related stateful information generated by the provider about the user accounts related to this alert.
    user_states: Optional[List[UserSecurityState]] = None
    # Complex type containing details about the security product/service vendor, provider, and subprovider (for example, vendor=Microsoft; provider=Windows Defender ATP; subProvider=AppLocker). Required.
    vendor_information: Optional[SecurityVendorInformation] = None
    # Threat intelligence pertaining to one or more vulnerabilities related to this alert.
    vulnerability_states: Optional[List[VulnerabilityState]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Alert:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Alert
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Alert()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .alert_detection import AlertDetection
        from .alert_feedback import AlertFeedback
        from .alert_history_state import AlertHistoryState
        from .alert_severity import AlertSeverity
        from .alert_status import AlertStatus
        from .alert_trigger import AlertTrigger
        from .cloud_app_security_state import CloudAppSecurityState
        from .entity import Entity
        from .file_security_state import FileSecurityState
        from .host_security_state import HostSecurityState
        from .investigation_security_state import InvestigationSecurityState
        from .malware_state import MalwareState
        from .message_security_state import MessageSecurityState
        from .network_connection import NetworkConnection
        from .process import Process
        from .registry_key_state import RegistryKeyState
        from .security_resource import SecurityResource
        from .security_vendor_information import SecurityVendorInformation
        from .uri_click_security_state import UriClickSecurityState
        from .user_security_state import UserSecurityState
        from .vulnerability_state import VulnerabilityState

        from .alert_detection import AlertDetection
        from .alert_feedback import AlertFeedback
        from .alert_history_state import AlertHistoryState
        from .alert_severity import AlertSeverity
        from .alert_status import AlertStatus
        from .alert_trigger import AlertTrigger
        from .cloud_app_security_state import CloudAppSecurityState
        from .entity import Entity
        from .file_security_state import FileSecurityState
        from .host_security_state import HostSecurityState
        from .investigation_security_state import InvestigationSecurityState
        from .malware_state import MalwareState
        from .message_security_state import MessageSecurityState
        from .network_connection import NetworkConnection
        from .process import Process
        from .registry_key_state import RegistryKeyState
        from .security_resource import SecurityResource
        from .security_vendor_information import SecurityVendorInformation
        from .uri_click_security_state import UriClickSecurityState
        from .user_security_state import UserSecurityState
        from .vulnerability_state import VulnerabilityState

        fields: Dict[str, Callable[[Any], None]] = {
            "activityGroupName": lambda n : setattr(self, 'activity_group_name', n.get_str_value()),
            "alertDetections": lambda n : setattr(self, 'alert_detections', n.get_collection_of_object_values(AlertDetection)),
            "assignedTo": lambda n : setattr(self, 'assigned_to', n.get_str_value()),
            "azureSubscriptionId": lambda n : setattr(self, 'azure_subscription_id', n.get_str_value()),
            "azureTenantId": lambda n : setattr(self, 'azure_tenant_id', n.get_str_value()),
            "category": lambda n : setattr(self, 'category', n.get_str_value()),
            "closedDateTime": lambda n : setattr(self, 'closed_date_time', n.get_datetime_value()),
            "cloudAppStates": lambda n : setattr(self, 'cloud_app_states', n.get_collection_of_object_values(CloudAppSecurityState)),
            "comments": lambda n : setattr(self, 'comments', n.get_collection_of_primitive_values(str)),
            "confidence": lambda n : setattr(self, 'confidence', n.get_int_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "detectionIds": lambda n : setattr(self, 'detection_ids', n.get_collection_of_primitive_values(str)),
            "eventDateTime": lambda n : setattr(self, 'event_date_time', n.get_datetime_value()),
            "feedback": lambda n : setattr(self, 'feedback', n.get_enum_value(AlertFeedback)),
            "fileStates": lambda n : setattr(self, 'file_states', n.get_collection_of_object_values(FileSecurityState)),
            "historyStates": lambda n : setattr(self, 'history_states', n.get_collection_of_object_values(AlertHistoryState)),
            "hostStates": lambda n : setattr(self, 'host_states', n.get_collection_of_object_values(HostSecurityState)),
            "incidentIds": lambda n : setattr(self, 'incident_ids', n.get_collection_of_primitive_values(str)),
            "investigationSecurityStates": lambda n : setattr(self, 'investigation_security_states', n.get_collection_of_object_values(InvestigationSecurityState)),
            "lastEventDateTime": lambda n : setattr(self, 'last_event_date_time', n.get_datetime_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "malwareStates": lambda n : setattr(self, 'malware_states', n.get_collection_of_object_values(MalwareState)),
            "messageSecurityStates": lambda n : setattr(self, 'message_security_states', n.get_collection_of_object_values(MessageSecurityState)),
            "networkConnections": lambda n : setattr(self, 'network_connections', n.get_collection_of_object_values(NetworkConnection)),
            "processes": lambda n : setattr(self, 'processes', n.get_collection_of_object_values(Process)),
            "recommendedActions": lambda n : setattr(self, 'recommended_actions', n.get_collection_of_primitive_values(str)),
            "registryKeyStates": lambda n : setattr(self, 'registry_key_states', n.get_collection_of_object_values(RegistryKeyState)),
            "securityResources": lambda n : setattr(self, 'security_resources', n.get_collection_of_object_values(SecurityResource)),
            "severity": lambda n : setattr(self, 'severity', n.get_enum_value(AlertSeverity)),
            "sourceMaterials": lambda n : setattr(self, 'source_materials', n.get_collection_of_primitive_values(str)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(AlertStatus)),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_primitive_values(str)),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "triggers": lambda n : setattr(self, 'triggers', n.get_collection_of_object_values(AlertTrigger)),
            "uriClickSecurityStates": lambda n : setattr(self, 'uri_click_security_states', n.get_collection_of_object_values(UriClickSecurityState)),
            "userStates": lambda n : setattr(self, 'user_states', n.get_collection_of_object_values(UserSecurityState)),
            "vendorInformation": lambda n : setattr(self, 'vendor_information', n.get_object_value(SecurityVendorInformation)),
            "vulnerabilityStates": lambda n : setattr(self, 'vulnerability_states', n.get_collection_of_object_values(VulnerabilityState)),
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
        writer.write_str_value("activityGroupName", self.activity_group_name)
        writer.write_collection_of_object_values("alertDetections", self.alert_detections)
        writer.write_str_value("assignedTo", self.assigned_to)
        writer.write_str_value("azureSubscriptionId", self.azure_subscription_id)
        writer.write_str_value("azureTenantId", self.azure_tenant_id)
        writer.write_str_value("category", self.category)
        writer.write_datetime_value("closedDateTime", self.closed_date_time)
        writer.write_collection_of_object_values("cloudAppStates", self.cloud_app_states)
        writer.write_collection_of_primitive_values("comments", self.comments)
        writer.write_int_value("confidence", self.confidence)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_collection_of_primitive_values("detectionIds", self.detection_ids)
        writer.write_datetime_value("eventDateTime", self.event_date_time)
        writer.write_enum_value("feedback", self.feedback)
        writer.write_collection_of_object_values("fileStates", self.file_states)
        writer.write_collection_of_object_values("historyStates", self.history_states)
        writer.write_collection_of_object_values("hostStates", self.host_states)
        writer.write_collection_of_primitive_values("incidentIds", self.incident_ids)
        writer.write_collection_of_object_values("investigationSecurityStates", self.investigation_security_states)
        writer.write_datetime_value("lastEventDateTime", self.last_event_date_time)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_object_values("malwareStates", self.malware_states)
        writer.write_collection_of_object_values("messageSecurityStates", self.message_security_states)
        writer.write_collection_of_object_values("networkConnections", self.network_connections)
        writer.write_collection_of_object_values("processes", self.processes)
        writer.write_collection_of_primitive_values("recommendedActions", self.recommended_actions)
        writer.write_collection_of_object_values("registryKeyStates", self.registry_key_states)
        writer.write_collection_of_object_values("securityResources", self.security_resources)
        writer.write_enum_value("severity", self.severity)
        writer.write_collection_of_primitive_values("sourceMaterials", self.source_materials)
        writer.write_enum_value("status", self.status)
        writer.write_collection_of_primitive_values("tags", self.tags)
        writer.write_str_value("title", self.title)
        writer.write_collection_of_object_values("triggers", self.triggers)
        writer.write_collection_of_object_values("uriClickSecurityStates", self.uri_click_security_states)
        writer.write_collection_of_object_values("userStates", self.user_states)
        writer.write_object_value("vendorInformation", self.vendor_information)
        writer.write_collection_of_object_values("vulnerabilityStates", self.vulnerability_states)
    

