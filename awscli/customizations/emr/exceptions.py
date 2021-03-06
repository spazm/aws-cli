# Copyright 2014 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

from awscli.customizations.emr import constants


class EmrError(Exception):
    """
    The base exception class for Emr exceptions.

    :ivar msg: The descriptive message associated with the error.
    """
    fmt = 'An unspecified error occured'

    def __init__(self, **kwargs):
        msg = self.fmt.format(**kwargs)
        Exception.__init__(self, msg)
        self.kwargs = kwargs


class MissingParametersError(EmrError):
    """
    One or more required parameters were not supplied.

    :ivar object: The object that has missing parameters.
        This can be an operation or a parameter (in the
        case of inner params).  The str() of this object
        will be used so it doesn't need to implement anything
        other than str().
    :ivar missing: The names of the missing parameters.
    """
    fmt = ('aws: error: The following required parameters are missing for '
           '{object_name}: {missing}.')


class MissingRequiredInstanceGroupsError(EmrError):
    """
    In create-cluster command, none of --instance-group,
    --instance-count nor --instance-type were not supplied.
    """
    fmt = ('aws: error: Must specify either --instance-groups or '
           '--instance-type with --instance-count(optional) to '
           'configure instance groups.')


class InstanceGroupsValidationError(EmrError):
    """
    --instance-type and --instance-count are shortcut option
    for --instance-groups and they cannot be specified
    together with --instance-groups
    """
    fmt = ('aws: error: You may not specify --instance-type '
           'or --instance-count with --instance-groups, '
           'because --instance-type and --instance-count are '
           'shortcut options for --instance-groups.')


class InvalidAmiVersionError(EmrError):
    """
    The supplied ami-version is invalid.
    :ivar ami_version: The provided ami_version.
    """
    fmt = ('aws: error: The supplied AMI version "{ami_version}" is invalid.'
           ' Please see AMI Versions Supported in Amazon EMR in '
           'Amazon Elastic MapReduce Developer Guide: '
           'http://docs.aws.amazon.com/ElasticMapReduce/'
           'latest/DeveloperGuide/ami-versions-supported.html')


class MissingBooleanOptionsError(EmrError):
    """
    Required boolean options are not supplied.

    :ivar true_option
    :ivar false_option
    """
    fmt = ('aws: error: Must specify one of the following boolean options: '
           '{true_option}|{false_option}.')


class UnknownStepTypeError(EmrError):
    """
    The provided step type is not supported.

    :ivar step_type: the step_type provided.
    """
    fmt = ('aws: error: The step type {step_type} is not supported.')


class UnknownApplicationError(EmrError):
    """
    The provided application name is unknown.

    :ivar application_name: the application name provided.
    """
    fmt = ('aws: error: The application name {app_name} is not supported. '
           '"Name" should be one of the following: ' +
           (', '.join(constants.APPLICATIONS))) + '.'


class UnknownIamEndpointError(EmrError):
    """
    The IAM endpoint is not known for the specified region.

    :ivar region: The region specified.
    """
    fmt = 'IAM endpoint not known for region: {region}.' +\
          ' Specify the iam-endpoint using the --iam-endpoint option.'


class ResolveServicePrincipalError(EmrError):
    """
    The service principal could not be resolved from the region or the
    endpoint.
    """
    fmt = 'Could not resolve the service principal from' +\
          ' the region or the endpoint.'


class LogUriError(EmrError):
    """
    The LogUri is not specified and debugging is enabled for the cluster.
    """
    fmt = ('aws: error: LogUri not specified. You must specify a logUri '
           'if you enable debugging when creating a cluster.')


class MasterDNSNotAvailableError(EmrError):
    """
    Cannot get public dns of master node on the cluster.
    """
    fmt = 'Cannot get Public DNS of master node on the cluster. '\
          ' Please try again after some time.'


class WrongPuttyKeyError(EmrError):
    """
    A wrong key has been used with a compatible program.
    """
    fmt = 'Key file file format is incorrect. Putty expects a ppk file. '\
          'Please refer to documentation at http://docs.aws.amazon.com/'\
          'ElasticMapReduce/latest/DeveloperGuide/EMR_SetUp_SSH.html. '


class WrongSSHKeyError(EmrError):
    """
    A wrong key has been used with a compatible program.
    """
    fmt = 'Key file file format is incorrect. SSH expects a cer or pem file. '\
          'Please refer to documentation at http://docs.aws.amazon.com/'\
          'ElasticMapReduce/latest/DeveloperGuide/EMR_SetUp_SSH.html '


class SSHNotFoundError(EmrError):
    """
    SSH or Putty not available.
    """
    fmt = 'SSH or Putty not available. Please refer to the documentation '\
          'at http://docs.aws.amazon.com/ElasticMapReduce/latest/'\
          'DeveloperGuide/EMR_SetUp_SSH.html.'


class SCPNotFoundError(EmrError):
    """
    SCP or Pscp not available.
    """
    fmt = 'SCP or Pscp not available. Please refer to the documentation '\
          'at http://docs.aws.amazon.com/ElasticMapReduce/latest/'\
          'DeveloperGuide/EMR_SetUp_SSH.html. '


class SubnetAndAzValidationError(EmrError):
    """
    SubnetId and AvailabilityZone are mutual exclusive in --ec2-attributes.
    """
    fmt = ('aws: error: You may not specify both a SubnetId and an Availabili'
           'tyZone (placement) because ec2SubnetId implies a placement.')


class MissingApplicationsError(EmrError):
    """
    The application required for a step is not installed when creating a
    cluster.

    :ivar applications
    """

    def __init__(self, **kwargs):
        msg = ('aws: error: Some of the steps require the following'
               ' applications to be installed: ' +
               ', '.join(kwargs['applications']) + '. Please install the'
               ' applications using --applications.')
        Exception.__init__(self, msg)


class ClusterTerminatedError(EmrError):
    """
    The cluster is terminating or has already terminated.
    """
    fmt = 'aws: error: Cluster terminating or already terminated.'


class ClusterStatesFilterValidationError(EmrError):
    """
    In the list-clusters command, customers can specify only one
    of the following states filters:
    --cluster-states, --active, --terminated, --failed

    """
    fmt = ('aws: error: You can specify only one of the cluster state '
           'filters: --cluster-states, --active, --terminated, --failed.')
