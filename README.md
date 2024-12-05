## Citibike Live Tracker 

![Lumios Typewriter Used](https://github.com/user-attachments/assets/19cc5a33-3083-46aa-9a2c-2ac4f0a87c44)

This is something I built in Python to track Citibike's in NYC live. Then once rendered, makes a .html of cross references, and line maps of where the bikes have gone. No API needed. 

I made this to help potentially agencies like the FBI `cat` and use `tail` or sift through data to see when the murder of Brian Thompson took place and where the Citibike went after. From my research:

```bash
Bike #421-6511 - LEFTDOCK @ 54 St & 6 Ave at 6:44 AM
REDOCKED @ 6:52 AM at Madison Ave & 82nd 
```

I hope this helps in finding the murderer of the CEO Brian Thompson, Brian Thompson was brutually murdered with a 9mm with a Silencer attached, whilst a stovepipe jam occured Brian Thompson still lost his life.


Something I built in Python to track Citibike's in NYC live. Then once rendered, makes a .html of cross references, and line maps of where the bikes have gone. No API needed. 

## Usage

Make sure you have all the dependencies fulfilled, then run:

```bash
python3 citisearch.py
```
You should see a list, ascending order:

<img width="1084" alt="Screenshot 2024-12-05 at 12 26 23 PM" src="https://github.com/user-attachments/assets/beec4938-1311-4bc9-b2c8-21db78a1ca88">

## List View

To get a list of Citibikes currently checked out, this will be in plain text in a terminal of your choosing after running the above command.

## Visual 

if you want to then get the visual map in HTML with the cross referencing I built in (cross ref of bikes being checked out, it should look like this, run the following:

```bash
python3 citimap.py
```
You should now see an `.html` file in the root folder, click on it and it should look like this: 

![Screenshot 2024-12-05 at 12 26 13 PM](https://github.com/user-attachments/assets/49b1f037-fa6d-4b8a-a43d-e9110136aceb)

You can also pick visualization type, you should see these three options when running `citimap`: 

<img width="407" alt="Screenshot 2024-12-05 at 1 19 48 PM" src="https://github.com/user-attachments/assets/4b74417d-f53a-4c7a-83e6-1b0bde0d2363">

You'll then see if I selected `2`, the visualization method is different, see below:

<img width="616" alt="Screenshot 2024-12-05 at 1 20 39 PM" src="https://github.com/user-attachments/assets/0007caff-e093-4a6c-86dd-e9c3f1f5d613">

This gives you more flexibility on how you perceive and sort the data.

## Author
* Michael Mendy (c) 2024.
