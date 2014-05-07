Sublime plugin for [php.tools](https://github.com/dericofilho/php.tools)
================

### Installation

PHPTools is available via Sublime Text package manager. 

### Requirements 

- PHP
- [php.tools Requirements](https://github.com/dericofilho/php.tools)

### Settings 

```

    "debug":"True|False",
    "php_path":"/your/path/to/bin/php",
    "formatter_path":"/your/path/to/php/formatter"
    
```

**Note** In case ```php``` is not in $PATH you **MUST** declare it's path in the plugin's settings!

### Supports

At the moment it supports only [post_save_async](http://www.sublimetext.com/docs/3/api_reference.html#sublime_plugin.EventListener) to re format the code directly after save.


