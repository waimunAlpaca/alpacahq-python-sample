# alpacahq-python-sample

A simple python project to get you started on alpaca APIs.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

alpaca-trade-api-python is a python library for the Alpaca Commission Free Trading API. Note that this package supports only **python version 3.7 and above**.

Install the latest [Python](https://www.python.org/downloads/) >= 3.7.

Install the pandas, numpy, scipy, websockets packages.

```
pip3 install pandas numpy scipy websockets
```

Install the alpaca-trade-api package.

```
pip3 install alpaca-trade-api
```

### Setup the API KEY_ID and SECRET_KEY

1. Get the API Key & Secret from [Alpaca](https://app.alpaca.markets/paper/dashboard/overview).  

2. Set the `API_KEY` & `API_SECRET` values in `sample_.py` & `websocket.py`.  

### Run the project

To run the trade service

```
python sample.py
```

To run the websocket servicey

```
python websocket.py
```

## References

In the [examples](https://github.com/alpacahq/alpaca-trade-api-python/tree/master/examples) folder there's a few algorithms that connect to the paper-trading API.
* Long-short equity strategy
* Martingale strategy

In the [websockets](https://github.com/alpacahq/alpaca-trade-api-python/tree/master/examples/websockets) folder there's examples to do the following:
* Different subscriptions(channels) usage with alpaca/polygon streams
* Pause / resume connection
* Change subscriptions of existing connection
* ws disconnections handler (make sure we reconnect)


## Built With

* Official client SDKs [alpaca-trade-api-python](https://github.com/alpacahq/alpaca-trade-api-python/) / [PyPI](https://pypi.org/project/alpaca-trade-api/)
* [alpaca Broker API](https://alpaca.markets/docs/broker/)
* [alpaca Trading API](https://alpaca.markets/docs/trading/)
* [alpaca Market Data API](https://alpaca.markets/docs/market-data/)
* [README.md](https://github.com/waimunAlpaca/README.md) - Yet another README.md template! 

## Contributing

Want to file a bug, contribute some code, or improve documentation? Excellent! Read up on our [CONTRIBUTING.md](https://github.com/angular/angular/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Wai Mun** - *Initial work* - [waimunAlpaca](https://github.com/waimunAlpaca)

## License

This project is licensed under the Apache License License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* [CONTRIBUTING.md](https://github.com/angular/angular/blob/master/CONTRIBUTING.md) - Contributing to Angular.
* [Conventional Commits](https://www.conventionalcommits.org/) - A specification for adding human and machine readable meaning to commit messages.
