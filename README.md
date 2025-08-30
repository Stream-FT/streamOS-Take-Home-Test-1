# Take-Home Test

## Overview

Create a synchronous Python REST API that processes invoice creation requests. The API should demonstrate your skills in:

### REST API design and implementation
- Input/Output validation using Pydantic
- Business logic implementation
- External API integration
- Error handling and logging
- Documentation
- Unit testing
- Code organization and quality

## Problem Statement
Build a REST API endpoint that:

- Accepts invoice creation requests for a given charge
- Performs input validation and business logic checks
- Creates invoices via Rutter API
- Optionally sends email notifications with PDF attachments
- Returns the created invoice data

A postman collection will be provided with the API info to fetch the charge.

### Business Logic Implementation

1. Customer/Item Reconciliation Check

   Validate that the invoice has proper customer and item associations:

   - Check that the charge's stream_customer has a field uac_customer_id that contains a valid UUID (not null, not empty)
   - Check that the charge's line items have products where the uac_item_id field contains a valid UUID (not null, not empty)

2. Line Item Filter criteria for Invoice payload

    Filter the charge's line items before including in the payload using these exact conditions:

    - Include only line items where the suppress_line_item field equals false
    - Include only line items where the product_id field is not null

#### Both conditions must be true for a line item to be included in the final payload.


### Rutter API for invoice creation

- Make asynchronous request to Rutter API to create invoice
- Handle the response appropriately
- Rutter credentials will be provided


### Email Integration (Optional)
To send email notifications:

- After successful invoice creation, fetch invoice PDF. 
- Send email with PDF attachment to a hardcoded email address
- The email address configurable via environment variable for testing
- Email sending capability should be optional

The payload for email:
```json
{
    "to": "",
    "subject": "",
    "text": "",
    "attachments": [
        {
            "filename": "",
            "path": ""
        }
    ]
}
```


### Response
- Return the created invoice data to the client. 
- All responses should include schema for reference.

## Optional: Database Integration
For advanced implementation:

- Set up Docker with local database using provided schema in `prisma/schema.prisma`
- Seed data from postman
- Fetch charge from `uac_invoice` table
- Write Rutter API response to `acc_uac_invoice` table

## Technical Requirements

- Language: Python 3.8+
- Framework: FastAPI (recommended) or Flask
- Validation: Pydantic schemas
- HTTP Client: aiohttp or httpx for async operations
- Testing: pytest with appropriate coverage
- Documentation: Clear README with setup instructions

## Reference Documentation:

1. [streamOS Postman Collection](https://streamft.postman.co/workspace/StreamOS-Public-Workspace~6ce4ab6b-8321-4316-b19f-af88fc467417/collection/27246749-31cec77f-3e01-4822-8ae1-6a5cf415826e?action=share&creator=27246749&active-environment=27246749-350c6dff-2487-4280-92f7-4ebc27e5c859)


2. **Rutter API**
    - [Overview](https://docs.rutter.com/rest/2024-08-31/basics#introduction)
    - [Asynchronous operations](https://docs.rutter.com/rest/2024-08-31/basics#asynchronous-operations)
    - [Invoice Create](https://docs.rutter.com/rest/2024-08-31/invoices#create-an-invoice)
    - [Invoice PDF Fetch](https://docs.rutter.com/rest/2024-08-31/invoices#fetch-a-downloadable-link-of-the-invoice)

    ```bash
    RUTTER_BASE_URL=https://production.rutterapi.com
    RUTTER_VERSION=2023-03-14
    ```

3. Email Service
Make post request to: https://dev.email.streamos.io/sendMessage/081f69a9-ab4c-4014-b50f-021d9b447f91


## Deliverables

- Working API with proper error handling
- Unit tests with good coverage
- API endpoint documentation
- Clean code following Python best practices

