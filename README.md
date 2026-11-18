# EX01 Developing a Simple Webserver

# Date: 18-11-2026
# AIM:
To develop a simple webserver to serve html pages and display the configuration details of laptop.

# DESIGN STEPS:
## Step 1:
HTML content creation.

## Step 2:
Design of webserver workflow.

## Step 3:
Implementation using Python code.

## Step 4:
Serving the HTML pages.

## Step 5:
Testing the webserver.

# PROGRAM:
<!DOCTYPE html>
<html>
<head>
    <title>Computer Network Applications</title>
</head>
<body>

<h2>Computer Network Applications</h2>

<table border="1" cellpadding="8">
    <tr>
        <th>Application Name</th>
        <th>Network Protocol</th>
        <th>Description</th>
    </tr>

    <tr>
        <td>World Wide Web (HTTP/HTTPS)</td>
        <td>HTTP / TCP</td>
        <td>Browsing websites and web pages across the internet.</td>
    </tr>

    <tr>
        <td>Email (SMTP / IMAP)</td>
        <td>SMTP, POP3, IMAP</td>
        <td>Sending, receiving, and managing electronic mail.</td>
    </tr>

    <tr>
        <td>File Transfer Protocol (FTP)</td>
        <td>FTP / TCP</td>
        <td>Transferring files between a client and a server.</td>
    </tr>

    <tr>
        <td>Domain Name System (DNS)</td>
        <td>DNS / UDP, TCP</td>
        <td>Translating human-readable domain names into IP addresses.</td>
    </tr>

    <tr>
        <td>Remote Desktop (RDP / SSH)</td>
        <td>RDP, SSH / TCP</td>
        <td>Accessing and controlling a computer or server remotely.</td>
    </tr>

    <tr>
        <td>VoIP / Video Conferencing</td>
        <td>RTP, SIP / UDP</td>
        <td>Real-time voice and video communication over the network.</td>
    </tr>

</table>

</body>
</html>
import http.server
import socketserver

PORT = 8080

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        super().do_GET()

with socketserver.TCPServer(("", PORT), Handler) as server:
    print("This is my webserver")
    server.serve_forever()
# OUTPUT:
<img width="1607" height="886" alt="output png" src="https://github.com/user-attachments/assets/f6163b60-2b6a-413f-b78b-add2ffdd626d" />
<img width="1062" height="387" alt="Screenshot 2026-11-18 114735" src="https://github.com/user-attachments/assets/d8e4bb62-fb71-4fac-8d18-f062fe374d7d" />

# RESULT:
The program for implementing simple webserver is executed successfully.
