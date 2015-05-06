RESTAPI-CLIENT
================

This lib is used for call RestApi services.

## Installing

In your python environment use this command:

```bash
$ pip install restapi-client
```

Or, you can make a local clone of this repository and install with this commands:

```bash
$ python setup.py install
```

## Usage


Format of calls:

    <myserver.com>.<endpoint>.[save,get(id),get_all,delete(id),update(id,data)]

Example:

```python
>> from restapi import Client
>> api = Client()
>> ret = api.<endpointname>.get()
>> api.<endpointname>.save(dict_data)
>> ret = api.<endpointname>.get("<the_id>")
>> api.<endpointname>.update("<the_id>", dict_data)
>> api.<endpointname>.delete("<the_id>")
```

## Methods

**save( data )**:

 - **data**: dictionary parameter with the record properties

**get( [the_id] )**

 - **the_id**: The id of the specific record

**update( reg_id, user_data )**

 - **reg_id**: The id of the specific record
 - **user_data**: dictionary parameter with properties that will be updated in
 the record
 - `return`: The updated record

 **delete( reg_id )**

 - **reg_id**: The id of the specific record to be deleted
 - `return`: Nothing

### OBS:

> All methods have also the parameters _user_params_ and _user_headers_
when:
>
> * _user_params_: A dictionary object, that will be passed as uri parameters, like:
> http://servername.com/?param1=val1&param2=val2
> * _user_headers_: A dictionary object that wil be passwd as headers in the
> http call
> This lib does not support authentication

> All methods return a `restapi.ApiError` if the call have problems.

### Default Headers:

* **'Content-Type': 'application/json'**
