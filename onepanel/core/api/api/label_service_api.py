# coding: utf-8

"""
    Onepanel

    Onepanel API  # noqa: E501

    The version of the OpenAPI document: 0.11.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from onepanel.core.api.api_client import ApiClient
from onepanel.core.api.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class LabelServiceApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_labels(self, namespace, resource, uid, body, **kwargs):  # noqa: E501
        """add_labels  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_labels(namespace, resource, uid, body, async_req=True)
        >>> result = thread.get()

        :param namespace: (required)
        :type namespace: str
        :param resource: (required)
        :type resource: str
        :param uid: (required)
        :type uid: str
        :param body: (required)
        :type body: Labels
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetLabelsResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.add_labels_with_http_info(namespace, resource, uid, body, **kwargs)  # noqa: E501

    def add_labels_with_http_info(self, namespace, resource, uid, body, **kwargs):  # noqa: E501
        """add_labels  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_labels_with_http_info(namespace, resource, uid, body, async_req=True)
        >>> result = thread.get()

        :param namespace: (required)
        :type namespace: str
        :param resource: (required)
        :type resource: str
        :param uid: (required)
        :type uid: str
        :param body: (required)
        :type body: Labels
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GetLabelsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'namespace',
            'resource',
            'uid',
            'body'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_labels" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'namespace' is set
        if self.api_client.client_side_validation and ('namespace' not in local_var_params or  # noqa: E501
                                                        local_var_params['namespace'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `namespace` when calling `add_labels`")  # noqa: E501
        # verify the required parameter 'resource' is set
        if self.api_client.client_side_validation and ('resource' not in local_var_params or  # noqa: E501
                                                        local_var_params['resource'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `resource` when calling `add_labels`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if self.api_client.client_side_validation and ('uid' not in local_var_params or  # noqa: E501
                                                        local_var_params['uid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `uid` when calling `add_labels`")  # noqa: E501
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in local_var_params or  # noqa: E501
                                                        local_var_params['body'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `body` when calling `add_labels`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']  # noqa: E501
        if 'resource' in local_var_params:
            path_params['resource'] = local_var_params['resource']  # noqa: E501
        if 'uid' in local_var_params:
            path_params['uid'] = local_var_params['uid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/apis/v1beta1/{namespace}/{resource}/{uid}/labels', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetLabelsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def delete_label(self, namespace, resource, uid, key, **kwargs):  # noqa: E501
        """delete_label  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_label(namespace, resource, uid, key, async_req=True)
        >>> result = thread.get()

        :param namespace: (required)
        :type namespace: str
        :param resource: (required)
        :type resource: str
        :param uid: (required)
        :type uid: str
        :param key: (required)
        :type key: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetLabelsResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_label_with_http_info(namespace, resource, uid, key, **kwargs)  # noqa: E501

    def delete_label_with_http_info(self, namespace, resource, uid, key, **kwargs):  # noqa: E501
        """delete_label  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_label_with_http_info(namespace, resource, uid, key, async_req=True)
        >>> result = thread.get()

        :param namespace: (required)
        :type namespace: str
        :param resource: (required)
        :type resource: str
        :param uid: (required)
        :type uid: str
        :param key: (required)
        :type key: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GetLabelsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'namespace',
            'resource',
            'uid',
            'key'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_label" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'namespace' is set
        if self.api_client.client_side_validation and ('namespace' not in local_var_params or  # noqa: E501
                                                        local_var_params['namespace'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `namespace` when calling `delete_label`")  # noqa: E501
        # verify the required parameter 'resource' is set
        if self.api_client.client_side_validation and ('resource' not in local_var_params or  # noqa: E501
                                                        local_var_params['resource'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `resource` when calling `delete_label`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if self.api_client.client_side_validation and ('uid' not in local_var_params or  # noqa: E501
                                                        local_var_params['uid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `uid` when calling `delete_label`")  # noqa: E501
        # verify the required parameter 'key' is set
        if self.api_client.client_side_validation and ('key' not in local_var_params or  # noqa: E501
                                                        local_var_params['key'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `key` when calling `delete_label`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']  # noqa: E501
        if 'resource' in local_var_params:
            path_params['resource'] = local_var_params['resource']  # noqa: E501
        if 'uid' in local_var_params:
            path_params['uid'] = local_var_params['uid']  # noqa: E501
        if 'key' in local_var_params:
            path_params['key'] = local_var_params['key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/apis/v1beta1/{namespace}/{resource}/{uid}/labels/{key}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetLabelsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def get_labels(self, namespace, resource, uid, **kwargs):  # noqa: E501
        """get_labels  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_labels(namespace, resource, uid, async_req=True)
        >>> result = thread.get()

        :param namespace: (required)
        :type namespace: str
        :param resource: (required)
        :type resource: str
        :param uid: (required)
        :type uid: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetLabelsResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.get_labels_with_http_info(namespace, resource, uid, **kwargs)  # noqa: E501

    def get_labels_with_http_info(self, namespace, resource, uid, **kwargs):  # noqa: E501
        """get_labels  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_labels_with_http_info(namespace, resource, uid, async_req=True)
        >>> result = thread.get()

        :param namespace: (required)
        :type namespace: str
        :param resource: (required)
        :type resource: str
        :param uid: (required)
        :type uid: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GetLabelsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'namespace',
            'resource',
            'uid'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_labels" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'namespace' is set
        if self.api_client.client_side_validation and ('namespace' not in local_var_params or  # noqa: E501
                                                        local_var_params['namespace'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `namespace` when calling `get_labels`")  # noqa: E501
        # verify the required parameter 'resource' is set
        if self.api_client.client_side_validation and ('resource' not in local_var_params or  # noqa: E501
                                                        local_var_params['resource'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `resource` when calling `get_labels`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if self.api_client.client_side_validation and ('uid' not in local_var_params or  # noqa: E501
                                                        local_var_params['uid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `uid` when calling `get_labels`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']  # noqa: E501
        if 'resource' in local_var_params:
            path_params['resource'] = local_var_params['resource']  # noqa: E501
        if 'uid' in local_var_params:
            path_params['uid'] = local_var_params['uid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/apis/v1beta1/{namespace}/{resource}/{uid}/labels', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetLabelsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def replace_labels(self, namespace, resource, uid, body, **kwargs):  # noqa: E501
        """replace_labels  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.replace_labels(namespace, resource, uid, body, async_req=True)
        >>> result = thread.get()

        :param namespace: (required)
        :type namespace: str
        :param resource: (required)
        :type resource: str
        :param uid: (required)
        :type uid: str
        :param body: (required)
        :type body: Labels
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetLabelsResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.replace_labels_with_http_info(namespace, resource, uid, body, **kwargs)  # noqa: E501

    def replace_labels_with_http_info(self, namespace, resource, uid, body, **kwargs):  # noqa: E501
        """replace_labels  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.replace_labels_with_http_info(namespace, resource, uid, body, async_req=True)
        >>> result = thread.get()

        :param namespace: (required)
        :type namespace: str
        :param resource: (required)
        :type resource: str
        :param uid: (required)
        :type uid: str
        :param body: (required)
        :type body: Labels
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GetLabelsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'namespace',
            'resource',
            'uid',
            'body'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method replace_labels" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'namespace' is set
        if self.api_client.client_side_validation and ('namespace' not in local_var_params or  # noqa: E501
                                                        local_var_params['namespace'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `namespace` when calling `replace_labels`")  # noqa: E501
        # verify the required parameter 'resource' is set
        if self.api_client.client_side_validation and ('resource' not in local_var_params or  # noqa: E501
                                                        local_var_params['resource'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `resource` when calling `replace_labels`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if self.api_client.client_side_validation and ('uid' not in local_var_params or  # noqa: E501
                                                        local_var_params['uid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `uid` when calling `replace_labels`")  # noqa: E501
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in local_var_params or  # noqa: E501
                                                        local_var_params['body'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `body` when calling `replace_labels`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']  # noqa: E501
        if 'resource' in local_var_params:
            path_params['resource'] = local_var_params['resource']  # noqa: E501
        if 'uid' in local_var_params:
            path_params['uid'] = local_var_params['uid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/apis/v1beta1/{namespace}/{resource}/{uid}/labels', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetLabelsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
