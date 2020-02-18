# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=too-many-lines
# pylint: disable=line-too-long
from knack.help_files import helps  # pylint: disable=unused-import


helps['managed-network managed_networks'] = """
    type: group
    short-summary: managed-network managed_networks
"""

helps['managed-network managed_networks list'] = """
    type: command
    short-summary: The ListByResourceGroup ManagedNetwork operation retrieves all the Managed Network resources in a resource group in a paginated format.
"""

helps['managed-network managed_networks show'] = """
    type: command
    short-summary: The Get ManagedNetworks operation gets a Managed Network Resource, specified by the resource group and Managed Network name
"""

helps['managed-network managed_networks create'] = """
    type: command
    short-summary: The Put ManagedNetworks operation creates/updates a Managed Network Resource, specified by resource group and Managed Network name
"""

helps['managed-network managed_networks update'] = """
    type: command
    short-summary: Updates the specified Managed Network resource tags.
"""

helps['managed-network managed_networks delete'] = """
    type: command
    short-summary: The Delete ManagedNetworks operation deletes a Managed Network Resource, specified by the  resource group and Managed Network name
"""

helps['managed-network scope_assignments'] = """
    type: group
    short-summary: managed-network scope_assignments
"""

helps['managed-network scope_assignments list'] = """
    type: command
    short-summary: Get the specified scope assignment.
"""

helps['managed-network scope_assignments show'] = """
    type: command
    short-summary: Get the specified scope assignment.
"""

helps['managed-network scope_assignments create'] = """
    type: command
    short-summary: Creates a scope assignment.
"""

helps['managed-network scope_assignments update'] = """
    type: command
    short-summary: Creates a scope assignment.
"""

helps['managed-network scope_assignments delete'] = """
    type: command
    short-summary: Deletes a scope assignment.
"""

helps['managed-network managed_network_groups'] = """
    type: group
    short-summary: managed-network managed_network_groups
"""

helps['managed-network managed_network_groups list'] = """
    type: command
    short-summary: The ListByManagedNetwork ManagedNetworkGroup operation retrieves all the Managed Network Groups in a specified Managed Networks in a paginated format.
"""

helps['managed-network managed_network_groups show'] = """
    type: command
    short-summary: The Get ManagedNetworkGroups operation gets a Managed Network Group specified by the resource group, Managed Network name, and group name
"""

helps['managed-network managed_network_groups create'] = """
    type: command
    short-summary: The Put ManagedNetworkGroups operation creates or updates a Managed Network Group resource
"""

helps['managed-network managed_network_groups update'] = """
    type: command
    short-summary: The Put ManagedNetworkGroups operation creates or updates a Managed Network Group resource
"""

helps['managed-network managed_network_groups delete'] = """
    type: command
    short-summary: The Delete ManagedNetworkGroups operation deletes a Managed Network Group specified by the resource group, Managed Network name, and group name
"""

helps['managed-network managed_network_peering_policies'] = """
    type: group
    short-summary: managed-network managed_network_peering_policies
"""

helps['managed-network managed_network_peering_policies list'] = """
    type: command
    short-summary: The ListByManagedNetwork PeeringPolicies operation retrieves all the Managed Network Peering Policies in a specified Managed Network, in a paginated format.
"""

helps['managed-network managed_network_peering_policies show'] = """
    type: command
    short-summary: The Get ManagedNetworkPeeringPolicies operation gets a Managed Network Peering Policy resource, specified by the  resource group, Managed Network name, and peering policy name
"""

helps['managed-network managed_network_peering_policies create'] = """
    type: command
    short-summary: The Put ManagedNetworkPeeringPolicies operation creates/updates a new Managed Network Peering Policy
"""

helps['managed-network managed_network_peering_policies update'] = """
    type: command
    short-summary: The Put ManagedNetworkPeeringPolicies operation creates/updates a new Managed Network Peering Policy
"""

helps['managed-network managed_network_peering_policies delete'] = """
    type: command
    short-summary: The Delete ManagedNetworkPeeringPolicies operation deletes a Managed Network Peering Policy, specified by the  resource group, Managed Network name, and peering policy name
"""

helps['managed-network operations'] = """
    type: group
    short-summary: managed-network operations
"""

helps['managed-network operations list'] = """
    type: command
    short-summary: Lists all of the available MNC operations.
"""
