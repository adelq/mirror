# mirror
An open source Linux-based Amazon Echo clone.

**Demo**: https://www.youtube.com/watch?v=oE8QCfPZixs

## Supported commands

Mirror has a modules system that allows it to plug in different modules and recognize their commands.
Currently, this includes:

* **Music**: Play music through VLC and from Grooveshark
* **Todos**: Add and list items from a todo list
* **Weather**: Get the weather at your current location

## License

Mirror is made available under the terms of the MIT License. Please see the [LICENSE](LICENSE) file for more details.

## Contributing

The best way to contribute is to clone the repository and dig in!
To add a module, create a Python module under the `modules/` directory, and add a regex to `config.py` for the trigger phrase and the function it should call when triggered.
