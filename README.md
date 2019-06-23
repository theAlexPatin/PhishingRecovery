# Help I've been phished!

A python script to save your ass after you've been phished. It will navigate to the phishing site and repeatedly populate their page with fake username and passwords.

Ideally, they can't delineate between your real account and these fake accounts and won't get into your shit before you CHANGE YOUR PASSWORDS.

## Dependencies

- Python 3
- Chromedriver

## Installation

```
$ git clone https://github.com/theAlexPatin/PhishingRecovery.git
$ cd PhishingRecovery
$ pip install -r requirements.txt
```

## Usage

- Change `URL` to the phishing url
- Change `EMAIL_INPUT` to the name attribute of the email input field
- Change `PASSWORD_INPUT` to the name attribute of the password field
- Then run `$ python3 main.py`

![Example run-through](img/example.gif)

## Acknowledgements

I'd like to thank the dummy who got phished and had me bail him or her out.


## License

MIT License
