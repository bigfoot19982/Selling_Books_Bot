# Selling_Books_Bot


![Version](https://img.shields.io/pypi/v/aiogram?style=plastic)
![License](https://img.shields.io/pypi/l/aiogram?style=plastic)
![License](https://img.shields.io/pypi/l/asyncpg?style=plastic)
![Size](https://img.shields.io/github/repo-size/bigfoot19982/Selling_Books_Bot?style=plastic)
![last_commit](https://img.shields.io/github/last-commit/bigfoot19982/Selling_Books_Bot?style=plastic)

## Description

***Say, you have a bunch of items you need no more and you want to sell it all out.  
That's where you're going to have to use this telegram bot.  
It provides you with the opportunity to easily sell your stuff   
as well as the client with the opportunity to easily purchase it.***

***This particular telegram bot is is written to sell some of my books.***

<img src="https://sun9-87.userapi.com/impg/4JCpQBV8XNi617GwZUtTMls_t-cFwIi3g38TGg/BNwBr8PMAQc.jpg?size=1600x1364&quality=96&sign=0c642da53f6124b1fb9ddc7a3e7aa3de&type=album" width="400">

## How does it work exactly?
___________
### Initial data

In "data" folder there are three files named "arab", "history", and "the_world" representing three areas, which the books are dedicated to.
Each of the files comprises several books represented as instances of class Item. 
The description of each book is inserted into Postgresql DB table "books" as well.

<img src="https://sun9-25.userapi.com/impg/banjnt0SRUxQiXsA237h9KOy7Gowib-hwOmNQA/yMjbmn3GyUQ.jpg?size=1566x917&quality=96&sign=4062cc57e9285d099e0411aa98247821&type=album" width="700">

### The Beginning

On "/start" command the bot suggests a client three buttons epitomizing the areas where the latter may pick up a book from.

<img src="https://sun9-21.userapi.com/impg/XoaeTAJ_rcAcLtDzW74e2XXTIgzbD97qn8YcAg/JDP7j8Z9WQs.jpg?size=498x1080&quality=96&sign=2737a8339e094a14fb6ce05c74ec2211&type=album" width="250">

### The Choosing

After pressing "Area button" the client receives a number of books on the topic and chooses one.  
The client receives only the books that are not sold out at this point,  
i.e. the bot requests the DB whether "units_in_stock" for this particular item are more than zero.  
In case of having no books on the topic the bot asks the client to choose a book from another area.

First case | Second case
:----------:|:------------:
<img src="https://sun9-82.userapi.com/impg/r1cKdYEOMkEEJO7LPfXtnbmXjqmQPzOsFquU-Q/47Eqim0o7JM.jpg?size=498x1080&quality=96&sign=d18d490247f202ae55572006765b1114&type=album" width="250"> | <img src="https://sun9-9.userapi.com/impg/79YH-8gsJUAyyHanWpHa39uFHIQ3iYzBdGTEoQ/KvdpwyvfoqM.jpg?size=498x1080&quality=96&sign=cfba00b0bb78be761d6a9891e4eb7b5e&type=album" width="250">

### The Payment

Right after filling out the address and choosing the shipping option the client carries out the payment through embedded Tranzzo payment solution and gets a receipt.

Address | Shipping_opt | Payment
:------:|:------------:|:-------:
<img src="https://sun9-24.userapi.com/impg/_DyciVPy-ToXUzJ8Nz25rZSqOuP9AhAfiQ2zrw/D7orMATdRA8.jpg?size=738x1600&quality=96&sign=5fcd7c9083b2231119cf9151c57eb731&type=album" width="250"> | <img src="https://sun9-1.userapi.com/impg/OQTe_MJxKcV6BelIfXV_nYWUZxZU7eM62LgxEQ/2599vZ0o-no.jpg?size=738x1600&quality=96&sign=e650bb05f54f6f6a5d48903eb42f766f&type=album" width="250"> | <img src="https://sun9-42.userapi.com/impg/CoY_deRpE6bd9K2dKrR6kuLuD2KRKUfZVW7x3w/AUgR_YQc9S8.jpg?size=498x1080&quality=96&sign=3d6fa364fc7779cc87d5d43e5c410710&type=album" width="250"> 

### The Notification

As soon as the payment from the client is received, the owners of the bot are notified of the details of the new order in a special message.
Simultaneously, the order is inserted into table "orders" within Postgresql DB.

In Telegram | In Postgresql
:----------:|:------------:
<img src="https://sun9-78.userapi.com/impg/osNrzizU0MeMdlKq7TZ7YmeuQI383gv9vHnj-g/zsAVWAbpOoY.jpg?size=498x1080&quality=96&sign=5155f4f5580689862b9cc8a4b4d9a09a&type=album" width="250"> | <img src="https://sun9-66.userapi.com/impg/LBoH7guJbocJqAaQM3iujMmFiZWIXknChrZOkA/rD5Uq7d94ek.jpg?size=1280x495&quality=96&sign=cd90a1776a93b0eb3149ee3e56876097&type=album" width="700">

### The Implementation

When a bot owner implements the order, he or she merely replies to this special message by the word "Исполнено".
After that the DB considers the order implemented (by marking the column "done" as "True").

In Telegram | In Postgresql
:----------:|:------------:
<img src="https://sun9-24.userapi.com/impg/4m1oKlYl__Hungxac0jfdD7ukaWj2Duxkv-EOw/X2nVD2QMxpQ.jpg?size=498x1080&quality=96&sign=91e8f6698fc6a82aff22c6517c8398eb&type=album" width="250"> | <img src="https://sun9-60.userapi.com/impg/Cido3s1g_jl6puSFY1SgEvLOKx7qLcNaTMYPIQ/9PlY8JwH6k8.jpg?size=1280x586&quality=96&sign=5ab4fe3cdd6f70d83d709d48e813a72c&type=album" width="700">

### The prompt

The bot owner may forget how many orders he is to attend to.
Not to look it up into the DB he or she can simply ask the bot "Сколько невыполненных заказов?".
In response to that, the bot will send the number of orders to carry out.

<img src="https://sun9-35.userapi.com/impg/ss8-Yk6C_sYQu9Uqmq8Blea42RocTMFOG9iSQQ/X96TLMIiu58.jpg?size=498x1080&quality=96&sign=78f9b3a793d5180d3c0f7185febbd74a&type=album" width="250">
