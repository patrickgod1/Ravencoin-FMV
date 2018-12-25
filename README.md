# Ravencoin-FMV

This Python applicaton takes the transactions export file from the official Ravencoin wallet, and use the historical closing price (USD) from (https://coinmarketcap.com/currencies/ravencoin/historical-data/) to calculate the captial asset in US dollars. A possible use case is for estimate the fair market value at the time a coin is purchased or mined.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development.

On top of having Python 3.6+ installed, you'll need a few Python modules as well. To install:

```
pip3 install -r requirements.txt
```

### Compiling using PyInstaller

The project files includes a batch file (Windows platform only) with commands to run to compile into an executable. 

Other development platforms can run the following command in Terminal:

```
pyinstaller RavencoinFMV.spec .\RavencoinFMV.py
```
You may need to modify the file paths, if not in same current working directory.


### Screenshot

![ravencoinfmv](https://user-images.githubusercontent.com/41496510/50427361-b51a7680-085a-11e9-968c-1a0dbeedfd04.png)

<!---
## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system
--->

## Built With

* [Python 3.6](https://docs.python.org/3/) - The scripting language used.
* [Pandas](https://pandas.pydata.org/) - Data structure/anaylsis tool used.
* [PtQt5](https://pypi.org/project/PyQt5/) - Used to create GUI.
* [PyInstaller](https://www.pyinstaller.org/) - Used to create executable for release.

<!---
## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).
--->

## Authors
* **Patrick Yu** - *Initial work* - [patrickgod1](https://github.com/patrickgod1)
<!---
* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
--->

