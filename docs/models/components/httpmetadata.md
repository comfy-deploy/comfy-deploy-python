# HTTPMetadata


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `response`                                                   | [httpx.Response](https://www.python-httpx.org/api/#response) | :heavy_check_mark:                                           | Raw HTTP response; suitable for custom response parsing      |
| `request`                                                    | [httpx.Request](https://www.python-httpx.org/api/#request)   | :heavy_check_mark:                                           | Raw HTTP request; suitable for debugging                     |