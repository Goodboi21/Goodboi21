#!/usr/bin/env python
# coding: utf-8

# In[4]:


teams = [
    {
        "name": "Chennai Super Kings",
        "short": "CSK",
        "purse": 55.0,
        "retained": [
            {"name": "Ruturaj Gaikwad", "price": 18.0, "type": "capped"},
            {"name": "Matheesha Pathirana", "price": 13.0, "type": "foreigner"},
            {"name": "Shivam Dube", "price": 12.0, "type": "capped"},
            {"name": "Ravindra Jadeja", "price": 18.0, "type": "capped"},
            {"name": "MS Dhoni", "price": 4.0, "type": "uncapped"},
        ],
        "rtm": {"capped": 1, "uncapped": 0},
    },
    {
        "name": "Delhi Capitals",
        "short": "DC",
        "purse": 73.0,
        "retained": [
            {"name": "Axar Patel", "price": 16.5, "type": "capped"},
            {"name": "Kuldeep Yadav", "price": 13.25, "type": "capped"},
            {"name": "Tristan Stubbs", "price": 10.0, "type": "foreigner"},
            {"name": "Abishek Porel", "price": 4.0, "type": "uncapped"},
        ],
        "rtm": {"capped": 2, "uncapped": 0},
    },
    {
        "name": "Gujarat Titans",
        "short": "GT",
        "purse": 69.0,
        "retained": [
            {"name": "Rashid Khan", "price": 18.0, "type": "foreigner"},
            {"name": "Shubman Gill", "price": 16.5, "type": "capped"},
            {"name": "B Sai Sudharshan", "price": 8.5, "type": "capped"},
            {"name": "Rahul Tewatia", "price": 4.0, "type": "uncapped"},
            {"name": "Shahrukh Khan", "price": 4.0, "type": "uncapped"},
        ],
        "rtm": {"capped": 1, "uncapped": 0},
    },
    {
        "name": "Lucknow Super Giants",
        "short": "LSG",
        "purse": 69.0,
        "retained": [
            {"name": "Nicholas Pooran", "price": 21.0, "type": "foreigner"},
            {"name": "Ravi Bishnoi", "price": 11.0, "type": "capped"},
            {"name": "Mayank Yadav", "price": 11.0, "type": "capped"},
            {"name": "Mohsin Khan", "price": 4.0, "type": "uncapped"},
            {"name": "Ayush Badoni", "price": 4.0, "type": "uncapped"},
        ],
        "rtm": {"capped": 1, "uncapped": 0},
    },
    {
        "name": "Kolkata Knight Riders",
        "short": "KKR",
        "purse": 51.0,
        "retained": [
            {"name": "Rinku Singh", "price": 13.0, "type": "capped"},
            {"name": "Varun Chakravarthy", "price": 12.0, "type": "capped"},
            {"name": "Sunil Narine", "price": 12.0, "type": "foreigner"},
            {"name": "Andre Russell", "price": 12.0, "type": "foreigner"},
            {"name": "Harshit Rana", "price": 4.0, "type": "uncapped"},
            {"name": "Ramandeep Singh", "price": 4.0, "type": "uncapped"},
        ],
        "rtm": {"capped": 0, "uncapped": 0},
    },
    {
        "name": "Mumbai Indians",
        "short": "MI",
        "purse": 45.0,
        "retained": [
            {"name": "Jasprit Bumrah", "price": 18.0, "type": "capped"},
            {"name": "Suryakumar Yadav", "price": 16.35, "type": "capped"},
            {"name": "Hardik Pandya", "price": 16.35, "type": "capped"},
            {"name": "Rohit Sharma", "price": 16.3, "type": "capped"},
            {"name": "Tilak Varma", "price": 8.0, "type": "capped"},
        ],
        "rtm": {"capped": 0, "uncapped": 1},
    },
    {
        "name": "Punjab Kings",
        "short": "PBKS",
        "purse": 110.5,
        "retained": [
            {"name": "Shashank Singh", "price": 5.5, "type": "uncapped"},
            {"name": "Prabhsimran Singh", "price": 4.0, "type": "uncapped"},
        ],
        "rtm": {"capped": 4, "uncapped": 0},
    },
    {
        "name": "Rajasthan Royals",
        "short": "RR",
        "purse": 41.0,
        "retained": [
            {"name": "Sanju Samson", "price": 18.0, "type": "capped"},
            {"name": "Yashasvi Jaiswal", "price": 18.0, "type": "capped"},
            {"name": "Riyan Parag", "price": 14.0, "type": "capped"},
            {"name": "Dhruv Jurel", "price": 14.0, "type": "capped"},
            {"name": "Shimron Hetmyer", "price": 11.0, "type": "foreigner"},
            {"name": "Sandeep Sharma", "price": 4.0, "type": "uncapped"},
        ],
        "rtm": {"capped": 0, "uncapped": 0},
    },
    {
        "name": "Royal Challengers Bengaluru",
        "short": "RCB",
        "purse": 83.0,
        "retained": [
            {"name": "Virat Kohli", "price": 21.0, "type": "capped"},
            {"name": "Rajat Patidar", "price": 11.0, "type": "capped"},
            {"name": "Yash Dayal", "price": 5.0, "type": "uncapped"},
        ],
        "rtm": {"capped": 3, "uncapped": 0},
    },
    {
        "name": "Sunrisers Hyderabad",
        "short": "SRH",
        "purse": 45.0,
        "retained": [
            {"name": "Pat Cummins", "price": 18.0, "type": "foreigner"},
            {"name": "Abhishek Sharma", "price": 14.0, "type": "capped"},
            {"name": "Nitish Kumar Reddy", "price": 6.0, "type": "capped"},
            {"name": "Heinrich Klaasen", "price": 23.0, "type": "foreigner"},
            {"name": "Travis Head", "price": 14.0, "type": "foreigner"},
        ],
        "rtm": {"capped": 0, "uncapped": 1},
    },
]


# In[ ]:




