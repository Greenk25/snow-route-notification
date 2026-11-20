# Snow Route Notification System
Checks addresses from a CSV file and sends an email notification via SendGrid only to residents affected by a street ban.

## Why I Built This
This came from a real situation on Sherbrook Street. During a Snow Route Ban, people can get ticketed or towed.
But not everyone is home to see the notice — people might be away, at work, or dealing with other problems.
I built this to notify affected residents by email, so they have time to move their car. Resident emails and addresses are available in the residential street parking permit owners database.

## How It Works
1. Frontend button triggers the FastAPI backend
2. Backend loads addresses from `Residents.csv`
3. Address-matching logic finds only affected addresses
4. If no match, no emails are sent
5. If a match, SendGrid sends emails to those residents only
6. Backend returns JSON response, frontend displays the result

## Tech
Python, FastAPI, CSV, SendGrid, HTML / JS, JSON
