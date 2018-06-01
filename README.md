English | [简体中文](/README-zh_cn.md)

# MutualAdmire

[![Python 3.5][Python3.5_badge]][Python]
[![License: GPL v3][GPLV3_badge]][GPLV3]

<div align="center">
    <img src="https://raw.githubusercontent.com/HurryPeng/MutualAdmire/master/images/Admire.png" height="100">
</div>

A WeChat auto-reply robot based on [ItChat][Itchat]

## Origin

It can be a very embarrasing experience when someone always uses "![Admire][Admire_small]" to reply to you on WeChat, especially when s/he is more experienced than you in some ways. The only best way to reply is by sending the same emoji back, though it sometimes ends the conversation instantly. 

## Features

The robot counts how many "![Admire][Admire_small]"(s) you receive in a text message and replies with the same number of "![Admire][Admire_small]"(s) within one text message, as is shown below. 

![Chatting with Kristine][KristineScreenshot]

## Dependencies

- [ItChat][ItChat]

## Usage

Download MutualAdmire.py and run it on any device with Python3. It should be always running in order to work properly. Please be notified that [ItChat][ItChat] is based on Web WeChat and thus has conflicts with WeChat for PC. 

## Thanks for Open Source

- [ItChat][ItChat]: A complete and graceful API for Wechat

## Acknowledgements

- Kristine Jiang, whose endless "![Admire][Admire_small]"s inspired me to develop this project
- Sandra Zhou, who received mountains of test messages from me

## License

    Copyright (C) 2018  Haoran "Hurry" Peng

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

[Admire]: https://raw.githubusercontent.com/HurryPeng/MutualAdmire/master/images/Admire.png
[Admire_small]: https://raw.githubusercontent.com/HurryPeng/MutualAdmire/master/images/Admire-20x20.png
[ItChat]: https://github.com/littlecodersh/ItChat
[Python3.5_badge]: https://img.shields.io/badge/python-3.5-red.svg
[Python]: https://www.python.org
[GPLV3_badge]: https://img.shields.io/badge/License-GPL%20v3-blue.svg
[GPLV3]: https://www.gnu.org/licenses/gpl-3.0
[KristineScreenshot]: https://raw.githubusercontent.com/HurryPeng/MutualAdmire/master/images/Kristine.png
