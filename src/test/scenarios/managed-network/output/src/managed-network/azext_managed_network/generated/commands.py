# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from azure.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from azext_managed_network.generated._client_factory import cf_mn
    managed_network_mn = CliCommandType(
        operations_tmpl='azext_managed_network.vendored_sdks.managednetwork.operations._managed_network_operations#Mana'
        'gedNetworkOperations.{}',
        client_factory=cf_mn)
    with self.command_group('managed-network mn', managed_network_mn, client_factory=cf_mn,
                            is_experimental=True) as g:
        g.custom_command('list', 'managed_network_mn_list')
        g.custom_show_command('show', 'managed_network_mn_show')
        g.custom_command('create', 'managed_network_mn_create')
        g.custom_command('update', 'managed_network_mn_update', supports_no_wait=True)
        g.custom_command('delete', 'managed_network_mn_delete', supports_no_wait=True)
        g.wait_command('wait')

    from azext_managed_network.generated._client_factory import cf_scope_assignment
    managed_network_scope_assignment = CliCommandType(
        operations_tmpl='azext_managed_network.vendored_sdks.managednetwork.operations._scope_assignment_operations#Sco'
        'peAssignmentOperations.{}',
        client_factory=cf_scope_assignment)
    with self.command_group('managed-network scope-assignment', managed_network_scope_assignment,
                            client_factory=cf_scope_assignment, is_experimental=True) as g:
        g.custom_command('list', 'managed_network_scope_assignment_list')
        g.custom_show_command('show', 'managed_network_scope_assignment_show')
        g.custom_command('create', 'managed_network_scope_assignment_create')
        g.custom_command('update', 'managed_network_scope_assignment_update')
        g.custom_command('delete', 'managed_network_scope_assignment_delete')

    from azext_managed_network.generated._client_factory import cf_managed_network_group
    managed_network_managed_network_group = CliCommandType(
        operations_tmpl='azext_managed_network.vendored_sdks.managednetwork.operations._managed_network_group_operation'
        's#ManagedNetworkGroupOperations.{}',
        client_factory=cf_managed_network_group)
    with self.command_group('managed-network mn group', managed_network_managed_network_group,
                            client_factory=cf_managed_network_group) as g:
        g.custom_command('list', 'managed_network_mn_group_list')
        g.custom_show_command('show', 'managed_network_mn_group_show')
        g.custom_command('create', 'managed_network_mn_group_create', supports_no_wait=True)
        g.custom_command('update', 'managed_network_mn_group_update', supports_no_wait=True)
        g.custom_command('delete', 'managed_network_mn_group_delete', supports_no_wait=True)
        g.wait_command('wait')

    from azext_managed_network.generated._client_factory import cf_managed_network_peering_policy
    managed_network_managed_network_peering_policy = CliCommandType(
        operations_tmpl='azext_managed_network.vendored_sdks.managednetwork.operations._managed_network_peering_policy_'
        'operations#ManagedNetworkPeeringPolicyOperations.{}',
        client_factory=cf_managed_network_peering_policy)
    with self.command_group('managed-network managed-network-peering-policy',
                            managed_network_managed_network_peering_policy,
                            client_factory=cf_managed_network_peering_policy, is_experimental=True) as g:
        g.custom_command('list', 'managed_network_managed_network_peering_policy_list')
        g.custom_show_command('show', 'managed_network_managed_network_peering_policy_show')
        g.custom_command('hub-and-spoke-topology create', 'managed_network_managed_network_peering_policy_hub_and_spoke'
                         '_topology_create', supports_no_wait=True)
        g.generic_update_command('hub-and-spoke-topology update', setter_arg_name = 'properties', setter_name = 'begin_'
                                 'create_or_update', custom_func_name = 'managed_network_managed_network_peering_policy'
                                 '_hub_and_spoke_topology_update', supports_no_wait=True)
        g.custom_command('mesh-topology create', 'managed_network_managed_network_peering_policy_mesh_topology_create',
                          supports_no_wait=True)
        g.generic_update_command('mesh-topology update', setter_arg_name = 'properties', setter_name = 'begin_create_or'
                                 '_update', custom_func_name = 'managed_network_managed_network_peering_policy_mesh_top'
                                 'ology_update', supports_no_wait=True)
        g.custom_command('delete', 'managed_network_managed_network_peering_policy_delete', supports_no_wait=True)
        g.wait_command('wait')
