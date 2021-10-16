# Selling_Books_Bot


![Version](https://img.shields.io/pypi/v/aiogram?style=plastic)
![License](https://img.shields.io/pypi/l/aiogram?style=plastic)
![License](https://img.shields.io/pypi/l/asyncpg?style=plastic)
![Size](https://img.shields.io/github/repo-size/bigfoot19982/Selling_Books_Bot)
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
i.e. the bot requests the DB whether units_in_stock for this particular item are more than zero.  
In case of having no books on the topic the bot asks the client to choose a book from another area.

<img src="https://sun9-82.userapi.com/impg/r1cKdYEOMkEEJO7LPfXtnbmXjqmQPzOsFquU-Q/47Eqim0o7JM.jpg?size=498x1080&quality=96&sign=d18d490247f202ae55572006765b1114&type=album" width="250">

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
<img src="https://sun9-53.userapi.com/impg/uYGx_AWSpeSdBfavEdnPGLOQJccQmafHK6FkLQ/DWjsOXc_giI.jpg?size=498x1080&quality=96&sign=d4327161fb2ef58fd990822f822b1b56&type=album" width="250"> | <img src="https://sun9-47.userapi.com/impg/iC4ruJwI2Ab8kY0gpYfxN8VUtxt9AL3F_BDHuQ/jM7vYbkQ1r8.jpg?size=1280x524&quality=96&sign=6583c216cf4c38af9dc35f5e0e262205&type=album" width="700">

### The Implementation

When a bot owner implements the order, he or she merely replies to this special message by the word "Исполнено".
After that the DB considers the order implemented (by marking the column "done" as "True").

In Telegram | In Postgresql
:----------:|:------------:
<img src="https://sun9-18.userapi.com/impg/YPEC8ymysYEQK-sbWR2Tf0C5hm2ZEjGFOMQiRA/gZVfk645BEE.jpg?size=498x1080&quality=96&sign=39d431d19b980b23799d2ba1041187a6&type=album" width="250"> | <img src="https://sun9-5.userapi.com/impg/_xEvfDaQooi6RuOfcSNKp8l8Ogob1mZzMl0Vqg/C6XaxmIai8w.jpg?size=1598x691&quality=96&sign=fe73627629bb74773e6315927717f519&type=album" width="700">

### The prompt

The bot owner may forget how many orders he is to attend to.
Not to look it up into the DB he or she can simply ask the bot "Сколько невыполненных заказов?".
In response to that, the bot will send the number of orders to carry out.

<img src="https://sun9-63.userapi.com/impg/D46Z0gO6hKnFOTrvXW63UEhedEIx8UZ9AJ22gw/uvoyOlSpg2E.jpg?size=498x1080&quality=96&sign=7983225211e414f919545e75dbf2d857&type=album" width="250">
