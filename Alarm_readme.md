
# Python Alarm Clock

This is a simple Python alarm clock script that allows you to set an alarm and play an audio file when the alarm time is reached.

## Requirements

- Python 3.x
- pygame library (install using `pip install pygame`)

## Usage

1. Make sure you have Python and pygame installed on your system.

2. Clone the repository or download the script `alarm_clock.py`.

3. Place an audio file (e.g., `audio.mp3`) in the same directory as the script. This will be the sound played when the alarm goes off.

4. Open a terminal or command prompt and navigate to the directory containing the script.

5. Run the script:

   ```sh
   python alarm_clock.py
```sh

The script will prompt you to enter the time for the alarm in the format HH:MM:SS AM/PM. For example: 08:30:00 AM.

Once the alarm time is set, the script will continuously check the current time against the alarm time. When the alarm time is reached, the script will print "Wake Up!" and play the specified audio file.

To stop the alarm, you can press Ctrl+C in the terminal where the script is running.

Example
Here's an example of how to use the Python alarm clock script:

Run the script.

Enter the alarm time when prompted: 08:00:00 AM.

Wait for the alarm to go off. When the alarm time matches the current time, the script will print "Wake Up!" and play the audio file.

Notes
Make sure the audio file (audio.mp3) is in the same directory as the script.
You can replace audio.mp3 with any other audio file you want to use as the alarm sound.
The script uses the pygame library for playing audio.
