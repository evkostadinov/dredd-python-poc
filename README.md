# dredd-python-poc

Based on https://www.npmjs.com/package/dredd and https://github.com/apiaryio/dredd-hooks-python

## How the REST API automation brings value to the productivity and quality for current projects

1. Dredd reads our API description and step by step validates whether the API implementation replies with responses as they are described in the documentation.

2. Supports writing hooks — a glue code for each test setup and teardown for Python with Jenkins (CI integration).

3. Prevents Documentation degradation over time, the tool will check for discrepancies between our documentation and the actual implementation.
Keeps us save on HTTP API documentation errors, like:

 - new field added or removed from the API request or response, but not reflected in the documentation

 - new query string has been added which was not listed
 
 - or a new JSON-API style link (relationship) is being presented that was not available before
 
 - response headers changes

4. Leverage test data, so more complex cases can be covered, not only 200 replies, but posting FHIR objects to the backend and validating its compliance.

5. Running with different users, checking that various endpoints expect tokens to belong to either users

6. It leverages Design-first approach to developing APIs

## A medal system, to give people an idea of where their docs/specs are at
And to give API clients/consumers of the docs an idea of how much they could trust the docs.

🏅 Gold - Guaranteed accurate against code, thanks to the use of Dredd or JSON Schema Matchers, which means the API build will fail if the specification is lying

🥈 Silver - Not guaranteed to be entirely accurate, but confidence levels are high. There may be minor discrepancies.

🥉 Bronze - Hey look, at least there’s something… 😅


## Limitations
This can be a good start, but it should not be relied on as our complete test-suite. Dredd provides documentation testing, and essentially we end up with generated (to some degree) integration and contract testing as a side benefit. The tool doesn't completely replace other automated tests. We  should still unit test our code and have integration or end-to-end tests to cover various corner cases. Dredd helps ensuring the essentials we documented and promised in our API description file will always work in the implementation. High level journeys can't be really accomplished as this requires a proper programming language and framework around it.
