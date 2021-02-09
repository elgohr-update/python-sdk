# coding: utf-8

"""
    Onepanel

    Onepanel API  # noqa: E501

    The version of the OpenAPI document: 0.18.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from onepanel.core.api.configuration import Configuration


class WorkflowExecution(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'created_at': 'str',
        'uid': 'str',
        'name': 'str',
        'phase': 'str',
        'started_at': 'str',
        'finished_at': 'str',
        'manifest': 'str',
        'parameters': 'list[Parameter]',
        'workflow_template': 'WorkflowTemplate',
        'labels': 'list[KeyValue]',
        'metadata': 'WorkflowExecutionMetadata',
        'metrics': 'list[Metric]'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'uid': 'uid',
        'name': 'name',
        'phase': 'phase',
        'started_at': 'startedAt',
        'finished_at': 'finishedAt',
        'manifest': 'manifest',
        'parameters': 'parameters',
        'workflow_template': 'workflowTemplate',
        'labels': 'labels',
        'metadata': 'metadata',
        'metrics': 'metrics'
    }

    def __init__(self, created_at=None, uid=None, name=None, phase=None, started_at=None, finished_at=None, manifest=None, parameters=None, workflow_template=None, labels=None, metadata=None, metrics=None, local_vars_configuration=None):  # noqa: E501
        """WorkflowExecution - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._created_at = None
        self._uid = None
        self._name = None
        self._phase = None
        self._started_at = None
        self._finished_at = None
        self._manifest = None
        self._parameters = None
        self._workflow_template = None
        self._labels = None
        self._metadata = None
        self._metrics = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if uid is not None:
            self.uid = uid
        if name is not None:
            self.name = name
        if phase is not None:
            self.phase = phase
        if started_at is not None:
            self.started_at = started_at
        if finished_at is not None:
            self.finished_at = finished_at
        if manifest is not None:
            self.manifest = manifest
        if parameters is not None:
            self.parameters = parameters
        if workflow_template is not None:
            self.workflow_template = workflow_template
        if labels is not None:
            self.labels = labels
        if metadata is not None:
            self.metadata = metadata
        if metrics is not None:
            self.metrics = metrics

    @property
    def created_at(self):
        """Gets the created_at of this WorkflowExecution.  # noqa: E501


        :return: The created_at of this WorkflowExecution.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this WorkflowExecution.


        :param created_at: The created_at of this WorkflowExecution.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def uid(self):
        """Gets the uid of this WorkflowExecution.  # noqa: E501


        :return: The uid of this WorkflowExecution.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this WorkflowExecution.


        :param uid: The uid of this WorkflowExecution.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def name(self):
        """Gets the name of this WorkflowExecution.  # noqa: E501


        :return: The name of this WorkflowExecution.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WorkflowExecution.


        :param name: The name of this WorkflowExecution.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def phase(self):
        """Gets the phase of this WorkflowExecution.  # noqa: E501


        :return: The phase of this WorkflowExecution.  # noqa: E501
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this WorkflowExecution.


        :param phase: The phase of this WorkflowExecution.  # noqa: E501
        :type: str
        """

        self._phase = phase

    @property
    def started_at(self):
        """Gets the started_at of this WorkflowExecution.  # noqa: E501


        :return: The started_at of this WorkflowExecution.  # noqa: E501
        :rtype: str
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this WorkflowExecution.


        :param started_at: The started_at of this WorkflowExecution.  # noqa: E501
        :type: str
        """

        self._started_at = started_at

    @property
    def finished_at(self):
        """Gets the finished_at of this WorkflowExecution.  # noqa: E501


        :return: The finished_at of this WorkflowExecution.  # noqa: E501
        :rtype: str
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this WorkflowExecution.


        :param finished_at: The finished_at of this WorkflowExecution.  # noqa: E501
        :type: str
        """

        self._finished_at = finished_at

    @property
    def manifest(self):
        """Gets the manifest of this WorkflowExecution.  # noqa: E501


        :return: The manifest of this WorkflowExecution.  # noqa: E501
        :rtype: str
        """
        return self._manifest

    @manifest.setter
    def manifest(self, manifest):
        """Sets the manifest of this WorkflowExecution.


        :param manifest: The manifest of this WorkflowExecution.  # noqa: E501
        :type: str
        """

        self._manifest = manifest

    @property
    def parameters(self):
        """Gets the parameters of this WorkflowExecution.  # noqa: E501


        :return: The parameters of this WorkflowExecution.  # noqa: E501
        :rtype: list[Parameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this WorkflowExecution.


        :param parameters: The parameters of this WorkflowExecution.  # noqa: E501
        :type: list[Parameter]
        """

        self._parameters = parameters

    @property
    def workflow_template(self):
        """Gets the workflow_template of this WorkflowExecution.  # noqa: E501


        :return: The workflow_template of this WorkflowExecution.  # noqa: E501
        :rtype: WorkflowTemplate
        """
        return self._workflow_template

    @workflow_template.setter
    def workflow_template(self, workflow_template):
        """Sets the workflow_template of this WorkflowExecution.


        :param workflow_template: The workflow_template of this WorkflowExecution.  # noqa: E501
        :type: WorkflowTemplate
        """

        self._workflow_template = workflow_template

    @property
    def labels(self):
        """Gets the labels of this WorkflowExecution.  # noqa: E501


        :return: The labels of this WorkflowExecution.  # noqa: E501
        :rtype: list[KeyValue]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this WorkflowExecution.


        :param labels: The labels of this WorkflowExecution.  # noqa: E501
        :type: list[KeyValue]
        """

        self._labels = labels

    @property
    def metadata(self):
        """Gets the metadata of this WorkflowExecution.  # noqa: E501


        :return: The metadata of this WorkflowExecution.  # noqa: E501
        :rtype: WorkflowExecutionMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this WorkflowExecution.


        :param metadata: The metadata of this WorkflowExecution.  # noqa: E501
        :type: WorkflowExecutionMetadata
        """

        self._metadata = metadata

    @property
    def metrics(self):
        """Gets the metrics of this WorkflowExecution.  # noqa: E501


        :return: The metrics of this WorkflowExecution.  # noqa: E501
        :rtype: list[Metric]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this WorkflowExecution.


        :param metrics: The metrics of this WorkflowExecution.  # noqa: E501
        :type: list[Metric]
        """

        self._metrics = metrics

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WorkflowExecution):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkflowExecution):
            return True

        return self.to_dict() != other.to_dict()
