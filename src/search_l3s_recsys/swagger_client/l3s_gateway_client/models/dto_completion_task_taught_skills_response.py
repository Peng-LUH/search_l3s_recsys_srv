# coding: utf-8

"""
    L3S Gateway for SEARCH

    Welcome to the Swagger UI documentation site!  # noqa: E501

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DtoCompletionTaskTaughtSkillsResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'unit_id': 'str',
        'new_skills': 'list[str]',
        'existing_skills': 'list[str]'
    }

    attribute_map = {
        'unit_id': 'unit_id',
        'new_skills': 'new_skills',
        'existing_skills': 'existing_skills'
    }

    def __init__(self, unit_id=None, new_skills=None, existing_skills=None):  # noqa: E501
        """DtoCompletionTaskTaughtSkillsResponse - a model defined in Swagger"""  # noqa: E501
        self._unit_id = None
        self._new_skills = None
        self._existing_skills = None
        self.discriminator = None
        if unit_id is not None:
            self.unit_id = unit_id
        if new_skills is not None:
            self.new_skills = new_skills
        if existing_skills is not None:
            self.existing_skills = existing_skills

    @property
    def unit_id(self):
        """Gets the unit_id of this DtoCompletionTaskTaughtSkillsResponse.  # noqa: E501


        :return: The unit_id of this DtoCompletionTaskTaughtSkillsResponse.  # noqa: E501
        :rtype: str
        """
        return self._unit_id

    @unit_id.setter
    def unit_id(self, unit_id):
        """Sets the unit_id of this DtoCompletionTaskTaughtSkillsResponse.


        :param unit_id: The unit_id of this DtoCompletionTaskTaughtSkillsResponse.  # noqa: E501
        :type: str
        """

        self._unit_id = unit_id

    @property
    def new_skills(self):
        """Gets the new_skills of this DtoCompletionTaskTaughtSkillsResponse.  # noqa: E501


        :return: The new_skills of this DtoCompletionTaskTaughtSkillsResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._new_skills

    @new_skills.setter
    def new_skills(self, new_skills):
        """Sets the new_skills of this DtoCompletionTaskTaughtSkillsResponse.


        :param new_skills: The new_skills of this DtoCompletionTaskTaughtSkillsResponse.  # noqa: E501
        :type: list[str]
        """

        self._new_skills = new_skills

    @property
    def existing_skills(self):
        """Gets the existing_skills of this DtoCompletionTaskTaughtSkillsResponse.  # noqa: E501


        :return: The existing_skills of this DtoCompletionTaskTaughtSkillsResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._existing_skills

    @existing_skills.setter
    def existing_skills(self, existing_skills):
        """Sets the existing_skills of this DtoCompletionTaskTaughtSkillsResponse.


        :param existing_skills: The existing_skills of this DtoCompletionTaskTaughtSkillsResponse.  # noqa: E501
        :type: list[str]
        """

        self._existing_skills = existing_skills

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(DtoCompletionTaskTaughtSkillsResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DtoCompletionTaskTaughtSkillsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
