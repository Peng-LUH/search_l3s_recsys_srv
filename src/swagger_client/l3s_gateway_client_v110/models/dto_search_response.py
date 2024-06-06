# coding: utf-8

"""
    L3S Gateway for SEARCH

    Welcome to the Swagger UI documentation site!  # noqa: E501

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DtoSearchResponse(object):
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
        'user_id': 'str',
        'owner': 'str',
        'entity_id': 'str',
        'entity_type': 'str',
        'similarity': 'float'
    }

    attribute_map = {
        'user_id': 'user_id',
        'owner': 'owner',
        'entity_id': 'entity_id',
        'entity_type': 'entity_type',
        'similarity': 'similarity'
    }

    def __init__(self, user_id=None, owner=None, entity_id=None, entity_type=None, similarity=None):  # noqa: E501
        """DtoSearchResponse - a model defined in Swagger"""  # noqa: E501
        self._user_id = None
        self._owner = None
        self._entity_id = None
        self._entity_type = None
        self._similarity = None
        self.discriminator = None
        if user_id is not None:
            self.user_id = user_id
        if owner is not None:
            self.owner = owner
        if entity_id is not None:
            self.entity_id = entity_id
        if entity_type is not None:
            self.entity_type = entity_type
        if similarity is not None:
            self.similarity = similarity

    @property
    def user_id(self):
        """Gets the user_id of this DtoSearchResponse.  # noqa: E501

        user ID  # noqa: E501

        :return: The user_id of this DtoSearchResponse.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this DtoSearchResponse.

        user ID  # noqa: E501

        :param user_id: The user_id of this DtoSearchResponse.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def owner(self):
        """Gets the owner of this DtoSearchResponse.  # noqa: E501

        company ID  # noqa: E501

        :return: The owner of this DtoSearchResponse.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this DtoSearchResponse.

        company ID  # noqa: E501

        :param owner: The owner of this DtoSearchResponse.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def entity_id(self):
        """Gets the entity_id of this DtoSearchResponse.  # noqa: E501


        :return: The entity_id of this DtoSearchResponse.  # noqa: E501
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this DtoSearchResponse.


        :param entity_id: The entity_id of this DtoSearchResponse.  # noqa: E501
        :type: str
        """

        self._entity_id = entity_id

    @property
    def entity_type(self):
        """Gets the entity_type of this DtoSearchResponse.  # noqa: E501


        :return: The entity_type of this DtoSearchResponse.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this DtoSearchResponse.


        :param entity_type: The entity_type of this DtoSearchResponse.  # noqa: E501
        :type: str
        """

        self._entity_type = entity_type

    @property
    def similarity(self):
        """Gets the similarity of this DtoSearchResponse.  # noqa: E501


        :return: The similarity of this DtoSearchResponse.  # noqa: E501
        :rtype: float
        """
        return self._similarity

    @similarity.setter
    def similarity(self, similarity):
        """Sets the similarity of this DtoSearchResponse.


        :param similarity: The similarity of this DtoSearchResponse.  # noqa: E501
        :type: float
        """

        self._similarity = similarity

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
        if issubclass(DtoSearchResponse, dict):
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
        if not isinstance(other, DtoSearchResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
