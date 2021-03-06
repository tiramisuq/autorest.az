# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines


def attestation_attestation_provider_list(cmd, client,
                                          resource_group_name=None):
    if resource_group_name is not None:
        return client.list_by_resource_group(resource_group_name=resource_group_name)
    return client.list()


def attestation_attestation_provider_show(cmd, client,
                                          resource_group_name,
                                          provider_name):
    return client.get(resource_group_name=resource_group_name,
                      provider_name=provider_name)


def attestation_attestation_provider_create(cmd, client,
                                            resource_group_name,
                                            provider_name,
                                            location,
                                            tags=None,
                                            attestation_policy=None,
                                            policy_signing_certificates_keys=None):
    return client.create(resource_group_name=resource_group_name,
                         provider_name=provider_name,
                         location=location,
                         tags=tags,
                         attestation_policy=attestation_policy,
                         keys=policy_signing_certificates_keys)


def attestation_attestation_provider_update(cmd, client,
                                            resource_group_name,
                                            provider_name,
                                            tags=None):
    return client.update(resource_group_name=resource_group_name,
                         provider_name=provider_name,
                         tags=tags)


def attestation_attestation_provider_delete(cmd, client,
                                            resource_group_name,
                                            provider_name):
    return client.delete(resource_group_name=resource_group_name,
                         provider_name=provider_name)
