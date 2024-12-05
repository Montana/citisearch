Something I built in Python to track Citibike's in NYC live. Then once rendered, makes a .html of cross references, and line maps of where the bikes have gone. No API needed. 

## Usage

Make sure you have all the dependencies fulfilled, then run:

```bash
python3 citisearch.py
```
You should see a list, ascending order:

<img width="1084" alt="Screenshot 2024-12-05 at 12 26 23 PM" src="https://github.com/user-attachments/assets/beec4938-1311-4bc9-b2c8-21db78a1ca88">

To get a list of Citibikes currently checked out, if you want to then get the visual map in HTML with the cross referencing I built in (cross ref of bikes being checked out, it should look like this, run the following:

```bash
python3 citimap.py
```
You should now see an `.html` file in the root folder, click on it and it should look like this: 

![Screenshot 2024-12-05 at 12 26 13 PM](https://github.com/user-attachments/assets/49b1f037-fa6d-4b8a-a43d-e9110136aceb)

## Author
* Michael Mendy (c) 2024.
