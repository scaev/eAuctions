# eAuctions

### Welcome to eAuctions! 🗓

This is a web application for online auctions, built with Django. Users can create accounts, post an auction, bid on items, and view the bidding history for each item.

## Features

- User authentication and registration
- Create, view, and edit auctions
- Create, view, and bid on auctions
- Automatic closing of auctions when the end time is reached
- Display of the highest bid and remaining time for each auction
- View of bidding history for each auction

## Meet the Developers! 🤝

### 🧑‍💻 Gautham Battineni

### 🧑‍💻 Kaan Karadag

### 🧑‍💻 Kelvin Chan

## Meet the Design Team! 🤝

### 👩‍💻 Catie Camer

### 👩‍💻 Kateryna Bielotserkovska

## Installation

To run this application, you'll need to have Python 3 and Django installed on your system. You can install Django using pip:
pip install django
Once you have Django installed, you can clone this repository and navigate to the root directory:
git clone https://github.com/scaev/eAuctions.git
cd eAuctions
You'll need to apply the migrations to create the database tables:
python manage.py migrate
You can then start the development server:
python manage.py runserver
The application will be accessible at http://localhost:8000/ in your web browser.

## Usage

To use the application, you'll need to create an account. You can do this by clicking the "Sign Up" link on the home page and filling out the registration form.

Once you're logged in, you can create a new auction by clicking the "Sell" link on the home page. You'll need to provide a title, description, starting price, and end time for the auction.

Other users can then bid on your auction by entering a higher price on the auction page. The highest bid will be displayed on the auction page, and the auction will automatically close when the end time is reached.

## Wireframing & Concept 📝

![wireframe](https://i.imgur.com/ISFpMoe.png)
![wireframe](https://i.imgur.com/d3tneyT.png)

Prior to project start, wireframing was completed by design team to show ideal project design and flow. The above screenshot details a basic design concept prior to beginning the project.

![ERD](https://i.imgur.com/l13efHE.png)

Project planning materials are held in [this](https://trello.com/b/N6PWQ1w3/project-3-reauction) public Trello board.

Project wireframe and design materials are held in [this](https://app.zeplin.io/project/63e5457f2c2969191b237a65) public Zeplin board.

## Technologies Used 💻

![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Express.js](https://img.shields.io/badge/express.js-%23404d59.svg?style=for-the-badge&logo=express&logoColor=%2361DAFB)
![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![NPM](https://img.shields.io/badge/NPM-%23000000.svg?style=for-the-badge&logo=npm&logoColor=white)
![Azure](https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=microsoftazure&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Trello](https://img.shields.io/badge/Trello-%23026AA7.svg?style=for-the-badge&logo=Trello&logoColor=white)

## Contributing 🙏

If you'd like to contribute to this project, please fork the repository and create a new branch for your changes. Once you've made your changes, submit a pull request to merge your branch back into the main repository.

## Icebox Features 🧊

- Add items to watchlist without having to bid
- Have categories for the products being auctioned - preferably dropdown menu
- Display a message to the winner of a bid and to the seller when the bid closes successfully
- Adding calendar template for sell view

## Acknowledgments

This project was created as a learning exercise based on the Django lesson within a period of 10 days. Special thanks to the Design team and David Bland for helping us learn and create this project.
