# Parking Pulse - Spartahack 9 Project

## Team Members
- Balaji Ganeshbabu
- Lance Moy
- Sangwoon Jeong
- Vivek Revankar

## Project Description
The primary goal of this project is to detect a specific license plate and send out a email notification when detected.

## Getting Started

### Prerequisites
- Python installed on your system
- OpenCV

### Installation
1. Download the `parkingpulse.py` file from the repository.
```bash
python3 parkingpulse.py
```

## Usage

1. Open the `parkingpulse.py` file in your preferred text editor.
3. Add your email credentials to the file. (2FA must be turned on in order to generate the app password)
```python
s.login("Sender Email", "App Password")
```
```python
s.sendmail("Sender Email", "Reciever Email", msg.as_string())
```
4. Save the changes to the file.

## Running the Code

To run the Parking Pulse code:

```bash
python parkingpulse.py
