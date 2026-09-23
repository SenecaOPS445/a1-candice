#!/usr/bin/env python3

# Import the subprocess module
import subprocess

# Run test1.py and test the output using assert
def test_a1():

    # Run the script
    p = subprocess.Popen(['python3', 'a1.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Provide the input
    p.stdin.write(b"Candice\n")
    p.stdin.flush()
    p.stdin.write(b"1\n")
    p.stdin.flush()
    p.stdin.write(b"y\n")
    p.stdin.flush()

    # Read the output
    output = p.stdout.read().decode()

    # Check the output using assert
    assert "Candice" in output
    assert "Sir" or "Lady" or "Lord" or "Dame" or "Master" or "Mistress" or "King" or "Queen" or "Prince" or "Princess" in output
    assert "Mordor" or "Rivendell" or "The Shire" or "Gondor" or "Isengard" or "Lothlorien" or "Rohan" or "Minas Tirith" or "Hobbiton" in output

    # Close the process
    p.stdin.close()
    p.stdout.close()
    p.stderr.close()

# Run the test
test_a1()