#. This script is quite ugly but does the job :) 
#. If you update the variables inside the hashed box and then run it, it will update the website files
#. needed for each new meeting. 
#. You then need to commit and pull request the meeting update to the website. 

import datetime

from meeting_info import *
from pathlib import Path



if __name__ == "__main__":

    NEXT_MEETING = Path('templates/meeting.txt').read_text()
    EMAIL_ONEWEEK = Path('templates/email_oneweek.txt').read_text()
    EMAIL_TODAY = Path('templates/email_today.txt').read_text()
    HACKMD = Path('templates/hackmd.txt').read_text()

    # Turn the date into a Python date object
    date_obj = datetime.datetime.strptime(DATE, format1)
    # Turn the time into a Python time object
    time_obj = datetime.datetime.strptime(TIME, format1).strftime(format2)

    def create_timeanddate():
        """The timeanddate.com URL is produced from the URL parameters. So instead of manually using the form
        we can just change the URL parameters using the data provided."""

        url_base = "https://www.timeanddate.com/worldclock/fixedtime.html?msg=Data+Ethics+Club&iso="
        url_end = "T13&p1=299&ah=1"

        time.strftime(format2)

        return full_url

    def fill_template():

        template = read the templates
        filled_template =

        return filled_template


    def write_meeting_file():


    def update_next_meeting():