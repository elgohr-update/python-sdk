# core.api.WorkflowServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_workflow_template**](WorkflowServiceApi.md#archive_workflow_template) | **PUT** /apis/v1beta1/{namespace}/workflow_templates/{uid}/archive | 
[**create_workflow_execution**](WorkflowServiceApi.md#create_workflow_execution) | **POST** /apis/v1beta1/{namespace}/workflow_executions | 
[**create_workflow_template**](WorkflowServiceApi.md#create_workflow_template) | **POST** /apis/v1beta1/{namespace}/workflow_templates | 
[**create_workflow_template_version**](WorkflowServiceApi.md#create_workflow_template_version) | **POST** /apis/v1beta1/{namespace}/workflow_templates/{workflowTemplate.uid}/versions | 
[**get_workflow_execution**](WorkflowServiceApi.md#get_workflow_execution) | **GET** /apis/v1beta1/{namespace}/workflow_executions/{name} | 
[**get_workflow_execution_logs**](WorkflowServiceApi.md#get_workflow_execution_logs) | **GET** /apis/v1beta1/{namespace}/workflow_executions/{name}/pods/{podName}/containers/{containerName}/logs | 
[**get_workflow_execution_metrics**](WorkflowServiceApi.md#get_workflow_execution_metrics) | **GET** /apis/v1beta1/{namespace}/workflow_executions/{name}/pods/{podName}/metrics | 
[**get_workflow_template**](WorkflowServiceApi.md#get_workflow_template) | **GET** /apis/v1beta1/{namespace}/workflow_templates/{uid} | 
[**get_workflow_template2**](WorkflowServiceApi.md#get_workflow_template2) | **GET** /apis/v1beta1/{namespace}/workflow_templates/{uid}/versions/{version} | 
[**list_workflow_executions**](WorkflowServiceApi.md#list_workflow_executions) | **GET** /apis/v1beta1/{namespace}/workflow_executions | 
[**list_workflow_template_versions**](WorkflowServiceApi.md#list_workflow_template_versions) | **GET** /apis/v1beta1/{namespace}/workflow_templates/{uid}/versions | 
[**list_workflow_templates**](WorkflowServiceApi.md#list_workflow_templates) | **GET** /apis/v1beta1/{namespace}/workflow_templates | 
[**resubmit_workflow_execution**](WorkflowServiceApi.md#resubmit_workflow_execution) | **PUT** /apis/v1beta1/{namespace}/workflow_executions/{name}/resubmit | 
[**terminate_workflow_execution**](WorkflowServiceApi.md#terminate_workflow_execution) | **PUT** /apis/v1beta1/{namespace}/workflow_executions/{name}/terminate | 
[**update_workflow_template_version**](WorkflowServiceApi.md#update_workflow_template_version) | **PUT** /apis/v1beta1/{namespace}/workflow_templates/{workflowTemplate.uid}/versions/{workflowTemplate.version} | 
[**watch_workflow_execution**](WorkflowServiceApi.md#watch_workflow_execution) | **GET** /apis/v1beta1/{namespace}/workflow_executions/{name}/watch | 


# **archive_workflow_template**
> ArchiveWorkflowTemplateResponse archive_workflow_template(namespace, uid)



### Example

* Api Key Authentication (bearer):
```python
from __future__ import print_function
import time
import core.api
from core.api.rest import ApiException
from pprint import pprint
configuration = core.api.Configuration()
# Configure API key authorization: bearer
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Enter a context with an instance of the API client
with core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
uid = 'uid_example' # str | 

    try:
        api_response = api_instance.archive_workflow_template(namespace, uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->archive_workflow_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **uid** | **str**|  | 

### Return type

[**ArchiveWorkflowTemplateResponse**](ArchiveWorkflowTemplateResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_workflow_execution**
> WorkflowExecution create_workflow_execution(namespace, body)



### Example

* Api Key Authentication (bearer):
```python
from __future__ import print_function
import time
import core.api
from core.api.rest import ApiException
from pprint import pprint
configuration = core.api.Configuration()
# Configure API key authorization: bearer
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Enter a context with an instance of the API client
with core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
body = core.api.WorkflowExecution() # WorkflowExecution | 

    try:
        api_response = api_instance.create_workflow_execution(namespace, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->create_workflow_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **body** | [**WorkflowExecution**](WorkflowExecution.md)|  | 

### Return type

[**WorkflowExecution**](WorkflowExecution.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_workflow_template**
> WorkflowTemplate create_workflow_template(namespace, body)



### Example

* Api Key Authentication (bearer):
```python
from __future__ import print_function
import time
import core.api
from core.api.rest import ApiException
from pprint import pprint
configuration = core.api.Configuration()
# Configure API key authorization: bearer
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Enter a context with an instance of the API client
with core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
body = core.api.WorkflowTemplate() # WorkflowTemplate | 

    try:
        api_response = api_instance.create_workflow_template(namespace, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->create_workflow_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **body** | [**WorkflowTemplate**](WorkflowTemplate.md)|  | 

### Return type

[**WorkflowTemplate**](WorkflowTemplate.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_workflow_template_version**
> WorkflowTemplate create_workflow_template_version(namespace, workflow_template_uid, body)



### Example

* Api Key Authentication (bearer):
```python
from __future__ import print_function
import time
import core.api
from core.api.rest import ApiException
from pprint import pprint
configuration = core.api.Configuration()
# Configure API key authorization: bearer
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Enter a context with an instance of the API client
with core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
workflow_template_uid = 'workflow_template_uid_example' # str | 
body = core.api.WorkflowTemplate() # WorkflowTemplate | 

    try:
        api_response = api_instance.create_workflow_template_version(namespace, workflow_template_uid, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->create_workflow_template_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **workflow_template_uid** | **str**|  | 
 **body** | [**WorkflowTemplate**](WorkflowTemplate.md)|  | 

### Return type

[**WorkflowTemplate**](WorkflowTemplate.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_execution**
> WorkflowExecution get_workflow_execution(namespace, name)



### Example

* Api Key Authentication (bearer):
```python
from __future__ import print_function
import time
import core.api
from core.api.rest import ApiException
from pprint import pprint
configuration = core.api.Configuration()
# Configure API key authorization: bearer
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Enter a context with an instance of the API client
with core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
name = 'name_example' # str | 

    try:
        api_response = api_instance.get_workflow_execution(namespace, name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->get_workflow_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **name** | **str**|  | 

### Return type

[**WorkflowExecution**](WorkflowExecution.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_execution_logs**
> StreamResultOfLogEntry get_workflow_execution_logs(namespace, name, pod_name, container_name)



### Example

* Api Key Authentication (bearer):
```python
from __future__ import print_function
import time
import core.api
from core.api.rest import ApiException
from pprint import pprint
configuration = core.api.Configuration()
# Configure API key authorization: bearer
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Enter a context with an instance of the API client
with core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
name = 'name_example' # str | 
pod_name = 'pod_name_example' # str | 
container_name = 'container_name_example' # str | 

    try:
        api_response = api_instance.get_workflow_execution_logs(namespace, name, pod_name, container_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->get_workflow_execution_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **name** | **str**|  | 
 **pod_name** | **str**|  | 
 **container_name** | **str**|  | 

### Return type

[**StreamResultOfLogEntry**](StreamResultOfLogEntry.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response.(streaming responses) |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_execution_metrics**
> GetWorkflowExecutionMetricsResponse get_workflow_execution_metrics(namespace, name, pod_name)



### Example

* Api Key Authentication (bearer):
```python
from __future__ import print_function
import time
import core.api
from core.api.rest import ApiException
from pprint import pprint
configuration = core.api.Configuration()
# Configure API key authorization: bearer
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Enter a context with an instance of the API client
with core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
name = 'name_example' # str | 
pod_name = 'pod_name_example' # str | 

    try:
        api_response = api_instance.get_workflow_execution_metrics(namespace, name, pod_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->get_workflow_execution_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **name** | **str**|  | 
 **pod_name** | **str**|  | 

### Return type

[**GetWorkflowExecutionMetricsResponse**](GetWorkflowExecutionMetricsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_template**
> WorkflowTemplate get_workflow_template(namespace, uid, version=version)



### Example

* Api Key Authentication (bearer):
```python
from __future__ import print_function
import time
import core.api
from core.api.rest import ApiException
from pprint import pprint
configuration = core.api.Configuration()
# Configure API key authorization: bearer
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Enter a context with an instance of the API client
with core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
uid = 'uid_example' # str | 
version = 56 # int |  (optional)

    try:
        api_response = api_instance.get_workflow_template(namespace, uid, version=version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->get_workflow_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **uid** | **str**|  | 
 **version** | **int**|  | [optional] 

### Return type

[**WorkflowTemplate**](WorkflowTemplate.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_template2**
> WorkflowTemplate get_workflow_template2(namespace, uid, version)



### Example

* Api Key Authentication (bearer):
```python
from __future__ import print_function
import time
import core.api
from core.api.rest import ApiException
from pprint import pprint
configuration = core.api.Configuration()
# Configure API key authorization: bearer
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Enter a context with an instance of the API client
with core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
uid = 'uid_example' # str | 
version = 56 # int | 

    try:
        api_response = api_instance.get_workflow_template2(namespace, uid, version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->get_workflow_template2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **uid** | **str**|  | 
 **version** | **int**|  | 

### Return type

[**WorkflowTemplate**](WorkflowTemplate.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workflow_executions**
> ListWorkflowExecutionsResponse list_workflow_executions(namespace, workflow_template_uid=workflow_template_uid, workflow_template_version=workflow_template_version, page_size=page_size, page=page)



### Example

* Api Key Authentication (bearer):
```python
from __future__ import print_function
import time
import core.api
from core.api.rest import ApiException
from pprint import pprint
configuration = core.api.Configuration()
# Configure API key authorization: bearer
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Enter a context with an instance of the API client
with core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
workflow_template_uid = 'workflow_template_uid_example' # str |  (optional)
workflow_template_version = 'workflow_template_version_example' # str |  (optional)
page_size = 56 # int |  (optional)
page = 56 # int |  (optional)

    try:
        api_response = api_instance.list_workflow_executions(namespace, workflow_template_uid=workflow_template_uid, workflow_template_version=workflow_template_version, page_size=page_size, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->list_workflow_executions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **workflow_template_uid** | **str**|  | [optional] 
 **workflow_template_version** | **str**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **page** | **int**|  | [optional] 

### Return type

[**ListWorkflowExecutionsResponse**](ListWorkflowExecutionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workflow_template_versions**
> ListWorkflowTemplateVersionsResponse list_workflow_template_versions(namespace, uid)



### Example

* Api Key Authentication (bearer):
```python
from __future__ import print_function
import time
import core.api
from core.api.rest import ApiException
from pprint import pprint
configuration = core.api.Configuration()
# Configure API key authorization: bearer
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Enter a context with an instance of the API client
with core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
uid = 'uid_example' # str | 

    try:
        api_response = api_instance.list_workflow_template_versions(namespace, uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->list_workflow_template_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **uid** | **str**|  | 

### Return type

[**ListWorkflowTemplateVersionsResponse**](ListWorkflowTemplateVersionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workflow_templates**
> ListWorkflowTemplatesResponse list_workflow_templates(namespace)



### Example

* Api Key Authentication (bearer):
```python
from __future__ import print_function
import time
import core.api
from core.api.rest import ApiException
from pprint import pprint
configuration = core.api.Configuration()
# Configure API key authorization: bearer
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Enter a context with an instance of the API client
with core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 

    try:
        api_response = api_instance.list_workflow_templates(namespace)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->list_workflow_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 

### Return type

[**ListWorkflowTemplatesResponse**](ListWorkflowTemplatesResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resubmit_workflow_execution**
> WorkflowExecution resubmit_workflow_execution(namespace, name)



### Example

* Api Key Authentication (bearer):
```python
from __future__ import print_function
import time
import core.api
from core.api.rest import ApiException
from pprint import pprint
configuration = core.api.Configuration()
# Configure API key authorization: bearer
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Enter a context with an instance of the API client
with core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
name = 'name_example' # str | 

    try:
        api_response = api_instance.resubmit_workflow_execution(namespace, name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->resubmit_workflow_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **name** | **str**|  | 

### Return type

[**WorkflowExecution**](WorkflowExecution.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_workflow_execution**
> object terminate_workflow_execution(namespace, name)



### Example

* Api Key Authentication (bearer):
```python
from __future__ import print_function
import time
import core.api
from core.api.rest import ApiException
from pprint import pprint
configuration = core.api.Configuration()
# Configure API key authorization: bearer
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Enter a context with an instance of the API client
with core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
name = 'name_example' # str | 

    try:
        api_response = api_instance.terminate_workflow_execution(namespace, name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->terminate_workflow_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **name** | **str**|  | 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_workflow_template_version**
> WorkflowTemplate update_workflow_template_version(namespace, workflow_template_uid, workflow_template_version, body)



### Example

* Api Key Authentication (bearer):
```python
from __future__ import print_function
import time
import core.api
from core.api.rest import ApiException
from pprint import pprint
configuration = core.api.Configuration()
# Configure API key authorization: bearer
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Enter a context with an instance of the API client
with core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
workflow_template_uid = 'workflow_template_uid_example' # str | 
workflow_template_version = 56 # int | 
body = core.api.WorkflowTemplate() # WorkflowTemplate | 

    try:
        api_response = api_instance.update_workflow_template_version(namespace, workflow_template_uid, workflow_template_version, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->update_workflow_template_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **workflow_template_uid** | **str**|  | 
 **workflow_template_version** | **int**|  | 
 **body** | [**WorkflowTemplate**](WorkflowTemplate.md)|  | 

### Return type

[**WorkflowTemplate**](WorkflowTemplate.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_workflow_execution**
> StreamResultOfWorkflowExecution watch_workflow_execution(namespace, name)



### Example

* Api Key Authentication (bearer):
```python
from __future__ import print_function
import time
import core.api
from core.api.rest import ApiException
from pprint import pprint
configuration = core.api.Configuration()
# Configure API key authorization: bearer
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Enter a context with an instance of the API client
with core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
name = 'name_example' # str | 

    try:
        api_response = api_instance.watch_workflow_execution(namespace, name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->watch_workflow_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **name** | **str**|  | 

### Return type

[**StreamResultOfWorkflowExecution**](StreamResultOfWorkflowExecution.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response.(streaming responses) |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
