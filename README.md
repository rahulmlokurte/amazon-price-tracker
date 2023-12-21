# :email: amazon-price-tracker :email:

The repository is used to track the price of a particular product on Amazon. It will be used to notify via an Email if the product price drops below our expected price.

## Usage

The product URL, buying price, email id are all taken from the `.env` file

```python
URL = os.getenv("URL")
email_id = os.getenv("EMAIL_ID")
password = os.getenv("APP_PASSWORD")
BUY_PRICE = os.getenv("BUY_PRICE")
```

## constraints

- Only support Gmail SMTP
- Create an APP_PASSWORD in your google account