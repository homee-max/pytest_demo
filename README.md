# homee-auto-test

This repository is for Homee automation test, this repository cover test products including APP UI automation test, API test, AI test, and Web test. Test type including regression, smoke, and release.

### Onboarding

1. Test development training material, code review flow, and coding style please refer to the wiki:

   - To Be continue...
2. Clone repository and set library

   git clone https://github.com/homee-ai/homee-auto-test.git
   cd homee-auto-test/
   pip install -r requirements.txt
3. Architecture document and trigger method

- To Be continue...

### Code Scan Rules

In this repository, code scan through [Ruff](https://beta.ruff.rs/docs/) (An extremely fast Python linter, written in Rust), and here is our skip rules:

* [E501](https://www.flake8rules.com/rules/E501.html)：Line too long (82 > 79 characters)
* [E402](https://www.flake8rules.com/rules/E402.html)：Module level import not at top of file
* [E701](https://www.flake8rules.com/rules/E701.html)：Multiple statements on one line (colon)
* [F401](https://www.flake8rules.com/rules/F401.html)：Module imported but unused
* [F405](https://www.flake8rules.com/rules/F405.html)：Name may be undefined, or defined from star imports: module
* [F403](https://www.flake8rules.com/rules/F403.html)：‘from module import *’ used; unable to detect undefined names
