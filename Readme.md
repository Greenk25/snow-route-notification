# Snow Route Notification System

Checks addresses from a CSV file and sends an email notification
via SendGrid only to residents affected by a street ban.

## How It Works

1. Frontend button triggers the FastAPI backend
2. Backend loads addresses from `Residents.csv`
3. Address-matching logic finds only affected addresses
4. If no match, no emails are sent
5. If match, SendGrid sends emails to those residents only
6. Backend returns JSON response, frontend displays the result

## Tech

Python, FastAPI, CSV, SendGrid, HTML / JS, JSON

## How To Run

1. Install requirements: