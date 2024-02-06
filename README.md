# Email-AutoSend

## Overview
Email-AutoSend is a Python program designed to streamline the process of sending emails to recipients listed in a CSV or text file. With this tool, users can easily provide a structured message and have it sent to multiple recipients without the hassle of manual input.

## Features
- Read recipient email addresses from a CSV or text file.
- Customizable email structure, allowing users to provide their own message template.
- Support for sending emails through SMTP (Simple Mail Transfer Protocol).
- Easy-to-use command-line interface.

## Installation
1. Clone this repository to your local machine:
<br> git clone https://github.com/Dominion083/Email-AutoSend.git

2. Open the Project in your chosen IDE. You will need to have Pyhton installed on your machine.



## Usage
1. Prepare your CSV or text file(Email.csv) containing recipient email addresses. Ensure that each email address is listed on a separate line on the first column.
2. Run the program(Email.py) from the command line
3. A GUI Application would come up that allows you select the CSV File you want to use and input the common subject and body of the mail.
4. Click on send and your mail is on its way !!


## Configuration
You can configure your SMTP server details directly in the `Email.py` file. Also, you would need to set up 2FA for the sender email address. You would also need to grant access to less secure apps.

## Dependencies
- `smtplib`: For sending emails using SMTP.
- `csv`: For reading CSV files.
- `email`: For composing and sending emails.


## License
This project is licensed under the Apache - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Inspired by the need to automate email sending tasks.
- Thanks to the developers of Python and its libraries used in this project.

## Contributors
- [Dominion Aromolaran](https://github.com/Dominion083)

## Future Plans
In future updates, we plan to add the ability to attach files and images to the emails, further enhancing the functionality and usability of Email-AutoSend.