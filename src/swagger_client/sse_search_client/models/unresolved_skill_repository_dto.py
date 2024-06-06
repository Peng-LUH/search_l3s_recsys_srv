# coding: utf-8

"""
    Skill Repository

    The API description of the Skill Repository.  # noqa: E501

    OpenAPI spec version: 1.1.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class UnresolvedSkillRepositoryDto(object):
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
        'owner': 'str',
        'id': 'str',
        'taxonomy': 'str',
        'description': 'str',
        'access_rights': 'object',
        'name': 'str',
        'version': 'str',
        'skills': 'list[str]'
    }

    attribute_map = {
        'owner': 'owner',
        'id': 'id',
        'taxonomy': 'taxonomy',
        'description': 'description',
        'access_rights': 'access_rights',
        'name': 'name',
        'version': 'version',
        'skills': 'skills'
    }

    def __init__(self, owner=None, id=None, taxonomy=None, description=None, access_rights=None, name=None, version=None, skills=None):  # noqa: E501
        """UnresolvedSkillRepositoryDto - a model defined in Swagger"""  # noqa: E501
        self._owner = None
        self._id = None
        self._taxonomy = None
        self._description = None
        self._access_rights = None
        self._name = None
        self._version = None
        self._skills = None
        self.discriminator = None
        self.owner = owner
        self.id = id
        if taxonomy is not None:
            self.taxonomy = taxonomy
        if description is not None:
            self.description = description
        if access_rights is not None:
            self.access_rights = access_rights
        self.name = name
        if version is not None:
            self.version = version
        self.skills = skills

    @property
    def owner(self):
        """Gets the owner of this UnresolvedSkillRepositoryDto.  # noqa: E501


        :return: The owner of this UnresolvedSkillRepositoryDto.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this UnresolvedSkillRepositoryDto.


        :param owner: The owner of this UnresolvedSkillRepositoryDto.  # noqa: E501
        :type: str
        """
        if owner is None:
            raise ValueError("Invalid value for `owner`, must not be `None`")  # noqa: E501

        self._owner = owner

    @property
    def id(self):
        """Gets the id of this UnresolvedSkillRepositoryDto.  # noqa: E501


        :return: The id of this UnresolvedSkillRepositoryDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UnresolvedSkillRepositoryDto.


        :param id: The id of this UnresolvedSkillRepositoryDto.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def taxonomy(self):
        """Gets the taxonomy of this UnresolvedSkillRepositoryDto.  # noqa: E501


        :return: The taxonomy of this UnresolvedSkillRepositoryDto.  # noqa: E501
        :rtype: str
        """
        return self._taxonomy

    @taxonomy.setter
    def taxonomy(self, taxonomy):
        """Sets the taxonomy of this UnresolvedSkillRepositoryDto.


        :param taxonomy: The taxonomy of this UnresolvedSkillRepositoryDto.  # noqa: E501
        :type: str
        """

        self._taxonomy = taxonomy

    @property
    def description(self):
        """Gets the description of this UnresolvedSkillRepositoryDto.  # noqa: E501


        :return: The description of this UnresolvedSkillRepositoryDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UnresolvedSkillRepositoryDto.


        :param description: The description of this UnresolvedSkillRepositoryDto.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def access_rights(self):
        """Gets the access_rights of this UnresolvedSkillRepositoryDto.  # noqa: E501


        :return: The access_rights of this UnresolvedSkillRepositoryDto.  # noqa: E501
        :rtype: object
        """
        return self._access_rights

    @access_rights.setter
    def access_rights(self, access_rights):
        """Sets the access_rights of this UnresolvedSkillRepositoryDto.


        :param access_rights: The access_rights of this UnresolvedSkillRepositoryDto.  # noqa: E501
        :type: object
        """

        self._access_rights = access_rights

    @property
    def name(self):
        """Gets the name of this UnresolvedSkillRepositoryDto.  # noqa: E501


        :return: The name of this UnresolvedSkillRepositoryDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UnresolvedSkillRepositoryDto.


        :param name: The name of this UnresolvedSkillRepositoryDto.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def version(self):
        """Gets the version of this UnresolvedSkillRepositoryDto.  # noqa: E501


        :return: The version of this UnresolvedSkillRepositoryDto.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this UnresolvedSkillRepositoryDto.


        :param version: The version of this UnresolvedSkillRepositoryDto.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def skills(self):
        """Gets the skills of this UnresolvedSkillRepositoryDto.  # noqa: E501


        :return: The skills of this UnresolvedSkillRepositoryDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._skills

    @skills.setter
    def skills(self, skills):
        """Sets the skills of this UnresolvedSkillRepositoryDto.


        :param skills: The skills of this UnresolvedSkillRepositoryDto.  # noqa: E501
        :type: list[str]
        """
        if skills is None:
            raise ValueError("Invalid value for `skills`, must not be `None`")  # noqa: E501

        self._skills = skills

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
        if issubclass(UnresolvedSkillRepositoryDto, dict):
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
        if not isinstance(other, UnresolvedSkillRepositoryDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
