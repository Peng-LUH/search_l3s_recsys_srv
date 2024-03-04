# coding: utf-8

"""
    Skill Repository

    The API description of the Skill Repository.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class JobUpdateDto(object):
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
        'job_title': 'str',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'company_id': 'str',
        'job_id_at_berufe_net': 'str'
    }

    attribute_map = {
        'job_title': 'jobTitle',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'company_id': 'companyId',
        'job_id_at_berufe_net': 'jobIdAtBerufeNet'
    }

    def __init__(self, job_title=None, start_time=None, end_time=None, company_id=None, job_id_at_berufe_net=None):  # noqa: E501
        """JobUpdateDto - a model defined in Swagger"""  # noqa: E501
        self._job_title = None
        self._start_time = None
        self._end_time = None
        self._company_id = None
        self._job_id_at_berufe_net = None
        self.discriminator = None
        self.job_title = job_title
        self.start_time = start_time
        self.end_time = end_time
        self.company_id = company_id
        if job_id_at_berufe_net is not None:
            self.job_id_at_berufe_net = job_id_at_berufe_net

    @property
    def job_title(self):
        """Gets the job_title of this JobUpdateDto.  # noqa: E501


        :return: The job_title of this JobUpdateDto.  # noqa: E501
        :rtype: str
        """
        return self._job_title

    @job_title.setter
    def job_title(self, job_title):
        """Sets the job_title of this JobUpdateDto.


        :param job_title: The job_title of this JobUpdateDto.  # noqa: E501
        :type: str
        """
        if job_title is None:
            raise ValueError("Invalid value for `job_title`, must not be `None`")  # noqa: E501

        self._job_title = job_title

    @property
    def start_time(self):
        """Gets the start_time of this JobUpdateDto.  # noqa: E501


        :return: The start_time of this JobUpdateDto.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this JobUpdateDto.


        :param start_time: The start_time of this JobUpdateDto.  # noqa: E501
        :type: datetime
        """
        if start_time is None:
            raise ValueError("Invalid value for `start_time`, must not be `None`")  # noqa: E501

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this JobUpdateDto.  # noqa: E501


        :return: The end_time of this JobUpdateDto.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this JobUpdateDto.


        :param end_time: The end_time of this JobUpdateDto.  # noqa: E501
        :type: datetime
        """
        if end_time is None:
            raise ValueError("Invalid value for `end_time`, must not be `None`")  # noqa: E501

        self._end_time = end_time

    @property
    def company_id(self):
        """Gets the company_id of this JobUpdateDto.  # noqa: E501


        :return: The company_id of this JobUpdateDto.  # noqa: E501
        :rtype: str
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this JobUpdateDto.


        :param company_id: The company_id of this JobUpdateDto.  # noqa: E501
        :type: str
        """
        if company_id is None:
            raise ValueError("Invalid value for `company_id`, must not be `None`")  # noqa: E501

        self._company_id = company_id

    @property
    def job_id_at_berufe_net(self):
        """Gets the job_id_at_berufe_net of this JobUpdateDto.  # noqa: E501


        :return: The job_id_at_berufe_net of this JobUpdateDto.  # noqa: E501
        :rtype: str
        """
        return self._job_id_at_berufe_net

    @job_id_at_berufe_net.setter
    def job_id_at_berufe_net(self, job_id_at_berufe_net):
        """Sets the job_id_at_berufe_net of this JobUpdateDto.


        :param job_id_at_berufe_net: The job_id_at_berufe_net of this JobUpdateDto.  # noqa: E501
        :type: str
        """

        self._job_id_at_berufe_net = job_id_at_berufe_net

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
        if issubclass(JobUpdateDto, dict):
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
        if not isinstance(other, JobUpdateDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
